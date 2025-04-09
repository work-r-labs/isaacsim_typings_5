from __future__ import annotations
import carb as carb
from isaacsim.core.api.simulation_context.simulation_context import SimulationContext
from isaacsim.core.utils.prims import find_matching_prim_paths
from isaacsim.core.utils.prims import get_prim_at_path
import numpy as np
import omni as omni
from pxr import PhysxSchema
from pxr import UsdPhysics
import torch as torch
import warp as wp
__all__ = ['PhysxSchema', 'RigidContactView', 'SimulationContext', 'UsdPhysics', 'carb', 'find_matching_prim_paths', 'get_prim_at_path', 'np', 'omni', 'torch', 'wp']
class RigidContactView:
    """
    Provides high level functions to deal with rigid prims (one or many) that track their contacts through filters
        as well as their attributes/properties.
    
        This class wraps all matching rigid prims found at the regex provided at the ``prim_paths_expr`` argument
    
        .. warning::
    
            The rigid prim view object must be initialized in order to be able to operate on it.
            See the ``initialize`` method for more details.
    
        Args:
            prim_paths_expr (Union[str, List[str]]): prim paths regex to encapsulate all prims that match it.
                                    example: "/World/Env[1-5]/Cube" will match /World/Env1/Cube,
                                    /World/Env2/Cube..etc.
                                    (a non regex prim path can also be used to encapsulate one rigid prim).  Additionally a
                                    list of regex can be provided. example ["/World/Env[1-5]/Cube", "/World/Env[10-19]/Cube"].
            filter_paths_expr Union[List[str], List[List[str]]]: list of prim paths regex to filter the contacts for each corresponding
                                                                  prim_paths_expr. Example: ["/World/envs/env_2/Xform"] will filter the contacts corresponding to
                                                                  the expression passed.
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "rigid_contact_view".
            prepare_contact_sensors (bool, Optional): if rigid prims in the view are not cloned from a prim in a prepared state,
                                                      (although slow for large number of prims) this ensures that
                                                      appropriate physics settings are applied on all the prim in the view.
            disable_stablization (bool, optional): disables the contact stabilization parameter in the physics context
            max_contact_count (int, optional): maximum number of contact data to report when detailed contact information is needed
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>> from isaacsim.core.cloner import GridCloner
            >>> from isaacsim.core.api.sensors import RigidContactView
            >>> from pxr import UsdGeom
            >>>
            >>> env_zero_path = "/World/envs/env_0"
            >>> num_envs = 5
            >>>
            >>> # clone the environment (num_envs)
            >>> cloner = GridCloner(spacing=0)
            >>> cloner.define_base_env(env_zero_path)
            >>> UsdGeom.Xform.Define(stage_utils.get_current_stage(), env_zero_path)
            >>> stage_utils.get_current_stage().DefinePrim(f"{env_zero_path}/Xform", "Xform")
            >>> stage_utils.get_current_stage().DefinePrim(f"{env_zero_path}/Xform/Cube", "Cube")
            >>> # position the cubes on top of each other
            >>> position_offsets = np.zeros((num_envs, 3))
            >>> position_offsets[:, 2] = np.arange(num_envs) * 1.1
            >>> env_pos = cloner.clone(
            ...     source_prim_path=env_zero_path,
            ...     prim_paths=cloner.generate_paths("/World/envs/env", num_envs),
            ...     position_offsets=position_offsets
            ...     copy_from_source=True,
            ... )
            >>>
            >>> # wrap the prims
            >>> prims = RigidContactView(
            ...     prim_paths_expr="/World/envs/env.*/Xform",
            ...     name="RigidContactView_view",
            ...     filter_paths_expr=["/World/envs/env_2/Xform"],
            ...     max_contact_count=10,
            ... )
            >>> prims
            <isaacsim.core.api.sensors.rigid_contact_view.RigidContactView object at 0x7f8d4eb1abf0>
        
    """
    def __init__(self, prim_paths_expr: typing.Union[str, typing.List[str]], filter_paths_expr: typing.Union[typing.List[str], typing.List[typing.List[str]]], name: str = 'rigid_contact_view', prepare_contact_sensors: bool = True, disable_stablization: bool = True, max_contact_count: int = 0) -> None:
        ...
    def _invalidate_physics_handle_callback(self, event):
        ...
    def _prepare_contact_reporter(self, prim_at_path):
        """
        Prepares the contact reporter by removing the contact thresholds.
        """
    def get_contact_force_data(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True, dt: float = 1.0) -> typing.Tuple[typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray], typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray], typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray], typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray], typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray], typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]]:
        """
        Get more detailed contact information between the prims in the view and the filter prims.
        
                Specifically, this method provides individual contact normals, contact points, contact separations as well as
                contact forces for each pair (the sum of which equals the forces that the ``get_contact_force_matrix``
                method provides as the force aggregate of a pair)
        
                Given to the dynamic nature of collision between bodies, this method will provide buffers of contact data which
                are arranged sequentially for each pair. The starting index and the number of contact data points for each pair
                in this stream can be realized from pair_contacts_start_indices, and pair_contacts_count tensors.
                They both have a dimension of ``(num_shapes, num_filters)`` where ``num_filters`` is determined
                according to the ``filter_paths_expr`` parameter
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
                    dt (float): time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses
        
                Returns:
                    Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray],
                    Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray],
                    Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]:
                    A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3),
                    and distances with shape (max_contact_count, 1), as well as two tensors with shape (M, self.num_filters)
                    to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get detailed contact force data between the prims and the filter prims (the cube in the middle)
                    >>> data = prims.get_contact_force_data()
                    >>> data[0]  # normal forces
                    [[-168.53815]
                     [ -89.57392]
                     [-156.10307]
                     [ -75.17234]
                     [  98.0681 ]
                     [  52.56319]
                     [ 108.26558]
                     [  67.62025]
                     [   0.     ]
                     [   0.     ]]
                    >>> data[1]  # points
                    [[ 0.4948182  -0.49902824  1.5001888 ]
                     [ 0.4950411   0.49933064  1.5001996 ]
                     [-0.5024581   0.49930018  1.5001924 ]
                     [-0.5024276  -0.49880558  1.5001817 ]
                     [-0.5023767   0.497138    2.5001519 ]
                     [-0.502735   -0.49877006  2.5001822 ]
                     [ 0.4947694  -0.4989927   2.500226  ]
                     [ 0.4949917   0.49677914  2.5001955 ]
                     [ 0.          0.          0.        ]
                     [ 0.          0.          0.        ]]
                    >>> data[2]  # normals
                    [[-4.3812128e-05  3.0501858e-05  1.0000000e+00]
                     [-4.3812128e-05  3.0501858e-05  1.0000000e+00]
                     [-4.3812128e-05  3.0501858e-05  1.0000000e+00]
                     [-4.3812128e-05  3.0501858e-05  1.0000000e+00]
                     [ 2.1408198e-06 -7.0731985e-05  1.0000000e+00]
                     [ 2.1408198e-06 -7.0731985e-05  1.0000000e+00]
                     [ 2.1408198e-06 -7.0731985e-05  1.0000000e+00]
                     [ 2.1408198e-06 -7.0731985e-05  1.0000000e+00]
                     [ 0.0000000e+00  0.0000000e+00  0.0000000e+00]
                     [ 0.0000000e+00  0.0000000e+00  0.0000000e+00]]
                    >>> data[3]  # distances
                    [[ 3.7143487e-05]
                     [-4.0254322e-06]
                     [-4.0531158e-05]
                     [ 6.0737699e-07]
                     [ 1.9307560e-04]
                     [ 9.2272363e-05]
                     [ 4.6372414e-05]
                     [ 1.4718286e-04]
                     [ 0.0000000e+00]
                     [ 0.0000000e+00]]
                    >>> data[4]  # pair contacts count
                    [[0]
                     [4]
                     [0]
                     [4]
                     [0]]
                    >>> data[5]  # start indices of pair contacts
                    [[0]
                     [0]
                     [4]
                     [4]
                     [8]]
                
        """
    def get_contact_force_matrix(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True, dt: float = 1.0) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the contact forces between the prims in the view and the filter prims.
        
                E.g., a matrix of dimension ``(num_shapes, num_filters, 3)`` where ``num_filters`` is
                determined according to the ``filter_paths_expr`` parameter
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
                    dt (float): time step multiplier to convert the underlying impulses to forces. The function returns contact impulses if the default dt is used
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: Net contact forces between the view prim and the filter prims with shape (M, self.num_filters, 3).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the contact forces between the prims and the filter prims (the cube in the middle)
                    >>> prims.get_contact_force_matrix()
                    [[[ 0.0000000e+00  0.0000000e+00  0.0000000e+00]]
                     [[ 2.2649009e-02 -1.3710857e-02 -4.9047806e+02]]
                     [[ 0.0000000e+00  0.0000000e+00  0.0000000e+00]]
                     [[-3.3276828e-03 -2.3870371e-02  3.2733777e+02]]
                     [[ 0.0000000e+00  0.0000000e+00  0.0000000e+00]]]
                
        """
    def get_friction_data(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True, dt: float = 1.0) -> typing.Tuple[typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray], typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray], typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray], typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]]:
        """
        
                Gets friction data between the prims in the view and the filter prims. Specifically, this method provides frictional contact forces,
                and points. The data in reported for number of anchor points that includes tangential forces in a single tangent direction to contact normal.
                Given to the dynamic nature of collision between bodies, this method will provide buffers of friction data arranged sequentially for each pair.
                The starting index and the number of contact data points for each pair in this stream can be realized from pair_contacts_start_indices,
                and pair_contacts_count tensors. They both have a dimension of (self.num_shapes, self.num_filters) where filter_count is determined
                according to the filter_paths_expr parameter.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indicies to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
                    dt (float): time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses
        
                Returns:
                    Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray],
                        Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]:
                        A set of buffers for tangential forces per patch (at number of anchor points, each in a single directions)
                        with shape (max_contact_count, 3), points with shape (max_contact_count, 3),
                        as well as two tensors with shape (M, self.num_filters) to indicate the starting index and the number of
                        contact data points per pair in the aforementioned buffers.
                
        """
    def get_net_contact_forces(self, indices: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True, dt: float = 1.0) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the overall net contact forces on the prims in the view with respect to the world's frame.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
                    dt (float): time step multiplier to convert the underlying impulses to forces. The function returns contact impulses if the default dt is used
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: Net contact forces of the prims with shape (M,3).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the net contact force on all rigid bodies. Returned shape is (5, 3).
                    >>> prims.get_net_contact_forces()
                    [[ 1.8731881e-03  5.4876995e-03  1.6408131e+02]
                     [ 1.9060407e-02 -2.2513291e-02  1.6358723e+02]
                     [-2.1011427e-02  3.5647806e-02  1.6371542e+02]
                     [ 9.4006478e-05 -9.3258200e-03  1.6348369e+02]
                     [ 9.3709816e-05 -9.2963902e-03  1.6296776e+02]]
                    >>>
                    >>> # get the net contact force on the rigid bodies for the first, middle and last of the 5 envs
                    >>> prims.get_net_contact_forces(indices=np.array([0, 2, 4]))
                    [[ 1.8731881e-03  5.4876995e-03  1.6408131e+02]
                     [-2.1011427e-02  3.5647806e-02  1.6371542e+02]
                     [ 9.3709816e-05 -9.2963902e-03  1.6296776e+02]]
                
        """
    def initialize(self, physics_sim_view: omni.physics.tensors.bindings._physicsTensors.SimulationView = None) -> None:
        """
        Create a physics simulation view if not passed and set other properties using the PhysX tensor API
        
                .. note::
        
                    If the rigid prim view has been added to the world scene (e.g., ``world.scene.add(prims)``),
                    it will be automatically initialized when the world is reset (e.g., ``world.reset()``).
        
                .. warning::
        
                    This method needs to be called after each hard reset (e.g., Stop + Play on the timeline)
                    before interacting with any other class method.
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.initialize()
                
        """
    def is_physics_handle_valid(self) -> bool:
        """
        Check if rigid prim view's physics handler is initialized
        
                .. warning::
        
                    If the physics handler is not valid many of the methods that requires PhysX will return None.
        
                Returns:
                    bool: True if the physics handle of the view is valid (i.e physics is initialized for the view). Otherwise False.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.is_physics_handle_valid()
                    True
                
        """
    @property
    def num_filters(self) -> int:
        """
        
                Returns:
                    int: number of filters bodies that report their contact with the rigid prims.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_filters
                    1
                
        """
    @property
    def num_shapes(self) -> int:
        """
        
                Returns:
                    int: number of rigid shapes for the prims in the view.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_shapes
                    5
                
        """
