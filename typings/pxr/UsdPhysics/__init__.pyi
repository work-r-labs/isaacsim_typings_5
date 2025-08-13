from __future__ import annotations
import pxr.Usd
import pxr.UsdGeom
import typing
__all__: list[str] = ['ArticulationDesc', 'ArticulationDescVector', 'ArticulationRootAPI', 'Axis', 'Capsule1ShapeDesc', 'Capsule1ShapeDescVector', 'CapsuleShapeDesc', 'CapsuleShapeDescVector', 'CollisionAPI', 'CollisionGroup', 'CollisionGroupDesc', 'CollisionGroupDescVector', 'CollisionGroupTable', 'ConeShapeDesc', 'ConeShapeDescVector', 'CubeShapeDesc', 'CubeShapeDescVector', 'CustomJointDesc', 'CustomJointDescVector', 'CustomShapeDesc', 'CustomShapeDescVector', 'CustomUsdPhysicsTokens', 'Cylinder1ShapeDesc', 'Cylinder1ShapeDescVector', 'CylinderShapeDesc', 'CylinderShapeDescVector', 'D6JointDesc', 'D6JointDescVector', 'DistanceJoint', 'DistanceJointDesc', 'DistanceJointDescVector', 'DriveAPI', 'FilteredPairsAPI', 'FixedJoint', 'FixedJointDesc', 'FixedJointDescVector', 'Joint', 'JointDOF', 'JointDesc', 'JointDescVector', 'JointDrive', 'JointDriveDOFPair', 'JointLimit', 'JointLimitDOFPair', 'LimitAPI', 'MassAPI', 'MassUnits', 'MaterialAPI', 'MeshCollisionAPI', 'MeshShapeDesc', 'MeshShapeDescVector', 'ObjectDesc', 'ObjectType', 'PhysicsCollectionMembershipQueryVector', 'PhysicsJointDriveDOFVector', 'PhysicsJointLimitDOFVector', 'PhysicsSpherePointVector', 'PlaneShapeDesc', 'PlaneShapeDescVector', 'PrismaticJoint', 'PrismaticJointDesc', 'PrismaticJointDescVector', 'RevoluteJoint', 'RevoluteJointDesc', 'RevoluteJointDescVector', 'RigidBodyAPI', 'RigidBodyDesc', 'RigidBodyDescVector', 'RigidBodyMaterialDesc', 'RigidBodyMaterialDescVector', 'Scene', 'SceneDesc', 'SceneDescVector', 'ShapeDesc', 'SpherePoint', 'SpherePointsShapeDesc', 'SpherePointsShapeDescVector', 'SphereShapeDesc', 'SphereShapeDescVector', 'SphericalJoint', 'SphericalJointDesc', 'SphericalJointDescVector', 'Tokens']
class ArticulationDesc(ObjectDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def articulatedBodies(*args, **kwargs):
        ...
    @property
    def articulatedJoints(*args, **kwargs):
        ...
    @property
    def filteredCollisions(*args, **kwargs):
        ...
    @property
    def rootPrims(*args, **kwargs):
        ...
class ArticulationDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class ArticulationRootAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Axis(Boost.Python.enum):
    X: typing.ClassVar[Axis]  # value = pxr.UsdPhysics.Axis.X
    Y: typing.ClassVar[Axis]  # value = pxr.UsdPhysics.Axis.Y
    Z: typing.ClassVar[Axis]  # value = pxr.UsdPhysics.Axis.Z
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'X': pxr.UsdPhysics.Axis.X, 'Y': pxr.UsdPhysics.Axis.Y, 'Z': pxr.UsdPhysics.Axis.Z}
    values: typing.ClassVar[dict]  # value = {0: pxr.UsdPhysics.Axis.X, 1: pxr.UsdPhysics.Axis.Y, 2: pxr.UsdPhysics.Axis.Z}
