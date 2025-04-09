"""
Module provides the MdlMatrixAttributeModel, an extension of MatrixBaseAttributeModel for representing non-uniform matrix attributes in USD stages.
"""
from __future__ import annotations
import omni.kit.property.usd.usd_attribute_model
from omni.kit.property.usd.usd_attribute_model import MatrixBaseAttributeModel
from omni.kit.property.usd.usd_model_base import UsdBase
from pxr import Sdf
import pxr.Usd
from pxr import Usd
__all__: list = ['MdlMatrixAttributeModel']
class MdlMatrixAttributeModel(omni.kit.property.usd.usd_attribute_model.MatrixBaseAttributeModel):
    """
    Extension of MatrixBaseAttributeModel for displaying non-uniform matrices.
    
        This model is used to represent a matrix attribute where the dimensions of the matrix may not be uniform. It extends the functionality of MatrixBaseAttributeModel by managing the display and update of matrix values in the UI.
    
        Args:
            stage (:obj:`Usd.Stage`): The USD stage that the attribute belongs to.
            attribute_paths (List[:obj:`Sdf.Path`]): A list of paths to the attributes.
            dimensions (List[int]): The dimensions of the matrix as a list [rows, columns].
            self_refresh (bool): Whether the model should refresh itself automatically.
            metadata (dict): A dictionary containing metadata for the attribute.
    """
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], dimensions: typing.List[int], self_refresh: bool, metadata: dict):
        """
        Initializes the MdlMatrixAttributeModel with the given parameters.
        """
    def _on_value_changed(self, item):
        """
        Called when the submodel is chaged
        """
    def _update_value(self, force = False):
        ...
