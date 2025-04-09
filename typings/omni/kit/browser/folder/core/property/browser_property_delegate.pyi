from __future__ import annotations
import abc as abc
from omni.kit.browser.folder.core.models.folder_browser_item import FileDetailItem
from omni import ui
import omni.ui._ui
import typing
__all__: list = ['BrowserPropertyDelegate']
class BrowserPropertyDelegate(abc.ABC):
    """
    Base class for item property delegates
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'accepted', 'build_widgets'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __del__(self):
        ...
    def __init__(self):
        ...
    def _build_checkbox(self, model: typing.Optional[omni.ui._ui.AbstractValueModel] = None) -> omni.ui._ui.CheckBox:
        ...
    def _build_combobox(self, text: str, *args, **kwargs) -> omni.ui._ui.ComboBox:
        ...
    def _build_float_drag(self, model: typing.Optional[omni.ui._ui.AbstractValueModel] = None, name = 'models') -> omni.ui._ui.FloatDrag:
        ...
    def _build_float_field(self, model: typing.Optional[omni.ui._ui.SimpleFloatModel] = None) -> omni.ui._ui.FloatField:
        ...
    def _build_float_slider(self, model: typing.Optional[omni.ui._ui.AbstractValueModel] = None, name = 'models') -> omni.ui._ui.FloatSlider:
        ...
    def _build_int_drag(self, model: typing.Optional[omni.ui._ui.AbstractValueModel] = None, name = 'models') -> omni.ui._ui.IntDrag:
        ...
    def _build_label(self, text: str, width: typing.Optional[omni.ui._ui.Length] = 160, alignment = ...) -> omni.ui._ui.Label:
        ...
    def _build_string_field(self, model: typing.Optional[omni.ui._ui.SimpleStringModel] = None, text: str = '') -> omni.ui._ui.StringField:
        ...
    def accepted(self, detail_items: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]) -> bool:
        """
        
                Check if detail item could be shown by this delegate.
                Args:
                    detail_items (List[FileDetailItem]): Detail item to be shown.
                
        """
    def build_widgets(self, detail_items: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]) -> None:
        """
        
                Build widgets to Show detail items.
                Args:
                    detail_item (List[FileDetailItem]): Detail item to be shown.
                
        """
    def destroy(self):
        ...
HORIZONTAL_SPACING: int = 4
LABEL_HEIGHT: int = 18
LABEL_WIDTH: int = 160
