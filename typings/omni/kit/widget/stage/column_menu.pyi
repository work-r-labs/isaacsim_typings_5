from __future__ import annotations
from omni.kit.widget.stage.abstract_stage_column_delegate import AbstractStageColumnDelegate
import omni.kit.widget.stage.event
from omni.kit.widget.stage.event import Event
from omni.kit.widget.stage.event import EventSubscription
from omni import ui
import omni.ui._ui
import weakref as weakref
__all__: list = ['ColumnMenuItem', 'ColumnMenuModel', 'ColumnMenuDelegate']
class ColumnMenuDelegate(omni.ui._ui.AbstractItemDelegate):
    """
    
        Delegate is the representation layer. TreeView calls the methods
        of the delegate to create custom widgets for each item.
        
    """
    @staticmethod
    def _get_styles():
        ...
    def __init__(self):
        ...
    def _on_mouse_hovered(self, hovered: bool, container: omni.ui._ui.HStack) -> None:
        ...
    def _on_mouse_pressed(self, column_model: ColumnMenuModel) -> None:
        ...
    def _on_mouse_released(self, item_model: omni.ui._ui.SimpleBoolModel, column_model: ColumnMenuModel) -> None:
        ...
    def build_branch(self, model, item, column_id, level, expanded):
        """
        Create a branch widget that opens or closes subtree
        """
    def build_header(self, column_id):
        ...
    def build_widget(self, model: ColumnMenuModel, item: ColumnMenuItem, column_id, level, expanded):
        """
        Create a widget per column per item
        """
    def destroy(self):
        ...
class ColumnMenuItem(omni.ui._ui.AbstractItem):
    """
    Single item of the model
    """
    def __init__(self, model, text, checked):
        ...
    def __repr__(self):
        ...
    def _on_checked_changed(self, model):
        ...
class ColumnMenuModel(omni.ui._ui.AbstractItemModel):
    """
    
        Represents the model for available columns.
        
    """
    def __init__(self, enabled: typing.Optional[typing.List[str]] = None, accepted: typing.Optional[typing.List[str]] = None, **kwargs):
        ...
    def _on_column_delegate_changed(self, enabled = False):
        """
        Called by StageColumnDelegateRegistry
        """
    def destroy(self):
        ...
    def drop(self, target_item, source, drop_location = -1):
        """
        Reimplemented from AbstractItemModel. Called when dropping something to the item.
        """
    def drop_accepted(self, target_item, source, drop_location = -1):
        """
        Reimplemented from AbstractItemModel. Called to highlight target when drag and drop.
        """
    def get_columns(self) -> typing.List[typing.Tuple[str, bool]]:
        """
        
                Return all the columns in the format
        
                   `[("Visibility", True), ("Type", False)]`
        
                The first item is the column name, and the second item is a flag that
                is True if the column is enabled.
                
        """
    def get_drag_mime_data(self, item):
        """
        Returns Multipurpose Internet Mail Extensions (MIME) data for be able to drop this item somewhere
        """
    def get_item_children(self, item):
        """
        Returns all the children when the widget asks it.
        """
    def get_item_value_model(self, item, column_id):
        """
        
                Return value model.
                It's the object that tracks the specific value.
                In our case we use ui.SimpleStringModel.
                
        """
    def get_item_value_model_count(self, item):
        """
        The number of columns
        """
    def subscribe_delegate_changed(self, fn: typing.Callable[[typing.List[str]], NoneType]) -> omni.kit.widget.stage.event.EventSubscription:
        """
        
                Return the object that will automatically unsubscribe when destroyed.
                
        """
