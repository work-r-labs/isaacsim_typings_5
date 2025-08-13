from __future__ import annotations
import asyncio as asyncio
import carb as carb
import fnmatch as fnmatch
from functools import lru_cache
from functools import partial
import omni as omni
from omni.kit.property.adapter.core.scripts.core_adapter import PropertyType
from omni.kit.property.adapter.core.scripts.core_adapter import StageAdapter
from omni.kit.property.usd.asset_filepicker import replace_query
from omni.kit.property.usd.asset_filepicker import show_asset_file_picker
from omni.kit.property.usd.attribute_context_menu import AttributeContextMenu
from omni.kit.property.usd.attribute_context_menu import AttributeContextMenuEvent
from omni.kit.property.usd.control_state_manager import ControlStateManager
from omni.kit.property.usd.relationship import RelationshipArrayModel
from omni.kit.property.usd.relationship import SdfRelationshipArrayItemModel
from omni.kit.property.usd.usd_attribute_model import BoolArrayAttributeSingleChannelModel
from omni.kit.property.usd.usd_attribute_model import GfMatrixAttributeModel
from omni.kit.property.usd.usd_attribute_model import GfVecAttributeModel
from omni.kit.property.usd.usd_attribute_model import GfVecAttributeSingleChannelModel
from omni.kit.property.usd.usd_attribute_model import MatrixBaseAttributeModel
from omni.kit.property.usd.usd_attribute_model import MdlEnumAttributeModel
from omni.kit.property.usd.usd_attribute_model import SdfAssetPathArrayAttributeItemModel
from omni.kit.property.usd.usd_attribute_model import SdfAssetPathAttributeModel
from omni.kit.property.usd.usd_attribute_model import SdfTimeCodeModel
from omni.kit.property.usd.usd_attribute_model import TfTokenAttributeModel
from omni.kit.property.usd.usd_attribute_model import UsdAttributeModel
from omni.kit.property.usd.usd_object_model import MetadataObjectModel
from omni.kit.property.usd import widgets
from omni.kit.widget.highlight_label.highlight_label import HighlightLabel
from omni import ui
from pxr import Sdf
import pxr.Sdf
from pxr import Sdr
import pxr.Tf
from pxr import Usd
import pxr.Usd
import typing
from typing import Any
import weakref as weakref
__all__: list = ['get_ui_style', 'get_model_cls', 'SdfAssetPathDelegate', 'UsdPropertiesWidgetBuilder']
class SdfAssetPathDelegate(omni.ui._ui.AbstractItemDelegate):
    """
    
        Delegate is the representation layer. TreeView calls the methods
        of the delegate to create custom widgets for each item.
        
    """
    def __init__(self, stage, attr_name, widget_kwargs):
        ...
    def _build_additional(self, widget_kwargs, item_value_model, value_model):
        """
        
                Builds the additional widgets for the asset entry.
        
                This method builds the additional widgets for the asset entry.
                
        """
    def _build_asset_entry(self, widget_kwargs, item_value_model, value_model, frame, extra_widgets):
        ...
    def _build_remove_button(self, widget_kwargs, item_value_model, value_model):
        """
        
                Builds the remove button for the asset entry.
        
                This method builds the remove button for the asset entry.
                
        """
    def build_branch(self, model, item, column_id, level, expanded):
        """
        Create a branch widget that opens or closes subtree
        """
    def build_path_field(self, widget_kwargs, item_value_model, frame, extra_widgets):
        """
        
                Builds the path field for the asset entry.
        
                This method builds the path field for the asset entry and adds it to the extra widgets.
        
                Args:
                    widget_kwargs: The widget kwargs.
                    item_value_model: The item value model.
                    frame: The frame.
                    extra_widgets: The extra widgets.
                
        """
    def build_widget(self, model, item, column_id, level, expanded):
        """
        Create a widget per column per item
        """
