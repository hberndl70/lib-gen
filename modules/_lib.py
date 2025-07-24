"""
Library XML generation module for edX libraries.

This module handles the creation of library.xml files that serve as the main
inventory file for edX libraries, containing metadata and references to all
library components.
"""

import logging
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass
from lxml import etree
from lxml.builder import E

from . import _con
from . import _iof

logger = logging.getLogger(__name__)


class LibraryXMLError(Exception):
    """Custom exception for library XML generation errors."""
    pass


@dataclass
class LibraryMetadata:
    """Metadata for an edX library."""
    display_name: str
    library: str
    org: str
    url_name: str = _con.LIBRARY_URL_NAME
    xblock_family: str = _con.XBLOCK_FAMILY

    def __post_init__(self):
        """Validate metadata after initialization."""
        if not self.display_name.strip():
            raise ValueError("Display name cannot be empty")
        if not self.library.strip():
            raise ValueError("Library name cannot be empty")
        if not self.org.strip():
            raise ValueError("Organization cannot be empty")


@dataclass
class ProblemReference:
    """Reference to a problem within the library."""
    url_name: str

    def __post_init__(self):
        """Validate problem reference after initialization."""
        if not self.url_name.strip():
            raise ValueError("Problem URL name cannot be empty")


class LibraryXMLGenerator:
    """Generates library.xml files for edX libraries."""

    def __init__(self, working_directory: Optional[Union[str, Path]] = None):
        """
        Initialize the library XML generator.

        Args:
            working_directory: Working directory path (uses current if None)
        """
        self.working_dir = Path(working_directory) if working_directory else Path.cwd()

    def generate_library_xml(self, metadata: LibraryMetadata,
                            problem_references: List[ProblemReference]) -> etree._Element:
        """
        Generate the library XML element structure.

        Args:
            metadata: Library metadata
            problem_references: List of problem references

        Returns:
            XML element for the library

        Raises:
            LibraryXMLError: If generation fails
        """
        try:
            # Create the main library element
            library_element = self._create_library_element(metadata)

            # Add problem references
            for problem_ref in problem_references:
                problem_element = self._create_problem_element(problem_ref)
                library_element.append(problem_element)

            logger.info(f"Generated library XML with {len(problem_references)} problems")
            return library_element

        except Exception as e:
            raise LibraryXMLError(f"Failed to generate library XML: {e}")

    def write_library_xml_file(self, metadata: LibraryMetadata,
                              problem_references: List[ProblemReference],
                              output_path: Optional[Union[str, Path]] = None) -> Path:
        """
        Generate and write library XML to file.

        Args:
            metadata: Library metadata
            problem_references: List of problem references
            output_path: Output file path (uses default if None)

        Returns:
            Path to the written file

        Raises:
            LibraryXMLError: If writing fails
        """
        try:
            # Generate the XML structure
            library_element = self.generate_library_xml(metadata, problem_references)

            # Determine output path
            if output_path is None:
                output_path = (self.working_dir / _con.LIBRARY_FOLDER /
                             _con.LIBRARY_XML_FILENAME)
            else:
                output_path = Path(output_path)

            # Convert to bytes with pretty printing
            xml_bytes = etree.tostring(library_element, pretty_print=True, encoding='utf-8')

            # Write to file
            _iof.FileWriter.write_binary_file(xml_bytes, output_path)

            logger.info(f"Successfully wrote library XML to: {output_path}")
            return output_path

        except Exception as e:
            raise LibraryXMLError(f"Failed to write library XML file: {e}")

    def _create_library_element(self, metadata: LibraryMetadata) -> etree._Element:
        """
        Create the main library XML element with attributes.

        Args:
            metadata: Library metadata

        Returns:
            Library XML element
        """
        return E.library(
            **{
                'url_name': metadata.url_name,
                'xblock-family': metadata.xblock_family,
                'display_name': metadata.display_name,
                'org': metadata.org,
                'library': metadata.library
            }
        )

    def _create_problem_element(self, problem_ref: ProblemReference) -> etree._Element:
        """
        Create a problem reference element.

        Args:
            problem_ref: Problem reference

        Returns:
            Problem XML element
        """
        return E.problem(url_name=problem_ref.url_name)


