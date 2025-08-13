from __future__ import annotations
import warp as wp
import warp.context
import warp.types
__all__: list[str] = ['PARTICLE_FLAG_ACTIVE', 'eval_particle_forces', 'eval_particle_forces_kernel', 'particle_force', 'wp']
def eval_particle_forces(model, state, forces):
    ...
PARTICLE_FLAG_ACTIVE: warp.types.uint32  # value = <warp.types.uint32 object>
eval_particle_forces_kernel: warp.context.Kernel  # value = <warp.context.Kernel object>
particle_force: warp.context.Function  # value = <Function particle_force(n: vec3f, v: vec3f, c: builtins.float, k_n: builtins.float, k_d: builtins.float, k_f: builtins.float, k_mu: builtins.float)>
