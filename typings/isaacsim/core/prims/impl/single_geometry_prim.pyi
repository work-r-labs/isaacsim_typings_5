from __future__ import annotations
import isaacsim.core.prims.impl._impl.single_prim_wrapper
from isaacsim.core.prims.impl._impl.single_prim_wrapper import _SinglePrimWrapper
from isaacsim.core.prims.impl.geometry_prim import GeometryPrim
import numpy as np
from pxr import UsdGeom
import pxr.UsdGeom
import torch as torch
__all__ = ['GeometryPrim', 'SingleGeometryPrim', 'UsdGeom', 'np', 'torch']
class SingleGeometryPrim(isaacsim.core.prims.impl._impl.single_prim_wrapper._SinglePrimWrapper):
    """
    High level wrapper to deal with a Geom prim (only one geometry prim) and its attributes/properties.
    
        The ``prim_path`` should correspond to type UsdGeom.Cube, UsdGeom.Capsule, UsdGeom.Cone, UsdGeom.Cylinder,
        UsdGeom.Sphere or UsdGeom.Mesh.
    
        .. warning::
    
            The geometry object must be initialized in order to be able to operate on it.
            See the ``initialize`` method for more details.
    
        .. warning::
    
            Some methods require the prim to have the Physx Collision API. Instantiate the class with the ``collision``
            parameter to True to apply the collision API.
    
        Args:
            prim_path (str): prim path of the Prim to encapsulate or create.
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "xform_prim".
            position (Optional[Sequence[float]], optional): position in the world frame of the prim. shape is (3, ).
                                                        Defaults to None, which means left unchanged.
            translation (Optional[Sequence[float]], optional): translation in the local frame of the prim
                                                            (with respect to its parent prim). shape is (3, ).
                                                            Defaults to None, which means left unchanged.
            orientation (Optional[Sequence[float]], optional): quaternion orientation in the world/ local frame of the prim
                                                            (depends if translation or position is specified).
                                                            quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                            Defaults to None, which means left unchanged.
            scale (Optional[Sequence[float]], optional): local scale to be applied to the prim's dimensions. shape is (3, ).
                                                    Defaults to None, which means left unchanged.
            visible (bool, optional): set to false for an invisible prim in the stage while rendering. Defaults to True.
            collision (bool, optional): Set to True if the geometry should have a collider (i.e not only a visual geometry).
                                        Defaults to False.
            track_contact_forces (bool, Optional) : if enabled, the view will track the net contact forces on each geometry prim in the view.
                                                    Note that the collision flag should be set to True to report contact forces. Defaults to False.
            prepare_contact_sensors (bool, Optional): applies contact reporter API to the prim if it already does not have one. Defaults to False.
            disable_stablization (bool, optional): disables the contact stabilization parameter in the physics context. Defaults to True.
            contact_filter_prim_paths_expr (Optional[List[str]], Optional): a list of filter expressions which allows for tracking contact forces
                                                                    between the geometry prim and this subset through get_contact_force_matrix().
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>> from isaacsim.core.prims import SingleGeometryPrim
            >>>
            >>> # create a Cube at the given path
            >>> stage_utils.get_current_stage().DefinePrim("/World/Xform", "Xform")
            >>> stage_utils.get_current_stage().DefinePrim("/World/Xform/Cube", "Cube")
            >>>
            >>> # wrap the prim as geometry prim
            >>> prim = SingleGeometryPrim("/World/Xform", collision=True)
            >>> prim
            <isaacsim.core.prims.single_geometry_prim.SingleGeometryPrim object at 0x7fe960247400>
        
    """
    def __init__(self, prim_path: str, name: str = 'geometry_prim', position: typing.Optional[typing.Sequence[float]] = None, translation: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None, scale: typing.Optional[typing.Sequence[float]] = None, visible: typing.Optional[bool] = None, collision: bool = False, track_contact_forces: bool = False, prepare_contact_sensor: bool = False, disable_stablization: bool = True, contact_filter_prim_paths_expr: typing.Optional[typing.List[str]] = list()) -> None:
        ...
    def apply_physics_material(self, physics_material: PhysicsMaterial, weaker_than_descendants: bool = False):
        """
        Used to apply physics material to the held prim and optionally its descendants.
        
                Args:
                    physics_material (PhysicsMaterial): physics material to be applied to the held prim. This where you want to
                                                        define friction, restitution..etc. Note: if a physics material is not
                                                        defined, the defaults will be used from PhysX.
                    weaker_than_descendants (bool, optional): True if the material shouldn't override the descendants
                                                              materials, otherwise False. Defaults to False.
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.core.api.materials import PhysicsMaterial
                    >>>
                    >>> # create a rigid body physical material
                    >>> material = PhysicsMaterial(
                    ...     prim_path="/World/physics_material/aluminum",  # path to the material prim to create
                    ...     dynamic_friction=0.4,
                    ...     static_friction=1.1,
                    ...     restitution=0.1
                    ... )
                    >>> prim.apply_physics_material(material)
                
        """
    def get_applied_physics_material(self) -> PhysicsMaterial:
        """
        Return the current applied physics material in case it was applied using apply_physics_material or not.
        
                Returns:
                    PhysicsMaterial: the current applied physics material.
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a physics material applied
                    >>> prim.get_applied_physics_material()
                    <isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
                
        """
    def get_collision_approximation(self) -> str:
        """
        Get the collision approximation
        
                .. list-table::
                    :header-rows: 1
        
                    * - Approximation
                      - Full name
                      - Description
                    * - ``"none"``
                      - Triangle Mesh
                      - The mesh geometry is used directly as a collider without any approximation
                    * - ``"convexDecomposition"``
                      - Convex Decomposition
                      - A convex mesh decomposition is performed. This results in a set of convex mesh colliders
                    * - ``"convexHull"``
                      - Convex Hull
                      - A convex hull of the mesh is generated and used as the collider
                    * - ``"boundingSphere"``
                      - Bounding Sphere
                      - A bounding sphere is computed around the mesh and used as a collider
                    * - ``"boundingCube"``
                      - Bounding Cube
                      - An optimally fitting box collider is computed around the mesh
                    * - ``"meshSimplification"``
                      - Mesh Simplification
                      - A mesh simplification step is performed, resulting in a simplified triangle mesh collider
                    * - ``"sdf"``
                      - SDF Mesh
                      - SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
                    * - ``"sphereFill"``
                      - Sphere Approximation
                      - A sphere mesh decomposition is performed. This results in a set of sphere colliders
        
                Returns:
                    str: approximation used for collision
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.get_collision_approximation()
                    none
                
        """
    def get_collision_enabled(self) -> bool:
        """
        Check if the Collision API is enabled
        
                Returns:
                    bool: True if the Collision API is enabled. Otherwise False
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.get_collision_enabled()
                    True
                
        """
    def get_contact_force_data(self, dt: float = 1.0) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                If the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims
                in the view and the filter prims including the normal contact forces, normal directions, contact points, separations.
                The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while
                the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
        
                Args:
                    dt (float): time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses
        
                Returns:
                    Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray],
                    Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray],
                    Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]:
                    A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3),
                    and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters)
                    to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.
                
        """
    def get_contact_force_matrix(self, dt: float = 1.0) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                If the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims
                in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3)
                where num_filters is the determined according to the filter_paths_expr parameter.
        
                Args:
                    dt (float): time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).
                
        """
    def get_contact_offset(self) -> float:
        """
        Get the contact offset
        
                Shapes whose distance is less than the sum of their contact offset values will generate contacts
        
                Search for *Advanced Collision Detection* in |physx_docs| for more details
        
                Returns:
                    float: contact offset of the collision shape. Default value is -inf, means default is picked by simulation.
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.get_contact_offset()
                    -inf
                
        """
    def get_friction_data(self, dt: float = 1.0) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                If the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims
                in the view and the filter prims including the tangential forces, and points.
                The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while
                the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
        
                Args:
                    dt (float): time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses
        
                Returns:
                    Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray],
                    Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]:
                    A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3),
                    as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of
                    contact data points per pair in the aforementioned buffers.
                
        """
    def get_min_torsional_patch_radius(self) -> float:
        """
        Get the minimum radius of the contact patch used to apply torsional friction
        
                Search for *"Torsional Patch Radius"* in |physx_docs| for more details
        
                Returns:
                    float: minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.get_min_torsional_patch_radius()
                    0.0
                
        """
    def get_net_contact_forces(self, dt: float = 1.0) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                If contact forces of the prims in the view are tracked, this method returns the net contact forces on prims.
                i.e., a matrix of dimension (1, 3)
        
                Args:
                    dt (float): time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: Net contact forces of the prims with shape (3).
                
        """
    def get_rest_offset(self) -> float:
        """
        Get the rest offset
        
                Two shapes will come to rest at a distance equal to the sum of their rest offset values.
                If the rest offset is 0, they should converge to touching exactly
        
                Search for *Advanced Collision Detection* in |physx_docs| for more details
        
                Returns:
                    float: rest offset of the collision shape.
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.get_rest_offset()
                    -inf
                
        """
    def get_torsional_patch_radius(self) -> float:
        """
        Get the radius of the contact patch used to apply torsional friction
        
                Search for *"Torsional Patch Radius"* in |physx_docs| for more details
        
                Returns:
                    float: radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.get_torsional_patch_radius()
                    0.0
                
        """
    def set_collision_approximation(self, approximation_type: str) -> None:
        """
        Set the collision approximation
        
                .. list-table::
                    :header-rows: 1
        
                    * - Approximation
                      - Full name
                      - Description
                    * - ``"none"``
                      - Triangle Mesh
                      - The mesh geometry is used directly as a collider without any approximation
                    * - ``"convexDecomposition"``
                      - Convex Decomposition
                      - A convex mesh decomposition is performed. This results in a set of convex mesh colliders
                    * - ``"convexHull"``
                      - Convex Hull
                      - A convex hull of the mesh is generated and used as the collider
                    * - ``"boundingSphere"``
                      - Bounding Sphere
                      - A bounding sphere is computed around the mesh and used as a collider
                    * - ``"boundingCube"``
                      - Bounding Cube
                      - An optimally fitting box collider is computed around the mesh
                    * - ``"meshSimplification"``
                      - Mesh Simplification
                      - A mesh simplification step is performed, resulting in a simplified triangle mesh collider
                    * - ``"sdf"``
                      - SDF Mesh
                      - SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
                    * - ``"sphereFill"``
                      - Sphere Approximation
                      - A sphere mesh decomposition is performed. This results in a set of sphere colliders
        
                .. note ::
        
                    Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
        
                .. warning::
        
                    Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance
                    impact due to higher computational cost
        
                Args:
                    approximation_type (str): approximation used for collision
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.set_collision_approximation("convexDecomposition")
                
        """
    def set_collision_enabled(self, enabled: bool) -> None:
        """
        Enable/disable the Collision API
        
                Args:
                    enabled (bool): Whether to enable or disable the Collision API
        
                Example:
        
                .. code-block:: python
        
                    >>> # disable collisions
                    >>> prim.set_collision_enabled(False)
                
        """
    def set_contact_offset(self, offset: float) -> None:
        """
        Set the contact offset
        
                Shapes whose distance is less than the sum of their contact offset values will generate contacts
        
                Search for *Advanced Collision Detection* in |physx_docs| for more details
        
                .. warning::
        
                    The contact offset must be positive and greater than the rest offset
        
                Args:
                    offset (float): Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0].
                                    Default value is -inf, means default is picked by simulation based on the shape extent.
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.set_contact_offset(0.02)
                
        """
    def set_min_torsional_patch_radius(self, radius: float) -> None:
        """
        Set the minimum radius of the contact patch used to apply torsional friction
        
                Search for *"Torsional Patch Radius"* in |physx_docs| for more details
        
                Args:
                    radius (float): minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.set_min_torsional_patch_radius(0.05)
                
        """
    def set_rest_offset(self, offset: float) -> None:
        """
        Set the rest offset
        
                Two shapes will come to rest at a distance equal to the sum of their rest offset values.
                If the rest offset is 0, they should converge to touching exactly
        
                Search for *Advanced Collision Detection* in |physx_docs| for more details
        
                .. warning::
        
                    The contact offset must be positive and greater than the rest offset
        
                Args:
                    offset (float): Rest offset of a collision shape. Allowed range [-max_float, contact_offset.
                                    Default value is -inf, means default is picked by simulation. For rigid bodies its zero.
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.set_rest_offset(0.01)
                
        """
    def set_torsional_patch_radius(self, radius: float) -> None:
        """
        Set the radius of the contact patch used to apply torsional friction
        
                Search for *"Torsional Patch Radius"* in |physx_docs| for more details
        
                Args:
                    radius (float): radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.set_torsional_patch_radius(0.1)
                
        """
    @property
    def geom(self) -> pxr.UsdGeom.Gprim:
        """
        
                Returns:
                    UsdGeom.Gprim: USD geometry object encapsulated.
                
        """
