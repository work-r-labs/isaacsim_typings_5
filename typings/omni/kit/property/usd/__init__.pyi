"""
This module provides USD property widgets and related utilities for use in the Omniverse Kit.
"""
from __future__ import annotations
import enum
from enum import IntEnum
from omni.kit.property.usd.control_state_manager import ControlStateManager
from omni.kit.property.usd.custom_layout_helper import CustomLayoutFrame
from omni.kit.property.usd.custom_layout_helper import CustomLayoutGroup
from omni.kit.property.usd.custom_layout_helper import CustomLayoutProperty
from omni.kit.property.usd.placeholder_attribute import PlaceholderAttribute
from omni.kit.property.usd.prim_path_widget import PrimPathWidget
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from omni.kit.property.usd.references_widget import PayloadReferenceWidget
from omni.kit.property.usd.relationship import RelationshipTargetPicker
from omni.kit.property.usd.relationship import SelectionWatch
from omni.kit.property.usd.usd_attribute_model import FloatModel
from omni.kit.property.usd.usd_attribute_model import GfMatrixAttributeModel
from omni.kit.property.usd.usd_attribute_model import GfQuatAttributeModel
from omni.kit.property.usd.usd_attribute_model import GfQuatEulerAttributeModel
from omni.kit.property.usd.usd_attribute_model import GfVecAttributeModel
from omni.kit.property.usd.usd_attribute_model import GfVecAttributeSingleChannelModel
from omni.kit.property.usd.usd_attribute_model import IntModel
from omni.kit.property.usd.usd_attribute_model import MdlEnumAttributeModel
from omni.kit.property.usd.usd_attribute_model import SdfAssetPathArrayAttributeItemModel
from omni.kit.property.usd.usd_attribute_model import SdfAssetPathArrayAttributeSingleEntryModel
from omni.kit.property.usd.usd_attribute_model import SdfAssetPathAttributeModel
from omni.kit.property.usd.usd_attribute_model import SdfTimeCodeModel
from omni.kit.property.usd.usd_attribute_model import TfTokenAttributeModel
from omni.kit.property.usd.usd_attribute_model import UsdAttributeInvertedModel
from omni.kit.property.usd.usd_attribute_model import UsdAttributeModel
from omni.kit.property.usd.usd_model_base import UsdBase
from omni.kit.property.usd.usd_model_items import AllowedTokenItem
from omni.kit.property.usd.usd_model_items import InvalidTokenItem
from omni.kit.property.usd.usd_model_items import OptionItem
from omni.kit.property.usd.usd_model_items import SdfAssetPathItem
from omni.kit.property.usd.usd_model_items import UsdFloatItem
from omni.kit.property.usd.usd_model_items import UsdMatrixItem
from omni.kit.property.usd.usd_model_items import UsdQuatItem
from omni.kit.property.usd.usd_model_items import UsdVectorItem
from omni.kit.property.usd.usd_object_model import MetadataObjectModel
from omni.kit.property.usd.usd_property_widget import SchemaPropertiesWidget
from omni.kit.property.usd.usd_property_widget import UsdPropertiesWidget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from omni.kit.property.usd.usd_property_widget_builder import UsdPropertiesWidgetBuilder
from omni.kit.property.usd.widgets import Examples
from omni.kit.property.usd.widgets import SelectionNotifier
from omni.kit.property.usd.widgets import UsdPropertyWidgets
import typing
from . import add_attribute_popup
from . import asset_filepicker
from . import attribute_context_menu
from . import context_menu
from . import control_state_manager
from . import custom_layout_helper
from . import message_bus_events
from . import placeholder_attribute
from . import prim_path_widget
from . import prim_selection_payload
from . import property_preferences_page
from . import references_widget
from . import relationship
from . import usd_attribute_model
from . import usd_model_base
from . import usd_model_items
from . import usd_object_model
from . import usd_property_widget
from . import usd_property_widget_builder
from . import usd_style
from . import variants_model
from . import variants_widget
from . import versioning_helper
from . import widgets
__all__: list = ['AllowedTokenItem', 'ControlStateManager', 'FloatModel', 'GfMatrixAttributeModel', 'GfQuatAttributeModel', 'GfQuatEulerAttributeModel', 'GfVecAttributeModel', 'GfVecAttributeSingleChannelModel', 'IntModel', 'MdlEnumAttributeModel', 'OptionItem', 'PlaceholderAttribute', 'PrimPathWidget', 'PrimSelectionPayload', 'SdfAssetPathArrayAttributeItemModel', 'SdfAssetPathArrayAttributeSingleEntryModel', 'SdfAssetPathAttributeModel', 'SdfAssetPathItem', 'SdfTimeCodeModel', 'SelectionNotifier', 'TfTokenAttributeModel', 'UsdAttributeInvertedModel', 'UsdAttributeModel', 'UsdBase', 'UsdFloatItem', 'UsdMatrixItem', 'UsdPropertyWidgets', 'UsdQuatItem', 'UsdVectorItem', 'UsdPropertiesWidget', 'UsdPropertiesWidgetBuilder', 'UsdPropertyUiEntry', 'SchemaPropertiesWidget', 'get_large_selection_count', 'RelationshipTargetPicker', 'SelectionWatch', 'MetadataObjectModel', 'PayloadReferenceWidget', 'CustomLayoutFrame', 'CustomLayoutGroup', 'CustomLayoutProperty', 'RegisteredSchemaCodes', 'register_schema', 'get_registered_schemas', 'is_registered_schema', 'ADDITIONAL_CHANGED_PATH_EVENT_TYPE', 'ADDITIONAL_CHANGED_PATH_GLOBAL_EVENT']
class RegisteredSchemaCodes(enum.IntEnum):
    """
    returned by is_registered_schema
    """
    FOUND: typing.ClassVar[RegisteredSchemaCodes]  # value = <RegisteredSchemaCodes.FOUND: 2>
    NOT_FOUND: typing.ClassVar[RegisteredSchemaCodes]  # value = <RegisteredSchemaCodes.NOT_FOUND: 1>
    NO_CREATE: typing.ClassVar[RegisteredSchemaCodes]  # value = <RegisteredSchemaCodes.NO_CREATE: 16>
    NO_REMOVE: typing.ClassVar[RegisteredSchemaCodes]  # value = <RegisteredSchemaCodes.NO_REMOVE: 32>
    PRIVATE: typing.ClassVar[RegisteredSchemaCodes]  # value = <RegisteredSchemaCodes.PRIVATE: 4>
    PUBLIC: typing.ClassVar[RegisteredSchemaCodes]  # value = <RegisteredSchemaCodes.PUBLIC: 8>
    @classmethod
    def __new__(cls, value):
        ...
    def __format__(self, format_spec):
        ...
