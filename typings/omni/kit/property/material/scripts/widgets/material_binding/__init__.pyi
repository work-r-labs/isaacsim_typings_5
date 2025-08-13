"""
This module provides the MaterialBindingWidget for material property binding in the UI.
"""
from __future__ import annotations
from omni.kit.property.material.scripts.widgets.material_binding.material_binding_widget import MaterialBindingWidget
from omni.kit.property.material.scripts.widgets.material_binding.material_utils import Constant
from omni.kit.property.material.scripts.widgets.material_binding.material_utils import get_binding_from_prims
from . import context_menu
from . import material_binding_widget
from . import material_utils
__all__: list[str] = ['Constant', 'MaterialBindingWidget', 'context_menu', 'get_binding_from_prims', 'material_binding_widget', 'material_utils']
