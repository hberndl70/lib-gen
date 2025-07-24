"""
File I/O operations module for lib-gen converter.

This module provides file and directory operations for the lib-gen application,
including reading/writing files, directory management, and archive creation.
"""

import json
import os
import shutil
import subprocess
import tarfile
from pathlib import Path
from typing import Dict, Any, Optional, Union
import logging

# Configure logging for this module
logger = logging.getLogger(__name__)


class FileOperationError(Exception):
    """Custom exception for file operation errors."""
    pass


class DirectoryManager:
    """Handles directory operations with proper error handling."""

    @staticmethod
    def get_working_directory() -> Path:
        """
        Get the current working directory.

        Returns:
            Path: Current working directory as Path object
        """
        return Path.cwd()

    @staticmethod
    def create_directory(path: Union[str, Path]) -> None:
        """
        Create directory with all necessary parent directories.

        Args:
            path: Directory path to create

        Raises:
            FileOperationError: If directory creation fails
        """
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {path}")
        except Exception as e:
            raise FileOperationError(f"Failed to create directory {path}: {e}")

    @staticmethod
    def delete_directory(path: Union[str, Path]) -> None:
        """
        Delete directory and all its contents.

        Args:
            path: Directory path to delete

        Raises:
            FileOperationError: If directory deletion fails
        """
        path_obj = Path(path)
        if not path_obj.exists():
            logger.info(f"Directory does not exist, skipping: {path}")
            return

        try:
            shutil.rmtree(path_obj)
            logger.info(f"Deleted directory: {path}")
        except Exception as e:
            raise FileOperationError(f"Failed to delete directory {path}: {e}")

    @staticmethod
    def copy_file(source: Union[str, Path], destination: Union[str, Path]) -> None:
        """
        Copy file from source to destination.

        Args:
            source: Source file path
            destination: Destination path (can be file or directory)

        Raises:
            FileOperationError: If file copy fails
        """
        source_path = Path(source)
        dest_path = Path(destination)

        if not source_path.exists():
            raise FileOperationError(f"Source file does not exist: {source}")

        try:
            if dest_path.is_dir():
                shutil.copy2(source_path, dest_path)
            else:
                shutil.copy2(source_path, dest_path)
            logger.info(f"Copied file from {source} to {destination}")
        except Exception as e:
            raise FileOperationError(f"Failed to copy file from {source} to {destination}: {e}")


