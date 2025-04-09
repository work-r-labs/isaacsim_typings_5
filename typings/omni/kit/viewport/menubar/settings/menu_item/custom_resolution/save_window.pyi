from __future__ import annotations
from omni import ui
import omni.ui._ui
import typing
__all__ = ['SAVE_WINDOW_STYLE', 'SaveWindow', 'ui']
class SaveWindow(omni.ui._ui.Window):
    """
    
        Window to save custom resolution.
        
    """
    PADDING: typing.ClassVar[int] = 8
    def _SaveWindow__build_ui(self):
        ...
    def _SaveWindow__on_cancel(self) -> None:
        ...
    def _SaveWindow__on_save(self) -> None:
        ...
    def __del__(self):
        ...
    def __init__(self, resolution: typing.Tuple[int, int], on_save_fn: typing.Callable[[str, typing.Tuple[int, int]], bool]):
        ...
    def _build_buttons(self):
        ...
    def _build_input(self):
        ...
    def _build_titlebar(self):
        ...
SAVE_WINDOW_STYLE: dict  # value = {'Window': {'secondary_background_color': 0}, 'Titlebar.Background': {'background_color': 'save_background'}, 'Input.Hint': {'color': 'input_hint'}, 'Image::close': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.settings-107.0.3+d02c707b/data/icons/close.svg'}, 'Button': {'background_color': 'save_background'}}
