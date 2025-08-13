from __future__ import annotations
import warp as wp
import warp.context
from warp.sim.articulation import eval_fk
import warp.sim.integrator
from warp.sim.integrator import Integrator
from warp.sim.integrator_euler import eval_bending_forces
from warp.sim.integrator_euler import eval_muscle_forces
from warp.sim.integrator_euler import eval_particle_body_contact_forces
from warp.sim.integrator_euler import eval_particle_ground_contact_forces
from warp.sim.integrator_euler import eval_spring_forces
from warp.sim.integrator_euler import eval_tetrahedral_forces
from warp.sim.integrator_euler import eval_triangle_contact_forces
from warp.sim.integrator_euler import eval_triangle_forces
import warp.sim.model
from warp.sim.model import Control
from warp.sim.model import Model
from warp.sim.model import State
from warp.sim.particles import eval_particle_forces
__all__: list[str] = ['Control', 'FeatherstoneIntegrator', 'Integrator', 'Model', 'State', 'adj_dense_cholesky', 'adj_dense_solve', 'compute_2d_rotational_dofs', 'compute_3d_rotational_dofs', 'compute_com_transforms', 'compute_link_transform', 'compute_link_velocity', 'compute_spatial_inertia', 'create_batched_cholesky_kernel', 'create_inertia_matrix_cholesky_kernel', 'create_inertia_matrix_kernel', 'dense_cholesky', 'dense_gemm', 'dense_index', 'dense_solve', 'dense_subs', 'eval_bending_forces', 'eval_dense_cholesky_batched', 'eval_dense_gemm_batched', 'eval_dense_solve_batched', 'eval_fk', 'eval_joint_force', 'eval_muscle_forces', 'eval_particle_body_contact_forces', 'eval_particle_forces', 'eval_particle_ground_contact_forces', 'eval_rigid_contacts', 'eval_rigid_fk', 'eval_rigid_id', 'eval_rigid_jacobian', 'eval_rigid_mass', 'eval_rigid_tau', 'eval_spring_forces', 'eval_tetrahedral_forces', 'eval_triangle_contact_forces', 'eval_triangle_forces', 'integrate_generalized_joints', 'jcalc_integrate', 'jcalc_motion', 'jcalc_tau', 'jcalc_transform', 'spatial_adjoint', 'spatial_cross', 'spatial_cross_dual', 'spatial_mass', 'spatial_transform_inertia', 'transform_twist', 'transform_wrench', 'wp']
class FeatherstoneIntegrator(warp.sim.integrator.Integrator):
    """
    A semi-implicit integrator using symplectic Euler that operates
        on reduced (also called generalized) coordinates to simulate articulated rigid body dynamics
        based on Featherstone's composite rigid body algorithm (CRBA).
    
        See: Featherstone, Roy. Rigid Body Dynamics Algorithms. Springer US, 2014.
    
        Instead of maximal coordinates :attr:`State.body_q` (rigid body positions) and :attr:`State.body_qd`
        (rigid body velocities) as is the case :class:`SemiImplicitIntegrator`, :class:`FeatherstoneIntegrator`
        uses :attr:`State.joint_q` and :attr:`State.joint_qd` to represent the positions and velocities of
        joints without allowing any redundant degrees of freedom.
    
        After constructing :class:`Model` and :class:`State` objects this time-integrator
        may be used to advance the simulation state forward in time.
    
        Note:
            Unlike :class:`SemiImplicitIntegrator` and :class:`XPBDIntegrator`, :class:`FeatherstoneIntegrator` does not simulate rigid bodies with nonzero mass as floating bodies if they are not connected through any joints. Floating-base systems require an explicit free joint with which the body is connected to the world, see :meth:`ModelBuilder.add_joint_free`.
    
        Semi-implicit time integration is a variational integrator that
        preserves energy, however it not unconditionally stable, and requires a time-step
        small enough to support the required stiffness and damping forces.
    
        See: https://en.wikipedia.org/wiki/Semi-implicit_Euler_method
    
        Example
        -------
    
        .. code-block:: python
    
            integrator = wp.FeatherstoneIntegrator(model)
    
            # simulation loop
            for i in range(100):
                state = integrator.simulate(model, state_in, state_out, dt)
    
        Note:
            The :class:`FeatherstoneIntegrator` requires the :class:`Model` to be passed in as a constructor argument.
    
        
    """
    def __init__(self, model, angular_damping = 0.05, update_mass_matrix_every = 1, friction_smoothing = 1.0, use_tile_gemm = False, fuse_cholesky = True):
        """
        
                Args:
                    model (Model): the model to be simulated.
                    angular_damping (float, optional): Angular damping factor. Defaults to 0.05.
                    update_mass_matrix_every (int, optional): How often to update the mass matrix (every n-th time the :meth:`simulate` function gets called). Defaults to 1.
                    friction_smoothing (float, optional): The delta value for the Huber norm (see :func:`warp.math.norm_huber`) used for the friction velocity normalization. Defaults to 1.0.
                
        """
    def allocate_model_aux_vars(self, model):
        ...
    def allocate_state_aux_vars(self, model, target, requires_grad):
        ...
    def compute_articulation_indices(self, model):
        ...
    def simulate(self, model: warp.sim.model.Model, state_in: warp.sim.model.State, state_out: warp.sim.model.State, dt: float, control: warp.sim.model.Control = None):
        ...