class ConfigurationLoader:
    """Loads configuration data for library generation."""

    @staticmethod
    def load_from_config_file(config_file_path: Union[str, Path]) -> LibraryMetadata:
        """
        Load library metadata from configuration file.

        Args:
            config_file_path: Path to configuration JSON file

        Returns:
            LibraryMetadata object

        Raises:
            LibraryXMLError: If loading or parsing fails
        """
        try:
            config_data = _iof.FileReader.read_json(config_file_path)

            # Extract required fields
            display_name = config_data.get("DISPLAY_NAME")
            library = config_data.get("LIBRARY")
            org = config_data.get("ORG")

            # Validate required fields
            missing_fields = []
            if not display_name:
                missing_fields.append("DISPLAY_NAME")
            if not library:
                missing_fields.append("LIBRARY")
            if not org:
                missing_fields.append("ORG")

            if missing_fields:
                raise LibraryXMLError(f"Missing required configuration fields: {missing_fields}")

            return LibraryMetadata(
                display_name=display_name,
                library=library,
                org=org
            )

        except Exception as e:
            if isinstance(e, LibraryXMLError):
                raise
            raise LibraryXMLError(f"Failed to load configuration from {config_file_path}: {e}")


class ProblemReferenceGenerator:
    """Generates problem references for the library."""

    @staticmethod
    def generate_problem_references(problem_count: int) -> List[ProblemReference]:
        """
        Generate problem references for a given number of problems.

        Args:
            problem_count: Number of problems to generate references for

        Returns:
            List of ProblemReference objects

        Raises:
            LibraryXMLError: If generation fails
        """
        if problem_count < 1:
            raise LibraryXMLError("Problem count must be at least 1")

        try:
            references = []
            for i in range(1, problem_count + 1):
                filename = _iof.FilenameGenerator.create_32char_filename(
                    _con.CBP_FILENAME_TEMPLATE, str(i)
                )
                references.append(ProblemReference(url_name=filename))

            logger.info(f"Generated {len(references)} problem references")
            return references

        except Exception as e:
            raise LibraryXMLError(f"Failed to generate problem references: {e}")


class LibraryXMLService:
    """High-level service for library XML operations."""

    def __init__(self, working_directory: Optional[Union[str, Path]] = None):
        """
        Initialize the service.

        Args:
            working_directory: Working directory path (uses current if None)
        """
        self.working_dir = Path(working_directory) if working_directory else Path.cwd()
        self.generator = LibraryXMLGenerator(self.working_dir)

    def create_library_from_config(self, problem_count: int,
                                  config_file_path: Optional[Union[str, Path]] = None) -> Path:
        """
        Create library XML from configuration file and problem count.

        Args:
            problem_count: Number of problems in the library
            config_file_path: Path to config file (uses default if None)

        Returns:
            Path to the created library XML file

        Raises:
            LibraryXMLError: If creation fails
        """
        try:
            # Determine config file path
            if config_file_path is None:
                config_file_path = (self.working_dir / _con.INPUT_FOLDER /
                                  _con.CONFIG_FILENAME)

            # Load metadata from config
            metadata = ConfigurationLoader.load_from_config_file(config_file_path)

            # Generate problem references
            problem_references = ProblemReferenceGenerator.generate_problem_references(problem_count)

            # Generate and write the library XML
            output_path = self.generator.write_library_xml_file(metadata, problem_references)

            logger.info(f"Successfully created library XML for {problem_count} problems")
            return output_path

        except Exception as e:
            if isinstance(e, LibraryXMLError):
                raise
            raise LibraryXMLError(f"Failed to create library from config: {e}")


# =============================================================================
# Legacy Functions (maintaining backward compatibility)
# =============================================================================

def Write_LIB_XML(problem_count: int) -> None:
    """
    Write library XML file (legacy function).

    Args:
        problem_count: Number of problems in the library

    Raises:
        LibraryXMLError: If writing fails
    """
    try:
        service = LibraryXMLService()
        service.create_library_from_config(problem_count)
        logger.info("Legacy Write_LIB_XML completed successfully")
    except Exception as e:
        raise LibraryXMLError(f"Legacy Write_LIB_XML failed: {e}")


# =============================================================================
# Utility Functions
# =============================================================================

def validate_library_xml(xml_file_path: Union[str, Path]) -> bool:
    """
    Validate that a library XML file is well-formed.

    Args:
        xml_file_path: Path to XML file to validate

    Returns:
        True if valid, False otherwise
    """
    try:
        xml_content = _iof.FileReader.read_text_file(xml_file_path)
        etree.fromstring(xml_content.encode('utf-8'))
        return True
    except Exception as e:
        logger.error(f"Invalid library XML: {e}")
        return False


def extract_problem_count_from_xml(xml_file_path: Union[str, Path]) -> int:
    """
    Extract the number of problems from a library XML file.

    Args:
        xml_file_path: Path to library XML file

    Returns:
        Number of problems found in the XML

    Raises:
        LibraryXMLError: If extraction fails
    """
    try:
        xml_content = _iof.FileReader.read_text_file(xml_file_path)
        root = etree.fromstring(xml_content.encode('utf-8'))

        problem_elements = root.findall('.//problem')
        count = len(problem_elements)

        logger.info(f"Found {count} problems in library XML")
        return count

    except Exception as e:
        raise LibraryXMLError(f"Failed to extract problem count from XML: {e}")
