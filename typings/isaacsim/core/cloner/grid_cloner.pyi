from __future__ import annotations
import isaacsim.core.cloner.cloner
from isaacsim.core.cloner.cloner import Cloner
import numpy
import numpy as np
import omni as omni
from pxr import Gf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
import torch as torch
__all__ = ['Cloner', 'Gf', 'GridCloner', 'Usd', 'UsdGeom', 'np', 'omni', 'torch']
class GridCloner(isaacsim.core.cloner.cloner.Cloner):
    """
    This is a specialized Cloner class that will automatically generate clones in a grid fashion.
    """
    def __init__(self, spacing: float, num_per_row: int = -1, stage: pxr.Usd.Stage = None):
        """
        
                Args:
                    spacing (float): Spacing between clones.
                    num_per_row (int): Number of clones to place in a row. Defaults to sqrt(num_clones).
                    stage (Usd.Stage): Usd stage where source prim and clones are added to.
                
        """
    def clone(self, source_prim_path: str, prim_paths: typing.List[str], position_offsets: numpy.ndarray = None, orientation_offsets: numpy.ndarray = None, replicate_physics: bool = False, base_env_path: str = None, root_path: str = None, copy_from_source: bool = False, enable_env_ids: bool = False):
        """
        Creates clones in a grid fashion. Positions of clones are computed automatically.
        
                Args:
                    source_prim_path (str): Path of source object.
                    prim_paths (List[str]): List of destination paths.
                    position_offsets (np.ndarray): Positions to be applied as local translations on top of computed clone position.
                                                   Defaults to None, no offset will be applied.
                    orientation_offsets (np.ndarray): Orientations to be applied as local rotations for each clone.
                                                   Defaults to None, no offset will be applied.
                    replicate_physics (bool): Uses omni.physics replication. This will replicate physics properties directly for paths beginning with root_path and skip physics parsing for anything under the base_env_path.
                    base_env_path (str): Path to namespace for all environments. Required if replicate_physics=True and define_base_env() not called.
                    root_path (str): Prefix path for each environment. Required if replicate_physics=True and generate_paths() not called.
                    copy_from_source: (bool): Setting this to False will inherit all clones from the source prim; any changes made to the source prim will be reflected in the clones.
                                 Setting this to True will make copies of the source prim when creating new clones; changes to the source prim will not be reflected in clones. Defaults to False. Note that setting this to True will take longer to execute.
                    enable_env_ids (bool): Setting this enables co-location of clones in physics with automatic filtering of collisions between clones.
                Returns:
                    positions (List): Computed positions of all clones.
                
        """
    def get_clone_transforms(self, num_clones: int, position_offsets: numpy.ndarray = None, orientation_offsets: numpy.ndarray = None):
        """
        Computes the positions and orientations of clones in a grid.
        
                Args:
                    num_clones (int): Number of clones.
                    position_offsets (np.ndarray): Positions to be applied as local translations on top of computed clone position.
                    position_offsets (np.ndarray | torch.Tensor): Positions to be applied as local translations on top of computed clone position.
                                                   Defaults to None, no offset will be applied.
                    orientation_offsets (np.ndarray | torch.Tensor): Orientations to be applied as local rotations for each clone.
                                                   Defaults to None, no offset will be applied.
                Returns:
                    positions (List): Computed positions of all clones.
                    orientations (List): Computed orientations of all clones.
                
        """
