#!/usr/bin/env python3
"""
Test script for lib-gen refactored modules.

This script validates that all the refactored modules work correctly
and provides examples of how to use the new APIs.
"""

import sys
import tempfile
import shutil
from pathlib import Path

# Add the modules directory to the path
sys.path.insert(0, str(Path(__file__).parent / 'modules'))

def test_constants():
    """Test the constants module."""
    print("Testing constants module...")

    try:
        from modules import _con

        # Test that all constants are accessible
        assert _con.INPUT_FOLDER == 'input'
        assert _con.OUTPUT_FOLDER == 'output'
        assert _con.LIBRARY_FOLDER == 'library'
        assert _con.DEFAULT_DESCRIPTION is not None
        assert _con.CBP_FILENAME_TEMPLATE == '00000000000000000000000000000000'

        # Test backward compatibility
        assert _con.INP_FOLDER == _con.INPUT_FOLDER
        assert _con.OUT_FOLDER == _con.OUTPUT_FOLDER
        assert _con.LIB_FOLDER == _con.LIBRARY_FOLDER

        print("✓ Constants module tests passed")
        return True

    except Exception as e:
        print(f"✗ Constants module tests failed: {e}")
        return False


def test_iof_module():
    """Test the I/O functions module."""
    print("Testing I/O module...")

    try:
        from modules import _iof

        # Test directory operations
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            test_dir = temp_path / 'test_directory'

            # Test directory creation
            _iof.DirectoryManager.create_directory(test_dir)
            assert test_dir.exists()

            # Test file operations
            test_file = test_dir / 'test.txt'
            test_content = "Hello, World!"

            _iof.FileWriter.write_text_file(test_content, test_file)
            assert test_file.exists()

            read_content = _iof.FileReader.read_text_file(test_file)
            assert read_content == test_content

            # Test JSON operations
            json_file = test_dir / 'test.json'
            json_data = {'test': 'value', 'number': 42}

            import json
            with open(json_file, 'w') as f:
                json.dump(json_data, f)

            read_json = _iof.FileReader.read_json(json_file)
            assert read_json == json_data

            # Test filename generation
            filename = _iof.FilenameGenerator.create_32char_filename(
                '00000000000000000000000000000000',
                123
            )
            assert len(filename) == 32
            assert filename.endswith('123')

            # Test legacy functions
            working_dir = _iof.Working_DIR()
            assert isinstance(working_dir, str)

        print("✓ I/O module tests passed")
        return True

    except Exception as e:
        print(f"✗ I/O module tests failed: {e}")
        return False


def test_xml_module():
    """Test the XML generation module."""
    print("Testing XML module...")

    try:
        from modules import _xml

        # Test Choice creation
        choice1 = _xml.Choice.from_markdown("[ ] Wrong answer")
        assert choice1.text == "Wrong answer"
        assert choice1.is_correct == False

        choice2 = _xml.Choice.from_markdown("[x] Correct answer")
        assert choice2.text == "Correct answer"
        assert choice2.is_correct == True

        # Test XML generation
        generator = _xml.CheckboxProblemGenerator()
        choices = [choice1, choice2]

        xml_bytes = generator.generate_problem_xml(
            "Test Problem",
            "What is the correct answer?",
            choices
        )

        assert isinstance(xml_bytes, bytes)
        assert b'Test Problem' in xml_bytes
        assert b'What is the correct answer?' in xml_bytes
        assert b'Wrong answer' in xml_bytes
        assert b'Correct answer' in xml_bytes

        # Test legacy functions
        legacy_xml = _xml.Block_2(
            "Legacy Test",
            "Legacy Question",
            "[ ] Wrong",
            "[x] Right"
        )
        assert isinstance(legacy_xml, bytes)

        print("✓ XML module tests passed")
        return True

    except Exception as e:
        print(f"✗ XML module tests failed: {e}")
        return False


def test_library_module():
    """Test the library XML generation module."""
    print("Testing library module...")

    try:
        from modules import _lib

        # Test library metadata
        metadata = _lib.LibraryMetadata(
            display_name="Test Library",
            library="TestLib",
            org="TestOrg"
        )

        assert metadata.display_name == "Test Library"
        assert metadata.library == "TestLib"
        assert metadata.org == "TestOrg"

        # Test problem references
        references = _lib.ProblemReferenceGenerator.generate_problem_references(3)
        assert len(references) == 3
        assert all(len(ref.url_name) == 32 for ref in references)

        # Test XML generation
        generator = _lib.LibraryXMLGenerator()
        library_xml = generator.generate_library_xml(metadata, references)

        assert library_xml.tag == 'library'
        assert library_xml.get('display_name') == "Test Library"

        problem_elements = library_xml.findall('problem')
        assert len(problem_elements) == 3

        print("✓ Library module tests passed")
        return True

    except Exception as e:
        print(f"✗ Library module tests failed: {e}")
        return False


