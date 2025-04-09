from __future__ import annotations
import carb as carb
from functools import partial
import omni.kit.widget.searchfield.searchword
from omni.kit.widget.searchfield.searchword import SearchWordButton
from omni.kit.widget.searchfield.suggest_window import SuggestWindow
from omni import ui
import omni.ui._ui
import typing
__all__ = ['SearchField', 'SearchWordButton', 'SuggestWindow', 'UI_STYLE', 'carb', 'partial', 'ui']
class SearchField:
    """
    
        Represents a search field where users can input search words and receive suggestions.
        
    """
    CLOSE_IMAGE_SIZE: typing.ClassVar[int] = 12
    SEARCH_IMAGE_SIZE: typing.ClassVar[int] = 16
    def __init__(self, width: typing.Optional[omni.ui._ui.Length] = None, height: typing.Optional[omni.ui._ui.Length] = ..., on_search_fn: typing.Callable[[typing.Optional[typing.List[str]]], NoneType] = None, subscribe_edit_changed: bool = False, show_tokens: bool = True, style: typing.Dict = None, suggestions: typing.Optional[typing.List[str]] = None, max_suggestions: int = 10, separator = ' '):
        """
        
                Construct a search field.
        
                Keyword Args:
                    width (Optional[ui.Length]): Widget width. Default None, means auto.
                    height (Optional[ui.Length]): Widget height. Default ui.Pixel(26). Use None for auto.
                    on_search_fn (Callable[[Optional[List[str]]], None]): Function called to do searching.
                    subscribe_edit_changed (bool): True to retrieve on_search_fn called when input changed. Default False only retrieve on_search_fn called when input ended.
                    show_tokens (bool): Default True to show tokens if end edit. Do nothing if False.
                    style (Dict): Widget additional style. Default None, means using default style.
                    suggestions (Optional[List[str]]): Show suggestion list when input search words. Default None means not supported.
                    max_suggestions (int): Max number of suggestions to show at same time.
                    separator (Optional[str]): Separator to break the search string into multiple words. None means no separate. Defaults to " ".
        
                Properties:
                    visible (bool): Widget visibility.
                    enabled (bool): Enable/Disable widget.
                    search_words (Optional[List[str]]): Search words.
                    suggestions (Optional[List[str]]): Suggestions.
                    max_suggestions (int): Maximum number of suggestions.
                    text (str): Text in the search field.
                
        """
    def _build_search_words(self):
        ...
    def _build_ui(self):
        ...
    def _convert_words_to_string(self) -> None:
        ...
    def _get_search_words(self) -> typing.List[str]:
        ...
    def _hide_search_word(self, index: int, widget: omni.kit.widget.searchfield.searchword.SearchWordButton) -> None:
        ...
    def _notify(self, search_words) -> bool:
        ...
    def _on_begin_edit(self, model):
        ...
    def _on_clear_clicked(self) -> None:
        ...
    def _on_double_click(self):
        ...
    def _on_end_edit(self, model: omni.ui._ui.AbstractValueModel) -> None:
        ...
    def _on_text_edit(self, model: omni.ui._ui.AbstractValueModel) -> None:
        ...
    def _set_in_searching(self, in_searching: bool) -> None:
        ...
    def _show_suggest_window(self) -> None:
        ...
    def clear(self):
        """
        clear search words
        """
    def destroy(self):
        """
        
                Clean resources.
                
        """
    def set_filter(self, filter_cls):
        """
        
                Set filter.
        
                :meta private:
                
        """
    @property
    def enabled(self) -> bool:
        """
        
                Widget enabled/disabled
                
        """
    @enabled.setter
    def enabled(self, value):
        ...
    @property
    def max_suggestions(self) -> int:
        """
        Max number of suggestion words appeared
        """
    @max_suggestions.setter
    def max_suggestions(self, count: int) -> None:
        ...
    @property
    def search_words(self) -> typing.Optional[typing.List[str]]:
        """
        
                Current words appeared in the search field.
                
        """
    @search_words.setter
    def search_words(self, words: typing.List[str]) -> None:
        ...
    @property
    def suggestions(self) -> typing.Optional[typing.List[str]]:
        """
        
                Suggestion words to show when input in search field
                
        """
    @suggestions.setter
    def suggestions(self, words: typing.List[str]) -> None:
        ...
    @property
    def text(self) -> str:
        """
        
                Text currently in search field
                
        """
    @text.setter
    def text(self, text: str) -> None:
        ...
    @property
    def visible(self) -> bool:
        """
        
                Widget visibility
                
        """
    @visible.setter
    def visible(self, value):
        ...
UI_STYLE: dict  # value = {'SearchField': {'background_color': 0, 'border_radius': 0, 'border_width': 0, 'background_selected_color': 4283650900}, 'SearchField.Frame': {'background_color': 'shade:4280492319;light=4283650900', 'border_radius': 0.0, 'border_color': 0, 'border_width': 2}, 'SearchField.Frame:selected': {'background_color': 'shade:4280492319;light=4283650900', 'border_radius': 0, 'border_color': 'shade:4291401548', 'border_width': 2}, 'SearchField.Hint': {'color': 'shade:4283058762;light=4292269782'}, 'SearchField.Search': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.searchfield-1.1.8+d02c707b/icons/search.svg', 'color': 'shade:4283058762;light=4292269782'}, 'SearchField.Clear': {'background_color': 0, 'padding': 4}, 'SearchField.Clear:hovered': {'background_color': 'shade:4282006074;light=4290295992'}, 'SearchField.Clear.Image': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.searchfield-1.1.8+d02c707b/icons/close.svg', 'color': 'shade:4286940549'}, 'SearchField.Word': {'background_color': 'shade:4292465852'}, 'SearchField.Word.Label': {'color': 'shade:4287460877'}, 'SearchField.Word.Button': {'background_color': 0, 'padding': 2}, 'SearchField.Word.Button.Image': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.searchfield-1.1.8+d02c707b/icons/close.svg', 'color': 'shade:4287460877'}, 'TreeView.Frame': {'background_color': 3710066975, 'border_color': 2861205367, 'border_width': 0.5}, 'Tooltips.Spacer': {'background_color': 0, 'color': 0, 'alignment': <Alignment.LEFT: 2>, 'padding': 0, 'margin': 0}, 'Tooltips.Item': {'background_color': 0, 'padding': 4}, 'Tooltips.Item:hovered': {'background_color': 4287268727}, 'Tooltips.Item:checked': {'background_color': 4287268727}, 'Tooltips.Item.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT: 2>}}
