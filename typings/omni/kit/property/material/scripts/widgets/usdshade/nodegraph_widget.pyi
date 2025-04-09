"""
Provides a widget for displaying and interacting with USD Shade Node Graphs within the USD material property extension.
"""
from __future__ import annotations
import omni.kit.property.material.scripts.widgets.usdshade.base_widget
from omni.kit.property.material.scripts.widgets.usdshade.base_widget import UsdShadeBaseWidget
from pxr import UsdShade
__all__: list = ['UsdShadeNodeGraphWidget']
class UsdShadeNodeGraphWidget(omni.kit.property.material.scripts.widgets.usdshade.base_widget.UsdShadeBaseWidget):
    """
    A widget for displaying and interacting with a USD Shade Node Graph.
    
        This widget extends the UsdShadeBaseWidget to provide a graphical interface for
        managing USD Shade Node Graphs, which are used to define complex shading networks
        for digital assets. It offers a default title but can be customized upon
        initialization.
    
        Args:
            title (str): The title of the widget. Defaults to 'Node Graph'.
    """
    def __init__(self, title: str = 'Node Graph'):
        """
        Initializes the UsdShadeNodeGraphWidget with a default or provided title.
        """
    def _identical_selection(self) -> bool:
        ...
