from __future__ import annotations
import carb as carb
import gc as gc
from isaacsim.core.nodes.scripts.utils import register_annotator_from_node_with_telemetry
from isaacsim.core.nodes.scripts.utils import register_node_writer_with_telemetry
from isaacsim.core.utils.stage import traverse_stage
from isaacsim.sensors.rtx.bindings._isaacsim_sensors_rtx import acquire_interface as _acquire
from isaacsim.sensors.rtx.bindings._isaacsim_sensors_rtx import release_interface as _release
import numpy as np
import omni as omni
from omni.replicator import core as rep
from omni.replicator.core.scripts.annotators import AnnotatorRegistry
from omni.syntheticdata.scripts import sensors
__all__ = ['AnnotatorRegistry', 'EXTENSION_NAME', 'Extension', 'carb', 'gc', 'np', 'omni', 'register_annotator_from_node_with_telemetry', 'register_node_writer_with_telemetry', 'rep', 'sensors', 'traverse_stage']
class Extension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id: str):
        ...
    def register_nodes(self):
        ...
    def unregister_nodes(self):
        ...
EXTENSION_NAME: str = 'Isaac Sensor'
