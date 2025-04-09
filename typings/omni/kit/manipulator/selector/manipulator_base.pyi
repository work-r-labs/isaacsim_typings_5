from __future__ import annotations
import abc
from abc import ABC
from abc import abstractmethod
import asyncio as asyncio
from omni.kit.manipulator.selector.extension import get_manipulator_selector
from pxr import Sdf
import pxr.Usd
from pxr import Usd
import typing
__all__ = ['ABC', 'ManipulatorBase', 'Sdf', 'Usd', 'abstractmethod', 'asyncio', 'get_manipulator_selector']
class ManipulatorBase(abc.ABC):
    """
    
        Base class for prim manipulator that works with ManipulatorSelector.
        Instead of subscribing to UsdStageEvent for selection change, manipulator should inherit this class and implements
        all abstractmethods to support choosing between multiple types of prim manipulators based on their order and enable
        criterions.
    
        The order of the manipulator is specified at carb.settings path `/persistent/exts/omni.kit.manipulator.selector/orders/<name>"`
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'on_selection_changed', 'enabled'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __del__(self):
        ...
    def __init__(self, name: str, usd_context_name: str):
        """
        
                Constructor.
        
                Args:
                    name (str): name of the manipulator. It must match the <name> in the setting path specifies order.
                    usd_context_name (str): name of the UsdContext this manipulator operates on.
                
        """
    def _delayed_register(self):
        ...
    def destroy(self):
        ...
    def on_selection_changed(self, stage: pxr.Usd.Stage, selection: typing.Optional[typing.List[pxr.Sdf.Path]], *args, **kwargs) -> bool:
        """
        
                Function called when selection changes or types of prim manipulators are added or removed.
        
                Args:
                    stage (Usd.Stage): the usd stage of which the selection change happens. It is the same as the stage of the
                                       UsdContext this manipulator works on.
                    selection (Union[List[Sdf.Path], None]): the list of selected prim paths. If it is None (different from []),
                                                             it means another manipulator with higher priority has handled the
                                                             selection and this manipulator should yield.
        
                Return:
                    True if selected prim paths can be handled by this manipulator and subsequent manipulator with higher order
                    should yield.
                    False if selected prim paths can not be handled. Function should always return False if `selection` is None.
                
        """
    @property
    def enabled(self) -> bool:
        """
        
                Returns if this manipulator is enabled.
                
        """
    @enabled.setter
    def enabled(self, value: bool):
        """
        
                Sets if this manipulator is enabled. A disabled manipulator should hide itself.
                
        """
