from __future__ import annotations
import abc as abc
from omni.kit.widget.stage.stage_item import StageItem
from omni import ui
import pxr.Sdf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
import typing
__all__: list = ['AbstractStageColumnDelegate', 'StageColumnItem']
class AbstractStageColumnDelegate:
    """
    
        An abstract object that is used to build stage widget columns.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'build_widget'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def build_header(self, **kwargs):
        """
        
                Builds the header widget. If the column is sortable, stage widget will build a background rectangle with hover
                state to indicate users if the column is sortable, so that all columns delegates don't need to build that by
                themselves. This can be overriden to build customized widgets as column header.
                
        """
    def build_widget(self, item: StageColumnItem, **kwargs):
        """
        
                Builds the widget for the given path. Works inside a ui.Frame in async mode.
                Once the widget is created, it will replace the content of the frame. It allows to await something for a while
                and creates the widget when the result is available.
        
                Args:
                    item (StageColumnItem): DEPRECATED. It includes the non-cached simple prim
                        information. It's better to use keyword argument `stage_item` instead, which
                        provides cached rich information about the prim influened by this column.
        
                Keyword Args:
                    stage_model (StageModel): The instance of current StageModel.
                    stage_item (StageItem): The current StageItem to build. It's possible that
                        stage_item is None when TreeView enabled display of root node.
                
        """
    def destroy(self):
        """
        Place to release resources.
        """
    def on_header_hovered(self, hovered: bool):
        """
        
                Callback when header area is hovered.
        
                Args:
                    hovered (bool): Whether the header area is hovered.
                
        """
    def on_stage_items_destroyed(self, items: typing.List[omni.kit.widget.stage.stage_item.StageItem]):
        """
        
                Called when stage items are destroyed to give the opportunity for delegates to release corresponding resources.
        
                Args:
                    items (List[StageItem]): Stage items to be destroyed.
                
        """
    @property
    def initial_width(self) -> typing.Union[omni.ui._ui.Pixel, omni.ui._ui.Fraction, omni.ui._ui.Percent]:
        """
        
                The initial width of the column.
        
                Returns:
                    Union[ui.Pixel, ui.Fraction, ui.Percent]: Column width
                
        """
    @property
    def minimum_width(self) -> typing.Union[omni.ui._ui.Pixel, omni.ui._ui.Fraction, omni.ui._ui.Percent]:
        """
        
                The minimum width of the column.
        
                Returns:
                    Union[ui.Pixel, ui.Fraction, ui.Percent]: Minimum column width
                
        """
    @property
    def order(self) -> int:
        """
        
                The order to sort columns. The columns are sorted in ascending order from left to right of the stage widget.
                So the smaller the order is, the closer the column is to the left of the stage widget.
        
                Returns:
                    int: sort order
                
        """
    @property
    def resizable(self):
        """
        
                Whether the column is resizable. If it's True, the column can be resized by dragging its border lines. If it's
                False, the column can't be resized. The default value is True.
        
                Returns:
                    bool: resizable or not
                
        """
    @property
    def sortable(self) -> bool:
        """
        
                Whether this column is sortable or not. When it's True, stage widget will build header widget with hover and
                selection state to tell user it's sortable. This is only used to indicate to users that this column is sortable
                from the UX point of view.
        
                Returns:
                    bool: sortable or not
                
        """
class StageColumnItem:
    """
    
        A dataclass that manages information needed for building columns for a StageItem.
        It's not clear what data we need to pass to build_widget. Apart from path, there are potentially other information
        the column has. To keep the API unchanged over time, we pass in data as a struct. It also allows passing in custom
        data derived from this class.
        
    """
    def __init__(self, path: pxr.Sdf.Path, stage: pxr.Usd.Stage, enabled: bool, expanded: bool = True):
        """
        
                Constructor.
        
                Args:
                    path (Sdf.Path): Full path of the item
                    stage (Usd.Stage): USD Stage
                    enabled (bool): When false, the widget should be grayed out
        
                Keyword Args:
                    expanded (bool): Whether the item should be expanded.
                
        """
    @property
    def enabled(self) -> bool:
        """
        
                Whether the item is enabled.
        
                Returns:
                    bool: Enabled or not
                
        """
    @property
    def expanded(self) -> bool:
        """
        
                Whether the item is expanded.
        
                Returns:
                    bool: Expanded or not
                
        """
    @property
    def path(self) -> pxr.Sdf.Path:
        """
        
                The path of the item.
        
                Returns:
                    Sdf.Path: The path of the item.
                
        """
    @property
    def stage(self) -> pxr.Usd.Stage:
        """
        
                The stage that the item belongs to.
        
                Returns:
                    Usd.Stage: The stage that the item belongs to.
                
        """
