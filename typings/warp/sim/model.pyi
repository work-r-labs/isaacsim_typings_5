"""
A module for building simulation models and state.
"""
from __future__ import annotations
import copy as copy
import math as math
import numpy as np
import typing
import warp as wp
import warp.codegen
from warp.sim.graph_coloring import ColoringAlgorithm
from warp.sim.graph_coloring import color_trimesh
from warp.sim.graph_coloring import combine_independent_particle_coloring
from warp.sim.inertia import compute_box_inertia
from warp.sim.inertia import compute_capsule_inertia
from warp.sim.inertia import compute_cone_inertia
from warp.sim.inertia import compute_cylinder_inertia
from warp.sim.inertia import compute_mesh_inertia
from warp.sim.inertia import compute_sphere_inertia
from warp.sim.inertia import transform_inertia
import warp.types
__all__: list[str] = ['ColoringAlgorithm', 'Control', 'GEO_BOX', 'GEO_CAPSULE', 'GEO_CONE', 'GEO_CYLINDER', 'GEO_MESH', 'GEO_NONE', 'GEO_PLANE', 'GEO_SDF', 'GEO_SPHERE', 'JOINT_BALL', 'JOINT_COMPOUND', 'JOINT_D6', 'JOINT_DISTANCE', 'JOINT_FIXED', 'JOINT_FREE', 'JOINT_MODE_FORCE', 'JOINT_MODE_TARGET_POSITION', 'JOINT_MODE_TARGET_VELOCITY', 'JOINT_PRISMATIC', 'JOINT_REVOLUTE', 'JOINT_UNIVERSAL', 'JointAxis', 'Mat33', 'Mesh', 'Model', 'ModelBuilder', 'ModelShapeGeometry', 'ModelShapeMaterials', 'PARTICLE_FLAG_ACTIVE', 'Quat', 'SDF', 'State', 'Transform', 'Vec3', 'Vec4', 'color_trimesh', 'combine_independent_particle_coloring', 'compute_box_inertia', 'compute_capsule_inertia', 'compute_cone_inertia', 'compute_cylinder_inertia', 'compute_mesh_inertia', 'compute_shape_mass', 'compute_sphere_inertia', 'copy', 'flag_to_int', 'math', 'np', 'transform_inertia', 'wp']
class Control:
    """
    Time-varying control data for a :class:`Model`.
    
        Time-varying control data includes joint control inputs, muscle activations,
        and activation forces for triangle and tetrahedral elements.
    
        The exact attributes depend on the contents of the model. Control objects
        should generally be created using the :func:`Model.control()` function.
        
    """
    def __init__(self, model: Model = None):
        ...
    def clear(self) -> None:
        """
        Reset the control inputs to zero.
        """
    def reset(self) -> None:
        """
        Reset the control inputs to zero.
        """
class JointAxis:
    """
    
        Describes a joint axis that can have limits and be driven towards a target.
    
        Attributes:
    
            axis (3D vector or JointAxis): The 3D axis that this JointAxis object describes, or alternatively another JointAxis object to copy from
            limit_lower (float): The lower position limit of the joint axis
            limit_upper (float): The upper position limit of the joint axis
            limit_ke (float): The elastic stiffness of the joint axis limits, only respected by :class:`SemiImplicitIntegrator` and :class:`FeatherstoneIntegrator`
            limit_kd (float): The damping stiffness of the joint axis limits, only respected by :class:`SemiImplicitIntegrator` and :class:`FeatherstoneIntegrator`
            action (float): The force applied by default to this joint axis, or the target position or velocity (depending on the mode, see `Joint modes`_) of the joint axis
            target_ke (float): The proportional gain of the joint axis target drive PD controller
            target_kd (float): The derivative gain of the joint axis target drive PD controller
            mode (int): The mode of the joint axis, see `Joint modes`_
        
    """
    def __init__(self, axis, limit_lower = ..., limit_upper = ..., limit_ke = 100.0, limit_kd = 10.0, action = None, target_ke = 0.0, target_kd = 0.0, mode = 0):
        ...
class Mesh:
    """
    Describes a triangle collision mesh for simulation
    
        Example mesh creation from a triangle OBJ mesh file:
        ====================================================
    
        See :func:`load_mesh` which is provided as a utility function.
    
        .. code-block:: python
    
            import numpy as np
            import warp as wp
            import warp.sim
            import openmesh
    
            m = openmesh.read_trimesh("mesh.obj")
            mesh_points = np.array(m.points())
            mesh_indices = np.array(m.face_vertex_indices(), dtype=np.int32).flatten()
            mesh = wp.sim.Mesh(mesh_points, mesh_indices)
    
        Attributes:
    
            vertices (List[Vec3]): Mesh 3D vertices points
            indices (List[int]): Mesh indices as a flattened list of vertex indices describing triangles
            I (Mat33): 3x3 inertia matrix of the mesh assuming density of 1.0 (around the center of mass)
            mass (float): The total mass of the body assuming density of 1.0
            com (Vec3): The center of mass of the body
        
    """
    def __hash__(self):
        """
        
                Computes a hash of the mesh data for use in caching. The hash considers the mesh vertices, indices, and whether the mesh is solid or not.
                
        """
    def __init__(self, vertices: list[Vec3], indices: list[int], compute_inertia = True, is_solid = True):
        """
        Construct a Mesh object from a triangle mesh
        
                The mesh center of mass and inertia tensor will automatically be
                calculated using a density of 1.0. This computation is only valid
                if the mesh is closed (two-manifold).
        
                Args:
                    vertices: List of vertices in the mesh
                    indices: List of triangle indices, 3 per-element
                    compute_inertia: If True, the mass, inertia tensor and center of mass will be computed assuming density of 1.0
                    is_solid: If True, the mesh is assumed to be a solid during inertia computation, otherwise it is assumed to be a hollow surface
                
        """
    def finalize(self, device = None):
        """
        
                Constructs a simulation-ready :class:`Mesh` object from the mesh data and returns its ID.
        
                Args:
                    device: The device on which to allocate the mesh buffers
        
                Returns:
                    The ID of the simulation-ready :class:`Mesh`
                
        """
