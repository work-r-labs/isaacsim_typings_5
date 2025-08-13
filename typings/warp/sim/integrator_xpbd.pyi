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
import warp.types
__all__: list[str] = ['Control', 'Integrator', 'JOINT_MODE_FORCE', 'JOINT_MODE_TARGET_POSITION', 'JOINT_MODE_TARGET_VELOCITY', 'Model', 'ModelShapeMaterials', 'PARTICLE_FLAG_ACTIVE', 'State', 'XPBDIntegrator', 'apply_body_delta_velocities', 'apply_body_deltas', 'apply_joint_actions', 'apply_particle_deltas', 'apply_particle_ground_restitution', 'apply_particle_shape_restitution', 'apply_rigid_restitution', 'bending_constraint', 'compute_angular_correction', 'compute_angular_correction_3d', 'compute_contact_constraint_delta', 'compute_linear_correction_3d', 'compute_positional_correction', 'solve_body_contact_positions', 'solve_body_joints', 'solve_particle_ground_contacts', 'solve_particle_particle_contacts', 'solve_particle_shape_contacts', 'solve_simple_body_joints', 'solve_springs', 'solve_tetrahedra', 'solve_tetrahedra2', 'update_body_velocities', 'update_joint_axis_limits', 'update_joint_axis_mode', 'update_joint_axis_target_ke_kd', 'vec_abs', 'vec_leaky_max', 'vec_leaky_min', 'vec_max', 'vec_min', 'velocity_at_point', 'wp']
class XPBDIntegrator(warp.sim.integrator.Integrator):
    """
    An implicit integrator using eXtended Position-Based Dynamics (XPBD) for rigid and soft body simulation.
    
        References:
            - Miles Macklin, Matthias Müller, and Nuttapong Chentanez. 2016. XPBD: position-based simulation of compliant constrained dynamics. In Proceedings of the 9th International Conference on Motion in Games (MIG '16). Association for Computing Machinery, New York, NY, USA, 49-54. https://doi.org/10.1145/2994258.2994272
            - Matthias Müller, Miles Macklin, Nuttapong Chentanez, Stefan Jeschke, and Tae-Yong Kim. 2020. Detailed rigid body simulation with extended position based dynamics. In Proceedings of the ACM SIGGRAPH/Eurographics Symposium on Computer Animation (SCA '20). Eurographics Association, Goslar, DEU, Article 10, 1-12. https://doi.org/10.1111/cgf.14105
    
        After constructing :class:`Model`, :class:`State`, and :class:`Control` (optional) objects, this time-integrator
        may be used to advance the simulation state forward in time.
    
        Example
        -------
    
        .. code-block:: python
    
            integrator = wp.XPBDIntegrator()
    
            # simulation loop
            for i in range(100):
                state = integrator.simulate(model, state_in, state_out, dt, control)
    
        
    """
    def __init__(self, iterations = 2, soft_body_relaxation = 0.9, soft_contact_relaxation = 0.9, joint_linear_relaxation = 0.7, joint_angular_relaxation = 0.4, rigid_contact_relaxation = 0.8, rigid_contact_con_weighting = True, angular_damping = 0.0, enable_restitution = False):
        ...
    def apply_body_deltas(self, model: warp.sim.model.Model, state_in: warp.sim.model.State, state_out: warp.sim.model.State, body_deltas: warp.types.array, dt: float, rigid_contact_inv_weight: warp.types.array = None):
        ...
    def apply_particle_deltas(self, model: warp.sim.model.Model, state_in: warp.sim.model.State, state_out: warp.sim.model.State, particle_deltas: warp.types.array, dt: float):
        ...
    def simulate(self, model: warp.sim.model.Model, state_in: warp.sim.model.State, state_out: warp.sim.model.State, dt: float, control: warp.sim.model.Control = None):
        ...