class UsdPropertiesWidgetBuilder:
    """
    
        Builds the properties widget for the asset entry.
    
        This class builds the properties widget for the asset entry.
        
    """
    default_range_steps: typing.ClassVar[dict] = {}
    tf_bool: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('bool')
    tf_bool_array: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('VtArray<bool>')
    tf_double: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('double')
    tf_float: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('float')
    tf_gf_mtx2d: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfMatrix2d')
    tf_gf_mtx3d: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfMatrix3d')
    tf_gf_mtx4d: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfMatrix4d')
    tf_gf_vec2d: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfVec2d')
    tf_gf_vec2f: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfVec2f')
    tf_gf_vec2h: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfVec2h')
    tf_gf_vec2i: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfVec2i')
    tf_gf_vec3d: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfVec3d')
    tf_gf_vec3f: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfVec3f')
    tf_gf_vec3h: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfVec3h')
    tf_gf_vec3i: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfVec3i')
    tf_gf_vec4d: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfVec4d')
    tf_gf_vec4f: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfVec4f')
    tf_gf_vec4h: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfVec4h')
    tf_gf_vec4i: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('GfVec4i')
    tf_half: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('pxr_half::half')
    tf_int: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('int')
    tf_int64: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('long')
    tf_sdf_asset_array_path: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('VtArray<SdfAssetPath>')
    tf_sdf_asset_path: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('SdfAssetPath')
    tf_sdf_time_code: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('SdfTimeCode')
    tf_string: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('string')
    tf_tf_token: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('TfToken')
    tf_uchar: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('unsigned char')
    tf_uint: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('unsigned int')
    tf_uint64: typing.ClassVar[pxr.Tf.Type]  # value = Tf.Type.FindByName('unsigned long')
    widget_builder_coverage_table: typing.ClassVar[dict]  # value = {Tf.Type.FindByName('pxr_half::half'): False, Tf.Type.FindByName('float'): False, Tf.Type.FindByName('double'): False, Tf.Type.FindByName('unsigned char'): False, Tf.Type.FindByName('unsigned int'): False, Tf.Type.FindByName('int'): False, Tf.Type.FindByName('long'): False, Tf.Type.FindByName('unsigned long'): False, Tf.Type.FindByName('bool'): False, Tf.Type.FindByName('VtArray<bool>'): False, Tf.Type.FindByName('string'): False, Tf.Type.FindByName('GfMatrix2d'): False, Tf.Type.FindByName('GfMatrix3d'): False, Tf.Type.FindByName('GfMatrix4d'): False, Tf.Type.FindByName('GfVec2i'): False, Tf.Type.FindByName('GfVec2h'): False, Tf.Type.FindByName('GfVec2f'): False, Tf.Type.FindByName('GfVec2d'): False, Tf.Type.FindByName('GfVec3i'): False, Tf.Type.FindByName('GfVec3h'): False, Tf.Type.FindByName('GfVec3f'): False, Tf.Type.FindByName('GfVec3d'): False, Tf.Type.FindByName('GfVec4i'): False, Tf.Type.FindByName('GfVec4h'): False, Tf.Type.FindByName('GfVec4f'): False, Tf.Type.FindByName('GfVec4d'): False, Tf.Type.FindByName('TfToken'): False, Tf.Type.FindByName('SdfAssetPath'): False, Tf.Type.FindByName('SdfTimeCode'): False, Tf.Type.FindByName('VtArray<SdfAssetPath>'): False}
    widget_builder_table: typing.ClassVar[dict]  # value = {Tf.Type.FindByName('pxr_half::half'): UsdPropertiesWidgetBuilder.floating_point_builder, Tf.Type.FindByName('float'): UsdPropertiesWidgetBuilder.floating_point_builder, Tf.Type.FindByName('double'): UsdPropertiesWidgetBuilder.floating_point_builder, Tf.Type.FindByName('unsigned char'): UsdPropertiesWidgetBuilder.integer_builder, Tf.Type.FindByName('unsigned int'): UsdPropertiesWidgetBuilder.integer_builder, Tf.Type.FindByName('int'): UsdPropertiesWidgetBuilder.integer_builder, Tf.Type.FindByName('long'): UsdPropertiesWidgetBuilder.integer_builder, Tf.Type.FindByName('unsigned long'): UsdPropertiesWidgetBuilder.integer_builder, Tf.Type.FindByName('bool'): UsdPropertiesWidgetBuilder.bool_builder, Tf.Type.FindByName('VtArray<bool>'): UsdPropertiesWidgetBuilder.bool_array_builder, Tf.Type.FindByName('string'): UsdPropertiesWidgetBuilder.string_builder, Tf.Type.FindByName('GfMatrix2d'): UsdPropertiesWidgetBuilder.gf_matrix_builder, Tf.Type.FindByName('GfMatrix3d'): UsdPropertiesWidgetBuilder.gf_matrix_builder, Tf.Type.FindByName('GfMatrix4d'): UsdPropertiesWidgetBuilder.gf_matrix_builder, Tf.Type.FindByName('GfVec2i'): UsdPropertiesWidgetBuilder.vec2_per_channel_builder, Tf.Type.FindByName('GfVec2h'): UsdPropertiesWidgetBuilder.vec2_per_channel_builder, Tf.Type.FindByName('GfVec2f'): UsdPropertiesWidgetBuilder.vec2_per_channel_builder, Tf.Type.FindByName('GfVec2d'): UsdPropertiesWidgetBuilder.vec2_per_channel_builder, Tf.Type.FindByName('GfVec3i'): UsdPropertiesWidgetBuilder.vec3_per_channel_builder, Tf.Type.FindByName('GfVec3h'): UsdPropertiesWidgetBuilder.vec3_per_channel_builder, Tf.Type.FindByName('GfVec3f'): UsdPropertiesWidgetBuilder.vec3_per_channel_builder, Tf.Type.FindByName('GfVec3d'): UsdPropertiesWidgetBuilder.vec3_per_channel_builder, Tf.Type.FindByName('GfVec4i'): UsdPropertiesWidgetBuilder.vec4_per_channel_builder, Tf.Type.FindByName('GfVec4h'): UsdPropertiesWidgetBuilder.vec4_per_channel_builder, Tf.Type.FindByName('GfVec4f'): UsdPropertiesWidgetBuilder.vec4_per_channel_builder, Tf.Type.FindByName('GfVec4d'): UsdPropertiesWidgetBuilder.vec4_per_channel_builder, Tf.Type.FindByName('TfToken'): UsdPropertiesWidgetBuilder.tftoken_builder, Tf.Type.FindByName('SdfAssetPath'): UsdPropertiesWidgetBuilder.sdf_asset_path_builder, Tf.Type.FindByName('SdfTimeCode'): UsdPropertiesWidgetBuilder.time_code_builder, Tf.Type.FindByName('VtArray<SdfAssetPath>'): UsdPropertiesWidgetBuilder.sdf_asset_path_array_builder}
    @staticmethod
    def _convert_asset_path(path: str) -> str:
        """
        
                Converts an asset path.
        
                This method converts an asset path.
        
                Args:
                    path: The path.
        
                Returns:
                    The converted asset path.
                
        """
    @staticmethod
    def _create_drag_or_slider(drag_widget, slider_widget, **kwargs):
        """
        
                Creates a drag or slider widget.
        
                This method creates a drag or slider widget.
        
                Args:
                    drag_widget: The drag widget.
                    slider_widget: The slider widget.
                    kwargs: The keyword arguments.
        
                Returns:
                    The drag or slider widget.
                
        """
    @staticmethod
    def _create_mixed_text_overlay(widget_model = None, model = None, comp = -1, content_clipping: bool = False):
        """
        
                Creates a mixed text overlay.
        
                This method creates a mixed text overlay.
        
                Args:
                    widget_model: The widget model.
                    model: The model.
                    comp: The component.
                    content_clipping: The content clipping.
        
                Returns:
                    The mixed text overlay widget.
                
        """
    @staticmethod
    def _get_attr_value_range(metadata):
        """
        
                Gets the attribute value range.
        
                This method gets the attribute value range.
        
                Args:
                    metadata: The metadata.
        
                Returns:
                    The attribute value range.
                
        """
    @staticmethod
    def _get_attr_value_soft_range(metadata, model = None, use_override = True):
        """
        
                Gets the attribute value soft range.
        
                This method gets the attribute value soft range.
        
                Args:
                    metadata: The metadata.
                    model: The model.
                    use_override: Whether to use the override.
        
                Returns:
                    The attribute value soft range.
                
        """
    @staticmethod
    def _get_attr_value_ui_type(metadata):
        """
        
                Gets the attribute value UI type.
        
                This method gets the attribute value UI type.
        
                Args:
                    metadata: The metadata.
        
                Returns:
                    The attribute value UI type.
                
        """
    @staticmethod
    def _get_display_name(attr_name, metadata):
        """
        
                Gets the display name.
        
                This method gets the display name.
        
                Args:
                    attr_name: The attribute name.
                    metadata: The metadata.
        
                Returns:
                    The display name.
                
        """
    @staticmethod
    def _get_type_name(metadata):
        """
        
                Gets the type name.
        
                This method gets the type name.
        
                Args:
                    metadata: The metadata.
        
                Returns:
                    The type name.
                
        """
    @staticmethod
    def can_accept_file_drop(payload: str, model_weak, allow_multi_files = False) -> bool:
        """
        
                Checks if the file drop is allowed.
        
                This method checks if the file drop is allowed.
        
                Args:
                    payload: The payload.
                    model_weak: The model weak.
                    allow_multi_files: Whether to allow multiple files.
        
                Returns:
                    True if the file drop is allowed, False otherwise.
                
        """
    @staticmethod
    def can_accept_prim_path_drop(payload: str, model_weak, stage, allow_multi_files = False) -> bool:
        """
        
                Checks if the payload can be accepted as a prim path drop.
        
                This method checks if the payload can be accepted as a prim path drop.
        
                Args:
                    payload: The payload.
                    model_weak: The model weak.
                    stage: The stage.
                    allow_multi_files: Whether to allow multi files.
        
                Returns:
                    bool: True if the payload can be accepted as a prim path drop, False otherwise.
                
        """
    @staticmethod
    def convert_asset_path(path: str) -> str:
        """
        
                Converts an asset path.
        
                This method converts an asset path.
        
                Args:
                    path: The path.
        
                Returns:
                    The converted asset path.
                
        """
    @staticmethod
    def create_drag_or_slider(drag_widget, slider_widget, **kwargs):
        """
        
                Creates a drag or slider widget.
        
                This method creates a drag or slider widget.
        
                Args:
                    drag_widget: The drag widget.
                    slider_widget: The slider widget.
                    kwargs: The keyword arguments.
        
                Returns:
                    The drag or slider widget.
                
        """
    @staticmethod
    def create_mixed_text_overlay(widget_model = None, model = None, comp = -1, content_clipping: bool = False):
        """
        
                Creates a mixed text overlay.
        
                This method creates a mixed text overlay.
        
                Args:
                    widget_model: The widget model.
                    model: The model.
                    comp: The component.
                    content_clipping: The content clipping.
        
                Returns:
                    The mixed text overlay widget.
                
        """
    @staticmethod
    def get_attr_value_range(metadata):
        """
        
                Gets the attribute value range.
        
                This method gets the attribute value range.
        
                Args:
                    metadata: The metadata.
        
                Returns:
                    The attribute value range.
                
        """
    @staticmethod
    def get_attr_value_soft_range(metadata, model = None, use_override = True):
        """
        
                Gets the attribute value soft range.
        
                This method gets the attribute value soft range.
        
                Args:
                    metadata: The metadata.
                    model: The model.
                    use_override: Whether to use the override.
        
                Returns:
                    The attribute value soft range.
                
        """
    @staticmethod
    def get_display_name(attr_name, metadata):
        """
        
                Gets the display name.
        
                This method gets the display name.
        
                Args:
                    attr_name: The attribute name.
                    metadata: The metadata.
        
                Returns:
                    The display name.
                
        """
    @staticmethod
    def get_type_name(metadata):
        """
        
                Gets the type name.
        
                This method gets the type name.
        
                Args:
                    metadata: The metadata.
        
                Returns:
                    The type name.
                
        """
    @staticmethod
    def is_model_readonly(model):
        """
        
                Checks if the model is readonly.
        
                This method checks if the model is readonly.
        
                Args:
                    model: The model.
        
                Returns:
                    True if the model is readonly, False otherwise.
                
        """
    @classmethod
    def _assign_asset_path_value(cls, stage_weak, model_weak, payload: str, assign_value_fn: typing.Callable[[typing.Any, str], NoneType], frame = None):
        ...
    @classmethod
    def _assign_asset_resolved_value(cls, stage_weak, model_weak, payload: str, assign_value_fn: typing.Callable[[typing.Any, str], NoneType], frame = None):
        ...
    @classmethod
    def _bool_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the bool builder for the asset entry.
        
                This method builds the bool builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The bool model.
                
        """
    @classmethod
    def _build_asset_checkpoint_ui(cls, model, frame):
        """
        
                Builds the asset checkpoint ui for the asset entry.
        
                This method builds the asset checkpoint ui for the asset entry.
        
                Args:
                    model: The model.
                    frame: The frame.
                
        """
    @classmethod
    def _build_path_field(cls, model, stage, attr_name, widget_kwargs, frame, extra_widgets):
        """
        
                Builds a path field.
        
                This method builds a path field.
        
                Args:
                    model: The model.
                    stage: The stage.
                    attr_name: The attribute name.
                    widget_kwargs: The widget kwargs.
                    frame: The frame.
                    extra_widgets: The extra widgets.
        
                Returns:
                    The path field widget and overlay widget.
                
        """
    @classmethod
    def _build_prim_path_field(cls, model, list_item_model, stage, attr_name, widget_kwargs, frame, extra_widgets):
        """
        
                Builds the prim path field for the asset entry.
        
                This method builds the prim path field for the asset entry and adds it to the extra widgets.
        
                Args:
                    model: The model.
                    list_item_model: The list item model.
                    stage: The stage.
                    attr_name: The attribute name.
                    widget_kwargs: The widget kwargs.
                    frame: The frame.
                    extra_widgets: The extra widgets.
                
        """
    @classmethod
    def _create_attribute_context_menu(cls, widget, model, comp_index = -1):
        """
        
                Creates an attribute context menu for the attribute.
        
                This method creates an attribute context menu for the attribute.
        
                Args:
                    widget: The widget.
                    model: The model.
                    comp_index: The component index.
        
                Returns:
                    The attribute context menu.
                
        """
    @classmethod
    def _create_bool_per_channel(cls, stage, attr_name, prim_paths, comp_count, type_name, tf_type, metadata, label, additional_widget_kwargs = None):
        """
        
                Creates a bool per channel.
        
                This method creates a bool per channel.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    prim_paths: The prim paths.
                    comp_count: The component count.
                    type_name: The type name.
                    tf_type: The tf type.
                    metadata: The metadata.
                    label: The label.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The bool per channel widget.
                
        """
    @classmethod
    def _create_color_or_drag_per_channel(cls, stage, attr_name, prim_paths, comp_count, type_name, tf_type, metadata, label, additional_widget_kwargs = None):
        """
        
                Creates a color or drag per channel.
        
                This method creates a color or drag per channel.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    prim_paths: The prim paths.
                    comp_count: The component count.
                    type_name: The type name.
                    tf_type: The tf type.
                    metadata: The metadata.
                    label: The label.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The color or drag per channel widget.
                
        """
    @classmethod
    def _create_color_or_multidrag(cls, stage, attr_name, prim_paths, comp_count, type_name, tf_type, metadata, label, additional_widget_kwargs = None):
        """
        
                Creates a color or multidrag.
        
                This method creates a color or multidrag.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    prim_paths: The prim paths.
                    comp_count: The component count.
                    type_name: The type name.
                    tf_type: The tf type.
                    metadata: The metadata.
                    label: The label.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The color or multidrag widget.
                
        """
    @classmethod
    def _create_control_state(cls, model, value_widget = None, mixed_overlay = None, extra_widgets = None, **kwargs):
        """
        
                Creates a control state.
        
                This method creates a control state.
        
                Args:
                    model: The model.
                    value_widget: The value widget.
                    mixed_overlay: The mixed overlay.
                    extra_widgets: The extra widgets.
                    kwargs: The keyword arguments.
                
        """
    @classmethod
    def _create_drag_per_channel_with_labels_and_control(cls, drag_field_widget, slider_field_widget, models, metadata, labels, **kwargs):
        """
        
                Creates a drag per channel with labels and control.
        
                This method creates a drag per channel with labels and control.
        
                Args:
                    drag_field_widget: The drag field widget.
                    slider_field_widget: The slider field widget.
                    models: The models.
                    metadata: The metadata.
                    labels: The labels.
                    kwargs: The keyword arguments.
        
                Returns:
                    HStack widget.
                
        """
    @classmethod
    def _create_filepath_for_ui_type(cls, stage, attr_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs, additional_widget_kwargs):
        ...
    @classmethod
    def _create_float_drag_per_channel_with_labels_and_control(cls, models, metadata, labels, **kwargs):
        """
        
                Creates a float drag per channel with labels and control.
        
                This method creates a float drag per channel with labels and control.
        
                Args:
                    models: The models.
                    metadata: The metadata.
                    labels: The labels.
                    kwargs: The keyword arguments.
        
                Returns:
                    HStack widget.
                
        """
    @classmethod
    def _create_int_drag_per_channel_with_labels_and_control(cls, models, metadata, labels, **kwargs):
        """
        
                Creates a int drag per channel with labels and control.
        
                This method creates a int drag per channel with labels and control.
        
                Args:
                    models: The models.
                    metadata: The metadata.
                    labels: The labels.
                    kwargs: The keyword arguments.
        
                Returns:
                    HStack widget.
                
        """
    @classmethod
    def _create_label(cls, attr_name, metadata = None, additional_label_kwargs = None):
        """
        
                Creates a label for the attribute.
        
                This method creates a label for the attribute.
        
                Args:
                    attr_name: The attribute name.
                    metadata: The metadata.
                    additional_label_kwargs: The additional label kwargs.
        
                Returns:
                    The label widget.
                
        """
    @classmethod
    def _create_multi_drag_with_labels(cls, drag_field_widget, model, labels, comp_count, **kwargs):
        """
        
                Creates a multi drag with labels.
        
                This method creates a multi drag with labels.
        
                Args:
                    drag_field_widget: The drag field widget.
                    model: The model.
                    labels: The labels.
                    comp_count: The component count.
                    kwargs: The keyword arguments.
        
                Returns:
                    The multi drag with widget and overlay widget.
                
        """
    @classmethod
    def _create_multi_float_drag_with_labels(cls, model, labels, comp_count, **kwargs):
        """
        
                Creates a multi float drag with labels.
        
                This method creates a multi float drag with labels.
        
                Args:
                    model: The model.
                    labels: The labels.
                    comp_count: The component count.
                    kwargs: The keyword arguments.
        
                Returns:
                    The multi float drag with widget and overlay widget.
                
        """
    @classmethod
    def _create_multi_int_drag_with_labels(cls, model, labels, comp_count, **kwargs):
        """
        
                Creates a multi int drag with labels.
        
                This method creates a multi int drag with labels.
        
                Args:
                    model: The model.
                    labels: The labels.
                    comp_count: The component count.
                    kwargs: The keyword arguments.
        
                Returns:
                    The multi int drag with widget and overlay widget.
                
        """
    @classmethod
    def _create_path_widget(cls, model, stage, attr_name, metadata, prim_paths, additional_label_kwargs, additional_widget_kwargs):
        ...
    @classmethod
    def _create_text_label(cls, attr_name, metadata = None, additional_label_kwargs = None):
        """
        
                Creates a text label for the attribute.
        
                This method creates a text label for the attribute.
        
                Args:
                    attr_name: The attribute name.
                    metadata: The metadata.
                    additional_label_kwargs: The additional label kwargs.
        
                Returns:
                    The text label widget.
                
        """
    @classmethod
    def _fallback_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the fallback builder for the asset entry.
        
                This method builds the fallback builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The fallback builder model.
                
        """
    @classmethod
    def _floating_point_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the floating point builder for the asset entry.
        
                This method builds the floating point builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The floating point builder model.
                
        """
    @classmethod
    def _generate_tooltip_string(cls, attr_name, metadata):
        """
        
                Generates a tooltip string for the attribute.
        
                This method generates a tooltip string for the attribute.
        
                Args:
                    attr_name: The attribute name.
                    metadata: The metadata.
        
                Returns:
                    The tooltip string.
                
        """
    @classmethod
    def _get_alignment(cls):
        """
        
                Gets the alignment for the label.
        
                This method gets the alignment for the label.
        
                Returns:
                    The alignment.
                
        """
    @classmethod
    def _get_attr_value_range_kwargs(cls, metadata):
        """
        
                Gets the attribute value range kwargs.
        
                This method gets the attribute value range kwargs.
        
                Args:
                    metadata: The metadata.
        
                Returns:
                    The attribute value range kwargs.
                
        """
    @classmethod
    def _get_attr_value_soft_range_kwargs(cls, metadata, model = None):
        """
        
                Gets the attribute value soft range kwargs.
        
                This method gets the attribute value soft range kwargs.
        
                Args:
                    metadata: The metadata.
                    model: The model.
        
                Returns:
                    The attribute value soft range kwargs.
                
        """
    @classmethod
    def _get_layers_with_strongest_value_opinions_on_model(cls, model, stage) -> list[pxr.Sdf.Layer]:
        ...
    @classmethod
    def _integer_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the integer builder for the asset entry.
        
                This method builds the integer builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The integer model.
                
        """
    @classmethod
    def _relationship_builder(cls, stage, attr_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the relationship builder for the asset entry.
        
                This method builds the relationship builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The relationship builder model.
                
        """
    @classmethod
    def _sdf_asset_path_array_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the sdf asset path array builder for the asset entry.
        
                This method builds the sdf asset path array builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The sdf asset path array builder model.
                
        """
    @classmethod
    def _sdf_asset_path_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the sdf asset path builder for the asset entry.
        
                This method builds the sdf asset path builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The sdf asset path builder model.
                
        """
    @classmethod
    def _setup_soft_float_dynamic_range(cls, attr_name, metadata, default_step, model, widget):
        """
        
                Sets up the soft float dynamic range.
        
                This method sets up the soft float dynamic range.
        
                Args:
                    attr_name: The attribute name.
                    metadata: The metadata.
                    default_step: The default step.
                    model: The model.
                    widget: The widget.
                
        """
    @classmethod
    def _string_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the string builder for the asset entry.
        
                This method builds the string builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The string builder model.
                
        """
    @classmethod
    def _tftoken_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the tftoken builder for the asset entry.
        
                This method builds the tftoken builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The tftoken builder model.
                
        """
    @classmethod
    def _time_code_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Creates a time code builder.
        
                This method creates a time code builder.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The time code builder model.
                
        """
    @classmethod
    def _vec2_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The entire vector is built as one multi-drag field
        
                This method builds the vec2 builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The vec2 builder model.
                
        """
    @classmethod
    def _vec2_per_channel_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The vector is split into components and each one has their own drag field and status control
                
        """
    @classmethod
    def _vec3_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The entire vector is built as one multi-drag field
                
        """
    @classmethod
    def _vec3_per_channel_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The vector is split into components and each one has their own drag field and status control
                
        """
    @classmethod
    def _vec4_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The entire vector is built as one multi-drag field
                
        """
    @classmethod
    def _vec4_per_channel_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The vector is split into components and each one has their own drag field and status control
                
        """
    @classmethod
    def bool_array_builder(cls: typing.Type[ForwardRef('UsdPropertiesWidgetBuilder')], stage: pxr.Usd.Stage, attr_name: str, type_name: pxr.Sdf.ValueTypeName, metadata: dict, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs: typing.Optional[dict] = None, additional_widget_kwargs: typing.Optional[dict] = None):
        """
        
                The array is split into components and each one has their own checkBox
        
                This method builds the bool array builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The bool array builder model.
                
        """
    @classmethod
    def bool_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the bool builder for the asset entry.
        
                This method builds the bool builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The bool model.
                
        """
    @classmethod
    def build(cls, stage, attr_name, metadata, property_type, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the properties widget for the asset entry.
        
                This method builds the properties widget for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    metadata: The metadata.
                    property_type: The property type.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The properties widget model.
                
        """
    @classmethod
    def build_path_field(cls, model, stage, attr_name, widget_kwargs, frame, extra_widgets):
        """
        
                Builds a path field.
        
                This method builds a path field.
        
                Args:
                    model: The model.
                    stage: The stage.
                    attr_name: The attribute name.
                    widget_kwargs: The widget kwargs.
                    frame: The frame.
                    extra_widgets: The extra widgets.
        
                Returns:
                    The path field widget and overlay widget.
                
        """
    @classmethod
    def build_prim_path_field(cls, model, list_item_model, stage, attr_name, widget_kwargs, frame, extra_widgets):
        """
        
                Builds the prim path field for the asset entry.
        
                This method builds the prim path field for the asset entry and adds it to the extra widgets.
        
                Args:
                    model: The model.
                    list_item_model: The list item model.
                    stage: The stage.
                    attr_name: The attribute name.
                    widget_kwargs: The widget kwargs.
                    frame: The frame.
                    extra_widgets: The extra widgets.
                
        """
    @classmethod
    def create_attribute_context_menu(cls, widget, model, comp_index = -1):
        """
        
                Creates an attribute context menu for the attribute.
        
                This method creates an attribute context menu for the attribute.
        
                Args:
                    widget: The widget.
                    model: The model.
                    comp_index: The component index.
        
                Returns:
                    The attribute context menu.
                
        """
    @classmethod
    def create_bool_per_channel(cls, stage, attr_name, prim_paths, comp_count, type_name, tf_type, metadata, label, additional_widget_kwargs = None):
        """
        
                Creates a bool per channel.
        
                This method creates a bool per channel.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    prim_paths: The prim paths.
                    comp_count: The component count.
                    type_name: The type name.
                    tf_type: The tf type.
                    metadata: The metadata.
                    label: The label.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The bool per channel widget.
                
        """
    @classmethod
    def create_color_or_drag_per_channel(cls, stage, attr_name, prim_paths, comp_count, type_name, tf_type, metadata, label, additional_widget_kwargs = None):
        """
        
                Creates a color or drag per channel.
        
                This method creates a color or drag per channel.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    prim_paths: The prim paths.
                    comp_count: The component count.
                    type_name: The type name.
                    tf_type: The tf type.
                    metadata: The metadata.
                    label: The label.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The color or drag per channel widget.
                
        """
    @classmethod
    def create_color_or_multidrag(cls, stage, attr_name, prim_paths, comp_count, type_name, tf_type, metadata, label, additional_widget_kwargs = None):
        """
        
                Creates a color or multidrag.
        
                This method creates a color or multidrag.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    prim_paths: The prim paths.
                    comp_count: The component count.
                    type_name: The type name.
                    tf_type: The tf type.
                    metadata: The metadata.
                    label: The label.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The color or multidrag widget.
                
        """
    @classmethod
    def create_control_state(cls, model, value_widget = None, mixed_overlay = None, extra_widgets = None, **kwargs):
        """
        
                Creates a control state.
        
                This method creates a control state.
        
                Args:
                    model: The model.
                    value_widget: The value widget.
                    mixed_overlay: The mixed overlay.
                    extra_widgets: The extra widgets.
                    kwargs: The keyword arguments.
                
        """
    @classmethod
    def create_drag_per_channel_with_labels_and_control(cls, drag_field_widget, slider_field_widget, models, metadata, labels, **kwargs):
        """
        
                Creates a drag per channel with labels and control.
        
                This method creates a drag per channel with labels and control.
        
                Args:
                    drag_field_widget: The drag field widget.
                    slider_field_widget: The slider field widget.
                    models: The models.
                    metadata: The metadata.
                    labels: The labels.
                    kwargs: The keyword arguments.
        
                Returns:
                    HStack widget.
                
        """
    @classmethod
    def create_float_drag_per_channel_with_labels_and_control(cls, models, metadata, labels, **kwargs):
        """
        
                Creates a float drag per channel with labels and control.
        
                This method creates a float drag per channel with labels and control.
        
                Args:
                    models: The models.
                    metadata: The metadata.
                    labels: The labels.
                    kwargs: The keyword arguments.
        
                Returns:
                    HStack widget.
                
        """
    @classmethod
    def create_int_drag_per_channel_with_labels_and_control(cls, models, metadata, labels, **kwargs):
        """
        
                Creates a int drag per channel with labels and control.
        
                This method creates a int drag per channel with labels and control.
        
                Args:
                    models: The models.
                    metadata: The metadata.
                    labels: The labels.
                    kwargs: The keyword arguments.
        
                Returns:
                    HStack widget.
                
        """
    @classmethod
    def create_label(cls, attr_name, metadata = None, additional_label_kwargs = None):
        """
        
                Creates a label for the attribute.
        
                This method creates a label for the attribute.
        
                Args:
                    attr_name: The attribute name.
                    metadata: The metadata.
                    additional_label_kwargs: The additional label kwargs.
        
                Returns:
                    The label widget.
                
        """
    @classmethod
    def create_multi_drag_with_labels(cls, drag_field_widget, model, labels, comp_count, **kwargs):
        """
        
                Creates a multi drag with labels.
        
                This method creates a multi drag with labels.
        
                Args:
                    drag_field_widget: The drag field widget.
                    model: The model.
                    labels: The labels.
                    comp_count: The component count.
                    kwargs: The keyword arguments.
        
                Returns:
                    The multi drag with widget and overlay widget.
                
        """
    @classmethod
    def create_multi_float_drag_with_labels(cls, model, labels, comp_count, **kwargs):
        """
        
                Creates a multi float drag with labels.
        
                This method creates a multi float drag with labels.
        
                Args:
                    model: The model.
                    labels: The labels.
                    comp_count: The component count.
                    kwargs: The keyword arguments.
        
                Returns:
                    The multi float drag with widget and overlay widget.
                
        """
    @classmethod
    def create_multi_int_drag_with_labels(cls, model, labels, comp_count, **kwargs):
        """
        
                Creates a multi int drag with labels.
        
                This method creates a multi int drag with labels.
        
                Args:
                    model: The model.
                    labels: The labels.
                    comp_count: The component count.
                    kwargs: The keyword arguments.
        
                Returns:
                    The multi int drag with widget and overlay widget.
                
        """
    @classmethod
    def create_text_label(cls, attr_name, metadata = None, additional_label_kwargs = None):
        """
        
                Creates a text label for the attribute.
        
                This method creates a text label for the attribute.
        
                Args:
                    attr_name: The attribute name.
                    metadata: The metadata.
                    additional_label_kwargs: The additional label kwargs.
        
                Returns:
                    The text label widget.
                
        """
    @classmethod
    def fallback_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the fallback builder for the asset entry.
        
                This method builds the fallback builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The fallback builder model.
                
        """
    @classmethod
    def floating_point_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the floating point builder for the asset entry.
        
                This method builds the floating point builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The floating point builder model.
                
        """
    @classmethod
    def generate_tooltip_string(cls, attr_name, metadata):
        """
        
                Generates a tooltip string for the attribute.
        
                This method generates a tooltip string for the attribute.
        
                Args:
                    attr_name: The attribute name.
                    metadata: The metadata.
        
                Returns:
                    The tooltip string.
                
        """
    @classmethod
    def get_attr_value_range_kwargs(cls, metadata):
        """
        
                Gets the attribute value range kwargs.
        
                This method gets the attribute value range kwargs.
        
                Args:
                    metadata: The metadata.
        
                Returns:
                    The attribute value range kwargs.
                
        """
    @classmethod
    def get_attr_value_soft_range_kwargs(cls, metadata, model = None):
        """
        
                Gets the attribute value soft range kwargs.
        
                This method gets the attribute value soft range kwargs.
        
                Args:
                    metadata: The metadata.
                    model: The model.
        
                Returns:
                    The attribute value soft range kwargs.
                
        """
    @classmethod
    def gf_matrix_builder(cls: typing.Type[ForwardRef('UsdPropertiesWidgetBuilder')], stage: pxr.Usd.Stage, attr_name: str, type_name: pxr.Sdf.ValueTypeName, metadata: dict, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs: typing.Optional[dict] = None, additional_widget_kwargs: typing.Optional[dict] = None) -> typing.Optional[omni.kit.property.usd.usd_attribute_model.GfMatrixAttributeModel]:
        """
        
                Builds the gf matrix builder for the asset entry.
        
                This method builds the gf matrix builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The gf matrix builder model.
                
        """
    @classmethod
    def init_builder_table(cls):
        """
        
                Initializes the builder table.
        
                This method initializes the builder table.
                
        """
    @classmethod
    def integer_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the integer builder for the asset entry.
        
                This method builds the integer builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The integer model.
                
        """
    @classmethod
    def matrix_builder(cls: typing.Type[ForwardRef('UsdPropertiesWidgetBuilder')], matrix_model: omni.kit.property.usd.usd_attribute_model.MatrixBaseAttributeModel, column_count: int, stage: pxr.Usd.Stage, attr_name: str, metadata: dict, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs: typing.Optional[dict] = None, additional_widget_kwargs: typing.Optional[dict] = None) -> omni.kit.property.usd.usd_attribute_model.MatrixBaseAttributeModel:
        """
        
                Builds the matrix builder for the asset entry.
        
                This method builds the matrix builder for the asset entry.
        
                Args:
                    matrix_model: The matrix model.
                    column_count: The column count.
                    stage: The stage.
                    attr_name: The attribute name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The matrix builder model.
                
        """
    @classmethod
    def relationship_builder(cls, stage, attr_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the relationship builder for the asset entry.
        
                This method builds the relationship builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The relationship builder model.
                
        """
    @classmethod
    def reset_builder_coverage_table(cls):
        """
        
                Resets the builder coverage table.
        
                This method resets the builder coverage table.
                
        """
    @classmethod
    def sdf_asset_path_array_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the sdf asset path array builder for the asset entry.
        
                This method builds the sdf asset path array builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The sdf asset path array builder model.
                
        """
    @classmethod
    def sdf_asset_path_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the sdf asset path builder for the asset entry.
        
                This method builds the sdf asset path builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The sdf asset path builder model.
                
        """
    @classmethod
    def shutdown(cls):
        """
        
                Shuts down the builder.
        
                This method shuts down the builder.
                
        """
    @classmethod
    def startup(cls):
        """
        
                Starts up the builder.
        
                This method starts up the builder.
                
        """
    @classmethod
    def string_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the string builder for the asset entry.
        
                This method builds the string builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The string builder model.
                
        """
    @classmethod
    def tftoken_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Builds the tftoken builder for the asset entry.
        
                This method builds the tftoken builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The tftoken builder model.
                
        """
    @classmethod
    def time_code_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                Creates a time code builder.
        
                This method creates a time code builder.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The time code builder model.
                
        """
    @classmethod
    def validate_url(cls, model, layer, on_complete) -> None:
        """
        Validates model string as URL and calls on_complete with either None for no URL, omni.client.Result.OK or omni.client.Result.ERROR.
        
                Args:
                    model (ui.SimpleStringModel): model to read string from
                    layer (Sdf.Layer): Layer handle.
                    on_complete (callable): Function to call when completed.
                
        """
    @classmethod
    def vec2_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The entire vector is built as one multi-drag field
        
                This method builds the vec2 builder for the asset entry.
        
                Args:
                    stage: The stage.
                    attr_name: The attribute name.
                    type_name: The type name.
                    metadata: The metadata.
                    prim_paths: The prim paths.
                    additional_label_kwargs: The additional label kwargs.
                    additional_widget_kwargs: The additional widget kwargs.
        
                Returns:
                    The vec2 builder model.
                
        """
    @classmethod
    def vec2_per_channel_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The vector is split into components and each one has their own drag field and status control
                
        """
    @classmethod
    def vec3_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The entire vector is built as one multi-drag field
                
        """
    @classmethod
    def vec3_per_channel_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The vector is split into components and each one has their own drag field and status control
                
        """
    @classmethod
    def vec4_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The entire vector is built as one multi-drag field
                
        """
    @classmethod
    def vec4_per_channel_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The vector is split into components and each one has their own drag field and status control
                
        """
def _get_plus_glyph(*args, **kwargs):
    ...
def get_model_cls(cls, args, key = 'model_cls'):
    """
    
        Retrieves the model class from the arguments.
    
        Args:
            cls: The default model class.
            args: The arguments.
            key: The key to retrieve the model class from the arguments.
    
        Returns:
            The model class.
        
    """
def get_model_kwargs(args, key = 'model_kwargs'):
    """
    
        Retrieves the model kwargs from the arguments.
    
        Args:
            args: The arguments.
            key: The key to retrieve the model kwargs from the arguments.
    
        Returns:
            The model kwargs.
        
    """
def get_ui_style():
    """
    
        Retrieves the UI style from the settings.
    
        Returns:
            str: The UI style.
        
    """
def is_relative_path(path: str) -> bool:
    """
    
        Checks if the path is a relative path.
    
        Args:
            path: The path to check.
    
        Returns:
            bool: True if the path is a relative path, False otherwise.
        
    """
HORIZONTAL_SPACING: int = 4
LABEL_HEIGHT: int = 18
LABEL_WIDTH: int = 160
LABEL_WIDTH_LIGHT: int = 235
