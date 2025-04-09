from __future__ import annotations
import carb as carb
import enum
from enum import Enum
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.usd import layers
from omni.kit.widget.stage.event import Event
from omni.kit.widget.stage.event import EventSubscription
from omni.kit.widget.stage.stage_drag_and_drop_handler import AssetType
from omni.kit.widget.stage.stage_drag_and_drop_handler import StageDragAndDropHandler
from omni.kit.widget.stage.stage_item import StageItem
from omni.kit.widget.stage.utils import handle_exception
from omni import ui
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
import typing
__all__: list = ['StageModel', 'StageItemSortPolicy']
class StageItemSortPolicy(enum.Enum):
    """
    Sort policy for stage items.
    """
    DEFAULT: typing.ClassVar[StageItemSortPolicy]  # value = <StageItemSortPolicy.DEFAULT: 0>
    NAME_COLUMN_A_TO_Z: typing.ClassVar[StageItemSortPolicy]  # value = <StageItemSortPolicy.NAME_COLUMN_A_TO_Z: 3>
    NAME_COLUMN_NEW_TO_OLD: typing.ClassVar[StageItemSortPolicy]  # value = <StageItemSortPolicy.NAME_COLUMN_NEW_TO_OLD: 1>
    NAME_COLUMN_OLD_TO_NEW: typing.ClassVar[StageItemSortPolicy]  # value = <StageItemSortPolicy.NAME_COLUMN_OLD_TO_NEW: 2>
    NAME_COLUMN_Z_TO_A: typing.ClassVar[StageItemSortPolicy]  # value = <StageItemSortPolicy.NAME_COLUMN_Z_TO_A: 4>
    TYPE_COLUMN_A_TO_Z: typing.ClassVar[StageItemSortPolicy]  # value = <StageItemSortPolicy.TYPE_COLUMN_A_TO_Z: 5>
    TYPE_COLUMN_Z_TO_A: typing.ClassVar[StageItemSortPolicy]  # value = <StageItemSortPolicy.TYPE_COLUMN_Z_TO_A: 6>
    VISIBILITY_COLUMN_INVISIBLE_TO_VISIBLE: typing.ClassVar[StageItemSortPolicy]  # value = <StageItemSortPolicy.VISIBILITY_COLUMN_INVISIBLE_TO_VISIBLE: 7>
    VISIBILITY_COLUMN_VISIBLE_TO_INVISIBLE: typing.ClassVar[StageItemSortPolicy]  # value = <StageItemSortPolicy.VISIBILITY_COLUMN_VISIBLE_TO_INVISIBLE: 8>
