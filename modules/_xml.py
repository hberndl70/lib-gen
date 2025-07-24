"""
XML generation module for edX checkbox problems.

This module provides functionality to generate XML structures for edX checkbox
problems with variable numbers of answer choices. It eliminates code duplication
by using a unified approach for generating XML blocks.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from lxml import etree
from lxml.builder import E
import logging

from . import _con

logger = logging.getLogger(__name__)


class XMLGenerationError(Exception):
    """Custom exception for XML generation errors."""
    pass


@dataclass
class Choice:
    """Represents a single choice in a checkbox problem."""
    text: str
    is_correct: bool

    @classmethod
    def from_markdown(cls, markdown_text: str) -> 'Choice':
        """
        Create a Choice from markdown checkbox format.

        Args:
            markdown_text: Text like "[ ] Wrong answer" or "[x] Correct answer"

        Returns:
            Choice object

        Raises:
            XMLGenerationError: If markdown format is invalid
        """
        if not markdown_text.startswith(('[x]', '[ ]')):
            raise XMLGenerationError(f"Invalid checkbox format: {markdown_text}")

        is_correct = markdown_text.startswith('[x]')
        text = markdown_text[4:].strip()  # Remove checkbox marker and whitespace

        return cls(text=text, is_correct=is_correct)


@dataclass
class ProblemConfiguration:
    """Configuration settings for checkbox problems."""
    max_attempts: str = _con.DEFAULT_MAX_ATTEMPTS
    weight: str = _con.DEFAULT_WEIGHT
    show_reset_button: str = _con.DEFAULT_SHOW_RESET_BUTTON
    show_answer: str = _con.DEFAULT_SHOW_ANSWER
    markdown_value: str = _con.DEFAULT_MARKDOWN_VALUE
    description: str = _con.DEFAULT_DESCRIPTION


class XMLElementBuilder:
    """Utility class for building XML elements with proper formatting."""

    @staticmethod
    def create_label_element(label_text: str) -> etree._Element:
        """
        Create a label element with paragraph formatting.

        Args:
            label_text: Text content for the label

        Returns:
            XML element for the label
        """
        label_html = f"{_con.PARAGRAPH_OPEN_TAG}{label_text}{_con.PARAGRAPH_CLOSE_TAG}"
        return etree.XML(label_html)

    @staticmethod
    def create_choice_element(choice: Choice) -> etree._Element:
        """
        Create a choice element from a Choice object.

        Args:
            choice: Choice object containing text and correctness

        Returns:
            XML element for the choice
        """
        correct_value = 'true' if choice.is_correct else 'false'
        choice_html = f'{_con.CHOICE_OPEN_TAG}correct="{correct_value}">{choice.text}{_con.CHOICE_CLOSE_TAG}'
        return etree.XML(choice_html)


class CheckboxProblemGenerator:
    """Main class for generating checkbox problem XML."""

    def __init__(self, config: Optional[ProblemConfiguration] = None):
        """
        Initialize the generator with configuration.

        Args:
            config: Problem configuration (uses defaults if None)
        """
        self.config = config or ProblemConfiguration()

    def generate_problem_xml(self, display_name: str, label_text: str,
                           choices: List[Choice]) -> bytes:
        """
        Generate complete XML for a checkbox problem.

        Args:
            display_name: Display name for the problem
            label_text: Question text/label
            choices: List of Choice objects

        Returns:
            XML bytes for the problem

        Raises:
            XMLGenerationError: If generation fails or validation errors occur
        """
        self._validate_inputs(display_name, label_text, choices)

        try:
            # Create the main problem element
            problem_element = self._create_problem_element(display_name)

            # Create the choice response structure
            choice_response = self._create_choice_response(label_text, choices)
            problem_element.append(choice_response)

            # Convert to XML bytes with pretty printing
            xml_bytes = etree.tostring(problem_element, pretty_print=True, encoding='utf-8')

            logger.info(f"Generated XML for problem: {display_name}")
            return xml_bytes

        except Exception as e:
            raise XMLGenerationError(f"Failed to generate XML for problem '{display_name}': {e}")

    def _validate_inputs(self, display_name: str, label_text: str, choices: List[Choice]) -> None:
        """
        Validate inputs for XML generation.

        Args:
            display_name: Display name to validate
            label_text: Label text to validate
            choices: Choices to validate

        Raises:
            XMLGenerationError: If validation fails
        """
        if not display_name.strip():
            raise XMLGenerationError("Display name cannot be empty")

        if not label_text.strip():
            raise XMLGenerationError("Label text cannot be empty")

        if not choices:
            raise XMLGenerationError("At least one choice is required")

        if len(choices) < 2:
            raise XMLGenerationError("At least two choices are required for a meaningful problem")

        if len(choices) > 8:
            logger.warning(f"Problem has {len(choices)} choices, which may be too many for good UX")

        # Check if at least one correct answer exists
        if not any(choice.is_correct for choice in choices):
            logger.warning("No correct answers found in choices")

    def _create_problem_element(self, display_name: str) -> etree._Element:
        """
        Create the main problem element with attributes.

        Args:
            display_name: Display name for the problem

        Returns:
            Problem XML element
        """
        return E.problem(
            **{
                'display_name': display_name,
                'markdown': self.config.markdown_value,
                'max_attempts': self.config.max_attempts,
                'show_reset_button': self.config.show_reset_button,
                'showanswer': self.config.show_answer,
                'weight': self.config.weight
            }
        )

    def _create_choice_response(self, label_text: str, choices: List[Choice]) -> etree._Element:
        """
        Create the choice response element structure.

        Args:
            label_text: Question text/label
            choices: List of Choice objects

        Returns:
            Choice response XML element
        """
        # Create label element
        label_element = XMLElementBuilder.create_label_element(label_text)

        # Create description element
        description_element = E.description(self.config.description)

        # Create choice elements
        choice_elements = [XMLElementBuilder.create_choice_element(choice) for choice in choices]

        # Create checkbox group with all choices
        checkbox_group = E.checkboxgroup(*choice_elements)

        # Create the complete choice response
        choice_response = E.choiceresponse(
            label_element,
            description_element,
            checkbox_group
        )

        return choice_response


class LegacyXMLGenerator:
    """
    Legacy XML generator that maintains compatibility with the old API.

    This class provides the old Block_X functions for backward compatibility
    while using the new improved implementation internally.
    """

    def __init__(self):
        self.generator = CheckboxProblemGenerator()

    def _parse_legacy_choices(self, *choice_texts: str) -> List[Choice]:
        """
        Parse legacy choice texts into Choice objects.

        Args:
            *choice_texts: Variable number of choice text strings

        Returns:
            List of Choice objects
        """
        choices = []
        for choice_text in choice_texts:
            if choice_text:  # Skip empty strings
                choices.append(Choice.from_markdown(choice_text))
        return choices

    def generate_block(self, display_name: str, label_text: str, *choice_texts: str) -> bytes:
        """
        Generate XML block with variable number of choices (legacy API).

        Args:
            display_name: Display name for the problem
            label_text: Question text/label
            *choice_texts: Variable number of choice texts in markdown format

        Returns:
            XML bytes for the problem
        """
        choices = self._parse_legacy_choices(*choice_texts)
        return self.generator.generate_problem_xml(display_name, label_text, choices)


# =============================================================================
# Legacy Functions (maintaining backward compatibility)
# =============================================================================

# Create a global instance for legacy functions
_legacy_generator = LegacyXMLGenerator()

def Block_2(display_name: str, label_text: str, choice1: str, choice2: str) -> bytes:
    """Generate 2-choice problem XML (legacy function)."""
    return _legacy_generator.generate_block(display_name, label_text, choice1, choice2)

def Block_3(display_name: str, label_text: str, choice1: str, choice2: str, choice3: str) -> bytes:
    """Generate 3-choice problem XML (legacy function)."""
    return _legacy_generator.generate_block(display_name, label_text, choice1, choice2, choice3)

def Block_4(display_name: str, label_text: str, choice1: str, choice2: str,
           choice3: str, choice4: str) -> bytes:
    """Generate 4-choice problem XML (legacy function)."""
    return _legacy_generator.generate_block(display_name, label_text, choice1, choice2, choice3, choice4)

def Block_5(display_name: str, label_text: str, choice1: str, choice2: str,
           choice3: str, choice4: str, choice5: str) -> bytes:
    """Generate 5-choice problem XML (legacy function)."""
    return _legacy_generator.generate_block(display_name, label_text, choice1, choice2, choice3, choice4, choice5)

def Block_6(display_name: str, label_text: str, choice1: str, choice2: str,
           choice3: str, choice4: str, choice5: str, choice6: str) -> bytes:
    """Generate 6-choice problem XML (legacy function)."""
    return _legacy_generator.generate_block(display_name, label_text, choice1, choice2, choice3, choice4, choice5, choice6)

def Block_7(display_name: str, label_text: str, choice1: str, choice2: str,
           choice3: str, choice4: str, choice5: str, choice6: str, choice7: str) -> bytes:
    """Generate 7-choice problem XML (legacy function)."""
    return _legacy_generator.generate_block(display_name, label_text, choice1, choice2, choice3, choice4, choice5, choice6, choice7)

def Block_8(display_name: str, label_text: str, choice1: str, choice2: str,
           choice3: str, choice4: str, choice5: str, choice6: str, choice7: str, choice8: str) -> bytes:
    """Generate 8-choice problem XML (legacy function)."""
    return _legacy_generator.generate_block(display_name, label_text, choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8)


# =============================================================================
# Utility Functions
# =============================================================================

def Display_Name(value: str) -> Dict[str, str]:
    """Create display_name attribute dict (legacy function)."""
    return {'display_name': value}

def Markdown(value: str) -> Dict[str, str]:
    """Create markdown attribute dict (legacy function)."""
    return {'markdown': value}

def Max_Attempts(value: str) -> Dict[str, str]:
    """Create max_attempts attribute dict (legacy function)."""
    return {'max_attempts': value}

def Show_Reset_Button(value: str) -> Dict[str, str]:
    """Create show_reset_button attribute dict (legacy function)."""
    return {'show_reset_button': value}

def ShowAnswer(value: str) -> Dict[str, str]:
    """Create showanswer attribute dict (legacy function)."""
    return {'showanswer': value}

def Weight(value: str) -> Dict[str, str]:
    """Create weight attribute dict (legacy function)."""
    return {'weight': value}

def Correct_Tag(value: str) -> str:
    """Create correct attribute string (legacy function)."""
    return f'correct="{value}">'

def Check_RoW(choice_text: str) -> str:
    """Check if choice is correct (legacy function)."""
    return 'true' if choice_text.startswith('[x]') else 'false'

def Build_Label(label_text: str) -> str:
    """Build label HTML (legacy function)."""
    return f"{_con.PARAGRAPH_OPEN_TAG}{label_text}{_con.PARAGRAPH_CLOSE_TAG}"

def Build_Choice(choice_text: str, correct_value: str) -> str:
    """Build choice HTML (legacy function)."""
    return f'{_con.CHOICE_OPEN_TAG}correct="{correct_value}">{choice_text}{_con.CHOICE_CLOSE_TAG}'
