"""

        This extension provides an interface to the URDF importer.

        Example:
            Setup the configuration parameters before importing.
            Files must be parsed before imported.

            ::

                from isaacsim.asset.importer.urdf import _urdf
                urdf_interface = _urdf.acquire_urdf_interface()

                # setup config params
                import_config = _urdf.ImportConfig()
                import_config.set_merge_fixed_joints(False)
                import_config.set_fix_base(True)

                # parse and import file
                imported_robot = urdf_interface.parse_urdf(robot_path, filename, import_config)
                urdf_interface.import_robot(robot_path, filename, imported_robot, import_config, "")


        Refer to the sample documentation for more examples and usage
                
"""
from __future__ import annotations
import typing
__all__ = ['GEOMETRY_BOX', 'GEOMETRY_CAPSULE', 'GEOMETRY_CYLINDER', 'GEOMETRY_MESH', 'GEOMETRY_SPHERE', 'ImportConfig', 'JOINT_CONTINUOUS', 'JOINT_DRIVE_ACCELERATION', 'JOINT_DRIVE_FORCE', 'JOINT_DRIVE_NONE', 'JOINT_DRIVE_POSITION', 'JOINT_DRIVE_VELOCITY', 'JOINT_FIXED', 'JOINT_FLOATING', 'JOINT_PLANAR', 'JOINT_PRISMATIC', 'JOINT_REVOLUTE', 'Orientation', 'Position', 'Urdf', 'UrdfAxis', 'UrdfCamera', 'UrdfCollision', 'UrdfColor', 'UrdfDynamics', 'UrdfGeometry', 'UrdfGeometryType', 'UrdfInertia', 'UrdfInertial', 'UrdfJoint', 'UrdfJointDrive', 'UrdfJointDriveType', 'UrdfJointMap', 'UrdfJointMimic', 'UrdfJointTargetType', 'UrdfJointType', 'UrdfLimit', 'UrdfLink', 'UrdfLinkMap', 'UrdfMaterial', 'UrdfMaterialMap', 'UrdfOrigin', 'UrdfRay', 'UrdfRayDim', 'UrdfRobot', 'UrdfVisual', 'acquire_urdf_interface', 'release_urdf_interface']
class ImportConfig:
    def __init__(self) -> None:
        ...
    def set_collision_from_visuals(self, arg0: bool) -> None:
        ...
    def set_convex_decomp(self, arg0: bool) -> None:
        ...
    def set_create_physics_scene(self, arg0: bool) -> None:
        ...
    def set_default_drive_strength(self, arg0: float) -> None:
        ...
    def set_default_drive_type(self, arg0: int) -> None:
        ...
    def set_default_position_drive_damping(self, arg0: float) -> None:
        ...
    def set_density(self, arg0: float) -> None:
        ...
    def set_distance_scale(self, arg0: float) -> None:
        ...
    def set_fix_base(self, arg0: bool) -> None:
        ...
    def set_import_inertia_tensor(self, arg0: bool) -> None:
        ...
    def set_make_default_prim(self, arg0: bool) -> None:
        ...
    def set_merge_fixed_joints(self, arg0: bool) -> None:
        ...
    def set_override_joint_dynamics(self, arg0: bool) -> None:
        ...
    def set_parse_mimic(self, arg0: bool) -> None:
        ...
    def set_replace_cylinders_with_capsules(self, arg0: bool) -> None:
        ...
    def set_self_collision(self, arg0: bool) -> None:
        ...
    def set_subdivision_scheme(self, arg0: int) -> None:
        ...
    def set_up_vector(self, arg0: float, arg1: float, arg2: float) -> None:
        ...
    @property
    def collision_from_visuals(self) -> bool:
        """
        Generate convex collision from the visual meshes.
        """
    @collision_from_visuals.setter
    def collision_from_visuals(self, arg0: bool) -> None:
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
    def create_physics_scene(self) -> bool:
        """
        add a physics scene to the stage on import if none exists
        """
    @create_physics_scene.setter
    def create_physics_scene(self, arg0: bool) -> None:
        ...
    @property
    def default_drive_strength(self) -> float:
        """
        default drive stiffness used for joints if drive type is position or velocity and none is authored
        """
    @default_drive_strength.setter
    def default_drive_strength(self, arg0: float) -> None:
        ...
    @property
    def default_drive_type(self) -> ...:
        """
        default drive type used for joints
        """
    @default_drive_type.setter
    def default_drive_type(self, arg0: ...) -> None:
        ...
    @property
    def default_position_drive_damping(self) -> float:
        """
        default drive damping used if drive type is set to position and no damping is authored
        """
    @default_position_drive_damping.setter
    def default_position_drive_damping(self, arg0: float) -> None:
        ...
    @property
    def density(self) -> float:
        """
        default density used for links, use 0 to autocompute
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
        Import inertia tensor from urdf, if not specified in urdf it will import as identity
        """
    @import_inertia_tensor.setter
    def import_inertia_tensor(self, arg0: bool) -> None:
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
    def merge_fixed_joints(self) -> bool:
        """
        Consolidating links that are connected by fixed joints
        """
    @merge_fixed_joints.setter
    def merge_fixed_joints(self, arg0: bool) -> None:
        ...
    @property
    def override_joint_dynamics(self) -> bool:
        """
        Use default values for all joints
        """
    @override_joint_dynamics.setter
    def override_joint_dynamics(self, arg0: bool) -> None:
        ...
    @property
    def parse_mimic(self) -> bool:
        """
        Parse Mimic Joint flag using PhysX Tendons
        """
    @parse_mimic.setter
    def parse_mimic(self, arg0: bool) -> None:
        ...
    @property
    def replace_cylinders_with_capsules(self) -> bool:
        """
        Replace all cylinder bodies in the URDF with capsules.
        """
    @replace_cylinders_with_capsules.setter
    def replace_cylinders_with_capsules(self, arg0: bool) -> None:
        ...
    @property
    def self_collision(self) -> bool:
        """
        Self collisions between links in the articulation
        """
    @self_collision.setter
    def self_collision(self, arg0: bool) -> None:
        ...
    @property
    def subdivision_scheme(self) -> ...:
        """
        Subdivision scheme to be used for mesh normals
        """
    @subdivision_scheme.setter
    def subdivision_scheme(self, arg0: ...) -> None:
        ...
    @property
    def up_vector(self) -> ...:
        """
        Up vector used for import
        """
    @up_vector.setter
    def up_vector(self, arg0: ...) -> None:
        ...
