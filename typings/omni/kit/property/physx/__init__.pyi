from __future__ import annotations
from collections import namedtuple
import omni as omni
from omni.kit.property.physx.builders import ModelWithWidgetBuilder
from omni.kit.property.physx.database import Component
from omni.kit.property.physx.utils import get_title_from_schema
from omni.kit.property.physx.utils import get_widget_name
from omni.kit.property.physx.utils import rebuild_property_window
from omni.kit.property.physx.widgets import InvisibleWidget
from omni.kit.property.physx.widgets import JointVisualizationWidget
from omni.kit.property.physx.widgets import MainFrameWidget
from omni.kit.property.physx.widgets import PhysicsCustomPropertiesWidget
from omni.kit.property.physx.widgets import PhysicsDefaultMaterialBindingWidget
from omni.kit.property.physx.widgets import PhysicsMaterialBindingWidget
from omni.kit.property.physx.widgets import PhysicsWidget
from omni.kit.window import property as p
import pxr.PhysxSchema
import pxr.UsdGeom
import pxr.UsdPhysics
import typing
from . import builders
from . import database
from . import databaseUtils
from . import externals
from . import models
from . import overrides
from . import utils
from . import widgets
__all__ = ['Component', 'CustomPropertyData', 'Extension', 'InvisibleWidget', 'JointVisualizationWidget', 'MainFrameWidget', 'Manager', 'ModelWithWidgetBuilder', 'PhysicsCustomPropertiesWidget', 'PhysicsDefaultMaterialBindingWidget', 'PhysicsMaterialBindingWidget', 'PhysicsWidget', 'builders', 'custom_builders', 'custom_widgets', 'database', 'databaseUtils', 'externals', 'get_title_from_schema', 'get_widget_name', 'models', 'namedtuple', 'omni', 'overrides', 'p', 'rebuild_property_window', 'refresh', 'register_builder', 'register_custom_property', 'register_schema', 'register_widget', 'unregister_builder', 'unregister_schema', 'unregister_widget', 'utils', 'widgets']
class CustomPropertyData(tuple):
    """
    CustomPropertyData(display_name, read_only)
    """
    __match_args__: typing.ClassVar[tuple] = ('display_name', 'read_only')
    __slots__: typing.ClassVar[tuple] = tuple()
    _field_defaults: typing.ClassVar[dict] = {}
    _fields: typing.ClassVar[tuple] = ('display_name', 'read_only')
    @staticmethod
    def __new__(_cls, display_name, read_only):
        """
        Create new instance of CustomPropertyData(display_name, read_only)
        """
    @classmethod
    def _make(cls, iterable):
        """
        Make a new CustomPropertyData object from a sequence or iterable
        """
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
    def _asdict(self):
        """
        Return a new dict which maps field names to their values.
        """
    def _replace(self, **kwds):
        """
        Return a new CustomPropertyData object replacing specified fields with new values
        """
class Extension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
class Manager:
    instance: typing.ClassVar[Manager]  # value = <omni.kit.property.physx.Manager object>
    scheme: typing.ClassVar[str] = 'prim'
    def __init__(self):
        ...
    def _register_widgets(self):
        ...
    def _unregister_widgets(self):
        ...
    def on_shutdown(self):
        ...
    def register_property(self, name, data):
        ...
def refresh():
    ...
def register_builder(property_name, builder_data):
    ...
def register_custom_property(name, override_display_name = None, read_only = False):
    ...
def register_schema(schema, order = None, component = None, custom_widget = None, prefix = None):
    ...
def register_widget(name, widget):
    ...
def unregister_builder(property_name):
    ...
def unregister_schema(schema):
    ...
def unregister_widget(name):
    ...
