from __future__ import annotations
import enum
from enum import Enum
import numpy as np
import typing
import warp as wp
import warp as warp
__all__: list[str] = ['ColoringAlgorithm', 'Enum', 'color_graph', 'color_trimesh', 'combine_independent_particle_coloring', 'construct_trimesh_graph_edges', 'construct_trimesh_graph_edges_kernel', 'convert_to_color_groups', 'count_color_group_size', 'fill_color_groups', 'np', 'validate_graph_coloring', 'warp', 'wp']
class ColoringAlgorithm(enum.Enum):
    GREEDY: typing.ClassVar[ColoringAlgorithm]  # value = <ColoringAlgorithm.GREEDY: 1>
    MCS: typing.ClassVar[ColoringAlgorithm]  # value = <ColoringAlgorithm.MCS: 0>
def color_graph(num_nodes, graph_edge_indices, balance_colors = True, target_max_min_color_ratio = 1.1, algorithm: ColoringAlgorithm = ...):
    """
    
        A function that generates coloring for a graph, which is represented by the number of nodes and an array of edges.
        It returns a list of `np.array` with `dtype`=`int`. The length of the list is the number of colors
        and each `np.array` contains the indices of vertices with this color.
    
        Args:
            num_nodes: The number of the nodes in the graph
            graph_edge_indices: A `wp.array` with of shape (number_edges, 2)
            balance_colors: Whether to apply the color balancing algorithm to balance the size of each color
            target_max_min_color_ratio: the color balancing algorithm will stop when the ratio between the largest color and
                the smallest color reaches this value
            algorithm: Value should an enum type of ColoringAlgorithm, otherwise it will raise an error. ColoringAlgorithm.mcs means using the MCS coloring algorithm,
                while ColoringAlgorithm.ordered_greedy means using the degree-ordered greedy algorithm. The MCS algorithm typically generates 30% to 50% fewer colors
                compared to the ordered greedy algorithm, while maintaining the same linear complexity. Although MCS has a constant overhead that makes it about twice
                as slow as the greedy algorithm, it produces significantly better coloring results. We recommend using MCS, especially if coloring is only part of the
                preprocessing stage.e.
    
        Note:
    
            References to the coloring algorithm:
            MCS: Pereira, F. M. Q., & Palsberg, J. (2005, November). Register allocation via coloring of chordal graphs. In Asian Symposium on Programming Languages and Systems (pp. 315-329). Berlin, Heidelberg: Springer Berlin Heidelberg.
            Ordered Greedy: Ton-That, Q. M., Kry, P. G., & Andrews, S. (2023). Parallel block Neo-Hookean XPBD using graph clustering. Computers & Graphics, 110, 1-10.
        
    """
def color_trimesh(num_nodes, trimesh_edge_indices, include_bending_energy, balance_colors = True, target_max_min_color_ratio = 1.1, algorithm: ColoringAlgorithm = ...):
    """
    
        A function that generates vertex coloring for a trimesh, which is represented by the number of vertices and edges of the mesh.
        It will convert the trimesh to a graph and then apply coloring.
        It returns a list of `np.array` with `dtype`=`int`. The length of the list is the number of colors
        and each `np.array` contains the indices of vertices with this color.
    
        Args:
            num_nodes: The number of the nodes in the graph
            trimesh_edge_indices: A `wp.array` with of shape (number_edges, 4), each row is (o1, o2, v1, v2), see `sim.Model`'s definition of `edge_indices`.
            include_bending_energy: whether to consider bending energy in the coloring process. If set to `True`, the generated
                graph will contain all the edges connecting o1 and o2; otherwise, the graph will be equivalent to the trimesh.
            balance_colors: the parameter passed to `color_graph`, see `color_graph`'s document
            target_max_min_color_ratio: the parameter passed to `color_graph`, see `color_graph`'s document
            algorithm: the parameter passed to `color_graph`, see `color_graph`'s document
    
        
    """
def combine_independent_particle_coloring(color_groups_1, color_groups_2):
    """
    
        A function that combines 2 independent coloring groups. Note that color_groups_1 and color_groups_2 must be from 2 independent
        graphs so that there is no connection between them. This algorithm will sort color_groups_1 in ascending order and
        sort color_groups_2 in descending order, and combine each group with the same index, this way we are always combining
        the smaller group with the larger group.
    
        Args:
            color_groups_1: A list of `np.array` with `dtype`=`int`. The length of the list is the number of colors
                and each `np.array` contains the indices of vertices with this color.
            color_groups_2: A list of `np.array` with `dtype`=`int`. The length of the list is the number of colors
                and each `np.array` contains the indices of vertices with this color.
    
        
    """
def construct_trimesh_graph_edges(trimesh_edge_indices, return_wp_array = False):
    ...
def convert_to_color_groups(num_colors, particle_colors, return_wp_array = False, device = 'cpu'):
    ...
construct_trimesh_graph_edges_kernel: warp.context.Kernel  # value = <warp.context.Kernel object>
count_color_group_size: warp.context.Kernel  # value = <warp.context.Kernel object>
fill_color_groups: warp.context.Kernel  # value = <warp.context.Kernel object>
validate_graph_coloring: warp.context.Kernel  # value = <warp.context.Kernel object>
