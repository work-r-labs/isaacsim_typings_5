from __future__ import annotations
import warp as wp
import warp.context
__all__: list[str] = ['compute_2d_rotational_dofs', 'compute_3d_rotational_dofs', 'eval_articulation_fk', 'eval_articulation_ik', 'eval_fk', 'eval_ik', 'eval_single_articulation_fk', 'invert_2d_rotational_dofs', 'invert_3d_rotational_dofs', 'quat_decompose', 'quat_twist', 'reconstruct_angular_q_qd', 'wp']
def eval_fk(model, joint_q, joint_qd, mask, state):
    """
    
        Evaluates the model's forward kinematics given the joint coordinates and updates the state's body information (:attr:`State.body_q` and :attr:`State.body_qd`).
    
        Args:
            model (Model): The model to evaluate.
            joint_q (array): Generalized joint position coordinates, shape [joint_coord_count], float
            joint_qd (array): Generalized joint velocity coordinates, shape [joint_dof_count], float
            mask (array): The mask to use to enable / disable FK for an articulation. If None then treat all as enabled, shape [articulation_count], int/bool
            state (State): The state to update.
        
    """
def eval_ik(model, state, joint_q, joint_qd):
    """
    
        Evaluates the model's inverse kinematics given the state's body information (:attr:`State.body_q` and :attr:`State.body_qd`) and updates the generalized joint coordinates `joint_q` and `joint_qd`.
    
        Args:
            model (Model): The model to evaluate.
            state (State): The state with the body's maximal coordinates (positions :attr:`State.body_q` and velocities :attr:`State.body_qd`) to use.
            joint_q (array): Generalized joint position coordinates, shape [joint_coord_count], float
            joint_qd (array): Generalized joint velocity coordinates, shape [joint_dof_count], float
        
    """
compute_2d_rotational_dofs: warp.context.Function  # value = <Function compute_2d_rotational_dofs(axis_0: vec3f, axis_1: vec3f, q0: builtins.float, q1: builtins.float, qd0: builtins.float, qd1: builtins.float)>
compute_3d_rotational_dofs: warp.context.Function  # value = <Function compute_3d_rotational_dofs(axis_0: vec3f, axis_1: vec3f, axis_2: vec3f, q0: builtins.float, q1: builtins.float, q2: builtins.float, qd0: builtins.float, qd1: builtins.float, qd2: builtins.float)>
eval_articulation_fk: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_articulation_ik: warp.context.Kernel  # value = <warp.context.Kernel object>
eval_single_articulation_fk: warp.context.Function  # value = <Function eval_single_articulation_fk(joint_start: builtins.int, joint_end: builtins.int, joint_q: array(ndim=1, dtype=float32), joint_qd: array(ndim=1, dtype=float32), joint_q_start: array(ndim=1, dtype=int32), joint_qd_start: array(ndim=1, dtype=int32), joint_type: array(ndim=1, dtype=int32), joint_parent: array(ndim=1, dtype=int32), joint_child: array(ndim=1, dtype=int32), joint_X_p: array(ndim=1, dtype=transformf), joint_X_c: array(ndim=1, dtype=transformf), joint_axis: array(ndim=1, dtype=vec3f), joint_axis_start: array(ndim=1, dtype=int32), joint_axis_dim: array(ndim=2, dtype=int32), body_com: array(ndim=1, dtype=vec3f), body_q: array(ndim=1, dtype=transformf), body_qd: array(ndim=1, dtype=vector(length=6, dtype=float32)))>
invert_2d_rotational_dofs: warp.context.Function  # value = <Function invert_2d_rotational_dofs(axis_0: vec3f, axis_1: vec3f, q_p: quatf, q_c: quatf, w_err: vec3f)>
invert_3d_rotational_dofs: warp.context.Function  # value = <Function invert_3d_rotational_dofs(axis_0: vec3f, axis_1: vec3f, axis_2: vec3f, q_p: quatf, q_c: quatf, w_err: vec3f)>
quat_decompose: warp.context.Function  # value = <Function quat_decompose(q: quatf)>
quat_twist: warp.context.Function  # value = <Function quat_twist(axis: vec3f, q: quatf)>
reconstruct_angular_q_qd: warp.context.Function  # value = <Function reconstruct_angular_q_qd(q_pc: quatf, w_err: vec3f, X_wp: transformf, axis: vec3f)>
