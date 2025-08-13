from __future__ import annotations
__all__: list[str] = ['SurfaceGripperInterface', 'acquire_surface_gripper_interface', 'release_surface_gripper_interface']
class SurfaceGripperInterface:
    """
    """
    def close_gripper(self, prim_path: str) -> bool:
        """
        Closes a surface gripper at the specified USD path.
        """
    def get_gripped_objects(self, prim_path: str) -> list[str]:
        """
        Gets a list of objects currently gripped by the specified gripper.
        """
    def get_gripper_status(self, prim_path: str) -> str:
        """
        Gets the status of a surface gripper at the specified USD path.
        """
    def open_gripper(self, prim_path: str) -> bool:
        """
        Opens a surface gripper at the specified USD path.
        """
    def set_gripper_action(self, prim_path: str, action: float) -> bool:
        """
        Sets the action of a surface gripper at the specified USD path.
        """
def acquire_surface_gripper_interface(plugin_name: str = None, library_path: str = None) -> ...:
    """
    Acquire Surface Gripper interface. This is the base object that all of the Surface Gripper functions are defined on
    """
def release_surface_gripper_interface(arg0: ...) -> None:
    """
    Release Surface Gripper interface. Generally this does not need to be called, the Surface Gripper interface is released on extension shutdown
    """