def test_parsing_module():
    """Test the parsing and conversion module."""
    print("Testing parsing module...")

    try:
        from modules import _par

        # Test markdown validation
        valid_markdown = """# Problem 1

## Question 1

[ ] Wrong answer

[x] Correct answer

===

"""

        result = _par.MarkdownValidator.validate_markdown_content(valid_markdown)
        assert result == _par.ValidationResult.SUCCESS

        # Test markdown to HTML conversion
        html_content = _par.MarkdownConverter.convert_to_html(valid_markdown)
        assert '<h1>Problem 1</h1>' in html_content
        assert '<h2>Question 1</h2>' in html_content

        # Test HTML parsing
        parser = _par.HTMLParser()
        problems = parser.parse_html_content(html_content)

        assert len(problems) == 1
        assert problems[0].display_name == "Problem 1"
        assert problems[0].question_text == "Question 1"
        assert len(problems[0].choices) == 2

        print("✓ Parsing module tests passed")
        return True

    except Exception as e:
        print(f"✗ Parsing module tests failed: {e}")
        return False


def test_cli_module():
    """Test the CLI module components."""
    print("Testing CLI module...")

    try:
        from modules import _cli

        # Test argument parser
        parser = _cli.ArgumentParser()

        # Test with valid arguments
        args = parser.parse_arguments(['test_lib'])
        assert args.library == 'test_lib'
        assert args.verbose == False
        assert args.quiet == False

        # Test with verbose flag
        args = parser.parse_arguments(['test_lib', '--verbose'])
        assert args.verbose == True

        # Test configuration validation
        try:
            _cli.CLIError("Test error")
            _cli.ValidationError("Test validation error")
        except:
            pass  # These are just exception classes

        print("✓ CLI module tests passed")
        return True

    except Exception as e:
        print(f"✗ CLI module tests failed: {e}")
        return False


def run_integration_test():
    """Run an integration test of the complete pipeline."""
    print("Running integration test...")

    try:
        from modules import _par, _iof

        # Create test markdown content
        test_markdown = """# Test Problem 1

## What is 2 + 2?

[ ] 3

[x] 4

[ ] 5

===

# Test Problem 2

## What is the capital of France?

[ ] London

[x] Paris

[ ] Berlin

===

"""

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Setup test directories
            input_dir = temp_path / 'input'
            output_dir = temp_path / 'output'
            library_dir = temp_path / 'library'
            problem_dir = library_dir / 'problem'

            for directory in [input_dir, output_dir, library_dir, problem_dir]:
                _iof.DirectoryManager.create_directory(directory)

            # Create test files
            markdown_file = input_dir / 'test.md'
            html_file = output_dir / 'test.html'
            xml_file = output_dir / 'test.xml'

            _iof.FileWriter.write_text_file(test_markdown, markdown_file)

            # Create test config
            config_data = {
                "INP_MARKDOWN": "test.md",
                "OUT_HTML": "test.html",
                "OUT_XML": "test.xml",
                "DISPLAY_NAME": "Test Library",
                "LIBRARY": "TestLib",
                "ORG": "TestOrg"
            }

            config_file = input_dir / 'config.json'
            import json
            with open(config_file, 'w') as f:
                json.dump(config_data, f)

            # Run the conversion pipeline
            pipeline = _par.ConversionPipeline(temp_path)
            success = pipeline.process_markdown_file(
                markdown_file,
                html_file,
                xml_file,
                problem_dir
            )

            assert success == True
            assert html_file.exists()
            assert xml_file.exists()

            # Check that problem files were created
            problem_files = list(problem_dir.glob('*.xml'))
            assert len(problem_files) == 2

        print("✓ Integration test passed")
        return True

    except Exception as e:
        print(f"✗ Integration test failed: {e}")
        return False


def main():
    """Run all tests."""
    print("Running lib-gen module tests...")
    print("=" * 50)

    tests = [
        test_constants,
        test_iof_module,
        test_xml_module,
        test_library_module,
        test_parsing_module,
        test_cli_module,
        run_integration_test
    ]

    passed = 0
    failed = 0

    for test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__} crashed: {e}")
            failed += 1
        print()

    print("=" * 50)
    print(f"Test Results: {passed} passed, {failed} failed")

    if failed == 0:
        print("🎉 All tests passed! The refactored modules are working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
