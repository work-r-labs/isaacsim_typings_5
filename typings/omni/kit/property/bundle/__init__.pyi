"""
This module provides classes for registering and managing custom property widgets for USD prims within the Omniverse Kit application.
"""
from __future__ import annotations
import omni as omni
from omni.kit.property.bundle.geom_scheme_delegate import GeomPrimSchemeDelegate
from omni.kit.property.bundle.material_scheme_delegate import MaterialPrimSchemeDelegate
from omni.kit.property.bundle.material_scheme_delegate import ShaderPrimSchemeDelegate
from omni.kit.property.bundle.path_scheme_delegate import PathPrimSchemeDelegate
from omni.kit.property.bundle.widgets import BundlePropertyWidgets
from . import geom_scheme_delegate
from . import material_scheme_delegate
from . import path_scheme_delegate
from . import widgets
__all__: list = ['BundlePropertyWidgets', 'GeomPrimSchemeDelegate', 'MaterialPrimSchemeDelegate', 'PathPrimSchemeDelegate', 'ShaderPrimSchemeDelegate']
