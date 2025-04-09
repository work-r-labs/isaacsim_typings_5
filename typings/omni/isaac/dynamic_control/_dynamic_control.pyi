"""

        The Dynamic Control extension provides a set of utilities to control physics objects. 
        It provides opaque handles for different physics objects that remain valid between PhysX scene resets, which occur whenever play or stop is pressed.
        
        Attributes:
            INVALID_HANDLE: This value is returned when trying to acquire a dynamic control handle for an invalid usd path

        The following attributes correspond to states that can be get/set from Degrees of Freedom and Rigid Bodies  
        
        Attributes:
            STATE_NONE: No state selected
            STATE_POS: Position states
            STATE_VEL: Velocity states
            STATE_EFFORT: Force/Torque states
            STATE_ALL: All states
        
        The following attributes correspond to joint axes when specifying a 6 Dof (D6) Joint
        
        Attributes:
            AXIS_NONE: No axis selected
            AXIS_X: Corresponds to translation around the body x-axis
            AXIS_Y: Corresponds to translation around the body y-axis
            AXIS_Z: Corresponds to translation around the body z-axis
            AXIS_TWIST: Corresponds to rotation around the body x-axis
            AXIS_SWING_1: Corresponds to rotation around the body y-axis
            AXIS_SWING_2: Corresponds to rotation around the body z-axis
            AXIS_ALL_TRANSLATION: Corresponds to all Translation axes
            AXIS_ALL_ROTATION: Corresponds to all Rotation axes
            AXIS_ALL: Corresponds to all axes
        
"""
from __future__ import annotations
import carb._carb
import numpy
import numpy.dtypes
import typing
import typing_extensions
__all__ = ['AXIS_ALL', 'AXIS_ALL_ROTATION', 'AXIS_ALL_TRANSLATION', 'AXIS_NONE', 'AXIS_SWING_1', 'AXIS_SWING_2', 'AXIS_TWIST', 'AXIS_X', 'AXIS_Y', 'AXIS_Z', 'ArticulationProperties', 'AttractorProperties', 'D6JointProperties', 'DOF_NONE', 'DOF_ROTATION', 'DOF_TRANSLATION', 'DRIVE_ACCELERATION', 'DRIVE_FORCE', 'DofProperties', 'DofState', 'DofType', 'DriveMode', 'DynamicControl', 'INVALID_HANDLE', 'JOINT_FIXED', 'JOINT_NONE', 'JOINT_PRISMATIC', 'JOINT_REVOLUTE', 'JOINT_SPHERICAL', 'JointType', 'OBJECT_ARTICULATION', 'OBJECT_ATTRACTOR', 'OBJECT_D6JOINT', 'OBJECT_DOF', 'OBJECT_JOINT', 'OBJECT_NONE', 'OBJECT_RIGIDBODY', 'ObjectType', 'RigidBodyProperties', 'RigidBodyState', 'STATE_ALL', 'STATE_EFFORT', 'STATE_NONE', 'STATE_POS', 'STATE_VEL', 'Transform', 'Velocity', 'acquire_dynamic_control_interface', 'release_dynamic_control_interface']
class ArticulationProperties:
    """
    Articulation Properties
    """
    def __getstate__(self) -> tuple:
        ...
    def __init__(self) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    @property
    def enable_self_collisions(self) -> bool:
        """
        Allow links in articulation to collide with each other (:obj:`bool`)
        """
    @enable_self_collisions.setter
    def enable_self_collisions(self, arg0: bool) -> None:
        ...
    @property
    def solver_position_iteration_count(self) -> int:
        """
        Position solver iterations (:obj:`int`)
        """
    @solver_position_iteration_count.setter
    def solver_position_iteration_count(self, arg0: int) -> None:
        ...
    @property
    def solver_velocity_iteration_count(self) -> int:
        """
        Velocity solver iterations (:obj:`int`)
        """
    @solver_velocity_iteration_count.setter
    def solver_velocity_iteration_count(self, arg0: int) -> None:
        ...
class AttractorProperties:
    """
    The Attractor is used to pull a rigid body towards a pose. Each pose axis can be individually selected.
    """
    def __getstate__(self) -> tuple:
        ...
    def __init__(self) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    @property
    def axes(self) -> int:
        """
        Axes to set the attractor, using DcAxisFlags. Multiple axes can be selected using bitwise combination of each axis flag. if axis flag is set to zero, the attractor will be disabled and won't impact in solver computational complexity.
        """
    @axes.setter
    def axes(self, arg0: int) -> None:
        ...
    @property
    def body(self) -> int:
        """
        Rigid body to set the attractor to
        """
    @body.setter
    def body(self, arg0: int) -> None:
        ...
    @property
    def damping(self) -> float:
        """
        Damping to be used on attraction solver. (:obj:`float`)
        """
    @damping.setter
    def damping(self, arg0: float) -> None:
        ...
    @property
    def force_limit(self) -> float:
        """
        Maximum force to be applied by drive. (:obj:`float`)
        """
    @force_limit.setter
    def force_limit(self, arg0: float) -> None:
        ...
    @property
    def offset(self) -> Transform:
        """
        Offset from rigid body origin to set the attractor pose. (:obj:`omni.isaac.dynamic_control._dynamic_control.Transform`)
        """
    @offset.setter
    def offset(self, arg0: Transform) -> None:
        ...
    @property
    def stiffness(self) -> float:
        """
        Stiffness to be used on attraction for solver. Stiffness value should be larger than the largest agent kinematic chain stifness (:obj:`float`)
        """
    @stiffness.setter
    def stiffness(self, arg0: float) -> None:
        ...
    @property
    def target(self) -> Transform:
        """
        Target pose to attract to. (:obj:`omni.isaac.dynamic_control._dynamic_control.Transform`)
        """
    @target.setter
    def target(self, arg0: Transform) -> None:
        ...
