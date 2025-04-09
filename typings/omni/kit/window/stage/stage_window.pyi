from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.widget.stage.selection_watch import DefaultSelectionWatch as SelectionWatch
from omni.kit.widget.stage.stage_widget import StageWidget
from omni.kit.window.stage.external_drag_drop_helper import destroy_external_drag_drop
from omni.kit.window.stage.external_drag_drop_helper import setup_external_drag_drop
from omni import ui
from pxr import Usd
__all__: list = ['StageWindow']
class CustomizedStageWidget(omni.kit.widget.stage.stage_widget.StageWidget):
    def get_delegate(self):
        ...
    def get_treeview(self):
        ...
    @property
    def auto_reload_prims(self) -> bool:
        """
        
                Whether prims are auto loaded.
        
                Returns:
                    bool
                
        """
    @auto_reload_prims.setter
    def auto_reload_prims(self, value):
        ...
    @property
    def children_reorder_supported(self) -> bool:
        """
        
                Whether children re-ordering is supported.
        
                Returns:
                    bool
                
        """
    @children_reorder_supported.setter
    def children_reorder_supported(self, value):
        ...
    @property
    def show_abstract_prims(self) -> bool:
        """
        
                Whether to show abstract prims.
        
                Returns:
                    bool
                
        """
    @show_abstract_prims.setter
    def show_abstract_prims(self, value):
        ...
    @property
    def show_prim_display_name(self) -> bool:
        """
        
                Whether to show display names for prims.
        
                Returns:
                    bool
                
        """
    @show_prim_display_name.setter
    def show_prim_display_name(self, value):
        ...
    @property
    def show_undefined_prims(self) -> bool:
        """
        
                Whether to show undefined prims.
        
                Returns:
                    bool
                
        """
    @show_undefined_prims.setter
    def show_undefined_prims(self, value):
        ...
class StageWindow(omni.ui._ui.Window):
    """
    The Stage window
    """
    def __init__(self, usd_context_name: str = ''):
        ...
    def _columns_changed(self, columns: typing.List[typing.Tuple[str, bool]]):
        """
        
                Called by StageWidget when columns are changed or toggled.
                
        """
    def _on_stage_closing(self):
        """
        Called when close the stage
        """
    def _on_stage_opened(self):
        """
        Called when opening a new stage
        """
    def _on_usd_context_event(self, event: carb.events._events.IEvent):
        """
        Called on USD Context event
        """
    def _visibility_changed_fn(self, visible):
        ...
    def destroy(self):
        """
        
                Called by extension before destroying this object. It doesn't happen automatically.
                Without this hot reloading doesn't work.
                
        """
    def get_widget(self) -> CustomizedStageWidget:
        ...
    def set_visibility_changed_listener(self, listener):
        ...
