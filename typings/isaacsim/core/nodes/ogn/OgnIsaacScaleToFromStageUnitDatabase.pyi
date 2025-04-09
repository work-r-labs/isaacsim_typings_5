"""
Support for simplified access to data on nodes of type isaacsim.core.nodes.OgnIsaacScaleToFromStageUnit

 __   ___ .  .  ___  __       ___  ___  __      __   __   __   ___
/ _` |__  |\\ | |__  |__)  /\\   |  |__  |  \\    /  ` /  \\ |  \\ |__
\\__| |___ | \\| |___ |  \\ /--\\  |  |___ |__/    \\__, \\__/ |__/ |___

 __   __     .  .  __  ___     .  .  __   __     ___
|  \\ /  \\    |\\ | /  \\  |      |\\/| /  \\ |  \\ | |__  \\ /
|__/ \\__/    | \\| \\__/  |      |  | \\__/ |__/ | |     |

This node converts meters to/from stage units
"""
from __future__ import annotations
import carb as carb
import isaacsim.core.nodes.ogn.python.nodes.OgnIsaacScaleToFromStageUnit
from omni.graph import core as og
import omni.graph.core._impl.database
import omni.graph.core._impl.runtime
import omni.graph.core._omni_graph_core
from omni.graph.core import _omni_graph_core as _og
from omni.graph.tools import ogn
import sys as sys
import traceback as traceback
import typing
__all__ = ['OgnIsaacScaleToFromStageUnitDatabase', 'carb', 'og', 'ogn', 'sys', 'traceback']
class OgnIsaacScaleToFromStageUnitDatabase(omni.graph.core._impl.database.Database):
    """
    Helper class providing simplified access to data on nodes of type isaacsim.core.nodes.OgnIsaacScaleToFromStageUnit
    
        Class Members:
            node: Node being evaluated
    
        Attribute Value Properties:
            Inputs:
                inputs.conversion
                inputs.value
            Outputs:
                outputs.result
    
        Predefined Tokens:
            tokens.toStage
            tokens.toMeters
        
    """
    class ValuesForInputs(omni.graph.core._impl.database.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES: typing.ClassVar[set] = {'conversion', '_setting_locked', '_batchedReadValues', '_batchedReadAttributes'}
        conversion = ...
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
        @property
        def value(self) -> omni.graph.core._impl.runtime.RuntimeAttribute:
            """
            Get the runtime wrapper class for the attribute inputs.value
            """
        @value.setter
        def value(self, value_to_set: typing.Any):
            """
            Assign another attribute's value to outputs.value
            """
    class ValuesForOutputs(omni.graph.core._impl.database.DynamicAttributeAccess):
        LOCAL_PROPERTY_NAMES: typing.ClassVar[dict] = {}
        def __init__(self, node: omni.graph.core._omni_graph_core.Node, attributes, dynamic_attributes: omni.graph.core._impl.database.DynamicAttributeInterface):
            """
            Initialize simplified access for the attribute data
            """
        def _commit(self):
            ...
        @property
        def result(self) -> omni.graph.core._impl.runtime.RuntimeAttribute:
            """
            Get the runtime wrapper class for the attribute outputs.result
            """
        @result.setter
        def result(self, value_to_set: typing.Any):
            """
            Assign another attribute's value to outputs.result
            """
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
    class tokens:
        toMeters: typing.ClassVar[str] = 'Convert to meters'
        toStage: typing.ClassVar[str] = 'Convert to stage units'
    GENERATOR_VERSION: typing.ClassVar[tuple] = (1, 79, 1)
    INTERFACE: typing.ClassVar[omni.graph.core._impl.database._AllAttributeDefinitions]  # value = <omni.graph.core._impl.database._AllAttributeDefinitions object>
    PER_NODE_DATA: typing.ClassVar[dict] = {}
    TARGET_VERSION: typing.ClassVar[tuple] = (2, 181, 8)
    NODE_TYPE_CLASS = isaacsim.core.nodes.ogn.python.nodes.OgnIsaacScaleToFromStageUnit.OgnIsaacScaleToFromStageUnit
    @staticmethod
    def deregister():
        ...
    @staticmethod
    def register(node_type_class):
        ...
    def __init__(self, node):
        ...
