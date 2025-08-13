from __future__ import annotations
import numpy as np
import typing
import warp as wp
import warp.codegen
import warp.context
from warp.sim.collide import TriMeshCollisionDetector
import warp.sim.integrator
from warp.sim.integrator import Integrator
import warp.sim.model
from warp.sim.model import Control
from warp.sim.model import Model
from warp.sim.model import State
import warp.types
from warp.types import float32
from warp.types import matrix
__all__: list[str] = ['Control', 'ForceElementAdjacencyInfo', 'Integrator', 'Model', 'ModelShapeMaterials', 'PARTICLE_FLAG_ACTIVE', 'State', 'TriMeshCollisionDetector', 'TriMeshCollisionInfo', 'VBDIntegrator', 'VBD_DEBUG_PRINTING_OPTIONS', 'VBD_copy_particle_positions_back', 'VBD_solve_trimesh_no_self_contact', 'VBD_solve_trimesh_with_self_contact_penetration_free', 'apply_conservative_bound_truncation', 'assemble_membrane_hessian', 'build_orthonormal_basis', 'calculate_triangle_deformation_gradient', 'compute_friction', 'compute_particle_conservative_bound', 'convert_body_particle_contact_data_kernel', 'evaluate_body_particle_contact', 'evaluate_dihedral_angle_based_bending_force_hessian', 'evaluate_edge_edge_contact', 'evaluate_ground_contact_force_hessian', 'evaluate_self_contact_force_norm', 'evaluate_stvk_force_hessian', 'evaluate_vertex_triangle_collision_force_hessian', 'float32', 'forward_step', 'forward_step_penetration_free', 'get_edge_colliding_edges', 'get_edge_colliding_edges_count', 'get_triangle_colliding_vertices', 'get_triangle_colliding_vertices_count', 'get_vertex_adjacent_edge_id_order', 'get_vertex_adjacent_face_id_order', 'get_vertex_colliding_triangles', 'get_vertex_colliding_triangles_count', 'get_vertex_num_adjacent_edges', 'get_vertex_num_adjacent_faces', 'green_strain', 'mat32', 'mat66', 'mat_vec_cross', 'mat_vec_cross_from_3_basis', 'matrix', 'np', 'triangle_closest_point', 'update_velocity', 'validate_conservative_bound', 'wp']
class VBDIntegrator(warp.sim.integrator.Integrator):
    """
    An implicit integrator using Vertex Block Descent (VBD) for cloth simulation.
    
        References:
            - Anka He Chen, Ziheng Liu, Yin Yang, and Cem Yuksel. 2024. Vertex Block Descent. ACM Trans. Graph. 43, 4, Article 116 (July 2024), 16 pages. https://doi.org/10.1145/3658179
    
        Note that VBDIntegrator's constructor requires a :class:`Model` object as input, so that it can do some precomputation and preallocate the space.
        After construction, you must provide the same :class:`Model` object that you used that was used during construction.
        Currently, you must manually provide particle coloring and assign it to `model.particle_coloring` to make VBD work.
    
        VBDIntegrator.simulate accepts three arguments: class:`Model`, :class:`State`, and :class:`Control` (optional) objects, this time-integrator
        may be used to advance the simulation state forward in time.
    
        Example
        -------
    
        .. code-block:: python
    
            model.particle_coloring = # load or generate particle coloring
            integrator = wp.VBDIntegrator(model)
    
            # simulation loop
            for i in range(100):
                state = integrator.simulate(model, state_in, state_out, dt, control)
    
        
    """
    count_num_adjacent_edges: typing.ClassVar[warp.context.Kernel]  # value = <warp.context.Kernel object>
    count_num_adjacent_faces: typing.ClassVar[warp.context.Kernel]  # value = <warp.context.Kernel object>
    fill_adjacent_edges: typing.ClassVar[warp.context.Kernel]  # value = <warp.context.Kernel object>
    fill_adjacent_faces: typing.ClassVar[warp.context.Kernel]  # value = <warp.context.Kernel object>
    def __init__(self, model: warp.sim.model.Model, iterations = 10, handle_self_contact = False, penetration_free_conservative_bound_relaxation = 0.42, friction_epsilon = 0.01, body_particle_contact_buffer_pre_alloc = 4, vertex_collision_buffer_pre_alloc = 32, edge_collision_buffer_pre_alloc = 64, triangle_collision_buffer_pre_alloc = 32, edge_edge_parallel_epsilon = 1e-05):
        ...
    def collision_detection_penetration_free(self, current_state, dt):
        ...
    def compute_force_element_adjacency(self, model):
        ...
    def convert_body_particle_contact_data(self):
        ...
    def simulate(self, model: warp.sim.model.Model, state_in: warp.sim.model.State, state_out: warp.sim.model.State, dt: float, control: warp.sim.model.Control = None):
        ...
    def simulate_one_step_no_self_contact(self, model: warp.sim.model.Model, state_in: warp.sim.model.State, state_out: warp.sim.model.State, dt: float, control: warp.sim.model.Control = None):
        ...
    def simulate_one_step_with_collisions_penetration_free(self, model: warp.sim.model.Model, state_in: warp.sim.model.State, state_out: warp.sim.model.State, dt: float, control: warp.sim.model.Control = None):
        ...
