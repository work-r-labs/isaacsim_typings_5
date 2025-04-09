from __future__ import annotations
import omni as omni
from omni.kit.viewport.menubar.core.model.usd_object_model import USDObjectModel
import pxr.Sdf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
__all__: list = ['USDMetadataModel']
class USDMetadataModel(omni.kit.viewport.menubar.core.model.usd_object_model.USDObjectModel):
    """
    A simple value model to watch the specified metadata.
    """
    def __init__(self, stage: pxr.Usd.Stage, path: pxr.Sdf.Path, md_key: str):
        """
        
                Constructor.
        
                Args:
                    stage (Usd.Stage): USD stage.
                    path (Sdf.Path): Path in stage.
                    md_key (str): Meta data key.
                
        """
    def _get_value(self) -> typing.Any:
        """
        Get the value directly from USD
        """
    def set_value(self, value: typing.Any):
        """
        
                Set the value directly to USD.
        
                Args:
                    value (Any): New value to set.
                
        """
