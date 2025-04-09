from __future__ import annotations
import dataclasses
from dataclasses import dataclass
import omni as omni
from omni.kit.property.adapter.core.scripts.core_adapter import StageAdapter
from omni.kit.property.usd.custom_layout_helper import CustomLayoutFrame
from omni.kit.property.usd.custom_layout_helper import CustomLayoutGroup
from omni.kit.property.usd.custom_layout_helper import CustomLayoutProperty
from omni.kit.property.usd.usd_property_widget import MultiSchemaPropertiesWidget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from omni.kit.property.usd.usd_property_widget import create_primspec_bool
from omni.kit.property.usd.usd_property_widget import create_primspec_int
from omni import ui
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
import typing
__all__ = ['CustomAttributeInfo', 'CustomLayoutFrame', 'CustomLayoutGroup', 'CustomLayoutProperty', 'GeometrySchemaAttributesWidget', 'ImageableSchemaAttributesWidget', 'MultiSchemaPropertiesWidget', 'Sdf', 'StageAdapter', 'Usd', 'UsdGeom', 'UsdPropertyUiEntry', 'create_primspec_bool', 'create_primspec_int', 'dataclass', 'omni', 'ui']
class CustomAttributeInfo:
    """
    CustomAttributeInfo(schema_name: str, display_name: str, type_name: str, default_value: Any, predicate: Callable[[Any], bool] = None)
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'schema_name': Field(name='schema_name',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'display_name': Field(name='display_name',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'type_name': Field(name='type_name',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'default_value': Field(name='default_value',type=typing.Any,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'predicate': Field(name='predicate',type=typing.Callable[[typing.Any], bool],default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=True)
    __match_args__: typing.ClassVar[tuple] = ('schema_name', 'display_name', 'type_name', 'default_value', 'predicate')
    predicate = None
    def __delattr__(self, name):
        ...
    def __eq__(self, other):
        ...
    def __hash__(self):
        ...
    def __init__(self, schema_name: str, display_name: str, type_name: str, default_value: typing.Any, predicate: typing.Callable[[typing.Any], bool] = None) -> None:
        ...
    def __repr__(self):
        ...
    def __setattr__(self, name, value):
        ...
    def get_metadata(self):
        ...
    def is_supported(self, prim):
        ...
class GeometrySchemaAttributesWidget(omni.kit.property.usd.usd_property_widget.MultiSchemaPropertiesWidget):
    def __init__(self, title: str, schema, schema_subclasses: list, include_list: list = None, exclude_list: list = None):
        """
        
                Constructor.
        
                Args:
                    title (str): Title of the widgets on the Collapsable Frame.
                    schema: The USD IsA schema or applied API schema to filter attributes.
                    schema_subclasses (list): list of subclasses
                    include_list (list): list of additional schema named to add
                    exclude_list (list): list of additional schema named to remove
                
        """
    def _customize_props_layout(self, attrs):
        ...
    def _inverse_bool_builder(self, stage, attr_name, metadata, property_type, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        ...
    def _is_prim_refinement_level_supported(self, prim):
        ...
    def get_additional_kwargs(self, ui_prop: omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry):
        """
        
                Override this function if you want to supply additional arguments when building the label or ui widget.
                
        """
    def on_new_payload(self, payload):
        """
        
                See PropertyWidget.on_new_payload
                
        """
class ImageableSchemaAttributesWidget(omni.kit.property.usd.usd_property_widget.MultiSchemaPropertiesWidget):
    def __init__(self, title: str, schema, schema_subclasses: list, include_list: list = None, exclude_list: list = None):
        """
        
                Constructor.
        
                Args:
                    title (str): Title of the widgets on the Collapsable Frame.
                    schema: The USD IsA schema or applied API schema to filter attributes.
                    schema_subclasses (list): list of subclasses
                    include_list (list): list of additional schema named to add
                    exclude_list (list): list of additional schema named to remove
                
        """
    def _customize_props_layout(self, attrs):
        ...
    def _is_prim_single_sided_supported(self, prim):
        ...
    def add_custom_attribute(self, attribute_name, display_name, type_name = 'bool', default_value = False, predicate: typing.Callable[[typing.Any], bool] = None):
        """
        
                Add custom attribute with placeholder.
                
        """
    def on_new_payload(self, payload):
        """
        
                See PropertyWidget.on_new_payload
                
        """
    def remove_custom_attribute(self, attribute_name):
        ...