class D6JointProperties:
    """
    Creates  a general D6 Joint between two rigid Bodies.
    """
    def __getstate__(self) -> tuple:
        ...
    def __init__(self) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    @property
    def axes(self) -> int:
        """
        Axes to set the attractor, using DcAxisFlags. Multiple axes can be selected using bitwise combination of each axis flag. if axis flag is set to zero, the attractor will be disabled and won't impact in solver computational complexity.
        """
    @axes.setter
    def axes(self, arg0: int) -> None:
        ...
    @property
    def body0(self) -> int:
        """
        parent body
        """
    @body0.setter
    def body0(self, arg0: int) -> None:
        ...
    @property
    def body1(self) -> int:
        """
        child body
        """
    @body1.setter
    def body1(self, arg0: int) -> None:
        ...
    @property
    def damping(self) -> float:
        """
        Joint Damping. (:obj:`float`)
        """
    @damping.setter
    def damping(self, arg0: float) -> None:
        ...
    @property
    def force_limit(self) -> float:
        """
        Joint Breaking Force. (:obj:`float`)
        """
    @force_limit.setter
    def force_limit(self, arg0: float) -> None:
        ...
    @property
    def name(self) -> str:
        """
        Joint Name (:obj:`str`)
        """
    @name.setter
    def name(self, arg0: str) -> None:
        ...
    @property
    def pose0(self) -> Transform:
        """
        Transform from body 0 to joint. (:obj:`omni.isaac.dynamic_control._dynamic_control.Transform`)
        """
    @pose0.setter
    def pose0(self, arg0: Transform) -> None:
        ...
    @property
    def pose1(self) -> Transform:
        """
        Transform from body 1 to joint. (:obj:`omni.isaac.dynamic_control._dynamic_control.Transform`)
        """
    @pose1.setter
    def pose1(self, arg0: Transform) -> None:
        ...
    @property
    def stiffness(self) -> float:
        """
        Joint Stiffness. Stiffness value should be larger than the largest agent kinematic chain stifness (:obj:`float`)
        """
    @stiffness.setter
    def stiffness(self, arg0: float) -> None:
        ...
    @property
    def torque_limit(self) -> float:
        """
        Joint Breaking torque. (:obj:`float`)
        """
    @torque_limit.setter
    def torque_limit(self, arg0: float) -> None:
        ...
class DofProperties:
    """
    Properties of a degree-of-freedom (DOF)
    """
    def __getstate__(self) -> tuple:
        ...
    def __init__(self) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    @property
    def damping(self) -> float:
        """
        Damping of DOF (:obj:`float`)
        """
    @damping.setter
    def damping(self, arg0: float) -> None:
        ...
    @property
    def drive_mode(self) -> DriveMode:
        """
        Drive mode for the DOF (:obj:`omni.isaac.dynamic_control._dynamic_control.DriveMode`)
        """
    @drive_mode.setter
    def drive_mode(self, arg0: DriveMode) -> None:
        ...
    @property
    def has_limits(self) -> bool:
        """
        Flags whether the DOF has limits (read only) (:obj:`bool`)
        """
    @has_limits.setter
    def has_limits(self, arg0: bool) -> None:
        ...
    @property
    def lower(self) -> float:
        """
        lower limit of DOF. In radians or meters (read only) (:obj:`float`)
        """
    @lower.setter
    def lower(self, arg0: float) -> None:
        ...
    @property
    def max_effort(self) -> float:
        """
        Maximum effort of DOF. in N or N*stage_units (:obj:`float`)
        """
    @max_effort.setter
    def max_effort(self, arg0: float) -> None:
        ...
    @property
    def max_velocity(self) -> float:
        """
        Maximum velocity of DOF. In Radians/s, or stage_units/s (:obj:`float`)
        """
    @max_velocity.setter
    def max_velocity(self, arg0: float) -> None:
        ...
    @property
    def stiffness(self) -> float:
        """
        Stiffness of DOF (:obj:`float`)
        """
    @stiffness.setter
    def stiffness(self, arg0: float) -> None:
        ...
    @property
    def type(self) -> DofType:
        """
                                   Type of joint (read only) (:obj:`omni.isaac.dynamic_control._dynamic_control.DofType`)
        """
    @type.setter
    def type(self, arg0: DofType) -> None:
        ...
    @property
    def upper(self) -> float:
        """
        upper limit of DOF. In radians or meters (read only) (:obj:`float`)
        """
    @upper.setter
    def upper(self, arg0: float) -> None:
        ...