class Capsule1ShapeDesc(ShapeDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def axis(*args, **kwargs):
        ...
    @property
    def bottomRadius(*args, **kwargs):
        ...
    @property
    def halfHeight(*args, **kwargs):
        ...
    @property
    def topRadius(*args, **kwargs):
        ...
class Capsule1ShapeDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class CapsuleShapeDesc(ShapeDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def axis(*args, **kwargs):
        ...
    @property
    def halfHeight(*args, **kwargs):
        ...
    @property
    def radius(*args, **kwargs):
        ...
class CapsuleShapeDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class CollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSimulationOwnerRel(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSimulationOwnerRel(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class CollisionGroup(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def ComputeCollisionGroupTable(*args, **kwargs):
        ...
    @staticmethod
    def CreateFilteredGroupsRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateInvertFilteredGroupsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMergeGroupNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCollidersCollectionAPI(*args, **kwargs):
        ...
    @staticmethod
    def GetFilteredGroupsRel(*args, **kwargs):
        ...
    @staticmethod
    def GetInvertFilteredGroupsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMergeGroupNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class CollisionGroupDesc(ObjectDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def filteredGroups(*args, **kwargs):
        ...
    @property
    def invertFilteredGroups(*args, **kwargs):
        ...
    @property
    def mergeGroupName(*args, **kwargs):
        ...
    @property
    def mergedGroups(*args, **kwargs):
        ...
class CollisionGroupDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class CollisionGroupTable(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 88
    @staticmethod
    def GetGroups(*args, **kwargs):
        ...
    @staticmethod
    def IsCollisionEnabled(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ConeShapeDesc(ShapeDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def axis(*args, **kwargs):
        ...
    @property
    def halfHeight(*args, **kwargs):
        ...
    @property
    def radius(*args, **kwargs):
        ...
class ConeShapeDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class CubeShapeDesc(ShapeDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def halfExtents(*args, **kwargs):
        ...
class CubeShapeDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class CustomJointDesc(JointDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class CustomJointDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class CustomShapeDesc(ShapeDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def customGeometryToken(*args, **kwargs):
        ...
class CustomShapeDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class CustomUsdPhysicsTokens(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def instancerTokens(*args, **kwargs):
        ...
    @instancerTokens.setter
    def instancerTokens(*args, **kwargs):
        ...
    @property
    def jointTokens(*args, **kwargs):
        ...
    @jointTokens.setter
    def jointTokens(*args, **kwargs):
        ...
    @property
    def shapeTokens(*args, **kwargs):
        ...
    @shapeTokens.setter
    def shapeTokens(*args, **kwargs):
        ...
class Cylinder1ShapeDesc(ShapeDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def axis(*args, **kwargs):
        ...
    @property
    def bottomRadius(*args, **kwargs):
        ...
    @property
    def halfHeight(*args, **kwargs):
        ...
    @property
    def topRadius(*args, **kwargs):
        ...
class Cylinder1ShapeDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class CylinderShapeDesc(ShapeDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def axis(*args, **kwargs):
        ...
    @property
    def halfHeight(*args, **kwargs):
        ...
    @property
    def radius(*args, **kwargs):
        ...
class CylinderShapeDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class D6JointDesc(JointDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def jointDrives(*args, **kwargs):
        ...
    @property
    def jointLimits(*args, **kwargs):
        ...
class D6JointDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class DistanceJoint(Joint):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateMaxDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class DistanceJointDesc(JointDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def limit(*args, **kwargs):
        ...
    @property
    def maxEnabled(*args, **kwargs):
        ...
    @property
    def minEnabled(*args, **kwargs):
        ...
class DistanceJointDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class DriveAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxForceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTargetPositionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTargetVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAll(*args, **kwargs):
        ...
    @staticmethod
    def GetDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxForceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTargetPositionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTargetVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysicsDriveAPIPath(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class FilteredPairsAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateFilteredPairsRel(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetFilteredPairsRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class FixedJoint(Joint):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class FixedJointDesc(JointDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class FixedJointDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class Joint(pxr.UsdGeom.Imageable):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateBody0Rel(*args, **kwargs):
        ...
    @staticmethod
    def CreateBody1Rel(*args, **kwargs):
        ...
    @staticmethod
    def CreateBreakForceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateBreakTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateExcludeFromArticulationAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateJointEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLocalPos0Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLocalPos1Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLocalRot0Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLocalRot1Attr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetBody0Rel(*args, **kwargs):
        ...
    @staticmethod
    def GetBody1Rel(*args, **kwargs):
        ...
    @staticmethod
    def GetBreakForceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetBreakTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetExcludeFromArticulationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetJointEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLocalPos0Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetLocalPos1Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetLocalRot0Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetLocalRot1Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class JointDOF(Boost.Python.enum):
    Distance: typing.ClassVar[JointDOF]  # value = pxr.UsdPhysics.JointDOF.Distance
    RotX: typing.ClassVar[JointDOF]  # value = pxr.UsdPhysics.JointDOF.RotX
    RotY: typing.ClassVar[JointDOF]  # value = pxr.UsdPhysics.JointDOF.RotY
    RotZ: typing.ClassVar[JointDOF]  # value = pxr.UsdPhysics.JointDOF.RotZ
    TransX: typing.ClassVar[JointDOF]  # value = pxr.UsdPhysics.JointDOF.TransX
    TransY: typing.ClassVar[JointDOF]  # value = pxr.UsdPhysics.JointDOF.TransY
    TransZ: typing.ClassVar[JointDOF]  # value = pxr.UsdPhysics.JointDOF.TransZ
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'Distance': pxr.UsdPhysics.JointDOF.Distance, 'TransX': pxr.UsdPhysics.JointDOF.TransX, 'TransY': pxr.UsdPhysics.JointDOF.TransY, 'TransZ': pxr.UsdPhysics.JointDOF.TransZ, 'RotX': pxr.UsdPhysics.JointDOF.RotX, 'RotY': pxr.UsdPhysics.JointDOF.RotY, 'RotZ': pxr.UsdPhysics.JointDOF.RotZ}
    values: typing.ClassVar[dict]  # value = {0: pxr.UsdPhysics.JointDOF.Distance, 1: pxr.UsdPhysics.JointDOF.TransX, 2: pxr.UsdPhysics.JointDOF.TransY, 3: pxr.UsdPhysics.JointDOF.TransZ, 4: pxr.UsdPhysics.JointDOF.RotX, 5: pxr.UsdPhysics.JointDOF.RotY, 6: pxr.UsdPhysics.JointDOF.RotZ}
class JointDesc(ObjectDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def body0(*args, **kwargs):
        ...
    @property
    def body1(*args, **kwargs):
        ...
    @property
    def breakForce(*args, **kwargs):
        ...
    @property
    def breakTorque(*args, **kwargs):
        ...
    @property
    def collisionEnabled(*args, **kwargs):
        ...
    @property
    def excludeFromArticulation(*args, **kwargs):
        ...
    @property
    def jointEnabled(*args, **kwargs):
        ...
    @property
    def localPose0Orientation(*args, **kwargs):
        ...
    @property
    def localPose0Position(*args, **kwargs):
        ...
    @property
    def localPose1Orientation(*args, **kwargs):
        ...
    @property
    def localPose1Position(*args, **kwargs):
        ...
    @property
    def rel0(*args, **kwargs):
        ...
    @property
    def rel1(*args, **kwargs):
        ...
class JointDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class JointDrive(Boost.Python.instance):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def acceleration(*args, **kwargs):
        ...
    @property
    def damping(*args, **kwargs):
        ...
    @property
    def enabled(*args, **kwargs):
        ...
    @property
    def forceLimit(*args, **kwargs):
        ...
    @property
    def stiffness(*args, **kwargs):
        ...
    @property
    def targetPosition(*args, **kwargs):
        ...
    @property
    def targetVelocity(*args, **kwargs):
        ...
class JointDriveDOFPair(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def first(*args, **kwargs):
        ...
    @first.setter
    def first(*args, **kwargs):
        ...
    @property
    def second(*args, **kwargs):
        ...
    @second.setter
    def second(*args, **kwargs):
        ...
class JointLimit(Boost.Python.instance):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def enabled(*args, **kwargs):
        ...
    @property
    def lower(*args, **kwargs):
        ...
    @property
    def upper(*args, **kwargs):
        ...
class JointLimitDOFPair(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def first(*args, **kwargs):
        ...
    @first.setter
    def first(*args, **kwargs):
        ...
    @property
    def second(*args, **kwargs):
        ...
    @second.setter
    def second(*args, **kwargs):
        ...
class LimitAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateHighAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLowAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAll(*args, **kwargs):
        ...
    @staticmethod
    def GetHighAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLowAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysicsLimitAPIPath(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class MassAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateCenterOfMassAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDiagonalInertiaAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMassAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePrincipalAxesAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCenterOfMassAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDiagonalInertiaAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMassAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPrincipalAxesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class MassUnits(Boost.Python.instance):
    grams: typing.ClassVar[float] = 0.001
    kilograms: typing.ClassVar[float] = 1.0
    slugs: typing.ClassVar[float] = 14.5939
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class MaterialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateDensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDynamicFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRestitutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStaticFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDynamicFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRestitutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetStaticFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class MeshCollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateApproximationAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetApproximationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class MeshShapeDesc(ShapeDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def approximation(*args, **kwargs):
        ...
    @property
    def doubleSided(*args, **kwargs):
        ...
    @property
    def meshScale(*args, **kwargs):
        ...
class MeshShapeDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class ObjectDesc(Boost.Python.instance):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def isValid(*args, **kwargs):
        ...
    @property
    def primPath(*args, **kwargs):
        ...
    @property
    def type(*args, **kwargs):
        ...
class ObjectType(Boost.Python.enum):
    Articulation: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.Articulation
    Capsule1Shape: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.Capsule1Shape
    CapsuleShape: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.CapsuleShape
    CollisionGroup: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.CollisionGroup
    ConeShape: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.ConeShape
    CubeShape: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.CubeShape
    CustomJoint: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.CustomJoint
    CustomShape: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.CustomShape
    Cylinder1Shape: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.Cylinder1Shape
    CylinderShape: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.CylinderShape
    D6Joint: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.D6Joint
    DistanceJoint: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.DistanceJoint
    FixedJoint: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.FixedJoint
    MeshShape: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.MeshShape
    PlaneShape: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.PlaneShape
    PrismaticJoint: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.PrismaticJoint
    RevoluteJoint: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.RevoluteJoint
    RigidBody: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.RigidBody
    RigidBodyMaterial: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.RigidBodyMaterial
    Scene: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.Scene
    SpherePointsShape: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.SpherePointsShape
    SphereShape: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.SphereShape
    SphericalJoint: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.SphericalJoint
    Undefined: typing.ClassVar[ObjectType]  # value = pxr.UsdPhysics.ObjectType.Undefined
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'Undefined': pxr.UsdPhysics.ObjectType.Undefined, 'Scene': pxr.UsdPhysics.ObjectType.Scene, 'RigidBody': pxr.UsdPhysics.ObjectType.RigidBody, 'SphereShape': pxr.UsdPhysics.ObjectType.SphereShape, 'CubeShape': pxr.UsdPhysics.ObjectType.CubeShape, 'CapsuleShape': pxr.UsdPhysics.ObjectType.CapsuleShape, 'Capsule1Shape': pxr.UsdPhysics.ObjectType.Capsule1Shape, 'CylinderShape': pxr.UsdPhysics.ObjectType.CylinderShape, 'Cylinder1Shape': pxr.UsdPhysics.ObjectType.Cylinder1Shape, 'ConeShape': pxr.UsdPhysics.ObjectType.ConeShape, 'MeshShape': pxr.UsdPhysics.ObjectType.MeshShape, 'PlaneShape': pxr.UsdPhysics.ObjectType.PlaneShape, 'CustomShape': pxr.UsdPhysics.ObjectType.CustomShape, 'SpherePointsShape': pxr.UsdPhysics.ObjectType.SpherePointsShape, 'FixedJoint': pxr.UsdPhysics.ObjectType.FixedJoint, 'RevoluteJoint': pxr.UsdPhysics.ObjectType.RevoluteJoint, 'PrismaticJoint': pxr.UsdPhysics.ObjectType.PrismaticJoint, 'SphericalJoint': pxr.UsdPhysics.ObjectType.SphericalJoint, 'DistanceJoint': pxr.UsdPhysics.ObjectType.DistanceJoint, 'D6Joint': pxr.UsdPhysics.ObjectType.D6Joint, 'CustomJoint': pxr.UsdPhysics.ObjectType.CustomJoint, 'RigidBodyMaterial': pxr.UsdPhysics.ObjectType.RigidBodyMaterial, 'Articulation': pxr.UsdPhysics.ObjectType.Articulation, 'CollisionGroup': pxr.UsdPhysics.ObjectType.CollisionGroup}
    values: typing.ClassVar[dict]  # value = {0: pxr.UsdPhysics.ObjectType.Undefined, 1: pxr.UsdPhysics.ObjectType.Scene, 2: pxr.UsdPhysics.ObjectType.RigidBody, 3: pxr.UsdPhysics.ObjectType.SphereShape, 4: pxr.UsdPhysics.ObjectType.CubeShape, 5: pxr.UsdPhysics.ObjectType.CapsuleShape, 6: pxr.UsdPhysics.ObjectType.Capsule1Shape, 7: pxr.UsdPhysics.ObjectType.CylinderShape, 8: pxr.UsdPhysics.ObjectType.Cylinder1Shape, 9: pxr.UsdPhysics.ObjectType.ConeShape, 10: pxr.UsdPhysics.ObjectType.MeshShape, 11: pxr.UsdPhysics.ObjectType.PlaneShape, 12: pxr.UsdPhysics.ObjectType.CustomShape, 13: pxr.UsdPhysics.ObjectType.SpherePointsShape, 14: pxr.UsdPhysics.ObjectType.FixedJoint, 15: pxr.UsdPhysics.ObjectType.RevoluteJoint, 16: pxr.UsdPhysics.ObjectType.PrismaticJoint, 17: pxr.UsdPhysics.ObjectType.SphericalJoint, 18: pxr.UsdPhysics.ObjectType.DistanceJoint, 19: pxr.UsdPhysics.ObjectType.D6Joint, 20: pxr.UsdPhysics.ObjectType.CustomJoint, 21: pxr.UsdPhysics.ObjectType.RigidBodyMaterial, 22: pxr.UsdPhysics.ObjectType.Articulation, 23: pxr.UsdPhysics.ObjectType.CollisionGroup}
class PhysicsCollectionMembershipQueryVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class PhysicsJointDriveDOFVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class PhysicsJointLimitDOFVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class PhysicsSpherePointVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class PlaneShapeDesc(ShapeDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def axis(*args, **kwargs):
        ...
class PlaneShapeDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class PrismaticJoint(Joint):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLowerLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUpperLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLowerLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetUpperLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class PrismaticJointDesc(JointDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def axis(*args, **kwargs):
        ...
    @property
    def drive(*args, **kwargs):
        ...
    @property
    def limit(*args, **kwargs):
        ...
class PrismaticJointDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class RevoluteJoint(Joint):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLowerLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUpperLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLowerLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetUpperLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class RevoluteJointDesc(JointDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def axis(*args, **kwargs):
        ...
    @property
    def drive(*args, **kwargs):
        ...
    @property
    def limit(*args, **kwargs):
        ...
class RevoluteJointDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class RigidBodyAPI(pxr.Usd.APISchemaBase):
    class MassInformation(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 104
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @property
        def centerOfMass(*args, **kwargs):
            ...
        @centerOfMass.setter
        def centerOfMass(*args, **kwargs):
            ...
        @property
        def inertia(*args, **kwargs):
            ...
        @inertia.setter
        def inertia(*args, **kwargs):
            ...
        @property
        def localPos(*args, **kwargs):
            ...
        @localPos.setter
        def localPos(*args, **kwargs):
            ...
        @property
        def localRot(*args, **kwargs):
            ...
        @localRot.setter
        def localRot(*args, **kwargs):
            ...
        @property
        def volume(*args, **kwargs):
            ...
        @volume.setter
        def volume(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def ComputeMassProperties(*args, **kwargs):
        ...
    @staticmethod
    def CreateAngularVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateKinematicEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRigidBodyEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSimulationOwnerRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateStartsAsleepAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAngularVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetKinematicEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRigidBodyEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSimulationOwnerRel(*args, **kwargs):
        ...
    @staticmethod
    def GetStartsAsleepAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class RigidBodyDesc(ObjectDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def angularVelocity(*args, **kwargs):
        ...
    @property
    def collisions(*args, **kwargs):
        ...
    @property
    def filteredCollisions(*args, **kwargs):
        ...
    @property
    def kinematicBody(*args, **kwargs):
        ...
    @property
    def linearVelocity(*args, **kwargs):
        ...
    @property
    def position(*args, **kwargs):
        ...
    @property
    def rigidBodyEnabled(*args, **kwargs):
        ...
    @property
    def rotation(*args, **kwargs):
        ...
    @property
    def scale(*args, **kwargs):
        ...
    @property
    def simulationOwners(*args, **kwargs):
        ...
    @property
    def startsAsleep(*args, **kwargs):
        ...
class RigidBodyDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class RigidBodyMaterialDesc(ObjectDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def density(*args, **kwargs):
        ...
    @property
    def dynamicFriction(*args, **kwargs):
        ...
    @property
    def restitution(*args, **kwargs):
        ...
    @property
    def staticFriction(*args, **kwargs):
        ...
class RigidBodyMaterialDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class Scene(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateGravityDirectionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGravityMagnitudeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetGravityDirectionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGravityMagnitudeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class SceneDesc(ObjectDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def gravityDirection(*args, **kwargs):
        ...
    @property
    def gravityMagnitude(*args, **kwargs):
        ...
class SceneDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class ShapeDesc(ObjectDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def collisionEnabled(*args, **kwargs):
        ...
    @property
    def collisionGroups(*args, **kwargs):
        ...
    @property
    def filteredCollisions(*args, **kwargs):
        ...
    @property
    def localPos(*args, **kwargs):
        ...
    @property
    def localRot(*args, **kwargs):
        ...
    @property
    def localScale(*args, **kwargs):
        ...
    @property
    def materials(*args, **kwargs):
        ...
    @property
    def rigidBody(*args, **kwargs):
        ...
    @property
    def simulationOwners(*args, **kwargs):
        ...
class SpherePoint(Boost.Python.instance):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def center(*args, **kwargs):
        ...
    @property
    def radius(*args, **kwargs):
        ...
class SpherePointsShapeDesc(ShapeDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def spherePoints(*args, **kwargs):
        ...
class SpherePointsShapeDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class SphereShapeDesc(ShapeDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def radius(*args, **kwargs):
        ...
class SphereShapeDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class SphericalJoint(Joint):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateConeAngle0LimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateConeAngle1LimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetConeAngle0LimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetConeAngle1LimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class SphericalJointDesc(JointDesc):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def axis(*args, **kwargs):
        ...
    @property
    def limit(*args, **kwargs):
        ...
class SphericalJointDescVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def extend(*args, **kwargs):
        ...
class Tokens(Boost.Python.instance):
    PhysicsArticulationRootAPI: typing.ClassVar[str] = 'PhysicsArticulationRootAPI'
    PhysicsCollisionAPI: typing.ClassVar[str] = 'PhysicsCollisionAPI'
    PhysicsCollisionGroup: typing.ClassVar[str] = 'PhysicsCollisionGroup'
    PhysicsDistanceJoint: typing.ClassVar[str] = 'PhysicsDistanceJoint'
    PhysicsDriveAPI: typing.ClassVar[str] = 'PhysicsDriveAPI'
    PhysicsFilteredPairsAPI: typing.ClassVar[str] = 'PhysicsFilteredPairsAPI'
    PhysicsFixedJoint: typing.ClassVar[str] = 'PhysicsFixedJoint'
    PhysicsJoint: typing.ClassVar[str] = 'PhysicsJoint'
    PhysicsLimitAPI: typing.ClassVar[str] = 'PhysicsLimitAPI'
    PhysicsMassAPI: typing.ClassVar[str] = 'PhysicsMassAPI'
    PhysicsMaterialAPI: typing.ClassVar[str] = 'PhysicsMaterialAPI'
    PhysicsMeshCollisionAPI: typing.ClassVar[str] = 'PhysicsMeshCollisionAPI'
    PhysicsPrismaticJoint: typing.ClassVar[str] = 'PhysicsPrismaticJoint'
    PhysicsRevoluteJoint: typing.ClassVar[str] = 'PhysicsRevoluteJoint'
    PhysicsRigidBodyAPI: typing.ClassVar[str] = 'PhysicsRigidBodyAPI'
    PhysicsScene: typing.ClassVar[str] = 'PhysicsScene'
    PhysicsSphericalJoint: typing.ClassVar[str] = 'PhysicsSphericalJoint'
    acceleration: typing.ClassVar[str] = 'acceleration'
    angular: typing.ClassVar[str] = 'angular'
    boundingCube: typing.ClassVar[str] = 'boundingCube'
    boundingSphere: typing.ClassVar[str] = 'boundingSphere'
    colliders: typing.ClassVar[str] = 'colliders'
    convexDecomposition: typing.ClassVar[str] = 'convexDecomposition'
    convexHull: typing.ClassVar[str] = 'convexHull'
    distance: typing.ClassVar[str] = 'distance'
    drive: typing.ClassVar[str] = 'drive'
    drive_MultipleApplyTemplate_PhysicsDamping: typing.ClassVar[str] = 'drive:__INSTANCE_NAME__:physics:damping'
    drive_MultipleApplyTemplate_PhysicsMaxForce: typing.ClassVar[str] = 'drive:__INSTANCE_NAME__:physics:maxForce'
    drive_MultipleApplyTemplate_PhysicsStiffness: typing.ClassVar[str] = 'drive:__INSTANCE_NAME__:physics:stiffness'
    drive_MultipleApplyTemplate_PhysicsTargetPosition: typing.ClassVar[str] = 'drive:__INSTANCE_NAME__:physics:targetPosition'
    drive_MultipleApplyTemplate_PhysicsTargetVelocity: typing.ClassVar[str] = 'drive:__INSTANCE_NAME__:physics:targetVelocity'
    drive_MultipleApplyTemplate_PhysicsType: typing.ClassVar[str] = 'drive:__INSTANCE_NAME__:physics:type'
    force: typing.ClassVar[str] = 'force'
    kilogramsPerUnit: typing.ClassVar[str] = 'kilogramsPerUnit'
    limit: typing.ClassVar[str] = 'limit'
    limit_MultipleApplyTemplate_PhysicsHigh: typing.ClassVar[str] = 'limit:__INSTANCE_NAME__:physics:high'
    limit_MultipleApplyTemplate_PhysicsLow: typing.ClassVar[str] = 'limit:__INSTANCE_NAME__:physics:low'
    linear: typing.ClassVar[str] = 'linear'
    meshSimplification: typing.ClassVar[str] = 'meshSimplification'
    none: typing.ClassVar[str] = 'none'
    physicsAngularVelocity: typing.ClassVar[str] = 'physics:angularVelocity'
    physicsApproximation: typing.ClassVar[str] = 'physics:approximation'
    physicsAxis: typing.ClassVar[str] = 'physics:axis'
    physicsBody0: typing.ClassVar[str] = 'physics:body0'
    physicsBody1: typing.ClassVar[str] = 'physics:body1'
    physicsBreakForce: typing.ClassVar[str] = 'physics:breakForce'
    physicsBreakTorque: typing.ClassVar[str] = 'physics:breakTorque'
    physicsCenterOfMass: typing.ClassVar[str] = 'physics:centerOfMass'
    physicsCollisionEnabled: typing.ClassVar[str] = 'physics:collisionEnabled'
    physicsConeAngle0Limit: typing.ClassVar[str] = 'physics:coneAngle0Limit'
    physicsConeAngle1Limit: typing.ClassVar[str] = 'physics:coneAngle1Limit'
    physicsDensity: typing.ClassVar[str] = 'physics:density'
    physicsDiagonalInertia: typing.ClassVar[str] = 'physics:diagonalInertia'
    physicsDynamicFriction: typing.ClassVar[str] = 'physics:dynamicFriction'
    physicsExcludeFromArticulation: typing.ClassVar[str] = 'physics:excludeFromArticulation'
    physicsFilteredGroups: typing.ClassVar[str] = 'physics:filteredGroups'
    physicsFilteredPairs: typing.ClassVar[str] = 'physics:filteredPairs'
    physicsGravityDirection: typing.ClassVar[str] = 'physics:gravityDirection'
    physicsGravityMagnitude: typing.ClassVar[str] = 'physics:gravityMagnitude'
    physicsInvertFilteredGroups: typing.ClassVar[str] = 'physics:invertFilteredGroups'
    physicsJointEnabled: typing.ClassVar[str] = 'physics:jointEnabled'
    physicsKinematicEnabled: typing.ClassVar[str] = 'physics:kinematicEnabled'
    physicsLocalPos0: typing.ClassVar[str] = 'physics:localPos0'
    physicsLocalPos1: typing.ClassVar[str] = 'physics:localPos1'
    physicsLocalRot0: typing.ClassVar[str] = 'physics:localRot0'
    physicsLocalRot1: typing.ClassVar[str] = 'physics:localRot1'
    physicsLowerLimit: typing.ClassVar[str] = 'physics:lowerLimit'
    physicsMass: typing.ClassVar[str] = 'physics:mass'
    physicsMaxDistance: typing.ClassVar[str] = 'physics:maxDistance'
    physicsMergeGroup: typing.ClassVar[str] = 'physics:mergeGroup'
    physicsMinDistance: typing.ClassVar[str] = 'physics:minDistance'
    physicsPrincipalAxes: typing.ClassVar[str] = 'physics:principalAxes'
    physicsRestitution: typing.ClassVar[str] = 'physics:restitution'
    physicsRigidBodyEnabled: typing.ClassVar[str] = 'physics:rigidBodyEnabled'
    physicsSimulationOwner: typing.ClassVar[str] = 'physics:simulationOwner'
    physicsStartsAsleep: typing.ClassVar[str] = 'physics:startsAsleep'
    physicsStaticFriction: typing.ClassVar[str] = 'physics:staticFriction'
    physicsUpperLimit: typing.ClassVar[str] = 'physics:upperLimit'
    physicsVelocity: typing.ClassVar[str] = 'physics:velocity'
    rotX: typing.ClassVar[str] = 'rotX'
    rotY: typing.ClassVar[str] = 'rotY'
    rotZ: typing.ClassVar[str] = 'rotZ'
    transX: typing.ClassVar[str] = 'transX'
    transY: typing.ClassVar[str] = 'transY'
    transZ: typing.ClassVar[str] = 'transZ'
    x: typing.ClassVar[str] = 'X'
    y: typing.ClassVar[str] = 'Y'
    z: typing.ClassVar[str] = 'Z'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class _CanApplyResult(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def whyNot(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'usdPhysics'