JOINT_MODE_FORCE: int = 0
JOINT_MODE_TARGET_POSITION: int = 1
JOINT_MODE_TARGET_VELOCITY: int = 2
ModelShapeMaterials: warp.codegen.Struct  # value = <warp.codegen.Struct object>
PARTICLE_FLAG_ACTIVE: warp.types.uint32  # value = <warp.types.uint32 object>
apply_body_delta_velocities: warp.context.Kernel  # value = <warp.context.Kernel object>
apply_body_deltas: warp.context.Kernel  # value = <warp.context.Kernel object>
apply_joint_actions: warp.context.Kernel  # value = <warp.context.Kernel object>
apply_particle_deltas: warp.context.Kernel  # value = <warp.context.Kernel object>
apply_particle_ground_restitution: warp.context.Kernel  # value = <warp.context.Kernel object>
apply_particle_shape_restitution: warp.context.Kernel  # value = <warp.context.Kernel object>
apply_rigid_restitution: warp.context.Kernel  # value = <warp.context.Kernel object>
bending_constraint: warp.context.Kernel  # value = <warp.context.Kernel object>
compute_angular_correction: warp.context.Function  # value = <Function compute_angular_correction(err: builtins.float, derr: builtins.float, tf_a: transformf, tf_b: transformf, I_inv_a: mat33(f), I_inv_b: mat33(f), angular_a: vec3f, angular_b: vec3f, lambda_in: builtins.float, compliance: builtins.float, damping: builtins.float, dt: builtins.float)>
compute_angular_correction_3d: warp.context.Function  # value = <Function compute_angular_correction_3d(corr: vec3f, q1: quatf, q2: quatf, m_inv1: builtins.float, m_inv2: builtins.float, I_inv1: mat33(f), I_inv2: mat33(f), alpha_tilde: builtins.float, relaxation: builtins.float, dt: builtins.float)>
compute_contact_constraint_delta: warp.context.Function  # value = <Function compute_contact_constraint_delta(err: builtins.float, tf_a: transformf, tf_b: transformf, m_inv_a: builtins.float, m_inv_b: builtins.float, I_inv_a: mat33(f), I_inv_b: mat33(f), linear_a: vec3f, linear_b: vec3f, angular_a: vec3f, angular_b: vec3f, relaxation: builtins.float, dt: builtins.float)>
compute_linear_correction_3d: warp.context.Function  # value = <Function compute_linear_correction_3d(dx: vec3f, r1: vec3f, r2: vec3f, tf1: transformf, tf2: transformf, m_inv1: builtins.float, m_inv2: builtins.float, I_inv1: mat33(f), I_inv2: mat33(f), lambda_in: builtins.float, compliance: builtins.float, damping: builtins.float, dt: builtins.float)>
compute_positional_correction: warp.context.Function  # value = <Function compute_positional_correction(err: builtins.float, derr: builtins.float, tf_a: transformf, tf_b: transformf, m_inv_a: builtins.float, m_inv_b: builtins.float, I_inv_a: mat33(f), I_inv_b: mat33(f), linear_a: vec3f, linear_b: vec3f, angular_a: vec3f, angular_b: vec3f, lambda_in: builtins.float, compliance: builtins.float, damping: builtins.float, dt: builtins.float)>
solve_body_contact_positions: warp.context.Kernel  # value = <warp.context.Kernel object>
solve_body_joints: warp.context.Kernel  # value = <warp.context.Kernel object>
solve_particle_ground_contacts: warp.context.Kernel  # value = <warp.context.Kernel object>
solve_particle_particle_contacts: warp.context.Kernel  # value = <warp.context.Kernel object>
solve_particle_shape_contacts: warp.context.Kernel  # value = <warp.context.Kernel object>
solve_simple_body_joints: warp.context.Kernel  # value = <warp.context.Kernel object>
solve_springs: warp.context.Kernel  # value = <warp.context.Kernel object>
solve_tetrahedra: warp.context.Kernel  # value = <warp.context.Kernel object>
solve_tetrahedra2: warp.context.Kernel  # value = <warp.context.Kernel object>
update_body_velocities: warp.context.Kernel  # value = <warp.context.Kernel object>
update_joint_axis_limits: warp.context.Function  # value = <Function update_joint_axis_limits(axis: vec3f, limit_lower: builtins.float, limit_upper: builtins.float, input_limits: vector(length=6, dtype=float32))>
update_joint_axis_mode: warp.context.Function  # value = <Function update_joint_axis_mode(mode: int32, axis: vec3f, input_axis_mode: vec3i)>
update_joint_axis_target_ke_kd: warp.context.Function  # value = <Function update_joint_axis_target_ke_kd(axis: vec3f, target: builtins.float, target_ke: builtins.float, target_kd: builtins.float, input_target_ke_kd: mat33(f))>
vec_abs: warp.context.Function  # value = <Function vec_abs(a: vec3f)>
vec_leaky_max: warp.context.Function  # value = <Function vec_leaky_max(a: vec3f, b: vec3f)>
vec_leaky_min: warp.context.Function  # value = <Function vec_leaky_min(a: vec3f, b: vec3f)>
vec_max: warp.context.Function  # value = <Function vec_max(a: vec3f, b: vec3f)>
vec_min: warp.context.Function  # value = <Function vec_min(a: vec3f, b: vec3f)>
velocity_at_point: warp.context.Function  # value = <Function velocity_at_point(qd: vector(length=6, dtype=float32), r: vec3f)>