class DofState:
    """
    States of a Degree of Freedom in the Asset architecture
    """
    dtype: typing.ClassVar[numpy.dtypes.VoidDType]  # value = dtype([('pos', '<f4'), ('vel', '<f4'), ('effort', '<f4')])
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self, pos: float = None, vel: float = None, effort: float = None) -> None:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    @property
    def effort(self) -> float:
        """
        DOF effort due to gravity, torque if it's a revolute DOF, or force if it's a prismatic DOF (:obj:`float`)
        """
    @effort.setter
    def effort(self, arg0: float) -> None:
        ...
    @property
    def pos(self) -> float:
        """
        DOF position, in radians if it's a revolute DOF, or stage_units (m, cm, etc), if it's a prismatic DOF (:obj:`float`)
        """
    @pos.setter
    def pos(self, arg0: float) -> None:
        ...
    @property
    def vel(self) -> float:
        """
        DOF velocity, in radians/s if it's a revolute DOF, or stage_units/s (m/s, cm/s, etc), if it's a prismatic DOF (:obj:`float`)
        """
    @vel.setter
    def vel(self, arg0: float) -> None:
        ...
class DofType:
    """
    Types of degree of freedom
    
    Members:
    
      DOF_NONE : invalid/unknown/uninitialized DOF type
    
      DOF_ROTATION : The degrees of freedom correspond to a rotation between bodies
    
      DOF_TRANSLATION : The degrees of freedom correspond to a translation between bodies.
    """
    DOF_NONE: typing.ClassVar[DofType]  # value = <DofType.DOF_NONE: 0>
    DOF_ROTATION: typing.ClassVar[DofType]  # value = <DofType.DOF_ROTATION: 1>
    DOF_TRANSLATION: typing.ClassVar[DofType]  # value = <DofType.DOF_TRANSLATION: 2>
    __members__: typing.ClassVar[dict[str, DofType]]  # value = {'DOF_NONE': <DofType.DOF_NONE: 0>, 'DOF_ROTATION': <DofType.DOF_ROTATION: 1>, 'DOF_TRANSLATION': <DofType.DOF_TRANSLATION: 2>}
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
class DriveMode:
    """
    DOF drive mode
    
    Members:
    
      DRIVE_FORCE : Use Force Based Drive Controller
    
      DRIVE_ACCELERATION : Use Acceleration Based Drive Controller
    """
    DRIVE_ACCELERATION: typing.ClassVar[DriveMode]  # value = <DriveMode.DRIVE_ACCELERATION: 1>
    DRIVE_FORCE: typing.ClassVar[DriveMode]  # value = <DriveMode.DRIVE_FORCE: 0>
    __members__: typing.ClassVar[dict[str, DriveMode]]  # value = {'DRIVE_FORCE': <DriveMode.DRIVE_FORCE: 0>, 'DRIVE_ACCELERATION': <DriveMode.DRIVE_ACCELERATION: 1>}
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
class DynamicControl:
    """
    The following functions are provided on the dynamic control interface
    """
    def apply_body_force(self, arg0: int, arg1: carb._carb.Float3, arg2: carb._carb.Float3, arg3: bool) -> bool:
        """
        Apply a force to a rigid body at a position, coordinates can be specified in global or local coordinates
        """
    def apply_body_torque(self, arg0: int, arg1: carb._carb.Float3, arg2: bool) -> bool:
        """
        Apply a torque to a rigid body, can be specified in global or local coordinates
        """
    def create_d6_joint(self, arg0: D6JointProperties) -> int:
        """
        Create a D6 joint
        """
    def create_rigid_body_attractor(self, arg0: AttractorProperties) -> int:
        """
        Greate an attractor for ridig body
        """
    def destroy_d6_joint(self, arg0: int) -> bool:
        """
        Destroy D6 joint
        """
    def destroy_rigid_body_attractor(self, arg0: int) -> bool:
        """
        Destroy attractor
        """
    def find_articulation_body(self, arg0: int, arg1: str) -> int:
        """
        Finds actor rigid body given its name
        """
    def find_articulation_body_index(self, arg0: int, arg1: str) -> int:
        """
        Find index in articulation body array, -1 on error
        """
    def find_articulation_dof(self, arg0: int, arg1: str) -> int:
        """
        Finds actor degree-of-freedom given its name
        """
    def find_articulation_dof_index(self, arg0: int, arg1: str) -> int:
        """
        get index in articulation DOF array, -1 on error
        """
    def find_articulation_joint(self, arg0: int, arg1: str) -> int:
        """
        Get the joint from an atriculation given their name
        """
    def get_articulation(self, arg0: str) -> int:
        """
                    Returns:
                        handle: Handle to the articulation, INVALID_HANDLE otherwise
        """
    def get_articulation_body(self, arg0: int, arg1: int) -> int:
        """
        Gets actor rigid body given its index
        """
    def get_articulation_body_count(self, arg0: int) -> int:
        """
        Gets number of rigid bodies for an actor
        """
    def get_articulation_body_states(self, arg0: int, arg1: int) -> typing.Any:
        """
        Get array of an actor's rigid body states
        """
    def get_articulation_dof(self, arg0: int, arg1: int) -> int:
        """
        Gets actor degree-of-freedom given its index
        """
    def get_articulation_dof_count(self, arg0: int) -> int:
        """
        Gets number of degrees-of-freedom for an actor
        """
    def get_articulation_dof_efforts(self, arg0: int) -> typing.Any:
        """
        Get array of efforts for articulation
        """
    def get_articulation_dof_masses(self, arg0: int) -> typing.Any:
        """
        Get array of an actor's degree-of-freedom effective masses
        """
    def get_articulation_dof_position_targets(self, arg0: int) -> typing.Any:
        """
        Get array of position targets for articulation
        """
    def get_articulation_dof_properties(self, arg0: int) -> typing.Any:
        """
        Get array of an actor's degree-of-freedom properties
        """
    def get_articulation_dof_states(self, arg0: int, arg1: int) -> typing.Any:
        """
        Get array of an actor's degree-of-freedom states
        """
    def get_articulation_dof_velocity_targets(self, arg0: int) -> typing.Any:
        """
        Get array of velocity targets for articulation
        """
    def get_articulation_joint(self, arg0: int, arg1: int) -> int:
        """
        Gets the joint from an articulation given an index 
        """
    def get_articulation_joint_count(self, arg0: int) -> int:
        """
        Get the number of joints in an articulation
        """
    def get_articulation_name(self, arg0: int) -> str:
        """
                         Returns:
                            string: The name of the articulation
        """
    def get_articulation_path(self, arg0: int) -> str:
        """
                         Returns:
                            string: The path to the articulation
        """
    @typing.overload
    def get_articulation_properties(self, arg0: int, arg1: ArticulationProperties) -> bool:
        """
        Get Properties for an articulation
        """
    @typing.overload
    def get_articulation_properties(self, arg0: int) -> typing.Any:
        """
        Get Properties for an articulation
        """
    def get_articulation_root_body(self, arg0: int) -> int:
        """
        Get the root rigid body of an actor
        """
    def get_attractor_properties(self, arg0: int) -> typing.Any:
        """
        Get properties for attractor
        """
    def get_d6_joint(self, arg0: str) -> int:
        """
                    Returns:
                        handle: Handle to the d6 joint, INVALID_HANDLE otherwise
        """
    def get_dof(self, arg0: str) -> int:
        """
                    Returns:
                        handle: Handle to the degree of freedom, INVALID_HANDLE otherwise
        """
    def get_dof_child_body(self, arg0: int) -> int:
        """
        Get child rigid body for degree of freedom
        """
    def get_dof_effort(self, arg0: int) -> float:
        """
        Get effort applied to degree of freedom
        """
    def get_dof_joint(self, arg0: int) -> int:
        """
        Get joint associated with the degree of freedom
        """
    def get_dof_name(self, arg0: int) -> str:
        """
        Get Name of this degree of freedom
        """
    def get_dof_parent_body(self, arg0: int) -> int:
        """
        Get parent rigid body for degree of freedom
        """
    def get_dof_path(self, arg0: int) -> str:
        """
        Get path to degree of freedom
        """
    def get_dof_position(self, arg0: int) -> float:
        """
        Get position/rotation for this degree of freedom
        """
    def get_dof_position_target(self, arg0: int) -> float:
        """
        Get position target for degree of freedom
        """
    @typing.overload
    def get_dof_properties(self, arg0: int, arg1: DofProperties) -> bool:
        """
        Get degree of freedom properties
        """
    @typing.overload
    def get_dof_properties(self, arg0: int) -> typing.Any:
        """
        Get degree of freedom properties
        """
    def get_dof_state(self, arg0: int, arg1: int) -> DofState:
        """
        Get current state for degree of freedom
        """
    def get_dof_type(self, arg0: int) -> DofType:
        """
        Get type of degree of freedom
        """
    def get_dof_velocity(self, arg0: int) -> float:
        """
        Get linear/angular velocity of degree of freedom
        """
    def get_dof_velocity_target(self, arg0: int) -> float:
        """
        Get velocity target for degree of freedom
        """
    def get_joint(self, arg0: str) -> int:
        """
                    Returns:
                        handle: Handle to the joint, INVALID_HANDLE otherwise
        """
    def get_joint_child_body(self, arg0: int) -> int:
        """
        Get child rigid body for joint
        """
    def get_joint_dof(self, arg0: int, arg1: int) -> int:
        """
        Get a degree of freedom for joint give its index
        """
    def get_joint_dof_count(self, arg0: int) -> int:
        """
        Get number of degrees of freedon constrained by joint
        """
    def get_joint_name(self, arg0: int) -> str:
        """
        Get name of joint
        """
    def get_joint_parent_body(self, arg0: int) -> int:
        """
        Get parent rigid body for joint
        """
    def get_joint_path(self, arg0: int) -> str:
        """
        Get path for joint
        """
    def get_joint_type(self, arg0: int) -> JointType:
        """
        Get joint type
        """
    def get_object(self, arg0: str) -> int:
        """
                    Returns:
                        handle: Handle to the physics object defined by the usd path, INVALID_HANDLE otherwise
        """
    def get_object_type(self, arg0: int) -> ObjectType:
        """
        \\
                    Returns:
                        :obj:`omni.isaac.dynamic_control._dynamic_control.ObjectType`: Type of object returned by get_object
        """
    def get_object_type_name(self, arg0: int) -> str:
        """
                    Returns:
                        string: The object type name as a string
        """
    def get_relative_body_poses(self, arg0: int, arg1: list[int]) -> list[Transform]:
        """
        given a list of body handles, return poses relative to the parent
        """
    def get_rigid_body(self, arg0: str) -> int:
        """
                    Returns:
                        handle: Handle to the rigid body, INVALID_HANDLE otherwise
        """
    def get_rigid_body_angular_velocity(self, arg0: int) -> carb._carb.Float3:
        """
        Get the angular velocity of this rigid body
        """
    def get_rigid_body_child_joint(self, arg0: int, arg1: int) -> int:
        """
        Get the child joint of a rigid body given its index
        """
    def get_rigid_body_child_joint_count(self, arg0: int) -> int:
        """
        Gets the number of joints that are children to this rigid body
        """
    def get_rigid_body_linear_velocity(self, arg0: int) -> carb._carb.Float3:
        """
        Get the linear velocity of this rigid body in global coordinates
        """
    def get_rigid_body_local_linear_velocity(self, arg0: int) -> carb._carb.Float3:
        """
        Get the linear velocity of this rigid body in local coordinates
        """
    def get_rigid_body_name(self, arg0: int) -> str:
        """
        Gets the rigid body name given a handle
        """
    def get_rigid_body_parent_joint(self, arg0: int) -> int:
        """
        Gets parent joint to a rigid body
        """
    def get_rigid_body_path(self, arg0: int) -> str:
        """
        Gets the path to a rigid body given its handle
        """
    def get_rigid_body_pose(self, arg0: int) -> Transform:
        """
        Get the pose of a rigid body
        """
    @typing.overload
    def get_rigid_body_properties(self, arg0: int, arg1: RigidBodyProperties) -> bool:
        """
        Get Properties for a rigid body
        """
    @typing.overload
    def get_rigid_body_properties(self, arg0: int) -> typing.Any:
        """
        Get Properties for a rigid body
        """
    def is_simulating(self) -> bool:
        """
                    Returns:
                        bool: True if simulating, False otherwise
        """
    def peek_object_type(self, arg0: str) -> ObjectType:
        """
                    Returns:
                        string: The object type name as a string
        """
    def set_articulation_dof_efforts(self, arg0: int, arg1: numpy.ndarray[numpy.float32]) -> bool:
        """
        Sets efforts on an actor's degrees-of-freedom.
        """
    def set_articulation_dof_position_targets(self, arg0: int, arg1: numpy.ndarray[numpy.float32]) -> bool:
        """
        Sets an actor's degree-of-freedom position targets.
        """
    def set_articulation_dof_properties(self, arg0: int, arg1: numpy.ndarray[DofProperties]) -> bool:
        """
        Sets properties for an actor's degrees-of-freedom.
        """
    def set_articulation_dof_states(self, arg0: int, arg1: numpy.ndarray[DofState], arg2: int) -> bool:
        """
        Sets states for an actor's degrees-of-freedom.
        """
    def set_articulation_dof_velocity_targets(self, arg0: int, arg1: numpy.ndarray[numpy.float32]) -> bool:
        """
        Sets an actor's degree-of-freedom velocity targets.
        """
    def set_articulation_properties(self, arg0: int, arg1: ArticulationProperties) -> bool:
        """
        Sets properties for articulation
        """
    def set_attractor_properties(self, arg0: int, arg1: AttractorProperties) -> bool:
        """
        Set properties for this attractor
        """
    def set_attractor_target(self, arg0: int, arg1: Transform) -> bool:
        """
        Set target pose for attractor
        """
    def set_d6_joint_properties(self, arg0: int, arg1: D6JointProperties) -> bool:
        """
        Modifies properties of the selected joint.
        """
    def set_dof_effort(self, arg0: int, arg1: float) -> bool:
        """
        Set effort on degree of freedom
        """
    def set_dof_position(self, arg0: int, arg1: float) -> bool:
        """
        Set position/rotation for this degree of freedom
        """
    def set_dof_position_target(self, arg0: int, arg1: float) -> bool:
        """
        Set position target for degree of freedom
        """
    def set_dof_properties(self, arg0: int, arg1: DofProperties) -> bool:
        """
        Set degree of freedom properties
        """
    def set_dof_state(self, arg0: int, arg1: DofState, arg2: int) -> bool:
        """
        Set degree of freedom state
        """
    def set_dof_velocity(self, arg0: int, arg1: float) -> bool:
        """
        Set linear angular velocity of degree of freedom
        """
    def set_dof_velocity_target(self, arg0: int, arg1: float) -> bool:
        """
        Set velocity target for degree of freedom
        """
    def set_origin_offset(self, arg0: int, arg1: carb._carb.Float3) -> bool:
        """
        Offset origin for a rigid body
        """
    def set_rigid_body_angular_velocity(self, arg0: int, arg1: carb._carb.Float3) -> bool:
        """
        Set the angular velocity of this rigid body
        """
    def set_rigid_body_disable_gravity(self, arg0: int, arg1: bool) -> bool:
        """
        enables or disables the force of gravity from the given body
        """
    def set_rigid_body_disable_simulation(self, arg0: int, arg1: bool) -> bool:
        """
        enables or disables Simulation of a given rigid body
        """
    def set_rigid_body_linear_velocity(self, arg0: int, arg1: carb._carb.Float3) -> bool:
        """
        Set the linear velocity of the rigid body
        """
    def set_rigid_body_pose(self, arg0: int, arg1: Transform) -> bool:
        """
        Set the pose of a rigid body
        """
    def set_rigid_body_properties(self, arg0: int, arg1: RigidBodyProperties) -> bool:
        """
        Set Properties for a rigid body
        """
    def sleep_articulation(self, arg0: int) -> bool:
        """
        Put articulation to sleep
        """
    def sleep_rigid_body(self, arg0: int) -> bool:
        """
        Put rigid body to sleep
        """
    def wake_up_articulation(self, arg0: int) -> bool:
        """
        Enable physics for a articulation
        """
    def wake_up_rigid_body(self, arg0: int) -> bool:
        """
        Enable physics for a rigid body
        """
