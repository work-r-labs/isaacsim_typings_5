from __future__ import annotations
from functools import partial
import omni as omni
from omni.kit.widget.stage.stage_widget import StageWidget
from omni import ui
from pxr import Sdf
from pxr import Usd
import pxr.Usd
import weakref as weakref
__all__: list = ['filter_prims', 'SelectionWatch', 'RelationshipTargetPicker', 'RelationshipArrayModel', 'SdfRelationshipArraySingleEntryModel', 'SdfRelationshipArrayItemModel', 'RelationshipEditWidget']
class RelationshipArrayModel(omni.ui._ui.AbstractValueModel):
    """
    
        RelationshipArrayModel is the model for the relationship array.
        
    """
    def __init__(self, stage, property_paths, additional_widget_kwargs):
        """
        
                Initialize the RelationshipArrayModel.
        
                Args:
                    stage: The stage.
                    property_paths: The property paths.
                    additional_widget_kwargs: The additional widget kwargs.
                
        """
    def _on_usd_changed(self, *args, **kwargs):
        """
        
                On USD changed.
        
                Args:
                    *args: The args.
                    **kwargs: The kwargs.
                
        """
    def _set_dirty(self, *args, **kwargs):
        """
        
                Set dirty.
        
                Args:
                    *args: The args.
                    **kwargs: The kwargs.
                
        """
    def _update_shared_targets(self):
        """
        
                Update the shared targets.
                
        """
    def clean(self):
        """
        
                Clean the RelationshipArrayModel.
                
        """
    def get_property_paths(self):
        """
        
                Get the property paths.
        
                Returns:
                    List[Sdf.Path]: The property paths.
                
        """
    def get_relationship_paths(self) -> typing.List[pxr.Sdf.Path]:
        """
        
                Get the relationship paths.
        
                Returns:
                    List[Sdf.Path]: The relationship paths.
                
        """
    def get_targets(self) -> typing.List[pxr.Sdf.Path]:
        """
        
                Get the targets.
        
                Returns:
                    List[Sdf.Path]: The targets.
                
        """
    def get_value(self):
        """
        
                Get the value.
        
                Returns:
                    List[Sdf.Path]: The value.
                
        """
    def is_ambiguous(self) -> bool:
        """
        
                Check if the targets are ambiguous.
        
                Returns:
                    bool: True if the targets are ambiguous, False otherwise.
                
        """
    def set_targets(self, targets: typing.List[pxr.Sdf.Path]):
        """
        
                Set the targets.
        
                Args:
                    targets: The targets.
                
        """
    def set_value(self, targets: typing.List[pxr.Sdf.Path]):
        """
        
                Set the value.
        
                Args:
                    targets: The targets.
                
        """
class RelationshipEditWidget:
    """
    
        DEPRECATED!
    
        Existing extensions depend on this class but the UI has been updated. Please update your extensions.
        
    """
    def __init__(self, stage, attr_name, prim_paths, additional_widget_kwargs = None):
        ...
    def _build(self):
        """
        
                Build the RelationshipEditWidget.
                
        """
    def _set_dirty(self):
        """
        
                Set dirty.
                
        """
    def clean(self):
        """
        
                Clean the RelationshipEditWidget.
                
        """
    def get_all_comp_ambiguous(self) -> typing.List[bool]:
        """
        
                Get all components ambiguous.
        
                Returns:
                    List[bool]: The all components ambiguous.
                
        """
    def get_property_paths(self) -> typing.List[pxr.Sdf.Path]:
        """
        
                Get the property paths.
        
                Returns:
                    List[Sdf.Path]: The property paths.
                
        """
    def get_relationship_paths(self) -> typing.List[pxr.Sdf.Path]:
        """
        
                Get the relationship paths.
        
                Returns:
                    List[Sdf.Path]: The relationship paths.
                
        """
    def get_targets(self) -> typing.List[pxr.Sdf.Path]:
        """
        
                Get the targets.
        
                Returns:
                    List[Sdf.Path]: The targets.
                
        """
    def is_ambiguous(self) -> bool:
        """
        
                Check if the targets are ambiguous.
        
                Returns:
                    bool: True if the targets are ambiguous, False otherwise.
                
        """
    def set_targets(self, targets: typing.List[pxr.Sdf.Path]):
        """
        
                Set the targets.
        
                Args:
                    targets: The targets.
                
        """
    def set_value(self, targets: typing.List[pxr.Sdf.Path]):
        """
        
                Set the value.
        
                Args:
                    targets: The targets.
                
        """
