"""
This module provides classes for caching and indexing graph nodes, ports, and connections to improve model access efficiency.
"""
from __future__ import annotations
from collections import defaultdict
import itertools as itertools
from omni.kit.widget.graph.graph_model import GraphModel
import weakref as weakref
__all__: list = ['GraphNodeIndex']
class CacheConnection:
    """
    The structure to keep connections in the cache and don't access the model many times
    """
    def __eq__(self, other):
        ...
    def __hash__(self):
        ...
    def __init__(self, source_cached_port: CachePort, target_cached_port: CachePort):
        ...
    def __repr__(self):
        ...
    @property
    def pair(self):
        ...
class CacheNode:
    """
    The structure to keep in the cache and don't access the model many times
    """
    def __eq__(self, other):
        ...
    def __hash__(self):
        ...
    def __init__(self, node: typing.Any, state: typing.Optional[omni.kit.widget.graph.graph_model.GraphModel.ExpansionState], cached_ports: typing.List[omni.kit.widget.graph.graph_node_index.CachePort], stacking_order: int, icon: str, additional_hash = 0):
        ...
    def __repr__(self):
        ...
class CachePort:
    """
    
        The structure to keep in the ports and their properties and don't
        access the model many times.
        
    """
    def __eq__(self, other):
        ...
    def __hash__(self):
        ...
    def __init__(self, port: typing.Any, name: str, state: typing.Optional[omni.kit.widget.graph.graph_model.GraphModel.ExpansionState], child_count: int, level: int, relative_position: int, parent_child_count: int, siblings_below, parent_cached_port: typing.Optional[weakref.ProxyType] = None):
        ...
    def __repr__(self):
        ...
class GraphNodeDiff:
    """
    
        The object that keeps the difference that is the list of nodes and
        connections to add and delete.
        
    """
    def __init__(self, nodes_to_add: typing.List[omni.kit.widget.graph.graph_node_index.CacheNode] = None, nodes_to_del: typing.List[omni.kit.widget.graph.graph_node_index.CacheNode] = None, connections_to_add: typing.List[omni.kit.widget.graph.graph_node_index.CacheConnection] = None, connections_to_del: typing.List[omni.kit.widget.graph.graph_node_index.CacheConnection] = None):
        ...
    def __repr__(self):
        ...
    @property
    def valid(self):
        ...
class GraphNodeIndex:
    """
    A class for caching and indexing graph nodes, ports, and connections to improve access efficiency in a model.
    
        This class provides methods for quickly accessing and modifying nodes and connections within a graph model based on a hierarchical index. It's designed to optimize read and write operations by maintaining an internal cache of graph elements.
    
        Args:
            model (Optional[GraphModel]): The graph model to index.
            port_grouping (bool): Flag indicating whether to group ports.
    
        Note:
            The initialization of this class involves building caches and indices for nodes, ports, and connections, and may have performance implications on large graphs.
        
    """
    def __init__(self, model: typing.Optional[omni.kit.widget.graph.graph_model.GraphModel], port_grouping: bool):
        """
        Initializes a new instance of the GraphNodeIndex class.
        """
    def get_diff(self, other: GraphNodeIndex):
        """
        Generates the difference object: the list of nodes and connections to add and delete.
        
                Args:
                    other (GraphNodeIndex): The GraphNodeIndex to compare with the current GraphNodeIndex.
        
                Returns:
                    GraphNodeDiff: An object representing the difference between this GraphNodeIndex and another.
        """
    def mutate(self, diff: typing.Union[ForwardRef('GraphNodeIndex'), omni.kit.widget.graph.graph_node_index.GraphNodeDiff]) -> typing.Tuple[typing.Set]:
        """
        Apply the difference to the cache index.
        
                Args:
                    diff (Union["GraphNodeIndex", GraphNodeDiff]): The difference to apply to the current GraphNodeIndex.
        
                Returns:
                    Tuple[Set]: A tuple containing sets of added nodes, deleted nodes, added connections, and deleted connections.
                
        """