class JointType:
    """
    Joint Types that can be specified
    
    Members:
    
      JOINT_NONE : invalid/unknown/uninitialized joint type
    
      JOINT_FIXED : Fixed Joint
    
      JOINT_REVOLUTE : Revolute Joint
    
      JOINT_PRISMATIC : Prismatic Joint
    
      JOINT_SPHERICAL : Spherical Joint
    """
    JOINT_FIXED: typing.ClassVar[JointType]  # value = <JointType.JOINT_FIXED: 1>
    JOINT_NONE: typing.ClassVar[JointType]  # value = <JointType.JOINT_NONE: 0>
    JOINT_PRISMATIC: typing.ClassVar[JointType]  # value = <JointType.JOINT_PRISMATIC: 3>
    JOINT_REVOLUTE: typing.ClassVar[JointType]  # value = <JointType.JOINT_REVOLUTE: 2>
    JOINT_SPHERICAL: typing.ClassVar[JointType]  # value = <JointType.JOINT_SPHERICAL: 4>
    __members__: typing.ClassVar[dict[str, JointType]]  # value = {'JOINT_NONE': <JointType.JOINT_NONE: 0>, 'JOINT_FIXED': <JointType.JOINT_FIXED: 1>, 'JOINT_REVOLUTE': <JointType.JOINT_REVOLUTE: 2>, 'JOINT_PRISMATIC': <JointType.JOINT_PRISMATIC: 3>, 'JOINT_SPHERICAL': <JointType.JOINT_SPHERICAL: 4>}
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
class ObjectType:
    """
    Types of Objects
    
    Members:
    
      OBJECT_NONE : Invalid/unknown/uninitialized object type
    
      OBJECT_RIGIDBODY : The object is a rigid body or a link on an articulation
    
      OBJECT_JOINT : The object is a joint
    
      OBJECT_DOF : The object is a degree of freedon
    
      OBJECT_ARTICULATION : The object is an articulation
    
      OBJECT_ATTRACTOR : The object is an attractor
    
      OBJECT_D6JOINT : The object is a generic D6 joint
    """
    OBJECT_ARTICULATION: typing.ClassVar[ObjectType]  # value = <ObjectType.OBJECT_ARTICULATION: 4>
    OBJECT_ATTRACTOR: typing.ClassVar[ObjectType]  # value = <ObjectType.OBJECT_ATTRACTOR: 5>
    OBJECT_D6JOINT: typing.ClassVar[ObjectType]  # value = <ObjectType.OBJECT_D6JOINT: 6>
    OBJECT_DOF: typing.ClassVar[ObjectType]  # value = <ObjectType.OBJECT_DOF: 3>
    OBJECT_JOINT: typing.ClassVar[ObjectType]  # value = <ObjectType.OBJECT_JOINT: 2>
    OBJECT_NONE: typing.ClassVar[ObjectType]  # value = <ObjectType.OBJECT_NONE: 0>
    OBJECT_RIGIDBODY: typing.ClassVar[ObjectType]  # value = <ObjectType.OBJECT_RIGIDBODY: 1>
    __members__: typing.ClassVar[dict[str, ObjectType]]  # value = {'OBJECT_NONE': <ObjectType.OBJECT_NONE: 0>, 'OBJECT_RIGIDBODY': <ObjectType.OBJECT_RIGIDBODY: 1>, 'OBJECT_JOINT': <ObjectType.OBJECT_JOINT: 2>, 'OBJECT_DOF': <ObjectType.OBJECT_DOF: 3>, 'OBJECT_ARTICULATION': <ObjectType.OBJECT_ARTICULATION: 4>, 'OBJECT_ATTRACTOR': <ObjectType.OBJECT_ATTRACTOR: 5>, 'OBJECT_D6JOINT': <ObjectType.OBJECT_D6JOINT: 6>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
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
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class RigidBodyProperties:
    """
    Rigid Body Properties
    """
    def __getstate__(self) -> tuple:
        ...
    def __init__(self) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    @property
    def cMassLocalPose(self) -> carb._carb.Float3:
        """
        Local center of mass position (:obj:`carb._carb.Float3`)
        """
    @cMassLocalPose.setter
    def cMassLocalPose(self, arg0: carb._carb.Float3) -> None:
        ...
    @property
    def mass(self) -> float:
        """
        Mass of rigid body (:obj:`float`)
        """
    @mass.setter
    def mass(self, arg0: float) -> None:
        ...
    @property
    def max_contact_impulse(self) -> float:
        """
        Sets a limit on the impulse that may be applied at a contact. (:obj:`float`)
        """
    @max_contact_impulse.setter
    def max_contact_impulse(self, arg0: float) -> None:
        ...
    @property
    def max_depeneration_velocity(self) -> float:
        """
        This value controls how much velocity the solver can introduce to correct for penetrations in contacts. (:obj:`float`)
        """
    @max_depeneration_velocity.setter
    def max_depeneration_velocity(self, arg0: float) -> None:
        ...
    @property
    def moment(self) -> carb._carb.Float3:
        """
        Diagonal moment of inertia (:obj:`carb._carb.Float3`)
        """
    @moment.setter
    def moment(self, arg0: carb._carb.Float3) -> None:
        ...
    @property
    def solver_position_iteration_count(self) -> int:
        """
        Position solver iterations (:obj:`int`)
        """
    @solver_position_iteration_count.setter
    def solver_position_iteration_count(self, arg0: int) -> None:
        ...
    @property
    def solver_velocity_iteration_count(self) -> int:
        """
        Velocity solver iterations (:obj:`int`)
        """
    @solver_velocity_iteration_count.setter
    def solver_velocity_iteration_count(self, arg0: int) -> None:
        ...
