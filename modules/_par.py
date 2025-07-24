"""
Parsing and conversion module for lib-gen converter.

This module handles the complete parsing pipeline:
1. Markdown validation and structure checking
2. Markdown to HTML conversion
3. HTML parsing and content extraction
4. XML generation for checkbox problems
"""

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any, Optional, Union, Tuple
from enum import Enum

import markdown
from bs4 import BeautifulSoup, Tag

from . import _con
from . import _iof
from . import _lib
from . import _xml

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


class ParsingError(Exception):
    """Custom exception for parsing errors."""
    pass


class ConversionError(Exception):
    """Custom exception for conversion errors."""
    pass


class ValidationResult(Enum):
    """Enumeration for validation results."""
    SUCCESS = "success"
    CHECKBOX_ERROR = "checkbox_error"
    FORMAT_ERROR = "format_error"
    BLANKS_ERROR = "blanks_error"


@dataclass
class MarkdownStructure:
    """Structure information extracted from markdown."""
    h1_count: int  # Number of level 1 headers (problems)
    h2_count: int  # Number of level 2 headers (questions)
    end_markers: int  # Number of '===' end markers
    checkbox_count: int  # Number of checkboxes
    invalid_checkbox_count: int  # Number of invalid checkboxes (uppercase X)
    newline_count: int  # Number of double newlines


@dataclass
class ProblemData:
    """Data structure for a single checkbox problem."""
    display_name: str
    question_text: str
    choices: List[_xml.Choice]


class MarkdownValidator:
    """Validates markdown structure and format."""

    @staticmethod
    def validate_markdown_file(file_path: Union[str, Path]) -> ValidationResult:
        """
        Validate markdown file structure.

        Args:
            file_path: Path to markdown file

        Returns:
            ValidationResult indicating success or type of error

        Raises:
            ValidationError: If file cannot be read or validation fails
        """
        try:
            content = _iof.FileReader.read_text_file(file_path)
            return MarkdownValidator.validate_markdown_content(content)
        except Exception as e:
            raise ValidationError(f"Failed to validate markdown file {file_path}: {e}")

    @staticmethod
    def validate_markdown_content(content: str) -> ValidationResult:
        """
        Validate markdown content structure.

        Args:
            content: Markdown content as string

        Returns:
            ValidationResult indicating success or type of error
        """
        try:
            structure = MarkdownValidator._extract_structure(content)
            return MarkdownValidator._validate_structure(structure)
        except Exception as e:
            logger.error(f"Failed to validate markdown content: {e}")
            raise ValidationError(f"Markdown validation failed: {e}")

    @staticmethod
    def _extract_structure(content: str) -> MarkdownStructure:
        """
        Extract structural information from markdown content.

        Args:
            content: Markdown content

        Returns:
            MarkdownStructure object with counts
        """
        # Count level 1 headers (problems)
        h1_count = len(re.findall(r'^# |[^#]# ', content, re.MULTILINE))

        # Count level 2 headers (questions)
        h2_count = len(re.findall(r'[#]# ', content))

        # Count end of problem markers
        end_markers = len(re.findall(r'===', content))

        # Count valid checkboxes
        checkbox_count = len(re.findall(r'\[[ x]\]', content))

        # Count invalid checkboxes (uppercase X)
        invalid_checkbox_count = len(re.findall(r'\[[X]\]', content))

        # Count double newlines
        newline_count = len(re.findall(r'[/\n]{2}', content))

        return MarkdownStructure(
            h1_count=h1_count,
            h2_count=h2_count,
            end_markers=end_markers,
            checkbox_count=checkbox_count,
            invalid_checkbox_count=invalid_checkbox_count,
            newline_count=newline_count
        )

    @staticmethod
    def _validate_structure(structure: MarkdownStructure) -> ValidationResult:
        """
        Validate the extracted structure.

        Args:
            structure: MarkdownStructure to validate

        Returns:
            ValidationResult indicating validation outcome
        """
        # Check for invalid checkboxes (uppercase X)
        if structure.invalid_checkbox_count > 0:
            logger.error(f"Found {structure.invalid_checkbox_count} invalid checkboxes with uppercase 'X'")
            return ValidationResult.CHECKBOX_ERROR

        # Check format consistency (h1 == h2 == end_markers)
        if not (structure.h1_count == structure.h2_count == structure.end_markers):
            logger.error(f"Format mismatch: H1={structure.h1_count}, H2={structure.h2_count}, Markers={structure.end_markers}")
            return ValidationResult.FORMAT_ERROR

        # Check blank lines consistency
        expected_structure_count = structure.h1_count + structure.h2_count + structure.end_markers + structure.checkbox_count
        if expected_structure_count - structure.newline_count != 0:
            logger.error(f"Blank lines mismatch: Expected structure count={expected_structure_count}, Newlines={structure.newline_count}")
            return ValidationResult.BLANKS_ERROR

        logger.info("Markdown structure validation passed")
        return ValidationResult.SUCCESS