class Orientation:
    """
    """
    w: float
    x: float
    y: float
    z: float
    def __init__(self) -> None:
        ...
class Position:
    """
    """
    x: float
    y: float
    z: float
    def __init__(self) -> None:
        ...
class Urdf:
    def compute_natural_stiffness(self, arg0: UrdfRobot, arg1: str, arg2: float) -> float:
        """
                        Compute the natural stiffness of a joint.
        
                        Args:
                            arg0 (:obj:`isaacsim.asset.importer.urdf._urdf.UrdfRobot`): The parsed URDF, the output from :obj:`parse_urdf`
        
                            arg1 (:obj:`str`): The name of the joint
        
                            arg2 (:obj:`float`): The natural frequency of the joint
        
                        Returns:
                            :obj:`float`: The natural stiffness of the joint
        """
    def get_kinematic_chain(self, arg0: UrdfRobot) -> dict:
        """
                        Get the kinematic chain of the robot. Mostly used for graphic display of the kinematic tree.
        
                        Args:
                            arg0 (:obj:`isaacsim.asset.importer.urdf._urdf.UrdfRobot`): The parsed URDF, the output from :obj:`parse_urdf`
        
                        Returns:
                            :obj:`dict`: A dictionary with information regarding the parent-child relationship between all the links and joints
        """
    def import_robot(self, assetRoot: str, assetName: str, robot: UrdfRobot, importConfig: ImportConfig, stage: str = '', getArticulationRoot: bool = False) -> str:
        """
                        Importing the robot, from the already parsed URDF file.
        
                        Args:
                            arg0 (:obj:`str`): The absolute path to where the urdf file is
        
                            arg1 (:obj:`str`): The name of the urdf file
        
                            arg2 (:obj:`isaacsim.asset.importer.urdf._urdf.UrdfRobot`): The parsed URDF file, the output from :obj:`parse_urdf`
        
                            arg3 (:obj:`isaacsim.asset.importer.urdf._urdf.ImportConfig`): Import configuration parameters
        
                            arg4 (:obj:`str`): optional: path to stage to use for importing. leaving it empty will import on open stage. If the open stage is a new stage, textures will not load.
        
                        Returns:
                            :obj:`str`: Path to the robot on the USD stage.
        """
    def parse_string_urdf(self, arg0: str, arg1: ImportConfig) -> UrdfRobot:
        """
                        Parse URDF file into the internal data structure, which is displayed in the importer window for inspection.
        
                        Args:
                            arg0 (:obj:`str`): The urdf in text format
        
                            arg2 (:obj:`isaacsim.asset.importer.urdf._urdf.ImportConfig`): Import configuration parameters
        
                        Returns:
                            :obj:`isaacsim.asset.importer.urdf._urdf.UrdfRobot`: Parsed URDF stored in an internal structure.
        """
    def parse_urdf(self, arg0: str, arg1: str, arg2: ImportConfig) -> UrdfRobot:
        """
                        Parse URDF file into the internal data structure, which is displayed in the importer window for inspection.
        
                        Args:
                            arg0 (:obj:`str`): The absolute path to where the urdf file is
        
                            arg1 (:obj:`str`): The name of the urdf file
        
                            arg2 (:obj:`isaacsim.asset.importer.urdf._urdf.ImportConfig`): Import configuration parameters
        
                        Returns:
                            :obj:`isaacsim.asset.importer.urdf._urdf.UrdfRobot`: Parsed URDF stored in an internal structure.
        """
