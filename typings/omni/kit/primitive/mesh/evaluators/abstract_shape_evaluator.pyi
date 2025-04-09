from __future__ import annotations
from pxr import Gf
__all__ = ['AbstractShapeEvaluator', 'Gf']
class AbstractShapeEvaluator:
    """
    A base class for evaluating geometric shapes.
    
        This abstract class serves as a template for creating shape evaluators. Subclasses are expected to implement the `eval` method, which calculates geometric data for a given shape based on provided attributes.
    
        Args:
            attributes (dict): A dictionary containing shape-specific attributes needed for evaluation.
    """
    @staticmethod
    def build_setting_ui():
        """
        Builds the UI for setting configurations. This method should be implemented by subclasses.
        """
    @staticmethod
    def get_default_half_scale():
        """
        Returns the default half scale value.
        
                Returns:
                    int: The default half scale value.
        """
    @staticmethod
    def reset_setting():
        """
        Resets the settings to their default values. This method should be implemented by subclasses.
        """
    def __init__(self, attributes: dict):
        """
        Initializes an instance of the AbstractShapeEvaluator.
        """
    def eval(self, **kwargs) -> typing.Tuple[typing.List[pxr.Gf.Vec3f], typing.List[pxr.Gf.Vec3f], typing.List[pxr.Gf.Vec2f], typing.List[int], typing.List[int]]:
        """
        It must be implemented to return tuple
                [points, normals, uvs, face_indices, face_vertex_counts], where:
                * points and normals are array of Gf.Vec3f.
                * uvs are array of Gf.Vec2f that represents uv coordinates.
                * face_indexes are array of int that represents face indices.
                * face_vertex_counts are array of int that represents vertex count per face.
                * Normals and uvs must be face varying.
        
                Keyword Args:
                    **kwargs: Arbitrary keyword arguments.
        
                Returns:
                    Tuple[List[Gf.Vec3f], List[Gf.Vec3f], List[Gf.Vec2f], List[int], List[int]]: Tuple containing lists of points, normals, uvs, face_indices, and face_vertex_counts.
                
        """