class MarkdownConverter:
    """Converts markdown to HTML."""

    @staticmethod
    def convert_file_to_html(markdown_path: Union[str, Path],
                           html_path: Union[str, Path]) -> None:
        """
        Convert markdown file to HTML file.

        Args:
            markdown_path: Input markdown file path
            html_path: Output HTML file path

        Raises:
            ConversionError: If conversion fails
        """
        try:
            markdown_content = _iof.FileReader.read_text_file(markdown_path)
            html_content = MarkdownConverter.convert_to_html(markdown_content)
            _iof.FileWriter.write_html_file(html_content, html_path)
            logger.info(f"Converted markdown to HTML: {markdown_path} -> {html_path}")
        except Exception as e:
            raise ConversionError(f"Failed to convert markdown file to HTML: {e}")

    @staticmethod
    def convert_to_html(markdown_content: str) -> str:
        """
        Convert markdown content to HTML.

        Args:
            markdown_content: Markdown content string

        Returns:
            HTML content string

        Raises:
            ConversionError: If conversion fails
        """
        try:
            html_content = markdown.markdown(markdown_content)
            logger.debug("Successfully converted markdown to HTML")
            return html_content
        except Exception as e:
            raise ConversionError(f"Failed to convert markdown to HTML: {e}")


class HTMLParser:
    """Parses HTML content to extract problem data."""

    def __init__(self):
        """Initialize the HTML parser."""
        self.soup: Optional[BeautifulSoup] = None

    def parse_html_content(self, html_content: str) -> List[ProblemData]:
        """
        Parse HTML content and extract problem data.

        Args:
            html_content: HTML content string

        Returns:
            List of ProblemData objects

        Raises:
            ParsingError: If parsing fails
        """
        try:
            self.soup = BeautifulSoup(html_content, "html.parser")
            return self._extract_problems()
        except Exception as e:
            raise ParsingError(f"Failed to parse HTML content: {e}")

    def parse_html_file(self, html_path: Union[str, Path]) -> List[ProblemData]:
        """
        Parse HTML file and extract problem data.

        Args:
            html_path: Path to HTML file

        Returns:
            List of ProblemData objects

        Raises:
            ParsingError: If parsing fails
        """
        try:
            html_content = _iof.FileReader.read_html_file(html_path)
            return self.parse_html_content(html_content)
        except Exception as e:
            raise ParsingError(f"Failed to parse HTML file {html_path}: {e}")

    def _extract_problems(self) -> List[ProblemData]:
        """
        Extract problem data from parsed HTML.

        Returns:
            List of ProblemData objects

        Raises:
            ParsingError: If extraction fails
        """
        if not self.soup:
            raise ParsingError("No HTML content loaded")

        try:
            # Extract all relevant elements
            display_names = self.soup.find_all('h1')
            questions = self.soup.find_all('h2')
            paragraphs = self.soup.find_all('p')

            if len(display_names) != len(questions):
                raise ParsingError(f"Mismatch between display names ({len(display_names)}) and questions ({len(questions)})")

            problems = []
            paragraph_index = 0

            for i in range(len(display_names)):
                display_name = display_names[i].get_text().strip()
                question_text = self._extract_question_text(questions[i])

                # Extract choices for this problem
                choices, consumed_paragraphs = self._extract_choices_for_problem(paragraphs, paragraph_index)
                paragraph_index += consumed_paragraphs

                problems.append(ProblemData(
                    display_name=display_name,
                    question_text=question_text,
                    choices=choices
                ))

            logger.info(f"Extracted {len(problems)} problems from HTML")
            return problems

        except Exception as e:
            raise ParsingError(f"Failed to extract problems from HTML: {e}")

    def _extract_question_text(self, question_element: Tag) -> str:
        """
        Extract question text from h2 element.

        Args:
            question_element: BeautifulSoup Tag object

        Returns:
            Question text as string
        """
        # Join all contents of the question element
        contents = question_element.contents
        return ''.join(str(content) for content in contents).strip()

    def _extract_choices_for_problem(self, paragraphs: List[Tag],
                                   start_index: int) -> Tuple[List[_xml.Choice], int]:
        """
        Extract choices for a single problem.

        Args:
            paragraphs: List of paragraph elements
            start_index: Starting index in paragraphs list

        Returns:
            Tuple of (choices list, number of paragraphs consumed)

        Raises:
            ParsingError: If choice extraction fails
        """
        choices = []
        consumed = 0

        for i in range(start_index, len(paragraphs)):
            paragraph_text = paragraphs[i].get_text().strip()

            # Check for end marker
            if paragraph_text == _con.PROBLEM_SEPARATOR:
                consumed += 1
                break

            # Extract choice content
            choice_content = ''.join(str(content) for content in paragraphs[i].contents).strip()

            try:
                choice = _xml.Choice.from_markdown(choice_content)
                choices.append(choice)
                consumed += 1
            except Exception as e:
                logger.warning(f"Failed to parse choice '{choice_content}': {e}")
                consumed += 1

        if not choices:
            raise ParsingError(f"No choices found for problem starting at paragraph {start_index}")

        return choices, consumed


