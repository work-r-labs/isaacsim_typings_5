from __future__ import annotations
import carb as carb
from isaacsim.core.nodes.bindings._isaacsim_core_nodes import acquire_interface
from isaacsim.core.nodes.bindings._isaacsim_core_nodes import release_interface
from isaacsim.core.nodes.scripts.utils import register_annotator_from_node_with_telemetry
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.stage import get_current_stage
import numpy as np
import omni as omni
from omni.replicator.core.scripts.annotators import AnnotatorRegistry
from omni.syntheticdata import _syntheticdata as sd
from omni.syntheticdata.scripts import sensors
from pxr import Sdf
from pxr import Usd
__all__ = ['AnnotatorRegistry', 'Extension', 'Sdf', 'Usd', 'acquire_interface', 'carb', 'get_current_stage', 'get_prim_at_path', 'np', 'omni', 'register_annotator_from_node_with_telemetry', 'release_interface', 'sd', 'sensors']
class Extension(omni.ext._extensions.IExt):
    def _on_stage_open_event(self, event):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
    def register_nodes(self):
        ...
    def unregister_nodes(self):
        ...
