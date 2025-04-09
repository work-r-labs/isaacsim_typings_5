from __future__ import annotations
__all__ = ['ARTICULATION_ATTRIBUTES', 'RIGID_PRIM_ATTRIBUTES', 'SIMULATION_CONTEXT_ATTRIBUTES', 'TENDON_ATTRIBUTES']
ARTICULATION_ATTRIBUTES: list = ['stiffness', 'damping', 'joint_friction', 'position', 'orientation', 'linear_velocity', 'angular_velocity', 'velocity', 'joint_positions', 'joint_velocities', 'lower_dof_limits', 'upper_dof_limits', 'max_efforts', 'joint_armatures', 'joint_max_velocities', 'joint_efforts', 'body_masses', 'body_inertias', 'material_properties', 'contact_offset', 'rest_offset', 'tendon_stiffnesses', 'tendon_dampings', 'tendon_limit_stiffnesses', 'tendon_lower_limits', 'tendon_upper_limits', 'tendon_rest_lengths', 'tendon_offsets']
RIGID_PRIM_ATTRIBUTES: list = ['angular_velocity', 'linear_velocity', 'velocity', 'position', 'orientation', 'force', 'mass', 'inertia', 'material_properties', 'contact_offset', 'rest_offset']
SIMULATION_CONTEXT_ATTRIBUTES: list = ['gravity']
TENDON_ATTRIBUTES: list = ['tendon_stiffnesses', 'tendon_dampings', 'tendon_limit_stiffnesses', 'tendon_lower_limits', 'tendon_upper_limits', 'tendon_rest_lengths', 'tendon_offsets']