class RigidBodyState:
    """
    Containing states to get/set for a rigid body in the simulation
    """
    dtype: typing.ClassVar[numpy.dtypes.VoidDType]  # value = dtype([('pose', [('p', [('x', '<f4'), ('y', '<f4'), ('z', '<f4')]), ('r', [('x', '<f4'), ('y', '<f4'), ('z', '<f4'), ('w', '<f4')])]), ('vel', [('linear', [('x', '<f4'), ('y', '<f4'), ('z', '<f4')]), ('angular', [('x', '<f4'), ('y', '<f4'), ('z', '<f4')])])])
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self, pose: Transform = None, vel: Velocity = None) -> None:
        """
        Initialize rigid body state from pose and velocity
        """
    @typing.overload
    def __init__(self) -> None:
        """
        initialize from another RigidBodyState
        """
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    @property
    def pose(self) -> Transform:
        """
        Transform with position and orientation of rigid body (:obj:`omni.isaac.dynamic_control._dynamic_control.Transform`)
        """
    @pose.setter
    def pose(self, arg0: Transform) -> None:
        ...
    @property
    def vel(self) -> Velocity:
        """
        Linear and angular velocities of rigid body (:obj:`omni.isaac.dynamic_control._dynamic_control.Velocity`)
        """
    @vel.setter
    def vel(self, arg0: Velocity) -> None:
        ...
