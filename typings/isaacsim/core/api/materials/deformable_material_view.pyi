from __future__ import annotations
import carb as carb
from isaacsim.core.api.simulation_context.simulation_context import SimulationContext
from isaacsim.core.utils.prims import find_matching_prim_paths
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import is_prim_path_valid
import numpy as np
import omni as omni
from pxr import PhysxSchema
import torch as torch
__all__ = ['DeformableMaterialView', 'PhysxSchema', 'SimulationContext', 'carb', 'find_matching_prim_paths', 'get_prim_at_path', 'is_prim_path_valid', 'np', 'omni', 'torch']
class DeformableMaterialView:
    """
    The view class to deal with deformableMaterial prims.
        Provides high level functions to deal with deformable material (1 or more deformable materials)
        as well as its attributes/ properties. This object wraps all matching materials found at the regex provided at the prim_paths_expr.
        This object wraps all matching materials Prims found at the regex provided at the prim_paths_expr.
        
    """
    def __init__(self, prim_paths_expr: str, name: str = 'deformable_material_view', dynamic_frictions: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, youngs_moduli: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, poissons_ratios: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, elasticity_dampings: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, damping_scales: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None):
        """
        
                Args:
                    prim_paths_expr(str): Prim paths regex to encapsulate all prims that match it.
                    name(str): Shortname to be used as a key by Scene class.
                    dynamic_frictions (Union[np.ndarray, torch.Tensor], optional): The dynamic friction coefficient tensor, shape is (N, ).
                    youngs_moduli (Union[np.ndarray, torch.Tensor], optional): The Young's modulus coefficient tensor, shape is (N, ).
                    poissons_ratios (Union[np.ndarray, torch.Tensor], optional): The Possion ratio coefficient tensor, shape is (N, ).
                    elasticity_dampings (Union[np.ndarray, torch.Tensor], optional): Material damping parameter tensor, shape is (N, ).
                    damping_scales (Union[np.ndarray, torch.Tensor], optional): The damping scale coefficient tensor, shape is (N, ).
                
        """
    def _apply_material_api(self, index):
        ...
    def _invalidate_physics_handle_callback(self, event):
        ...
    def get_damping_scales(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the damping scale of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: damping scale tensor with shape (M, )
                
        """
    def get_dynamic_frictions(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the dynamic friction of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                   Union[np.ndarray, torch.Tensor]: dynamic friction tensor with shape (M, )
                
        """
    def get_elasticity_dampings(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the elasticity dampings of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: elasticity dampings tensor with shape (M, )
                
        """
    def get_poissons_ratios(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the poissons ratios of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: poissons ratio tensor with shape (M, )
                
        """
    def get_youngs_moduli(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the Youngs moduli of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: Youngs moduli tensor with shape (M, )
                
        """
    def initialize(self, physics_sim_view: omni.physics.tensors.bindings._physicsTensors.SimulationView = None) -> None:
        """
        Create a physics simulation view if not passed and creates a rigid body view in physX.
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
                
        """
    def is_physics_handle_valid(self) -> bool:
        """
        
                Returns:
                    bool: True if the physics handle of the view is valid (i.e physics is initialized for the view). Otherwise False.
                
        """
    def is_valid(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> bool:
        """
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    bool: True if all prim paths specified in the view correspond to a valid prim in stage. False otherwise.
                
        """
    def post_reset(self) -> None:
        """
        Resets the deformables to their initial states.
        """
    def set_damping_scales(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the damping scale for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material damping scale tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_dynamic_frictions(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the dynamic friction for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material dynamic friction tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_elasticity_dampings(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the elasticity_dampings for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material damping tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_poissons_ratios(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the poissons ratios for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material poissons ratio tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_youngs_moduli(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the youngs moduli for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material drag tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    @property
    def count(self) -> int:
        """
        
                Returns:
                    int: number of rigid shapes for the prims in the view.
                
        """
    @property
    def name(self) -> str:
        """
        
                Returns:
                    str: name given to the view when instantiating it.
                
        """