custom_builders: dict  # value = {'physxRigidBody:lockedPosAxis': [builders.BitfieldWidgetBuilder, ['X', 'Y', 'Z']], 'physxRigidBody:lockedRotAxis': [builders.BitfieldWidgetBuilder, ['X', 'Y', 'Z']], 'physics:body0': [builders.RelationshipWidgetBuilder, [pxr.UsdGeom.Xformable], 1], 'physics:body1': [builders.RelationshipWidgetBuilder, [pxr.UsdGeom.Xformable], 1], 'physics:localRot0': [builders.QuatEulerRotationBuilder], 'physics:localRot1': [builders.QuatEulerRotationBuilder], 'physics:principalAxes': [builders.QuatEulerRotationBuilder], 'physics:simulationOwner': [builders.RelationshipWidgetBuilder, [pxr.UsdPhysics.Scene]], 'physics:filteredGroups': [builders.RelationshipWidgetBuilder, [pxr.UsdPhysics.CollisionGroup]], 'physxContactReport:reportPairs': [builders.RelationshipWidgetBuilder, list(), 0, <function <lambda> at 0x709ee7fc2d40>], 'physics:hinge0': [builders.RelationshipWidgetBuilder, [pxr.UsdPhysics.RevoluteJoint], 1], 'physics:hinge1': [builders.RelationshipWidgetBuilder, [pxr.UsdPhysics.RevoluteJoint], 1], 'physics:hinge': [builders.RelationshipWidgetBuilder, [pxr.UsdPhysics.RevoluteJoint], 1], 'physics:prismatic': [builders.RelationshipWidgetBuilder, [pxr.UsdPhysics.PrismaticJoint], 1], 'groundMaterials': [builders.RelationshipWidgetBuilder, list(), 0, <function <lambda> at 0x709ee7fc2dd0>], 'physxVehicleContext:verticalAxis': [builders.PrettyPrintTokenComboBuilder, ['X+', 'X-', 'Y+', 'Y-', 'Z+', 'Z-', 'undefined']], 'physxVehicleContext:longitudinalAxis': [builders.PrettyPrintTokenComboBuilder, ['X+', 'X-', 'Y+', 'Y-', 'Z+', 'Z-', 'undefined']], 'physxVehicleTire:frictionTable': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc2e60>], 'physxVehicleWheelAttachment:wheel': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc2ef0>], 'physxVehicleWheelAttachment:tire': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc2f80>], 'physxVehicleWheelAttachment:suspension': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc3010>], 'physxVehicleWheelAttachment:suspensionFrameOrientation': [builders.QuatEulerRotationBuilder], 'physxVehicleWheelAttachment:wheelFrameOrientation': [builders.QuatEulerRotationBuilder], 'physxVehicleWheelAttachment:collisionGroup': [builders.RelationshipWidgetBuilder, [pxr.UsdPhysics.CollisionGroup], 1], 'physxVehicleDriveStandard:engine': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc30a0>], 'physxVehicleDriveStandard:gears': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc3130>], 'physxVehicleDriveStandard:autoGearBox': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc31c0>], 'physxVehicleDriveStandard:clutch': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc3250>], 'physxVehicle:drive': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc32e0>], 'physxVehicle:referenceFrameIsCenterOfMass': [builders.ReferenceFrameIsCenterOfMassWidgetBuilder, 'physxVehicle:referenceFrameIsCenterOfMass'], 'physxPhysics:simulationOwner': [builders.RelationshipWidgetBuilder, [pxr.UsdPhysics.Scene, pxr.PhysxSchema.PhysxParticleSystem], 1], 'rigid': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc3370>], 'deformable': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc3400>], 'physxScene:broadphaseType': [builders.ModelWithWidgetBuilder], 'physxScene:collisionSystem': [builders.ModelWithWidgetBuilder], 'state:angular:physics:position': [builders.ModelWithWidgetBuilder], 'state:angular:physics:velocity': [builders.ModelWithWidgetBuilder], 'state:linear:physics:position': [builders.ModelWithWidgetBuilder], 'state:linear:physics:velocity': [builders.ModelWithWidgetBuilder], 'state:rotX:physics:position': [builders.ModelWithWidgetBuilder], 'state:rotX:physics:velocity': [builders.ModelWithWidgetBuilder], 'state:rotY:physics:position': [builders.ModelWithWidgetBuilder], 'state:rotY:physics:velocity': [builders.ModelWithWidgetBuilder], 'state:rotZ:physics:position': [builders.ModelWithWidgetBuilder], 'state:rotZ:physics:velocity': [builders.ModelWithWidgetBuilder], 'state:transX:physics:position': [builders.ModelWithWidgetBuilder], 'state:transX:physics:velocity': [builders.ModelWithWidgetBuilder], 'state:transY:physics:position': [builders.ModelWithWidgetBuilder], 'state:transY:physics:velocity': [builders.ModelWithWidgetBuilder], 'state:transZ:physics:position': [builders.ModelWithWidgetBuilder], 'state:transZ:physics:velocity': [builders.ModelWithWidgetBuilder], 'physxDeformable:kinematicEnabled': [builders.ModelWithWidgetBuilder], 'physxDeformable:simulationHexahedralResolution': [builders.ModelWithWidgetBuilder], 'physxDeformable:collisionSimplificationRemeshing': [builders.ModelWithWidgetBuilder], 'physxDeformable:collisionSimplificationRemeshingResolution': [builders.ModelWithWidgetBuilder], 'physxDeformable:collisionSimplificationTargetTriangleCount': [builders.ModelWithWidgetBuilder], 'physxDeformable:collisionSimplificationForceConforming': [builders.ModelWithWidgetBuilder], 'physxAutoAttachment:enableDeformableVertexAttachments': [builders.ModelWithWidgetBuilder], 'physxAutoAttachment:deformableVertexOverlapOffset': [builders.ModelWithWidgetBuilder], 'physxAutoAttachment:enableRigidSurfaceAttachments': [builders.ModelWithWidgetBuilder], 'physxAutoAttachment:rigidSurfaceSamplingDistance': [builders.ModelWithWidgetBuilder], 'physxAutoAttachment:enableCollisionFiltering': [builders.ModelWithWidgetBuilder], 'physxAutoAttachment:collisionFilteringOffset': [builders.ModelWithWidgetBuilder], 'physxAutoAttachment:maskShapes': [builders.RelationshipWidgetBuilder, list(), 0, <function <lambda> at 0x709ee7fc3490>], 'parentLink': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc3520>], 'jointAxis': [builders.HideWidgetBuilder], 'physics:approximation': [builders.PrettyPrintTokenComboBuilder, ['Triangle Mesh', 'Convex Decomposition', 'Convex Hull', 'Bounding Sphere', 'Bounding Cube', 'Mesh Simplification'], [('sdf', 'SDF Mesh'), ('sphereFill', 'Sphere Approximation')]], 'actor0': [builders.RelationshipWidgetBuilder, [pxr.UsdGeom.Xformable], 1], 'actor1': [builders.RelationshipWidgetBuilder, [pxr.UsdGeom.Xformable], 1], 'simulationOwner': [builders.RelationshipWidgetBuilder, [pxr.UsdPhysics.Scene], 1], 'physics:localSpaceVelocities': [builders.LocalSpaceVelocitiesWidgetBuilder, 'physics:localSpaceVelocities'], 'physxMaterial:compliantContactDamping': [builders.ModelWithWidgetBuilder], 'physxMimicJoint:rotX:referenceJoint': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc35b0>], 'physxMimicJoint:rotY:referenceJoint': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc3640>], 'physxMimicJoint:rotZ:referenceJoint': [builders.RelationshipWidgetBuilder, list(), 1, <function <lambda> at 0x709ee7fc36d0>], 'physxMimicJoint:rotX:referenceJointAxis': [builders.ModelWithWidgetBuilder], 'physxMimicJoint:rotY:referenceJointAxis': [builders.ModelWithWidgetBuilder], 'physxMimicJoint:rotZ:referenceJointAxis': [builders.ModelWithWidgetBuilder]}
custom_widgets: dict = {pxr.UsdPhysics.MassAPI: widgets.MassAPIWidget, pxr.UsdPhysics.Joint: widgets.JointWidget, pxr.UsdPhysics.FixedJoint: widgets.FixedJointWidget, pxr.UsdPhysics.RevoluteJoint: widgets.RevoluteJointWidget, pxr.UsdPhysics.PrismaticJoint: widgets.PrismaticJointWidget, pxr.UsdPhysics.DistanceJoint: widgets.DistanceJointWidget, pxr.UsdPhysics.SphericalJoint: widgets.SphericalJointWidget, pxr.PhysxSchema.PhysxPhysicsGearJoint: widgets.GearJointWidget, pxr.PhysxSchema.PhysxPhysicsRackAndPinionJoint: widgets.RackAndPinionJoint, pxr.UsdPhysics.LimitAPI: widgets.LimitWidget, pxr.UsdPhysics.DriveAPI: widgets.DriveWidget, pxr.PhysxSchema.JointStateAPI: widgets.JointStateWidget, pxr.UsdPhysics.Scene: widgets.ExtendedSceneWidget, pxr.UsdPhysics.MaterialAPI: widgets.ExtendedMaterialWidget, pxr.PhysxSchema.PhysxTendonAxisAPI: widgets.FixedTendonWidget, pxr.PhysxSchema.PhysxTendonAxisRootAPI: widgets.FixedTendonWidget, pxr.PhysxSchema.PhysxTendonAttachmentRootAPI: widgets.SpatialTendonWidget, pxr.PhysxSchema.PhysxTendonAttachmentAPI: widgets.SpatialTendonWidget, pxr.PhysxSchema.PhysxTendonAttachmentLeafAPI: widgets.SpatialTendonWidget, pxr.UsdPhysics.CollisionAPI: widgets.ExtendedColliderWidget, pxr.UsdPhysics.RigidBodyAPI: widgets.LocalSpaceVelocitiesWidget, pxr.PhysxSchema.PhysxDeformableBodyAPI: widgets.ExtendedDeformableBodyWidget, pxr.PhysxSchema.PhysxDeformableSurfaceAPI: widgets.ExtendedDeformableSurfaceWidget, pxr.PhysxSchema.PhysxDeformableSurfaceMaterialAPI: widgets.ExtendedDeformalbeSurfaceMaterialWidget, pxr.PhysxSchema.PhysxPhysicsAttachment: widgets.ExtendedAttachmentWidget, pxr.PhysxSchema.PhysxAutoAttachmentAPI: widgets.ExtendedComputeAutoAttachmentWidget, pxr.PhysxSchema.TetrahedralMesh: widgets.ExtendedTetrahedralMeshWidget, pxr.PhysxSchema.PhysxVehicleContextAPI: widgets.ExtendedVehicleContextWidget, pxr.PhysxSchema.PhysxVehicleAPI: widgets.ExtendedVehicleWidget, pxr.PhysxSchema.PhysxVehicleWheelAPI: widgets.ExtendedVehicleWheelWidget, pxr.PhysxSchema.PhysxVehicleSuspensionAPI: widgets.ExtendedVehicleSuspensionWidget, pxr.PhysxSchema.PhysxVehicleTireAPI: widgets.ExtendedVehicleTireWidget, pxr.PhysxSchema.PhysxVehicleWheelAttachmentAPI: widgets.ExtendedVehicleWheelAttachmentWidget, pxr.PhysxSchema.PhysxVehicleDriveStandardAPI: widgets.ExtendedVehicleDriveStandardWidget, pxr.PhysxSchema.PhysxVehicleMultiWheelDifferentialAPI: widgets.ExtendedVehicleMultiWheelDifferentialWidget, pxr.PhysxSchema.PhysxVehicleControllerAPI: widgets.ExtendedVehicleControllerWidget, pxr.PhysxSchema.PhysxVehicleTankControllerAPI: widgets.ExtendedVehicleControllerBaseWidget, pxr.PhysxSchema.PhysxParticleClothAPI: widgets.ExtendedParticleClothWidget, pxr.PhysxSchema.PhysxAutoParticleClothAPI: widgets.ExtendedAutoParticleClothWidget, pxr.PhysxSchema.PhysxParticleSystem: widgets.ExtendedParticleSystemWidget, pxr.PhysxSchema.PhysxMimicJointAPI: widgets.ExtendedMimicJointWidget}
