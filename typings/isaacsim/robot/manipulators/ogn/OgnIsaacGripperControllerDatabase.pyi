"""
Support for simplified access to data on nodes of type isaacsim.robot.manipulators.IsaacGripperController

 __   ___ .  .  ___  __       ___  ___  __      __   __   __   ___
/ _` |__  |\\ | |__  |__)  /\\   |  |__  |  \\    /  ` /  \\ |  \\ |__
\\__| |___ | \\| |___ |  \\ /--\\  |  |___ |__/    \\__, \\__/ |__/ |___

 __   __     .  .  __  ___     .  .  __   __     ___
|  \\ /  \\    |\\ | /  \\  |      |\\/| /  \\ |  \\ | |__  \\ /
|__/ \\__/    | \\| \\__/  |      |  | \\__/ |__/ | |     |

Isaac Sim Gripper Controller Node
"""
from __future__ import annotations
import isaacsim.robot.manipulators.ogn.python.nodes.OgnIsaacGripperController
import numpy as numpy
from omni.graph import core as og
import omni.graph.core._impl.database
import omni.graph.core._omni_graph_core
from omni.graph.core import _omni_graph_core as _og
from omni.graph.tools import ogn
import sys as sys
import traceback as traceback
import typing
import usdrt as usdrt
__all__ = ['OgnIsaacGripperControllerDatabase', 'numpy', 'og', 'ogn', 'sys', 'traceback', 'usdrt']
class OgnIsaacGripperControllerDatabase(omni.graph.core._impl.database.Database):
    """
    Helper class providing simplified access to data on nodes of type isaacsim.robot.manipulators.IsaacGripperController
    
        Class Members:
            node: Node being evaluated
    
        Attribute Value Properties:
            Inputs:
                inputs.articulationRootPrim
                inputs.close
                inputs.closePosition
                inputs.execIn
                inputs.gripperPrim
                inputs.gripperSpeed
                inputs.jointNames
                inputs.open
                inputs.openPosition
                inputs.stop
            Outputs:
                outputs.jointNames
                outputs.positionCommands
        
    """
    class ValuesForInputs(omni.graph.core._impl.database.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES: typing.ClassVar[set] = {'_setting_locked', 'open', 'close', 'execIn', '_batchedReadValues', 'stop', '_batchedReadAttributes'}
        articulationRootPrim = ...
        close = ...
        closePosition = ...
        execIn = ...
        gripperPrim = ...
        gripperSpeed = ...
        jointNames = ...
        open = ...
        openPosition = ...
        stop = ...
        def __getattr__(self, item: str):
            ...
        def __init__(self, node: omni.graph.core._omni_graph_core.Node, attributes, dynamic_attributes: omni.graph.core._impl.database.DynamicAttributeInterface):
            """
            Initialize simplified access for the attribute data
            """
        def __setattr__(self, item: str, new_value):
            ...
        def _prefetch(self):
            ...
    class ValuesForOutputs(omni.graph.core._impl.database.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES: typing.ClassVar[dict] = {}
        jointNames = ...
        positionCommands = ...
        def __init__(self, node: omni.graph.core._omni_graph_core.Node, attributes, dynamic_attributes: omni.graph.core._impl.database.DynamicAttributeInterface):
            """
            Initialize simplified access for the attribute data
            """
        def _commit(self):
            ...
    class ValuesForState(omni.graph.core._impl.database.DynamicAttributeAccess):
        """
        Helper class that creates natural hierarchical access to state attributes
        """
        def __init__(self, node: omni.graph.core._omni_graph_core.Node, attributes, dynamic_attributes: omni.graph.core._impl.database.DynamicAttributeInterface):
            """
            Initialize simplified access for the attribute data
            """
    class abi:
        """
        Class defining the ABI interface for the node type
        """
        @staticmethod
        def compute(context, node):
            ...
        @staticmethod
        def get_node_type():
            ...
        @staticmethod
        def init_instance(node, graph_instance_id):
            ...
        @staticmethod
        def initialize(context, node):
            ...
        @staticmethod
        def initialize_nodes(context, nodes):
            ...
        @staticmethod
        def initialize_type(node_type):
            ...
        @staticmethod
        def on_connection_type_resolve(node):
            ...
        @staticmethod
        def release(node):
            ...
        @staticmethod
        def release_instance(node, graph_instance_id):
            ...
        @staticmethod
        def update_node_version(context, node, old_version, new_version):
            ...
    GENERATOR_VERSION: typing.ClassVar[tuple] = (1, 79, 1)
    INTERFACE: typing.ClassVar[omni.graph.core._impl.database._AllAttributeDefinitions]  # value = <omni.graph.core._impl.database._AllAttributeDefinitions object>
    PER_NODE_DATA: typing.ClassVar[dict] = {}
    TARGET_VERSION: typing.ClassVar[tuple] = (2, 181, 8)
    NODE_TYPE_CLASS = isaacsim.robot.manipulators.ogn.python.nodes.OgnIsaacGripperController.OgnIsaacGripperController
    @staticmethod
    def deregister():
        ...
    @staticmethod
    def register(node_type_class):
        ...
    @classmethod
    def _populate_role_data(cls):
        """
        Populate a role structure with the non-default roles on this node type
        """
    def __init__(self, node):
        ...