class UrdfAxis:
    """
    """
    x: float
    y: float
    z: float
    def __init__(self) -> None:
        ...
class UrdfCamera:
    """
    """
    clip_far: float
    clip_near: float
    format: str
    h_fov: float
    height: float
    name: str
    origin: UrdfOrigin
    update_rate: float
    width: float
    def __init__(self) -> None:
        ...
class UrdfCollision:
    """
    """
    geometry: UrdfGeometry
    name: str
    origin: UrdfOrigin
    def __init__(self) -> None:
        ...
class UrdfColor:
    """
    """
    a: float
    b: float
    g: float
    r: float
    def __init__(self) -> None:
        ...
class UrdfDynamics:
    """
    """
    damping: float
    friction: float
    stiffness: float
    def __init__(self) -> None:
        ...
    def set_damping(self, arg0: float) -> None:
        ...
    def set_friction(self, arg0: float) -> None:
        ...
    def set_stiffness(self, arg0: float) -> None:
        ...
class UrdfGeometry:
    """
    """
    length: float
    mesh_file_path: str
    radius: float
    scale_x: float
    scale_y: float
    scale_z: float
    size_x: float
    size_y: float
    size_z: float
    type: UrdfGeometryType
    def __init__(self) -> None:
        ...
class UrdfGeometryType:
    """
    
    
    Members:
    
      GEOMETRY_BOX
    
      GEOMETRY_CYLINDER
    
      GEOMETRY_CAPSULE
    
      GEOMETRY_SPHERE
    
      GEOMETRY_MESH
    """
    GEOMETRY_BOX: typing.ClassVar[UrdfGeometryType]  # value = <UrdfGeometryType.GEOMETRY_BOX: 0>
    GEOMETRY_CAPSULE: typing.ClassVar[UrdfGeometryType]  # value = <UrdfGeometryType.GEOMETRY_CAPSULE: 2>
    GEOMETRY_CYLINDER: typing.ClassVar[UrdfGeometryType]  # value = <UrdfGeometryType.GEOMETRY_CYLINDER: 1>
    GEOMETRY_MESH: typing.ClassVar[UrdfGeometryType]  # value = <UrdfGeometryType.GEOMETRY_MESH: 4>
    GEOMETRY_SPHERE: typing.ClassVar[UrdfGeometryType]  # value = <UrdfGeometryType.GEOMETRY_SPHERE: 3>
    __members__: typing.ClassVar[dict[str, UrdfGeometryType]]  # value = {'GEOMETRY_BOX': <UrdfGeometryType.GEOMETRY_BOX: 0>, 'GEOMETRY_CYLINDER': <UrdfGeometryType.GEOMETRY_CYLINDER: 1>, 'GEOMETRY_CAPSULE': <UrdfGeometryType.GEOMETRY_CAPSULE: 2>, 'GEOMETRY_SPHERE': <UrdfGeometryType.GEOMETRY_SPHERE: 3>, 'GEOMETRY_MESH': <UrdfGeometryType.GEOMETRY_MESH: 4>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UrdfInertia:
    """
    """
    ixx: float
    ixy: float
    ixz: float
    iyy: float
    iyz: float
    izz: float
    def __init__(self) -> None:
        ...
