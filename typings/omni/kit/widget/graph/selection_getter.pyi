"""
This module provides the SelectionGetter class to retrieve the selection from a given GraphModel.
"""
from __future__ import annotations
import omni.kit.widget.graph.abstract_batch_position_getter
from omni.kit.widget.graph.abstract_batch_position_getter import AbstractBatchPositionGetter
import omni.kit.widget.graph.graph_model
from omni.kit.widget.graph.graph_model import GraphModel
import typing
__all__: list = ['SelectionGetter']
class SelectionGetter(omni.kit.widget.graph.abstract_batch_position_getter.AbstractBatchPositionGetter):
    """
    A class for retrieving the selection from a GraphModel.
    
        This helper class is designed to be used in conjunction with GraphModelBatchPosition to obtain the current selection within the GraphModel.
    
        Args:
            model (GraphModel): The graph model from which the selection is to be retrieved.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __call__(self, drive_item: typing.Any):
        ...
    def __init__(self, model: omni.kit.widget.graph.graph_model.GraphModel):
        """
        Initializes a new instance of the SelectionGetter class.
        """
