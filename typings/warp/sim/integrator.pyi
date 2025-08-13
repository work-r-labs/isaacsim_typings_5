from __future__ import annotations
import warp as wp
import warp.context
import warp.sim.model
from warp.sim.model import Control
from warp.sim.model import Model
from warp.sim.model import State
import warp.types
__all__: list[str] = ['Control', 'Integrator', 'Model', 'PARTICLE_FLAG_ACTIVE', 'State', 'integrate_bodies', 'integrate_particles', 'integrate_rigid_body', 'wp']
class Integrator:
    """
    
        Generic base class for integrators. Provides methods to integrate rigid bodies and particles.
        
    """
    def integrate_bodies(self, model: warp.sim.model.Model, state_in: warp.sim.model.State, state_out: warp.sim.model.State, dt: float, angular_damping: float = 0.0):
        """
        
                Integrate the rigid bodies of the model.
        
                Args:
                    model (Model): The model to integrate.
                    state_in (State): The input state.
                    state_out (State): The output state.
                    dt (float): The time step (typically in seconds).
                    angular_damping (float, optional): The angular damping factor. Defaults to 0.0.
                
        """
    def integrate_particles(self, model: warp.sim.model.Model, state_in: warp.sim.model.State, state_out: warp.sim.model.State, dt: float):
        """
        
                Integrate the particles of the model.
        
                Args:
                    model (Model): The model to integrate.
                    state_in (State): The input state.
                    state_out (State): The output state.
                    dt (float): The time step (typically in seconds).
                
        """
    def simulate(self, model: warp.sim.model.Model, state_in: warp.sim.model.State, state_out: warp.sim.model.State, dt: float, control: warp.sim.model.Control = None):
        """
        
                Simulate the model for a given time step using the given control input.
        
                Args:
                    model (Model): The model to simulate.
                    state_in (State): The input state.
                    state_out (State): The output state.
                    dt (float): The time step (typically in seconds).
                    control (Control): The control input. Defaults to `None` which means the control values from the :class:`Model` are used.
                
        """
PARTICLE_FLAG_ACTIVE: warp.types.uint32  # value = <warp.types.uint32 object>
integrate_bodies: warp.context.Kernel  # value = <warp.context.Kernel object>
integrate_particles: warp.context.Kernel  # value = <warp.context.Kernel object>
integrate_rigid_body: warp.context.Function  # value = <Function integrate_rigid_body(q: transformf, qd: vector(length=6, dtype=float32), f: vector(length=6, dtype=float32), com: vec3f, inertia: mat33(f), inv_mass: builtins.float, inv_inertia: mat33(f), gravity: vec3f, angular_damping: builtins.float, dt: builtins.float)>