class UrdfInertial:
    """
    """
    has_inertia: bool
    has_mass: bool
    has_origin: bool
    inertia: UrdfInertia
    mass: float
    origin: UrdfOrigin
    def __init__(self) -> None:
        ...
class UrdfJoint:
    """
    """
    axis: UrdfAxis
    child_link_name: str
    children_joints: list[str]
    drive: UrdfJointDrive
    dynamics: UrdfDynamics
    inertia: float
    limit: UrdfLimit
    mimic: UrdfJointMimic
    name: str
    origin: UrdfOrigin
    parent_joint: str
    parent_link_name: str
    type: UrdfJointType
    def __init__(self) -> None:
        ...
class UrdfJointDrive:
    """
    """
    damping: float
    damping_ratio: float
    drive_type: UrdfJointDriveType
    natural_frequency: float
    strength: float
    target: float
    target_type: UrdfJointTargetType
    def __init__(self) -> None:
        ...
    def set_damping(self, arg0: float) -> None:
        ...
    def set_drive_type(self, arg0: int) -> None:
        ...
    def set_strength(self, arg0: float) -> None:
        ...
    def set_target(self, arg0: float) -> None:
        ...
    def set_target_type(self, arg0: int) -> None:
        ...
class UrdfJointDriveType:
    """
    
    
    Members:
    
      JOINT_DRIVE_ACCELERATION
    
      JOINT_DRIVE_FORCE
    """
    JOINT_DRIVE_ACCELERATION: typing.ClassVar[UrdfJointDriveType]  # value = <UrdfJointDriveType.JOINT_DRIVE_ACCELERATION: 0>
    JOINT_DRIVE_FORCE: typing.ClassVar[UrdfJointDriveType]  # value = <UrdfJointDriveType.JOINT_DRIVE_FORCE: 2>
    __members__: typing.ClassVar[dict[str, UrdfJointDriveType]]  # value = {'JOINT_DRIVE_ACCELERATION': <UrdfJointDriveType.JOINT_DRIVE_ACCELERATION: 0>, 'JOINT_DRIVE_FORCE': <UrdfJointDriveType.JOINT_DRIVE_FORCE: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UrdfJointMap:
    def __getitem__(self: dict[str, UrdfJoint], arg0: str) -> UrdfJoint:
        ...
    def __init__(self) -> None:
        ...
    def __iter__(self: dict[str, UrdfJoint]) -> typing.Iterator:
        ...
    def __len__(self: dict[str, UrdfJoint]) -> int:
        ...
    def items(self: dict[str, UrdfJoint]) -> typing.Iterator:
        ...
class UrdfJointMimic:
    """
    """
    joint: str
    multiplier: float
    offset: float
    def __init__(self) -> None:
        ...