class RelationshipTargetPicker:
    """
    
        RelationshipTargetPicker is used to pick the target of the relationship.
        
    """
    @staticmethod
    def _on_select(weak_self: callable):
        ...
    def __init__(self, stage, filter_type_list, filter_lambda, additional_widget_kwargs):
        """
        
                Initialize the RelationshipTargetPicker.
        
                Args:
                    stage (Usd.Stage): The stage.
                    filter_type_list (List[str]): The filter type list.
                    filter_lambda (Callable): The filter lambda.
                    additional_widget_kwargs (dict): The additional widget kwargs.
                
        """
    def _on_selection_changed(self, paths):
        """
        
                On selection changed.
        
                Args:
                    paths: The paths.
                
        """
    def clean(self):
        """
        
                Clean the RelationshipTargetPicker.
                
        """
    def show(self, targets_limit, on_targets_selected: typing.Optional[typing.Callable] = None):
        """
        
                Show the RelationshipTargetPicker.
        
                Args:
                    targets_limit: The targets limit.
                    on_targets_selected: The on targets selected callback.
                
        """
class RelationshipTargetPickerOld:
    """
    
        DEPRECATED
        
    """
    def __init__(self, stage, relationship_widget, filter_type_list, filter_lambda, on_add_targets: typing.Optional[typing.Callable] = None):
        ...
    def _on_selection_changed(self, paths):
        """
        
                On selection changed.
        
                Args:
                    paths: The paths.
                
        """
    def clean(self):
        """
        
                Clean the RelationshipTargetPickerOld.
                
        """
    def show(self, targets_limit):
        """
        
                Show the RelationshipTargetPickerOld.
        
                Args:
                    targets_limit: The targets limit.
                
        """
class SdfRelationshipArrayItemModel(omni.ui._ui.AbstractItemModel):
    """
    
        SdfRelationshipArrayItemModel is the model for the item of the relationship array.
        
    """
    class SdfRelationshipPathItem(omni.ui._ui.AbstractItem):
        """
        
                Single item of the model
                
        """
        def __init__(self, stage: pxr.Usd.Stage, property_paths: typing.List[pxr.Sdf.Path], index: int, self_refresh: bool, metadata: dict, additional_widget_kwargs = None):
            """
            
                        Initialize the SdfRelationshipPathItem.
            
                        Args:
                            stage: The stage.
                            property_paths: The property paths.
                            index: The index.
                            self_refresh: Whether to refresh the item.
                            metadata: The metadata.
                            additional_widget_kwargs: The additional widget kwargs.
                        
            """
        def destroy(self):
            """
            
                        Destroy the SdfRelationshipPathItem.
                        
            """
        def is_ambiguous(self) -> bool:
            """
            
                        Check if the targets are ambiguous.
            
                        Returns:
                            bool: True if the targets are ambiguous, False otherwise.
                        
            """
    def __init__(self, stage: pxr.Usd.Stage, property_paths: typing.List[pxr.Sdf.Path], metadata: dict, delegate, additional_widget_kwargs):
        """
        
                Initialize the SdfRelationshipArrayItemModel.
        
                Args:
                    stage: The stage.
                    property_paths: The property paths.
                    metadata: The metadata.
                    delegate: The delegate.
                    additional_widget_kwargs: The additional widget kwargs.
                
        """
    def _on_usd_changed(self, *args, **kwargs):
        """
        
                On USD changed.
        
                Args:
                    *args: The args.
                    **kwargs: The kwargs.
                
        """
    def _repopulate_entries(self, value):
        """
        
                Repopulate the entries.
        
                Args:
                    value: The value.
                
        """
    def _set_dirty(self, *args, **kwargs):
        """
        
                Set dirty.
        
                Args:
                    *args: The args.
                    **kwargs: The kwargs.
                
        """
    def clean(self):
        """
        
                Clean the SdfRelationshipArrayItemModel.
                
        """
    def drop(self, target_item, source, drop_location = -1):
        """
        
                Drop the item.
        
                Args:
                    target_item: The target item.
                    source: The source.
                    drop_location: The drop location.
                
        """
    def drop_accepted(self, target_item, source, drop_location = -1):
        """
        
                Check if the drop is accepted.
        
                Args:
                    target_item: The target item.
                    source: The source.
                    drop_location: The drop location.
                
        """
    def get_attribute_paths(self) -> typing.List[pxr.Sdf.Path]:
        """
        
                Get the attribute paths.
        
                Returns:
                    List[Sdf.Path]: The attribute paths.
                
        """
    def get_drag_mime_data(self, item):
        """
        
                Get the drag mime data.
        
                Args:
                    item: The item.
                
        """
    def get_item_children(self, item):
        """
        
                Get the item children.
        
                Args:
                    item: The item.
                
        """
    def get_item_value_model(self, item, column_id):
        """
        
                Get the item value model.
        
                Args:
                    item: The item.
                    column_id: The column id.
                
        """
    def get_item_value_model_count(self, item):
        """
        
                Get the item value model count.
        
                Args:
                    item: The item.
                
        """
    def get_property_paths(self) -> typing.List[pxr.Sdf.Path]:
        """
        
                Get the property paths.
        
                Returns:
                    List[Sdf.Path]: The property paths.
                
        """
    def get_value(self, *args, **kwargs):
        """
        
                Get the value.
        
                Args:
                    *args: The args.
                    **kwargs: The kwargs.
                
        """
    def is_ambiguous(self) -> bool:
        """
        
                Check if the targets are ambiguous.
        
                Returns:
                    bool: True if the targets are ambiguous, False otherwise.
                
        """
    def set_value(self, *args, **kwargs):
        """
        
                Set the value.
        
                Args:
                    *args: The args.
                    **kwargs: The kwargs.
                
        """
    @property
    def value_model(self):
        """
        
                Get the value model.
        
                Returns:
                    RelationshipArrayModel: The value model.
                
        """
