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
__all__ = ['ParticleMaterialView', 'PhysxSchema', 'SimulationContext', 'carb', 'find_matching_prim_paths', 'get_prim_at_path', 'is_prim_path_valid', 'np', 'omni', 'torch']
class ParticleMaterialView:
    """
    The view class to deal with particleMaterial prims.
        Provides high level functions to deal with particle material (1 or more particle materials)
        as well as its attributes/ properties. This object wraps all matching materials found at the regex provided at the prim_paths_expr.
        This object wraps all matching materials Prims found at the regex provided at the prim_paths_expr.
        
    """
    def __init__(self, prim_paths_expr: str, name: str = 'particle_material_view', frictions: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, particle_friction_scales: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, dampings: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, viscosities: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, vorticity_confinements: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, surface_tensions: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, cohesions: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, adhesions: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, particle_adhesion_scales: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, adhesion_offset_scales: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, gravity_scales: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, lifts: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, drags: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None):
        """
        
                Args:
                    prim_paths_expr(str): Prim paths regex to encapsulate all prims that match it.
                    name(str): Shortname to be used as a key by Scene class.
                    frictions (Union[np.ndarray, torch.Tensor], optional): The friction coefficient tensor, shape is (N, ).
                    particle_friction_scales (Union[np.ndarray, torch.Tensor], optional): The coefficient that scales friction for
                        solid particle-particle interactions, shape is (N, ).
                    dampings (Union[np.ndarray, torch.Tensor], optional): The global velocity damping tensor, shape is (N, ).
                    viscosities (Union[np.ndarray, torch.Tensor], optional): The viscosity tensor of fluid particles, shape is (N, ).
                    vorticity_confinements (Union[np.ndarray, torch.Tensor], optional): The vorticity confinement tensor for fluid particles, shape is (N, ).
                    surface_tensions (Union[np.ndarray, torch.Tensor], optional): The surface tension tensor, shape is (N, ).
                    cohesions (Union[np.ndarray, torch.Tensor], optional): The cohesion tensor for interaction between fluid particles, shape is (N, ).
                    adhesions (Union[np.ndarray, torch.Tensor], optional): The adhesion tensor for interaction between particles (solid or fluid),
                        and rigid or deformable objects, shape is (N, ).
                    particle_adhesion_scales (Union[np.ndarray, torch.Tensor], optional): The coefficient tensor that scales adhesion for solid
                        particle-particle iterations, shape is (N, ).
                    adhesion_offset_scales (Union[np.ndarray, torch.Tensor], optional): The offset scale tensor defines at which adhesion ceases
                        to take effect, shape is (N, ).
                    gravity_scales (Union[np.ndarray, torch.Tensor], optional): The gravitational acceleration scaling tensor. It can be used
                        to approximate lighter-than-air inflatables, shape is (N, ).
                    lifts (Union[np.ndarray, torch.Tensor], optional): The lift coefficient tensor for cloth and inflatable particle objects, shape is (N, ).
                    drags (Union[np.ndarray, torch.Tensor], optional): The drag coefficient tensor for cloth and inflatable particle objects, shape is (N, ).
                
        """
    def _apply_material_api(self, index):
        ...
    def _invalidate_physics_handle_callback(self, event):
        ...
    def get_adhesion_offset_scales(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the adhesion offset scale of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: adhesion offset scale tensor with shape (M, )
                
        """
    def get_adhesions(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the adhesion of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: adhesion tensor with shape (M, )
                
        """
    def get_cohesions(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the cohesion of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: cohesion tensor with shape (M, )
                
        """
    def get_dampings(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the dampings of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: dampings tensor with shape (M, )
                
        """
    def get_drags(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the drags of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: drag tensor with shape (M, )
                
        """
    def get_frictions(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the friction of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                   Union[np.ndarray, torch.Tensor]: friction tensor with shape (M, )
                
        """
    def get_gravity_scales(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the gravity scale of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: gravity scale tensor with shape (M, )
                
        """
    def get_lifts(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the lifts of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: lift tensor with shape (M, )
                
        """
    def get_particle_adhesion_scales(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the adhesion scale of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: adhesion scale tensor with shape (M, )
                
        """
    def get_particle_friction_scales(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the particle friction scale of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: particle friction scale tensor with shape (M, )
                
        """
    def get_surface_tensions(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the surface tension of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: surface tension tensor with shape (M, )
                
        """
    def get_viscosities(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the viscosity of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: viscosity tensor with shape (M, )
                
        """
    def get_vorticity_confinements(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Gets the vorticity confinement of materials indicated by the indices.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: vorticity confinement tensor with shape (M, )
                
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
        Resets the particles to their initial states.
        """
    def set_adhesion_offset_scales(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the adhesion offset scale for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material adhesion offset scale tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_adhesions(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the particle adhesion for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material particle adhesion scale tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_cohesions(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the particle cohesion for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material particle cohesion scale tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_dampings(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the dampings for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material damping tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_drags(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the drags for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material drag tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_frictions(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the friction for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material friction tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_gravity_scales(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the gravity scale for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material gravity scale tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_lifts(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the lifts for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material lift tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_particle_adhesion_scales(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the particle adhesion for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material particle adhesion scale tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_particle_friction_scales(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the particle friction scale for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material particle friction scale tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_surface_tensions(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the particle surface tension for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material particle surface tension scale tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_viscosities(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the particle viscosity for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material particle viscosity scale tensor with the shape (M, ).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional): indices to specify which material prims to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                
        """
    def set_vorticity_confinements(self, values: typing.Union[numpy.ndarray, torch.Tensor, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, NoneType] = None) -> None:
        """
        Sets the vorticity confinement for the material prims indicated by the indices.
        
                Args:
                    values (Optional[Union[np.ndarray, torch.Tensor]], optional): material particle vorticity confinement scale tensor with the shape (M, ).
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