class Transform:
    """
    Represents a 3D transform in the system
    """
    __hash__: typing.ClassVar[None] = None
    dtype: typing.ClassVar[numpy.dtypes.VoidDType]  # value = dtype([('p', [('x', '<f4'), ('y', '<f4'), ('z', '<f4')]), ('r', [('x', '<f4'), ('y', '<f4'), ('z', '<f4'), ('w', '<f4')])])
    @staticmethod
    def from_buffer(arg0: typing_extensions.Buffer) -> typing.Any:
        """
        assign a transform from an array of 7 values [p.x, p.y, p.z, r.x, r.y, r.z, r.w]
        """
    def __eq__(self, arg0: Transform) -> bool:
        ...
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self, p: carb._carb.Float3 = None, r: carb._carb.Float4 = None) -> None:
        """
        Initialize from a position and a rotation quaternion
        """
    @typing.overload
    def __init__(self) -> None:
        """
        Initialize from another Transform object
        """
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    @property
    def p(self) -> carb._carb.Float3:
        """
        Position as a tuple of (x,y,z) (:obj:`carb._carb.Float3`)
        """
    @p.setter
    def p(self, arg0: carb._carb.Float3) -> None:
        ...
    @property
    def r(self) -> carb._carb.Float4:
        """
        Rotation Quaternion, represented in the format :math:`x\\hat{i} + y\\hat{j} + z\\hat{k} + w` (:obj:`carb._carb.Float4`)
        """
    @r.setter
    def r(self, arg0: carb._carb.Float4) -> None:
        ...
