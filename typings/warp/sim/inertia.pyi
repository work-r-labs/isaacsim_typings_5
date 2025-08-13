"""
Helper functions for computing rigid body inertia properties.
"""
from __future__ import annotations
import numpy as np
import typing
import warp as wp
import warp.context
__all__: list[str] = ['compute_box_inertia', 'compute_capsule_inertia', 'compute_cone_inertia', 'compute_cylinder_inertia', 'compute_hollow_mesh_inertia', 'compute_mesh_inertia', 'compute_solid_mesh_inertia', 'compute_sphere_inertia', 'np', 'transform_inertia', 'triangle_inertia', 'wp']
def compute_box_inertia(density: float, w: float, h: float, d: float) -> tuple[float, wp.vec3, wp.mat33]:
    """
    Helper to compute mass and inertia of a solid box
    
        Args:
            density: The box density
            w: The box width along the x-axis
            h: The box height along the y-axis
            d: The box depth along the z-axis
    
        Returns:
    
            A tuple of (mass, inertia) with inertia specified around the origin
        
    """
def compute_capsule_inertia(density: float, r: float, h: float) -> tuple[float, wp.vec3, wp.mat33]:
    """
    Helper to compute mass and inertia of a solid capsule extending along the y-axis
    
        Args:
            density: The capsule density
            r: The capsule radius
            h: The capsule height (full height of the interior cylinder)
    
        Returns:
    
            A tuple of (mass, inertia) with inertia specified around the origin
        
    """
def compute_cone_inertia(density: float, r: float, h: float) -> tuple[float, wp.vec3, wp.mat33]:
    """
    Helper to compute mass and inertia of a solid cone extending along the y-axis
    
        Args:
            density: The cone density
            r: The cone radius
            h: The cone height (extent along the y-axis)
    
        Returns:
    
            A tuple of (mass, inertia) with inertia specified around the origin
        
    """
def compute_cylinder_inertia(density: float, r: float, h: float) -> tuple[float, wp.vec3, wp.mat33]:
    """
    Helper to compute mass and inertia of a solid cylinder extending along the y-axis
    
        Args:
            density: The cylinder density
            r: The cylinder radius
            h: The cylinder height (extent along the y-axis)
    
        Returns:
    
            A tuple of (mass, inertia) with inertia specified around the origin
        
    """
def compute_mesh_inertia(density: float, vertices: list, indices: list, is_solid: bool = True, thickness: list[float] | float = 0.001) -> tuple[float, wp.vec3, wp.mat33, float]:
    """
    
        Compute the mass, center of mass, inertia, and volume of a triangular mesh.
    
        Args:
            density: The density of the mesh material.
            vertices: A list of vertex positions (3D coordinates).
            indices: A list of triangle indices (each triangle is defined by 3 vertex indices).
            is_solid: If True, compute inertia for a solid mesh; if False, for a hollow mesh using the given thickness.
            thickness: Thickness of the mesh if it is hollow. Can be a single value or a list of values for each vertex.
    
        Returns:
            A tuple containing:
                - mass: The mass of the mesh.
                - com: The center of mass (3D coordinates).
                - I: The inertia tensor (3x3 matrix).
                - volume: The signed volume of the mesh.
        
    """
def compute_sphere_inertia(density: float, r: float) -> tuple[float, wp.vec3, wp.mat33]:
    """
    Helper to compute mass and inertia of a solid sphere
    
        Args:
            density: The sphere density
            r: The sphere radius
    
        Returns:
    
            A tuple of (mass, inertia) with inertia specified around the origin
        
    """
def transform_inertia(m, I, p, q) -> wp.mat33:
    ...
compute_hollow_mesh_inertia: warp.context.Kernel  # value = <warp.context.Kernel object>
compute_solid_mesh_inertia: warp.context.Kernel  # value = <warp.context.Kernel object>
triangle_inertia: warp.context.Function  # value = <Function triangle_inertia(v0: vec3f, v1: vec3f, v2: vec3f)>
