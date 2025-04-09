"""
This module provides the BackdropGetter class to identify nodes within a specified backdrop in a graph widget.
"""
from __future__ import annotations
import carb as carb
from functools import lru_cache
import omni.kit.widget.graph.abstract_batch_position_getter
from omni.kit.widget.graph.abstract_batch_position_getter import AbstractBatchPositionGetter
import omni.kit.widget.graph.graph_model
from omni.kit.widget.graph.graph_model import GraphModel
import typing
__all__: list = ['BackdropGetter']
class BackdropGetter(omni.kit.widget.graph.abstract_batch_position_getter.AbstractBatchPositionGetter):
    """
    A class to identify nodes within a specified backdrop in a graph widget.
    
        Args:
            model (GraphModel): The graph model instance to work with.
            is_backdrop_fn (Callable[[Any], bool]): Function to determine if a node is a backdrop.
            graph_widget (Optional): The graph widget instance, if any.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __call__(self, drive_item: typing.Any) -> typing.Optional[typing.List[typing.Any]]:
        ...
    def __init__(self, model: omni.kit.widget.graph.graph_model.GraphModel, is_backdrop_fn: typing.Callable[[typing.Any], bool], graph_widget = None):
        """
        Initialize the BackdropGetter with the provided model and backdrop identification function.
        """
def __get_input(*args, **kwargs):
    ...
def _is_alt_down() -> bool:
    ...
