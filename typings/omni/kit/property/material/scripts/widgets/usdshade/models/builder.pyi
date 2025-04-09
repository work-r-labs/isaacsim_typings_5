"""
This module provides a builder class for constructing custom USD shading property models and UI elements, as well as a function to get the appropriate builder based on property metadata.
"""
from __future__ import annotations
from omni.kit.property.material.scripts.widgets.usdshade.models.expression import CallExpressionModel
from omni.kit.property.material.scripts.widgets.usdshade.models.matrix import MdlMatrixAttributeModel
from omni.kit.property.material.scripts.widgets.usdshade.models.output import UsdShadeOutputModel
import omni.kit.property.usd.usd_property_widget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from omni.kit.property.usd.usd_property_widget_builder import UsdPropertiesWidgetBuilder
from omni.kit.property.usd.usd_property_widget_builder import get_model_cls
from omni.kit.property.usd.usd_property_widget_builder import get_model_kwargs
from omni import ui
from pxr import Sdf
from pxr import Sdr
from pxr import UsdShade
__all__: list = ['UsdShadeCustomModelsBuilder']
class UsdShadeCustomModelsBuilder:
    """
    A class responsible for constructing custom models for USD shading properties.
    
        This class includes methods that build custom UI components based on the shading attributes and metadata provided. These methods are used to generate UI elements like call expressions, matrices, outputs, and checkboxes that correspond to various USD shading property types. Each method is a class method, ensuring that direct instantiation of the class is not required to utilize the functionality.
        
    """
    @classmethod
    def call_expression_builder(cls, stage, attr_name, metadata, type_name, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        Builds and returns a CallExpressionModel for the given attribute.
        
                Args:
                    stage: The stage to which the model belongs.
                    attr_name (str): The name of the attribute for which the model is created.
                    metadata (dict): Metadata associated with the attribute.
                    type_name (str): The type name of the attribute.
                    prim_paths (List[:obj:`Sdf.Path`]): List of paths to the primitives containing the attribute.
                    additional_label_kwargs (Optional[dict]): Additional kwargs for the label creation.
                    additional_widget_kwargs (Optional[dict]): Additional kwargs for the widget creation.
        
                Returns:
                    :obj:`CallExpressionModel`: The created CallExpressionModel instance.
        """
    @classmethod
    def checkbox_builder(cls, stage, attr_name, metadata, type_name, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        Builds and returns a boolean property widget.
        
                Args:
                    stage: The stage to which the model belongs.
                    attr_name (str): The name of the attribute for which the model is created.
                    metadata (dict): Metadata associated with the attribute.
                    type_name (str): The type name of the attribute.
                    prim_paths (List[:obj:`Sdf.Path`]): List of paths to the primitives containing the attribute.
                    additional_label_kwargs (Optional[dict]): Additional kwargs for label creation.
                    additional_widget_kwargs (Optional[dict]): Additional kwargs for widget creation.
        """
    @classmethod
    def matrix_builder(cls, stage, attr_name, metadata, type_name, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        Builds and returns a model for matrix attributes.
        
                Args:
                    stage: The stage to which the model belongs.
                    attr_name (str): The name of the attribute for which the model is created.
                    metadata (dict): Metadata associated with the attribute.
                    type_name (str): The type name of the attribute.
                    prim_paths (List[:obj:`Sdf.Path`]): List of paths to the primitives containing the attribute.
                    additional_label_kwargs (Optional[dict]): Additional kwargs for label creation.
                    additional_widget_kwargs (Optional[dict]): Additional kwargs for widget creation.
        
                Returns:
                    The created matrix attribute model.
        """
    @classmethod
    def outputs_builder(cls, stage, attr_name, metadata, type_name, prim_paths: typing.List[pxr.Sdf.Path], additional_label_kwargs = None, additional_widget_kwargs = None):
        """
        For outputs create a string field with no value that is locked for editing.
        
                Args:
                    stage: The stage to which the model belongs.
                    attr_name (str): The name of the attribute for which the model is created.
                    metadata (dict): Metadata associated with the attribute.
                    type_name (str): The type name of the attribute.
                    prim_paths (List[:obj:`Sdf.Path`]): List of paths to the primitives containing the attribute.
                    additional_label_kwargs (Optional[dict]): Additional kwargs for label creation.
                    additional_widget_kwargs (Optional[dict]): Additional kwargs for widget creation.
        
                Returns:
                    :obj:`UsdShadeOutputModel`: The created UsdShadeOutputModel instance.
        """
def get_custom_ui_prop_build_fn(ui_prop: omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry) -> None:
    """
    Returns a function that builds custom UI property models based on the specified ui_prop.
    
        Args:
            ui_prop (:obj:`UsdPropertyUiEntry`): The UI property entry that contains metadata to determine the appropriate custom model builder function.
    
        Returns:
            Optional[Callable]: A function that is used to build a custom UI property model if a matching builder is found; otherwise, None.
        
    """
HORIZONTAL_SPACING: int = 4
