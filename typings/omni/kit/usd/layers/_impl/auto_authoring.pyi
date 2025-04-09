from __future__ import annotations
import omni.kit.usd.layers._omni_kit_usd_layers
from omni.kit.usd.layers._omni_kit_usd_layers import ILayersInstance
from omni.kit.usd.layers._omni_kit_usd_layers import acquire_auto_authoring_interface
from omni.kit.usd.layers._omni_kit_usd_layers import release_auto_authoring_interface
__all__: list = ['AutoAuthoring']
class AutoAuthoring:
    """
    
        (Experimental) USD supports switching edit targets so that all authoring will take place in that specified layer. When it's working
        with multiple sublayers, this kind of freedom may cause experience issues. The user has to be aware the changes made are
        not overridden in any stronger layer. We extend a new mode called Auto Authoring to improve it. In this mode, all
        changes will firstly go into a middle delegate layer and it will then distribute edits (per frame) into their
        corresponding layers where the edits have the strongest opinions. So it cannot switch edit targets freely,
        and users do not need to be aware of the existence of multi-sublayers and how USD will compose the changes.
        
    """
    def __init__(self, layers_instance: omni.kit.usd.layers._omni_kit_usd_layers.ILayersInstance, usd_context) -> None:
        ...
    def _destroy(self):
        ...
    def get_default_layer(self) -> str:
        """
        Gets the default layer.
        """
    def is_auto_authoring_layer(self, layer_identifier: str) -> bool:
        """
        Checks if a layer is an auto authoring layer.
        """
    def is_enabled(self) -> bool:
        """
        Checks if UsdContext is in Auto Authoring mode.
        """
    def set_default_layer(self, layer_identifier: str):
        """
        Sets the default layer to receive the newly created opinions.
        """
    @property
    def usd_context(self):
        ...