class SdfRelationshipArraySingleEntryModel(omni.ui._ui.SimpleStringModel):
    """
    
        SdfRelationshipArraySingleEntryModel is the model for the single entry of the relationship array.
        
    """
    def __init__(self, stage: pxr.Usd.Stage, property_paths: typing.List[pxr.Sdf.Path], index: int):
        """
        
                Initialize the SdfRelationshipArraySingleEntryModel.
        
                Args:
                    stage: The stage.
                    property_paths: The property paths.
                    index: The index.
                
        """
    def _on_usd_changed(self, *args, **kwargs):
        """
        
                On USD changed.
        
                Args:
                    *args: The args.
                    **kwargs: The kwargs.
                
        """
    def _set_dirty(self, *args, **kwargs):
        """
        
                Set dirty.
        
                Args:
                    *args: The args.
                    **kwargs: The kwargs.
                
        """
    def clean(self):
        """
        
                Clean the SdfRelationshipArraySingleEntryModel.
                
        """
    def get_value(self):
        """
        
                Get the value.
        
                Returns:
                    str: The value.
                
        """
    def get_value_as_string(self):
        """
        
                Get the value as string.
        
                Returns:
                    str: The value as string.
                
        """
    def set_value(self, value):
        """
        
                Set the value.
        
                Args:
                    value: The value.
                
        """
    def set_value_as_string(self, value):
        """
        
                Set the value as string.
        
                Args:
                    value: The value.
                
        """
class SelectionWatch:
    """
    
        SelectionWatch is used to watch the selection of the stage.
        
    """
    def __init__(self, stage, on_selection_changed_fn, filter_type_list, filter_lambda, tree_view = None):
        ...
    def _on_widget_selection_changed(self, selection):
        """
        
                On widget selection changed.
        
                Args:
                    selection (List[Sdf.Path]): The selection.
                
        """
    def clear_selection(self):
        """
        
                Clear the selection.
                
        """
    def enable_filtering_checking(self, enable: bool):
        """
        
                It is used to prevent selecting the prims that are filtered out but
                still displayed when such prims have filtered children. When `enable`
                is True, SelectionWatch should consider filtering when changing Kit's
                selection.
                
        """
    def reset(self, targets_limit):
        """
        
                Reset the targets limit.
        
                Args:
                    targets_limit (int): The targets limit.
                
        """
    def set_filtering(self, filter_string: typing.Optional[str]):
        """
        
                Set the filtering.
        
                Args:
                    filter_string (Optional[str]): The filter string.
                
        """
    def set_tree_view(self, tree_view):
        """
        
                Set the tree view.
        
                Args:
                    tree_view (TreeView): The tree view.
                
        """
class SelectionWatchOld:
    """
    
        DEPRECATED
        
    """
    def __init__(self, stage, on_selection_changed_fn, filter_type_list, filter_lambda, tree_view = None):
        """
        
                Initialize the SelectionWatchOld.
        
                Args:
                    stage: The stage.
                    on_selection_changed_fn: The on selection changed function.
                    filter_type_list: The filter type list.
                    filter_lambda: The filter lambda.
                    tree_view: The tree view.
                
        """
    def _on_widget_selection_changed(self, selection):
        """
        
                On widget selection changed.
        
                Args:
                    selection: The selection.
                
        """
    def clear_selection(self):
        """
        
                Clear the selection.
                
        """
    def enable_filtering_checking(self, enable: bool):
        """
        
                It is used to prevent selecting the prims that are filtered out but
                still displayed when such prims have filtered children. When `enable`
                is True, SelectionWatch should consider filtering when changing Kit's
                selection.
                
        """
    def reset(self, targets_limit):
        """
        
                Reset the targets limit.
        
                Args:
                    targets_limit: The targets limit.
                
        """
    def set_filtering(self, filter_string: typing.Optional[str]):
        """
        
                Set the filtering.
        
                Args:
                    filter_string: The filter string.
                
        """
    def set_tree_view(self, tree_view):
        """
        
                Set the tree view.
        
                Args:
                    tree_view: The tree view.
                
        """
def filter_prims(stage, prim_list, type_list):
    """
    
        Filter the prims based on the type list.
        
    """