class Model:
    """
    Holds the definition of the simulation model
    
        This class holds the non-time varying description of the system, i.e.:
        all geometry, constraints, and parameters used to describe the simulation.
    
        Attributes:
            requires_grad (float): Indicates whether the model was finalized (see :meth:`ModelBuilder.finalize`) with gradient computation enabled
            num_envs (int): Number of articulation environments that were added to the ModelBuilder via `add_builder`
    
            particle_q (array): Particle positions, shape [particle_count, 3], float
            particle_qd (array): Particle velocities, shape [particle_count, 3], float
            particle_mass (array): Particle mass, shape [particle_count], float
            particle_inv_mass (array): Particle inverse mass, shape [particle_count], float
            particle_radius (array): Particle radius, shape [particle_count], float
            particle_max_radius (float): Maximum particle radius (useful for HashGrid construction)
            particle_ke (array): Particle normal contact stiffness (used by :class:`SemiImplicitIntegrator`), shape [particle_count], float
            particle_kd (array): Particle normal contact damping (used by :class:`SemiImplicitIntegrator`), shape [particle_count], float
            particle_kf (array): Particle friction force stiffness (used by :class:`SemiImplicitIntegrator`), shape [particle_count], float
            particle_mu (array): Particle friction coefficient, shape [particle_count], float
            particle_cohesion (array): Particle cohesion strength, shape [particle_count], float
            particle_adhesion (array): Particle adhesion strength, shape [particle_count], float
            particle_grid (HashGrid): HashGrid instance used for accelerated simulation of particle interactions
            particle_flags (array): Particle enabled state, shape [particle_count], bool
            particle_max_velocity (float): Maximum particle velocity (to prevent instability)
    
            shape_transform (array): Rigid shape transforms, shape [shape_count, 7], float
            shape_visible (array): Rigid shape visibility, shape [shape_count], bool
            shape_body (array): Rigid shape body index, shape [shape_count], int
            body_shapes (dict): Mapping from body index to list of attached shape indices
            shape_materials (ModelShapeMaterials): Rigid shape contact materials, shape [shape_count], float
            shape_shape_geo (ModelShapeGeometry): Shape geometry properties (geo type, scale, thickness, etc.), shape [shape_count, 3], float
            shape_geo_src (list): List of `wp.Mesh` instances used for rendering of mesh geometry
    
            shape_collision_group (list): Collision group of each shape, shape [shape_count], int
            shape_collision_group_map (dict): Mapping from collision group to list of shape indices
            shape_collision_filter_pairs (set): Pairs of shape indices that should not collide
            shape_collision_radius (array): Collision radius of each shape used for bounding sphere broadphase collision checking, shape [shape_count], float
            shape_ground_collision (list): Indicates whether each shape should collide with the ground, shape [shape_count], bool
            shape_shape_collision (list): Indicates whether each shape should collide with any other shape, shape [shape_count], bool
            shape_contact_pairs (array): Pairs of shape indices that may collide, shape [contact_pair_count, 2], int
            shape_ground_contact_pairs (array): Pairs of shape, ground indices that may collide, shape [ground_contact_pair_count, 2], int
    
            spring_indices (array): Particle spring indices, shape [spring_count*2], int
            spring_rest_length (array): Particle spring rest length, shape [spring_count], float
            spring_stiffness (array): Particle spring stiffness, shape [spring_count], float
            spring_damping (array): Particle spring damping, shape [spring_count], float
            spring_control (array): Particle spring activation, shape [spring_count], float
    
            tri_indices (array): Triangle element indices, shape [tri_count*3], int
            tri_poses (array): Triangle element rest pose, shape [tri_count, 2, 2], float
            tri_activations (array): Triangle element activations, shape [tri_count], float
            tri_materials (array): Triangle element materials, shape [tri_count, 5], float
            tri_areas (array): Triangle element rest areas, shape [tri_count], float
    
            edge_indices (array): Bending edge indices, shape [edge_count*4], int, each row is [o0, o1, v1, v2], where v1, v2 are on the edge
            edge_rest_angle (array): Bending edge rest angle, shape [edge_count], float
            edge_rest_length (array): Bending edge rest length, shape [edge_count], float
            edge_bending_properties (array): Bending edge stiffness and damping parameters, shape [edge_count, 2], float
    
            tet_indices (array): Tetrahedral element indices, shape [tet_count*4], int
            tet_poses (array): Tetrahedral rest poses, shape [tet_count, 3, 3], float
            tet_activations (array): Tetrahedral volumetric activations, shape [tet_count], float
            tet_materials (array): Tetrahedral elastic parameters in form :math:`k_{mu}, k_{lambda}, k_{damp}`, shape [tet_count, 3]
    
            muscle_start (array): Start index of the first muscle point per muscle, shape [muscle_count], int
            muscle_params (array): Muscle parameters, shape [muscle_count, 5], float
            muscle_bodies (array): Body indices of the muscle waypoints, int
            muscle_points (array): Local body offset of the muscle waypoints, float
            muscle_activations (array): Muscle activations, shape [muscle_count], float
    
            body_q (array): Poses of rigid bodies used for state initialization, shape [body_count, 7], float
            body_qd (array): Velocities of rigid bodies used for state initialization, shape [body_count, 6], float
            body_com (array): Rigid body center of mass (in local frame), shape [body_count, 7], float
            body_inertia (array): Rigid body inertia tensor (relative to COM), shape [body_count, 3, 3], float
            body_inv_inertia (array): Rigid body inverse inertia tensor (relative to COM), shape [body_count, 3, 3], float
            body_mass (array): Rigid body mass, shape [body_count], float
            body_inv_mass (array): Rigid body inverse mass, shape [body_count], float
            body_name (list): Rigid body names, shape [body_count], str
    
            joint_q (array): Generalized joint positions used for state initialization, shape [joint_coord_count], float
            joint_qd (array): Generalized joint velocities used for state initialization, shape [joint_dof_count], float
            joint_act (array): Generalized joint control inputs, shape [joint_axis_count], float
            joint_type (array): Joint type, shape [joint_count], int
            joint_parent (array): Joint parent body indices, shape [joint_count], int
            joint_child (array): Joint child body indices, shape [joint_count], int
            joint_ancestor (array): Maps from joint index to the index of the joint that has the current joint parent body as child (-1 if no such joint ancestor exists), shape [joint_count], int
            joint_X_p (array): Joint transform in parent frame, shape [joint_count, 7], float
            joint_X_c (array): Joint mass frame in child frame, shape [joint_count, 7], float
            joint_axis (array): Joint axis in child frame, shape [joint_axis_count, 3], float
            joint_armature (array): Armature for each joint axis (only used by :class:`FeatherstoneIntegrator`), shape [joint_dof_count], float
            joint_target_ke (array): Joint stiffness, shape [joint_axis_count], float
            joint_target_kd (array): Joint damping, shape [joint_axis_count], float
            joint_axis_start (array): Start index of the first axis per joint, shape [joint_count], int
            joint_axis_dim (array): Number of linear and angular axes per joint, shape [joint_count, 2], int
            joint_axis_mode (array): Joint axis mode, shape [joint_axis_count], int. See `Joint modes`_.
            joint_linear_compliance (array): Joint linear compliance, shape [joint_count], float
            joint_angular_compliance (array): Joint linear compliance, shape [joint_count], float
            joint_enabled (array): Controls which joint is simulated (bodies become disconnected if False), shape [joint_count], int
    
                Note:
    
                   This setting is not supported by :class:`FeatherstoneIntegrator`.
    
            joint_limit_lower (array): Joint lower position limits, shape [joint_axis_count], float
            joint_limit_upper (array): Joint upper position limits, shape [joint_axis_count], float
            joint_limit_ke (array): Joint position limit stiffness (used by the Euler integrators), shape [joint_axis_count], float
            joint_limit_kd (array): Joint position limit damping (used by the Euler integrators), shape [joint_axis_count], float
            joint_twist_lower (array): Joint lower twist limit, shape [joint_count], float
            joint_twist_upper (array): Joint upper twist limit, shape [joint_count], float
            joint_q_start (array): Start index of the first position coordinate per joint (note the last value is an additional sentinel entry to allow for querying the q dimensionality of joint i via ``joint_q_start[i+1] - joint_q_start[i]``), shape [joint_count + 1], int
            joint_qd_start (array): Start index of the first velocity coordinate per joint (note the last value is an additional sentinel entry to allow for querying the qd dimensionality of joint i via ``joint_qd_start[i+1] - joint_qd_start[i]``), shape [joint_count + 1], int
            articulation_start (array): Articulation start index, shape [articulation_count], int
            joint_name (list): Joint names, shape [joint_count], str
            joint_attach_ke (float): Joint attachment force stiffness (used by :class:`SemiImplicitIntegrator`)
            joint_attach_kd (float): Joint attachment force damping (used by :class:`SemiImplicitIntegrator`)
    
            soft_contact_radius (float): Contact radius used for self-collisions in the VBD integrator.
            soft_contact_margin (float): Contact margin for generation of soft contacts
            soft_contact_ke (float): Stiffness of soft contacts (used by the Euler integrators)
            soft_contact_kd (float): Damping of soft contacts (used by the Euler integrators)
            soft_contact_kf (float): Stiffness of friction force in soft contacts (used by the Euler integrators)
            soft_contact_mu (float): Friction coefficient of soft contacts
            soft_contact_restitution (float): Restitution coefficient of soft contacts (used by :class:`XPBDIntegrator`)
    
            soft_contact_count (array): Number of active particle-shape contacts, shape [1], int
            soft_contact_particle (array), Index of particle per soft contact point, shape [soft_contact_max], int
            soft_contact_shape (array), Index of shape per soft contact point, shape [soft_contact_max], int
            soft_contact_body_pos (array), Positional offset of soft contact point in body frame, shape [soft_contact_max], vec3
            soft_contact_body_vel (array), Linear velocity of soft contact point in body frame, shape [soft_contact_max], vec3
            soft_contact_normal (array), Contact surface normal of soft contact point in world space, shape [soft_contact_max], vec3
            soft_contact_tids (array), Thread indices of the soft contact points, shape [soft_contact_max], int
    
            rigid_contact_max (int): Maximum number of potential rigid body contact points to generate ignoring the `rigid_mesh_contact_max` limit.
            rigid_contact_max_limited (int): Maximum number of potential rigid body contact points to generate respecting the `rigid_mesh_contact_max` limit.
            rigid_mesh_contact_max (int): Maximum number of rigid body contact points to generate per mesh (0 = unlimited, default)
            rigid_contact_margin (float): Contact margin for generation of rigid body contacts
            rigid_contact_torsional_friction (float): Torsional friction coefficient for rigid body contacts (used by :class:`XPBDIntegrator`)
            rigid_contact_rolling_friction (float): Rolling friction coefficient for rigid body contacts (used by :class:`XPBDIntegrator`)
    
            rigid_contact_count (array): Number of active shape-shape contacts, shape [1], int
            rigid_contact_point0 (array): Contact point relative to frame of body 0, shape [rigid_contact_max], vec3
            rigid_contact_point1 (array): Contact point relative to frame of body 1, shape [rigid_contact_max], vec3
            rigid_contact_offset0 (array): Contact offset due to contact thickness relative to body 0, shape [rigid_contact_max], vec3
            rigid_contact_offset1 (array): Contact offset due to contact thickness relative to body 1, shape [rigid_contact_max], vec3
            rigid_contact_normal (array): Contact normal in world space, shape [rigid_contact_max], vec3
            rigid_contact_thickness (array): Total contact thickness, shape [rigid_contact_max], float
            rigid_contact_shape0 (array): Index of shape 0 per contact, shape [rigid_contact_max], int
            rigid_contact_shape1 (array): Index of shape 1 per contact, shape [rigid_contact_max], int
            rigid_contact_tids (array): Triangle indices of the contact points, shape [rigid_contact_max], int
            rigid_contact_pairwise_counter (array): Pairwise counter for contact generation, shape [rigid_contact_max], int
            rigid_contact_broad_shape0 (array): Broadphase shape index of shape 0 per contact, shape [rigid_contact_max], int
            rigid_contact_broad_shape1 (array): Broadphase shape index of shape 1 per contact, shape [rigid_contact_max], int
            rigid_contact_point_id (array): Contact point ID, shape [rigid_contact_max], int
            rigid_contact_point_limit (array): Contact point limit, shape [rigid_contact_max], int
    
            ground (bool): Whether the ground plane and ground contacts are enabled
            ground_plane (array): Ground plane 3D normal and offset, shape [4], float
            up_vector (np.ndarray): Up vector of the world, shape [3], float
            up_axis (int): Up axis, 0 for x, 1 for y, 2 for z
            gravity (np.ndarray): Gravity vector, shape [3], float
    
            particle_count (int): Total number of particles in the system
            body_count (int): Total number of bodies in the system
            shape_count (int): Total number of shapes in the system
            joint_count (int): Total number of joints in the system
            tri_count (int): Total number of triangles in the system
            tet_count (int): Total number of tetrahedra in the system
            edge_count (int): Total number of edges in the system
            spring_count (int): Total number of springs in the system
            contact_count (int): Total number of contacts in the system
            muscle_count (int): Total number of muscles in the system
            articulation_count (int): Total number of articulations in the system
            joint_dof_count (int): Total number of velocity degrees of freedom of all joints in the system
            joint_coord_count (int): Total number of position degrees of freedom of all joints in the system
    
            particle_coloring (list of array): The coloring of all the particles, used for VBD's Gauss-Seidel iteration.
    
            device (wp.Device): Device on which the Model was allocated
    
        Note:
            It is strongly recommended to use the ModelBuilder to construct a simulation rather
            than creating your own Model object directly, however it is possible to do so if
            desired.
        
    """
    def __init__(self, device = None):
        ...
    def _allocate_soft_contacts(self, target, count, requires_grad = False):
        ...
    def allocate_rigid_contacts(self, target = None, count = None, limited_contact_count = None, requires_grad = False):
        ...
    def allocate_soft_contacts(self, count, requires_grad = False):
        ...
    def control(self, requires_grad = None, clone_variables = True) -> Control:
        """
        
                Returns a control object for the model.
        
                The returned control object will be initialized with the control inputs given in the model description.
        
                Args:
                    requires_grad (bool): Manual overwrite whether the control variables should have `requires_grad` enabled (defaults to `None` to use the model's setting :attr:`requires_grad`)
                    clone_variables (bool): Whether to clone the control inputs or use the original data
        
                Returns:
                    Control: The control object
                
        """
    def count_contact_points(self):
        """
        
                Counts the maximum number of rigid contact points that need to be allocated.
                This function returns two values corresponding to the maximum number of potential contacts
                excluding the limiting from `Model.rigid_mesh_contact_max` and the maximum number of
                contact points that may be generated when considering the `Model.rigid_mesh_contact_max` limit.
        
                :returns:
                    - potential_count (int): Potential number of contact points
                    - actual_count (int): Actual number of contact points
                
        """
    def find_shape_contact_pairs(self):
        ...
    def state(self, requires_grad = None) -> State:
        """
        Returns a state object for the model
        
                The returned state will be initialized with the initial configuration given in
                the model description.
        
                Args:
                    requires_grad (bool): Manual overwrite whether the state variables should have `requires_grad` enabled (defaults to `None` to use the model's setting :attr:`requires_grad`)
        
                Returns:
                    State: The state object
                
        """
    @property
    def soft_contact_max(self):
        """
        Maximum number of soft contacts that can be registered
        """