class ProblemXMLGenerator:
    """Generates XML for checkbox problems."""

    def __init__(self, working_directory: Optional[Union[str, Path]] = None):
        """
        Initialize the XML generator.

        Args:
            working_directory: Working directory path
        """
        self.working_dir = Path(working_directory) if working_directory else Path.cwd()
        self.xml_generator = _xml.CheckboxProblemGenerator()

    def generate_problems_xml(self, problems: List[ProblemData],
                            xml_output_path: Union[str, Path],
                            problem_folder_path: Union[str, Path]) -> None:
        """
        Generate XML files for all problems.

        Args:
            problems: List of ProblemData objects
            xml_output_path: Path for combined XML output
            problem_folder_path: Path to folder for individual problem files

        Raises:
            ConversionError: If XML generation fails
        """
        try:
            # Generate library XML first
            library_service = _lib.LibraryXMLService(self.working_dir)
            library_service.create_library_from_config(len(problems))

            # Generate individual problem XML files
            for i, problem in enumerate(problems, 1):
                self._generate_single_problem_xml(problem, i, xml_output_path, problem_folder_path)

            logger.info(f"Generated XML for {len(problems)} problems")

        except Exception as e:
            raise ConversionError(f"Failed to generate problems XML: {e}")

    def _generate_single_problem_xml(self, problem: ProblemData, problem_number: int,
                                   xml_output_path: Union[str, Path],
                                   problem_folder_path: Union[str, Path]) -> None:
        """
        Generate XML for a single problem.

        Args:
            problem: ProblemData object
            problem_number: Sequential number of the problem
            xml_output_path: Path for combined XML output
            problem_folder_path: Path to folder for individual problem files

        Raises:
            ConversionError: If XML generation fails
        """
        try:
            # Generate XML content
            xml_bytes = self.xml_generator.generate_problem_xml(
                problem.display_name,
                problem.question_text,
                problem.choices
            )

            # Create individual problem file
            problem_filename = _iof.FilenameGenerator.create_32char_filename(
                _con.CBP_FILENAME_TEMPLATE, str(problem_number)
            )
            problem_file_path = Path(problem_folder_path) / f"{problem_filename}.xml"

            _iof.FileWriter.write_binary_file(xml_bytes, problem_file_path)

            # Append to combined XML file
            _iof.FileWriter.append_binary_file(xml_bytes, xml_output_path)

            logger.debug(f"Generated XML for problem {problem_number}: {problem.display_name}")

        except Exception as e:
            raise ConversionError(f"Failed to generate XML for problem {problem_number}: {e}")


