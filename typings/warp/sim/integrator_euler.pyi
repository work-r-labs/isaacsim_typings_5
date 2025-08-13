"""
This module contains time-integration objects for simulating
models + state forward in time.

"""
from __future__ import annotations
import warp as wp
import warp.codegen
import warp.context
import warp.sim.integrator
from warp.sim.integrator import Integrator
import warp.sim.model
from warp.sim.model import Control
from warp.sim.model import Model
from warp.sim.model import State
from warp.sim.particles import eval_particle_forces
import warp.types
__all__: list[str] = ['Control', 'Integrator', 'Model', 'ModelShapeGeometry', 'ModelShapeMaterials', 'PARTICLE_FLAG_ACTIVE', 'SemiImplicitIntegrator', 'State', 'compute_forces', 'compute_muscle_force', 'eval_bending', 'eval_bending_forces', 'eval_body_contact_forces', 'eval_body_joint_forces', 'eval_body_joints', 'eval_joint_force', 'eval_muscle_forces', 'eval_muscles', 'eval_particle_body_contact_forces', 'eval_particle_contacts', 'eval_particle_forces', 'eval_particle_ground_contact_forces', 'eval_particle_ground_contacts', 'eval_rigid_contacts', 'eval_spring_forces', 'eval_springs', 'eval_tetrahedra', 'eval_tetrahedral_forces', 'eval_triangle_contact_forces', 'eval_triangle_forces', 'eval_triangles', 'eval_triangles_body_contacts', 'eval_triangles_contact', 'quat_decompose', 'quat_twist', 'triangle_closest_point_barycentric', 'wp']
class SemiImplicitIntegrator(warp.sim.integrator.Integrator):
    """
    A semi-implicit integrator using symplectic Euler
    
        After constructing `Model` and `State` objects this time-integrator
        may be used to advance the simulation state forward in time.
    
        Semi-implicit time integration is a variational integrator that
        preserves energy, however it not unconditionally stable, and requires a time-step
        small enough to support the required stiffness and damping forces.
    
        See: https://en.wikipedia.org/wiki/Semi-implicit_Euler_method
    
        Example
        -------
    
        .. code-block:: python
    
            integrator = wp.SemiImplicitIntegrator()
    
            # simulation loop
            for i in range(100):
                state = integrator.simulate(model, state_in, state_out, dt)
    
        
    """
    def __init__(self, angular_damping: float = 0.05, friction_smoothing: float = 1.0):
        """
        
                Args:
                    angular_damping (float, optional): Angular damping factor. Defaults to 0.05.
                    friction_smoothing (float, optional): The delta value for the Huber norm (see :func:`warp.math.norm_huber`) used for the friction velocity normalization. Defaults to 1.0.
                
        """
    def simulate(self, model: warp.sim.model.Model, state_in: warp.sim.model.State, state_out: warp.sim.model.State, dt: float, control: warp.sim.model.Control = None):
        ...
def compute_forces(model: warp.sim.model.Model, state: warp.sim.model.State, control: warp.sim.model.Control, particle_f: warp.types.array, body_f: warp.types.array, dt: float, friction_smoothing: float = 1.0):
    ...
def eval_bending_forces(model: warp.sim.model.Model, state: warp.sim.model.State, particle_f: warp.types.array):
    ...
def eval_body_contact_forces(model: warp.sim.model.Model, state: warp.sim.model.State, particle_f: warp.types.array, friction_smoothing: float = 1.0):
    ...
def eval_body_joint_forces(model: warp.sim.model.Model, state: warp.sim.model.State, control: warp.sim.model.Control, body_f: warp.types.array):
    ...
def eval_muscle_forces(model: warp.sim.model.Model, state: warp.sim.model.State, control: warp.sim.model.Control, body_f: warp.types.array):
    ...
def eval_particle_body_contact_forces(model: warp.sim.model.Model, state: warp.sim.model.State, particle_f: warp.types.array, body_f: warp.types.array, body_f_in_world_frame: bool = False):
    ...
def eval_particle_ground_contact_forces(model: warp.sim.model.Model, state: warp.sim.model.State, particle_f: warp.types.array):
    ...
def eval_spring_forces(model: warp.sim.model.Model, state: warp.sim.model.State, particle_f: warp.types.array):
    ...
def eval_tetrahedral_forces(model: warp.sim.model.Model, state: warp.sim.model.State, control: warp.sim.model.Control, particle_f: warp.types.array):
    ...
def eval_triangle_contact_forces(model: warp.sim.model.Model, state: warp.sim.model.State, particle_f: warp.types.array):
    ...
def eval_triangle_forces(model: warp.sim.model.Model, state: warp.sim.model.State, control: warp.sim.model.Control, particle_f: warp.types.array):
    ...
ModelShapeGeometry: warp.codegen.Struct  # value = <warp.codegen.Struct object>
ModelShapeMaterials: warp.codegen.Struct  # value = <warp.codegen.Struct object>
PARTICLE_FLAG_ACTIVE: warp.types.uint32  # value = <warp.types.uint32 object>
compute_muscle_force: warp.context.Function  # value = <Function compute_muscle_force(i: builtins.int, body_X_s: array(ndim=1, dtype=transformf), body_v_s: array(ndim=1, dtype=vector(length=6, dtype=float32)), body_com: array(ndim=1, dtype=vec3f), muscle_links: array(ndim=1, dtype=int32), muscle_points: array(ndim=1, dtype=vec3f), muscle_activation: builtins.float, body_f_s: array(ndim=1, dtype=vector(length=6, dtype=float32)))>
eval_bending: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_body_joints: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_joint_force: warp.context.Function  # value = <Function eval_joint_force(q: builtins.float, qd: builtins.float, act: builtins.float, target_ke: builtins.float, target_kd: builtins.float, limit_lower: builtins.float, limit_upper: builtins.float, limit_ke: builtins.float, limit_kd: builtins.float, mode: int32)>
eval_muscles: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_particle_contacts: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_particle_ground_contacts: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_rigid_contacts: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_springs: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_tetrahedra: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_triangles: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_triangles_body_contacts: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_triangles_contact: warp.context.Kernel  # value = <warp.context.Kernel object>
quat_decompose: warp.context.Function  # value = <Function quat_decompose(q: quatf)>
quat_twist: warp.context.Function  # value = <Function quat_twist(axis: vec3f, q: quatf)>
triangle_closest_point_barycentric: warp.context.Function  # value = <Function triangle_closest_point_barycentric(a: vec3f, b: vec3f, c: vec3f, p: vec3f)>