class Velocity:
    """
    Linear and angular velocity
    """
    dtype: typing.ClassVar[numpy.dtypes.VoidDType]  # value = dtype([('linear', [('x', '<f4'), ('y', '<f4'), ('z', '<f4')]), ('angular', [('x', '<f4'), ('y', '<f4'), ('z', '<f4')])])
    def __getstate__(self) -> tuple:
        ...
    @typing.overload
    def __init__(self, linear: carb._carb.Float3 = None, angular: carb._carb.Float3 = None) -> None:
        """
        initialize from a linear velocity and angular velocity
        """
    @typing.overload
    def __init__(self) -> None:
        """
        initialize from another Velocity Object
        """
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    @property
    def angular(self) -> carb._carb.Float3:
        """
        Angular 3D velocity as a tuple (x,y,z), (:obj:`carb._carb.Float3`)
        """
    @angular.setter
    def angular(self, arg0: carb._carb.Float3) -> None:
        ...
    @property
    def linear(self) -> carb._carb.Float3:
        """
        Linear 3D velocity as a tuple (x,y,z) , (:obj:`carb._carb.Float3`)
        """
    @linear.setter
    def linear(self, arg0: carb._carb.Float3) -> None:
        ...
def acquire_dynamic_control_interface(plugin_name: str = None, library_path: str = None) -> ...:
    """
    Acquire dynamic control interface. This is the base object that all of the dynamic control functions are defined on
    """
