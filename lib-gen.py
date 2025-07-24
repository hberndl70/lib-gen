#!/usr/bin/env python3
"""
lib-gen: Markdown to XML converter for edX library generator

A tool that converts markdown files to XML format suitable for edX library import.
Generates a compressed archive that can be directly imported into an edX library.
"""

import sys
import time
from typing import Optional

from modules import _cli


def measure_execution_time(func):
    """Decorator to measure and display execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"\nExecution completed in {execution_time:.2f} seconds\n")
    return wrapper


@measure_execution_time
def run_conversion() -> Optional[int]:
    """
    Run the markdown to XML conversion process.

    Returns:
        Optional[int]: Exit code (None for success, non-zero for error)
    """
    try:
        _cli.CLI()
        return None
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        return 1
    except Exception as e:
        print(f"Error during conversion: {e}")
        return 1


def main() -> int:
    """
    Main entry point for the lib-gen application.

    Returns:
        int: Exit code (0 for success, non-zero for error)
    """
    print("lib-gen: Markdown to XML converter for edX library generator")
    print("=" * 60)

    exit_code = run_conversion()
    return exit_code or 0


if __name__ == "__main__":
    sys.exit(main())
