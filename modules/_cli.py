"""
Command Line Interface module for lib-gen converter.

This module provides the CLI interface for the lib-gen application, handling
command-line arguments, file validation, directory setup, and orchestrating
the conversion process from markdown to edX library XML format.
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional, Dict, Any, List
from dataclasses import dataclass

from . import _con
from . import _iof
from . import _par

logger = logging.getLogger(__name__)


class CLIError(Exception):
    """Custom exception for CLI-related errors."""
    pass


class ValidationError(Exception):
    """Custom exception for input validation errors."""
    pass


@dataclass
class CLIConfiguration:
    """Configuration loaded from the CLI and config files."""
    library_name: str
    working_directory: Path
    input_folder: Path
    output_folder: Path
    library_folder: Path
    problem_folder: Path
    policies_folder: Path
    markdown_file: Path
    html_file: Path
    xml_file: Path
    config_file: Path
    assets_file: Path
    archive_file: Path

    # Configuration from JSON
    inp_markdown: str
    out_html: str
    out_xml: str
    display_name: str
    library: str
    org: str


class ArgumentParser:
    """Handles command-line argument parsing."""

    def __init__(self):
        """Initialize the argument parser."""
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """
        Create and configure the argument parser.

        Returns:
            Configured ArgumentParser instance
        """
        parser = argparse.ArgumentParser(
            prog='lib-gen',
            description='Convert markdown files to edX library XML format',
            epilog='For more information, see the README.md file.',
            formatter_class=argparse.RawDescriptionHelpFormatter
        )

        parser.add_argument(
            'library',
            type=str,
            help='Name of the library (used for archive filename)'
        )

        parser.add_argument(
            '-v', '--verbose',
            action='store_true',
            help='Enable verbose logging output'
        )

        parser.add_argument(
            '-q', '--quiet',
            action='store_true',
            help='Suppress all output except errors'
        )

        parser.add_argument(
            '--working-dir',
            type=str,
            default='.',
            help='Working directory path (default: current directory)'
        )

        return parser

    def parse_arguments(self, args: Optional[List[str]] = None) -> argparse.Namespace:
        """
        Parse command-line arguments.

        Args:
            args: List of arguments to parse (uses sys.argv if None)

        Returns:
            Parsed arguments namespace

        Raises:
            CLIError: If argument parsing fails
        """
        try:
            parsed_args = self.parser.parse_args(args)

            # Validate library name
            if not parsed_args.library or not parsed_args.library.strip():
                raise CLIError("Library name cannot be empty")

            # Validate verbose/quiet conflict
            if parsed_args.verbose and parsed_args.quiet:
                raise CLIError("Cannot specify both --verbose and --quiet options")

            return parsed_args

        except argparse.ArgumentError as e:
            raise CLIError(f"Invalid command-line arguments: {e}")
        except SystemExit:
            # argparse calls sys.exit on error, we want to handle it ourselves
            raise CLIError("Invalid command-line arguments")


class ConfigurationLoader:
    """Loads and validates configuration files."""

    @staticmethod
    def load_json_config(config_file_path: Path) -> Dict[str, Any]:
        """
        Load and validate JSON configuration file.

        Args:
            config_file_path: Path to configuration file

        Returns:
            Dictionary containing configuration data

        Raises:
            ValidationError: If configuration is invalid or missing
        """
        if not config_file_path.exists():
            raise ValidationError(f"Configuration file does not exist: {config_file_path}")

        try:
            config_data = _iof.FileReader.read_json(config_file_path)

            # Validate required fields
            required_fields = ['INP_MARKDOWN', 'OUT_HTML', 'OUT_XML',
                             'DISPLAY_NAME', 'LIBRARY', 'ORG']
            missing_fields = []

            for field in required_fields:
                if field not in config_data or not config_data[field]:
                    missing_fields.append(field)

            if missing_fields:
                raise ValidationError(f"Missing required configuration fields: {missing_fields}")

            logger.info(f"Successfully loaded configuration from: {config_file_path}")
            return config_data

        except Exception as e:
            if isinstance(e, ValidationError):
                raise
            raise ValidationError(f"Failed to load configuration file: {e}")

    @staticmethod
    def validate_assets_file(assets_file_path: Path) -> bool:
        """
        Validate that assets file exists.

        Args:
            assets_file_path: Path to assets file

        Returns:
            True if file exists, False otherwise
        """
        exists = assets_file_path.exists()
        if not exists:
            logger.warning(f"Assets file does not exist: {assets_file_path}")
        else:
            logger.info(f"Found assets file: {assets_file_path}")
        return exists


class DirectorySetup:
    """Handles directory structure creation and cleanup."""

    def __init__(self, working_directory: Path):
        """
        Initialize directory setup.

        Args:
            working_directory: Base working directory
        """
        self.working_dir = working_directory

    def setup_directories(self, config: CLIConfiguration) -> None:
        """
        Create necessary directory structure.

        Args:
            config: CLI configuration object

        Raises:
            CLIError: If directory setup fails
        """
        try:
            logger.info("Setting up directory structure...")

            # Clean and create output directory
            self._setup_directory(config.output_folder, clean=True)

            # Clean and create library structure
            self._setup_directory(config.library_folder, clean=True)
            self._setup_directory(config.problem_folder, clean=False)
            self._setup_directory(config.policies_folder, clean=False)

            logger.info("Directory structure setup completed")

        except Exception as e:
            raise CLIError(f"Failed to setup directories: {e}")

    def _setup_directory(self, directory_path: Path, clean: bool = False) -> None:
        """
        Setup a single directory with optional cleaning.

        Args:
            directory_path: Path to directory
            clean: Whether to clean existing directory first

        Raises:
            CLIError: If directory setup fails
        """
        try:
            if clean and directory_path.exists():
                _iof.DirectoryManager.delete_directory(directory_path)

            _iof.DirectoryManager.create_directory(directory_path)
            logger.debug(f"Setup directory: {directory_path}")

        except Exception as e:
            raise CLIError(f"Failed to setup directory {directory_path}: {e}")

    def copy_policy_file(self, source_path: Path, destination_dir: Path) -> None:
        """
        Copy policy file to destination directory.

        Args:
            source_path: Source policy file path
            destination_dir: Destination directory path

        Raises:
            CLIError: If copy operation fails
        """
        try:
            if source_path.exists():
                _iof.DirectoryManager.copy_file(source_path, destination_dir)
                logger.info(f"Copied policy file: {source_path} -> {destination_dir}")
            else:
                logger.warning(f"Policy file not found, skipping copy: {source_path}")

        except Exception as e:
            raise CLIError(f"Failed to copy policy file: {e}")


class ConversionOrchestrator:
    """Orchestrates the complete conversion process."""

    def __init__(self, config: CLIConfiguration):
        """
        Initialize the conversion orchestrator.

        Args:
            config: CLI configuration object
        """
        self.config = config
        self.pipeline = _par.ConversionPipeline(config.working_directory)

    def run_conversion(self) -> bool:
        """
        Run the complete conversion process.

        Returns:
            True if conversion successful, False otherwise

        Raises:
            CLIError: If conversion fails
        """
        try:
            logger.info("Starting conversion process...")

            # Check if archive already exists and remove it
            self._cleanup_existing_archive()

            # Run the markdown validation and conversion pipeline
            success = self.pipeline.process_markdown_file(
                self.config.markdown_file,
                self.config.html_file,
                self.config.xml_file,
                self.config.problem_folder
            )

            if not success:
                logger.error("Conversion pipeline failed")
                return False

            # Create the final archive
            self._create_archive()

            logger.info("Conversion process completed successfully")
            return True

        except Exception as e:
            logger.error(f"Conversion process failed: {e}")
            raise CLIError(f"Conversion failed: {e}")

    def _cleanup_existing_archive(self) -> None:
        """Remove existing archive file if it exists."""
        try:
            if self.config.archive_file.exists():
                _iof.ArchiveManager.delete_archive(self.config.archive_file)
                logger.info(f"Removed existing archive: {self.config.archive_file}")
        except Exception as e:
            logger.warning(f"Failed to remove existing archive: {e}")

    def _create_archive(self) -> None:
        """
        Create the final tar.gz archive.

        Raises:
            CLIError: If archive creation fails
        """
        try:
            logger.info("Creating tar.gz archive...")

            _iof.ArchiveManager.create_tar_gz_archive(
                self.config.library_folder,
                self.config.archive_file,
                self.config.library_folder.name
            )

            logger.info(f"Archive created successfully: {self.config.archive_file}")

        except Exception as e:
            raise CLIError(f"Failed to create archive: {e}")


class CLIApplication:
    """Main CLI application class."""

    def __init__(self):
        """Initialize the CLI application."""
        self.arg_parser = ArgumentParser()
        self.setup_logging()

    def setup_logging(self, level: int = logging.INFO) -> None:
        """
        Setup logging configuration.

        Args:
            level: Logging level
        """
        logging.basicConfig(
            level=level,
            format='%(levelname)s: %(message)s',
            handlers=[logging.StreamHandler(sys.stdout)]
        )

    def run(self, args: Optional[List[str]] = None) -> int:
        """
        Run the CLI application.

        Args:
            args: Command-line arguments (uses sys.argv if None)

        Returns:
            Exit code (0 for success, non-zero for error)
        """
        try:
            # Parse command-line arguments
            parsed_args = self.arg_parser.parse_arguments(args)

            # Configure logging based on arguments
            if parsed_args.quiet:
                self.setup_logging(logging.ERROR)
            elif parsed_args.verbose:
                self.setup_logging(logging.DEBUG)

            # Create configuration
            config = self._create_configuration(parsed_args)

            # Setup directories
            directory_setup = DirectorySetup(config.working_directory)
            directory_setup.setup_directories(config)
            directory_setup.copy_policy_file(config.assets_file, config.policies_folder)

            # Run conversion
            orchestrator = ConversionOrchestrator(config)
            success = orchestrator.run_conversion()

            return 0 if success else 1

        except (CLIError, ValidationError) as e:
            logger.error(str(e))
            return 1
        except KeyboardInterrupt:
            logger.info("Operation cancelled by user")
            return 1
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return 1

    def _create_configuration(self, args: argparse.Namespace) -> CLIConfiguration:
        """
        Create configuration object from parsed arguments and config files.

        Args:
            args: Parsed command-line arguments

        Returns:
            CLIConfiguration object

        Raises:
            ValidationError: If configuration creation fails
        """
        try:
            # Setup basic paths
            working_dir = Path(args.working_dir).resolve()
            input_folder = working_dir / _con.INPUT_FOLDER
            output_folder = working_dir / _con.OUTPUT_FOLDER
            library_folder = working_dir / _con.LIBRARY_FOLDER

            # Validate working directory
            if not working_dir.exists():
                raise ValidationError(f"Working directory does not exist: {working_dir}")

            # Load configuration files
            config_file = input_folder / _con.CONFIG_FILENAME
            json_config = ConfigurationLoader.load_json_config(config_file)

            # Validate assets file
            assets_file = input_folder / _con.POLICIES_FILENAME
            ConfigurationLoader.validate_assets_file(assets_file)

            # Create full configuration
            config = CLIConfiguration(
                library_name=args.library,
                working_directory=working_dir,
                input_folder=input_folder,
                output_folder=output_folder,
                library_folder=library_folder,
                problem_folder=library_folder / _con.PROBLEM_FOLDER,
                policies_folder=library_folder / _con.POLICIES_FOLDER,
                config_file=config_file,
                assets_file=assets_file,

                # File paths based on configuration
                markdown_file=input_folder / json_config['INP_MARKDOWN'],
                html_file=output_folder / json_config['OUT_HTML'],
                xml_file=output_folder / json_config['OUT_XML'],
                archive_file=working_dir / f"{_con.LIBRARY_ARCHIVE_PREFIX}{args.library}.tar.gz",

                # Configuration values
                inp_markdown=json_config['INP_MARKDOWN'],
                out_html=json_config['OUT_HTML'],
                out_xml=json_config['OUT_XML'],
                display_name=json_config['DISPLAY_NAME'],
                library=json_config['LIBRARY'],
                org=json_config['ORG']
            )

            # Validate input markdown file exists
            if not config.markdown_file.exists():
                raise ValidationError(f"Input markdown file does not exist: {config.markdown_file}")

            logger.info(f"Configuration created successfully for library: {args.library}")
            return config

        except Exception as e:
            if isinstance(e, ValidationError):
                raise
            raise ValidationError(f"Failed to create configuration: {e}")


# =============================================================================
# Legacy Functions (maintaining backward compatibility)
# =============================================================================

def CLI() -> None:
    """
    Main CLI entry point (legacy function).

    Raises:
        SystemExit: With appropriate exit code
    """
    try:
        app = CLIApplication()
        exit_code = app.run()
        sys.exit(exit_code)
    except Exception as e:
        logger.error(f"CLI execution failed: {e}")
        sys.exit(1)


# =============================================================================
# Utility Functions
# =============================================================================

def print_version_info() -> None:
    """Print version and system information."""
    print("lib-gen: Markdown to XML converter for edX library generator")
    print("Version: 1.0.0")
    print("Python version:", sys.version)


def validate_environment() -> bool:
    """
    Validate that the environment has required dependencies.

    Returns:
        True if environment is valid, False otherwise
    """
    required_modules = ['markdown', 'lxml', 'bs4']

    for module_name in required_modules:
        try:
            __import__(module_name)
        except ImportError as e:
            logger.error(f"Missing required dependency: {e}")
            return False

    return True


if __name__ == "__main__":
    CLI()
