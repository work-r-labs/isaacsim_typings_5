from __future__ import annotations
from isaacsim.core.utils.prims import set_targets
import omni as omni
from omni.replicator import core as rep
__all__ = ['omni', 'register_annotator_from_node_with_telemetry', 'register_node_writer_with_telemetry', 'rep', 'set_target_prims', 'set_targets']
def register_annotator_from_node_with_telemetry(*args, **kwargs):
    ...
def register_node_writer_with_telemetry(*args, **kwargs):
    ...
def set_target_prims(primPath: str, targetPrimPaths: list, inputName: str = 'inputs:targetPrim'):
    ...