class UrdfJointTargetType:
    """
    
    
    Members:
    
      JOINT_DRIVE_NONE
    
      JOINT_DRIVE_POSITION
    
      JOINT_DRIVE_VELOCITY
    """
    JOINT_DRIVE_NONE: typing.ClassVar[UrdfJointTargetType]  # value = <UrdfJointTargetType.JOINT_DRIVE_NONE: 0>
    JOINT_DRIVE_POSITION: typing.ClassVar[UrdfJointTargetType]  # value = <UrdfJointTargetType.JOINT_DRIVE_POSITION: 1>
    JOINT_DRIVE_VELOCITY: typing.ClassVar[UrdfJointTargetType]  # value = <UrdfJointTargetType.JOINT_DRIVE_VELOCITY: 2>
    __members__: typing.ClassVar[dict[str, UrdfJointTargetType]]  # value = {'JOINT_DRIVE_NONE': <UrdfJointTargetType.JOINT_DRIVE_NONE: 0>, 'JOINT_DRIVE_POSITION': <UrdfJointTargetType.JOINT_DRIVE_POSITION: 1>, 'JOINT_DRIVE_VELOCITY': <UrdfJointTargetType.JOINT_DRIVE_VELOCITY: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UrdfJointType:
    """
    
    
    Members:
    
      JOINT_REVOLUTE
    
      JOINT_CONTINUOUS
    
      JOINT_PRISMATIC
    
      JOINT_FIXED
    
      JOINT_FLOATING
    
      JOINT_PLANAR
    """
    JOINT_CONTINUOUS: typing.ClassVar[UrdfJointType]  # value = <UrdfJointType.JOINT_CONTINUOUS: 1>
    JOINT_FIXED: typing.ClassVar[UrdfJointType]  # value = <UrdfJointType.JOINT_FIXED: 3>
    JOINT_FLOATING: typing.ClassVar[UrdfJointType]  # value = <UrdfJointType.JOINT_FLOATING: 4>
    JOINT_PLANAR: typing.ClassVar[UrdfJointType]  # value = <UrdfJointType.JOINT_PLANAR: 5>
    JOINT_PRISMATIC: typing.ClassVar[UrdfJointType]  # value = <UrdfJointType.JOINT_PRISMATIC: 2>
    JOINT_REVOLUTE: typing.ClassVar[UrdfJointType]  # value = <UrdfJointType.JOINT_REVOLUTE: 0>
    __members__: typing.ClassVar[dict[str, UrdfJointType]]  # value = {'JOINT_REVOLUTE': <UrdfJointType.JOINT_REVOLUTE: 0>, 'JOINT_CONTINUOUS': <UrdfJointType.JOINT_CONTINUOUS: 1>, 'JOINT_PRISMATIC': <UrdfJointType.JOINT_PRISMATIC: 2>, 'JOINT_FIXED': <UrdfJointType.JOINT_FIXED: 3>, 'JOINT_FLOATING': <UrdfJointType.JOINT_FLOATING: 4>, 'JOINT_PLANAR': <UrdfJointType.JOINT_PLANAR: 5>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UrdfLimit:
    """
    """
    effort: float
    lower: float
    upper: float
    velocity: float
    def __init__(self) -> None:
        ...
    def set_effort(self, arg0: float) -> None:
        ...
    def set_lower(self, arg0: float) -> None:
        ...
    def set_upper(self, arg0: float) -> None:
        ...
    def set_velocity(self, arg0: float) -> None:
        ...
class UrdfLink:
    """
    """
    cameras: list[UrdfCamera]
    collisions: list[UrdfCollision]
    inertial: UrdfInertial
    lidars: list[UrdfRay]
    name: str
    visuals: list[UrdfVisual]
    def __init__(self) -> None:
        ...
class UrdfLinkMap:
    def __getitem__(self: dict[str, UrdfLink], arg0: str) -> UrdfLink:
        ...
    def __init__(self) -> None:
        ...
    def __iter__(self: dict[str, UrdfLink]) -> typing.Iterator:
        ...
    def __len__(self: dict[str, UrdfLink]) -> int:
        ...
    def items(self: dict[str, UrdfLink]) -> typing.Iterator:
        ...
