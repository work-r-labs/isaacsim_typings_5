from __future__ import annotations
import carb as carb
import ctypes as ctypes
import gc as gc
from isaacsim.core.nodes.scripts.utils import register_annotator_from_node_with_telemetry
from isaacsim.core.nodes.scripts.utils import register_node_writer_with_telemetry
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.sensors.rtx.bindings._isaacsim_sensors_rtx import acquire_interface as _acquire
from isaacsim.sensors.rtx.bindings._isaacsim_sensors_rtx import release_interface as _release
from isaacsim.sensors.rtx import generic_model_output as gmo_utils
import isaacsim.sensors.rtx.generic_model_output._generic_model_output
import numpy as np
import omni as omni
from omni.graph import core as og
from omni.replicator import core as rep
from omni.replicator.core.scripts.annotators import AnnotatorRegistry
from omni.syntheticdata.scripts import sensors
__all__: list[str] = ['AnnotatorRegistry', 'EXTENSION_NAME', 'Extension', 'carb', 'ctypes', 'gc', 'get_gmo_data', 'get_prim_at_path', 'gmo_utils', 'np', 'og', 'omni', 'register_annotator_from_node_with_telemetry', 'register_node_writer_with_telemetry', 'rep', 'sensors']
class Extension(omni.ext._extensions.IExt):
    def _on_attach_callback_base(self, annotator_name: str, connections: typing.List[typing.Tuple[str, str, str, str]], node: omni.graph.core._omni_graph_core.Node):
        """
        
                Callback function for annotator attachment. Will connect ancestral upstream node(s) to each other and annotator node, if user
                desires connections beyond immediate parent nodes.
        
                Args:
                    annotator_name (str): Name of annotator being attached.
                    connections (List[Tuple[str, str, str, str]]): List of connections to create between nodes, specified as (source_node, source_attr, target_node, target_attr). source_node and target_node are node types; if desired target is annotator node, provide node prim path.
                    node (og.Node): Annotator node being attached.
                
        """
    def _update_upstream_node_attributes(self, upstream_node_type_name: str, attribute: str, value, node: omni.graph.core._omni_graph_core.Node):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id: str):
        ...
    def register_nodes(self):
        ...
    def unregister_nodes(self):
        ...
def get_gmo_data(dataPtr: typing.Union[int, numpy.ndarray]) -> isaacsim.sensors.rtx.generic_model_output._generic_model_output.GenericModelOutput:
    """
    Retrieves GMO buffer from pointer to GMO buffer.
    
        Args:
            dataPtr (int): Expected uint64 pointer to GMO buffer.
    
        Returns:
            gmo_utils.GenericModelOutput: GMO buffer at dataPtr. Empty struct if dataPtr is 0 or None.
        
    """
EXTENSION_NAME: str = 'Isaac Sensor'
