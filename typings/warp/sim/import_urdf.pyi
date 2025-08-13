from __future__ import annotations
import numpy as np
import os as os
import warp as wp
from warp.sim.model import Mesh
from xml.etree import ElementTree as ET
__all__: list[str] = ['ET', 'Mesh', 'np', 'os', 'parse_urdf', 'wp']
def parse_urdf(urdf_filename, builder, xform = None, floating = False, base_joint: typing.Union[dict, str, NoneType] = None, density = 1000.0, stiffness = 100.0, damping = 10.0, armature = 0.0, contact_ke = 10000.0, contact_kd = 1000.0, contact_kf = 100.0, contact_ka = 0.0, contact_mu = 0.25, contact_restitution = 0.5, contact_thickness = 0.0, limit_ke = 100.0, limit_kd = 10.0, joint_limit_lower = -1000000.0, joint_limit_upper = 1000000.0, scale = 1.0, hide_visuals = False, parse_visuals_as_colliders = False, force_show_colliders = False, enable_self_collisions = True, ignore_inertial_definitions = True, ensure_nonstatic_links = True, static_link_mass = 0.01, collapse_fixed_joints = False):
    """
    
        Parses a URDF file and adds the bodies and joints to the given ModelBuilder.
    
        Args:
            urdf_filename (str): The filename of the URDF file to parse.
            builder (ModelBuilder): The :class:`ModelBuilder` to add the bodies and joints to.
            xform (:ref:`transform <transform>`): The transform to apply to the root body.
            floating (bool): If True, the root body is a free joint. If False, the root body is connected via a fixed joint to the world, unless a `base_joint` is defined.
            base_joint (Union[str, dict]): The joint by which the root body is connected to the world. This can be either a string defining the joint axes of a D6 joint with comma-separated positional and angular axis names (e.g. "px,py,rz" for a D6 joint with linear axes in x, y and an angular axis in z) or a dict with joint parameters (see :meth:`ModelBuilder.add_joint`).
            density (float): The density of the shapes in kg/m^3 which will be used to calculate the body mass and inertia.
            stiffness (float): The stiffness of the joints.
            damping (float): The damping of the joints.
            armature (float): The armature of the joints (bias to add to the inertia diagonals that may stabilize the simulation).
            contact_ke (float): The stiffness of the shape contacts (used by the Euler integrators).
            contact_kd (float): The damping of the shape contacts (used by the Euler integrators).
            contact_kf (float): The friction stiffness of the shape contacts (used by the Euler integrators).
            contact_ka (float): The adhesion distance of the shape contacts (used by the Euler integrators).
            contact_mu (float): The friction coefficient of the shape contacts.
            contact_restitution (float): The restitution coefficient of the shape contacts.
            contact_thickness (float): The thickness to add to the shape geometry.
            limit_ke (float): The stiffness of the joint limits (used by the Euler integrators).
            limit_kd (float): The damping of the joint limits (used by the Euler integrators).
            joint_limit_lower (float): The default lower joint limit if not specified in the URDF.
            joint_limit_upper (float): The default upper joint limit if not specified in the URDF.
            scale (float): The scaling factor to apply to the imported mechanism.
            hide_visuals (bool): If True, hide visual shapes.
            parse_visuals_as_colliders (bool): If True, the geometry defined under the `<visual>` tags is used for collision handling instead of the `<collision>` geometries.
            force_show_colliders (bool): If True, the collision shapes are always shown, even if there are visual shapes.
            enable_self_collisions (bool): If True, self-collisions are enabled.
            ignore_inertial_definitions (bool): If True, the inertial parameters defined in the URDF are ignored and the inertia is calculated from the shape geometry.
            ensure_nonstatic_links (bool): If True, links with zero mass are given a small mass (see `static_link_mass`) to ensure they are dynamic.
            static_link_mass (float): The mass to assign to links with zero mass (if `ensure_nonstatic_links` is set to True).
            collapse_fixed_joints (bool): If True, fixed joints are removed and the respective bodies are merged.
        
    """