def release_dynamic_control_interface(arg0: ...) -> None:
    """
    Release dynamic control interface. Generally this does not need to be called, the dynamic control interface is released on extension shutdown
    """
AXIS_ALL: int = 63
AXIS_ALL_ROTATION: int = 56
AXIS_ALL_TRANSLATION: int = 7
AXIS_NONE: int = 0
AXIS_SWING_1: int = 16
AXIS_SWING_2: int = 32
AXIS_TWIST: int = 8
AXIS_X: int = 1
AXIS_Y: int = 2
AXIS_Z: int = 4
DOF_NONE: DofType  # value = <DofType.DOF_NONE: 0>
DOF_ROTATION: DofType  # value = <DofType.DOF_ROTATION: 1>
DOF_TRANSLATION: DofType  # value = <DofType.DOF_TRANSLATION: 2>
DRIVE_ACCELERATION: DriveMode  # value = <DriveMode.DRIVE_ACCELERATION: 1>
DRIVE_FORCE: DriveMode  # value = <DriveMode.DRIVE_FORCE: 0>
INVALID_HANDLE: int = 0
JOINT_FIXED: JointType  # value = <JointType.JOINT_FIXED: 1>
JOINT_NONE: JointType  # value = <JointType.JOINT_NONE: 0>
JOINT_PRISMATIC: JointType  # value = <JointType.JOINT_PRISMATIC: 3>
JOINT_REVOLUTE: JointType  # value = <JointType.JOINT_REVOLUTE: 2>
JOINT_SPHERICAL: JointType  # value = <JointType.JOINT_SPHERICAL: 4>
OBJECT_ARTICULATION: ObjectType  # value = <ObjectType.OBJECT_ARTICULATION: 4>
OBJECT_ATTRACTOR: ObjectType  # value = <ObjectType.OBJECT_ATTRACTOR: 5>
OBJECT_D6JOINT: ObjectType  # value = <ObjectType.OBJECT_D6JOINT: 6>
OBJECT_DOF: ObjectType  # value = <ObjectType.OBJECT_DOF: 3>
OBJECT_JOINT: ObjectType  # value = <ObjectType.OBJECT_JOINT: 2>
OBJECT_NONE: ObjectType  # value = <ObjectType.OBJECT_NONE: 0>
OBJECT_RIGIDBODY: ObjectType  # value = <ObjectType.OBJECT_RIGIDBODY: 1>
STATE_ALL: int = 7
STATE_EFFORT: int = 4
STATE_NONE: int = 0
STATE_POS: int = 1
STATE_VEL: int = 2
