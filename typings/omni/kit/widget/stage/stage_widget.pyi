from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit import notification_manager as nm
from omni.kit.usd import layers
from omni.kit.widget.options_button.options_button import OptionsButton
from omni.kit.widget.options_menu.option_custom import OptionCustom
from omni.kit.widget.options_menu.option_delegate import OptionLabelMenuItemDelegate
from omni.kit.widget.options_menu.option_item import OptionItem
from omni.kit.widget.options_menu.option_separator import OptionSeparator
from omni.kit.widget.searchfield.searchfield import SearchField
from omni.kit.widget.stage.column_menu import ColumnMenuDelegate
from omni.kit.widget.stage.column_menu import ColumnMenuItem
from omni.kit.widget.stage.column_menu import ColumnMenuModel
from omni.kit.widget.stage.context_menu import ContextMenu
from omni.kit.widget.stage.event import Event
from omni.kit.widget.stage.event import EventSubscription
from omni.kit.widget.stage.stage_delegate import StageDelegate
from omni.kit.widget.stage.stage_filter import StageFilterButton
from omni.kit.widget.stage.stage_model import StageModel
from omni.kit.widget.stage.stage_settings import StageSettings
from omni.kit.widget.stage.stage_style import Styles as StageStyles
from omni import ui
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
from pxr import UsdSkel
import weakref as weakref
__all__: list = ['StageWidget']
class StageWidget:
    """
    
        The Stage widget that represents the stage with a tree view displaying the prim hierarchy with multiple columns.
        For each treeview item, multiple columns representing different aspects for the prim can be customized and
        displayed. It also provides context menu items associated with the stage/prims.
        
    """
    @staticmethod
    def _get_path_converter() -> typing.Callable:
        """
        
                The Path conversion function to use for prim paths.
        
                Returns:
                    Callable: The path conversion function.
                
        """
    @staticmethod
    def _set_widget_visible(widget: omni.ui._ui.Widget, visible):
        """
        Utility for using in lambdas
        """
    @staticmethod
    def build_layout(*args, **kwargs):
        """
        Creates all the widgets in the widget.
        """
    @staticmethod
    def get_context_menu(*args, **kwargs):
        """
        
                Gets the context menu object associated with the current stage widget.
        
                Returns:
                    ContextMenu: The ContextMenu associated with the delegate.
                
        """
    @staticmethod
    def set_widget_visible(widget: omni.ui._ui.Widget, visible):
        """
        Utility for using in lambdas
        """
    @staticmethod
    def update_icons(*args, **kwargs):
        """
        Called to update icons in the TreeView
        """
    def __init__(self, stage: pxr.Usd.Stage, columns_accepted: typing.List[str] = None, columns_enabled: typing.List[str] = None, lazy_payloads: bool = False, **kwargs):
        """
        
                The constructor for the Stage Widget.
        
                Args:
                    stage (Usd.Stage): The instance of USD stage to be managed by this widget.
        
                Keyword Args:
                    columns_accepted (List[str]): The list of columns that are supported. By default, it's all registered
                        columns if this arg is not provided.
                    columns_enabled (List[str]): The list of columns that are enabled when the widget is shown by default.
                    lazy_payloads (bool): Whether it should load all payloads when stage items are shown or not.
                        False by default.
                    children_reorder_supported (bool): Whether it should enable children reorder support or not. By default,
                        children reorder support is disabled, which means you cannot reorder children in the widget, and
                        renaming name of prim will put the prim at the end of the children list. REMINDER: Enabling this
                        option has performance penalty as it will trigger re-composition to the parent of the reordered/renamed
                        prims.
                    show_prim_display_name (bool): Whether it's to show displayName from prim's metadata or the name of the prim.
                        By default, it's False, which means it shows name of the prim.
                    auto_reload_prims (bool): Whether it will auto-reload prims if there are any new changes from disk. By
                        default, it's disabled.
                    show_undefined_prims (bool): Whether it's to show prims that have no def or not.
                        By default, it's False.
                    show_inactive_prims (bool): Whether it's to show prims that have active=False.
                        By default, it's True.
                    show_abstract_prims (bool): Whether it's to show prims that have are abstract.
                        By default, it's True.
        
                Other:
                    All other arguments inside kwargs except the above 3 will be passed as params to the ui.Frame for the
                    stage widget.
                
        """
    def _build_layout(self):
        """
        Creates all the widgets in the widget.
        """
    def _build_options_button(self):
        """
        
                Builds the options buttons.
                Options include:
                    Auto Reload Primitives: Whether to auto reload prims.
                    Reload Outdated Primitives: Reloads outdated prims when triggered.
                    Reset: Resets all options to default.
                    Flat List Search: Whether to turn on flat list search.
                    Show Root: Whether to show root.
                    Show Display Names: Whether to show display names for prims.
                    Show Inactive Prims: Whether to show inactive prims.
                    Show Undefined Prims: Whether to show undefined prims.
                    Show Abstract Prims: Whether to show abstract prims.
                    Enable Children Reorder: Whether to enable children re-ordering.
                    Columns: Groups all registered column types, and creates a sub item for each registered column type.
                
        """
    def _cancel_expand_task(self):
        ...
    def _clear_filter_types(self):
        ...
    def _filter_by_abstract_state(self, enabled):
        """
        Filter Abstract On/Off
        """
    def _filter_by_active_state(self, enabled):
        """
        Filter Active On/Off
        """
    def _filter_by_api_type(self, api_types, enabled):
        """
        
                Set filtering by USD api type.
        
                Args:
                    api_types: The api type or the list of types it's necessary to add or remove from filters.
                    enabled: True to add to filters, False to remove them from the filter list.
                
        """
    def _filter_by_def_state(self, enabled):
        """
        Filter Def On/Off
        """
    def _filter_by_flattener_basemesh(self, enabled):
        ...
    def _filter_by_flattener_decal(self, enabled):
        ...
    def _filter_by_lambda(self, filters: dict, enabled):
        """
        
                Set filtering by lambda.
        
                Args:
                    filters: The dictionary of this form: {"type_name_string", lambda prim: True}. When lambda is True,
                             the prim will be shown.
                    enabled: True to add to filters, False to remove them from the filter list.
                
        """
    def _filter_by_text(self, filter_text: str):
        """
        Set the search filter string to the models and widgets
        """
    def _filter_by_type(self, usd_types, enabled):
        """
        
                Set filtering by USD type.
        
                Args:
                    usd_types: The type or the list of types it's necessary to add or remove from filters.
                    enabled: True to add to filters, False to remove them from the filter list.
                
        """
    def _filter_by_visibility(self, enabled):
        """
        Filter Hidden On/Off
        """
    def _get_geom_primvar(self, prim, primvar_name):
        ...
    def _get_stage_model(self, stage: pxr.Usd.Stage):
        ...
    def _on_column_changed(self, column_model: omni.kit.widget.stage.column_menu.ColumnMenuModel, item: omni.kit.widget.stage.column_menu.ColumnMenuItem = None):
        """
        Called by Column Model when columns are changed or toggled
        """
    def _on_column_selection_changed(self, _):
        ...
    def _on_flat_changed(self, flat: bool):
        """
        Toggle flat/not flat search
        """
    def _on_reload_all_prims(self):
        ...
    def _on_reload_prims(self, not_in_session = True):
        ...
    def _on_reset(self):
        """
        Toggle "Reset" menu
        """
    def _on_show_root_changed(self, show: bool):
        """
        Called to trigger "Show Root" menu item
        """
    def _update_icons(self):
        """
        Called to update icons in the TreeView
        """
    def collapse(self, path: pxr.Sdf.Path):
        """
        
                Set the given path to be collapsed.
        
                Args:
                    path (Sdf.Path): Path to be collapsed.
                
        """
    def destroy(self):
        """
        
                Called by extension before destroying this object. It doesn't happen automatically.
                Without this hot reloading doesn't work.
                
        """
    def expand(self, path: pxr.Sdf.Path):
        """
        
                Sets the given path to be expanded.
        
                Args:
                    path (Sdf.Path): Path to be expanded.
                
        """
    def filter_by_abstract_state(self, enabled):
        """
        Filter Abstract On/Off
        """
    def filter_by_active_state(self, enabled):
        """
        Filter Active On/Off
        """
    def filter_by_api_type(self, api_types, enabled):
        """
        
                Set filtering by USD api type.
        
                Args:
                    api_types: The api type or the list of types it's necessary to add or remove from filters.
                    enabled: True to add to filters, False to remove them from the filter list.
                
        """
    def filter_by_def_state(self, enabled):
        """
        Filter Def On/Off
        """
    def filter_by_lambda(self, filters: dict, enabled):
        """
        
                Set filtering by lambda.
        
                Args:
                    filters: The dictionary of this form: {"type_name_string", lambda prim: True}. When lambda is True,
                             the prim will be shown.
                    enabled: True to add to filters, False to remove them from the filter list.
                
        """
    def filter_by_text(self, filter_text: str):
        """
        Set the search filter string to the models and widgets
        """
    def filter_by_type(self, usd_types, enabled):
        """
        
                Set filtering by USD type.
        
                Args:
                    usd_types: The type or the list of types it's necessary to add or remove from filters.
                    enabled: True to add to filters, False to remove them from the filter list.
                
        """
    def filter_by_visibility(self, enabled):
        """
        Filter Hidden On/Off
        """
    def get_model(self) -> omni.kit.widget.stage.stage_model.StageModel:
        """
        
                Gets the stage model.
        
                Returns:
                    Optional[StageModel]: If the treeview is visible, returns the treeview stage model, otherwise returns None.
                
        """
    def open_stage(self, stage: pxr.Usd.Stage):
        """
        
                Called when opening a new stage.
        
                Args:
                    stage (Usd.Stage): The stage that is being opened.
                
        """
    def set_columns_widths(self):
        """
        Sets the column width for treeview and flat treeview.
        """
    def set_fixed_width_columns(self):
        """
        Sets the fixed width columns record for treeview and flat treeview.
        """
    def set_selection_watch(self, selection):
        """
        
                Sets the selection watch of the current stage widget.
        
                Args:
                    selection (omni.kit.widget.stage.DefaultSelectionWatch): The selection watch.
                
        """
    def subscribe_columns_changed(self, fn: typing.Callable[[typing.List[typing.Tuple[str, bool]]], NoneType]) -> omni.kit.widget.stage.event.EventSubscription:
        """
        
                Subscribe to columns changed event with fn.
        
                Args:
                    fn (Callable[[List[Tuple[str, bool]]], None]): The event handler for the subscription.
        
                Returns:
                    EventSubscription: The event subscription object.
                
        """
    def update_filter_menu_state(self, filter_type_list: list):
        """
        
                Enable filters.
        
                Args:
                    filter_type_list (list): List of usd types to be enabled. If not all usd types are pre-defined, hide filter
                    button and Reset in the options button.
                
        """
    @property
    def auto_reload_prims(self) -> bool:
        """
        
                Whether prims are auto loaded.
        
                Returns:
                    bool
                
        """
    @auto_reload_prims.setter
    def auto_reload_prims(self, enabled: bool):
        """
        
                Sets whether prims should be autoloaded.
        
                Args:
                    enabled (bool): Value to set.
                
        """
    @property
    def children_reorder_supported(self) -> bool:
        """
        
                Whether children re-ordering is supported.
        
                Returns:
                    bool
                
        """
    @children_reorder_supported.setter
    def children_reorder_supported(self, enabled: bool):
        """
        
                Sets whether children re-ordering should be supported.
        
                Args:
                    enabled (bool): Value to set.
                
        """
    @property
    def show_abstract_prims(self) -> bool:
        """
        
                Whether to show abstract prims.
        
                Returns:
                    bool
                
        """
    @show_abstract_prims.setter
    def show_abstract_prims(self, show: bool):
        """
        
                Sets whether to show abstract prims.
        
                Args:
                    show (bool): Value to set.
                
        """
    @property
    def show_inactive_prims(self) -> bool:
        """
        
                Whether to show all inactive prims.
        
                Returns:
                    bool
                
        """
    @show_inactive_prims.setter
    def show_inactive_prims(self, show: bool):
        """
        
                Sets whether to show all inactive prims.
        
                Args:
                    show (bool): Value to set.
                
        """
    @property
    def show_prim_display_name(self) -> bool:
        """
        
                Whether to show display names for prims.
        
                Returns:
                    bool
                
        """
    @show_prim_display_name.setter
    def show_prim_display_name(self, show: bool):
        """
        
                Sets whether to show display names for prims.
        
                Args:
                    show (bool): Value to set.
                
        """
    @property
    def show_undefined_prims(self) -> bool:
        """
        
                Whether to show undefined prims.
        
                Returns:
                    bool
                
        """
    @show_undefined_prims.setter
    def show_undefined_prims(self, show: bool):
        """
        
                Sets whether to show undefined prims.
        
                Args:
                    show (bool): Value to set.
                
        """
