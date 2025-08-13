from __future__ import annotations
import json as json
import numpy as np
import omni.replicator.core.scripts.utils.utils
from omni.replicator.core.scripts.utils.utils import ReplicatorItem
__all__: list[str] = ['NumpyEncoder', 'ReplicatorItem', 'calculate_truncation_ratio_simple', 'get_distribution_params', 'get_image_space_points', 'get_semantics', 'json', 'np', 'set_distribution_params']
class NumpyEncoder(json.encoder.JSONEncoder):
    def default(self, obj):
        ...
def calculate_truncation_ratio_simple(corners, img_width, img_height):
    """
    
        Calculate the truncation ratio of a cuboid using a simplified bounding box method.
        Args:
            corners: (9, 2) numpy array containing the projected corners of the cuboid.
            img_width: width of image
            img_height: height of image
    
        Returns:
            The truncation ratio of the cuboid.
            1 means object is fully truncated and 0 means object is fully within screen.
        
    """
def get_distribution_params(distribution: omni.replicator.core.scripts.utils.utils.ReplicatorItem, parameters: typing.List[str]) -> typing.List:
    """
    
        Args:
            distribution (ReplicatorItem): A replicator distribution object.
            parameters (List[str]): A list of the names of the replicator distribution parameters.
        Returns:
            List[str]: A list of the distribution parameters of the given replicator distribution object.
    
        
    """
def get_image_space_points(points, view_proj_matrix):
    """
    
        Args:
            points: numpy array of N points (N, 3) in the world space. Points will be projected into the image space.
            view_proj_matrix: Desired view projection matrix, transforming points from world frame to image space of desired camera
        Returns:
            numpy array of shape (N, 3) of points projected into the image space.
        
    """
def get_semantics(num_semantics, num_semantic_tokens, instance_semantic_map, min_semantic_idx, max_semantic_hierarchy_depth, semantic_token_map, required_semantic_types):
    ...
def set_distribution_params(distribution: omni.replicator.core.scripts.utils.utils.ReplicatorItem, parameters: typing.Dict) -> None:
    """
    
        Args:
            distribution (ReplicatorItem): The replicator distribution object to be modified.
            parameters (Dict): A dictionary where the keys are the names of the replicator
                               distribution parameters and the values are the parameter values
                               to be set.
        
    """
