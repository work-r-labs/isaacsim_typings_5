from __future__ import annotations
import asyncio as asyncio
from functools import partial
import omni as omni
from omni import ui
__all__ = ['MAX_SUGGESTIONS', 'SuggestItem', 'SuggestModel', 'SuggestWindow', 'UI_STYLE', 'asyncio', 'omni', 'partial', 'ui']
class SuggestItem(omni.ui._ui.AbstractItem):
    """
    Item for suggest model
    """
    def __init__(self, text: str):
        ...
class SuggestModel(omni.ui._ui.AbstractItemModel):
    """
    Item model to show in suggest treeview
    """
    suggestions: typing.List[str]
    def __init__(self, suggestions: typing.List[str] = list(), max_suggestions = 10):
        ...
    def get_item_children(self, item: typing.Optional[omni.ui._ui.AbstractItem] = None) -> typing.List[omni.kit.widget.searchfield.suggest_window.SuggestItem]:
        """
        Returns all the children when the widget asks it.
        """
    def get_item_value_model(self, item: SuggestItem, column_id: int) -> omni.ui._ui.SimpleStringModel:
        ...
    def get_item_value_model_count(self, item: SuggestItem) -> int:
        """
        The number of columns
        """
class SuggestWindow(omni.ui._ui.Window):
    """
    
        A suggest window to show a input field (instead of search field) and a treeview (show suggestions)
        
    """
    max_suggestions: int
    suggestions: typing.List[str]
    def _SuggestWindow__build_suggestions(self):
        ...
    def __init__(self, search_field: omni.ui._ui.StringField, suggestions: typing.List[str] = list(), max_suggestions = 10, on_end_edit_fn: typing.Callable = None, on_double_clicked_fn: typing.Callable = None):
        ...
    def _build_suggest_list(self):
        ...
    def _build_ui(self):
        ...
    def _on_double_click(self):
        ...
    def _on_end_edit(self, model: omni.ui._ui.AbstractValueModel) -> None:
        ...
    def _on_suggestion_pressed(self, text: str) -> None:
        ...
    def _on_text_edit(self, model: omni.ui._ui.AbstractValueModel) -> None:
        ...
    def _on_visibility_changed(self, visible: bool) -> None:
        ...
    def destroy(self):
        ...
MAX_SUGGESTIONS: int = 10
UI_STYLE: dict  # value = {'SearchField': {'background_color': 0, 'border_radius': 0, 'border_width': 0, 'background_selected_color': 4283650900}, 'SearchField.Frame': {'background_color': 'shade:4280492319;light=4283650900', 'border_radius': 0.0, 'border_color': 0, 'border_width': 2}, 'SearchField.Frame:selected': {'background_color': 'shade:4280492319;light=4283650900', 'border_radius': 0, 'border_color': 'shade:4291401548', 'border_width': 2}, 'SearchField.Hint': {'color': 'shade:4283058762;light=4292269782'}, 'SearchField.Search': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.searchfield-1.1.8+d02c707b/icons/search.svg', 'color': 'shade:4283058762;light=4292269782'}, 'SearchField.Clear': {'background_color': 0, 'padding': 4}, 'SearchField.Clear:hovered': {'background_color': 'shade:4282006074;light=4290295992'}, 'SearchField.Clear.Image': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.searchfield-1.1.8+d02c707b/icons/close.svg', 'color': 'shade:4286940549'}, 'SearchField.Word': {'background_color': 'shade:4292465852'}, 'SearchField.Word.Label': {'color': 'shade:4287460877'}, 'SearchField.Word.Button': {'background_color': 0, 'padding': 2}, 'SearchField.Word.Button.Image': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.searchfield-1.1.8+d02c707b/icons/close.svg', 'color': 'shade:4287460877'}, 'TreeView.Frame': {'background_color': 3710066975, 'border_color': 2861205367, 'border_width': 0.5}, 'Tooltips.Spacer': {'background_color': 0, 'color': 0, 'alignment': <Alignment.LEFT: 2>, 'padding': 0, 'margin': 0}, 'Tooltips.Item': {'background_color': 0, 'padding': 4}, 'Tooltips.Item:hovered': {'background_color': 4287268727}, 'Tooltips.Item:checked': {'background_color': 4287268727}, 'Tooltips.Item.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT: 2>}}
