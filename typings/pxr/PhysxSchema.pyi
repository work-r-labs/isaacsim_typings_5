from __future__ import annotations
import pxr.Usd
import pxr.UsdGeom
import pxr.UsdPhysics
import typing
__all__ = ['JointStateAPI', 'PhysxArticulationAPI', 'PhysxAutoAttachmentAPI', 'PhysxAutoParticleClothAPI', 'PhysxCameraAPI', 'PhysxCameraDroneAPI', 'PhysxCameraFollowAPI', 'PhysxCameraFollowLookAPI', 'PhysxCameraFollowVelocityAPI', 'PhysxCharacterControllerAPI', 'PhysxCollisionAPI', 'PhysxContactReportAPI', 'PhysxConvexDecompositionCollisionAPI', 'PhysxConvexHullCollisionAPI', 'PhysxCookedDataAPI', 'PhysxDeformableAPI', 'PhysxDeformableBodyAPI', 'PhysxDeformableBodyMaterialAPI', 'PhysxDeformableSurfaceAPI', 'PhysxDeformableSurfaceMaterialAPI', 'PhysxDiffuseParticlesAPI', 'PhysxForceAPI', 'PhysxHairAPI', 'PhysxHairMaterialAPI', 'PhysxJointAPI', 'PhysxLimitAPI', 'PhysxMaterialAPI', 'PhysxMeshMergeCollisionAPI', 'PhysxMimicJointAPI', 'PhysxPBDMaterialAPI', 'PhysxParticleAPI', 'PhysxParticleAnisotropyAPI', 'PhysxParticleClothAPI', 'PhysxParticleIsosurfaceAPI', 'PhysxParticleSamplingAPI', 'PhysxParticleSetAPI', 'PhysxParticleSmoothingAPI', 'PhysxParticleSystem', 'PhysxPhysicsAttachment', 'PhysxPhysicsDistanceJointAPI', 'PhysxPhysicsGearJoint', 'PhysxPhysicsInstancer', 'PhysxPhysicsJointInstancer', 'PhysxPhysicsRackAndPinionJoint', 'PhysxResidualReportingAPI', 'PhysxRigidBodyAPI', 'PhysxSDFMeshCollisionAPI', 'PhysxSceneAPI', 'PhysxSceneQuasistaticAPI', 'PhysxSphereFillCollisionAPI', 'PhysxSurfaceVelocityAPI', 'PhysxTendonAttachmentAPI', 'PhysxTendonAttachmentLeafAPI', 'PhysxTendonAttachmentRootAPI', 'PhysxTendonAxisAPI', 'PhysxTendonAxisRootAPI', 'PhysxTriangleMeshCollisionAPI', 'PhysxTriangleMeshSimplificationCollisionAPI', 'PhysxTriggerAPI', 'PhysxTriggerStateAPI', 'PhysxVehicleAPI', 'PhysxVehicleAckermannSteeringAPI', 'PhysxVehicleAutoGearBoxAPI', 'PhysxVehicleBrakesAPI', 'PhysxVehicleClutchAPI', 'PhysxVehicleContextAPI', 'PhysxVehicleControllerAPI', 'PhysxVehicleDriveBasicAPI', 'PhysxVehicleDriveStandardAPI', 'PhysxVehicleEngineAPI', 'PhysxVehicleGearsAPI', 'PhysxVehicleMultiWheelDifferentialAPI', 'PhysxVehicleNonlinearCommandResponseAPI', 'PhysxVehicleSteeringAPI', 'PhysxVehicleSuspensionAPI', 'PhysxVehicleSuspensionComplianceAPI', 'PhysxVehicleTankControllerAPI', 'PhysxVehicleTankDifferentialAPI', 'PhysxVehicleTireAPI', 'PhysxVehicleTireFrictionTable', 'PhysxVehicleWheelAPI', 'PhysxVehicleWheelAttachmentAPI', 'PhysxVehicleWheelControllerAPI', 'TetrahedralMesh', 'Tokens']
class JointStateAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreatePositionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAll(*args, **kwargs):
        ...
    @staticmethod
    def GetPositionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysicsJointStateAPIPath(*args, **kwargs):
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
class PhysxArticulationAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateArticulationEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnabledSelfCollisionsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSleepThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSolverPositionIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSolverVelocityIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStabilizationThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetArticulationEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnabledSelfCollisionsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSleepThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSolverPositionIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSolverVelocityIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetStabilizationThresholdAttr(*args, **kwargs):
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
class PhysxAutoAttachmentAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionFilteringOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDeformableVertexOverlapOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableCollisionFilteringAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableDeformableFilteringPairsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableDeformableVertexAttachmentsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableRigidSurfaceAttachmentsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRigidSurfaceSamplingDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionFilteringOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDeformableVertexOverlapOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableCollisionFilteringAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableDeformableFilteringPairsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableDeformableVertexAttachmentsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableRigidSurfaceAttachmentsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRigidSurfaceSamplingDistanceAttr(*args, **kwargs):
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
class PhysxAutoParticleClothAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateDisableMeshWeldingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringBendStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringShearStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringStretchStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDisableMeshWeldingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringBendStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringShearStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringStretchStiffnessAttr(*args, **kwargs):
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
class PhysxCameraAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateAlwaysUpdateEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysxCameraSubjectRel(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAlwaysUpdateEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysxCameraSubjectRel(*args, **kwargs):
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
class PhysxCameraDroneAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateFeedForwardVelocityGainAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFollowDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFollowHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHorizontalVelocityGainAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePositionOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRotationFilterTimeConstantAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVelocityFilterTimeConstantAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVerticalVelocityGainAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetFeedForwardVelocityGainAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFollowDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFollowHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHorizontalVelocityGainAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPositionOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRotationFilterTimeConstantAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetVelocityFilterTimeConstantAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVerticalVelocityGainAttr(*args, **kwargs):
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
class PhysxCameraFollowAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateCameraPositionTimeConstantAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFollowMaxDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFollowMaxSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFollowMinDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFollowMinSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFollowTurnRateGainAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLookAheadMaxDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLookAheadMaxSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLookAheadMinDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLookAheadMinSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLookAheadTurnRateGainAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLookPositionHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLookPositionTimeConstantAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePitchAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePitchAngleTimeConstantAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePositionOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSlowPitchAngleSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSlowSpeedPitchAngleScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVelocityNormalMinSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateYawAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateYawRateTimeConstantAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCameraPositionTimeConstantAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFollowMaxDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFollowMaxSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFollowMinDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFollowMinSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFollowTurnRateGainAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLookAheadMaxDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLookAheadMaxSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLookAheadMinDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLookAheadMinSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLookAheadTurnRateGainAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLookPositionHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLookPositionTimeConstantAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPitchAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPitchAngleTimeConstantAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPositionOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSlowPitchAngleSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSlowSpeedPitchAngleScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVelocityNormalMinSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetYawAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetYawRateTimeConstantAttr(*args, **kwargs):
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
class PhysxCameraFollowLookAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateDownHillGroundAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDownHillGroundPitchAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFollowReverseDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFollowReverseSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUpHillGroundAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUpHillGroundPitchAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVelocityBlendTimeConstantAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDownHillGroundAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDownHillGroundPitchAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFollowReverseDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFollowReverseSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetUpHillGroundAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetUpHillGroundPitchAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVelocityBlendTimeConstantAttr(*args, **kwargs):
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
class PhysxCameraFollowVelocityAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
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
class PhysxCharacterControllerAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateClimbingModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateContactOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateInvisibleWallHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxJumpHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMoveTargetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateNonWalkableModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateScaleCoeffAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSimulationOwnerRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateSlopeLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStepOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUpAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVolumeGrowthAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetClimbingModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetContactOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetInvisibleWallHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxJumpHeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMoveTargetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNonWalkableModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetScaleCoeffAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSimulationOwnerRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSlopeLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetStepOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetUpAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVolumeGrowthAttr(*args, **kwargs):
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
class PhysxCollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateContactOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinTorsionalPatchRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRestOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTorsionalPatchRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetContactOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinTorsionalPatchRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRestOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTorsionalPatchRadiusAttr(*args, **kwargs):
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
class PhysxContactReportAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateReportPairsRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetReportPairsRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetThresholdAttr(*args, **kwargs):
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
class PhysxConvexDecompositionCollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateErrorPercentageAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHullVertexLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxConvexHullsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinThicknessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateShrinkWrapAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVoxelResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetErrorPercentageAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHullVertexLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxConvexHullsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinThicknessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetShrinkWrapAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVoxelResolutionAttr(*args, **kwargs):
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
class PhysxConvexHullCollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateHullVertexLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinThicknessAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetHullVertexLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinThicknessAttr(*args, **kwargs):
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
class PhysxCookedDataAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateBufferAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAll(*args, **kwargs):
        ...
    @staticmethod
    def GetBufferAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysxCookedDataAPIPath(*args, **kwargs):
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
class PhysxDeformableAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateDeformableEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableCCDAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxDepenetrationVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRestPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSelfCollisionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSelfCollisionFilterDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSettlingThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSimulationIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSimulationOwnerRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateSimulationVelocitiesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSleepDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSleepThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSolverPositionIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVertexVelocityDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDeformableEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableCCDAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxDepenetrationVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRestPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSelfCollisionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSelfCollisionFilterDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSettlingThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSimulationIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSimulationOwnerRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSimulationVelocitiesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSleepDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSleepThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSolverPositionIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVertexVelocityDampingAttr(*args, **kwargs):
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
class PhysxDeformableBodyAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionRestPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDisableGravityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSimulationPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSimulationRestPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionRestPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDisableGravityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSimulationPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSimulationRestPointsAttr(*args, **kwargs):
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
class PhysxDeformableBodyMaterialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateDampingScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDynamicFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateElasticityDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePoissonsRatioAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateYoungsModulusAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDampingScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDynamicFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetElasticityDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPoissonsRatioAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetYoungsModulusAttr(*args, **kwargs):
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
class PhysxDeformableSurfaceAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateBendingStiffnessScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionIterationMultiplierAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionPairUpdateFrequencyAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFlatteningEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetBendingStiffnessScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionIterationMultiplierAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionPairUpdateFrequencyAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFlatteningEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxVelocityAttr(*args, **kwargs):
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
class PhysxDeformableSurfaceMaterialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
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
    def CreatePoissonsRatioAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateThicknessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateYoungsModulusAttr(*args, **kwargs):
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
    def GetPoissonsRatioAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetThicknessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetYoungsModulusAttr(*args, **kwargs):
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
class PhysxDiffuseParticlesAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateAirDragAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateBubbleDragAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateBuoyancyAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionDecayAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDiffuseParticlesEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDivergenceWeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateKineticEnergyWeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLifetimeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxDiffuseParticleMultiplierAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePressureWeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUseAccurateVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAirDragAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetBubbleDragAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetBuoyancyAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionDecayAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDiffuseParticlesEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDivergenceWeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetKineticEnergyWeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLifetimeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxDiffuseParticleMultiplierAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPressureWeightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetUseAccurateVelocityAttr(*args, **kwargs):
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
class PhysxForceAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateForceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateForceEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWorldFrameEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetForceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetForceEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWorldFrameEnabledAttr(*args, **kwargs):
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
class PhysxHairAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateExternalCollisionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGlobalShapeComplianceAtRootAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGlobalShapeComplianceStrandAttenuationAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateInterHairRepulsionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLocalShapeMatchingComplianceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLocalShapeMatchingGroupOverlapAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLocalShapeMatchingGroupSizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLocalShapeMatchingLinearStretchingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSegmentLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTwosidedAttachmentAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVelSmoothingAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetExternalCollisionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGlobalShapeComplianceAtRootAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGlobalShapeComplianceStrandAttenuationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetInterHairRepulsionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLocalShapeMatchingComplianceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLocalShapeMatchingGroupOverlapAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLocalShapeMatchingGroupSizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLocalShapeMatchingLinearStretchingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSegmentLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTwosidedAttachmentAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVelSmoothingAttr(*args, **kwargs):
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
class PhysxHairMaterialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateContactOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateContactOffsetMultiplierAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCurveBendStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCurveThicknessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDynamicFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateYoungsModulusAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetContactOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetContactOffsetMultiplierAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCurveBendStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCurveThicknessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDynamicFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetYoungsModulusAttr(*args, **kwargs):
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
class PhysxJointAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateArmatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableProjectionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateJointFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxJointVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetArmatureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableProjectionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetJointFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxJointVelocityAttr(*args, **kwargs):
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
class PhysxLimitAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateBounceThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateContactDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRestitutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAll(*args, **kwargs):
        ...
    @staticmethod
    def GetBounceThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetContactDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRestitutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysxLimitAPIPath(*args, **kwargs):
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
class PhysxMaterialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateCompliantContactAccelerationSpringAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCompliantContactDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCompliantContactStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDampingCombineModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFrictionCombineModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateImprovePatchFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRestitutionCombineModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCompliantContactAccelerationSpringAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCompliantContactDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCompliantContactStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDampingCombineModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFrictionCombineModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetImprovePatchFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRestitutionCombineModeAttr(*args, **kwargs):
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
class PhysxMeshMergeCollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
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
    def GetCollisionMeshesCollectionAPI(*args, **kwargs):
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
class PhysxMimicJointAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateGearingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateReferenceJointAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateReferenceJointRel(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAll(*args, **kwargs):
        ...
    @staticmethod
    def GetGearingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetReferenceJointAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetReferenceJointRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysxMimicJointAPIPath(*args, **kwargs):
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
class PhysxPBDMaterialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateAdhesionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateAdhesionOffsetScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCflCoefficientAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCohesionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDragAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGravityScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLiftAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateParticleAdhesionScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateParticleFrictionScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSurfaceTensionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateViscosityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVorticityConfinementAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAdhesionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetAdhesionOffsetScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCflCoefficientAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCohesionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDensityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDragAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFrictionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGravityScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLiftAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetParticleAdhesionScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetParticleFrictionScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSurfaceTensionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetViscosityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVorticityConfinementAttr(*args, **kwargs):
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
class PhysxParticleAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateParticleEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateParticleGroupAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateParticleSystemRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateSelfCollisionAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetParticleEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetParticleGroupAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetParticleSystemRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSelfCollisionAttr(*args, **kwargs):
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
class PhysxParticleAnisotropyAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateParticleAnisotropyEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetParticleAnisotropyEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetScaleAttr(*args, **kwargs):
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
class PhysxParticleClothAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreatePressureAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRestPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSelfCollisionFilterAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringDampingsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringRestLengthsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringStiffnessesAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetPressureAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRestPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSelfCollisionFilterAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringDampingsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringRestLengthsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringStiffnessesAttr(*args, **kwargs):
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
class PhysxParticleIsosurfaceAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateGridFilteringPassesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGridSmoothingRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGridSpacingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateIsosurfaceEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxSubgridsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxTrianglesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxVerticesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateNumMeshNormalSmoothingPassesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateNumMeshSmoothingPassesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSurfaceDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetGridFilteringPassesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGridSmoothingRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGridSpacingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetIsosurfaceEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxSubgridsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxTrianglesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxVerticesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNumMeshNormalSmoothingPassesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNumMeshSmoothingPassesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSurfaceDistanceAttr(*args, **kwargs):
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
class PhysxParticleSamplingAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxSamplesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateParticlesRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateSamplingDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVolumeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxSamplesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetParticlesRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSamplingDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetVolumeAttr(*args, **kwargs):
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
class PhysxParticleSetAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateFluidAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSimulationPointsAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetFluidAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSimulationPointsAttr(*args, **kwargs):
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
class PhysxParticleSmoothingAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateParticleSmoothingEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStrengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetParticleSmoothingEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetStrengthAttr(*args, **kwargs):
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
class PhysxParticleSystem(pxr.UsdGeom.Gprim):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateContactOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableCCDAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFluidRestOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGlobalSelfCollisionEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxDepenetrationVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxNeighborhoodAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateNeighborhoodScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateNonParticleCollisionEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateParticleContactOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateParticleSystemEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRestOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSimulationOwnerRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateSolidRestOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSolverPositionIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWindAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetContactOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableCCDAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFluidRestOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGlobalSelfCollisionEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxDepenetrationVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxNeighborhoodAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNeighborhoodScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetNonParticleCollisionEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetParticleContactOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetParticleSystemEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRestOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSimulationOwnerRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSolidRestOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSolverPositionIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWindAttr(*args, **kwargs):
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
class PhysxPhysicsAttachment(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateActor0Rel(*args, **kwargs):
        ...
    @staticmethod
    def CreateActor1Rel(*args, **kwargs):
        ...
    @staticmethod
    def CreateAttachmentEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionFilterIndices0Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionFilterIndices1Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFilterType0Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFilterType1Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePoints0Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePoints1Attr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetActor0Rel(*args, **kwargs):
        ...
    @staticmethod
    def GetActor1Rel(*args, **kwargs):
        ...
    @staticmethod
    def GetActorRel(*args, **kwargs):
        ...
    @staticmethod
    def GetAttachmentEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionFilterIndices0Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionFilterIndices1Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionFilterIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFilterType0Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetFilterType1Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetFilterTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPoints0Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetPoints1Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetPointsAttr(*args, **kwargs):
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
class PhysxPhysicsDistanceJointAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringStiffnessAttr(*args, **kwargs):
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
class PhysxPhysicsGearJoint(pxr.UsdPhysics.Joint):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateGearRatioAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHinge0Rel(*args, **kwargs):
        ...
    @staticmethod
    def CreateHinge1Rel(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetGearRatioAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHinge0Rel(*args, **kwargs):
        ...
    @staticmethod
    def GetHinge1Rel(*args, **kwargs):
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
class PhysxPhysicsInstancer(pxr.UsdGeom.Imageable):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreatePhysicsProtoIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysicsPrototypesRel(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysicsProtoIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysicsPrototypesRel(*args, **kwargs):
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
class PhysxPhysicsJointInstancer(PhysxPhysicsInstancer):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreatePhysicsBody0IndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysicsBody0sRel(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysicsBody1IndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysicsBody1sRel(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysicsLocalPos0sAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysicsLocalPos1sAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysicsLocalRot0sAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysicsLocalRot1sAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysicsBody0IndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysicsBody0sRel(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysicsBody1IndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysicsBody1sRel(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysicsLocalPos0sAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysicsLocalPos1sAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysicsLocalRot0sAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysicsLocalRot1sAttr(*args, **kwargs):
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
class PhysxPhysicsRackAndPinionJoint(pxr.UsdPhysics.Joint):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateHingeRel(*args, **kwargs):
        ...
    @staticmethod
    def CreatePrismaticRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateRatioAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetHingeRel(*args, **kwargs):
        ...
    @staticmethod
    def GetPrismaticRel(*args, **kwargs):
        ...
    @staticmethod
    def GetRatioAttr(*args, **kwargs):
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
class PhysxResidualReportingAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysxResidualReportingMaxResidualPositionIterationAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysxResidualReportingMaxResidualVelocityIterationAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysxResidualReportingRmsResidualPositionIterationAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePhysxResidualReportingRmsResidualVelocityIterationAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysxResidualReportingMaxResidualPositionIterationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysxResidualReportingMaxResidualVelocityIterationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysxResidualReportingRmsResidualPositionIterationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPhysxResidualReportingRmsResidualVelocityIterationAttr(*args, **kwargs):
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
class PhysxRigidBodyAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateAngularDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCfmScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateContactSlopCoefficientAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDisableGravityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableCCDAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableGyroscopicForcesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableSpeculativeCCDAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLinearDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLockedPosAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLockedRotAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxAngularVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxContactImpulseAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxDepenetrationVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxLinearVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRetainAccelerationsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSleepThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSolveContactAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSolverPositionIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSolverVelocityIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStabilizationThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAngularDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCfmScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetContactSlopCoefficientAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDisableGravityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableCCDAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableGyroscopicForcesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableSpeculativeCCDAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLinearDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLockedPosAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLockedRotAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxAngularVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxContactImpulseAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxDepenetrationVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxLinearVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRetainAccelerationsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSleepThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSolveContactAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSolverPositionIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSolverVelocityIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetStabilizationThresholdAttr(*args, **kwargs):
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
class PhysxSDFMeshCollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateSdfBitsPerSubgridPixelAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSdfEnableRemeshingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSdfMarginAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSdfNarrowBandThicknessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSdfResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSdfSubgridResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSdfTriangleCountReductionFactorAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSdfBitsPerSubgridPixelAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSdfEnableRemeshingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSdfMarginAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSdfNarrowBandThicknessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSdfResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSdfSubgridResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSdfTriangleCountReductionFactorAttr(*args, **kwargs):
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
class PhysxSceneAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateBounceThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateBroadphaseTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionSystemAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableCCDAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableEnhancedDeterminismAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableExternalForcesEveryIterationAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableGPUDynamicsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableResidualReportingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableSceneQuerySupportAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableStabilizationAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFrictionCorrelationDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFrictionOffsetThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFrictionTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuCollisionStackSizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuFoundLostAggregatePairsCapacityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuFoundLostPairsCapacityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuHeapCapacityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuMaxDeformableSurfaceContactsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuMaxHairContactsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuMaxNumPartitionsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuMaxParticleContactsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuMaxRigidContactCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuMaxRigidPatchCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuMaxSoftBodyContactsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuTempBufferCapacityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGpuTotalAggregatePairsCapacityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateInvertCollisionGroupFilterAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxBiasCoefficientAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxPositionIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxVelocityIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinPositionIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinVelocityIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateReportKinematicKinematicPairsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateReportKinematicStaticPairsAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSolverTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTimeStepsPerSecondAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUpdateTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetBounceThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetBroadphaseTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionSystemAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableCCDAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableEnhancedDeterminismAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableExternalForcesEveryIterationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableGPUDynamicsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableResidualReportingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableSceneQuerySupportAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableStabilizationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFrictionCorrelationDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFrictionOffsetThresholdAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFrictionTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuCollisionStackSizeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuFoundLostAggregatePairsCapacityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuFoundLostPairsCapacityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuHeapCapacityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuMaxDeformableSurfaceContactsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuMaxHairContactsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuMaxNumPartitionsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuMaxParticleContactsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuMaxRigidContactCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuMaxRigidPatchCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuMaxSoftBodyContactsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuTempBufferCapacityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGpuTotalAggregatePairsCapacityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetInvertCollisionGroupFilterAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxBiasCoefficientAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxPositionIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxVelocityIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinPositionIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinVelocityIterationCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetReportKinematicKinematicPairsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetReportKinematicStaticPairsAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSolverTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTimeStepsPerSecondAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetUpdateTypeAttr(*args, **kwargs):
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
class PhysxSceneQuasistaticAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnableQuasistaticAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetEnableQuasistaticAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetQuasistaticActorsCollectionAPI(*args, **kwargs):
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
class PhysxSphereFillCollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateFillModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxSpheresAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSeedCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVoxelResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetFillModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxSpheresAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSeedCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVoxelResolutionAttr(*args, **kwargs):
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
class PhysxSurfaceVelocityAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateSurfaceAngularVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSurfaceVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSurfaceVelocityEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSurfaceVelocityLocalSpaceAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSurfaceAngularVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSurfaceVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSurfaceVelocityEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSurfaceVelocityLocalSpaceAttr(*args, **kwargs):
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
class PhysxTendonAttachmentAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateGearingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLocalPosAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateParentAttachmentAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateParentLinkRel(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAll(*args, **kwargs):
        ...
    @staticmethod
    def GetGearingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLocalPosAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetParentAttachmentAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetParentLinkRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysxTendonAttachmentAPIPath(*args, **kwargs):
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
class PhysxTendonAttachmentLeafAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateLowerLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRestLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUpperLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAll(*args, **kwargs):
        ...
    @staticmethod
    def GetLowerLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRestLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetUpperLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysxTendonAttachmentLeafAPIPath(*args, **kwargs):
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
class PhysxTendonAttachmentRootAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
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
    def CreateLimitStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTendonEnabledAttr(*args, **kwargs):
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
    def GetLimitStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTendonEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysxTendonAttachmentRootAPIPath(*args, **kwargs):
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
class PhysxTendonAxisAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateForceCoefficientAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGearingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateJointAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAll(*args, **kwargs):
        ...
    @staticmethod
    def GetForceCoefficientAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGearingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetJointAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysxTendonAxisAPIPath(*args, **kwargs):
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
class PhysxTendonAxisRootAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
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
    def CreateLimitStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLowerLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRestLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTendonEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUpperLimitAttr(*args, **kwargs):
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
    def GetLimitStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLowerLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRestLengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTendonEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetUpperLimitAttr(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysxTendonAxisRootAPIPath(*args, **kwargs):
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
class PhysxTriangleMeshCollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateWeldToleranceAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetWeldToleranceAttr(*args, **kwargs):
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
class PhysxTriangleMeshSimplificationCollisionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateSimplificationMetricAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWeldToleranceAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSimplificationMetricAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWeldToleranceAttr(*args, **kwargs):
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
class PhysxTriggerAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateEnterScriptTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLeaveScriptTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateOnEnterScriptAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateOnLeaveScriptAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetEnterScriptTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLeaveScriptTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOnEnterScriptAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetOnLeaveScriptAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def UnapplyAPISchema(*args, **kwargs):
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
class PhysxTriggerStateAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateTriggeredCollisionsRel(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTriggeredCollisionsRel(*args, **kwargs):
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
class PhysxVehicleAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateDriveRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateHighForwardSpeedSubStepCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLateralStickyTireDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLateralStickyTireThresholdSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLateralStickyTireThresholdTimeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLimitSuspensionExpansionVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLongitudinalStickyTireDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLongitudinalStickyTireThresholdSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLongitudinalStickyTireThresholdTimeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLowForwardSpeedSubStepCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinActiveLongitudinalSlipDenominatorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinLateralSlipDenominatorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinLongitudinalSlipDenominatorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMinPassiveLongitudinalSlipDenominatorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSubStepThresholdLongitudinalSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSuspensionLineQueryTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVehicleEnabledAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDriveRel(*args, **kwargs):
        ...
    @staticmethod
    def GetHighForwardSpeedSubStepCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLateralStickyTireDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLateralStickyTireThresholdSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLateralStickyTireThresholdTimeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLimitSuspensionExpansionVelocityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLongitudinalStickyTireDampingAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLongitudinalStickyTireThresholdSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLongitudinalStickyTireThresholdTimeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLowForwardSpeedSubStepCountAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinActiveLongitudinalSlipDenominatorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinLateralSlipDenominatorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinLongitudinalSlipDenominatorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMinPassiveLongitudinalSlipDenominatorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSubStepThresholdLongitudinalSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSuspensionLineQueryTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVehicleEnabledAttr(*args, **kwargs):
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
class PhysxVehicleAckermannSteeringAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxSteerAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateStrengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTrackWidthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheel0Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheel1Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheelBaseAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxSteerAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetStrengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTrackWidthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWheel0Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetWheel1Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetWheelBaseAttr(*args, **kwargs):
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
class PhysxVehicleAutoGearBoxAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateDownRatiosAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLatencyAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUpRatiosAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDownRatiosAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLatencyAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetUpRatiosAttr(*args, **kwargs):
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
class PhysxVehicleBrakesAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxBrakeTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTorqueMultipliersAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheelsAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAll(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxBrakeTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTorqueMultipliersAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWheelsAttr(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysxVehicleBrakesAPIPath(*args, **kwargs):
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
class PhysxVehicleClutchAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateStrengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetStrengthAttr(*args, **kwargs):
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
class PhysxVehicleContextAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateForwardAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLongitudinalAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUpAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateUpdateModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVerticalAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetForwardAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLongitudinalAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetUpAxisAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetUpdateModeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetVerticalAxisAttr(*args, **kwargs):
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
class PhysxVehicleControllerAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateAcceleratorAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateBrake0Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreateBrake1Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreateBrakeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateHandbrakeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSteerAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSteerLeftAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSteerRightAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTargetGearAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAcceleratorAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetBrake0Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetBrake1Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetBrakeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetHandbrakeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSteerAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSteerLeftAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSteerRightAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTargetGearAttr(*args, **kwargs):
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
class PhysxVehicleDriveBasicAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreatePeakTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetPeakTorqueAttr(*args, **kwargs):
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
class PhysxVehicleDriveStandardAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateAutoGearBoxRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateClutchRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateEngineRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateGearsRel(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAutoGearBoxRel(*args, **kwargs):
        ...
    @staticmethod
    def GetClutchRel(*args, **kwargs):
        ...
    @staticmethod
    def GetEngineRel(*args, **kwargs):
        ...
    @staticmethod
    def GetGearsRel(*args, **kwargs):
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
class PhysxVehicleEngineAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateDampingRateFullThrottleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDampingRateZeroThrottleClutchDisengagedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDampingRateZeroThrottleClutchEngagedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateIdleRotationSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxRotationSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMoiAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePeakTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTorqueCurveAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDampingRateFullThrottleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDampingRateZeroThrottleClutchDisengagedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDampingRateZeroThrottleClutchEngagedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetIdleRotationSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxRotationSpeedAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMoiAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPeakTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTorqueCurveAttr(*args, **kwargs):
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
class PhysxVehicleGearsAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateRatioScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRatiosAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSwitchTimeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetRatioScaleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRatiosAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSwitchTimeAttr(*args, **kwargs):
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
class PhysxVehicleMultiWheelDifferentialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateAverageWheelSpeedRatiosAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTorqueRatiosAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheelsAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAverageWheelSpeedRatiosAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetTorqueRatiosAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWheelsAttr(*args, **kwargs):
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
class PhysxVehicleNonlinearCommandResponseAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateCommandValuesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpeedResponsesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpeedResponsesPerCommandValueAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAll(*args, **kwargs):
        ...
    @staticmethod
    def GetCommandValuesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSpeedResponsesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSpeedResponsesPerCommandValueAttr(*args, **kwargs):
        ...
    @staticmethod
    def IsPhysxVehicleNonlinearCommandResponseAPIPath(*args, **kwargs):
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
class PhysxVehicleSteeringAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateAngleMultipliersAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxSteerAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheelsAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAngleMultipliersAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxSteerAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetWheelsAttr(*args, **kwargs):
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
class PhysxVehicleSuspensionAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateCamberAtMaxCompressionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCamberAtMaxDroopAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCamberAtRestAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxCompressionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxDroopAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringDamperRateAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSpringStrengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSprungMassAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTravelDistanceAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCamberAtMaxCompressionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCamberAtMaxDroopAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCamberAtRestAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxCompressionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxDroopAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringDamperRateAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSpringStrengthAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSprungMassAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTravelDistanceAttr(*args, **kwargs):
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
class PhysxVehicleSuspensionComplianceAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateSuspensionForceAppPointAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTireForceAppPointAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheelCamberAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheelToeAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSuspensionForceAppPointAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTireForceAppPointAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWheelCamberAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWheelToeAngleAttr(*args, **kwargs):
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
class PhysxVehicleTankControllerAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateThrust0Attr(*args, **kwargs):
        ...
    @staticmethod
    def CreateThrust1Attr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetThrust0Attr(*args, **kwargs):
        ...
    @staticmethod
    def GetThrust1Attr(*args, **kwargs):
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
class PhysxVehicleTankDifferentialAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateNumberOfWheelsPerTrackAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateThrustIndexPerTrackAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTrackToWheelIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheelIndicesInTrackOrderAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetNumberOfWheelsPerTrackAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetThrustIndexPerTrackAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTrackToWheelIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWheelIndicesInTrackOrderAttr(*args, **kwargs):
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
class PhysxVehicleTireAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateCamberStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCamberStiffnessPerUnitGravityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFrictionTableRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateFrictionVsSlipGraphAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLatStiffXAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLatStiffYAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLateralStiffnessGraphAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLongitudinalStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateLongitudinalStiffnessPerUnitGravityAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRestLoadAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCamberStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCamberStiffnessPerUnitGravityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFrictionTableRel(*args, **kwargs):
        ...
    @staticmethod
    def GetFrictionVsSlipGraphAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLatStiffXAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLatStiffYAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLateralStiffnessGraphAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLongitudinalStiffnessAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetLongitudinalStiffnessPerUnitGravityAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRestLoadAttr(*args, **kwargs):
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
class PhysxVehicleTireFrictionTable(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateDefaultFrictionValueAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFrictionValuesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateGroundMaterialsRel(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDefaultFrictionValueAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFrictionValuesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetGroundMaterialsRel(*args, **kwargs):
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
class PhysxVehicleWheelAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateDampingRateAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMassAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxBrakeTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxHandBrakeTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaxSteerAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMoiAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateToeAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWidthAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDampingRateAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMassAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxBrakeTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxHandBrakeTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaxSteerAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMoiAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRadiusAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetToeAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWidthAttr(*args, **kwargs):
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
class PhysxVehicleWheelAttachmentAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateCollisionGroupRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateDrivenAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateIndexAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSuspensionForceAppPointOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSuspensionFrameOrientationAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSuspensionFramePositionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSuspensionRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateSuspensionTravelDirectionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTireForceAppPointOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateTireRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheelCenterOfMassOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheelFrameOrientationAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheelFramePositionAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateWheelRel(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCollisionGroupRel(*args, **kwargs):
        ...
    @staticmethod
    def GetDrivenAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetIndexAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSuspensionForceAppPointOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSuspensionFrameOrientationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSuspensionFramePositionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSuspensionRel(*args, **kwargs):
        ...
    @staticmethod
    def GetSuspensionTravelDirectionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTireForceAppPointOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetTireRel(*args, **kwargs):
        ...
    @staticmethod
    def GetWheelCenterOfMassOffsetAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWheelFrameOrientationAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWheelFramePositionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetWheelRel(*args, **kwargs):
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
class PhysxVehicleWheelControllerAPI(pxr.Usd.APISchemaBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def CreateBrakeTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDriveTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSteerAngleAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetBrakeTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDriveTorqueAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSteerAngleAttr(*args, **kwargs):
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
class TetrahedralMesh(pxr.UsdGeom.PointBased):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateIndicesAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetIndicesAttr(*args, **kwargs):
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
class Tokens(Boost.Python.instance):
    acceleration: typing.ClassVar[str] = 'acceleration'
    actor0: typing.ClassVar[str] = 'actor0'
    actor1: typing.ClassVar[str] = 'actor1'
    alwaysUpdateEnabled: typing.ClassVar[str] = 'alwaysUpdateEnabled'
    asynchronous: typing.ClassVar[str] = 'Asynchronous'
    attachmentEnabled: typing.ClassVar[str] = 'attachmentEnabled'
    average: typing.ClassVar[str] = 'average'
    bitsPerPixel16: typing.ClassVar[str] = 'BitsPerPixel16'
    bitsPerPixel32: typing.ClassVar[str] = 'BitsPerPixel32'
    bitsPerPixel8: typing.ClassVar[str] = 'BitsPerPixel8'
    brakes0: typing.ClassVar[str] = 'brakes0'
    brakes1: typing.ClassVar[str] = 'brakes1'
    clothConstaint: typing.ClassVar[str] = 'clothConstaint'
    collisionFilterIndices0: typing.ClassVar[str] = 'collisionFilterIndices0'
    collisionFilterIndices1: typing.ClassVar[str] = 'collisionFilterIndices1'
    collisionmeshes: typing.ClassVar[str] = 'collisionmeshes'
    constrained: typing.ClassVar[str] = 'constrained'
    contactOffset: typing.ClassVar[str] = 'contactOffset'
    convexDecomposition: typing.ClassVar[str] = 'convexDecomposition'
    convexHull: typing.ClassVar[str] = 'convexHull'
    defaultFrictionValue: typing.ClassVar[str] = 'defaultFrictionValue'
    disabled: typing.ClassVar[str] = 'Disabled'
    drive: typing.ClassVar[str] = 'drive'
    easy: typing.ClassVar[str] = 'easy'
    enableCCD: typing.ClassVar[str] = 'enableCCD'
    filterType0: typing.ClassVar[str] = 'filterType0'
    filterType1: typing.ClassVar[str] = 'filterType1'
    flood: typing.ClassVar[str] = 'flood'
    fluidRestOffset: typing.ClassVar[str] = 'fluidRestOffset'
    force: typing.ClassVar[str] = 'force'
    frictionValues: typing.ClassVar[str] = 'frictionValues'
    gPU: typing.ClassVar[str] = 'GPU'
    geometry: typing.ClassVar[str] = 'Geometry'
    globalSelfCollisionEnabled: typing.ClassVar[str] = 'globalSelfCollisionEnabled'
    groundMaterials: typing.ClassVar[str] = 'groundMaterials'
    indices: typing.ClassVar[str] = 'indices'
    mBP: typing.ClassVar[str] = 'MBP'
    max: typing.ClassVar[str] = 'max'
    maxDepenetrationVelocity: typing.ClassVar[str] = 'maxDepenetrationVelocity'
    maxNeighborhood: typing.ClassVar[str] = 'maxNeighborhood'
    maxVelocity: typing.ClassVar[str] = 'maxVelocity'
    min: typing.ClassVar[str] = 'min'
    multiply: typing.ClassVar[str] = 'multiply'
    negX: typing.ClassVar[str] = 'negX'
    negY: typing.ClassVar[str] = 'negY'
    negZ: typing.ClassVar[str] = 'negZ'
    neighborhoodScale: typing.ClassVar[str] = 'neighborhoodScale'
    nonParticleCollisionEnabled: typing.ClassVar[str] = 'nonParticleCollisionEnabled'
    oneDirectional: typing.ClassVar[str] = 'oneDirectional'
    pCM: typing.ClassVar[str] = 'PCM'
    pGS: typing.ClassVar[str] = 'PGS'
    particleContactOffset: typing.ClassVar[str] = 'particleContactOffset'
    particleSystemEnabled: typing.ClassVar[str] = 'particleSystemEnabled'
    patch: typing.ClassVar[str] = 'patch'
    physicsBody0Indices: typing.ClassVar[str] = 'physics:body0Indices'
    physicsBody0s: typing.ClassVar[str] = 'physics:body0s'
    physicsBody1Indices: typing.ClassVar[str] = 'physics:body1Indices'
    physicsBody1s: typing.ClassVar[str] = 'physics:body1s'
    physicsGearRatio: typing.ClassVar[str] = 'physics:gearRatio'
    physicsHinge: typing.ClassVar[str] = 'physics:hinge'
    physicsHinge0: typing.ClassVar[str] = 'physics:hinge0'
    physicsHinge1: typing.ClassVar[str] = 'physics:hinge1'
    physicsLocalPos0s: typing.ClassVar[str] = 'physics:localPos0s'
    physicsLocalPos1s: typing.ClassVar[str] = 'physics:localPos1s'
    physicsLocalRot0s: typing.ClassVar[str] = 'physics:localRot0s'
    physicsLocalRot1s: typing.ClassVar[str] = 'physics:localRot1s'
    physicsPrismatic: typing.ClassVar[str] = 'physics:prismatic'
    physicsProtoIndices: typing.ClassVar[str] = 'physics:protoIndices'
    physicsPrototypes: typing.ClassVar[str] = 'physics:prototypes'
    physicsRatio: typing.ClassVar[str] = 'physics:ratio'
    physxArticulationArticulationEnabled: typing.ClassVar[str] = 'physxArticulation:articulationEnabled'
    physxArticulationEnabledSelfCollisions: typing.ClassVar[str] = 'physxArticulation:enabledSelfCollisions'
    physxArticulationSleepThreshold: typing.ClassVar[str] = 'physxArticulation:sleepThreshold'
    physxArticulationSolverPositionIterationCount: typing.ClassVar[str] = 'physxArticulation:solverPositionIterationCount'
    physxArticulationSolverVelocityIterationCount: typing.ClassVar[str] = 'physxArticulation:solverVelocityIterationCount'
    physxArticulationStabilizationThreshold: typing.ClassVar[str] = 'physxArticulation:stabilizationThreshold'
    physxAutoAttachmentCollisionFilteringOffset: typing.ClassVar[str] = 'physxAutoAttachment:collisionFilteringOffset'
    physxAutoAttachmentDeformableVertexOverlapOffset: typing.ClassVar[str] = 'physxAutoAttachment:deformableVertexOverlapOffset'
    physxAutoAttachmentEnableCollisionFiltering: typing.ClassVar[str] = 'physxAutoAttachment:enableCollisionFiltering'
    physxAutoAttachmentEnableDeformableFilteringPairs: typing.ClassVar[str] = 'physxAutoAttachment:enableDeformableFilteringPairs'
    physxAutoAttachmentEnableDeformableVertexAttachments: typing.ClassVar[str] = 'physxAutoAttachment:enableDeformableVertexAttachments'
    physxAutoAttachmentEnableRigidSurfaceAttachments: typing.ClassVar[str] = 'physxAutoAttachment:enableRigidSurfaceAttachments'
    physxAutoAttachmentRigidSurfaceSamplingDistance: typing.ClassVar[str] = 'physxAutoAttachment:rigidSurfaceSamplingDistance'
    physxAutoParticleClothDisableMeshWelding: typing.ClassVar[str] = 'physxAutoParticleCloth:disableMeshWelding'
    physxAutoParticleClothSpringBendStiffness: typing.ClassVar[str] = 'physxAutoParticleCloth:springBendStiffness'
    physxAutoParticleClothSpringDamping: typing.ClassVar[str] = 'physxAutoParticleCloth:springDamping'
    physxAutoParticleClothSpringShearStiffness: typing.ClassVar[str] = 'physxAutoParticleCloth:springShearStiffness'
    physxAutoParticleClothSpringStretchStiffness: typing.ClassVar[str] = 'physxAutoParticleCloth:springStretchStiffness'
    physxCameraSubject: typing.ClassVar[str] = 'physxCamera:subject'
    physxCharacterControllerClimbingMode: typing.ClassVar[str] = 'physxCharacterController:climbingMode'
    physxCharacterControllerContactOffset: typing.ClassVar[str] = 'physxCharacterController:contactOffset'
    physxCharacterControllerInvisibleWallHeight: typing.ClassVar[str] = 'physxCharacterController:invisibleWallHeight'
    physxCharacterControllerMaxJumpHeight: typing.ClassVar[str] = 'physxCharacterController:maxJumpHeight'
    physxCharacterControllerMoveTarget: typing.ClassVar[str] = 'physxCharacterController:moveTarget'
    physxCharacterControllerNonWalkableMode: typing.ClassVar[str] = 'physxCharacterController:nonWalkableMode'
    physxCharacterControllerScaleCoeff: typing.ClassVar[str] = 'physxCharacterController:scaleCoeff'
    physxCharacterControllerSimulationOwner: typing.ClassVar[str] = 'physxCharacterController:simulationOwner'
    physxCharacterControllerSlopeLimit: typing.ClassVar[str] = 'physxCharacterController:slopeLimit'
    physxCharacterControllerStepOffset: typing.ClassVar[str] = 'physxCharacterController:stepOffset'
    physxCharacterControllerUpAxis: typing.ClassVar[str] = 'physxCharacterController:upAxis'
    physxCharacterControllerVolumeGrowth: typing.ClassVar[str] = 'physxCharacterController:volumeGrowth'
    physxCollisionContactOffset: typing.ClassVar[str] = 'physxCollision:contactOffset'
    physxCollisionCustomGeometry: typing.ClassVar[str] = 'physxCollisionCustomGeometry'
    physxCollisionMinTorsionalPatchRadius: typing.ClassVar[str] = 'physxCollision:minTorsionalPatchRadius'
    physxCollisionRestOffset: typing.ClassVar[str] = 'physxCollision:restOffset'
    physxCollisionTorsionalPatchRadius: typing.ClassVar[str] = 'physxCollision:torsionalPatchRadius'
    physxContactReportReportPairs: typing.ClassVar[str] = 'physxContactReport:reportPairs'
    physxContactReportThreshold: typing.ClassVar[str] = 'physxContactReport:threshold'
    physxConvexDecompositionCollisionErrorPercentage: typing.ClassVar[str] = 'physxConvexDecompositionCollision:errorPercentage'
    physxConvexDecompositionCollisionHullVertexLimit: typing.ClassVar[str] = 'physxConvexDecompositionCollision:hullVertexLimit'
    physxConvexDecompositionCollisionMaxConvexHulls: typing.ClassVar[str] = 'physxConvexDecompositionCollision:maxConvexHulls'
    physxConvexDecompositionCollisionMinThickness: typing.ClassVar[str] = 'physxConvexDecompositionCollision:minThickness'
    physxConvexDecompositionCollisionShrinkWrap: typing.ClassVar[str] = 'physxConvexDecompositionCollision:shrinkWrap'
    physxConvexDecompositionCollisionVoxelResolution: typing.ClassVar[str] = 'physxConvexDecompositionCollision:voxelResolution'
    physxConvexHullCollisionHullVertexLimit: typing.ClassVar[str] = 'physxConvexHullCollision:hullVertexLimit'
    physxConvexHullCollisionMinThickness: typing.ClassVar[str] = 'physxConvexHullCollision:minThickness'
    physxCookedData: typing.ClassVar[str] = 'physxCookedData'
    physxCookedData_MultipleApplyTemplate_Buffer: typing.ClassVar[str] = 'physxCookedData:__INSTANCE_NAME__:buffer'
    physxDeformableBodyMaterialDampingScale: typing.ClassVar[str] = 'physxDeformableBodyMaterial:dampingScale'
    physxDeformableBodyMaterialDensity: typing.ClassVar[str] = 'physxDeformableBodyMaterial:density'
    physxDeformableBodyMaterialDynamicFriction: typing.ClassVar[str] = 'physxDeformableBodyMaterial:dynamicFriction'
    physxDeformableBodyMaterialElasticityDamping: typing.ClassVar[str] = 'physxDeformableBodyMaterial:elasticityDamping'
    physxDeformableBodyMaterialPoissonsRatio: typing.ClassVar[str] = 'physxDeformableBodyMaterial:poissonsRatio'
    physxDeformableBodyMaterialYoungsModulus: typing.ClassVar[str] = 'physxDeformableBodyMaterial:youngsModulus'
    physxDeformableCollisionIndices: typing.ClassVar[str] = 'physxDeformable:collisionIndices'
    physxDeformableCollisionPoints: typing.ClassVar[str] = 'physxDeformable:collisionPoints'
    physxDeformableCollisionRestPoints: typing.ClassVar[str] = 'physxDeformable:collisionRestPoints'
    physxDeformableDeformableEnabled: typing.ClassVar[str] = 'physxDeformable:deformableEnabled'
    physxDeformableDisableGravity: typing.ClassVar[str] = 'physxDeformable:disableGravity'
    physxDeformableEnableCCD: typing.ClassVar[str] = 'physxDeformable:enableCCD'
    physxDeformableMaxDepenetrationVelocity: typing.ClassVar[str] = 'physxDeformable:maxDepenetrationVelocity'
    physxDeformableRestPoints: typing.ClassVar[str] = 'physxDeformable:restPoints'
    physxDeformableSelfCollision: typing.ClassVar[str] = 'physxDeformable:selfCollision'
    physxDeformableSelfCollisionFilterDistance: typing.ClassVar[str] = 'physxDeformable:selfCollisionFilterDistance'
    physxDeformableSettlingThreshold: typing.ClassVar[str] = 'physxDeformable:settlingThreshold'
    physxDeformableSimulationIndices: typing.ClassVar[str] = 'physxDeformable:simulationIndices'
    physxDeformableSimulationOwner: typing.ClassVar[str] = 'physxDeformable:simulationOwner'
    physxDeformableSimulationPoints: typing.ClassVar[str] = 'physxDeformable:simulationPoints'
    physxDeformableSimulationRestPoints: typing.ClassVar[str] = 'physxDeformable:simulationRestPoints'
    physxDeformableSimulationVelocities: typing.ClassVar[str] = 'physxDeformable:simulationVelocities'
    physxDeformableSleepDamping: typing.ClassVar[str] = 'physxDeformable:sleepDamping'
    physxDeformableSleepThreshold: typing.ClassVar[str] = 'physxDeformable:sleepThreshold'
    physxDeformableSolverPositionIterationCount: typing.ClassVar[str] = 'physxDeformable:solverPositionIterationCount'
    physxDeformableSurfaceBendingStiffnessScale: typing.ClassVar[str] = 'physxDeformableSurface:bendingStiffnessScale'
    physxDeformableSurfaceCollisionIterationMultiplier: typing.ClassVar[str] = 'physxDeformableSurface:collisionIterationMultiplier'
    physxDeformableSurfaceCollisionPairUpdateFrequency: typing.ClassVar[str] = 'physxDeformableSurface:collisionPairUpdateFrequency'
    physxDeformableSurfaceFlatteningEnabled: typing.ClassVar[str] = 'physxDeformableSurface:flatteningEnabled'
    physxDeformableSurfaceMaterialDensity: typing.ClassVar[str] = 'physxDeformableSurfaceMaterial:density'
    physxDeformableSurfaceMaterialDynamicFriction: typing.ClassVar[str] = 'physxDeformableSurfaceMaterial:dynamicFriction'
    physxDeformableSurfaceMaterialPoissonsRatio: typing.ClassVar[str] = 'physxDeformableSurfaceMaterial:poissonsRatio'
    physxDeformableSurfaceMaterialThickness: typing.ClassVar[str] = 'physxDeformableSurfaceMaterial:thickness'
    physxDeformableSurfaceMaterialYoungsModulus: typing.ClassVar[str] = 'physxDeformableSurfaceMaterial:youngsModulus'
    physxDeformableSurfaceMaxVelocity: typing.ClassVar[str] = 'physxDeformableSurface:maxVelocity'
    physxDeformableVertexVelocityDamping: typing.ClassVar[str] = 'physxDeformable:vertexVelocityDamping'
    physxDiffuseParticlesAirDrag: typing.ClassVar[str] = 'physxDiffuseParticles:airDrag'
    physxDiffuseParticlesBubbleDrag: typing.ClassVar[str] = 'physxDiffuseParticles:bubbleDrag'
    physxDiffuseParticlesBuoyancy: typing.ClassVar[str] = 'physxDiffuseParticles:buoyancy'
    physxDiffuseParticlesCollisionDecay: typing.ClassVar[str] = 'physxDiffuseParticles:collisionDecay'
    physxDiffuseParticlesDiffuseParticlesEnabled: typing.ClassVar[str] = 'physxDiffuseParticles:diffuseParticlesEnabled'
    physxDiffuseParticlesDivergenceWeight: typing.ClassVar[str] = 'physxDiffuseParticles:divergenceWeight'
    physxDiffuseParticlesKineticEnergyWeight: typing.ClassVar[str] = 'physxDiffuseParticles:kineticEnergyWeight'
    physxDiffuseParticlesLifetime: typing.ClassVar[str] = 'physxDiffuseParticles:lifetime'
    physxDiffuseParticlesMaxDiffuseParticleMultiplier: typing.ClassVar[str] = 'physxDiffuseParticles:maxDiffuseParticleMultiplier'
    physxDiffuseParticlesPressureWeight: typing.ClassVar[str] = 'physxDiffuseParticles:pressureWeight'
    physxDiffuseParticlesThreshold: typing.ClassVar[str] = 'physxDiffuseParticles:threshold'
    physxDiffuseParticlesUseAccurateVelocity: typing.ClassVar[str] = 'physxDiffuseParticles:useAccurateVelocity'
    physxDroneCameraFeedForwardVelocityGain: typing.ClassVar[str] = 'physxDroneCamera:feedForwardVelocityGain'
    physxDroneCameraFollowDistance: typing.ClassVar[str] = 'physxDroneCamera:followDistance'
    physxDroneCameraFollowHeight: typing.ClassVar[str] = 'physxDroneCamera:followHeight'
    physxDroneCameraHorizontalVelocityGain: typing.ClassVar[str] = 'physxDroneCamera:horizontalVelocityGain'
    physxDroneCameraMaxDistance: typing.ClassVar[str] = 'physxDroneCamera:maxDistance'
    physxDroneCameraMaxSpeed: typing.ClassVar[str] = 'physxDroneCamera:maxSpeed'
    physxDroneCameraPositionOffset: typing.ClassVar[str] = 'physxDroneCamera:positionOffset'
    physxDroneCameraRotationFilterTimeConstant: typing.ClassVar[str] = 'physxDroneCamera:rotationFilterTimeConstant'
    physxDroneCameraVelocityFilterTimeConstant: typing.ClassVar[str] = 'physxDroneCamera:velocityFilterTimeConstant'
    physxDroneCameraVerticalVelocityGain: typing.ClassVar[str] = 'physxDroneCamera:verticalVelocityGain'
    physxFollowCameraCameraPositionTimeConstant: typing.ClassVar[str] = 'physxFollowCamera:cameraPositionTimeConstant'
    physxFollowCameraFollowMaxDistance: typing.ClassVar[str] = 'physxFollowCamera:followMaxDistance'
    physxFollowCameraFollowMaxSpeed: typing.ClassVar[str] = 'physxFollowCamera:followMaxSpeed'
    physxFollowCameraFollowMinDistance: typing.ClassVar[str] = 'physxFollowCamera:followMinDistance'
    physxFollowCameraFollowMinSpeed: typing.ClassVar[str] = 'physxFollowCamera:followMinSpeed'
    physxFollowCameraFollowTurnRateGain: typing.ClassVar[str] = 'physxFollowCamera:followTurnRateGain'
    physxFollowCameraLookAheadMaxSpeed: typing.ClassVar[str] = 'physxFollowCamera:lookAheadMaxSpeed'
    physxFollowCameraLookAheadMinDistance: typing.ClassVar[str] = 'physxFollowCamera:lookAheadMinDistance'
    physxFollowCameraLookAheadMinSpeed: typing.ClassVar[str] = 'physxFollowCamera:lookAheadMinSpeed'
    physxFollowCameraLookAheadTurnRateGain: typing.ClassVar[str] = 'physxFollowCamera:lookAheadTurnRateGain'
    physxFollowCameraLookPositionHeight: typing.ClassVar[str] = 'physxFollowCamera:lookPositionHeight'
    physxFollowCameraLookPositionTimeConstant: typing.ClassVar[str] = 'physxFollowCamera:lookPositionTimeConstant'
    physxFollowCameraPitchAngle: typing.ClassVar[str] = 'physxFollowCamera:pitchAngle'
    physxFollowCameraPitchAngleTimeConstant: typing.ClassVar[str] = 'physxFollowCamera:pitchAngleTimeConstant'
    physxFollowCameraPositionOffset: typing.ClassVar[str] = 'physxFollowCamera:positionOffset'
    physxFollowCameraSlowPitchAngleSpeed: typing.ClassVar[str] = 'physxFollowCamera:slowPitchAngleSpeed'
    physxFollowCameraSlowSpeedPitchAngleScale: typing.ClassVar[str] = 'physxFollowCamera:slowSpeedPitchAngleScale'
    physxFollowCameraVelocityNormalMinSpeed: typing.ClassVar[str] = 'physxFollowCamera:velocityNormalMinSpeed'
    physxFollowCameraYawAngle: typing.ClassVar[str] = 'physxFollowCamera:yawAngle'
    physxFollowCameraYawRateTimeConstant: typing.ClassVar[str] = 'physxFollowCamera:yawRateTimeConstant'
    physxFollowFollowCameraLookAheadMaxDistance: typing.ClassVar[str] = 'physxFollowFollowCamera:lookAheadMaxDistance'
    physxFollowLookCameraDownHillGroundAngle: typing.ClassVar[str] = 'physxFollowLookCamera:downHillGroundAngle'
    physxFollowLookCameraDownHillGroundPitch: typing.ClassVar[str] = 'physxFollowLookCamera:downHillGroundPitch'
    physxFollowLookCameraFollowReverseDistance: typing.ClassVar[str] = 'physxFollowLookCamera:followReverseDistance'
    physxFollowLookCameraFollowReverseSpeed: typing.ClassVar[str] = 'physxFollowLookCamera:followReverseSpeed'
    physxFollowLookCameraUpHillGroundAngle: typing.ClassVar[str] = 'physxFollowLookCamera:upHillGroundAngle'
    physxFollowLookCameraUpHillGroundPitch: typing.ClassVar[str] = 'physxFollowLookCamera:upHillGroundPitch'
    physxFollowLookCameraVelocityBlendTimeConstant: typing.ClassVar[str] = 'physxFollowLookCamera:velocityBlendTimeConstant'
    physxForceForce: typing.ClassVar[str] = 'physxForce:force'
    physxForceForceEnabled: typing.ClassVar[str] = 'physxForce:forceEnabled'
    physxForceMode: typing.ClassVar[str] = 'physxForce:mode'
    physxForceTorque: typing.ClassVar[str] = 'physxForce:torque'
    physxForceWorldFrameEnabled: typing.ClassVar[str] = 'physxForce:worldFrameEnabled'
    physxHairExternalCollision: typing.ClassVar[str] = 'physxHair:externalCollision'
    physxHairGlobalShapeComplianceAtRoot: typing.ClassVar[str] = 'physxHair:globalShapeComplianceAtRoot'
    physxHairGlobalShapeComplianceStrandAttenuation: typing.ClassVar[str] = 'physxHair:globalShapeComplianceStrandAttenuation'
    physxHairInterHairRepulsion: typing.ClassVar[str] = 'physxHair:interHairRepulsion'
    physxHairLocalShapeMatchingCompliance: typing.ClassVar[str] = 'physxHair:localShapeMatchingCompliance'
    physxHairLocalShapeMatchingGroupOverlap: typing.ClassVar[str] = 'physxHair:localShapeMatchingGroupOverlap'
    physxHairLocalShapeMatchingGroupSize: typing.ClassVar[str] = 'physxHair:localShapeMatchingGroupSize'
    physxHairLocalShapeMatchingLinearStretching: typing.ClassVar[str] = 'physxHair:localShapeMatchingLinearStretching'
    physxHairMaterialContactOffset: typing.ClassVar[str] = 'physxHairMaterial:contactOffset'
    physxHairMaterialContactOffsetMultiplier: typing.ClassVar[str] = 'physxHairMaterial:contactOffsetMultiplier'
    physxHairMaterialCurveBendStiffness: typing.ClassVar[str] = 'physxHairMaterial:curveBendStiffness'
    physxHairMaterialCurveThickness: typing.ClassVar[str] = 'physxHairMaterial:curveThickness'
    physxHairMaterialDensity: typing.ClassVar[str] = 'physxHairMaterial:density'
    physxHairMaterialDynamicFriction: typing.ClassVar[str] = 'physxHairMaterial:dynamicFriction'
    physxHairMaterialYoungsModulus: typing.ClassVar[str] = 'physxHairMaterial:youngsModulus'
    physxHairSegmentLength: typing.ClassVar[str] = 'physxHair:segmentLength'
    physxHairTwosidedAttachment: typing.ClassVar[str] = 'physxHair:twosidedAttachment'
    physxHairVelSmoothing: typing.ClassVar[str] = 'physxHair:velSmoothing'
    physxJointArmature: typing.ClassVar[str] = 'physxJoint:armature'
    physxJointEnableProjection: typing.ClassVar[str] = 'physxJoint:enableProjection'
    physxJointJointFriction: typing.ClassVar[str] = 'physxJoint:jointFriction'
    physxJointMaxJointVelocity: typing.ClassVar[str] = 'physxJoint:maxJointVelocity'
    physxLimit: typing.ClassVar[str] = 'physxLimit'
    physxLimit_MultipleApplyTemplate_BounceThreshold: typing.ClassVar[str] = 'physxLimit:__INSTANCE_NAME__:bounceThreshold'
    physxLimit_MultipleApplyTemplate_ContactDistance: typing.ClassVar[str] = 'physxLimit:__INSTANCE_NAME__:contactDistance'
    physxLimit_MultipleApplyTemplate_Damping: typing.ClassVar[str] = 'physxLimit:__INSTANCE_NAME__:damping'
    physxLimit_MultipleApplyTemplate_Restitution: typing.ClassVar[str] = 'physxLimit:__INSTANCE_NAME__:restitution'
    physxLimit_MultipleApplyTemplate_Stiffness: typing.ClassVar[str] = 'physxLimit:__INSTANCE_NAME__:stiffness'
    physxMaterialCompliantContactAccelerationSpring: typing.ClassVar[str] = 'physxMaterial:compliantContactAccelerationSpring'
    physxMaterialCompliantContactDamping: typing.ClassVar[str] = 'physxMaterial:compliantContactDamping'
    physxMaterialCompliantContactStiffness: typing.ClassVar[str] = 'physxMaterial:compliantContactStiffness'
    physxMaterialDampingCombineMode: typing.ClassVar[str] = 'physxMaterial:dampingCombineMode'
    physxMaterialFrictionCombineMode: typing.ClassVar[str] = 'physxMaterial:frictionCombineMode'
    physxMaterialImprovePatchFriction: typing.ClassVar[str] = 'physxMaterial:improvePatchFriction'
    physxMaterialRestitutionCombineMode: typing.ClassVar[str] = 'physxMaterial:restitutionCombineMode'
    physxMimicJoint: typing.ClassVar[str] = 'physxMimicJoint'
    physxMimicJoint_MultipleApplyTemplate_Gearing: typing.ClassVar[str] = 'physxMimicJoint:__INSTANCE_NAME__:gearing'
    physxMimicJoint_MultipleApplyTemplate_Offset: typing.ClassVar[str] = 'physxMimicJoint:__INSTANCE_NAME__:offset'
    physxMimicJoint_MultipleApplyTemplate_ReferenceJoint: typing.ClassVar[str] = 'physxMimicJoint:__INSTANCE_NAME__:referenceJoint'
    physxMimicJoint_MultipleApplyTemplate_ReferenceJointAxis: typing.ClassVar[str] = 'physxMimicJoint:__INSTANCE_NAME__:referenceJointAxis'
    physxPBDMaterialAdhesion: typing.ClassVar[str] = 'physxPBDMaterial:adhesion'
    physxPBDMaterialAdhesionOffsetScale: typing.ClassVar[str] = 'physxPBDMaterial:adhesionOffsetScale'
    physxPBDMaterialCflCoefficient: typing.ClassVar[str] = 'physxPBDMaterial:cflCoefficient'
    physxPBDMaterialCohesion: typing.ClassVar[str] = 'physxPBDMaterial:cohesion'
    physxPBDMaterialDamping: typing.ClassVar[str] = 'physxPBDMaterial:damping'
    physxPBDMaterialDensity: typing.ClassVar[str] = 'physxPBDMaterial:density'
    physxPBDMaterialDrag: typing.ClassVar[str] = 'physxPBDMaterial:drag'
    physxPBDMaterialFriction: typing.ClassVar[str] = 'physxPBDMaterial:friction'
    physxPBDMaterialGravityScale: typing.ClassVar[str] = 'physxPBDMaterial:gravityScale'
    physxPBDMaterialLift: typing.ClassVar[str] = 'physxPBDMaterial:lift'
    physxPBDMaterialParticleAdhesionScale: typing.ClassVar[str] = 'physxPBDMaterial:particleAdhesionScale'
    physxPBDMaterialParticleFrictionScale: typing.ClassVar[str] = 'physxPBDMaterial:particleFrictionScale'
    physxPBDMaterialSurfaceTension: typing.ClassVar[str] = 'physxPBDMaterial:surfaceTension'
    physxPBDMaterialViscosity: typing.ClassVar[str] = 'physxPBDMaterial:viscosity'
    physxPBDMaterialVorticityConfinement: typing.ClassVar[str] = 'physxPBDMaterial:vorticityConfinement'
    physxParticleAnisotropyMax: typing.ClassVar[str] = 'physxParticleAnisotropy:max'
    physxParticleAnisotropyMin: typing.ClassVar[str] = 'physxParticleAnisotropy:min'
    physxParticleAnisotropyParticleAnisotropyEnabled: typing.ClassVar[str] = 'physxParticleAnisotropy:particleAnisotropyEnabled'
    physxParticleAnisotropyScale: typing.ClassVar[str] = 'physxParticleAnisotropy:scale'
    physxParticleFluid: typing.ClassVar[str] = 'physxParticle:fluid'
    physxParticleIsosurfaceGridFilteringPasses: typing.ClassVar[str] = 'physxParticleIsosurface:gridFilteringPasses'
    physxParticleIsosurfaceGridSmoothingRadius: typing.ClassVar[str] = 'physxParticleIsosurface:gridSmoothingRadius'
    physxParticleIsosurfaceGridSpacing: typing.ClassVar[str] = 'physxParticleIsosurface:gridSpacing'
    physxParticleIsosurfaceIsosurfaceEnabled: typing.ClassVar[str] = 'physxParticleIsosurface:isosurfaceEnabled'
    physxParticleIsosurfaceMaxSubgrids: typing.ClassVar[str] = 'physxParticleIsosurface:maxSubgrids'
    physxParticleIsosurfaceMaxTriangles: typing.ClassVar[str] = 'physxParticleIsosurface:maxTriangles'
    physxParticleIsosurfaceMaxVertices: typing.ClassVar[str] = 'physxParticleIsosurface:maxVertices'
    physxParticleIsosurfaceNumMeshNormalSmoothingPasses: typing.ClassVar[str] = 'physxParticleIsosurface:numMeshNormalSmoothingPasses'
    physxParticleIsosurfaceNumMeshSmoothingPasses: typing.ClassVar[str] = 'physxParticleIsosurface:numMeshSmoothingPasses'
    physxParticleIsosurfaceSurfaceDistance: typing.ClassVar[str] = 'physxParticleIsosurface:surfaceDistance'
    physxParticleParticleEnabled: typing.ClassVar[str] = 'physxParticle:particleEnabled'
    physxParticleParticleGroup: typing.ClassVar[str] = 'physxParticle:particleGroup'
    physxParticleParticleSystem: typing.ClassVar[str] = 'physxParticle:particleSystem'
    physxParticlePressure: typing.ClassVar[str] = 'physxParticle:pressure'
    physxParticleRestPoints: typing.ClassVar[str] = 'physxParticle:restPoints'
    physxParticleSamplingMaxSamples: typing.ClassVar[str] = 'physxParticleSampling:maxSamples'
    physxParticleSamplingParticles: typing.ClassVar[str] = 'physxParticleSampling:particles'
    physxParticleSamplingSamplingDistance: typing.ClassVar[str] = 'physxParticleSampling:samplingDistance'
    physxParticleSamplingVolume: typing.ClassVar[str] = 'physxParticleSampling:volume'
    physxParticleSelfCollision: typing.ClassVar[str] = 'physxParticle:selfCollision'
    physxParticleSelfCollisionFilter: typing.ClassVar[str] = 'physxParticle:selfCollisionFilter'
    physxParticleSimulationPoints: typing.ClassVar[str] = 'physxParticle:simulationPoints'
    physxParticleSmoothingParticleSmoothingEnabled: typing.ClassVar[str] = 'physxParticleSmoothing:particleSmoothingEnabled'
    physxParticleSmoothingStrength: typing.ClassVar[str] = 'physxParticleSmoothing:strength'
    physxParticleSpringDampings: typing.ClassVar[str] = 'physxParticle:springDampings'
    physxParticleSpringIndices: typing.ClassVar[str] = 'physxParticle:springIndices'
    physxParticleSpringRestLengths: typing.ClassVar[str] = 'physxParticle:springRestLengths'
    physxParticleSpringStiffnesses: typing.ClassVar[str] = 'physxParticle:springStiffnesses'
    physxPhysicsDistanceJointSpringDamping: typing.ClassVar[str] = 'physxPhysicsDistanceJoint:springDamping'
    physxPhysicsDistanceJointSpringEnabled: typing.ClassVar[str] = 'physxPhysicsDistanceJoint:springEnabled'
    physxPhysicsDistanceJointSpringStiffness: typing.ClassVar[str] = 'physxPhysicsDistanceJoint:springStiffness'
    physxResidualReportingMaxResidualPositionIteration: typing.ClassVar[str] = 'physxResidualReporting:maxResidualPositionIteration'
    physxResidualReportingMaxResidualVelocityIteration: typing.ClassVar[str] = 'physxResidualReporting:maxResidualVelocityIteration'
    physxResidualReportingRmsResidualPositionIteration: typing.ClassVar[str] = 'physxResidualReporting:rmsResidualPositionIteration'
    physxResidualReportingRmsResidualVelocityIteration: typing.ClassVar[str] = 'physxResidualReporting:rmsResidualVelocityIteration'
    physxRigidBodyAngularDamping: typing.ClassVar[str] = 'physxRigidBody:angularDamping'
    physxRigidBodyCfmScale: typing.ClassVar[str] = 'physxRigidBody:cfmScale'
    physxRigidBodyContactSlopCoefficient: typing.ClassVar[str] = 'physxRigidBody:contactSlopCoefficient'
    physxRigidBodyDisableGravity: typing.ClassVar[str] = 'physxRigidBody:disableGravity'
    physxRigidBodyEnableCCD: typing.ClassVar[str] = 'physxRigidBody:enableCCD'
    physxRigidBodyEnableGyroscopicForces: typing.ClassVar[str] = 'physxRigidBody:enableGyroscopicForces'
    physxRigidBodyEnableSpeculativeCCD: typing.ClassVar[str] = 'physxRigidBody:enableSpeculativeCCD'
    physxRigidBodyLinearDamping: typing.ClassVar[str] = 'physxRigidBody:linearDamping'
    physxRigidBodyLockedPosAxis: typing.ClassVar[str] = 'physxRigidBody:lockedPosAxis'
    physxRigidBodyLockedRotAxis: typing.ClassVar[str] = 'physxRigidBody:lockedRotAxis'
    physxRigidBodyMaxAngularVelocity: typing.ClassVar[str] = 'physxRigidBody:maxAngularVelocity'
    physxRigidBodyMaxContactImpulse: typing.ClassVar[str] = 'physxRigidBody:maxContactImpulse'
    physxRigidBodyMaxDepenetrationVelocity: typing.ClassVar[str] = 'physxRigidBody:maxDepenetrationVelocity'
    physxRigidBodyMaxLinearVelocity: typing.ClassVar[str] = 'physxRigidBody:maxLinearVelocity'
    physxRigidBodyRetainAccelerations: typing.ClassVar[str] = 'physxRigidBody:retainAccelerations'
    physxRigidBodySleepThreshold: typing.ClassVar[str] = 'physxRigidBody:sleepThreshold'
    physxRigidBodySolveContact: typing.ClassVar[str] = 'physxRigidBody:solveContact'
    physxRigidBodySolverPositionIterationCount: typing.ClassVar[str] = 'physxRigidBody:solverPositionIterationCount'
    physxRigidBodySolverVelocityIterationCount: typing.ClassVar[str] = 'physxRigidBody:solverVelocityIterationCount'
    physxRigidBodyStabilizationThreshold: typing.ClassVar[str] = 'physxRigidBody:stabilizationThreshold'
    physxSDFMeshCollisionSdfBitsPerSubgridPixel: typing.ClassVar[str] = 'physxSDFMeshCollision:sdfBitsPerSubgridPixel'
    physxSDFMeshCollisionSdfEnableRemeshing: typing.ClassVar[str] = 'physxSDFMeshCollision:sdfEnableRemeshing'
    physxSDFMeshCollisionSdfMargin: typing.ClassVar[str] = 'physxSDFMeshCollision:sdfMargin'
    physxSDFMeshCollisionSdfNarrowBandThickness: typing.ClassVar[str] = 'physxSDFMeshCollision:sdfNarrowBandThickness'
    physxSDFMeshCollisionSdfResolution: typing.ClassVar[str] = 'physxSDFMeshCollision:sdfResolution'
    physxSDFMeshCollisionSdfSubgridResolution: typing.ClassVar[str] = 'physxSDFMeshCollision:sdfSubgridResolution'
    physxSDFMeshCollisionSdfTriangleCountReductionFactor: typing.ClassVar[str] = 'physxSDFMeshCollision:sdfTriangleCountReductionFactor'
    physxSceneBounceThreshold: typing.ClassVar[str] = 'physxScene:bounceThreshold'
    physxSceneBroadphaseType: typing.ClassVar[str] = 'physxScene:broadphaseType'
    physxSceneCollisionSystem: typing.ClassVar[str] = 'physxScene:collisionSystem'
    physxSceneEnableCCD: typing.ClassVar[str] = 'physxScene:enableCCD'
    physxSceneEnableEnhancedDeterminism: typing.ClassVar[str] = 'physxScene:enableEnhancedDeterminism'
    physxSceneEnableExternalForcesEveryIteration: typing.ClassVar[str] = 'physxScene:enableExternalForcesEveryIteration'
    physxSceneEnableGPUDynamics: typing.ClassVar[str] = 'physxScene:enableGPUDynamics'
    physxSceneEnableResidualReporting: typing.ClassVar[str] = 'physxScene:enableResidualReporting'
    physxSceneEnableSceneQuerySupport: typing.ClassVar[str] = 'physxScene:enableSceneQuerySupport'
    physxSceneEnableStabilization: typing.ClassVar[str] = 'physxScene:enableStabilization'
    physxSceneFrictionCorrelationDistance: typing.ClassVar[str] = 'physxScene:frictionCorrelationDistance'
    physxSceneFrictionOffsetThreshold: typing.ClassVar[str] = 'physxScene:frictionOffsetThreshold'
    physxSceneFrictionType: typing.ClassVar[str] = 'physxScene:frictionType'
    physxSceneGpuCollisionStackSize: typing.ClassVar[str] = 'physxScene:gpuCollisionStackSize'
    physxSceneGpuFoundLostAggregatePairsCapacity: typing.ClassVar[str] = 'physxScene:gpuFoundLostAggregatePairsCapacity'
    physxSceneGpuFoundLostPairsCapacity: typing.ClassVar[str] = 'physxScene:gpuFoundLostPairsCapacity'
    physxSceneGpuHeapCapacity: typing.ClassVar[str] = 'physxScene:gpuHeapCapacity'
    physxSceneGpuMaxDeformableSurfaceContacts: typing.ClassVar[str] = 'physxScene:gpuMaxDeformableSurfaceContacts'
    physxSceneGpuMaxHairContacts: typing.ClassVar[str] = 'physxScene:gpuMaxHairContacts'
    physxSceneGpuMaxNumPartitions: typing.ClassVar[str] = 'physxScene:gpuMaxNumPartitions'
    physxSceneGpuMaxParticleContacts: typing.ClassVar[str] = 'physxScene:gpuMaxParticleContacts'
    physxSceneGpuMaxRigidContactCount: typing.ClassVar[str] = 'physxScene:gpuMaxRigidContactCount'
    physxSceneGpuMaxRigidPatchCount: typing.ClassVar[str] = 'physxScene:gpuMaxRigidPatchCount'
    physxSceneGpuMaxSoftBodyContacts: typing.ClassVar[str] = 'physxScene:gpuMaxSoftBodyContacts'
    physxSceneGpuTempBufferCapacity: typing.ClassVar[str] = 'physxScene:gpuTempBufferCapacity'
    physxSceneGpuTotalAggregatePairsCapacity: typing.ClassVar[str] = 'physxScene:gpuTotalAggregatePairsCapacity'
    physxSceneInvertCollisionGroupFilter: typing.ClassVar[str] = 'physxScene:invertCollisionGroupFilter'
    physxSceneMaxBiasCoefficient: typing.ClassVar[str] = 'physxScene:maxBiasCoefficient'
    physxSceneMaxPositionIterationCount: typing.ClassVar[str] = 'physxScene:maxPositionIterationCount'
    physxSceneMaxVelocityIterationCount: typing.ClassVar[str] = 'physxScene:maxVelocityIterationCount'
    physxSceneMinPositionIterationCount: typing.ClassVar[str] = 'physxScene:minPositionIterationCount'
    physxSceneMinVelocityIterationCount: typing.ClassVar[str] = 'physxScene:minVelocityIterationCount'
    physxSceneQuasistaticEnableQuasistatic: typing.ClassVar[str] = 'physxSceneQuasistatic:enableQuasistatic'
    physxSceneReportKinematicKinematicPairs: typing.ClassVar[str] = 'physxScene:reportKinematicKinematicPairs'
    physxSceneReportKinematicStaticPairs: typing.ClassVar[str] = 'physxScene:reportKinematicStaticPairs'
    physxSceneSolverType: typing.ClassVar[str] = 'physxScene:solverType'
    physxSceneTimeStepsPerSecond: typing.ClassVar[str] = 'physxScene:timeStepsPerSecond'
    physxSceneUpdateType: typing.ClassVar[str] = 'physxScene:updateType'
    physxSphereFillCollisionFillMode: typing.ClassVar[str] = 'physxSphereFillCollision:fillMode'
    physxSphereFillCollisionMaxSpheres: typing.ClassVar[str] = 'physxSphereFillCollision:maxSpheres'
    physxSphereFillCollisionSeedCount: typing.ClassVar[str] = 'physxSphereFillCollision:seedCount'
    physxSphereFillCollisionVoxelResolution: typing.ClassVar[str] = 'physxSphereFillCollision:voxelResolution'
    physxSurfaceVelocitySurfaceAngularVelocity: typing.ClassVar[str] = 'physxSurfaceVelocity:surfaceAngularVelocity'
    physxSurfaceVelocitySurfaceVelocity: typing.ClassVar[str] = 'physxSurfaceVelocity:surfaceVelocity'
    physxSurfaceVelocitySurfaceVelocityEnabled: typing.ClassVar[str] = 'physxSurfaceVelocity:surfaceVelocityEnabled'
    physxSurfaceVelocitySurfaceVelocityLocalSpace: typing.ClassVar[str] = 'physxSurfaceVelocity:surfaceVelocityLocalSpace'
    physxTendon: typing.ClassVar[str] = 'physxTendon'
    physxTendon_MultipleApplyTemplate_Damping: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:damping'
    physxTendon_MultipleApplyTemplate_ForceCoefficient: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:forceCoefficient'
    physxTendon_MultipleApplyTemplate_Gearing: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:gearing'
    physxTendon_MultipleApplyTemplate_JointAxis: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:jointAxis'
    physxTendon_MultipleApplyTemplate_LimitStiffness: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:limitStiffness'
    physxTendon_MultipleApplyTemplate_LocalPos: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:localPos'
    physxTendon_MultipleApplyTemplate_LowerLimit: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:lowerLimit'
    physxTendon_MultipleApplyTemplate_Offset: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:offset'
    physxTendon_MultipleApplyTemplate_ParentAttachment: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:parentAttachment'
    physxTendon_MultipleApplyTemplate_ParentLink: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:parentLink'
    physxTendon_MultipleApplyTemplate_RestLength: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:restLength'
    physxTendon_MultipleApplyTemplate_Stiffness: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:stiffness'
    physxTendon_MultipleApplyTemplate_TendonEnabled: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:tendonEnabled'
    physxTendon_MultipleApplyTemplate_UpperLimit: typing.ClassVar[str] = 'physxTendon:__INSTANCE_NAME__:upperLimit'
    physxTriangleMeshCollisionWeldTolerance: typing.ClassVar[str] = 'physxTriangleMeshCollision:weldTolerance'
    physxTriangleMeshSimplificationCollisionMetric: typing.ClassVar[str] = 'physxTriangleMeshSimplificationCollision:metric'
    physxTriangleMeshSimplificationCollisionWeldTolerance: typing.ClassVar[str] = 'physxTriangleMeshSimplificationCollision:weldTolerance'
    physxTriggerEnterScriptType: typing.ClassVar[str] = 'physxTrigger:enterScriptType'
    physxTriggerLeaveScriptType: typing.ClassVar[str] = 'physxTrigger:leaveScriptType'
    physxTriggerOnEnterScript: typing.ClassVar[str] = 'physxTrigger:onEnterScript'
    physxTriggerOnLeaveScript: typing.ClassVar[str] = 'physxTrigger:onLeaveScript'
    physxTriggerTriggeredCollisions: typing.ClassVar[str] = 'physxTrigger:triggeredCollisions'
    physxVehicleAckermannSteeringMaxSteerAngle: typing.ClassVar[str] = 'physxVehicleAckermannSteering:maxSteerAngle'
    physxVehicleAckermannSteeringStrength: typing.ClassVar[str] = 'physxVehicleAckermannSteering:strength'
    physxVehicleAckermannSteeringTrackWidth: typing.ClassVar[str] = 'physxVehicleAckermannSteering:trackWidth'
    physxVehicleAckermannSteeringWheel0: typing.ClassVar[str] = 'physxVehicleAckermannSteering:wheel0'
    physxVehicleAckermannSteeringWheel1: typing.ClassVar[str] = 'physxVehicleAckermannSteering:wheel1'
    physxVehicleAckermannSteeringWheelBase: typing.ClassVar[str] = 'physxVehicleAckermannSteering:wheelBase'
    physxVehicleAutoGearBoxDownRatios: typing.ClassVar[str] = 'physxVehicleAutoGearBox:downRatios'
    physxVehicleAutoGearBoxLatency: typing.ClassVar[str] = 'physxVehicleAutoGearBox:latency'
    physxVehicleAutoGearBoxUpRatios: typing.ClassVar[str] = 'physxVehicleAutoGearBox:upRatios'
    physxVehicleBrakes: typing.ClassVar[str] = 'physxVehicleBrakes'
    physxVehicleBrakes_MultipleApplyTemplate_MaxBrakeTorque: typing.ClassVar[str] = 'physxVehicleBrakes:__INSTANCE_NAME__:maxBrakeTorque'
    physxVehicleBrakes_MultipleApplyTemplate_TorqueMultipliers: typing.ClassVar[str] = 'physxVehicleBrakes:__INSTANCE_NAME__:torqueMultipliers'
    physxVehicleBrakes_MultipleApplyTemplate_Wheels: typing.ClassVar[str] = 'physxVehicleBrakes:__INSTANCE_NAME__:wheels'
    physxVehicleClutchStrength: typing.ClassVar[str] = 'physxVehicleClutch:strength'
    physxVehicleContextForwardAxis: typing.ClassVar[str] = 'physxVehicleContext:forwardAxis'
    physxVehicleContextLongitudinalAxis: typing.ClassVar[str] = 'physxVehicleContext:longitudinalAxis'
    physxVehicleContextUpAxis: typing.ClassVar[str] = 'physxVehicleContext:upAxis'
    physxVehicleContextUpdateMode: typing.ClassVar[str] = 'physxVehicleContext:updateMode'
    physxVehicleContextVerticalAxis: typing.ClassVar[str] = 'physxVehicleContext:verticalAxis'
    physxVehicleControllerAccelerator: typing.ClassVar[str] = 'physxVehicleController:accelerator'
    physxVehicleControllerBrake: typing.ClassVar[str] = 'physxVehicleController:brake'
    physxVehicleControllerBrake0: typing.ClassVar[str] = 'physxVehicleController:brake0'
    physxVehicleControllerBrake1: typing.ClassVar[str] = 'physxVehicleController:brake1'
    physxVehicleControllerHandbrake: typing.ClassVar[str] = 'physxVehicleController:handbrake'
    physxVehicleControllerSteer: typing.ClassVar[str] = 'physxVehicleController:steer'
    physxVehicleControllerSteerLeft: typing.ClassVar[str] = 'physxVehicleController:steerLeft'
    physxVehicleControllerSteerRight: typing.ClassVar[str] = 'physxVehicleController:steerRight'
    physxVehicleControllerTargetGear: typing.ClassVar[str] = 'physxVehicleController:targetGear'
    physxVehicleDrive: typing.ClassVar[str] = 'physxVehicle:drive'
    physxVehicleDriveBasicPeakTorque: typing.ClassVar[str] = 'physxVehicleDriveBasic:peakTorque'
    physxVehicleDriveStandardAutoGearBox: typing.ClassVar[str] = 'physxVehicleDriveStandard:autoGearBox'
    physxVehicleDriveStandardClutch: typing.ClassVar[str] = 'physxVehicleDriveStandard:clutch'
    physxVehicleDriveStandardEngine: typing.ClassVar[str] = 'physxVehicleDriveStandard:engine'
    physxVehicleDriveStandardGears: typing.ClassVar[str] = 'physxVehicleDriveStandard:gears'
    physxVehicleEngineDampingRateFullThrottle: typing.ClassVar[str] = 'physxVehicleEngine:dampingRateFullThrottle'
    physxVehicleEngineDampingRateZeroThrottleClutchDisengaged: typing.ClassVar[str] = 'physxVehicleEngine:dampingRateZeroThrottleClutchDisengaged'
    physxVehicleEngineDampingRateZeroThrottleClutchEngaged: typing.ClassVar[str] = 'physxVehicleEngine:dampingRateZeroThrottleClutchEngaged'
    physxVehicleEngineIdleRotationSpeed: typing.ClassVar[str] = 'physxVehicleEngine:idleRotationSpeed'
    physxVehicleEngineMaxRotationSpeed: typing.ClassVar[str] = 'physxVehicleEngine:maxRotationSpeed'
    physxVehicleEngineMoi: typing.ClassVar[str] = 'physxVehicleEngine:moi'
    physxVehicleEnginePeakTorque: typing.ClassVar[str] = 'physxVehicleEngine:peakTorque'
    physxVehicleEngineTorqueCurve: typing.ClassVar[str] = 'physxVehicleEngine:torqueCurve'
    physxVehicleGearsRatioScale: typing.ClassVar[str] = 'physxVehicleGears:ratioScale'
    physxVehicleGearsRatios: typing.ClassVar[str] = 'physxVehicleGears:ratios'
    physxVehicleGearsSwitchTime: typing.ClassVar[str] = 'physxVehicleGears:switchTime'
    physxVehicleHighForwardSpeedSubStepCount: typing.ClassVar[str] = 'physxVehicle:highForwardSpeedSubStepCount'
    physxVehicleLateralStickyTireDamping: typing.ClassVar[str] = 'physxVehicle:lateralStickyTireDamping'
    physxVehicleLateralStickyTireThresholdSpeed: typing.ClassVar[str] = 'physxVehicle:lateralStickyTireThresholdSpeed'
    physxVehicleLateralStickyTireThresholdTime: typing.ClassVar[str] = 'physxVehicle:lateralStickyTireThresholdTime'
    physxVehicleLimitSuspensionExpansionVelocity: typing.ClassVar[str] = 'physxVehicle:limitSuspensionExpansionVelocity'
    physxVehicleLongitudinalStickyTireDamping: typing.ClassVar[str] = 'physxVehicle:longitudinalStickyTireDamping'
    physxVehicleLongitudinalStickyTireThresholdSpeed: typing.ClassVar[str] = 'physxVehicle:longitudinalStickyTireThresholdSpeed'
    physxVehicleLongitudinalStickyTireThresholdTime: typing.ClassVar[str] = 'physxVehicle:longitudinalStickyTireThresholdTime'
    physxVehicleLowForwardSpeedSubStepCount: typing.ClassVar[str] = 'physxVehicle:lowForwardSpeedSubStepCount'
    physxVehicleMinActiveLongitudinalSlipDenominator: typing.ClassVar[str] = 'physxVehicle:minActiveLongitudinalSlipDenominator'
    physxVehicleMinLateralSlipDenominator: typing.ClassVar[str] = 'physxVehicle:minLateralSlipDenominator'
    physxVehicleMinLongitudinalSlipDenominator: typing.ClassVar[str] = 'physxVehicle:minLongitudinalSlipDenominator'
    physxVehicleMinPassiveLongitudinalSlipDenominator: typing.ClassVar[str] = 'physxVehicle:minPassiveLongitudinalSlipDenominator'
    physxVehicleMultiWheelDifferentialAverageWheelSpeedRatios: typing.ClassVar[str] = 'physxVehicleMultiWheelDifferential:averageWheelSpeedRatios'
    physxVehicleMultiWheelDifferentialTorqueRatios: typing.ClassVar[str] = 'physxVehicleMultiWheelDifferential:torqueRatios'
    physxVehicleMultiWheelDifferentialWheels: typing.ClassVar[str] = 'physxVehicleMultiWheelDifferential:wheels'
    physxVehicleNCR: typing.ClassVar[str] = 'physxVehicleNCR'
    physxVehicleNCR_MultipleApplyTemplate_CommandValues: typing.ClassVar[str] = 'physxVehicleNCR:__INSTANCE_NAME__:commandValues'
    physxVehicleNCR_MultipleApplyTemplate_SpeedResponses: typing.ClassVar[str] = 'physxVehicleNCR:__INSTANCE_NAME__:speedResponses'
    physxVehicleNCR_MultipleApplyTemplate_SpeedResponsesPerCommandValue: typing.ClassVar[str] = 'physxVehicleNCR:__INSTANCE_NAME__:speedResponsesPerCommandValue'
    physxVehicleSteeringAngleMultipliers: typing.ClassVar[str] = 'physxVehicleSteering:angleMultipliers'
    physxVehicleSteeringMaxSteerAngle: typing.ClassVar[str] = 'physxVehicleSteering:maxSteerAngle'
    physxVehicleSteeringWheels: typing.ClassVar[str] = 'physxVehicleSteering:wheels'
    physxVehicleSubStepThresholdLongitudinalSpeed: typing.ClassVar[str] = 'physxVehicle:subStepThresholdLongitudinalSpeed'
    physxVehicleSuspensionCamberAtMaxCompression: typing.ClassVar[str] = 'physxVehicleSuspension:camberAtMaxCompression'
    physxVehicleSuspensionCamberAtMaxDroop: typing.ClassVar[str] = 'physxVehicleSuspension:camberAtMaxDroop'
    physxVehicleSuspensionCamberAtRest: typing.ClassVar[str] = 'physxVehicleSuspension:camberAtRest'
    physxVehicleSuspensionComplianceSuspensionForceAppPoint: typing.ClassVar[str] = 'physxVehicleSuspensionCompliance:suspensionForceAppPoint'
    physxVehicleSuspensionComplianceTireForceAppPoint: typing.ClassVar[str] = 'physxVehicleSuspensionCompliance:tireForceAppPoint'
    physxVehicleSuspensionComplianceWheelCamberAngle: typing.ClassVar[str] = 'physxVehicleSuspensionCompliance:wheelCamberAngle'
    physxVehicleSuspensionComplianceWheelToeAngle: typing.ClassVar[str] = 'physxVehicleSuspensionCompliance:wheelToeAngle'
    physxVehicleSuspensionLineQueryType: typing.ClassVar[str] = 'physxVehicle:suspensionLineQueryType'
    physxVehicleSuspensionMaxCompression: typing.ClassVar[str] = 'physxVehicleSuspension:maxCompression'
    physxVehicleSuspensionMaxDroop: typing.ClassVar[str] = 'physxVehicleSuspension:maxDroop'
    physxVehicleSuspensionSpringDamperRate: typing.ClassVar[str] = 'physxVehicleSuspension:springDamperRate'
    physxVehicleSuspensionSpringStrength: typing.ClassVar[str] = 'physxVehicleSuspension:springStrength'
    physxVehicleSuspensionSprungMass: typing.ClassVar[str] = 'physxVehicleSuspension:sprungMass'
    physxVehicleSuspensionTravelDistance: typing.ClassVar[str] = 'physxVehicleSuspension:travelDistance'
    physxVehicleTankControllerThrust0: typing.ClassVar[str] = 'physxVehicleTankController:thrust0'
    physxVehicleTankControllerThrust1: typing.ClassVar[str] = 'physxVehicleTankController:thrust1'
    physxVehicleTankDifferentialNumberOfWheelsPerTrack: typing.ClassVar[str] = 'physxVehicleTankDifferential:numberOfWheelsPerTrack'
    physxVehicleTankDifferentialThrustIndexPerTrack: typing.ClassVar[str] = 'physxVehicleTankDifferential:thrustIndexPerTrack'
    physxVehicleTankDifferentialTrackToWheelIndices: typing.ClassVar[str] = 'physxVehicleTankDifferential:trackToWheelIndices'
    physxVehicleTankDifferentialWheelIndicesInTrackOrder: typing.ClassVar[str] = 'physxVehicleTankDifferential:wheelIndicesInTrackOrder'
    physxVehicleTireCamberStiffness: typing.ClassVar[str] = 'physxVehicleTire:camberStiffness'
    physxVehicleTireCamberStiffnessPerUnitGravity: typing.ClassVar[str] = 'physxVehicleTire:camberStiffnessPerUnitGravity'
    physxVehicleTireFrictionTable: typing.ClassVar[str] = 'physxVehicleTire:frictionTable'
    physxVehicleTireFrictionVsSlipGraph: typing.ClassVar[str] = 'physxVehicleTire:frictionVsSlipGraph'
    physxVehicleTireLatStiffX: typing.ClassVar[str] = 'physxVehicleTire:latStiffX'
    physxVehicleTireLatStiffY: typing.ClassVar[str] = 'physxVehicleTire:latStiffY'
    physxVehicleTireLateralStiffnessGraph: typing.ClassVar[str] = 'physxVehicleTire:lateralStiffnessGraph'
    physxVehicleTireLongitudinalStiffness: typing.ClassVar[str] = 'physxVehicleTire:longitudinalStiffness'
    physxVehicleTireLongitudinalStiffnessPerUnitGravity: typing.ClassVar[str] = 'physxVehicleTire:longitudinalStiffnessPerUnitGravity'
    physxVehicleTireRestLoad: typing.ClassVar[str] = 'physxVehicleTire:restLoad'
    physxVehicleVehicleEnabled: typing.ClassVar[str] = 'physxVehicle:vehicleEnabled'
    physxVehicleWheelAttachmentCollisionGroup: typing.ClassVar[str] = 'physxVehicleWheelAttachment:collisionGroup'
    physxVehicleWheelAttachmentDriven: typing.ClassVar[str] = 'physxVehicleWheelAttachment:driven'
    physxVehicleWheelAttachmentIndex: typing.ClassVar[str] = 'physxVehicleWheelAttachment:index'
    physxVehicleWheelAttachmentSuspension: typing.ClassVar[str] = 'physxVehicleWheelAttachment:suspension'
    physxVehicleWheelAttachmentSuspensionForceAppPointOffset: typing.ClassVar[str] = 'physxVehicleWheelAttachment:suspensionForceAppPointOffset'
    physxVehicleWheelAttachmentSuspensionFrameOrientation: typing.ClassVar[str] = 'physxVehicleWheelAttachment:suspensionFrameOrientation'
    physxVehicleWheelAttachmentSuspensionFramePosition: typing.ClassVar[str] = 'physxVehicleWheelAttachment:suspensionFramePosition'
    physxVehicleWheelAttachmentSuspensionTravelDirection: typing.ClassVar[str] = 'physxVehicleWheelAttachment:suspensionTravelDirection'
    physxVehicleWheelAttachmentTire: typing.ClassVar[str] = 'physxVehicleWheelAttachment:tire'
    physxVehicleWheelAttachmentTireForceAppPointOffset: typing.ClassVar[str] = 'physxVehicleWheelAttachment:tireForceAppPointOffset'
    physxVehicleWheelAttachmentWheel: typing.ClassVar[str] = 'physxVehicleWheelAttachment:wheel'
    physxVehicleWheelAttachmentWheelCenterOfMassOffset: typing.ClassVar[str] = 'physxVehicleWheelAttachment:wheelCenterOfMassOffset'
    physxVehicleWheelAttachmentWheelFrameOrientation: typing.ClassVar[str] = 'physxVehicleWheelAttachment:wheelFrameOrientation'
    physxVehicleWheelAttachmentWheelFramePosition: typing.ClassVar[str] = 'physxVehicleWheelAttachment:wheelFramePosition'
    physxVehicleWheelControllerBrakeTorque: typing.ClassVar[str] = 'physxVehicleWheelController:brakeTorque'
    physxVehicleWheelControllerDriveTorque: typing.ClassVar[str] = 'physxVehicleWheelController:driveTorque'
    physxVehicleWheelControllerSteerAngle: typing.ClassVar[str] = 'physxVehicleWheelController:steerAngle'
    physxVehicleWheelDampingRate: typing.ClassVar[str] = 'physxVehicleWheel:dampingRate'
    physxVehicleWheelMass: typing.ClassVar[str] = 'physxVehicleWheel:mass'
    physxVehicleWheelMaxBrakeTorque: typing.ClassVar[str] = 'physxVehicleWheel:maxBrakeTorque'
    physxVehicleWheelMaxHandBrakeTorque: typing.ClassVar[str] = 'physxVehicleWheel:maxHandBrakeTorque'
    physxVehicleWheelMaxSteerAngle: typing.ClassVar[str] = 'physxVehicleWheel:maxSteerAngle'
    physxVehicleWheelMoi: typing.ClassVar[str] = 'physxVehicleWheel:moi'
    physxVehicleWheelRadius: typing.ClassVar[str] = 'physxVehicleWheel:radius'
    physxVehicleWheelToeAngle: typing.ClassVar[str] = 'physxVehicleWheel:toeAngle'
    physxVehicleWheelWidth: typing.ClassVar[str] = 'physxVehicleWheel:width'
    points0: typing.ClassVar[str] = 'points0'
    points1: typing.ClassVar[str] = 'points1'
    posX: typing.ClassVar[str] = 'posX'
    posY: typing.ClassVar[str] = 'posY'
    posZ: typing.ClassVar[str] = 'posZ'
    preventClimbing: typing.ClassVar[str] = 'preventClimbing'
    preventClimbingForceSliding: typing.ClassVar[str] = 'preventClimbingForceSliding'
    quasistaticactors: typing.ClassVar[str] = 'quasistaticactors'
    raycast: typing.ClassVar[str] = 'raycast'
    referenceFrameIsCenterOfMass: typing.ClassVar[str] = 'physxVehicle:referenceFrameIsCenterOfMass'
    restOffset: typing.ClassVar[str] = 'restOffset'
    rotX: typing.ClassVar[str] = 'rotX'
    rotY: typing.ClassVar[str] = 'rotY'
    rotZ: typing.ClassVar[str] = 'rotZ'
    sAP: typing.ClassVar[str] = 'SAP'
    sAT: typing.ClassVar[str] = 'SAT'
    scriptFile: typing.ClassVar[str] = 'scriptFile'
    sdf: typing.ClassVar[str] = 'sdf'
    simulationOwner: typing.ClassVar[str] = 'simulationOwner'
    solidRestOffset: typing.ClassVar[str] = 'solidRestOffset'
    solverPositionIterationCount: typing.ClassVar[str] = 'solverPositionIterationCount'
    sphereFill: typing.ClassVar[str] = 'sphereFill'
    state: typing.ClassVar[str] = 'state'
    state_MultipleApplyTemplate_PhysicsPosition: typing.ClassVar[str] = 'state:__INSTANCE_NAME__:physics:position'
    state_MultipleApplyTemplate_PhysicsVelocity: typing.ClassVar[str] = 'state:__INSTANCE_NAME__:physics:velocity'
    steer: typing.ClassVar[str] = 'steer'
    surface: typing.ClassVar[str] = 'surface'
    sweep: typing.ClassVar[str] = 'sweep'
    synchronous: typing.ClassVar[str] = 'Synchronous'
    tGS: typing.ClassVar[str] = 'TGS'
    transX: typing.ClassVar[str] = 'transX'
    transY: typing.ClassVar[str] = 'transY'
    transZ: typing.ClassVar[str] = 'transZ'
    triangleMesh: typing.ClassVar[str] = 'triangleMesh'
    twoDirectional: typing.ClassVar[str] = 'twoDirectional'
    undefined: typing.ClassVar[str] = 'undefined'
    velocityChange: typing.ClassVar[str] = 'velocityChange'
    vertices: typing.ClassVar[str] = 'Vertices'
    wind: typing.ClassVar[str] = 'wind'
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
    __instance_size__: typing.ClassVar[int] = 32
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
__MFB_FULL_PACKAGE_NAME: str = 'physxSchema'