class mat32(warp.types.matrix.<locals>.mat_t):
    pass
class mat66(warp.types.matrix.<locals>.mat_t):
    pass
ForceElementAdjacencyInfo: warp.codegen.Struct  # value = <warp.codegen.Struct object>
ModelShapeMaterials: warp.codegen.Struct  # value = <warp.codegen.Struct object>
PARTICLE_FLAG_ACTIVE: warp.types.uint32  # value = <warp.types.uint32 object>
TriMeshCollisionInfo: warp.codegen.Struct  # value = <warp.codegen.Struct object>
VBD_DEBUG_PRINTING_OPTIONS: dict = {}
VBD_copy_particle_positions_back: warp.context.Kernel  # value = <warp.context.Kernel object>
VBD_solve_trimesh_no_self_contact: warp.context.Kernel  # value = <warp.context.Kernel object>
VBD_solve_trimesh_with_self_contact_penetration_free: warp.context.Kernel  # value = <warp.context.Kernel object>
_test_compute_force_element_adjacency: warp.context.Kernel  # value = <warp.context.Kernel object>
apply_conservative_bound_truncation: warp.context.Function  # value = <Function apply_conservative_bound_truncation(v_index: int32, pos_new: vec3f, pos_prev_collision_detection: array(ndim=1, dtype=vec3f), particle_conservative_bounds: array(ndim=1, dtype=float32))>
assemble_membrane_hessian: warp.context.Function  # value = <Function assemble_membrane_hessian(h: matrix(shape=(6, 6), dtype=float32), m1: builtins.float, m2: builtins.float)>
build_orthonormal_basis: warp.context.Function  # value = <Function build_orthonormal_basis(n: vec3f)>
calculate_triangle_deformation_gradient: warp.context.Function  # value = <Function calculate_triangle_deformation_gradient(face: builtins.int, tri_indices: array(ndim=2, dtype=int32), pos: array(ndim=1, dtype=vec3f), tri_pose: mat22(f))>
compute_friction: warp.context.Function  # value = <Function compute_friction(mu: builtins.float, normal_contact_force: builtins.float, T: mat32(f), u: vec2f, eps_u: builtins.float)>
compute_particle_conservative_bound: warp.context.Kernel  # value = <warp.context.Kernel object>
convert_body_particle_contact_data_kernel: warp.context.Kernel  # value = <warp.context.Kernel object>
evaluate_body_particle_contact: warp.context.Function  # value = <Function evaluate_body_particle_contact(particle_index: builtins.int, particle_pos: vec3f, particle_prev_pos: vec3f, contact_index: builtins.int, soft_contact_ke: builtins.float, friction_mu: builtins.float, friction_epsilon: builtins.float, particle_radius: array(ndim=1, dtype=float32), shape_materials: warp.sim.model.ModelShapeMaterials, shape_body: array(ndim=1, dtype=int32), body_q: array(ndim=1, dtype=transformf), body_qd: array(ndim=1, dtype=vector(length=6, dtype=float32)), body_com: array(ndim=1, dtype=vec3f), contact_shape: array(ndim=1, dtype=int32), contact_body_pos: array(ndim=1, dtype=vec3f), contact_body_vel: array(ndim=1, dtype=vec3f), contact_normal: array(ndim=1, dtype=vec3f), dt: builtins.float)>
evaluate_dihedral_angle_based_bending_force_hessian: warp.context.Function  # value = <Function evaluate_dihedral_angle_based_bending_force_hessian(bending_index: builtins.int, v_order: builtins.int, pos: array(ndim=1, dtype=vec3f), pos_prev: array(ndim=1, dtype=vec3f), edge_indices: array(ndim=2, dtype=int32), edge_rest_angle: array(ndim=1, dtype=float32), edge_rest_length: array(ndim=1, dtype=float32), stiffness: builtins.float, damping: builtins.float, dt: builtins.float)>
evaluate_edge_edge_contact: warp.context.Function  # value = <Function evaluate_edge_edge_contact(v: builtins.int, v_order: builtins.int, e1: builtins.int, e2: builtins.int, pos: array(ndim=1, dtype=vec3f), pos_prev: array(ndim=1, dtype=vec3f), edge_indices: array(ndim=2, dtype=int32), collision_radius: builtins.float, collision_stiffness: builtins.float, friction_coefficient: builtins.float, friction_epsilon: builtins.float, dt: builtins.float, edge_edge_parallel_epsilon: builtins.float)>
evaluate_ground_contact_force_hessian: warp.context.Function  # value = <Function evaluate_ground_contact_force_hessian(particle_pos: vec3f, particle_prev_pos: vec3f, particle_radius: builtins.float, ground_normal: vec3f, ground_level: builtins.float, soft_contact_ke: builtins.float, friction_mu: builtins.float, friction_epsilon: builtins.float, dt: builtins.float)>
evaluate_self_contact_force_norm: warp.context.Function  # value = <Function evaluate_self_contact_force_norm(dis: builtins.float, collision_radius: builtins.float, k: builtins.float)>
evaluate_stvk_force_hessian: warp.context.Function  # value = <Function evaluate_stvk_force_hessian(face: builtins.int, v_order: builtins.int, pos: array(ndim=1, dtype=vec3f), tri_indices: array(ndim=2, dtype=int32), tri_pose: mat22(f), area: builtins.float, mu: builtins.float, lmbd: builtins.float, damping: builtins.float)>
evaluate_vertex_triangle_collision_force_hessian: warp.context.Function  # value = <Function evaluate_vertex_triangle_collision_force_hessian(v: builtins.int, v_order: builtins.int, tri: builtins.int, pos: array(ndim=1, dtype=vec3f), pos_prev: array(ndim=1, dtype=vec3f), tri_indices: array(ndim=2, dtype=int32), collision_radius: builtins.float, collision_stiffness: builtins.float, friction_coefficient: builtins.float, friction_epsilon: builtins.float, dt: builtins.float)>
forward_step: warp.context.Kernel  # value = <warp.context.Kernel object>
forward_step_penetration_free: warp.context.Kernel  # value = <warp.context.Kernel object>
get_edge_colliding_edges: warp.context.Function  # value = <Function get_edge_colliding_edges(col_info: warp.sim.collide.TriMeshCollisionInfo, e: builtins.int, i_collision: builtins.int)>
get_edge_colliding_edges_count: warp.context.Function  # value = <Function get_edge_colliding_edges_count(col_info: warp.sim.collide.TriMeshCollisionInfo, e: builtins.int)>
get_triangle_colliding_vertices: warp.context.Function  # value = <Function get_triangle_colliding_vertices(col_info: warp.sim.collide.TriMeshCollisionInfo, tri: builtins.int, i_collision: builtins.int)>
get_triangle_colliding_vertices_count: warp.context.Function  # value = <Function get_triangle_colliding_vertices_count(col_info: warp.sim.collide.TriMeshCollisionInfo, tri: builtins.int)>
get_vertex_adjacent_edge_id_order: warp.context.Function  # value = <Function get_vertex_adjacent_edge_id_order(adjacency: warp.sim.integrator_vbd.ForceElementAdjacencyInfo, vertex: int32, edge: int32)>
get_vertex_adjacent_face_id_order: warp.context.Function  # value = <Function get_vertex_adjacent_face_id_order(adjacency: warp.sim.integrator_vbd.ForceElementAdjacencyInfo, vertex: int32, face: int32)>
get_vertex_colliding_triangles: warp.context.Function  # value = <Function get_vertex_colliding_triangles(col_info: warp.sim.collide.TriMeshCollisionInfo, v: builtins.int, i_collision: builtins.int)>
get_vertex_colliding_triangles_count: warp.context.Function  # value = <Function get_vertex_colliding_triangles_count(col_info: warp.sim.collide.TriMeshCollisionInfo, v: builtins.int)>
get_vertex_num_adjacent_edges: warp.context.Function  # value = <Function get_vertex_num_adjacent_edges(adjacency: warp.sim.integrator_vbd.ForceElementAdjacencyInfo, vertex: int32)>
get_vertex_num_adjacent_faces: warp.context.Function  # value = <Function get_vertex_num_adjacent_faces(adjacency: warp.sim.integrator_vbd.ForceElementAdjacencyInfo, vertex: int32)>
green_strain: warp.context.Function  # value = <Function green_strain(F: mat32(f))>
mat_vec_cross: warp.context.Function  # value = <Function mat_vec_cross(mat: mat33(f), a: vec3f)>
mat_vec_cross_from_3_basis: warp.context.Function  # value = <Function mat_vec_cross_from_3_basis(e1: vec3f, e2: vec3f, e3: vec3f, a: vec3f)>
triangle_closest_point: warp.context.Function  # value = <Function triangle_closest_point(a: vec3f, b: vec3f, c: vec3f, p: vec3f)>
update_velocity: warp.context.Kernel  # value = <warp.context.Kernel object>
validate_conservative_bound: warp.context.Kernel  # value = <warp.context.Kernel object>
