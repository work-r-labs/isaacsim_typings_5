"""
Support for simplified access to data on nodes of type isaacsim.robot.wheeled_robots.AckermannSteering

 __   ___ .  .  ___  __       ___  ___  __      __   __   __   ___
/ _` |__  |\\ | |__  |__)  /\\   |  |__  |  \\    /  ` /  \\ |  \\ |__
\\__| |___ | \\| |___ |  \\ /--\\  |  |___ |__/    \\__, \\__/ |__/ |___

 __   __     .  .  __  ___     .  .  __   __     ___
|  \\ /  \\    |\\ | /  \\  |      |\\/| /  \\ |  \\ | |__  \\ /
|__/ \\__/    | \\| \\__/  |      |  | \\__/ |__/ | |     |

NOTE: DEPRECATED as of Isaac Sim 4.1.0 in favour of OgnAckermannController Ackermann Steering Geometry
"""
from __future__ import annotations
import isaacsim.robot.wheeled_robots.ogn.python.nodes.OgnAckermann
import numpy as numpy
from omni.graph import core as og
import omni.graph.core._impl.database
from omni.graph.core import _omni_graph_core as _og
import omni.graph.core._omni_graph_core
from omni.graph.tools import ogn
import sys as sys
import traceback as traceback
import typing
__all__: list[str] = ['OgnAckermannDatabase', 'numpy', 'og', 'ogn', 'sys', 'traceback']
class OgnAckermannDatabase(omni.graph.core._impl.database.Database):
    """
    Helper class providing simplified access to data on nodes of type isaacsim.robot.wheeled_robots.AckermannSteering
    
        Class Members:
            node: Node being evaluated
    
        Attribute Value Properties:
            Inputs:
                inputs.DT
                inputs.acceleration
                inputs.currentLinearVelocity
                inputs.execIn
                inputs.invertSteeringAngle
                inputs.maxWheelRotation
                inputs.maxWheelVelocity
                inputs.speed
                inputs.steeringAngle
                inputs.trackWidth
                inputs.turningWheelRadius
                inputs.useAcceleration
                inputs.wheelBase
            Outputs:
                outputs.execOut
                outputs.leftWheelAngle
                outputs.rightWheelAngle
                outputs.wheelRotationVelocity
        
    """
    class ValuesForInputs(omni.graph.core._impl.database.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES: typing.ClassVar[set] = {'DT', 'execIn', 'turningWheelRadius', '_setting_locked', 'acceleration', 'trackWidth', 'currentLinearVelocity', 'maxWheelRotation', '_batchedReadValues', 'wheelBase', 'maxWheelVelocity', 'speed', 'steeringAngle', 'useAcceleration', '_batchedReadAttributes', 'invertSteeringAngle'}
        DT = ...
        acceleration = ...
        currentLinearVelocity = ...
        execIn = ...
        invertSteeringAngle = ...
        maxWheelRotation = ...
        maxWheelVelocity = ...
        speed = ...
        steeringAngle = ...
        trackWidth = ...
        turningWheelRadius = ...
        useAcceleration = ...
        wheelBase = ...
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
        LOCAL_PROPERTY_NAMES: typing.ClassVar[set] = {'_batchedWriteValues', 'execOut', 'rightWheelAngle', 'wheelRotationVelocity', 'leftWheelAngle'}
        execOut = ...
        leftWheelAngle = ...
        rightWheelAngle = ...
        wheelRotationVelocity = ...
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
    GENERATOR_VERSION: typing.ClassVar[tuple] = (1, 79, 2)
    INTERFACE: typing.ClassVar[omni.graph.core._impl.database._AllAttributeDefinitions]  # value = <omni.graph.core._impl.database._AllAttributeDefinitions object>
    PER_NODE_DATA: typing.ClassVar[dict] = {}
    TARGET_VERSION: typing.ClassVar[tuple] = (2, 184, 3)
    NODE_TYPE_CLASS = isaacsim.robot.wheeled_robots.ogn.python.nodes.OgnAckermann.OgnAckermann
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
