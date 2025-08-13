from __future__ import annotations
import numpy as np
import re as re
import warp as wp
__all__: list[str] = ['np', 'parse_usd', 're', 'resolve_usd_from_url', 'wp']
def parse_usd(source, builder, default_density = 1000.0, only_load_enabled_rigid_bodies = False, only_load_enabled_joints = True, contact_ke = 100000.0, contact_kd = 250.0, contact_kf = 500.0, contact_ka = 0.0, contact_mu = 0.6, contact_restitution = 0.0, contact_thickness = 0.0, joint_limit_ke = 100.0, joint_limit_kd = 10.0, armature = 0.0, invert_rotations = False, verbose = False, ignore_paths = None):
    """
    
        Parses a Universal Scene Description (USD) stage containing UsdPhysics schema definitions for rigid-body articulations and adds the bodies, shapes and joints to the given ModelBuilder.
    
        The USD description has to be either a path (file name or URL), or an existing USD stage instance that implements the `UsdStage <https://openusd.org/dev/api/class_usd_stage.html>`_ interface.
    
        Args:
            source (str | pxr.UsdStage): The file path to the USD file, or an existing USD stage instance.
            builder (ModelBuilder): The :class:`ModelBuilder` to add the bodies and joints to.
            default_density (float): The default density to use for bodies without a density attribute.
            only_load_enabled_rigid_bodies (bool): If True, only rigid bodies which do not have `physics:rigidBodyEnabled` set to False are loaded.
            only_load_enabled_joints (bool): If True, only joints which do not have `physics:jointEnabled` set to False are loaded.
            contact_ke (float): The default contact stiffness to use, only considered by the Euler integrators.
            contact_kd (float): The default contact damping to use, only considered by the Euler integrators.
            contact_kf (float): The default friction stiffness to use, only considered by the Euler integrators.
            contact_ka (float): The default adhesion distance to use, only considered by the Euler integrators.
            contact_mu (float): The default friction coefficient to use if a shape has not friction coefficient defined.
            contact_restitution (float): The default coefficient of restitution to use if a shape has not coefficient of restitution defined.
            contact_thickness (float): The thickness to add to the shape geometry.
            joint_limit_ke (float): The default stiffness to use for joint limits, only considered by the Euler integrators.
            joint_limit_kd (float): The default damping to use for joint limits, only considered by the Euler integrators.
            armature (float): The armature to use for the bodies.
            invert_rotations (bool): If True, inverts any rotations defined in the shape transforms.
            verbose (bool): If True, print additional information about the parsed USD file.
            ignore_paths (List[str]): A list of regular expressions matching prim paths to ignore.
    
        Returns:
            dict: Dictionary with the following entries:
    
            .. list-table::
                :widths: 25 75
    
                * - "fps"
                  - USD stage frames per second
                * - "duration"
                  - Difference between end time code and start time code of the USD stage
                * - "up_axis"
                  - Upper-case string of the stage's up axis ("X", "Y", or "Z")
                * - "path_shape_map"
                  - Mapping from prim path (str) of the UsdGeom to the respective shape index in :class:`ModelBuilder`
                * - "path_body_map"
                  - Mapping from prim path (str) of a rigid body prim (e.g. that implements the PhysicsRigidBodyAPI) to the respective body index in :class:`ModelBuilder`
                * - "path_shape_scale"
                  - Mapping from prim path (str) of the UsdGeom to its respective 3D world scale
                * - "mass_unit"
                  - The stage's Kilograms Per Unit (KGPU) definition (1.0 by default)
                * - "linear_unit"
                  - The stage's Meters Per Unit (MPU) definition (1.0 by default)
    
    
        Note:
            This importer is experimental and only supports a subset of the USD Physics schema. Please report any issues you encounter.
        
    """
def resolve_usd_from_url(url: str, target_folder_name: str = None, export_usda: bool = False):
    """
    
        Downloads a USD file from a URL and resolves all references to other USD files to be downloaded to the given target folder.
    
        Args:
            url (str): URL to the USD file.
            target_folder_name (str): Target folder name. If None, a timestamped folder will be created in the current directory.
            export_usda (bool): If True, converts each downloaded USD file to USDA and saves the additional USDA file in the target folder with the same base name as the original USD file.
    
        Returns:
            str: File path to the downloaded USD file.
        
    """
