"""
Support for simplified access to data on nodes of type isaacsim.robot.wheeled_robots.HolonomicRobotUsdSetup

 __   ___ .  .  ___  __       ___  ___  __      __   __   __   ___
/ _` |__  |\\ | |__  |__)  /\\   |  |__  |  \\    /  ` /  \\ |  \\ |__
\\__| |___ | \\| |___ |  \\ /--\\  |  |___ |__/    \\__, \\__/ |__/ |___

 __   __     .  .  __  ___     .  .  __   __     ___
|  \\ /  \\    |\\ | /  \\  |      |\\/| /  \\ |  \\ | |__  \\ /
|__/ \\__/    | \\| \\__/  |      |  | \\__/ |__/ | |     |

setup any robot to be ready to be used by the holonomic controller by extract attributes from USD
"""
from __future__ import annotations
import isaacsim.robot.wheeled_robots.ogn.python.nodes.OgnHolonomicRobotUsdSetup
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
__all__ = ['OgnHolonomicRobotUsdSetupDatabase', 'numpy', 'og', 'ogn', 'sys', 'traceback', 'usdrt']
class OgnHolonomicRobotUsdSetupDatabase(omni.graph.core._impl.database.Database):
    """
    Helper class providing simplified access to data on nodes of type isaacsim.robot.wheeled_robots.HolonomicRobotUsdSetup
    
        Class Members:
            node: Node being evaluated
    
        Attribute Value Properties:
            Inputs:
                inputs.comPrim
                inputs.comPrimPath
                inputs.robotPrim
                inputs.robotPrimPath
                inputs.usePath
            Outputs:
                outputs.mecanumAngles
                outputs.upAxis
                outputs.wheelAxis
                outputs.wheelDofNames
                outputs.wheelOrientations
                outputs.wheelPositions
                outputs.wheelRadius
        
    """
    class ValuesForInputs(omni.graph.core._impl.database.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES: typing.ClassVar[set] = {'_setting_locked', 'usePath', 'comPrimPath', '_batchedReadValues', 'robotPrimPath', '_batchedReadAttributes'}
        comPrim = ...
        comPrimPath = ...
        robotPrim = ...
        robotPrimPath = ...
        usePath = ...
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
        LOCAL_PROPERTY_NAMES: typing.ClassVar[set] = {'wheelAxis', '_batchedWriteValues', 'upAxis'}
        mecanumAngles = ...
        upAxis = ...
        wheelAxis = ...
        wheelDofNames = ...
        wheelOrientations = ...
        wheelPositions = ...
        wheelRadius = ...
        def __getattr__(self, item: str):
            ...
        def __init__(self, node: omni.graph.core._omni_graph_core.Node, attributes, dynamic_attributes: omni.graph.core._impl.database.DynamicAttributeInterface):
            """
            Initialize simplified access for the attribute data
            """
        def __setattr__(self, item: str, new_value):
            ...
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
    NODE_TYPE_CLASS = isaacsim.robot.wheeled_robots.ogn.python.nodes.OgnHolonomicRobotUsdSetup.OgnHolonomicRobotUsdSetup
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