class FileReader:
    """Handles file reading operations with proper error handling."""

    @staticmethod
    def read_json(file_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Read and parse JSON file.

        Args:
            file_path: Path to JSON file

        Returns:
            Dict containing parsed JSON data

        Raises:
            FileOperationError: If file reading or JSON parsing fails
        """
        path_obj = Path(file_path)

        if not path_obj.exists():
            raise FileOperationError(f"JSON file does not exist: {file_path}")

        try:
            with open(path_obj, 'r', encoding='utf-8') as file:
                data = json.load(file)
            logger.info(f"Successfully read JSON file: {file_path}")
            return data
        except json.JSONDecodeError as e:
            raise FileOperationError(f"Invalid JSON format in {file_path}: {e}")
        except Exception as e:
            raise FileOperationError(f"Failed to read JSON file {file_path}: {e}")

    @staticmethod
    def read_text_file(file_path: Union[str, Path], encoding: str = 'utf-8') -> str:
        """
        Read text file content.

        Args:
            file_path: Path to text file
            encoding: File encoding (default: utf-8)

        Returns:
            String containing file content

        Raises:
            FileOperationError: If file reading fails
        """
        path_obj = Path(file_path)

        if not path_obj.exists():
            raise FileOperationError(f"Text file does not exist: {file_path}")

        try:
            with open(path_obj, 'r', encoding=encoding) as file:
                content = file.read()
            logger.info(f"Successfully read text file: {file_path}")
            return content
        except Exception as e:
            raise FileOperationError(f"Failed to read text file {file_path}: {e}")

    @staticmethod
    def read_html_file(file_path: Union[str, Path]) -> str:
        """
        Read HTML file content.

        Args:
            file_path: Path to HTML file

        Returns:
            String containing HTML content
        """
        return FileReader.read_text_file(file_path, encoding='utf-8')


class FileWriter:
    """Handles file writing operations with proper error handling."""

    @staticmethod
    def write_text_file(content: str, file_path: Union[str, Path],
                       encoding: str = 'utf-8', mode: str = 'w') -> None:
        """
        Write text content to file.

        Args:
            content: Text content to write
            file_path: Path to output file
            encoding: File encoding (default: utf-8)
            mode: File write mode (default: 'w')

        Raises:
            FileOperationError: If file writing fails
        """
        path_obj = Path(file_path)

        # Ensure parent directory exists
        path_obj.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(path_obj, mode, encoding=encoding) as file:
                file.write(content)
            logger.info(f"Successfully wrote text file: {file_path}")
        except Exception as e:
            raise FileOperationError(f"Failed to write text file {file_path}: {e}")

    @staticmethod
    def write_binary_file(content: bytes, file_path: Union[str, Path],
                         mode: str = 'wb') -> None:
        """
        Write binary content to file.

        Args:
            content: Binary content to write
            file_path: Path to output file
            mode: File write mode (default: 'wb')

        Raises:
            FileOperationError: If file writing fails
        """
        path_obj = Path(file_path)

        # Ensure parent directory exists
        path_obj.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(path_obj, mode) as file:
                file.write(content)
            logger.info(f"Successfully wrote binary file: {file_path}")
        except Exception as e:
            raise FileOperationError(f"Failed to write binary file {file_path}: {e}")

    @staticmethod
    def append_binary_file(content: bytes, file_path: Union[str, Path]) -> None:
        """
        Append binary content to file.

        Args:
            content: Binary content to append
            file_path: Path to output file
        """
        FileWriter.write_binary_file(content, file_path, mode='ab')

    @staticmethod
    def write_html_file(html_content: str, file_path: Union[str, Path]) -> None:
        """
        Write HTML content to file.

        Args:
            html_content: HTML content to write
            file_path: Path to HTML output file
        """
        FileWriter.write_text_file(html_content, file_path, encoding='utf-8')

    @staticmethod
    def write_xml_file(xml_content: Union[str, bytes], file_path: Union[str, Path]) -> None:
        """
        Write XML content to file.

        Args:
            xml_content: XML content to write (string or bytes)
            file_path: Path to XML output file
        """
        if isinstance(xml_content, bytes):
            FileWriter.write_binary_file(xml_content, file_path)
        else:
            FileWriter.write_text_file(xml_content, file_path, encoding='utf-8')

    @staticmethod
    def append_xml_file(xml_content: Union[str, bytes], file_path: Union[str, Path]) -> None:
        """
        Append XML content to file.

        Args:
            xml_content: XML content to append (string or bytes)
            file_path: Path to XML output file
        """
        if isinstance(xml_content, bytes):
            FileWriter.append_binary_file(xml_content, file_path)
        else:
            FileWriter.write_text_file(xml_content, file_path, encoding='utf-8', mode='a')


class ArchiveManager:
    """Handles archive creation and management."""

    @staticmethod
    def delete_archive(archive_path: Union[str, Path]) -> None:
        """
        Delete archive file if it exists.

        Args:
            archive_path: Path to archive file

        Raises:
            FileOperationError: If archive deletion fails
        """
        path_obj = Path(archive_path)

        if not path_obj.exists():
            logger.info(f"Archive does not exist, skipping: {archive_path}")
            return

        try:
            path_obj.unlink()
            logger.info(f"Deleted archive: {archive_path}")
        except Exception as e:
            raise FileOperationError(f"Failed to delete archive {archive_path}: {e}")

    @staticmethod
    def create_tar_gz_archive(source_dir: Union[str, Path],
                             archive_path: Union[str, Path],
                             base_name: Optional[str] = None) -> None:
        """
        Create a tar.gz archive from a directory.

        Args:
            source_dir: Directory to archive
            archive_path: Path for the output archive
            base_name: Base name for files in archive (optional)

        Raises:
            FileOperationError: If archive creation fails
        """
        source_path = Path(source_dir)
        archive_path_obj = Path(archive_path)

        if not source_path.exists():
            raise FileOperationError(f"Source directory does not exist: {source_dir}")

        # Ensure parent directory exists
        archive_path_obj.parent.mkdir(parents=True, exist_ok=True)

        try:
            with tarfile.open(archive_path_obj, 'w:gz') as tar:
                tar.add(source_path, arcname=base_name or source_path.name)
            logger.info(f"Created tar.gz archive: {archive_path}")
        except Exception as e:
            raise FileOperationError(f"Failed to create archive {archive_path}: {e}")


class FilenameGenerator:
    """Generates specific filename formats required by the application."""

    @staticmethod
    def create_32char_filename(base_template: str, number: Union[int, str]) -> str:
        """
        Create a 32-character filename by inserting a number into a template.

        The template should be a string of 32 characters (typically zeros),
        and the number will replace characters at the end.

        Args:
            base_template: 32-character template string
            number: Number to insert (will be converted to string)

        Returns:
            32-character filename string

        Raises:
            ValueError: If template is not 32 characters or number is too long
        """
        if len(base_template) != 32:
            raise ValueError(f"Template must be exactly 32 characters, got {len(base_template)}")

        number_str = str(number)
        if len(number_str) > 32:
            raise ValueError(f"Number string too long: {len(number_str)} characters")

        # Replace the last n characters with the number
        result = base_template[:32 - len(number_str)] + number_str
        return result


# =============================================================================
# Convenience Functions (maintaining backward compatibility)
# =============================================================================

def Working_DIR() -> str:
    """Get current working directory (legacy function name)."""
    return str(DirectoryManager.get_working_directory())

def Create_DIR(path: Union[str, Path]) -> None:
    """Create directory (legacy function name)."""
    DirectoryManager.create_directory(path)

def Delete_DIR(path: Union[str, Path]) -> None:
    """Delete directory (legacy function name)."""
    DirectoryManager.delete_directory(path)

def Delete_GZ(archive_path: Union[str, Path]) -> None:
    """Delete GZ archive (legacy function name)."""
    ArchiveManager.delete_archive(archive_path)

def Copy_POL(source_file: Union[str, Path], destination_dir: Union[str, Path]) -> None:
    """Copy policy file (legacy function name)."""
    DirectoryManager.copy_file(source_file, destination_dir)

def Read_JSON(json_file: Union[str, Path]) -> Dict[str, Any]:
    """Read JSON file (legacy function name)."""
    return FileReader.read_json(json_file)

def Read_HTML(html_file: Union[str, Path]) -> str:
    """Read HTML file (legacy function name)."""
    return FileReader.read_html_file(html_file)

def Write_HTML(html_content: str, html_file: Union[str, Path]) -> None:
    """Write HTML file (legacy function name)."""
    FileWriter.write_html_file(html_content, html_file)

def Write_XML(xml_content: Union[str, bytes], xml_file: Union[str, Path]) -> None:
    """Write/append XML file (legacy function name)."""
    FileWriter.append_xml_file(xml_content, xml_file)

def Write_CBP(cbp_content: bytes, cbp_file: Union[str, Path]) -> None:
    """Write CBP file (legacy function name)."""
    FileWriter.write_binary_file(cbp_content, cbp_file)

def Create_TAR(working_dir: Union[str, Path], folder_name: str, tar_filename: str) -> None:
    """Create TAR.GZ archive (legacy function name)."""
    source_path = Path(working_dir) / folder_name
    archive_path = Path(working_dir) / f"{tar_filename}.gz"
    ArchiveManager.create_tar_gz_archive(source_path, archive_path, folder_name)

def Create_Name32(template: str, number: Union[int, str]) -> str:
    """Create 32-character filename (legacy function name)."""
    return FilenameGenerator.create_32char_filename(template, number)
