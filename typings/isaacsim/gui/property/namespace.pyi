from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from omni.kit.property.usd.usd_attribute_model import UsdAttributeModel
from omni.kit.property.usd.usd_property_widget import UsdPropertiesWidget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from omni.kit.property.usd.usd_property_widget_builder import UsdPropertiesWidgetBuilder
from omni.kit.window.property.templates.simple_property_widget import SimplePropertyWidget
from omni.kit.window.property.templates.simple_property_widget import build_frame_header
from omni import ui
import pathlib
from pxr import Gf
from pxr import Sdf
from pxr import Tf
from pxr import Usd
from usd.schema.isaac import robot_schema
__all__: list[str] = ['Gf', 'HORIZONTAL_SPACING', 'ICON_PATH', 'LABEL_HEIGHT', 'LABEL_WIDTH', 'PrimSelectionPayload', 'Sdf', 'SimplePropertyWidget', 'Singleton', 'Tf', 'Usd', 'UsdAttributeModel', 'UsdPropertiesWidget', 'UsdPropertiesWidgetBuilder', 'UsdPropertyUiEntry', 'asyncio', 'build_frame_header', 'carb', 'omni', 'robot_schema', 'ui']
def Singleton(class_):
    """
    A singleton decorator
    """
HORIZONTAL_SPACING: int = 4
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.property.usd-4.5.11+8131b85d/data/icons')
LABEL_HEIGHT: int = 18
LABEL_WIDTH: int = 160
