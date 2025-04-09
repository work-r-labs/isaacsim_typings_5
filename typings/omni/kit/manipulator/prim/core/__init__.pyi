"""
This module provides classes and functions for managing and manipulating USD primitive objects in Omniverse applications.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import concurrent as concurrent
from enum import Enum
from enum import Flag
from enum import IntEnum
from enum import auto
import math as math
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.manipulator.prim.core.extension import ManipulatorPrim2Core
from omni.kit.manipulator.prim.core.global_registry import clean_prim_data_accessor_registry
from omni.kit.manipulator.prim.core.global_registry import get_prim_data_accessor_registry
from omni.kit.manipulator.prim.core.global_registry import set_prim_data_accessor_registry
from omni.kit.manipulator.prim.core.model import OpFlag
from omni.kit.manipulator.prim.core.model import Placement
from omni.kit.manipulator.prim.core.model import PrimRotateChangedGesture
from omni.kit.manipulator.prim.core.model import PrimScaleChangedGesture
from omni.kit.manipulator.prim.core.model import PrimTransformModel
from omni.kit.manipulator.prim.core.model import PrimTranslateChangedGesture
from omni.kit.manipulator.prim.core.prim_data_accessor_registry import PrimDataAccessorRegistry
from omni.kit.manipulator.prim.core.prim_data_accessor_selector import PrimDataAccessorSelector
from omni.kit.manipulator.prim.core.prim_transform_manipulator import PrimTransformManipulator
from omni.kit.manipulator.prim.core.prim_transform_manipulator_registry import TransformManipulatorRegistry
from omni.kit.manipulator.prim.core.reference_prim_marker import ReferencePrimMarker
from omni.kit.manipulator.prim.core.settings_constants import Constants
from omni.kit.manipulator.prim.core.settings_constants import Constants as prim_c
from omni.kit.manipulator.prim.core.settings_constants import DataAccessorConstants
from omni.kit.manipulator.prim.core.toolbar_registry import get_toolbar_registry
from omni.kit.manipulator.prim.core.tools import PrimManipTools
from omni.kit.manipulator.prim.core.utils import compose_transform_ops_to_matrix
from omni.kit.manipulator.prim.core.utils import construct_transform_matrix_from_SRT
from omni.kit.manipulator.prim.core.utils import find_best_euler_angles
from omni.kit.manipulator.prim.core.utils import flatten
from omni.kit.manipulator.prim.core.utils import generate_compatible_euler_angles
from omni.kit.manipulator.prim.core.utils import repeat
from omni.kit.manipulator.tool.snap.manager import SnapProviderManager
from omni.kit.manipulator.tool.snap import settings_constants as snap_c
from omni.kit.manipulator.transform.model import AbstractTransformManipulatorModel
from omni.kit.manipulator.transform.settings_constants import Constants as transform_c
from omni.kit.manipulator.transform.settings_listener import OpSettingsListener
from omni.kit.manipulator.transform.settings_listener import SnapSettingsListener
from omni.kit.manipulator.transform.toolbar_registry import ToolbarRegistry
from omni.kit.manipulator.transform.types import Operation
from omni.kit.viewport.manipulator.transform.gestures import ViewportRotateChangedGesture
from omni.kit.viewport.manipulator.transform.gestures import ViewportScaleChangedGesture
from omni.kit.viewport.manipulator.transform.gestures import ViewportTranslateChangedGesture
from omni.kit.viewport.manipulator.transform.model import ManipulationMode
from omni.kit.viewport.manipulator.transform.model import ViewportTransformModel
from omni.ui import scene as sc
import pxr as pxr
from pxr import Gf
from pxr import Usd
from pxr import UsdGeom
import traceback as traceback
import usdrt as usdrt
from . import extension
from . import global_registry
from . import model
from . import prim_data_accessor_registry
from . import prim_data_accessor_selector
from . import prim_transform_manipulator
from . import prim_transform_manipulator_registry
from . import reference_prim_marker
from . import settings_constants
from . import tool_models
from . import toolbar_registry
from . import tools
from . import utils
__all__: list = ['get_prim_data_accessor_registry', 'PrimDataAccessorRegistry', 'TransformManipulatorRegistry', 'PrimTransformManipulator', 'PrimTransformModel', 'get_toolbar_registry', 'DataAccessorConstants', 'Constants']
PRINT_PERF_DATA: bool = True
TRANSFORM_GIZMO_CUSTOM_MANIPULATOR_ENABLED: str = '/app/transform/gizmoCustomManipulatorEnabled'
TRANSFORM_GIZMO_CUSTOM_MANIPULATOR_PRIMS: str = '/app/transform/gizmoCustomManipulatorPrims'
TRANSFORM_GIZMO_IS_USING: str = '/app/transform/gizmoIsUsing'
TRANSFORM_GIZMO_PIVOT_WORLD_POSITION: str = '/app/transform/tempPivotWorldPosition'
TRANSFORM_GIZMO_ROTATE_DELTA_XYZW: str = '/app/transform/gizmoRotateDeltaXYZW'
TRANSFORM_GIZMO_SCALE_DELTA_XYZ: str = '/app/transform/gizmoScaleDeltaXYZ'
TRANSFORM_GIZMO_TRANSLATE_DELTA_XYZ: str = '/app/transform/gizmoTranslateDeltaXYZ'
TRANSLATE_DELAY_FRAME_SETTING: str = '/exts/omni.kit.manipulator.prim.core/visual/delayFrame'