class StageModel(omni.ui._ui.AbstractItemModel):
    """
    The item model that watches the stage.
    """
    @staticmethod
    def _StageModel__delayed_prim_changed(*args, **kwargs):
        ...
    @staticmethod
    def _get_path_converter() -> typing.Callable:
        """
        
                The Path conversion function to use for prim paths.
        
                Returns:
                    Callable: The path conversion function.
                
        """
    @staticmethod
    def _get_stage_item_children(*args, **kwargs):
        """
        
                Gets all children stage items of path. If those stage items are not
                created, they will be created. This optimization is used to implement
                lazy loading that only paths that are accessed will create corresponding
                stage items.
                
        """
    @staticmethod
    def _on_layer_info_change(*args, **kwargs):
        """
        Called by Sdf.Notice.LayerInfoDidChange when the metadata of the root layer is changed
        """
    @staticmethod
    def _on_objects_changed(*args, **kwargs):
        """
        Called by Usd.Notice.ObjectsChanged
        """
    @staticmethod
    def _refresh_prim_subtree(*args, **kwargs):
        """
        
                Refresh prim subtree in lazy way. It will only refresh those
                stage items that are populated already to not load them beforehand
                to improve perf, except the absolute root node.
                
        """
    @staticmethod
    def can_item_have_children(*args, **kwds) -> bool:
        """
        
                Checks if the given item can have children.
                By default, if can_item_have_children is not provided, it will call get_item_children to get the count of
                children, so implementing this function to make sure we do lazy load for all items.
        
                Args:
                    item (Optional[StageItem]): The item to check.
        
                Returns:
                    bool: The result.
                
        """
    @staticmethod
    def find_full_chain(*args, **kwargs) -> typing.Optional[typing.List[omni.kit.widget.stage.stage_item.StageItem]]:
        """
        
                Returns the list of all the parent nodes and the node representing the given path.
                If path is empty or there's no root item, returns None.
        
                Args:
                    path (Optional[Union[Sdf.Path, str]]): Path to find item of.
                Returns:
                    List[StageItem]: Found items.
                
        """
    @staticmethod
    def get_item_children(*args, **kwds) -> typing.Union[typing.List[omni.kit.widget.stage.stage_item.StageItem], omni.kit.widget.stage.stage_item.StageItem]:
        """
        
                Gets the sorted children of the given item. Returns the root item when item is None.
                If filtering is on, will return a filtered list of child items.
        
                Args:
                    item (Optional[StageItem]): Item to find children of.
                Returns:
                    Union[List[StageItem], StageItem]: The child items.
                
        """
    @staticmethod
    def update_dirty(*args, **kwargs):
        """
        
                Create/remove dirty items that was collected from TfNotice. Can be called at any time to pump changes.
                
        """
    def _StageModel__on_exclusion_types_changed(self, item: carb.dictionary._dictionary.Item, event_type: carb.settings._settings.ChangeEventType):
        """
        Called when the exclusion list is changed
        """
    def _StageModel__on_layer_event(self, event):
        ...
    def _StageModel__on_selection_changed(self):
        ...
    def _StageModel__on_stage_event(self, event: carb.events._events.IEvent):
        ...
    def _StageModel__set_selected_stage_items(self, selections):
        ...
    def __init__(self, stage: pxr.Usd.Stage, flat = False, load_payloads = False, check_missing_references = False, **kwargs):
        """
        
                StageModel provides the model for TreeView of Stage Widget, which also manages all StageItems.
        
                Args:
                    stage (Usd.Stage): USD stage handle.
        
                Keyword Args:
                    flat (bool): If True, all StageItems will be children of the root node. This option only applies to
                        filtering mode.
                    load_payloads (bool): Whether payloads should be loaded automatically during stage traversal.
                    check_missing_references (bool): Deprecated.
                    children_reorder_supported (bool): Whether to enable children reordering for drag and drop. False by default.
                    show_prim_displayname (bool): Whether to show prim's displayName from metadata or path name. False by default.
                    show_undefined_prims (bool): Whether to show prims that have no def. False by default.
                    show_inactive_prims (bool): Whether to show inactive prims. True by default.
                    show_abstract_prims (bool): Whether to show abstract prims. True by default.
                
        """
    def _cache_stage_item(self, item: omni.kit.widget.stage.stage_item.StageItem):
        ...
    def _clear_filter_states(self, prim_path = None):
        ...
    def _clear_stage_item_cache(self):
        ...
    def _filter_prim(self, prim: pxr.Usd.Prim):
        ...
    def _get_all_stage_items_from_cache(self):
        ...
    def _get_stage_item_from_cache(self, path: pxr.Sdf.Path, create_if_not_existed = False):
        """
        Gets or creates stage item.
        """
    def _has_filters(self):
        ...
    def _pop_stage_item_from_cache(self, prim_path: pxr.Sdf.Path):
        ...
    def _prefilter(self, prim_path: pxr.Sdf.Path):
        """
        Recursively mark items that meet the filtering rule
        """
    def _refresh_stage_items(self, info_changed_items = list(), children_refreshed_items = list(), destroyed_items = list()):
        """
        
                `info_changed_items` includes only items that have flags/attributes updated.
                `children_refreshed_items` includes only items that have children updated.
                `destroyed_items` includes only items that are removed from stage.
                
        """
    def _remove_stage_item_from_cache(self, prim_path: pxr.Sdf.Path):
        ...
    def _should_prim_be_excluded_from_tree_view(self, prim):
        ...
    def destroy(self):
        """
        Destroys the instance, notifies column delegates and clear all subs and resources.
        """
    def drop(self, target_item, source, drop_location = -1):
        """
        
                Drop handler called when dropping something to the item.
                When drop_location is -1, it means to drop the source item on top of the target item. When drop_location is not
                -1, it means to drop the source item between items.
        
                Args:
                    target_item (StageItem): Drop target.
                    source (StageItem): Drop source.
                    drop_location (int): The drop location, default to -1.
                
        """
    def drop_accepted(self, target_item, source, drop_location = -1) -> bool:
        """
        
                Called to highlight the target when drag and dropping.
        
                Args:
                    target_item (StageItem): Drop target.
                    source (StageItem): Drop source.
                    drop_location (int): The drop location, default to -1.
        
                Returns:
                    bool: Drop accepted.
                
        """
    def filter(self, add = None, remove = None, clear = None) -> bool:
        """
        
                Updates the filter type names and refreshes the stage items with the new filter types.
                In most cases we need to filter by several types, so this method allows to add, remove and set the list of types
                to filter and updates the items if necessary.
        
                Keyword Args:
                    add (Optional[Dict]): A dictionary of this form: {"type_name_string", lambda prim: True}. When lambda is
                        True, the prim will be shown.
                    remove (Optional[Union[str, Dict, list, set]]): Removes filters by name if the filter name is in "remove".
                    clear: Removes all existing filters. When used with `add`, it will remove existing filters first and then
                        add the newly given ones.
        
                Returns:
                    True if the model has filters. False otherwise.
                
        """
    def filter_by_text(self, filter_name_text):
        """
        
                Filter stage model items by text.
                Currently, only single word that's case-insensitive or prim path are supported.
        
                Args:
                    filter_name_text (str): The filter text.
                
        """
    def find(self, path: pxr.Sdf.Path) -> omni.kit.widget.stage.stage_item.StageItem:
        """
        
                Finds the item with the given path if it's populated already.
        
                Args:
                    path (Sdf.Path): Path to find item of.
        
                Returns:
                    StageItem: The found item
                
        """
    def get_drag_mime_data(self, item: omni.kit.widget.stage.stage_item.StageItem) -> str:
        """
        
                Returns MIME (Multipurpose Internet Mail Extensions) data for dropping this item elsewhere.
        
                Args:
                    item (StageItem): The source item.
        
                Returns:
                    str: The MIME data constructed of item paths.
                
        """
    def get_filters(self) -> typing.Dict:
        """
        
                Return dict of filters.
        
                Returns:
                    Dict: The filters dictionary.
                
        """
    def get_item_value_model_count(self, item: typing.Optional[omni.kit.widget.stage.stage_item.StageItem]) -> int:
        """
        
                Gets item value model count.
        
                Args:
                    item (Optional[StageItem]): Unused.
        
                Returns:
                    int: The item value model count.
                
        """
    def get_items_sort_policy(self) -> StageItemSortPolicy:
        """
        
                Gets the sort policy for builtin columns.
        
                Returns:
                    StageItemSortPolicy: The sort policy.
                
        """
    def get_selected_stage_items(self) -> typing.List[omni.kit.widget.stage.stage_item.StageItem]:
        """
        Gets a list of current selected stage items.
        
                Returns:
                    List[StageItem]: A list of stage items.
                
        """
    def refresh_item_names(self):
        """
        Deprecated.
        """
    def rename_prim(self, prim_path: pxr.Sdf.Path, new_name: str) -> bool:
        """
        
                Renames a prim to the new name given.
        
                Args:
                    prim_path (Sdf.Path): The prim path to rename.
                    new_name (str): The new name to rename to.
        
                Returns:
                    bool: Whether the ranme is performed successfully.
                
        """
    def reset(self):
        """
        Forces a full update of items.
        """
    def set_item_value_model_count(self, count: int):
        """
        
                Internal method to set column count.
        
                Args:
                    count (int): Count value to set.
                
        """
    def set_items_sort_key_func(self, key_fn: typing.Callable[[omni.kit.widget.stage.stage_item.StageItem], NoneType], reverse = False):
        """
        
                Sets the key function to sort item children.
        
                Args:
                    key_fn (Callable[[StageItem], None]): The function that's used to sort children of item, which
                        be passed to list.sort as key function, for example, `lambda item: item.name`. If `key_fn` is
                        None and `reverse` is True, it will reverse items only. Or if `key_fn` is None and `reverse` is
                        False, it will clear sort function.
                    reverse (bool): By default, it's ascending order to sort with key_fn. If this flag is True,
                        it will sort children in reverse order.
                
        """
    def set_items_sort_policy(self, items_sort_policy: StageItemSortPolicy):
        """
        
                This is the old way to sort builtin columns (name, type, and visibility), which can only sort one builtin column
                at a time, and it will clear all existing sort functions customized by `append_column_sort_key_func` and only
                sort column specified by `items_sort_policy`. For more advanced sorting, see function
                `append_column_sort_key_func`, which supports chaining sort for multiple columns.
        
                Args:
                    items_sort_policy (StageItemSortPolicy): The sort policy to set.
                
        """
    def set_selected_stage_items(self, selections: typing.List[omni.kit.widget.stage.stage_item.StageItem], undo = False):
        """
        Sets a list of selections.
        
                It also sets selections for omni.kit.selection if this stage model manages the stage
                from a UsdContext.
        
                Args:
                    selections (List[StageItem]): Non-empty selection list to be set.
                    undo (bool): If the selection for omni.kit.selection can be undo. Defaults to False.
                
        """
    def subscribe_stage_items_destroyed(self, fn: typing.Callable[[typing.List[omni.kit.widget.stage.stage_item.StageItem]], NoneType]) -> omni.kit.widget.stage.event.EventSubscription:
        """
        
                Subscribe to changes when stage items are destroyed with fn.
                Return the object that will automatically unsubscribe when destroyed.
        
                Args:
                    fn (Callable[[List[StageItem]], None]): The event handler.
                Returns:
                    EventSubscription: The subscription object.
                
        """
    def subscribe_stage_items_selection_changed(self, fn: typing.Callable[[], NoneType]) -> omni.kit.widget.stage.event.EventSubscription:
        """
        
                Subscribe to changes when stage items are selected or unselected.
                Return the object that will automatically unsubscribe when destroyed.
        
                Why StageModel manages its own selection list is because omni.kit.selection only manages those selections
                that are valid prims. Valid prims are those ones that exist in the stage and active. We also need to support
                UX for those items that are inactive to do batch operations with them. Therefore, StageModel maintains its own
                selection list that is iosolated with omni.kit.selection, and it also keeps up with the omni.kit.selection
                events if necessary.
        
                Args:
                    fn (Callable[[], None]): The event handler to notify when selections are changed.
                Returns:
                    EventSubscription: The subscription object.
                
        """
    @property
    def check_missing_references(self):
        """
        Deprecated: It will always check missing references now.
        """
    @check_missing_references.setter
    def check_missing_references(self, value):
        """
        Deprecated.
        """
    @property
    def children_reorder_supported(self) -> bool:
        """
        
                Whether to support reorder children by drag and dropping.
        
                Returns:
                    bool: The setting value.
                
        """
    @children_reorder_supported.setter
    def children_reorder_supported(self, value: bool):
        """
        
                Sets whether children re-ordering should be supported.
        
                Args:
                    enabled (bool): Value to set.
                
        """
    @property
    def exclusion_types(self) -> typing.Optional[typing.List[str]]:
        """
        
                Gets the exclusion types.
        
                Returns:
                    Optional[List[str]]: The exclusion types if set, else None.
                
        """
    @property
    def flat(self) -> bool:
        """
        
                Whether the model is in flat mode or not.
                When in flat mode, all items will be the children of the root item, and empty children for other items.
        
                It will return False when show_prim_displayname is True, or when model has not filter text, even if this
                property is set to True. That means flat mode is currently used for searching only and show_prim_displayname is
                False.
                
        """
    @flat.setter
    def flat(self, value):
        """
        
                Sets search mode.
        
                Args:
                    value (bool): Value to set.
                
        """
    @property
    def root(self) -> omni.kit.widget.stage.stage_item.StageItem:
        """
        
                Gets the item that represents the absolute root.
        
                Returns:
                    StageItem: The root item.
                
        """
    @property
    def show_abstract_prims(self) -> bool:
        """
        
                Whether to show abstract prims.
        
                Returns:
                    bool
                
        """
    @show_abstract_prims.setter
    def show_abstract_prims(self, value):
        """
        
                Sets whether to show abstract prims.
        
                Args:
                    value (bool): Value to set.
                
        """
    @property
    def show_inactive_prims(self) -> bool:
        """
        
                Instructs stage delegate to show all inactive prims.
        
                Returns:
                    bool
                
        """
    @show_inactive_prims.setter
    def show_inactive_prims(self, value):
        """
        
                Sets whether to show all inactive prims.
        
                Args:
                    show (bool): Value to set.
                
        """
    @property
    def show_prim_displayname(self) -> bool:
        """
        
                Instructs stage delegate to show prim's displayName from USD or path name.
        
                Returns:
                    bool
                
        """
    @show_prim_displayname.setter
    def show_prim_displayname(self, value):
        """
        
                Sets whether to show display names for prims.
        
                Args:
                    show (bool): Value to set.
                
        """
    @property
    def show_undefined_prims(self) -> bool:
        """
        
                Whether to show prims that have no def.
        
                Returns:
                    bool
                
        """
    @show_undefined_prims.setter
    def show_undefined_prims(self, value):
        """
        
                Sets whether to show undefined prims.
        
                Args:
                    value (bool): Value to set.
                
        """
    @property
    def stage(self) -> pxr.Usd.Stage:
        """
        
                Gets the stage for the model.
        
                Returns:
                    Usd.Stage: The underlying usd stage for the model.
                
        """
    @property
    def usd_context(self) -> omni.usd._usd.UsdContext:
        """
        
                Gets the usd context for the model.
        
                Returns:
                    omni.usd.UsdContext: The underlying usd context for the model.
                
        """
EXCLUSION_TYPES_SETTING: str = 'ext/omni.kit.widget.stage/exclusion/types'