class ConversionPipeline:
    """Main pipeline for the complete conversion process."""

    def __init__(self, working_directory: Optional[Union[str, Path]] = None):
        """
        Initialize the conversion pipeline.

        Args:
            working_directory: Working directory path
        """
        self.working_dir = Path(working_directory) if working_directory else Path.cwd()
        self.html_parser = HTMLParser()
        self.xml_generator = ProblemXMLGenerator(self.working_dir)

    def process_markdown_file(self, markdown_path: Union[str, Path],
                            html_output_path: Union[str, Path],
                            xml_output_path: Union[str, Path],
                            problem_folder_path: Union[str, Path]) -> bool:
        """
        Process markdown file through the complete conversion pipeline.

        Args:
            markdown_path: Input markdown file path
            html_output_path: Output HTML file path
            xml_output_path: Output XML file path
            problem_folder_path: Path to folder for individual problem files

        Returns:
            True if successful, False otherwise

        Raises:
            ValidationError, ConversionError, ParsingError: If any step fails
        """
        try:
            logger.info(f"Starting conversion pipeline for: {markdown_path}")

            # Step 1: Validate markdown structure
            logger.info("Step 1: Validating markdown structure...")
            validation_result = MarkdownValidator.validate_markdown_file(markdown_path)

            if validation_result != ValidationResult.SUCCESS:
                self._log_validation_error(validation_result)
                return False

            # Step 2: Convert markdown to HTML
            logger.info("Step 2: Converting markdown to HTML...")
            MarkdownConverter.convert_file_to_html(markdown_path, html_output_path)

            # Step 3: Parse HTML and extract problems
            logger.info("Step 3: Parsing HTML and extracting problems...")
            problems = self.html_parser.parse_html_file(html_output_path)

            if not problems:
                logger.error("No problems found in HTML content")
                return False

            # Step 4: Generate XML for all problems
            logger.info("Step 4: Generating XML for problems...")
            self.xml_generator.generate_problems_xml(problems, xml_output_path, problem_folder_path)

            logger.info("Conversion pipeline completed successfully")
            return True

        except Exception as e:
            logger.error(f"Conversion pipeline failed: {e}")
            raise

    def _log_validation_error(self, validation_result: ValidationResult) -> None:
        """
        Log appropriate error message based on validation result.

        Args:
            validation_result: The validation result to log
        """
        error_messages = {
            ValidationResult.CHECKBOX_ERROR: "Invalid checkbox format found (use [x] or [ ], not [X])",
            ValidationResult.FORMAT_ERROR: "Markdown structure format is incorrect",
            ValidationResult.BLANKS_ERROR: "Blank line structure is incorrect"
        }

        message = error_messages.get(validation_result, "Unknown validation error")
        logger.error(f"Markdown validation failed: {message}")


# =============================================================================
# Legacy Functions (maintaining backward compatibility)
# =============================================================================

def Check_Markdown(input_file: Union[str, Path]) -> bool:
    """
    Check markdown file structure (legacy function).

    Args:
        input_file: Path to markdown file

    Returns:
        True if valid, False otherwise
    """
    try:
        result = MarkdownValidator.validate_markdown_file(input_file)
        return result == ValidationResult.SUCCESS
    except Exception as e:
        logger.error(f"Legacy Check_Markdown failed: {e}")
        return False


def Conv_Markdown(input_file: Union[str, Path]) -> str:
    """
    Convert markdown file to HTML (legacy function).

    Args:
        input_file: Path to markdown file

    Returns:
        HTML content as string
    """
    try:
        return MarkdownConverter.convert_to_html(
            _iof.FileReader.read_text_file(input_file)
        )
    except Exception as e:
        logger.error(f"Legacy Conv_Markdown failed: {e}")
        raise ConversionError(f"Failed to convert markdown: {e}")


def Parse_HTML(html_text: str, xml_file: Union[str, Path],
               cbp_folder: Union[str, Path]) -> None:
    """
    Parse HTML and generate XML files (legacy function).

    Args:
        html_text: HTML content string
        xml_file: Output XML file path
        cbp_folder: Folder path for individual problem files
    """
    try:
        parser = HTMLParser()
        problems = parser.parse_html_content(html_text)

        generator = ProblemXMLGenerator()
        generator.generate_problems_xml(problems, xml_file, cbp_folder)

        logger.info("Legacy Parse_HTML completed successfully")
    except Exception as e:
        logger.error(f"Legacy Parse_HTML failed: {e}")
        raise ParsingError(f"Failed to parse HTML: {e}")


# =============================================================================
# Utility Functions
# =============================================================================

def validate_and_log_results(validation_result: ValidationResult) -> None:
    """
    Log validation results with appropriate messages.

    Args:
        validation_result: Validation result to log
    """
    result_messages = {
        ValidationResult.SUCCESS: ("... format OK!", "... blanks OK!", "... boxes OK!"),
        ValidationResult.CHECKBOX_ERROR: ("... boxes ERROR!",),
        ValidationResult.FORMAT_ERROR: ("... format ERROR!",),
        ValidationResult.BLANKS_ERROR: ("... blanks ERROR!",)
    }

    messages = result_messages.get(validation_result, ("... unknown validation result!",))
    for message in messages:
        if "ERROR" in message:
            logger.error(message)
        else:
            logger.info(message)


def get_markdown_statistics(markdown_path: Union[str, Path]) -> MarkdownStructure:
    """
    Get statistical information about markdown file structure.

    Args:
        markdown_path: Path to markdown file

    Returns:
        MarkdownStructure with statistical information

    Raises:
        ValidationError: If file cannot be analyzed
    """
    try:
        content = _iof.FileReader.read_text_file(markdown_path)
        return MarkdownValidator._extract_structure(content)
    except Exception as e:
        raise ValidationError(f"Failed to analyze markdown statistics: {e}")
