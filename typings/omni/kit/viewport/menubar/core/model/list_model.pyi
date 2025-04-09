from __future__ import annotations
import omni.kit.viewport.menubar.core.model.reset_button
from omni.kit.viewport.menubar.core.model.reset_button import ResetHelper
from omni import ui
import omni.ui._ui
__all__: list = ['SimpleListItem', 'SimpleListModel', 'ColorModel']
class ColorModel(SimpleListModel, omni.kit.viewport.menubar.core.model.reset_button.ResetHelper):
    """
    A simple color model with reset supported
    """
    def __init__(self, colors: typing.List[float], default: typing.Optional[typing.List[float]] = None, on_color_changed_fn: typing.Callable[[typing.List[float]], NoneType] = None):
        """
        
                Constructor.
        
                Args:
                    colors (List[float]): colors.
        
                Keyword Args:
                    default (default: Optional[List[float]]): Default color values, defaults to None.
                    on_color_changed_fn (Callable[[List[float]], None]): Callback when color changed, defaults to None.
                
        """
    def _on_item_value_changed(self, item: SimpleListItem):
        """
        Called when the sub model is changed
        """
    def begin_edit(self, item):
        """
        Called when the user starts editing. Reimplemented from the base class.
        """
    def destroy(self) -> None:
        """
        Release resources
        """
    def end_edit(self, item):
        """
        Called when the user finishes editing. Reimplemented from the base class.
        """
    def get_default(self) -> typing.List[float]:
        """
        Get default colors
        """
    def get_value(self) -> typing.List[float]:
        """
        Get current colors
        """
    def restore_default(self) -> None:
        """
        Restore default colors
        """
    @property
    def colors(self) -> typing.List[float]:
        """
        Colors
        """
    @colors.setter
    def colors(self, values: typing.List[float]) -> None:
        ...
class SimpleListItem(omni.ui._ui.AbstractItem):
    """
    A single item in list model
    """
    def __init__(self, value: typing.Union[float, int, str, omni.ui._ui.AbstractValueModel], text: typing.Optional[str] = None):
        """
        
                Constructor.
        
                Args:
                    value (Union[float, int, str, ui.AbstractValueModel]): Item value.
        
                Keyword Args:
                    text (Optional[str]): Item text, defaults to None means using value.
                
        """
    def __repr__(self):
        ...
class SimpleListModel(omni.ui._ui.AbstractItemModel):
    """
    A simple data model contains list of values
    """
    def __init__(self, values: typing.List[float], texts: typing.Optional[typing.List[str]] = None):
        """
        
                Constructor.
        
                Args:
                    values (List[float]): Item values.
        
                Keyword Args:
                    texts (Optional[List[str]]): Item texts, defaults to None means using values.
                
        """
    def _on_item_value_changed(self, item: SimpleListItem):
        ...
    def _on_value_changed(self, item: SimpleListItem):
        """
        Called when the sub model is changed
        """
    def destroy(self) -> None:
        """
        Release resources
        """
    def get_item_children(self, item: typing.Optional[omni.ui._ui.AbstractItem] = None) -> typing.List[omni.ui._ui.AbstractItem]:
        """
        Returns all the children when the widget asks it.
        """
    def get_item_value_model(self, item: SimpleListItem, column_id: int):
        ...
    def get_item_value_model_count(self) -> int:
        """
        The number of columns
        """