def get_large_selection_count():
    """
    Fetches the count of large selections from the settings.
    
        Returns:
            int: The number of large selections as per the settings.
    """
def get_registered_schemas():
    """
    Get dictionary of all registered schema.
    """
def is_registered_schema(widget_names: list[str], schema_name: str) -> tuple[str, omni.kit.property.usd.RegisteredSchemaCodes]:
    """
    
        Check is schema is registered for widget.
    
        Args:
            widget_names (list[str]): List of name of widget that owns this schema.
            schema_name (str): Name of schema to get ownership flags.
    
        Returns:
            (str, RegisteredSchemaCodes): Name of owner and ownership flags. See RegisteredSchemaCodes for more info.
        
    """
def register_schema(widget_name: str, schemas: list, options: RegisteredSchemaCodes = ...):
    """
    
        Register schemas to widget, to add ownership.
    
        Args:
            widget_name (str): Name of widget that owns this schema.
            schemas (list): List of schemas.
            options (RegisteredSchemaCodes): Ownership flags of schemas.
        
    """
ADDITIONAL_CHANGED_PATH_EVENT_TYPE: int = 17954634024720962805
ADDITIONAL_CHANGED_PATH_GLOBAL_EVENT: str = 'omni.usd.property.usd.additional_changed_path'
property_widget_schemas: dict  # value = {'LightSchemaAttributesWidget': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}, 'CylinderLight': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}, 'DiskLight': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}, 'DistantLight': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}, 'DomeLight': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}, 'GeometryLight': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}, 'RectLight': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}, 'SphereLight': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}, 'ShapingAPI': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}, 'ShadowAPI': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}, 'LightFilter': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}, 'PortalLight': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}, 'ListAPI': {'LightAPI': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:lightLink': <RegisteredSchemaCodes.NO_REMOVE: 32>, 'CollectionAPI:shadowLink': <RegisteredSchemaCodes.NO_REMOVE: 32>}}
