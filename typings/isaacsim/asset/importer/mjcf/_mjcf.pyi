"""

        This extension provides an interface to the MJCF importer.

        Example:
            Setup the configuration parameters before importing.
            Files must be parsed before imported.

            ::

                from isaacsim.asset.importer.mjcf import _mjcf
                mjcf_interface = _mjcf.acquire_mjcf_interface()

                # setup config params
                import_config = _mjcf.ImportConfig()
                import_config.fix_base = True

                # parse and import file
                mjcf_interface.create_asset_mjcf(mjcf_path, prim_path, import_config)


        Refer to the sample documentation for more examples and usage
                
"""
from __future__ import annotations
__all__ = ['ImportConfig', 'Mjcf', 'acquire_mjcf_interface', 'release_mjcf_interface']
class ImportConfig:
    def __init__(self) -> None:
        ...
    def set_convex_decomp(self, arg0: bool) -> None:
        ...
    def set_create_body_for_fixed_joint(self, arg0: bool) -> None:
        ...
    def set_create_physics_scene(self, arg0: bool) -> None:
        ...
    def set_default_drive_strength(self, arg0: float) -> None:
        ...
    def set_density(self, arg0: float) -> None:
        ...
    def set_distance_scale(self, arg0: float) -> None:
        ...
    def set_fix_base(self, arg0: bool) -> None:
        ...
    def set_import_inertia_tensor(self, arg0: bool) -> None:
        ...
    def set_import_sites(self, arg0: bool) -> None:
        ...
    def set_instanceable_usd_path(self, arg0: str) -> None:
        ...
    def set_make_default_prim(self, arg0: bool) -> None:
        ...
    def set_make_instanceable(self, arg0: bool) -> None:
        ...
    def set_merge_fixed_joints(self, arg0: bool) -> None:
        ...
    def set_override_com(self, arg0: bool) -> None:
        ...
    def set_override_inertia(self, arg0: bool) -> None:
        ...
    def set_self_collision(self, arg0: bool) -> None:
        ...
    def set_visualize_collision_geoms(self, arg0: bool) -> None:
        ...
    @property
    def convex_decomp(self) -> bool:
        """
        Decompose a convex mesh into smaller pieces for a closer fit
        """
    @convex_decomp.setter
    def convex_decomp(self, arg0: bool) -> None:
        ...
    @property
    def create_body_for_fixed_joint(self) -> bool:
        """
        creates body for fixed joint
        """
    @create_body_for_fixed_joint.setter
    def create_body_for_fixed_joint(self, arg0: bool) -> None:
        ...
    @property
    def create_physics_scene(self) -> bool:
        """
        add a physics scene to the stage on import
        """
    @create_physics_scene.setter
    def create_physics_scene(self, arg0: bool) -> None:
        ...
    @property
    def default_drive_strength(self) -> float:
        """
        default drive stiffness used for joints
        """
    @default_drive_strength.setter
    def default_drive_strength(self, arg0: float) -> None:
        ...
    @property
    def density(self) -> float:
        """
        default density used for links
        """
    @density.setter
    def density(self, arg0: float) -> None:
        ...
    @property
    def distance_scale(self) -> float:
        """
        Set the unit scaling factor, 1.0 means meters, 100.0 means cm
        """
    @distance_scale.setter
    def distance_scale(self, arg0: float) -> None:
        ...
    @property
    def fix_base(self) -> bool:
        """
        Create fix joint for base link
        """
    @fix_base.setter
    def fix_base(self, arg0: bool) -> None:
        ...
    @property
    def import_inertia_tensor(self) -> bool:
        """
        Import inertia tensor from mjcf, if not specified in mjcf it will import as identity
        """
    @import_inertia_tensor.setter
    def import_inertia_tensor(self, arg0: bool) -> None:
        ...
    @property
    def instanceable_usd_path(self) -> str:
        """
        USD file to store instanceable mehses in
        """
    @instanceable_usd_path.setter
    def instanceable_usd_path(self, arg0: str) -> None:
        ...
    @property
    def make_default_prim(self) -> bool:
        """
        set imported robot as default prim
        """
    @make_default_prim.setter
    def make_default_prim(self, arg0: bool) -> None:
        ...
    @property
    def make_instanceable(self) -> bool:
        """
        Creates an instanceable version of the asset. All meshes will be placed in a separate USD file
        """
    @make_instanceable.setter
    def make_instanceable(self, arg0: bool) -> None:
        ...
    @property
    def merge_fixed_joints(self) -> bool:
        """
        Consolidating links that are connected by fixed joints
        """
    @merge_fixed_joints.setter
    def merge_fixed_joints(self, arg0: bool) -> None:
        ...
    @property
    def override_com(self) -> bool:
        """
        whether to compute the center of mass from geometry and override values given in the original asset
        """
    @override_com.setter
    def override_com(self, arg0: bool) -> None:
        ...
    @property
    def override_inertia_tensor(self) -> bool:
        """
        Whether to compute the inertia tensor from geometry and override values given in the original asset
        """
    @override_inertia_tensor.setter
    def override_inertia_tensor(self, arg0: bool) -> None:
        ...
    @property
    def self_collision(self) -> bool:
        """
        Self collisions between links in the articulation
        """
    @self_collision.setter
    def self_collision(self, arg0: bool) -> None:
        ...
class Mjcf:
    def create_asset_mjcf(self, fileName: str, primName: str, config: ImportConfig, stage_identifier: str = '') -> None:
        """
                        Parse and import MJCF file.
        
                        Args:
                            arg0 (:obj:`str`): The absolute path to the mjcf
        
                            arg1 (:obj:`str`): Path to the robot on the USD stage
        
                            arg2 (:obj:`isaacsim.asset.importer.mjcf._mjcf.ImportConfig`): Import configuration
        
                            arg3 (:obj:`str`): optional: path to stage to use for importing. leaving it empty will import on open stage. If the open stage is a new stage, textures will not load.
        """
def acquire_mjcf_interface(plugin_name: str = None, library_path: str = None) -> Mjcf:
    ...
def release_mjcf_interface(arg0: Mjcf) -> None:
    ...
