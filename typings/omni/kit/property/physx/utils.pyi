from __future__ import annotations
import asyncio as asyncio
from collections import namedtuple
from functools import partial
import math as math
import omni as omni
from omni.kit.property.physx.externals import Prompt
from omni.kit.window import property as property_window
from omni.physxui.scripts import utils
from pxr import Gf
from pxr import PhysxSchema
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdPhysics
import re as re
import typing
__all__ = ['Gf', 'Limits', 'OverlayButton', 'PhysxSchema', 'Prompt', 'Sdf', 'StringPrompt', 'Usd', 'UsdGeom', 'UsdPhysics', 'add_disabled_styles', 'asyncio', 'disabled_styles', 'enable_widget', 'generate_schema_primary_aliases', 'get_align_property_util', 'get_display_name', 'get_title_from_schema', 'get_widget_name', 'is_parent_api_instance', 'math', 'namedtuple', 'omni', 'partial', 'property_window', 're', 'rebuild_property_window', 'scroll_property_window_to_physx_component', 'split_at_capitals', 'utils']
class Limits:
    DEG_MAX: typing.ClassVar[int] = 360
    FLT_INF: typing.ClassVar[float]  # value = inf
    FLT_MAX: typing.ClassVar[float] = 3.402823e+38
    FLT_MIN: typing.ClassVar[float] = 1.17549435e-38
    FLT_NINF: typing.ClassVar[float]  # value = -inf
    FLT_NMAX: typing.ClassVar[float] = -3.402823e+38
    INFS: typing.ClassVar[list]  # value = [inf, -inf, 3.402823e+38, -3.402823e+38, 1.17549435e-38]
    INT_MAX: typing.ClassVar[int] = 2147483647
    RAD_MAX: typing.ClassVar[float] = 6.283185307179586
    RANGE_DEG: typing.ClassVar[list] = [-360, 360]
    RANGE_FLT_NONNEG: typing.ClassVar[list] = [0, 3.402823e+38]
    RANGE_FLT_POS: typing.ClassVar[list] = [1.17549435e-38, 3.402823e+38]
    RANGE_RAD: typing.ClassVar[list] = [-6.283185307179586, 6.283185307179586]
class OverlayButton(omni.ui._ui.Button):
    def __init__(self, text, collapsable_frame, pressed_fn, **kwargs):
        ...
class StringPrompt(omni.kit.property.physx.externals.Prompt):
    def _build_ui(self):
        ...
    def _on_ok_button_fn(self):
        ...
    def set_warning(self, warning):
        ...
def add_disabled_styles(widget):
    ...
def enable_widget(widget, enable):
    ...
def generate_schema_primary_aliases():
    ...
def get_align_property_util(text, body0base, widget, fixpos, fixrot):
    ...
def get_display_name(metadata, default):
    ...
def get_title_from_schema(schema):
    ...
def get_widget_name(schema):
    ...
def is_parent_api_instance(api_name, instance_name, payload):
    """
    
        if we cannot find the api:instance name in the applied api schemas list
        it means this one is here because of a child API that has its own widget
        and the properties are also shown there, so we skip this one
        
    """
def rebuild_property_window():
    ...
def scroll_property_window_to_physx_component(component_name: str, num_update_delay_cycles: int = 5):
    ...
def split_at_capitals(title):
    ...
disabled_styles: dict  # value = {'ComboBox:disabled': {'color': 'grey'}, 'CheckBox::greenCheck:disabled': {'font_size': 12, 'border_radius': 1.5}, 'Slider:disabled': {'color': 'grey'}, 'Label:disabled': {'color': 'grey'}}
