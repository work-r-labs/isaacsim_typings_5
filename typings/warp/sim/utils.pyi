from __future__ import annotations
import numpy as np
import warp as wp
import warp.context
__all__: list[str] = ['boltzmann', 'leaky_max', 'leaky_min', 'load_mesh', 'np', 'quat_decompose', 'quat_from_euler', 'quat_to_euler', 'quat_to_rpy', 'quat_twist', 'quat_twist_angle', 'smooth_max', 'smooth_min', 'transform_inertia', 'transform_twist', 'transform_wrench', 'vec_abs', 'vec_leaky_max', 'vec_leaky_min', 'vec_max', 'vec_min', 'velocity_at_point', 'visualize_meshes', 'wp']
def load_mesh(filename: str, method: str = None):
    """
    
        Loads a 3D triangular surface mesh from a file.
    
        Args:
            filename (str): The path to the 3D model file (obj, and other formats supported by the different methods) to load.
            method (str): The method to use for loading the mesh (default None). Can be either `"trimesh"`, `"meshio"`, `"pcu"`, or `"openmesh"`. If None, every method is tried and the first successful mesh import where the number of vertices is greater than 0 is returned.
    
        Returns:
            Tuple of (mesh_points, mesh_indices), where mesh_points is a Nx3 numpy array of vertex positions (float32),
            and mesh_indices is a Mx3 numpy array of vertex indices (int32) for the triangular faces.
        
    """
def visualize_meshes(meshes: typing.List[typing.Tuple[list, list]], num_cols = 0, num_rows = 0, titles = None, scale_axes = True, show_plot = True):
    ...
boltzmann: warp.context.Function  # value = <Function boltzmann(a: builtins.float, b: builtins.float, alpha: builtins.float)>
leaky_max: warp.context.Function  # value = <Function leaky_max(a: builtins.float, b: builtins.float)>
leaky_min: warp.context.Function  # value = <Function leaky_min(a: builtins.float, b: builtins.float)>
quat_decompose: warp.context.Function  # value = <Function quat_decompose(q: quatf)>
quat_from_euler: warp.context.Function  # value = <Function quat_from_euler(e: vec3f, i: builtins.int, j: builtins.int, k: builtins.int)>
quat_to_euler: warp.context.Function  # value = <Function quat_to_euler(q: quatf, i: builtins.int, j: builtins.int, k: builtins.int)>
quat_to_rpy: warp.context.Function  # value = <Function quat_to_rpy(q: quatf)>
quat_twist: warp.context.Function  # value = <Function quat_twist(axis: vec3f, q: quatf)>
quat_twist_angle: warp.context.Function  # value = <Function quat_twist_angle(axis: vec3f, q: quatf)>
smooth_max: warp.context.Function  # value = <Function smooth_max(a: builtins.float, b: builtins.float, eps: builtins.float)>
smooth_min: warp.context.Function  # value = <Function smooth_min(a: builtins.float, b: builtins.float, eps: builtins.float)>
transform_inertia: warp.context.Function  # value = <Function transform_inertia(t: transformf, I: matrix(shape=(6, 6), dtype=float32))>
transform_twist: warp.context.Function  # value = <Function transform_twist(t: transformf, x: vector(length=6, dtype=float32))>
transform_wrench: warp.context.Function  # value = <Function transform_wrench(t: transformf, x: vector(length=6, dtype=float32))>
vec_abs: warp.context.Function  # value = <Function vec_abs(a: vec3f)>
vec_leaky_max: warp.context.Function  # value = <Function vec_leaky_max(a: vec3f, b: vec3f)>
vec_leaky_min: warp.context.Function  # value = <Function vec_leaky_min(a: vec3f, b: vec3f)>
vec_max: warp.context.Function  # value = <Function vec_max(a: vec3f, b: vec3f)>
vec_min: warp.context.Function  # value = <Function vec_min(a: vec3f, b: vec3f)>
velocity_at_point: warp.context.Function  # value = <Function velocity_at_point(qd: vector(length=6, dtype=float32), r: vec3f)>
