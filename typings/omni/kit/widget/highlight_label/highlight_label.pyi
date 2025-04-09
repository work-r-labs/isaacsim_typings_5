"""
This module provides the HighlightLabel widget class for creating labels with highlighted text selections.
"""
from __future__ import annotations
import carb as carb
import math as math
from omni import ui
import omni.ui._ui
__all__ = ['HighlightLabel', 'UI_STYLE', 'carb', 'math', 'split_selection', 'ui']
class HighlightLabel:
    """
    Represents a label widget that can show highlighted words.
    
        Args:
            text (str): The text content of the label.
            highlight (Optional[str]): The word within `text` to be highlighted.
            match_case (bool): If `True`, matching is case-sensitive. Defaults to `False`.
            width (ui.Length): The width of the widget. Defaults to `ui.Fraction(1)`.
            height (ui.Length): The height of the widget. Defaults to `ui.Fraction(1)`.
            label_width (int): The width used for ui.Label.
            style (Dict): Custom styling for the widget.
    
        Keyword Args:
            alignment (Optional[ui.Alignment]): Aligns the content within the label. Default is `ui.Alignment.LEFT_CENTER`.
            name (Optional[str]): The name of the widget. Used for identifying widgets.
            style_type_name_override (Optional[str]): Overrides the default style type name for customization.
    """
    def __getattr__(self, attr):
        ...
    def __init__(self, text: str, highlight: typing.Optional[str] = None, match_case: bool = False, width: omni.ui._ui.Length = ..., height: omni.ui._ui.Length = ..., label_width: int | omni.ui._ui.Length = 0, style: typing.Dict = None, **kwargs):
        """
        Initializes the highlight label widget.
        """
    def _build_ui(self):
        ...
    @property
    def highlight(self) -> typing.Optional[str]:
        """
        Gets the highlight text of the label.
        
                Returns:
                    Optional[str]: The current highlight text of the label.
        """
    @highlight.setter
    def highlight(self, value: typing.Optional[str]) -> None:
        """
        Sets the highlight text of the label and rebuilds the UI.
        
                Args:
                    value (Optional[str]): The highlight text to set.
        """
    @property
    def hightlight(self) -> typing.Optional[str]:
        """
        Gets the highlight text of the label.
        
                Returns:
                    Optional[str]: The current highlight text of the label.
        """
    @property
    def text(self) -> str:
        """
        Gets the text of the label.
        
                Returns:
                    str: The current text of the label.
        """
    @text.setter
    def text(self, value: str) -> None:
        """
        Sets the text of the label and rebuilds the UI.
        
                Args:
                    value (str): The text to set.
        """
    @property
    def visible(self) -> None:
        """
        Gets the visibility of the widget.
        """
    @visible.setter
    def visible(self, value: bool) -> None:
        """
        Sets the visibility of the widget.
        
                Args:
                    value (bool): The visibility state to set.
        """
    @property
    def widget(self) -> typing.Optional[omni.ui._ui.HStack]:
        """
        Gets the widget's container.
        """
def split_selection(text, selection, match_case: bool = False):
    """
    
        Splits the provided text into a list of substrings to facilitate drawing segments of selected text.
    
        The resulting list alternates between unselected and selected text, starting with an unselected portion. If the entire text is selected, it returns a list starting with an empty string followed by the entire text.
    
        Args:
            text (str): The text to split based on the selection.
            selection (str): The substring to search for within `text`.
            match_case (bool, optional): If True, the search is case-sensitive; otherwise, it's case-insensitive. Defaults to False.
    
        Returns:
            list of str: A list containing the split parts of the text with the selection highlighted.
    
        Examples:
            - split_selection("helloworld", "o") -> ["hell", "o", "w", "o", "rld"]
            - split_selection("helloworld", "helloworld") -> ["", "helloworld"]
    """
UI_STYLE: dict  # value = {'HighlightLabel::highlight': {'color': 'highlight_highlight'}}
