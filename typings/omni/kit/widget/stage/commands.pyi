from __future__ import annotations
import carb as carb
import omni as omni
import pxr.Sdf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
import typing
__all__: list = ['ReorderPrimCommand', 'ChangePrimDisplayNameCommand']
class ChangePrimDisplayNameCommand(omni.kit.commands.command.Command):
    """
    
        Command to change the display name of a prim.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, stage: pxr.Usd.Stage, prim_path: pxr.Sdf.Path, new_display_name: str):
        """
        
                Constructor.
        
                Args:
                    stage (Usd.Stage): USD stage.
                    prim_path (Sdf.Path): Prim path.
                    new_display_name (str): New display name to be set.
                
        """
    def do(self):
        """
        Renames the prim display name with the new display name, or no operation performed if the prim doesn't exist.
        """
    def undo(self):
        """
        Undo the rename for display name of the prim.
        """
class ReorderPrimCommand(omni.kit.commands.command.Command):
    """
    
        Command to reorder prim under its parent.
        This command uses the support from USD to override the reorder property, and it will always be authored into the
        root layer without considering the edit target.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def _ReorderPrimCommand__move_to(self, location):
        ...
    def __init__(self, stage: pxr.Usd.Stage, prim_path: pxr.Sdf.Path, move_to_location: int):
        """
        
                Constructor.
        
                Args:
                    stage (Usd.Stage): USD stage.
                    prim_path (Sdf.Path): Prim to reorder.
                    move_to_location (int): Move to the location in its parent. If it's -1, it means to move
                        the prim to the bottom.
                
        """
    def do(self):
        """
        Moves the prim to the specified location.
        """
    def undo(self):
        """
        Restores the prim to its previous location.
        """
