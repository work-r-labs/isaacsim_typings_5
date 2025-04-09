"""
This module provides widgets for USD shade properties, including attribute, material, node graph, and shader widgets, along with utility functions.
"""
from __future__ import annotations
from omni.kit.property.material.scripts.widgets.usdshade.attribute_widget import UsdShadeAttributeWidget
from omni.kit.property.material.scripts.widgets.usdshade.material_widget import UsdShadeMaterialWidget
from omni.kit.property.material.scripts.widgets.usdshade.nodegraph_widget import UsdShadeNodeGraphWidget
from omni.kit.property.material.scripts.widgets.usdshade.shader_widget import UsdShadeShaderWidget
from omni.kit.property.material.scripts.widgets.usdshade.utils import get_sdr_shader_node_for_prim
from omni.kit.property.material.scripts.widgets.usdshade.utils import property_name_to_display_name
from omni.kit.property.material.scripts.widgets.usdshade.utils import remove_properties_and_connections
from . import attribute_widget
from . import base_widget
from . import material_widget
from . import models
from . import nodegraph_widget
from . import placeholder
from . import shader_widget
from . import usdshade_property_ui_entry
from . import utils
__all__ = ['UsdShadeAttributeWidget', 'UsdShadeMaterialWidget', 'UsdShadeNodeGraphWidget', 'UsdShadeShaderWidget', 'attribute_widget', 'base_widget', 'get_sdr_shader_node_for_prim', 'material_widget', 'models', 'nodegraph_widget', 'placeholder', 'property_name_to_display_name', 'remove_properties_and_connections', 'shader_widget', 'usdshade_property_ui_entry', 'utils']
