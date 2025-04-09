"""
This module provides widgets for manipulating USD material properties, including backdrop, material binding, and various USD shade components.
"""
from __future__ import annotations
from omni.kit.property.material.scripts.widgets.backdrop_widget import UsdUIBackdropWidget
from omni.kit.property.material.scripts.widgets.material_binding.material_binding_widget import MaterialBindingWidget
from omni.kit.property.material.scripts.widgets.usdshade.attribute_widget import UsdShadeAttributeWidget
from omni.kit.property.material.scripts.widgets.usdshade.material_widget import UsdShadeMaterialWidget
from omni.kit.property.material.scripts.widgets.usdshade.nodegraph_widget import UsdShadeNodeGraphWidget
from omni.kit.property.material.scripts.widgets.usdshade.shader_widget import UsdShadeShaderWidget
from omni.kit.property.material.scripts.widgets.usdshade.utils import remove_properties_and_connections
from . import backdrop_widget
from . import material_binding
from . import usdshade
__all__ = ['MaterialBindingWidget', 'UsdShadeAttributeWidget', 'UsdShadeMaterialWidget', 'UsdShadeNodeGraphWidget', 'UsdShadeShaderWidget', 'UsdUIBackdropWidget', 'backdrop_widget', 'material_binding', 'remove_properties_and_connections', 'usdshade']
