"""
This module defines an abstract base class for determining positions of graph nodes in a batch within a UI.
"""
from __future__ import annotations
import abc as abc
import omni.kit.widget.graph.graph_model
from omni.kit.widget.graph.graph_model import GraphModel
import typing
import weakref as weakref
__all__: list = ['AbstractBatchPositionGetter']
class AbstractBatchPositionGetter(abc.ABC):
    """
    Helper to get the nodes to move at the same time.
    
        This class is designed to be subclassed to implement specific strategies for determining
        the positions of a batch of nodes in a graph UI. It uses weak references to the graph model
        to avoid circular references and potential memory leaks.
    
        Args:
            model (GraphModel): The graph model associated with this position getter.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'__call__'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __call__(self, drive_item: typing.Any) -> typing.Optional[typing.List[typing.Any]]:
        ...
    def __init__(self, model: omni.kit.widget.graph.graph_model.GraphModel):
        """
        Initializes the AbstractBatchPositionGetter with a given graph model.
        """
    @property
    def model(self):
        """
        Gets the graph model.
        
                Returns:
                    A weak reference to the graph model.
        """
    @model.setter
    def model(self, value):
        """
        Sets the graph model with a weak reference.
        
                Args:
                    value (GraphModel): The graph model to set.
        """
