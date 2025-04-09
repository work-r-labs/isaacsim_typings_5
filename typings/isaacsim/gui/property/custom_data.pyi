from __future__ import annotations
import carb as carb
import numpy as np
from omni.kit.property.usd.usd_attribute_model import UsdAttributeModel
import omni.kit.property.usd.usd_property_widget
from omni.kit.property.usd.usd_property_widget import UsdPropertiesWidget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from omni.kit.property.usd.usd_property_widget_builder import UsdPropertiesWidgetBuilder
import omni.kit.window.property.templates.simple_property_widget
from omni.kit.window.property.templates.simple_property_widget import SimplePropertyWidget
from omni.kit.window.property.templates.simple_property_widget import build_frame_header
from omni import ui
import pathlib
from pxr import Gf
from pxr import Sdf
from pxr import Tf
from pxr import Usd
__all__ = ['CustomDataWidget', 'Gf', 'HORIZONTAL_SPACING', 'ICON_PATH', 'LABEL_HEIGHT', 'LABEL_WIDTH', 'Sdf', 'SimplePropertyWidget', 'Tf', 'Usd', 'UsdAttributeModel', 'UsdPropertiesWidget', 'UsdPropertiesWidgetBuilder', 'UsdPropertyUiEntry', 'build_frame_header', 'carb', 'iterate_custom_data', 'np', 'ui']
class CustomDataWidget(omni.kit.window.property.templates.simple_property_widget.SimplePropertyWidget):
    def _get_prim(self, prim_path):
        ...
    def build_items(self):
        ...
    def build_property_item(self, stage, ui_prop: omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry, prim_paths: typing.List[pxr.Sdf.Path]):
        ...
    def on_new_payload(self, payload):
        """
        
                See PropertyWidget.on_new_payload
                
        """
def iterate_custom_data(custom_data):
    ...
HORIZONTAL_SPACING: int = 4
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons')
LABEL_HEIGHT: int = 18
LABEL_WIDTH: int = 160
