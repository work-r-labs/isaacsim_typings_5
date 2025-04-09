import OmniScriptingSchema as OmniScriptingSchema
from __future__ import annotations
import omni as omni
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from omni.kit.property.usd.usd_property_widget import UsdPropertiesWidget
from omni.kit.scripting.scripts.utils import Prompt
from omni.kit.scripting.scripts.utils import open_script_file
from omni import ui
import pathlib
from pathlib import Path
from pxr import Sdf
from pxr import Usd
__all__ = ['ICON_PATH', 'OmniScriptingSchema', 'Path', 'PrimSelectionPayload', 'Prompt', 'REMOVE_BUTTON_STYLE', 'SCRIPTS_ATTR', 'SCRIPTS_DISPLAY_NAME', 'ScriptingAPIPropertiesWidget', 'ScriptingProperties', 'Sdf', 'Usd', 'UsdPropertiesWidget', 'omni', 'open_script_file', 'style', 'ui']
class ScriptingAPIPropertiesWidget(omni.kit.property.usd.usd_property_widget.UsdPropertiesWidget):
    def __init__(self, title: str):
        ...
    def _build_custom_frame_header(self, collapsed, text):
        ...
    def _customize_props_layout(self, attrs):
        ...
    def _filter_props_to_build(self, props):
        ...
    def _on_remove_with_prompt(self):
        ...
    def build_impl(self):
        ...
    def destroy(self):
        ...
    def get_additional_kwargs(self, ui_attr):
        ...
    def on_click_scripting(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload):
        ...
    def on_new_payload(self, payload):
        ...
    def on_show_scripting(self, objects: dict):
        ...
class ScriptingProperties:
    def __init__(self):
        ...
    def destroy(self):
        ...
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons')
REMOVE_BUTTON_STYLE: dict = {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/remove.svg', 'margin': 0, 'padding': 0}
SCRIPTS_ATTR: str = 'omni:scripting:scripts'
SCRIPTS_DISPLAY_NAME: str = 'Scripts'
style: dict = {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/remove.svg', 'margin': 0, 'padding': 0}