class ModelBuilder:
    """
    A helper class for building simulation models at runtime.
    
        Use the ModelBuilder to construct a simulation scene. The ModelBuilder
        and builds the scene representation using standard Python data structures (lists),
        this means it is not differentiable. Once :func:`finalize()`
        has been called the ModelBuilder transfers all data to Warp tensors and returns
        an object that may be used for simulation.
    
        Example
        -------
    
        .. code-block:: python
    
            import warp as wp
            import warp.sim
    
            builder = wp.sim.ModelBuilder()
    
            # anchor point (zero mass)
            builder.add_particle((0, 1.0, 0.0), (0.0, 0.0, 0.0), 0.0)
    
            # build chain
            for i in range(1, 10):
                builder.add_particle((i, 1.0, 0.0), (0.0, 0.0, 0.0), 1.0)
                builder.add_spring(i - 1, i, 1.0e3, 0.0, 0)
    
            # create model
            model = builder.finalize("cuda")
    
            state = model.state()
            control = model.control()  # optional, to support time-varying control inputs
            integrator = wp.sim.SemiImplicitIntegrator()
    
            for i in range(100):
                state.clear_forces()
                integrator.simulate(model, state, state, dt=1.0 / 60.0, control=control)
    
        Note:
            It is strongly recommended to use the ModelBuilder to construct a simulation rather
            than creating your own Model object directly, however it is possible to do so if
            desired.
        
    """
    default_edge_kd: typing.ClassVar[float] = 0.0
    default_edge_ke: typing.ClassVar[float] = 100.0
    default_joint_limit_kd: typing.ClassVar[float] = 1.0
    default_joint_limit_ke: typing.ClassVar[float] = 100.0
    default_particle_radius: typing.ClassVar[float] = 0.1
    default_shape_density: typing.ClassVar[float] = 1000.0
    default_shape_ka: typing.ClassVar[float] = 0.0
    default_shape_kd: typing.ClassVar[float] = 1000.0
    default_shape_ke: typing.ClassVar[float] = 100000.0
    default_shape_kf: typing.ClassVar[float] = 1000.0
    default_shape_mu: typing.ClassVar[float] = 0.5
    default_shape_restitution: typing.ClassVar[float] = 0.0
    default_shape_thickness: typing.ClassVar[float] = 1e-05
    default_spring_kd: typing.ClassVar[float] = 0.0
    default_spring_ke: typing.ClassVar[float] = 100.0
    default_tri_drag: typing.ClassVar[float] = 0.0
    default_tri_ka: typing.ClassVar[float] = 100.0
    default_tri_kd: typing.ClassVar[float] = 10.0
    default_tri_ke: typing.ClassVar[float] = 100.0
    default_tri_lift: typing.ClassVar[float] = 0.0
    def __init__(self, up_vector = (0.0, 1.0, 0.0), gravity = -9.80665):
        ...
    def _add_shape(self, body, pos, rot, type, scale, src = None, density = None, ke = None, kd = None, kf = None, ka = None, mu = None, restitution = None, thickness = None, is_solid = True, collision_group = -1, collision_filter_parent = True, has_ground_collision = True, has_shape_collision = True, is_visible = True):
        ...
    def _create_ground_plane(self):
        ...
    def _shape_radius(self, type, scale, src):
        """
        
                Calculates the radius of a sphere that encloses the shape, used for broadphase collision detection.
                
        """
    def _update_body_mass(self, i, m, I, p, q):
        ...
    def add_articulation(self):
        ...
    def add_body(self, origin: Transform | None = None, armature: float = 0.0, com: Vec3 | None = None, I_m: Mat33 | None = None, m: float = 0.0, name: str = None) -> int:
        """
        Adds a rigid body to the model.
        
                Args:
                    origin: The location of the body in the world frame
                    armature: Artificial inertia added to the body
                    com: The center of mass of the body w.r.t its origin
                    I_m: The 3x3 inertia tensor of the body (specified relative to the center of mass)
                    m: Mass of the body
                    name: Name of the body (optional)
        
                Returns:
                    The index of the body in the model
        
                Note:
                    If the mass (m) is zero then the body is treated as kinematic with no dynamics
        
                
        """
    def add_builder(self, builder, xform = None, update_num_env_count = True, separate_collision_group = True):
        """
        Copies the data from `builder`, another `ModelBuilder` to this `ModelBuilder`.
        
                Args:
                    builder (ModelBuilder): a model builder to add model data from.
                    xform (:ref:`transform <transform>`): offset transform applied to root bodies.
                    update_num_env_count (bool): if True, the number of environments is incremented by 1.
                    separate_collision_group (bool): if True, the shapes from the articulations in `builder` will all be put into a single new collision group, otherwise, only the shapes in collision group > -1 will be moved to a new group.
                
        """
    def add_cloth_grid(self, pos: Vec3, rot: Quat, vel: Vec3, dim_x: int, dim_y: int, cell_x: float, cell_y: float, mass: float, reverse_winding: bool = False, fix_left: bool = False, fix_right: bool = False, fix_top: bool = False, fix_bottom: bool = False, tri_ke: float = None, tri_ka: float = None, tri_kd: float = None, tri_drag: float = None, tri_lift: float = None, edge_ke: float = None, edge_kd: float = None, add_springs: bool = False, spring_ke: float = None, spring_kd: float = None, particle_radius: float = None):
        """
        Helper to create a regular planar cloth grid
        
                Creates a rectangular grid of particles with FEM triangles and bending elements
                automatically.
        
                Args:
                    pos: The position of the cloth in world space
                    rot: The orientation of the cloth in world space
                    vel: The velocity of the cloth in world space
                    dim_x_: The number of rectangular cells along the x-axis
                    dim_y: The number of rectangular cells along the y-axis
                    cell_x: The width of each cell in the x-direction
                    cell_y: The width of each cell in the y-direction
                    mass: The mass of each particle
                    reverse_winding: Flip the winding of the mesh
                    fix_left: Make the left-most edge of particles kinematic (fixed in place)
                    fix_right: Make the right-most edge of particles kinematic
                    fix_top: Make the top-most edge of particles kinematic
                    fix_bottom: Make the bottom-most edge of particles kinematic
                
        """
    def add_cloth_mesh(self, pos: Vec3, rot: Quat, scale: float, vel: Vec3, vertices: list[Vec3], indices: list[int], density: float, edge_callback = None, face_callback = None, tri_ke: float = None, tri_ka: float = None, tri_kd: float = None, tri_drag: float = None, tri_lift: float = None, edge_ke: float = None, edge_kd: float = None, add_springs: bool = False, spring_ke: float = None, spring_kd: float = None, particle_radius: float = None):
        """
        Helper to create a cloth model from a regular triangle mesh
        
                Creates one FEM triangle element and one bending element for every face
                and edge in the input triangle mesh
        
                Args:
                    pos: The position of the cloth in world space
                    rot: The orientation of the cloth in world space
                    vel: The velocity of the cloth in world space
                    vertices: A list of vertex positions
                    indices: A list of triangle indices, 3 entries per-face
                    density: The density per-area of the mesh
                    edge_callback: A user callback when an edge is created
                    face_callback: A user callback when a face is created
                    particle_radius: The particle_radius which controls particle based collisions.
                Note:
        
                    The mesh should be two manifold.
                
        """
    def add_edge(self, i: int, j: int, k: int, l: int, rest: float = None, edge_ke: float = None, edge_kd: float = None):
        """
        Adds a bending edge element between four particles in the system.
        
                Bending elements are designed to be between two connected triangles. Then
                bending energy is based of [Bridson et al. 2002]. Bending stiffness is controlled
                by the `model.tri_kb` parameter.
        
                Args:
                    i: The index of the first particle, i.e., opposite vertex 0
                    j: The index of the second particle, i.e., opposite vertex 1
                    k: The index of the third particle, i.e., vertex 0
                    l: The index of the fourth particle, i.e., vertex 1
                    rest: The rest angle across the edge in radians, if not specified it will be computed
        
                Note:
                    The edge lies between the particles indexed by 'k' and 'l' parameters with the opposing
                    vertices indexed by 'i' and 'j'. This defines two connected triangles with counter clockwise
                    winding: (i, k, l), (j, l, k).
        
                
        """
    def add_edges(self, i, j, k, l, rest: list[float] | None = None, edge_ke: list[float] | None = None, edge_kd: list[float] | None = None):
        """
        Adds bending edge elements between groups of four particles in the system.
        
                Bending elements are designed to be between two connected triangles. Then
                bending energy is based of [Bridson et al. 2002]. Bending stiffness is controlled
                by the `model.tri_kb` parameter.
        
                Args:
                    i: The index of the first particle, i.e., opposite vertex 0
                    j: The index of the second particle, i.e., opposite vertex 1
                    k: The index of the third particle, i.e., vertex 0
                    l: The index of the fourth particle, i.e., vertex 1
                    rest: The rest angles across the edges in radians, if not specified they will be computed
        
                Note:
                    The edge lies between the particles indexed by 'k' and 'l' parameters with the opposing
                    vertices indexed by 'i' and 'j'. This defines two connected triangles with counter clockwise
                    winding: (i, k, l), (j, l, k).
        
                
        """
    def add_joint(self, joint_type: wp.constant, parent: int, child: int, linear_axes: list[JointAxis] | None = None, angular_axes: list[JointAxis] | None = None, name: str = None, parent_xform: wp.transform | None = None, child_xform: wp.transform | None = None, linear_compliance: float = 0.0, angular_compliance: float = 0.0, armature: float = 0.01, collision_filter_parent: bool = True, enabled: bool = True) -> int:
        """
        
                Generic method to add any type of joint to this ModelBuilder.
        
                Args:
                    joint_type (constant): The type of joint to add (see `Joint types`_)
                    parent (int): The index of the parent body (-1 is the world)
                    child (int): The index of the child body
                    linear_axes (list(:class:`JointAxis`)): The linear axes (see :class:`JointAxis`) of the joint
                    angular_axes (list(:class:`JointAxis`)): The angular axes (see :class:`JointAxis`) of the joint
                    name (str): The name of the joint (optional)
                    parent_xform (:ref:`transform <transform>`): The transform of the joint in the parent body's local frame
                    child_xform (:ref:`transform <transform>`): The transform of the joint in the child body's local frame
                    linear_compliance (float): The linear compliance of the joint
                    angular_compliance (float): The angular compliance of the joint
                    armature (float): Artificial inertia added around the joint axes (only considered by :class:`FeatherstoneIntegrator`)
                    collision_filter_parent (bool): Whether to filter collisions between shapes of the parent and child bodies
                    enabled (bool): Whether the joint is enabled (not considered by :class:`FeatherstoneIntegrator`)
        
                Returns:
                    The index of the added joint
                
        """
    def add_joint_ball(self, parent: int, child: int, parent_xform: wp.transform | None = None, child_xform: wp.transform | None = None, linear_compliance: float = 0.0, angular_compliance: float = 0.0, armature: float = 0.01, name: str = None, collision_filter_parent: bool = True, enabled: bool = True) -> int:
        """
        Adds a ball (spherical) joint to the model. Its position is defined by a 4D quaternion (xyzw) and its velocity is a 3D vector.
        
                Args:
                    parent: The index of the parent body
                    child: The index of the child body
                    parent_xform (:ref:`transform <transform>`): The transform of the joint in the parent body's local frame
                    child_xform (:ref:`transform <transform>`): The transform of the joint in the child body's local frame
                    linear_compliance: The linear compliance of the joint
                    angular_compliance: The angular compliance of the joint
                    armature (float): Artificial inertia added around the joint axis (only considered by FeatherstoneIntegrator)
                    name: The name of the joint
                    collision_filter_parent: Whether to filter collisions between shapes of the parent and child bodies
                    enabled: Whether the joint is enabled
        
                Returns:
                    The index of the added joint
        
                
        """
    def add_joint_compound(self, parent: int, child: int, axis_0: JointAxis, axis_1: JointAxis, axis_2: JointAxis, parent_xform: wp.transform | None = None, child_xform: wp.transform | None = None, linear_compliance: float = 0.0, angular_compliance: float = 0.0, armature: float = 0.01, name: str = None, collision_filter_parent: bool = True, enabled: bool = True) -> int:
        """
        Adds a compound joint to the model, which has 3 degrees of freedom, one for each axis.
                Similar to the ball joint (see :meth:`add_ball_joint`), the compound joint allows bodies to move in a 3D rotation relative to each other,
                except that the rotation is defined by 3 axes instead of a quaternion.
                Depending on the choice of axes, the orientation can be specified through Euler angles, e.g. `z-x-z` or `x-y-x`, or through a Tait-Bryan angle sequence, e.g. `z-y-x` or `x-y-z`.
        
                Args:
                    parent: The index of the parent body
                    child: The index of the child body
                    axis_0 (3D vector or JointAxis): The first axis of the joint, can be a JointAxis object whose settings will be used instead of the other arguments
                    axis_1 (3D vector or JointAxis): The second axis of the joint, can be a JointAxis object whose settings will be used instead of the other arguments
                    axis_2 (3D vector or JointAxis): The third axis of the joint, can be a JointAxis object whose settings will be used instead of the other arguments
                    parent_xform (:ref:`transform <transform>`): The transform of the joint in the parent body's local frame
                    child_xform (:ref:`transform <transform>`): The transform of the joint in the child body's local frame
                    linear_compliance: The linear compliance of the joint
                    angular_compliance: The angular compliance of the joint
                    armature: Artificial inertia added around the joint axes
                    name: The name of the joint
                    collision_filter_parent: Whether to filter collisions between shapes of the parent and child bodies
                    enabled: Whether the joint is enabled
        
                Returns:
                    The index of the added joint
        
                
        """
    def add_joint_d6(self, parent: int, child: int, linear_axes: list[JointAxis] | None = None, angular_axes: list[JointAxis] | None = None, name: str = None, parent_xform: wp.transform | None = None, child_xform: wp.transform | None = None, linear_compliance: float = 0.0, angular_compliance: float = 0.0, armature: float = 0.01, collision_filter_parent: bool = True, enabled: bool = True):
        """
        Adds a generic joint with custom linear and angular axes. The number of axes determines the number of degrees of freedom of the joint.
        
                Args:
                    parent: The index of the parent body
                    child: The index of the child body
                    linear_axes: A list of linear axes
                    angular_axes: A list of angular axes
                    name: The name of the joint
                    parent_xform (:ref:`transform <transform>`): The transform of the joint in the parent body's local frame
                    child_xform (:ref:`transform <transform>`): The transform of the joint in the child body's local frame
                    linear_compliance: The linear compliance of the joint
                    angular_compliance: The angular compliance of the joint
                    armature: Artificial inertia added around the joint axes
                    collision_filter_parent: Whether to filter collisions between shapes of the parent and child bodies
                    enabled: Whether the joint is enabled
        
                Returns:
                    The index of the added joint
        
                
        """
    def add_joint_distance(self, parent: int, child: int, parent_xform: wp.transform | None = None, child_xform: wp.transform | None = None, min_distance: float = -1.0, max_distance: float = 1.0, compliance: float = 0.0, collision_filter_parent: bool = True, enabled: bool = True) -> int:
        """
        Adds a distance joint to the model. The distance joint constraints the distance between the joint anchor points on the two bodies (see :ref:`FK-IK`) it connects to the interval [`min_distance`, `max_distance`].
                It has 7 positional degrees of freedom (first 3 linear and then 4 angular dimensions for the orientation quaternion in `xyzw` notation) and 6 velocity degrees of freedom (first 3 angular and then 3 linear velocity dimensions).
        
                Args:
                    parent: The index of the parent body
                    child: The index of the child body
                    parent_xform (:ref:`transform <transform>`): The transform of the joint in the parent body's local frame
                    child_xform (:ref:`transform <transform>`): The transform of the joint in the child body's local frame
                    min_distance: The minimum distance between the bodies (no limit if negative)
                    max_distance: The maximum distance between the bodies (no limit if negative)
                    compliance: The compliance of the joint
                    collision_filter_parent: Whether to filter collisions between shapes of the parent and child bodies
                    enabled: Whether the joint is enabled
        
                Returns:
                    The index of the added joint
        
                .. note:: Distance joints are currently only supported in the :class:`XPBDIntegrator` at the moment.
        
                
        """
    def add_joint_fixed(self, parent: int, child: int, parent_xform: wp.transform | None = None, child_xform: wp.transform | None = None, linear_compliance: float = 0.0, angular_compliance: float = 0.0, armature: float = 0.01, name: str = None, collision_filter_parent: bool = True, enabled: bool = True) -> int:
        """
        Adds a fixed (static) joint to the model. It has no degrees of freedom.
                See :meth:`collapse_fixed_joints` for a helper function that removes these fixed joints and merges the connecting bodies to simplify the model and improve stability.
        
                Args:
                    parent: The index of the parent body
                    child: The index of the child body
                    parent_xform (:ref:`transform <transform>`): The transform of the joint in the parent body's local frame
                    child_xform (:ref:`transform <transform>`): The transform of the joint in the child body's local frame
                    linear_compliance: The linear compliance of the joint
                    angular_compliance: The angular compliance of the joint
                    armature (float): Artificial inertia added around the joint axis (only considered by FeatherstoneIntegrator)
                    name: The name of the joint
                    collision_filter_parent: Whether to filter collisions between shapes of the parent and child bodies
                    enabled: Whether the joint is enabled
        
                Returns:
                    The index of the added joint
        
                
        """
    def add_joint_free(self, child: int, parent_xform: wp.transform | None = None, child_xform: wp.transform | None = None, armature: float = 0.0, parent: int = -1, name: str = None, collision_filter_parent: bool = True, enabled: bool = True) -> int:
        """
        Adds a free joint to the model.
                It has 7 positional degrees of freedom (first 3 linear and then 4 angular dimensions for the orientation quaternion in `xyzw` notation) and 6 velocity degrees of freedom (first 3 angular and then 3 linear velocity dimensions).
        
                Args:
                    child: The index of the child body
                    parent_xform (:ref:`transform <transform>`): The transform of the joint in the parent body's local frame
                    child_xform (:ref:`transform <transform>`): The transform of the joint in the child body's local frame
                    armature (float): Artificial inertia added around the joint axis (only considered by FeatherstoneIntegrator)
                    parent: The index of the parent body (-1 by default to use the world frame, e.g. to make the child body and its children a floating-base mechanism)
                    name: The name of the joint
                    collision_filter_parent: Whether to filter collisions between shapes of the parent and child bodies
                    enabled: Whether the joint is enabled
        
                Returns:
                    The index of the added joint
        
                
        """
    def add_joint_prismatic(self, parent: int, child: int, parent_xform: wp.transform | None = None, child_xform: wp.transform | None = None, axis: Vec3 = (1.0, 0.0, 0.0), target: float = None, target_ke: float = 0.0, target_kd: float = 0.0, mode: int = 0, limit_lower: float = -10000.0, limit_upper: float = 10000.0, limit_ke: float = None, limit_kd: float = None, linear_compliance: float = 0.0, angular_compliance: float = 0.0, armature: float = 0.01, name: str = None, collision_filter_parent: bool = True, enabled: bool = True) -> int:
        """
        Adds a prismatic (sliding) joint to the model. It has one degree of freedom.
        
                Args:
                    parent: The index of the parent body
                    child: The index of the child body
                    parent_xform (:ref:`transform <transform>`): The transform of the joint in the parent body's local frame
                    child_xform (:ref:`transform <transform>`): The transform of the joint in the child body's local frame
                    axis (3D vector or JointAxis): The axis of rotation in the parent body's local frame, can be a JointAxis object whose settings will be used instead of the other arguments
                    target: The target position or velocity of the joint (if None, the joint is considered to be in force control mode)
                    target_ke: The stiffness of the joint target
                    target_kd: The damping of the joint target
                    limit_lower: The lower limit of the joint
                    limit_upper: The upper limit of the joint
                    limit_ke: The stiffness of the joint limit (None to use the default value :attr:`default_joint_limit_ke`)
                    limit_kd: The damping of the joint limit (None to use the default value :attr:`default_joint_limit_ke`)
                    linear_compliance: The linear compliance of the joint
                    angular_compliance: The angular compliance of the joint
                    armature: Artificial inertia added around the joint axis
                    name: The name of the joint
                    collision_filter_parent: Whether to filter collisions between shapes of the parent and child bodies
                    enabled: Whether the joint is enabled
        
                Returns:
                    The index of the added joint
        
                
        """
    def add_joint_revolute(self, parent: int, child: int, parent_xform: wp.transform | None = None, child_xform: wp.transform | None = None, axis: Vec3 = (1.0, 0.0, 0.0), target: float = None, target_ke: float = 0.0, target_kd: float = 0.0, mode: int = 0, limit_lower: float = -6.283185307179586, limit_upper: float = 6.283185307179586, limit_ke: float = None, limit_kd: float = None, linear_compliance: float = 0.0, angular_compliance: float = 0.0, armature: float = 0.01, name: str = None, collision_filter_parent: bool = True, enabled: bool = True) -> int:
        """
        Adds a revolute (hinge) joint to the model. It has one degree of freedom.
        
                Args:
                    parent: The index of the parent body
                    child: The index of the child body
                    parent_xform (:ref:`transform <transform>`): The transform of the joint in the parent body's local frame
                    child_xform (:ref:`transform <transform>`): The transform of the joint in the child body's local frame
                    axis (3D vector or JointAxis): The axis of rotation in the parent body's local frame, can be a JointAxis object whose settings will be used instead of the other arguments
                    target: The target angle (in radians) or target velocity of the joint (if None, the joint is considered to be in force control mode)
                    target_ke: The stiffness of the joint target
                    target_kd: The damping of the joint target
                    limit_lower: The lower limit of the joint
                    limit_upper: The upper limit of the joint
                    limit_ke: The stiffness of the joint limit (None to use the default value :attr:`default_joint_limit_ke`)
                    limit_kd: The damping of the joint limit (None to use the default value :attr:`default_joint_limit_kd`)
                    linear_compliance: The linear compliance of the joint
                    angular_compliance: The angular compliance of the joint
                    armature: Artificial inertia added around the joint axis
                    name: The name of the joint
                    collision_filter_parent: Whether to filter collisions between shapes of the parent and child bodies
                    enabled: Whether the joint is enabled
        
                Returns:
                    The index of the added joint
        
                
        """
    def add_joint_universal(self, parent: int, child: int, axis_0: JointAxis, axis_1: JointAxis, parent_xform: wp.transform | None = None, child_xform: wp.transform | None = None, linear_compliance: float = 0.0, angular_compliance: float = 0.0, armature: float = 0.01, name: str = None, collision_filter_parent: bool = True, enabled: bool = True) -> int:
        """
        Adds a universal joint to the model. U-joints have two degrees of freedom, one for each axis.
        
                Args:
                    parent: The index of the parent body
                    child: The index of the child body
                    axis_0 (3D vector or JointAxis): The first axis of the joint, can be a JointAxis object whose settings will be used instead of the other arguments
                    axis_1 (3D vector or JointAxis): The second axis of the joint, can be a JointAxis object whose settings will be used instead of the other arguments
                    parent_xform (:ref:`transform <transform>`): The transform of the joint in the parent body's local frame
                    child_xform (:ref:`transform <transform>`): The transform of the joint in the child body's local frame
                    linear_compliance: The linear compliance of the joint
                    angular_compliance: The angular compliance of the joint
                    armature: Artificial inertia added around the joint axes
                    name: The name of the joint
                    collision_filter_parent: Whether to filter collisions between shapes of the parent and child bodies
                    enabled: Whether the joint is enabled
        
                Returns:
                    The index of the added joint
        
                
        """
    def add_muscle(self, bodies: list[int], positions: list[Vec3], f0: float, lm: float, lt: float, lmax: float, pen: float) -> float:
        """
        Adds a muscle-tendon activation unit.
        
                Args:
                    bodies: A list of body indices for each waypoint
                    positions: A list of positions of each waypoint in the body's local frame
                    f0: Force scaling
                    lm: Muscle length
                    lt: Tendon length
                    lmax: Maximally efficient muscle length
        
                Returns:
                    The index of the muscle in the model
        
                .. note:: The simulation support for muscles is in progress and not yet fully functional.
        
                
        """
    def add_particle(self, pos: Vec3, vel: Vec3, mass: float, radius: float = None, flags: wp.uint32 = ...) -> int:
        """
        Adds a single particle to the model
        
                Args:
                    pos: The initial position of the particle
                    vel: The initial velocity of the particle
                    mass: The mass of the particle
                    radius: The radius of the particle used in collision handling. If None, the radius is set to the default value (:attr:`default_particle_radius`).
                    flags: The flags that control the dynamical behavior of the particle, see PARTICLE_FLAG_* constants
        
                Note:
                    Set the mass equal to zero to create a 'kinematic' particle that does is not subject to dynamics.
        
                Returns:
                    The index of the particle in the system
                
        """
    def add_particle_grid(self, pos: Vec3, rot: Quat, vel: Vec3, dim_x: int, dim_y: int, dim_z: int, cell_x: float, cell_y: float, cell_z: float, mass: float, jitter: float, radius_mean: float = None, radius_std: float = 0.0):
        ...
    def add_shape_box(self, body: int, pos: Vec3 = (0.0, 0.0, 0.0), rot: Quat = (0.0, 0.0, 0.0, 1.0), hx: float = 0.5, hy: float = 0.5, hz: float = 0.5, density: float = None, ke: float = None, kd: float = None, kf: float = None, ka: float = None, mu: float = None, restitution: float = None, is_solid: bool = True, thickness: float = None, has_ground_collision: bool = True, has_shape_collision: bool = True, collision_group: int = -1, is_visible: bool = True):
        """
        Adds a box collision shape to a body.
        
                Args:
                    body: The index of the parent body this shape belongs to (use -1 for static shapes)
                    pos: The location of the shape with respect to the parent frame
                    rot: The rotation of the shape with respect to the parent frame
                    hx: The half-extent along the x-axis
                    hy: The half-extent along the y-axis
                    hz: The half-extent along the z-axis
                    density: The density of the shape (None to use the default value :attr:`default_shape_density`)
                    ke: The contact elastic stiffness (None to use the default value :attr:`default_shape_ke`)
                    kd: The contact damping stiffness (None to use the default value :attr:`default_shape_kd`)
                    kf: The contact friction stiffness (None to use the default value :attr:`default_shape_kf`)
                    ka: The contact adhesion distance (None to use the default value :attr:`default_shape_ka`)
                    mu: The coefficient of friction (None to use the default value :attr:`default_shape_mu`)
                    restitution: The coefficient of restitution (None to use the default value :attr:`default_shape_restitution`)
                    is_solid: Whether the box is solid or hollow
                    thickness: Thickness to use for computing inertia of a hollow box, and for collision handling (None to use the default value :attr:`default_shape_thickness`)
                    has_ground_collision: If True, the shape will collide with the ground plane if `Model.ground` is True
                    has_shape_collision: If True, the shape will collide with other shapes
                    collision_group: The collision group of the shape
                    is_visible: Whether the box is visible
        
                Returns:
                    The index of the added shape
        
                
        """
    def add_shape_capsule(self, body: int, pos: Vec3 = (0.0, 0.0, 0.0), rot: Quat = (0.0, 0.0, 0.0, 1.0), radius: float = 1.0, half_height: float = 0.5, up_axis: int = 1, density: float = None, ke: float = None, kd: float = None, kf: float = None, ka: float = None, mu: float = None, restitution: float = None, is_solid: bool = True, thickness: float = None, has_ground_collision: bool = True, has_shape_collision: bool = True, collision_group: int = -1, is_visible: bool = True):
        """
        Adds a capsule collision shape to a body.
        
                Args:
                    body: The index of the parent body this shape belongs to (use -1 for static shapes)
                    pos: The location of the shape with respect to the parent frame
                    rot: The rotation of the shape with respect to the parent frame
                    radius: The radius of the capsule
                    half_height: The half length of the center cylinder along the up axis
                    up_axis: The axis along which the capsule is aligned (0=x, 1=y, 2=z)
                    density: The density of the shape (None to use the default value :attr:`default_shape_density`)
                    ke: The contact elastic stiffness (None to use the default value :attr:`default_shape_ke`)
                    kd: The contact damping stiffness (None to use the default value :attr:`default_shape_kd`)
                    kf: The contact friction stiffness (None to use the default value :attr:`default_shape_kf`)
                    ka: The contact adhesion distance (None to use the default value :attr:`default_shape_ka`)
                    mu: The coefficient of friction (None to use the default value :attr:`default_shape_mu`)
                    restitution: The coefficient of restitution (None to use the default value :attr:`default_shape_restitution`)
                    is_solid: Whether the capsule is solid or hollow
                    thickness: Thickness to use for computing inertia of a hollow capsule, and for collision handling (None to use the default value :attr:`default_shape_thickness`)
                    has_ground_collision: If True, the shape will collide with the ground plane if `Model.ground` is True
                    has_shape_collision: If True, the shape will collide with other shapes
                    collision_group: The collision group of the shape
                    is_visible: Whether the capsule is visible
        
                Returns:
                    The index of the added shape
        
                
        """
    def add_shape_cone(self, body: int, pos: Vec3 = (0.0, 0.0, 0.0), rot: Quat = (0.0, 0.0, 0.0, 1.0), radius: float = 1.0, half_height: float = 0.5, up_axis: int = 1, density: float = None, ke: float = None, kd: float = None, kf: float = None, ka: float = None, mu: float = None, restitution: float = None, is_solid: bool = True, thickness: float = None, has_ground_collision: bool = True, has_shape_collision: bool = True, collision_group: int = -1, is_visible: bool = True):
        """
        Adds a cone collision shape to a body.
        
                Args:
                    body: The index of the parent body this shape belongs to (use -1 for static shapes)
                    pos: The location of the shape with respect to the parent frame
                    rot: The rotation of the shape with respect to the parent frame
                    radius: The radius of the cone
                    half_height: The half length of the cone along the up axis
                    up_axis: The axis along which the cone is aligned (0=x, 1=y, 2=z)
                    density: The density of the shape (None to use the default value :attr:`default_shape_density`)
                    ke: The contact elastic stiffness (None to use the default value :attr:`default_shape_ke`)
                    kd: The contact damping stiffness (None to use the default value :attr:`default_shape_kd`)
                    kf: The contact friction stiffness (None to use the default value :attr:`default_shape_kf`)
                    ka: The contact adhesion distance (None to use the default value :attr:`default_shape_ka`)
                    mu: The coefficient of friction (None to use the default value :attr:`default_shape_mu`)
                    restitution: The coefficient of restitution (None to use the default value :attr:`default_shape_restitution`)
                    is_solid: Whether the cone is solid or hollow
                    thickness: Thickness to use for computing inertia of a hollow cone, and for collision handling (None to use the default value :attr:`default_shape_thickness`)
                    has_ground_collision: If True, the shape will collide with the ground plane if `Model.ground` is True
                    has_shape_collision: If True, the shape will collide with other shapes
                    collision_group: The collision group of the shape
                    is_visible: Whether the cone is visible
        
                Note:
                    Cones are currently not supported in rigid body collision handling.
        
                Returns:
                    The index of the added shape
        
                
        """
    def add_shape_cylinder(self, body: int, pos: Vec3 = (0.0, 0.0, 0.0), rot: Quat = (0.0, 0.0, 0.0, 1.0), radius: float = 1.0, half_height: float = 0.5, up_axis: int = 1, density: float = None, ke: float = None, kd: float = None, kf: float = None, ka: float = None, mu: float = None, restitution: float = None, is_solid: bool = True, thickness: float = None, has_ground_collision: bool = True, has_shape_collision: bool = True, collision_group: int = -1, is_visible: bool = True):
        """
        Adds a cylinder collision shape to a body.
        
                Args:
                    body: The index of the parent body this shape belongs to (use -1 for static shapes)
                    pos: The location of the shape with respect to the parent frame
                    rot: The rotation of the shape with respect to the parent frame
                    radius: The radius of the cylinder
                    half_height: The half length of the cylinder along the up axis
                    up_axis: The axis along which the cylinder is aligned (0=x, 1=y, 2=z)
                    density: The density of the shape (None to use the default value :attr:`default_shape_density`)
                    ke: The contact elastic stiffness (None to use the default value :attr:`default_shape_ke`)
                    kd: The contact damping stiffness (None to use the default value :attr:`default_shape_kd`)
                    kf: The contact friction stiffness (None to use the default value :attr:`default_shape_kf`)
                    ka: The contact adhesion distance (None to use the default value :attr:`default_shape_ka`)
                    mu: The coefficient of friction (None to use the default value :attr:`default_shape_mu`)
                    restitution: The coefficient of restitution (None to use the default value :attr:`default_shape_restitution`)
                    is_solid: Whether the cylinder is solid or hollow
                    thickness: Thickness to use for computing inertia of a hollow cylinder, and for collision handling (None to use the default value :attr:`default_shape_thickness`)
                    has_ground_collision: If True, the shape will collide with the ground plane if `Model.ground` is True
                    has_shape_collision: If True, the shape will collide with other shapes
                    collision_group: The collision group of the shape
                    is_visible: Whether the cylinder is visible
        
                Note:
                    Cylinders are currently not supported in rigid body collision handling.
        
                Returns:
                    The index of the added shape
        
                
        """
    def add_shape_mesh(self, body: int, pos: Vec3 | None = None, rot: Quat | None = None, mesh: Mesh | None = None, scale: Vec3 | None = None, density: float = None, ke: float = None, kd: float = None, kf: float = None, ka: float = None, mu: float = None, restitution: float = None, is_solid: bool = True, thickness: float = None, has_ground_collision: bool = True, has_shape_collision: bool = True, collision_group: int = -1, is_visible: bool = True):
        """
        Adds a triangle mesh collision shape to a body.
        
                Args:
                    body: The index of the parent body this shape belongs to (use -1 for static shapes)
                    pos: The location of the shape with respect to the parent frame
                      (None to use the default value ``wp.vec3(0.0, 0.0, 0.0)``)
                    rot: The rotation of the shape with respect to the parent frame
                      (None to use the default value ``wp.quat(0.0, 0.0, 0.0, 1.0)``)
                    mesh: The mesh object
                    scale: Scale to use for the collider. (None to use the default value ``wp.vec3(1.0, 1.0, 1.0)``)
                    density: The density of the shape (None to use the default value :attr:`default_shape_density`)
                    ke: The contact elastic stiffness (None to use the default value :attr:`default_shape_ke`)
                    kd: The contact damping stiffness (None to use the default value :attr:`default_shape_kd`)
                    kf: The contact friction stiffness (None to use the default value :attr:`default_shape_kf`)
                    ka: The contact adhesion distance (None to use the default value :attr:`default_shape_ka`)
                    mu: The coefficient of friction (None to use the default value :attr:`default_shape_mu`)
                    restitution: The coefficient of restitution (None to use the default value :attr:`default_shape_restitution`)
                    is_solid: If True, the mesh is solid, otherwise it is a hollow surface with the given wall thickness
                    thickness: Thickness to use for computing inertia of a hollow mesh, and for collision handling (None to use the default value :attr:`default_shape_thickness`)
                    has_ground_collision: If True, the shape will collide with the ground plane if `Model.ground` is True
                    has_shape_collision: If True, the shape will collide with other shapes
                    collision_group: The collision group of the shape
                    is_visible: Whether the mesh is visible
        
                Returns:
                    The index of the added shape
        
                
        """
    def add_shape_plane(self, plane: Vec4 = (0.0, 1.0, 0.0, 0.0), pos: Vec3 = None, rot: Quat = None, width: float = 10.0, length: float = 10.0, body: int = -1, ke: float = None, kd: float = None, kf: float = None, ka: float = None, mu: float = None, restitution: float = None, thickness: float = None, has_ground_collision: bool = False, has_shape_collision: bool = True, is_visible: bool = True, collision_group: int = -1):
        """
        
                Adds a plane collision shape.
                If pos and rot are defined, the plane is assumed to have its normal as (0, 1, 0).
                Otherwise, the plane equation defined through the `plane` argument is used.
        
                Args:
                    plane: The plane equation in form a*x + b*y + c*z + d = 0
                    pos: The position of the plane in world coordinates
                    rot: The rotation of the plane in world coordinates
                    width: The extent along x of the plane (infinite if 0)
                    length: The extent along z of the plane (infinite if 0)
                    body: The body index to attach the shape to (-1 by default to keep the plane static)
                    ke: The contact elastic stiffness (None to use the default value :attr:`default_shape_ke`)
                    kd: The contact damping stiffness (None to use the default value :attr:`default_shape_kd`)
                    kf: The contact friction stiffness (None to use the default value :attr:`default_shape_kf`)
                    ka: The contact adhesion distance (None to use the default value :attr:`default_shape_ka`)
                    mu: The coefficient of friction (None to use the default value :attr:`default_shape_mu`)
                    restitution: The coefficient of restitution (None to use the default value :attr:`default_shape_restitution`)
                    thickness: The thickness of the plane (0 by default) for collision handling (None to use the default value :attr:`default_shape_thickness`)
                    has_ground_collision: If True, the shape will collide with the ground plane if `Model.ground` is True
                    has_shape_collision: If True, the shape will collide with other shapes
                    is_visible: Whether the plane is visible
                    collision_group: The collision group of the shape
        
                Returns:
                    The index of the added shape
        
                
        """
    def add_shape_sdf(self, body: int, pos: Vec3 = (0.0, 0.0, 0.0), rot: Quat = (0.0, 0.0, 0.0, 1.0), sdf: SDF = None, scale: Vec3 = (1.0, 1.0, 1.0), density: float = None, ke: float = None, kd: float = None, kf: float = None, ka: float = None, mu: float = None, restitution: float = None, is_solid: bool = True, thickness: float = None, has_ground_collision: bool = True, has_shape_collision: bool = True, collision_group: int = -1, is_visible: bool = True):
        """
        Adds SDF collision shape to a body.
        
                Args:
                    body: The index of the parent body this shape belongs to (use -1 for static shapes)
                    pos: The location of the shape with respect to the parent frame
                    rot: The rotation of the shape with respect to the parent frame
                    sdf: The sdf object
                    scale: Scale to use for the collider
                    density: The density of the shape (None to use the default value :attr:`default_shape_density`)
                    ke: The contact elastic stiffness (None to use the default value :attr:`default_shape_ke`)
                    kd: The contact damping stiffness (None to use the default value :attr:`default_shape_kd`)
                    kf: The contact friction stiffness (None to use the default value :attr:`default_shape_kf`)
                    ka: The contact adhesion distance (None to use the default value :attr:`default_shape_ka`)
                    mu: The coefficient of friction (None to use the default value :attr:`default_shape_mu`)
                    restitution: The coefficient of restitution (None to use the default value :attr:`default_shape_restitution`)
                    is_solid: If True, the SDF is solid, otherwise it is a hollow surface with the given wall thickness
                    thickness: Thickness to use for collision handling (None to use the default value :attr:`default_shape_thickness`)
                    has_ground_collision: If True, the shape will collide with the ground plane if `Model.ground` is True
                    has_shape_collision: If True, the shape will collide with other shapes
                    collision_group: The collision group of the shape
                    is_visible: Whether the shape is visible
        
                Returns:
                    The index of the added shape
        
                
        """
    def add_shape_sphere(self, body, pos: Vec3 = (0.0, 0.0, 0.0), rot: Quat = (0.0, 0.0, 0.0, 1.0), radius: float = 1.0, density: float = None, ke: float = None, kd: float = None, kf: float = None, ka: float = None, mu: float = None, restitution: float = None, is_solid: bool = True, thickness: float = None, has_ground_collision: bool = True, has_shape_collision: bool = True, collision_group: int = -1, is_visible: bool = True):
        """
        Adds a sphere collision shape to a body.
        
                Args:
                    body: The index of the parent body this shape belongs to (use -1 for static shapes)
                    pos: The location of the shape with respect to the parent frame
                    rot: The rotation of the shape with respect to the parent frame
                    radius: The radius of the sphere
                    density: The density of the shape (None to use the default value :attr:`default_shape_density`)
                    ke: The contact elastic stiffness (None to use the default value :attr:`default_shape_ke`)
                    kd: The contact damping stiffness (None to use the default value :attr:`default_shape_kd`)
                    kf: The contact friction stiffness (None to use the default value :attr:`default_shape_kf`)
                    ka: The contact adhesion distance (None to use the default value :attr:`default_shape_ka`)
                    mu: The coefficient of friction (None to use the default value :attr:`default_shape_mu`)
                    restitution: The coefficient of restitution (None to use the default value :attr:`default_shape_restitution`)
                    is_solid: Whether the sphere is solid or hollow
                    thickness: Thickness to use for computing inertia of a hollow sphere, and for collision handling (None to use the default value :attr:`default_shape_thickness`)
                    has_ground_collision: If True, the shape will collide with the ground plane if `Model.ground` is True
                    has_shape_collision: If True, the shape will collide with other shapes
                    collision_group: The collision group of the shape
                    is_visible: Whether the sphere is visible
        
                Returns:
                    The index of the added shape
        
                
        """
    def add_soft_grid(self, pos: Vec3, rot: Quat, vel: Vec3, dim_x: int, dim_y: int, dim_z: int, cell_x: float, cell_y: float, cell_z: float, density: float, k_mu: float, k_lambda: float, k_damp: float, fix_left: bool = False, fix_right: bool = False, fix_top: bool = False, fix_bottom: bool = False, tri_ke: float = None, tri_ka: float = None, tri_kd: float = None, tri_drag: float = None, tri_lift: float = None):
        """
        Helper to create a rectangular tetrahedral FEM grid
        
                Creates a regular grid of FEM tetrahedra and surface triangles. Useful for example
                to create beams and sheets. Each hexahedral cell is decomposed into 5
                tetrahedral elements.
        
                Args:
                    pos: The position of the solid in world space
                    rot: The orientation of the solid in world space
                    vel: The velocity of the solid in world space
                    dim_x_: The number of rectangular cells along the x-axis
                    dim_y: The number of rectangular cells along the y-axis
                    dim_z: The number of rectangular cells along the z-axis
                    cell_x: The width of each cell in the x-direction
                    cell_y: The width of each cell in the y-direction
                    cell_z: The width of each cell in the z-direction
                    density: The density of each particle
                    k_mu: The first elastic Lame parameter
                    k_lambda: The second elastic Lame parameter
                    k_damp: The damping stiffness
                    fix_left: Make the left-most edge of particles kinematic (fixed in place)
                    fix_right: Make the right-most edge of particles kinematic
                    fix_top: Make the top-most edge of particles kinematic
                    fix_bottom: Make the bottom-most edge of particles kinematic
                
        """
    def add_soft_mesh(self, pos: Vec3, rot: Quat, scale: float, vel: Vec3, vertices: list[Vec3], indices: list[int], density: float, k_mu: float, k_lambda: float, k_damp: float, tri_ke: float = None, tri_ka: float = None, tri_kd: float = None, tri_drag: float = None, tri_lift: float = None):
        """
        Helper to create a tetrahedral model from an input tetrahedral mesh
        
                Args:
                    pos: The position of the solid in world space
                    rot: The orientation of the solid in world space
                    vel: The velocity of the solid in world space
                    vertices: A list of vertex positions, array of 3D points
                    indices: A list of tetrahedron indices, 4 entries per-element, flattened array
                    density: The density per-area of the mesh
                    k_mu: The first elastic Lame parameter
                    k_lambda: The second elastic Lame parameter
                    k_damp: The damping stiffness
                
        """
    def add_spring(self, i: int, j, ke: float, kd: float, control: float):
        """
        Adds a spring between two particles in the system
        
                Args:
                    i: The index of the first particle
                    j: The index of the second particle
                    ke: The elastic stiffness of the spring
                    kd: The damping stiffness of the spring
                    control: The actuation level of the spring
        
                Note:
                    The spring is created with a rest-length based on the distance
                    between the particles in their initial configuration.
        
                
        """
    def add_tetrahedron(self, i: int, j: int, k: int, l: int, k_mu: float = 1000.0, k_lambda: float = 1000.0, k_damp: float = 0.0) -> float:
        """
        Adds a tetrahedral FEM element between four particles in the system.
        
                Tetrahedra are modeled as viscoelastic elements with a NeoHookean energy
                density based on [Smith et al. 2018].
        
                Args:
                    i: The index of the first particle
                    j: The index of the second particle
                    k: The index of the third particle
                    l: The index of the fourth particle
                    k_mu: The first elastic Lame parameter
                    k_lambda: The second elastic Lame parameter
                    k_damp: The element's damping stiffness
        
                Return:
                    The volume of the tetrahedron
        
                Note:
                    The tetrahedron is created with a rest-pose based on the particle's initial configuration
        
                
        """
    def add_triangle(self, i: int, j: int, k: int, tri_ke: float = None, tri_ka: float = None, tri_kd: float = None, tri_drag: float = None, tri_lift: float = None) -> float:
        """
        Adds a triangular FEM element between three particles in the system.
        
                Triangles are modeled as viscoelastic elements with elastic stiffness and damping
                parameters specified on the model. See model.tri_ke, model.tri_kd.
        
                Args:
                    i: The index of the first particle
                    j: The index of the second particle
                    k: The index of the third particle
        
                Return:
                    The area of the triangle
        
                Note:
                    The triangle is created with a rest-length based on the distance
                    between the particles in their initial configuration.
                
        """
    def add_triangles(self, i: list[int], j: list[int], k: list[int], tri_ke: list[float] | None = None, tri_ka: list[float] | None = None, tri_kd: list[float] | None = None, tri_drag: list[float] | None = None, tri_lift: list[float] | None = None) -> list[float]:
        """
        Adds triangular FEM elements between groups of three particles in the system.
        
                Triangles are modeled as viscoelastic elements with elastic stiffness and damping
                Parameters specified on the model. See model.tri_ke, model.tri_kd.
        
                Args:
                    i: The indices of the first particle
                    j: The indices of the second particle
                    k: The indices of the third particle
        
                Return:
                    The areas of the triangles
        
                Note:
                    A triangle is created with a rest-length based on the distance
                    between the particles in their initial configuration.
        
                
        """
    def collapse_fixed_joints(self, verbose = False):
        """
        Removes fixed joints from the model and merges the bodies they connect. This is useful for simplifying the model for faster and more stable simulation.
        """
    def color(self, include_bending = False, balance_colors = True, target_max_min_color_ratio = 1.1, coloring_algorithm = ...):
        """
        
                Run coloring algorithm to generate coloring information.
        
                Args:
                    include_bending_energy: Whether to consider bending energy for trimeshes in the coloring process. If set to `True`, the generated
                        graph will contain all the edges connecting o1 and o2; otherwise, the graph will be equivalent to the trimesh.
                    balance_colors: Whether to apply the color balancing algorithm to balance the size of each color
                    target_max_min_color_ratio: the color balancing algorithm will stop when the ratio between the largest color and
                        the smallest color reaches this value
                    algorithm: Value should be an enum type of ColoringAlgorithm, otherwise it will raise an error. ColoringAlgorithm.mcs means using the MCS coloring algorithm,
                        while ColoringAlgorithm.ordered_greedy means using the degree-ordered greedy algorithm. The MCS algorithm typically generates 30% to 50% fewer colors
                        compared to the ordered greedy algorithm, while maintaining the same linear complexity. Although MCS has a constant overhead that makes it about twice
                        as slow as the greedy algorithm, it produces significantly better coloring results. We recommend using MCS, especially if coloring is only part of the
                        preprocessing.
        
                Note:
        
                    References to the coloring algorithm:
        
                    MCS: Pereira, F. M. Q., & Palsberg, J. (2005, November). Register allocation via coloring of chordal graphs. In Asian Symposium on Programming Languages and Systems (pp. 315-329). Berlin, Heidelberg: Springer Berlin Heidelberg.
        
                    Ordered Greedy: Ton-That, Q. M., Kry, P. G., & Andrews, S. (2023). Parallel block Neo-Hookean XPBD using graph clustering. Computers & Graphics, 110, 1-10.
        
                
        """
    def finalize(self, device = None, requires_grad = False) -> Model:
        """
        Convert this builder object to a concrete model for simulation.
        
                After building simulation elements this method should be called to transfer
                all data to device memory ready for simulation.
        
                Args:
                    device: The simulation device to use, e.g.: 'cpu', 'cuda'
                    requires_grad: Whether to enable gradient computation for the model
        
                Returns:
        
                    A model object.
                
        """
    def plot_articulation(self, show_body_names = True, show_joint_names = True, show_joint_types = True, plot_shapes = True, show_shape_types = True, show_legend = True):
        """
        
                Visualizes the model's articulation graph using matplotlib and networkx.
                Uses the spring layout algorithm from networkx to arrange the nodes.
                Bodies are shown as orange squares, shapes are shown as blue circles.
        
                Args:
                    show_body_names (bool): Whether to show the body names or indices
                    show_joint_names (bool): Whether to show the joint names or indices
                    show_joint_types (bool): Whether to show the joint types
                    plot_shapes (bool): Whether to render the shapes connected to the rigid bodies
                    show_shape_types (bool): Whether to show the shape geometry types
                    show_legend (bool): Whether to show a legend
                
        """
    def set_coloring(self, particle_coloring):
        """
        
                Set coloring information with user-provided coloring.
        
                Args:
                    particle_coloring: A list of list or `np.array` with `dtype`=`int`. The length of the list is the number of colors
                     and each list or `np.array` contains the indices of vertices with this color.
                
        """
    def set_ground_plane(self, normal = None, offset = 0.0, ke: float = None, kd: float = None, kf: float = None, mu: float = None, restitution: float = None):
        """
        
                Creates a ground plane for the world. If the normal is not specified,
                the up_vector of the ModelBuilder is used.
                
        """
    @property
    def articulation_count(self):
        ...
    @property
    def body_count(self):
        ...
    @property
    def edge_count(self):
        ...
    @property
    def joint_axis_count(self):
        ...
    @property
    def joint_count(self):
        ...
    @property
    def muscle_count(self):
        ...
    @property
    def particle_count(self):
        ...
    @property
    def shape_count(self):
        ...
    @property
    def spring_count(self):
        ...
    @property
    def tet_count(self):
        ...
    @property
    def tri_count(self):
        ...
