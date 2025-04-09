"""
This module provides USD property widgets and related utilities for use in the Omniverse Kit.
"""
from __future__ import annotations
from omni.kit.property.usd.control_state_manager import ControlStateManager
from omni.kit.property.usd.placeholder_attribute import PlaceholderAttribute
from omni.kit.property.usd.prim_path_widget import PrimPathWidget
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
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
from omni.kit.property.usd.usd_model_items import OptionItem
from omni.kit.property.usd.usd_model_items import SdfAssetPathItem
from omni.kit.property.usd.usd_model_items import UsdFloatItem
from omni.kit.property.usd.usd_model_items import UsdMatrixItem
from omni.kit.property.usd.usd_model_items import UsdQuatItem
from omni.kit.property.usd.usd_model_items import UsdVectorItem
from omni.kit.property.usd.widgets import Examples
from omni.kit.property.usd.widgets import UsdPropertyWidgets
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
__all__: list = ['AllowedTokenItem', 'ControlStateManager', 'FloatModel', 'GfMatrixAttributeModel', 'GfQuatAttributeModel', 'GfQuatEulerAttributeModel', 'GfVecAttributeModel', 'GfVecAttributeSingleChannelModel', 'IntModel', 'MdlEnumAttributeModel', 'OptionItem', 'PlaceholderAttribute', 'PrimPathWidget', 'PrimSelectionPayload', 'SdfAssetPathArrayAttributeItemModel', 'SdfAssetPathArrayAttributeSingleEntryModel', 'SdfAssetPathAttributeModel', 'SdfAssetPathItem', 'SdfTimeCodeModel', 'SelectionNotifier', 'TfTokenAttributeModel', 'UsdAttributeInvertedModel', 'UsdAttributeModel', 'UsdBase', 'UsdFloatItem', 'UsdMatrixItem', 'UsdPropertyWidgets', 'UsdQuatItem', 'UsdVectorItem', 'get_large_selection_count']
def get_large_selection_count():
    """
    Fetches the count of large selections from the settings.
    
        Returns:
            int: The number of large selections as per the settings.
    """
ADDITIONAL_CHANGED_PATH_EVENT_TYPE: int = 17954634024720962805
