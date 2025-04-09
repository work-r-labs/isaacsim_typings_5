from __future__ import annotations
import carb as carb
from omni import ui
import pathlib
__all__ = ['ICON_PATH', 'SearchWordButton', 'UI_STYLE', 'carb', 'ui']
class SearchWordButton:
    """
    
        Represents a search word widget, combined with a label to show the word and a close button to remove it.
        Args:
            word (str): String of word.
        Keyword args:
            on_close_fn (callable): Function called when close button clicked. Function signure:
                void on_close_fn(widget: SearchWordButton) 
        
    """
    def __init__(self, word: str, on_close_fn: callable = None):
        ...
    @property
    def visible(self) -> None:
        """
        
                Widget visibility
                
        """
    @visible.setter
    def visible(self, value: bool) -> None:
        ...
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.searchfield-1.1.8+d02c707b/icons')
UI_STYLE: dict  # value = {'SearchField': {'background_color': 0, 'border_radius': 0, 'border_width': 0, 'background_selected_color': 4283650900}, 'SearchField.Frame': {'background_color': 'shade:4280492319;light=4283650900', 'border_radius': 0.0, 'border_color': 0, 'border_width': 2}, 'SearchField.Frame:selected': {'background_color': 'shade:4280492319;light=4283650900', 'border_radius': 0, 'border_color': 'shade:4291401548', 'border_width': 2}, 'SearchField.Hint': {'color': 'shade:4283058762;light=4292269782'}, 'SearchField.Search': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.searchfield-1.1.8+d02c707b/icons/search.svg', 'color': 'shade:4283058762;light=4292269782'}, 'SearchField.Clear': {'background_color': 0, 'padding': 4}, 'SearchField.Clear:hovered': {'background_color': 'shade:4282006074;light=4290295992'}, 'SearchField.Clear.Image': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.searchfield-1.1.8+d02c707b/icons/close.svg', 'color': 'shade:4286940549'}, 'SearchField.Word': {'background_color': 'shade:4292465852'}, 'SearchField.Word.Label': {'color': 'shade:4287460877'}, 'SearchField.Word.Button': {'background_color': 0, 'padding': 2}, 'SearchField.Word.Button.Image': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.searchfield-1.1.8+d02c707b/icons/close.svg', 'color': 'shade:4287460877'}, 'TreeView.Frame': {'background_color': 3710066975, 'border_color': 2861205367, 'border_width': 0.5}, 'Tooltips.Spacer': {'background_color': 0, 'color': 0, 'alignment': <Alignment.LEFT: 2>, 'padding': 0, 'margin': 0}, 'Tooltips.Item': {'background_color': 0, 'padding': 4}, 'Tooltips.Item:hovered': {'background_color': 4287268727}, 'Tooltips.Item:checked': {'background_color': 4287268727}, 'Tooltips.Item.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT: 2>}}