class SDF:
    """
    Describes a signed distance field for simulation
    
        Attributes:
    
            volume (Volume): The volume defining the SDF
            I (Mat33): 3x3 inertia matrix of the SDF
            mass (float): The total mass of the SDF
            com (Vec3): The center of mass of the SDF
        
    """
    def __hash__(self):
        ...
    def __init__(self, volume = None, I = None, mass = 1.0, com = None):
        ...
    def finalize(self, device = None):
        ...
class State:
    """
    Time-varying state data for a :class:`Model`.
    
        Time-varying state data includes particle positions, velocities, rigid body states, and
        anything that is output from the integrator as derived data, e.g.: forces.
    
        The exact attributes depend on the contents of the model. State objects should
        generally be created using the :func:`Model.state()` function.
        
    """
    def __init__(self):
        ...
    def clear_forces(self) -> None:
        """
        Clear all forces (for particles and bodies) in the state object.
        """
    @property
    def body_count(self) -> int:
        """
        The number of bodies represented in the state.
        """
    @property
    def joint_coord_count(self) -> int:
        """
        The number of generalized joint position coordinates represented in the state.
        """
    @property
    def joint_dof_count(self) -> int:
        """
        The number of generalized joint velocity coordinates represented in the state.
        """
    @property
    def particle_count(self) -> int:
        """
        The number of particles represented in the state.
        """
    @property
    def requires_grad(self) -> bool:
        """
        Indicates whether the state arrays have gradient computation enabled.
        """
