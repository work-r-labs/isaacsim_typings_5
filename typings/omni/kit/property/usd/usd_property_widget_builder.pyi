from __future__ import annotations
import asyncio as asyncio
import carb as carb
import fnmatch as fnmatch
from functools import lru_cache
import omni as omni
from omni.client.utils import utils as clientutils
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
from omni.kit.widget.highlight_label.highlight_label import HighlightLabel
from omni import ui
import pathlib
import pxr.Sdf
from pxr import Sdf
from pxr import Sdr
import pxr.Tf
from pxr import Usd
import pxr.Usd
import typing
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
        ...
    def _build_asset_entry(self, widget_kwargs, item_value_model, value_model, frame, extra_widgets):
        ...
    def _build_remove_button(self, widget_kwargs, item_value_model, value_model):
        ...
    def build_branch(self, model, item, column_id, level, expanded):
        """
        Create a branch widget that opens or closes subtree
        """
    def build_path_field(self, widget_kwargs, item_value_model, frame, extra_widgets):
        ...
    def build_widget(self, model, item, column_id, level, expanded):
        """
        Create a widget per column per item
        """
class UsdPropertiesWidgetBuilder:
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
        ...
    @staticmethod
    def _create_drag_or_slider(drag_widget, slider_widget, **kwargs):
        ...
    @staticmethod
    def _create_mixed_text_overlay(widget_model = None, model = None, comp = -1, content_clipping: bool = False):
        ...
    @staticmethod
    def _get_attr_value_range(metadata):
        ...
    @staticmethod
    def _get_attr_value_soft_range(metadata, model = None, use_override = True):
        ...
    @staticmethod
    def _get_attr_value_ui_type(metadata):
        ...
    @staticmethod
    def _get_display_name(attr_name, metadata):
        ...
    @staticmethod
    def _get_type_name(metadata):
        ...
    @staticmethod
    def can_accept_file_drop(payload: str, model_weak, allow_multi_files = False) -> bool:
        ...
    @staticmethod
    def can_accept_prim_path_drop(payload: str, model_weak, stage, allow_multi_files = False) -> bool:
        ...
    @staticmethod
    def convert_asset_path(path: str) -> str:
        ...
    @staticmethod
    def create_drag_or_slider(drag_widget, slider_widget, **kwargs):
        ...
    @staticmethod
    def create_mixed_text_overlay(widget_model = None, model = None, comp = -1, content_clipping: bool = False):
        ...
    @staticmethod
    def get_attr_value_range(metadata):
        ...
    @staticmethod
    def get_attr_value_soft_range(metadata, model = None, use_override = True):
        ...
    @staticmethod
    def get_display_name(attr_name, metadata):
        ...
    @staticmethod
    def get_type_name(metadata):
        ...
    @staticmethod
    def is_model_readonly(model):
        ...
    @classmethod
    def _assign_asset_path_value(cls, stage_weak, model_weak, payload: str, assign_value_fn: typing.Callable[[typing.Any, str], NoneType], frame = None):
        ...
    @classmethod
    def _assign_asset_resolved_value(cls, stage_weak, model_weak, payload: str, assign_value_fn: typing.Callable[[typing.Any, str], NoneType], frame = None):
        ...
    @classmethod
    def _bool_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def _build_asset_checkpoint_ui(cls, model, frame):
        ...
    @classmethod
    def _build_path_field(cls, model, stage, attr_name, widget_kwargs, frame, extra_widgets):
        ...
    @classmethod
    def _build_prim_path_field(cls, model, list_item_model, stage, attr_name, widget_kwargs, frame, extra_widgets):
        ...
    @classmethod
    def _create_attribute_context_menu(cls, widget, model, comp_index = -1):
        ...
    @classmethod
    def _create_bool_per_channel(cls, stage, attr_name, prim_paths, comp_count, type_name, tf_type, metadata, label, additional_widget_kwargs = None):
        ...
    @classmethod
    def _create_color_or_drag_per_channel(cls, stage, attr_name, prim_paths, comp_count, type_name, tf_type, metadata, label, additional_widget_kwargs = None):
        ...
    @classmethod
    def _create_color_or_multidrag(cls, stage, attr_name, prim_paths, comp_count, type_name, tf_type, metadata, label, additional_widget_kwargs = None):
        ...
    @classmethod
    def _create_control_state(cls, model, value_widget = None, mixed_overlay = None, extra_widgets = None, **kwargs):
        ...
    @classmethod
    def _create_drag_per_channel_with_labels_and_control(cls, drag_field_widget, slider_field_widget, models, metadata, labels, **kwargs):
        ...
    @classmethod
    def _create_filepath_for_ui_type(cls, stage, attr_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs, additional_widget_kwargs):
        ...
    @classmethod
    def _create_float_drag_per_channel_with_labels_and_control(cls, models, metadata, labels, **kwargs):
        ...
    @classmethod
    def _create_int_drag_per_channel_with_labels_and_control(cls, models, metadata, labels, **kwargs):
        ...
    @classmethod
    def _create_label(cls, attr_name, metadata = None, additional_label_kwargs = None):
        ...
    @classmethod
    def _create_multi_drag_with_labels(cls, drag_field_widget, model, labels, comp_count, **kwargs):
        ...
    @classmethod
    def _create_multi_float_drag_with_labels(cls, model, labels, comp_count, **kwargs):
        ...
    @classmethod
    def _create_multi_int_drag_with_labels(cls, model, labels, comp_count, **kwargs):
        ...
    @classmethod
    def _create_path_widget(cls, model, stage, attr_name, metadata, prim_paths, additional_label_kwargs, additional_widget_kwargs):
        ...
    @classmethod
    def _create_text_label(cls, attr_name, metadata = None, additional_label_kwargs = None):
        ...
    @classmethod
    def _fallback_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def _floating_point_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def _generate_tooltip_string(cls, attr_name, metadata):
        ...
    @classmethod
    def _get_alignment(cls):
        ...
    @classmethod
    def _get_attr_value_range_kwargs(cls, metadata):
        ...
    @classmethod
    def _get_attr_value_soft_range_kwargs(cls, metadata, model = None):
        ...
    @classmethod
    def _get_layers_with_strongest_value_opinions_on_model(cls, model, stage) -> list[pxr.Sdf.Layer]:
        ...
    @classmethod
    def _integer_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def _relationship_builder(cls, stage, attr_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def _sdf_asset_path_array_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def _sdf_asset_path_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def _setup_soft_float_dynamic_range(cls, attr_name, metadata, default_step, model, widget):
        ...
    @classmethod
    def _string_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def _tftoken_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def _time_code_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def _vec2_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        
                The entire vector is built as one multi-drag field
                
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
                
        """
    @classmethod
    def bool_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def build(cls, stage, attr_name, metadata, property_type, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def build_path_field(cls, model, stage, attr_name, widget_kwargs, frame, extra_widgets):
        ...
    @classmethod
    def build_prim_path_field(cls, model, list_item_model, stage, attr_name, widget_kwargs, frame, extra_widgets):
        ...
    @classmethod
    def create_attribute_context_menu(cls, widget, model, comp_index = -1):
        ...
    @classmethod
    def create_bool_per_channel(cls, stage, attr_name, prim_paths, comp_count, type_name, tf_type, metadata, label, additional_widget_kwargs = None):
        ...
    @classmethod
    def create_color_or_drag_per_channel(cls, stage, attr_name, prim_paths, comp_count, type_name, tf_type, metadata, label, additional_widget_kwargs = None):
        ...
    @classmethod
    def create_color_or_multidrag(cls, stage, attr_name, prim_paths, comp_count, type_name, tf_type, metadata, label, additional_widget_kwargs = None):
        ...
    @classmethod
    def create_control_state(cls, model, value_widget = None, mixed_overlay = None, extra_widgets = None, **kwargs):
        ...
    @classmethod
    def create_drag_per_channel_with_labels_and_control(cls, drag_field_widget, slider_field_widget, models, metadata, labels, **kwargs):
        ...
    @classmethod
    def create_float_drag_per_channel_with_labels_and_control(cls, models, metadata, labels, **kwargs):
        ...
    @classmethod
    def create_int_drag_per_channel_with_labels_and_control(cls, models, metadata, labels, **kwargs):
        ...
    @classmethod
    def create_label(cls, attr_name, metadata = None, additional_label_kwargs = None):
        ...
    @classmethod
    def create_multi_drag_with_labels(cls, drag_field_widget, model, labels, comp_count, **kwargs):
        ...
    @classmethod
    def create_multi_float_drag_with_labels(cls, model, labels, comp_count, **kwargs):
        ...
    @classmethod
    def create_multi_int_drag_with_labels(cls, model, labels, comp_count, **kwargs):
        ...
    @classmethod
    def create_text_label(cls, attr_name, metadata = None, additional_label_kwargs = None):
        ...
    @classmethod
    def fallback_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def floating_point_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def generate_tooltip_string(cls, attr_name, metadata):
        ...
    @classmethod
    def get_attr_value_range_kwargs(cls, metadata):
        ...
    @classmethod
    def get_attr_value_soft_range_kwargs(cls, metadata, model = None):
        ...
    @classmethod
    def gf_matrix_builder(cls: typing.Type[ForwardRef('UsdPropertiesWidgetBuilder')], stage: pxr.Usd.Stage, attr_name: str, type_name: pxr.Sdf.ValueTypeName, metadata: dict, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs: typing.Optional[dict] = None, additional_widget_kwargs: typing.Optional[dict] = None) -> typing.Optional[omni.kit.property.usd.usd_attribute_model.GfMatrixAttributeModel]:
        ...
    @classmethod
    def init_builder_table(cls):
        ...
    @classmethod
    def integer_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def matrix_builder(cls: typing.Type[ForwardRef('UsdPropertiesWidgetBuilder')], matrix_model: omni.kit.property.usd.usd_attribute_model.MatrixBaseAttributeModel, column_count: int, stage: pxr.Usd.Stage, attr_name: str, metadata: dict, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs: typing.Optional[dict] = None, additional_widget_kwargs: typing.Optional[dict] = None) -> omni.kit.property.usd.usd_attribute_model.MatrixBaseAttributeModel:
        ...
    @classmethod
    def relationship_builder(cls, stage, attr_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def reset_builder_coverage_table(cls):
        ...
    @classmethod
    def sdf_asset_path_array_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def sdf_asset_path_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def shutdown(cls):
        ...
    @classmethod
    def startup(cls):
        ...
    @classmethod
    def string_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def tftoken_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    @classmethod
    def time_code_builder(cls, stage, attr_name, type_name, metadata, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
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
    ...
def get_model_kwargs(args, key = 'model_kwargs'):
    ...
def get_ui_style():
    ...
def is_relative_path(path: str) -> bool:
    ...
HORIZONTAL_SPACING: int = 4
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons')
LABEL_HEIGHT: int = 18
LABEL_WIDTH: int = 160
LABEL_WIDTH_LIGHT: int = 235
