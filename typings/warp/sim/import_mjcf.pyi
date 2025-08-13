from __future__ import annotations
import math as math
import numpy as np
import os as os
import re as re
import warp as wp
from warp.sim.model import Mesh
from xml.etree import ElementTree as ET
__all__: list[str] = ['ET', 'Mesh', 'math', 'np', 'os', 'parse_mjcf', 're', 'wp']
def parse_mjcf(mjcf_filename, builder, xform = None, floating = False, base_joint: typing.Union[dict, str, NoneType] = None, density = 1000.0, stiffness = 100.0, damping = 10.0, armature = 0.0, armature_scale = 1.0, contact_ke = 10000.0, contact_kd = 1000.0, contact_kf = 100.0, contact_ka = 0.0, contact_mu = 0.25, contact_restitution = 0.5, contact_thickness = 0.0, limit_ke = 100.0, limit_kd = 10.0, joint_limit_lower = -1000000.0, joint_limit_upper = 1000000.0, scale = 1.0, hide_visuals = False, parse_visuals_as_colliders = False, parse_meshes = True, up_axis = 'Z', ignore_names = tuple(), ignore_classes = None, visual_classes = ('visual'), collider_classes = ('collision'), no_class_as_colliders = True, force_show_colliders = False, enable_self_collisions = False, ignore_inertial_definitions = True, ensure_nonstatic_links = True, static_link_mass = 0.01, collapse_fixed_joints = False, verbose = False):
    """
    
        Parses MuJoCo XML (MJCF) file and adds the bodies and joints to the given ModelBuilder.
    
        Args:
            mjcf_filename (str): The filename of the MuJoCo file to parse.
            builder (ModelBuilder): The :class:`ModelBuilder` to add the bodies and joints to.
            xform (:ref:`transform <transform>`): The transform to apply to the imported mechanism.
            floating (bool): If True, the root body is a free joint. If False, the root body is connected via a fixed joint to the world, unless a `base_joint` is defined.
            base_joint (Union[str, dict]): The joint by which the root body is connected to the world. This can be either a string defining the joint axes of a D6 joint with comma-separated positional and angular axis names (e.g. "px,py,rz" for a D6 joint with linear axes in x, y and an angular axis in z) or a dict with joint parameters (see :meth:`ModelBuilder.add_joint`).
            density (float): The density of the shapes in kg/m^3 which will be used to calculate the body mass and inertia.
            stiffness (float): The stiffness of the joints.
            damping (float): The damping of the joints.
            armature (float): Default joint armature to use if `armature` has not been defined for a joint in the MJCF.
            armature_scale (float): Scaling factor to apply to the MJCF-defined joint armature values.
            contact_ke (float): The stiffness of the shape contacts.
            contact_kd (float): The damping of the shape contacts.
            contact_kf (float): The friction stiffness of the shape contacts.
            contact_ka (float): The adhesion distance of the shape contacts.
            contact_mu (float): The friction coefficient of the shape contacts.
            contact_restitution (float): The restitution coefficient of the shape contacts.
            contact_thickness (float): The thickness to add to the shape geometry.
            limit_ke (float): The stiffness of the joint limits.
            limit_kd (float): The damping of the joint limits.
            joint_limit_lower (float): The default lower joint limit if not specified in the MJCF.
            joint_limit_upper (float): The default upper joint limit if not specified in the MJCF.
            scale (float): The scaling factor to apply to the imported mechanism.
            hide_visuals (bool): If True, hide visual shapes.
            parse_visuals_as_colliders (bool): If True, the geometry defined under the `visual_classes` tags is used for collision handling instead of the `collider_classes` geometries.
            parse_meshes (bool): Whether geometries of type `"mesh"` should be parsed. If False, geometries of type `"mesh"` are ignored.
            up_axis (str): The up axis of the mechanism. Can be either `"X"`, `"Y"` or `"Z"`. The default is `"Z"`.
            ignore_names (List[str]): A list of regular expressions. Bodies and joints with a name matching one of the regular expressions will be ignored.
            ignore_classes (List[str]): A list of regular expressions. Bodies and joints with a class matching one of the regular expressions will be ignored.
            visual_classes (List[str]): A list of regular expressions. Visual geometries with a class matching one of the regular expressions will be parsed.
            collider_classes (List[str]): A list of regular expressions. Collision geometries with a class matching one of the regular expressions will be parsed.
            no_class_as_colliders: If True, geometries without a class are parsed as collision geometries. If False, geometries without a class are parsed as visual geometries.
            force_show_colliders (bool): If True, the collision shapes are always shown, even if there are visual shapes.
            enable_self_collisions (bool): If True, self-collisions are enabled.
            ignore_inertial_definitions (bool): If True, the inertial parameters defined in the MJCF are ignored and the inertia is calculated from the shape geometry.
            ensure_nonstatic_links (bool): If True, links with zero mass are given a small mass (see `static_link_mass`) to ensure they are dynamic.
            static_link_mass (float): The mass to assign to links with zero mass (if `ensure_nonstatic_links` is set to True).
            collapse_fixed_joints (bool): If True, fixed joints are removed and the respective bodies are merged.
            verbose (bool): If True, print additional information about parsing the MJCF.
        
    """