def compute_shape_mass(type, scale, src, density, is_solid, thickness):
    """
    Computes the mass, center of mass and 3x3 inertia tensor of a shape
    
        Args:
            type: The type of shape (GEO_SPHERE, GEO_BOX, etc.)
            scale: The scale of the shape
            src: The source shape (Mesh or SDF)
            density: The density of the shape
            is_solid: Whether the shape is solid or hollow
            thickness: The thickness of the shape (used for collision detection, and inertia computation of hollow shapes)
    
        Returns:
            The mass, center of mass and 3x3 inertia tensor of the shape
        
    """
def flag_to_int(flag):
    """
    Converts a flag to an integer.
    """
GEO_BOX: int = 1
GEO_CAPSULE: int = 2
GEO_CONE: int = 4
GEO_CYLINDER: int = 3
GEO_MESH: int = 5
GEO_NONE: int = 8
GEO_PLANE: int = 7
GEO_SDF: int = 6
GEO_SPHERE: int = 0
JOINT_BALL: int = 2
JOINT_COMPOUND: int = 5
JOINT_D6: int = 8
JOINT_DISTANCE: int = 7
JOINT_FIXED: int = 3
JOINT_FREE: int = 4
JOINT_MODE_FORCE: int = 0
JOINT_MODE_TARGET_POSITION: int = 1
JOINT_MODE_TARGET_VELOCITY: int = 2
JOINT_PRISMATIC: int = 0
JOINT_REVOLUTE: int = 1
JOINT_UNIVERSAL: int = 6
Mat33: typing._GenericAlias  # value = typing.List[float]
ModelShapeGeometry: warp.codegen.Struct  # value = <warp.codegen.Struct object>
ModelShapeMaterials: warp.codegen.Struct  # value = <warp.codegen.Struct object>
PARTICLE_FLAG_ACTIVE: warp.types.uint32  # value = <warp.types.uint32 object>
Quat: typing._GenericAlias  # value = typing.List[float]
Transform: typing._GenericAlias  # value = typing.Tuple[typing.List[float], typing.List[float]]
Vec3: typing._GenericAlias  # value = typing.List[float]
Vec4: typing._GenericAlias  # value = typing.List[float]