class UrdfMaterial:
    """
    """
    color: UrdfColor
    name: str
    texture_file_path: str
    def __init__(self) -> None:
        ...
class UrdfMaterialMap:
    def __getitem__(self, arg0: str) -> UrdfMaterial:
        ...
    def __init__(self) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def items(self) -> typing.Iterator:
        ...
class UrdfOrigin:
    """
    """
    p: Position
    q: Orientation
    def __init__(self) -> None:
        ...
class UrdfRay:
    """
    """
    has_horizontal: bool
    has_vertical: bool
    horizontal: UrdfRayDim
    name: str
    origin: UrdfOrigin
    update_rate: float
    vertical: UrdfRayDim
    def __init__(self) -> None:
        ...
class UrdfRayDim:
    """
    """
    max_angle: float
    min_angle: float
    resolution: float
    samples: int
    def __init__(self) -> None:
        ...
class UrdfRobot:
    """
    """
    asset_root: str
    joints: dict[str, UrdfJoint]
    links: dict[str, UrdfLink]
    name: str
    root_link: str
    urdf_path: str
    def __init__(self) -> None:
        ...
    @property
    def materials(self) -> ...:
        ...
    @materials.setter
    def materials(self, arg0: ..., isaacsim: ..., std: ..., std: ..., isaacsim: ...) -> None:
        ...
class UrdfVisual:
    """
    """
    geometry: UrdfGeometry
    material: UrdfMaterial
    name: str
    origin: UrdfOrigin
    def __init__(self) -> None:
        ...
def acquire_urdf_interface(plugin_name: str = None, library_path: str = None) -> Urdf:
    ...
def release_urdf_interface(arg0: Urdf) -> None:
    ...
GEOMETRY_BOX: UrdfGeometryType  # value = <UrdfGeometryType.GEOMETRY_BOX: 0>
GEOMETRY_CAPSULE: UrdfGeometryType  # value = <UrdfGeometryType.GEOMETRY_CAPSULE: 2>
GEOMETRY_CYLINDER: UrdfGeometryType  # value = <UrdfGeometryType.GEOMETRY_CYLINDER: 1>
GEOMETRY_MESH: UrdfGeometryType  # value = <UrdfGeometryType.GEOMETRY_MESH: 4>
GEOMETRY_SPHERE: UrdfGeometryType  # value = <UrdfGeometryType.GEOMETRY_SPHERE: 3>
JOINT_CONTINUOUS: UrdfJointType  # value = <UrdfJointType.JOINT_CONTINUOUS: 1>
JOINT_DRIVE_ACCELERATION: UrdfJointDriveType  # value = <UrdfJointDriveType.JOINT_DRIVE_ACCELERATION: 0>
JOINT_DRIVE_FORCE: UrdfJointDriveType  # value = <UrdfJointDriveType.JOINT_DRIVE_FORCE: 2>
JOINT_DRIVE_NONE: UrdfJointTargetType  # value = <UrdfJointTargetType.JOINT_DRIVE_NONE: 0>
JOINT_DRIVE_POSITION: UrdfJointTargetType  # value = <UrdfJointTargetType.JOINT_DRIVE_POSITION: 1>
JOINT_DRIVE_VELOCITY: UrdfJointTargetType  # value = <UrdfJointTargetType.JOINT_DRIVE_VELOCITY: 2>
JOINT_FIXED: UrdfJointType  # value = <UrdfJointType.JOINT_FIXED: 3>
JOINT_FLOATING: UrdfJointType  # value = <UrdfJointType.JOINT_FLOATING: 4>
JOINT_PLANAR: UrdfJointType  # value = <UrdfJointType.JOINT_PLANAR: 5>
JOINT_PRISMATIC: UrdfJointType  # value = <UrdfJointType.JOINT_PRISMATIC: 2>
JOINT_REVOLUTE: UrdfJointType  # value = <UrdfJointType.JOINT_REVOLUTE: 0>
