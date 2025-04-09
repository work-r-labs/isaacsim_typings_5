from __future__ import annotations
import omni.ui_scene._scene
__all__ = ['SceneCameraModel']
class SceneCameraModel(omni.ui_scene._scene.CameraModel):
    """
    The entity representing a scene camera model. This model is designed to improve navigation lag for viewing scenes.
    
    """
    def __init__(self, usdContextName: str, viewportHandle: int) -> None:
        """
        Constructor. It initializes SceneCameraModel with a given UsdContext name and a viewport handle.
        """
    def get_usdcontext_name(self) -> str:
        """
        Get the USD context name associated with the SceneCameraModel.
        """
    def get_viewport_handle(self) -> int:
        """
        Get the viewport handle associated with the SceneCameraModel.
        """
    def set_usdcontext_name(self, usdContextName: str) -> None:
        """
        Set a new USD context name for SceneCameraModel.
        """
    def set_viewport_handle(self, viewportHandle: int) -> None:
        """
        Set a new viewport handle for SceneCameraModel.
        """