def adj_dense_cholesky(n: int, A: array(ndim=1, dtype=float32), R: array(ndim=1, dtype=float32), A_start: int, R_start: int, L: array(ndim=1, dtype=float32)):
    ...
def adj_dense_solve(n: int, L_start: int, b_start: int, A: array(ndim=1, dtype=float32), L: array(ndim=1, dtype=float32), b: array(ndim=1, dtype=float32), x: array(ndim=1, dtype=float32), tmp: array(ndim=1, dtype=float32)):
    ...
def create_batched_cholesky_kernel(num_dofs):
    ...
def create_inertia_matrix_cholesky_kernel(num_joints, num_dofs):
    ...
def create_inertia_matrix_kernel(num_joints, num_dofs):
    ...
compute_2d_rotational_dofs: warp.context.Function  # value = <Function compute_2d_rotational_dofs(axis_0: vec3f, axis_1: vec3f, q0: builtins.float, q1: builtins.float, qd0: builtins.float, qd1: builtins.float)>
compute_3d_rotational_dofs: warp.context.Function  # value = <Function compute_3d_rotational_dofs(axis_0: vec3f, axis_1: vec3f, axis_2: vec3f, q0: builtins.float, q1: builtins.float, q2: builtins.float, qd0: builtins.float, qd1: builtins.float, qd2: builtins.float)>
compute_com_transforms: warp.context.Kernel  # value = <warp.context.Kernel object>
compute_link_transform: warp.context.Function  # value = <Function compute_link_transform(i: builtins.int, joint_type: array(ndim=1, dtype=int32), joint_parent: array(ndim=1, dtype=int32), joint_child: array(ndim=1, dtype=int32), joint_q_start: array(ndim=1, dtype=int32), joint_q: array(ndim=1, dtype=float32), joint_X_p: array(ndim=1, dtype=transformf), joint_X_c: array(ndim=1, dtype=transformf), body_X_com: array(ndim=1, dtype=transformf), joint_axis: array(ndim=1, dtype=vec3f), joint_axis_start: array(ndim=1, dtype=int32), joint_axis_dim: array(ndim=2, dtype=int32), body_q: array(ndim=1, dtype=transformf), body_q_com: array(ndim=1, dtype=transformf))>
compute_link_velocity: warp.context.Function  # value = <Function compute_link_velocity(i: builtins.int, joint_type: array(ndim=1, dtype=int32), joint_parent: array(ndim=1, dtype=int32), joint_child: array(ndim=1, dtype=int32), joint_q_start: array(ndim=1, dtype=int32), joint_qd_start: array(ndim=1, dtype=int32), joint_q: array(ndim=1, dtype=float32), joint_qd: array(ndim=1, dtype=float32), joint_axis: array(ndim=1, dtype=vec3f), joint_axis_start: array(ndim=1, dtype=int32), joint_axis_dim: array(ndim=2, dtype=int32), body_I_m: array(ndim=1, dtype=matrix(shape=(6, 6), dtype=float32)), body_q: array(ndim=1, dtype=transformf), body_q_com: array(ndim=1, dtype=transformf), joint_X_p: array(ndim=1, dtype=transformf), joint_X_c: array(ndim=1, dtype=transformf), gravity: vec3f, joint_S_s: array(ndim=1, dtype=vector(length=6, dtype=float32)), body_I_s: array(ndim=1, dtype=matrix(shape=(6, 6), dtype=float32)), body_v_s: array(ndim=1, dtype=vector(length=6, dtype=float32)), body_f_s: array(ndim=1, dtype=vector(length=6, dtype=float32)), body_a_s: array(ndim=1, dtype=vector(length=6, dtype=float32)))>
compute_spatial_inertia: warp.context.Kernel  # value = <warp.context.Kernel object>
dense_cholesky: warp.context.Function  # value = <Function dense_cholesky(n: builtins.int, A: array(ndim=1, dtype=float32), R: array(ndim=1, dtype=float32), A_start: builtins.int, R_start: builtins.int, L: array(ndim=1, dtype=float32))>
dense_gemm: warp.context.Function  # value = <Function dense_gemm(m: builtins.int, n: builtins.int, p: builtins.int, transpose_A: builtins.bool, transpose_B: builtins.bool, add_to_C: builtins.bool, A_start: builtins.int, B_start: builtins.int, C_start: builtins.int, A: array(ndim=1, dtype=float32), B: array(ndim=1, dtype=float32), C: array(ndim=1, dtype=float32))>
dense_index: warp.context.Function  # value = <Function dense_index(stride: builtins.int, i: builtins.int, j: builtins.int)>
dense_solve: warp.context.Function  # value = <Function dense_solve(n: builtins.int, L_start: builtins.int, b_start: builtins.int, A: array(ndim=1, dtype=float32), L: array(ndim=1, dtype=float32), b: array(ndim=1, dtype=float32), x: array(ndim=1, dtype=float32), tmp: array(ndim=1, dtype=float32))>
dense_subs: warp.context.Function  # value = <Function dense_subs(n: builtins.int, L_start: builtins.int, b_start: builtins.int, L: array(ndim=1, dtype=float32), b: array(ndim=1, dtype=float32), x: array(ndim=1, dtype=float32))>
eval_dense_cholesky_batched: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_dense_gemm_batched: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_dense_solve_batched: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_joint_force: warp.context.Function  # value = <Function eval_joint_force(q: builtins.float, qd: builtins.float, act: builtins.float, target_ke: builtins.float, target_kd: builtins.float, limit_lower: builtins.float, limit_upper: builtins.float, limit_ke: builtins.float, limit_kd: builtins.float, mode: int32)>
eval_rigid_contacts: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_rigid_fk: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_rigid_id: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_rigid_jacobian: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_rigid_mass: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_rigid_tau: warp.context.Kernel  # value = <warp.context.Kernel object>
integrate_generalized_joints: warp.context.Kernel  # value = <warp.context.Kernel object>
jcalc_integrate: warp.context.Function  # value = <Function jcalc_integrate(type: builtins.int, joint_q: array(ndim=1, dtype=float32), joint_qd: array(ndim=1, dtype=float32), joint_qdd: array(ndim=1, dtype=float32), coord_start: builtins.int, dof_start: builtins.int, lin_axis_count: builtins.int, ang_axis_count: builtins.int, dt: builtins.float, joint_q_new: array(ndim=1, dtype=float32), joint_qd_new: array(ndim=1, dtype=float32))>
jcalc_motion: warp.context.Function  # value = <Function jcalc_motion(type: builtins.int, joint_axis: array(ndim=1, dtype=vec3f), axis_start: builtins.int, lin_axis_count: builtins.int, ang_axis_count: builtins.int, X_sc: transformf, joint_q: array(ndim=1, dtype=float32), joint_qd: array(ndim=1, dtype=float32), q_start: builtins.int, qd_start: builtins.int, joint_S_s: array(ndim=1, dtype=vector(length=6, dtype=float32)))>
jcalc_tau: warp.context.Function  # value = <Function jcalc_tau(type: builtins.int, joint_target_ke: array(ndim=1, dtype=float32), joint_target_kd: array(ndim=1, dtype=float32), joint_limit_ke: array(ndim=1, dtype=float32), joint_limit_kd: array(ndim=1, dtype=float32), joint_S_s: array(ndim=1, dtype=vector(length=6, dtype=float32)), joint_q: array(ndim=1, dtype=float32), joint_qd: array(ndim=1, dtype=float32), joint_act: array(ndim=1, dtype=float32), joint_axis_mode: array(ndim=1, dtype=int32), joint_limit_lower: array(ndim=1, dtype=float32), joint_limit_upper: array(ndim=1, dtype=float32), coord_start: builtins.int, dof_start: builtins.int, axis_start: builtins.int, lin_axis_count: builtins.int, ang_axis_count: builtins.int, body_f_s: vector(length=6, dtype=float32), tau: array(ndim=1, dtype=float32))>
jcalc_transform: warp.context.Function  # value = <Function jcalc_transform(type: builtins.int, joint_axis: array(ndim=1, dtype=vec3f), axis_start: builtins.int, lin_axis_count: builtins.int, ang_axis_count: builtins.int, joint_q: array(ndim=1, dtype=float32), start: builtins.int)>
spatial_adjoint: warp.context.Function  # value = <Function spatial_adjoint(R: mat33(f), S: mat33(f))>
spatial_cross: warp.context.Function  # value = <Function spatial_cross(a: vector(length=6, dtype=float32), b: vector(length=6, dtype=float32))>
spatial_cross_dual: warp.context.Function  # value = <Function spatial_cross_dual(a: vector(length=6, dtype=float32), b: vector(length=6, dtype=float32))>
spatial_mass: warp.context.Function  # value = <Function spatial_mass(body_I_s: array(ndim=1, dtype=matrix(shape=(6, 6), dtype=float32)), joint_start: builtins.int, joint_count: builtins.int, M_start: builtins.int, M: array(ndim=1, dtype=float32))>
spatial_transform_inertia: warp.context.Function  # value = <Function spatial_transform_inertia(t: transformf, I: matrix(shape=(6, 6), dtype=float32))>
transform_twist: warp.context.Function  # value = <Function transform_twist(t: transformf, x: vector(length=6, dtype=float32))>
transform_wrench: warp.context.Function  # value = <Function transform_wrench(t: transformf, x: vector(length=6, dtype=float32))>
