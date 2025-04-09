from __future__ import annotations
import carb as carb
import enum
from enum import Enum
import pxr.Sdf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
import typing
__all__ = ['Enum', 'Sdf', 'Usd', 'Value_On_Layer', 'attr_has_timesample_on_key', 'carb', 'copy_timesamples_from_weaker_layer', 'get_attribute_effective_defaultvalue_layer_info', 'get_attribute_effective_timesample_layer_info', 'get_attribute_effective_value_layer_info', 'get_frame_time', 'get_frame_time_code', 'get_timesamples_count_in_authoring_layer']
class Value_On_Layer(enum.Enum):
    """
    Enum for the strength type of an attribute value.
    """
    No_Value: typing.ClassVar[Value_On_Layer]  # value = <Value_On_Layer.No_Value: 0>
    ON_STRONGER_LAYER: typing.ClassVar[Value_On_Layer]  # value = <Value_On_Layer.ON_STRONGER_LAYER: 1>
    ON_WEAKER_LAYER: typing.ClassVar[Value_On_Layer]  # value = <Value_On_Layer.ON_WEAKER_LAYER: 2>
def attr_has_timesample_on_key(attr: pxr.Usd.Attribute, time_code: pxr.Usd.TimeCode):
    """
    Internal. If attribute has authored value to the specific time code.
    """
def copy_timesamples_from_weaker_layer(stage, attr: pxr.Usd.Attribute):
    """
    Internal. Copy timesamples of the attribute from weak layer to the current edit target.
    """
def get_attribute_effective_defaultvalue_layer_info(stage, attr: pxr.Usd.Attribute):
    """
    Internal. Gets the strength type and layer for the default value of the attribute.
    """
def get_attribute_effective_timesample_layer_info(stage, attr: pxr.Usd.Attribute):
    """
    Internal. Gets the strength type and layer for the timesamples of the attribute.
    """
def get_attribute_effective_value_layer_info(stage, attr: pxr.Usd.Attribute):
    """
    Internal. Gets the strength type and layer for the default value or timesamples of the attribute.
    """
def get_frame_time(time_code, fps):
    """
    Internal. Utility to convert time code into frame time.
    """
def get_frame_time_code(time, fps):
    """
    Internal. Utility to convert fps into time code.
    """
def get_timesamples_count_in_authoring_layer(stage, attr_path: pxr.Sdf.Path):
    """
    Internal. Gets the count of timesamples of the attribute in the current edit target.
    """
