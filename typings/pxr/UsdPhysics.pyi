from __future__ import annotations
import pxr.Usd
import pxr.UsdGeom
import typing
__all__ = ['ArticulationRootAPI', 'CollisionAPI', 'CollisionGroup', 'CollisionGroupTable', 'DistanceJoint', 'DriveAPI', 'FilteredPairsAPI', 'FixedJoint', 'Joint', 'LimitAPI', 'MassAPI', 'MassUnits', 'MaterialAPI', 'MeshCollisionAPI', 'PrismaticJoint', 'RevoluteJoint', 'RigidBodyAPI', 'Scene', 'SphericalJoint', 'Tokens']
class ArticulationRootAPI(pxr.Usd.APISchemaBase):
    """
    
    PhysicsArticulationRootAPI can be applied to a scene graph node, and
    marks the subtree rooted here for inclusion in one or more reduced
    coordinate articulations. For floating articulations, this should be
    on the root body. For fixed articulations (robotics jargon for e.g. a
    robot arm for welding that is bolted to the floor), this API can be on
    a direct or indirect parent of the root joint which is connected to
    the world, or on the joint itself\\.\\.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> ArticulationRootAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"PhysicsArticulationRootAPI"to the
        token-valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdPhysicsArticulationRootAPI object is returned upon success.
        An invalid (or empty) UsdPhysicsArticulationRootAPI object is returned
        upon failure. See UsdPrim::ApplyAPI() for conditions resulting in
        failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, whyNot) -> bool
        
        
        Returns true if this **single-apply** API schema can be applied to the
        given ``prim`` .
        
        
        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates ``whyNot`` with the reason it can not be
        applied.
        
        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        whyNot : str
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> ArticulationRootAPI
        
        
        Return a UsdPhysicsArticulationRootAPI holding the prim adhering to
        this schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsArticulationRootAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsArticulationRootAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsArticulationRootAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsArticulationRootAPI on the prim held by
        ``schemaObj`` .
        
        
        Should be preferred over UsdPhysicsArticulationRootAPI
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class CollisionAPI(pxr.Usd.APISchemaBase):
    """
    
    Applies collision attributes to a UsdGeomXformable prim. If a
    simulation is running, this geometry will collide with other
    geometries that have PhysicsCollisionAPI applied. If a prim in the
    parent hierarchy has the RigidBodyAPI applied, this collider is a part
    of that body. If there is no body in the parent hierarchy, this
    collider is considered to be static.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> CollisionAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"PhysicsCollisionAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdPhysicsCollisionAPI object is returned upon success. An
        invalid (or empty) UsdPhysicsCollisionAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, whyNot) -> bool
        
        
        Returns true if this **single-apply** API schema can be applied to the
        given ``prim`` .
        
        
        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates ``whyNot`` with the reason it can not be
        applied.
        
        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        whyNot : str
        
        
        """
    @staticmethod
    def CreateCollisionEnabledAttr(*args, **kwargs):
        """
        
        CreateCollisionEnabledAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetCollisionEnabledAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateSimulationOwnerRel(*args, **kwargs):
        """
        
        CreateSimulationOwnerRel() -> Relationship
        
        
        See GetSimulationOwnerRel() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> CollisionAPI
        
        
        Return a UsdPhysicsCollisionAPI holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsCollisionAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetCollisionEnabledAttr(*args, **kwargs):
        """
        
        GetCollisionEnabledAttr() -> Attribute
        
        
        Determines if the PhysicsCollisionAPI is enabled.
        
        
        
        Declaration
        
        ``bool physics:collisionEnabled = 1``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def GetSimulationOwnerRel(*args, **kwargs):
        """
        
        GetSimulationOwnerRel() -> Relationship
        
        
        Single PhysicsScene that will simulate this collider.
        
        
        By default this object belongs to the first PhysicsScene. Note that if
        a RigidBodyAPI in the hierarchy above has a different simulationOwner
        then it has a precedence over this relationship.
        
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsCollisionAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsCollisionAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsCollisionAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdPhysicsCollisionAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class CollisionGroup(pxr.Usd.Typed):
    """
    
    Defines a collision group for coarse filtering. When a collision
    occurs between two objects that have a PhysicsCollisionGroup assigned,
    they will collide with each other unless this PhysicsCollisionGroup
    pair is filtered. See filteredGroups attribute.
    
    A CollectionAPI:colliders maintains a list of PhysicsCollisionAPI
    rel-s that defines the members of this Collisiongroup.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def ComputeCollisionGroupTable(*args, **kwargs):
        """
        
        **classmethod** ComputeCollisionGroupTable(stage) -> CollisionGroupTable
        
        
        Compute a table encoding all the collision groups filter rules for a
        stage.
        
        
        This can be used as a reference to validate an implementation of the
        collision groups filters. The returned table is diagonally symmetric.
        
        
        Parameters
        ----------
        stage : Stage
        
        
        """
    @staticmethod
    def CreateFilteredGroupsRel(*args, **kwargs):
        """
        
        CreateFilteredGroupsRel() -> Relationship
        
        
        See GetFilteredGroupsRel() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateInvertFilteredGroupsAttr(*args, **kwargs):
        """
        
        CreateInvertFilteredGroupsAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetInvertFilteredGroupsAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateMergeGroupNameAttr(*args, **kwargs):
        """
        
        CreateMergeGroupNameAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetMergeGroupNameAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> CollisionGroup
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> CollisionGroup
        
        
        Return a UsdPhysicsCollisionGroup holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsCollisionGroup(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetCollidersCollectionAPI(*args, **kwargs):
        """
        
        GetCollidersCollectionAPI() -> CollectionAPI
        
        
        Return the UsdCollectionAPI interface used for defining what colliders
        belong to the CollisionGroup.
        
        
        
        """
    @staticmethod
    def GetFilteredGroupsRel(*args, **kwargs):
        """
        
        GetFilteredGroupsRel() -> Relationship
        
        
        References a list of PhysicsCollisionGroups with which collisions
        should be ignored.
        
        
        
        """
    @staticmethod
    def GetInvertFilteredGroupsAttr(*args, **kwargs):
        """
        
        GetInvertFilteredGroupsAttr() -> Attribute
        
        
        Normally, the filter will disable collisions against the selected
        filter groups.
        
        
        However, if this option is set, the filter will disable collisions
        against all colliders except for those in the selected filter groups.
        
        Declaration
        
        ``bool physics:invertFilteredGroups``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        
        
        """
    @staticmethod
    def GetMergeGroupNameAttr(*args, **kwargs):
        """
        
        GetMergeGroupNameAttr() -> Attribute
        
        
        If non-empty, any collision groups in a stage with a matching
        mergeGroup should be considered to refer to the same collection.
        
        
        Matching collision groups should behave as if there were a single
        group containing referenced colliders and filter groups from both
        collections.
        
        Declaration
        
        ``string physics:mergeGroup``
        
        C++ Type
        
        std::string
        
        Usd Type
        
        SdfValueTypeNames->String
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsCollisionGroup on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsCollisionGroup::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsCollisionGroup on the prim held by ``schemaObj``
        .
        
        
        Should be preferred over UsdPhysicsCollisionGroup
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class CollisionGroupTable(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 80
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
class DistanceJoint(Joint):
    """
    
    Predefined distance joint type (Distance between rigid bodies may be
    limited to given minimum or maximum distance.)
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateMaxDistanceAttr(*args, **kwargs):
        """
        
        CreateMaxDistanceAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetMaxDistanceAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateMinDistanceAttr(*args, **kwargs):
        """
        
        CreateMinDistanceAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetMinDistanceAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> DistanceJoint
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> DistanceJoint
        
        
        Return a UsdPhysicsDistanceJoint holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsDistanceJoint(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetMaxDistanceAttr(*args, **kwargs):
        """
        
        GetMaxDistanceAttr() -> Attribute
        
        
        Maximum distance.
        
        
        If attribute is negative, the joint is not limited. Units: distance.
        
        Declaration
        
        ``float physics:maxDistance = -1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetMinDistanceAttr(*args, **kwargs):
        """
        
        GetMinDistanceAttr() -> Attribute
        
        
        Minimum distance.
        
        
        If attribute is negative, the joint is not limited. Units: distance.
        
        Declaration
        
        ``float physics:minDistance = -1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsDistanceJoint on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsDistanceJoint::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsDistanceJoint on the prim held by ``schemaObj``
        .
        
        
        Should be preferred over UsdPhysicsDistanceJoint
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class DriveAPI(pxr.Usd.APISchemaBase):
    """
    
    The PhysicsDriveAPI when applied to any joint primitive will drive the
    joint towards a given target. The PhysicsDriveAPI is a multipleApply
    schema: drive can be set per
    axis"transX","transY","transZ","rotX","rotY","rotZ"or its"linear"for
    prismatic joint or"angular"for revolute joints. Setting these as a
    multipleApply schema TfToken name will define the degree of freedom
    the DriveAPI is applied to. Each drive is an implicit force-limited
    damped spring: Force or acceleration = stiffness \\* (targetPosition -
    position)
    
       - damping \\* (targetVelocity - velocity)
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdPhysicsTokens. So to set an attribute to the value"rightHanded",
    use UsdPhysicsTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim, name) -> DriveAPI
        
        
        Applies this **multiple-apply** API schema to the given ``prim`` along
        with the given instance name, ``name`` .
        
        
        This information is stored by adding"PhysicsDriveAPI:<i>name</i>"to
        the token-valued, listOp metadata *apiSchemas* on the prim. For
        example, if ``name`` is'instance1', the
        token'PhysicsDriveAPI:instance1'is added to'apiSchemas'.
        
        A valid UsdPhysicsDriveAPI object is returned upon success. An invalid
        (or empty) UsdPhysicsDriveAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, name, whyNot) -> bool
        
        
        Returns true if this **multiple-apply** API schema can be applied,
        with the given instance name, ``name`` , to the given ``prim`` .
        
        
        If this schema can not be a applied the prim, this returns false and,
        if provided, populates ``whyNot`` with the reason it can not be
        applied.
        
        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        whyNot : str
        
        
        """
    @staticmethod
    def CreateDampingAttr(*args, **kwargs):
        """
        
        CreateDampingAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDampingAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateMaxForceAttr(*args, **kwargs):
        """
        
        CreateMaxForceAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetMaxForceAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateStiffnessAttr(*args, **kwargs):
        """
        
        CreateStiffnessAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetStiffnessAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateTargetPositionAttr(*args, **kwargs):
        """
        
        CreateTargetPositionAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetTargetPositionAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateTargetVelocityAttr(*args, **kwargs):
        """
        
        CreateTargetVelocityAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetTargetVelocityAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateTypeAttr(*args, **kwargs):
        """
        
        CreateTypeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetTypeAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> DriveAPI
        
        
        Return a UsdPhysicsDriveAPI holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        ``path`` must be of the format<path>.drive:name.
        
        This is shorthand for the following:
        
        .. code-block:: text
        
          TfToken name = SdfPath::StripNamespace(path.GetToken());
          UsdPhysicsDriveAPI(
              stage->GetPrimAtPath(path.GetPrimPath()), name);
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        
        ----------------------------------------------------------------------
        
        Get(prim, name) -> DriveAPI
        
        
        Return a UsdPhysicsDriveAPI with name ``name`` holding the prim
        ``prim`` .
        
        
        Shorthand for UsdPhysicsDriveAPI(prim, name);
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        
        """
    @staticmethod
    def GetAll(*args, **kwargs):
        """
        
        **classmethod** GetAll(prim) -> list[DriveAPI]
        
        
        Return a vector of all named instances of UsdPhysicsDriveAPI on the
        given ``prim`` .
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def GetDampingAttr(*args, **kwargs):
        """
        
        GetDampingAttr() -> Attribute
        
        
        Damping of the drive.
        
        
        Units: if linear drive: mass/second If angular drive:
        mass\\*DIST_UNITS\\*DIST_UNITS/second/second/degrees.
        
        Declaration
        
        ``float physics:damping = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetMaxForceAttr(*args, **kwargs):
        """
        
        GetMaxForceAttr() -> Attribute
        
        
        Maximum force that can be applied to drive.
        
        
        Units: if linear drive: mass\\*DIST_UNITS/second/second if angular
        drive: mass\\*DIST_UNITS\\*DIST_UNITS/second/second inf means not
        limited. Must be non-negative.
        
        Declaration
        
        ``float physics:maxForce = inf``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        
        ----------------------------------------------------------------------
        
        GetSchemaAttributeNames(includeInherited, instanceName) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes for a given instance name.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved. The names returned will have the
        proper namespace prefix.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        instanceName : str
        
        
        """
    @staticmethod
    def GetStiffnessAttr(*args, **kwargs):
        """
        
        GetStiffnessAttr() -> Attribute
        
        
        Stiffness of the drive.
        
        
        Units: if linear drive: mass/second/second if angular drive:
        mass\\*DIST_UNITS\\*DIST_UNITS/degree/second/second.
        
        Declaration
        
        ``float physics:stiffness = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetTargetPositionAttr(*args, **kwargs):
        """
        
        GetTargetPositionAttr() -> Attribute
        
        
        Target value for position.
        
        
        Units: if linear drive: distance if angular drive: degrees.
        
        Declaration
        
        ``float physics:targetPosition = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetTargetVelocityAttr(*args, **kwargs):
        """
        
        GetTargetVelocityAttr() -> Attribute
        
        
        Target value for velocity.
        
        
        Units: if linear drive: distance/second if angular drive:
        degrees/second.
        
        Declaration
        
        ``float physics:targetVelocity = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetTypeAttr(*args, **kwargs):
        """
        
        GetTypeAttr() -> Attribute
        
        
        Drive spring is for the acceleration at the joint (rather than the
        force).
        
        
        
        Declaration
        
        ``uniform token physics:type ="force"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        force, acceleration
        
        
        
        """
    @staticmethod
    def IsPhysicsDriveAPIPath(*args, **kwargs):
        """
        
        **classmethod** IsPhysicsDriveAPIPath(path, name) -> bool
        
        
        Checks if the given path ``path`` is of an API schema of type
        PhysicsDriveAPI.
        
        
        If so, it stores the instance name of the schema in ``name`` and
        returns true. Otherwise, it returns false.
        
        
        Parameters
        ----------
        path : Path
        
        name : str
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim, name)
        
        
        Construct a UsdPhysicsDriveAPI on UsdPrim ``prim`` with name ``name``
        .
        
        
        Equivalent to UsdPhysicsDriveAPI::Get ( prim.GetStage(),
        prim.GetPath().AppendProperty("drive:name"));
        
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj, name)
        
        
        Construct a UsdPhysicsDriveAPI on the prim held by ``schemaObj`` with
        name ``name`` .
        
        
        Should be preferred over UsdPhysicsDriveAPI (schemaObj.GetPrim(),
        name), as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        name : str
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class FilteredPairsAPI(pxr.Usd.APISchemaBase):
    """
    
    API to describe fine-grained filtering. If a collision between two
    objects occurs, this pair might be filtered if the pair is defined
    through this API. This API can be applied either to a body or
    collision or even articulation. The"filteredPairs"defines what objects
    it should not collide against. Note that FilteredPairsAPI filtering
    has precedence over CollisionGroup filtering.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> FilteredPairsAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"PhysicsFilteredPairsAPI"to the
        token-valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdPhysicsFilteredPairsAPI object is returned upon success. An
        invalid (or empty) UsdPhysicsFilteredPairsAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, whyNot) -> bool
        
        
        Returns true if this **single-apply** API schema can be applied to the
        given ``prim`` .
        
        
        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates ``whyNot`` with the reason it can not be
        applied.
        
        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        whyNot : str
        
        
        """
    @staticmethod
    def CreateFilteredPairsRel(*args, **kwargs):
        """
        
        CreateFilteredPairsRel() -> Relationship
        
        
        See GetFilteredPairsRel() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> FilteredPairsAPI
        
        
        Return a UsdPhysicsFilteredPairsAPI holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsFilteredPairsAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetFilteredPairsRel(*args, **kwargs):
        """
        
        GetFilteredPairsRel() -> Relationship
        
        
        Relationship to objects that should be filtered.
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsFilteredPairsAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsFilteredPairsAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsFilteredPairsAPI on the prim held by
        ``schemaObj`` .
        
        
        Should be preferred over UsdPhysicsFilteredPairsAPI
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class FixedJoint(Joint):
    """
    
    Predefined fixed joint type (All degrees of freedom are removed.)
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> FixedJoint
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> FixedJoint
        
        
        Return a UsdPhysicsFixedJoint holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsFixedJoint(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsFixedJoint on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsFixedJoint::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsFixedJoint on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdPhysicsFixedJoint (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Joint(pxr.UsdGeom.Imageable):
    """
    
    A joint constrains the movement of rigid bodies. Joint can be created
    between two rigid bodies or between one rigid body and world. By
    default joint primitive defines a D6 joint where all degrees of
    freedom are free. Three linear and three angular degrees of freedom.
    Note that default behavior is to disable collision between jointed
    bodies.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateBody0Rel(*args, **kwargs):
        """
        
        CreateBody0Rel() -> Relationship
        
        
        See GetBody0Rel() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateBody1Rel(*args, **kwargs):
        """
        
        CreateBody1Rel() -> Relationship
        
        
        See GetBody1Rel() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateBreakForceAttr(*args, **kwargs):
        """
        
        CreateBreakForceAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetBreakForceAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateBreakTorqueAttr(*args, **kwargs):
        """
        
        CreateBreakTorqueAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetBreakTorqueAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateCollisionEnabledAttr(*args, **kwargs):
        """
        
        CreateCollisionEnabledAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetCollisionEnabledAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateExcludeFromArticulationAttr(*args, **kwargs):
        """
        
        CreateExcludeFromArticulationAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetExcludeFromArticulationAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateJointEnabledAttr(*args, **kwargs):
        """
        
        CreateJointEnabledAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetJointEnabledAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateLocalPos0Attr(*args, **kwargs):
        """
        
        CreateLocalPos0Attr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetLocalPos0Attr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateLocalPos1Attr(*args, **kwargs):
        """
        
        CreateLocalPos1Attr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetLocalPos1Attr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateLocalRot0Attr(*args, **kwargs):
        """
        
        CreateLocalRot0Attr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetLocalRot0Attr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateLocalRot1Attr(*args, **kwargs):
        """
        
        CreateLocalRot1Attr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetLocalRot1Attr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> Joint
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> Joint
        
        
        Return a UsdPhysicsJoint holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsJoint(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetBody0Rel(*args, **kwargs):
        """
        
        GetBody0Rel() -> Relationship
        
        
        Relationship to any UsdGeomXformable.
        
        
        
        """
    @staticmethod
    def GetBody1Rel(*args, **kwargs):
        """
        
        GetBody1Rel() -> Relationship
        
        
        Relationship to any UsdGeomXformable.
        
        
        
        """
    @staticmethod
    def GetBreakForceAttr(*args, **kwargs):
        """
        
        GetBreakForceAttr() -> Attribute
        
        
        Joint break force.
        
        
        If set, joint is to break when this force limit is reached. (Used for
        linear DOFs.) Units: mass \\* distance / second / second
        
        Declaration
        
        ``float physics:breakForce = inf``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetBreakTorqueAttr(*args, **kwargs):
        """
        
        GetBreakTorqueAttr() -> Attribute
        
        
        Joint break torque.
        
        
        If set, joint is to break when this torque limit is reached. (Used for
        angular DOFs.) Units: mass \\* distance \\* distance / second / second
        
        Declaration
        
        ``float physics:breakTorque = inf``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetCollisionEnabledAttr(*args, **kwargs):
        """
        
        GetCollisionEnabledAttr() -> Attribute
        
        
        Determines if the jointed subtrees should collide or not.
        
        
        
        Declaration
        
        ``bool physics:collisionEnabled = 0``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        
        
        """
    @staticmethod
    def GetExcludeFromArticulationAttr(*args, **kwargs):
        """
        
        GetExcludeFromArticulationAttr() -> Attribute
        
        
        Determines if the joint can be included in an Articulation.
        
        
        
        Declaration
        
        ``uniform bool physics:excludeFromArticulation = 0``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetJointEnabledAttr(*args, **kwargs):
        """
        
        GetJointEnabledAttr() -> Attribute
        
        
        Determines if the joint is enabled.
        
        
        
        Declaration
        
        ``bool physics:jointEnabled = 1``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        
        
        """
    @staticmethod
    def GetLocalPos0Attr(*args, **kwargs):
        """
        
        GetLocalPos0Attr() -> Attribute
        
        
        Relative position of the joint frame to body0's frame.
        
        
        
        Declaration
        
        ``point3f physics:localPos0 = (0, 0, 0)``
        
        C++ Type
        
        GfVec3f
        
        Usd Type
        
        SdfValueTypeNames->Point3f
        
        
        
        """
    @staticmethod
    def GetLocalPos1Attr(*args, **kwargs):
        """
        
        GetLocalPos1Attr() -> Attribute
        
        
        Relative position of the joint frame to body1's frame.
        
        
        
        Declaration
        
        ``point3f physics:localPos1 = (0, 0, 0)``
        
        C++ Type
        
        GfVec3f
        
        Usd Type
        
        SdfValueTypeNames->Point3f
        
        
        
        """
    @staticmethod
    def GetLocalRot0Attr(*args, **kwargs):
        """
        
        GetLocalRot0Attr() -> Attribute
        
        
        Relative orientation of the joint frame to body0's frame.
        
        
        
        Declaration
        
        ``quatf physics:localRot0 = (1, 0, 0, 0)``
        
        C++ Type
        
        GfQuatf
        
        Usd Type
        
        SdfValueTypeNames->Quatf
        
        
        
        """
    @staticmethod
    def GetLocalRot1Attr(*args, **kwargs):
        """
        
        GetLocalRot1Attr() -> Attribute
        
        
        Relative orientation of the joint frame to body1's frame.
        
        
        
        Declaration
        
        ``quatf physics:localRot1 = (1, 0, 0, 0)``
        
        C++ Type
        
        GfQuatf
        
        Usd Type
        
        SdfValueTypeNames->Quatf
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsJoint on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsJoint::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsJoint on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdPhysicsJoint (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class LimitAPI(pxr.Usd.APISchemaBase):
    """
    
    The PhysicsLimitAPI can be applied to a PhysicsJoint and will restrict
    the movement along an axis. PhysicsLimitAPI is a multipleApply schema:
    The PhysicsJoint can be restricted
    along"transX","transY","transZ","rotX","rotY","rotZ","distance".
    Setting these as a multipleApply schema TfToken name will define the
    degree of freedom the PhysicsLimitAPI is applied to. Note that if the
    low limit is higher than the high limit, motion along this axis is
    considered locked.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim, name) -> LimitAPI
        
        
        Applies this **multiple-apply** API schema to the given ``prim`` along
        with the given instance name, ``name`` .
        
        
        This information is stored by adding"PhysicsLimitAPI:<i>name</i>"to
        the token-valued, listOp metadata *apiSchemas* on the prim. For
        example, if ``name`` is'instance1', the
        token'PhysicsLimitAPI:instance1'is added to'apiSchemas'.
        
        A valid UsdPhysicsLimitAPI object is returned upon success. An invalid
        (or empty) UsdPhysicsLimitAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, name, whyNot) -> bool
        
        
        Returns true if this **multiple-apply** API schema can be applied,
        with the given instance name, ``name`` , to the given ``prim`` .
        
        
        If this schema can not be a applied the prim, this returns false and,
        if provided, populates ``whyNot`` with the reason it can not be
        applied.
        
        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        whyNot : str
        
        
        """
    @staticmethod
    def CreateHighAttr(*args, **kwargs):
        """
        
        CreateHighAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetHighAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateLowAttr(*args, **kwargs):
        """
        
        CreateLowAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetLowAttr() , and also Create vs Get Property Methods for when to
        use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> LimitAPI
        
        
        Return a UsdPhysicsLimitAPI holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        ``path`` must be of the format<path>.limit:name.
        
        This is shorthand for the following:
        
        .. code-block:: text
        
          TfToken name = SdfPath::StripNamespace(path.GetToken());
          UsdPhysicsLimitAPI(
              stage->GetPrimAtPath(path.GetPrimPath()), name);
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        
        ----------------------------------------------------------------------
        
        Get(prim, name) -> LimitAPI
        
        
        Return a UsdPhysicsLimitAPI with name ``name`` holding the prim
        ``prim`` .
        
        
        Shorthand for UsdPhysicsLimitAPI(prim, name);
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        
        """
    @staticmethod
    def GetAll(*args, **kwargs):
        """
        
        **classmethod** GetAll(prim) -> list[LimitAPI]
        
        
        Return a vector of all named instances of UsdPhysicsLimitAPI on the
        given ``prim`` .
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def GetHighAttr(*args, **kwargs):
        """
        
        GetHighAttr() -> Attribute
        
        
        Upper limit.
        
        
        Units: degrees or distance depending on trans or rot axis applied to.
        inf means not limited in positive direction.
        
        Declaration
        
        ``float physics:high = inf``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetLowAttr(*args, **kwargs):
        """
        
        GetLowAttr() -> Attribute
        
        
        Lower limit.
        
        
        Units: degrees or distance depending on trans or rot axis applied to.
        \\-inf means not limited in negative direction.
        
        Declaration
        
        ``float physics:low = -inf``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        
        ----------------------------------------------------------------------
        
        GetSchemaAttributeNames(includeInherited, instanceName) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes for a given instance name.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved. The names returned will have the
        proper namespace prefix.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        instanceName : str
        
        
        """
    @staticmethod
    def IsPhysicsLimitAPIPath(*args, **kwargs):
        """
        
        **classmethod** IsPhysicsLimitAPIPath(path, name) -> bool
        
        
        Checks if the given path ``path`` is of an API schema of type
        PhysicsLimitAPI.
        
        
        If so, it stores the instance name of the schema in ``name`` and
        returns true. Otherwise, it returns false.
        
        
        Parameters
        ----------
        path : Path
        
        name : str
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim, name)
        
        
        Construct a UsdPhysicsLimitAPI on UsdPrim ``prim`` with name ``name``
        .
        
        
        Equivalent to UsdPhysicsLimitAPI::Get ( prim.GetStage(),
        prim.GetPath().AppendProperty("limit:name"));
        
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj, name)
        
        
        Construct a UsdPhysicsLimitAPI on the prim held by ``schemaObj`` with
        name ``name`` .
        
        
        Should be preferred over UsdPhysicsLimitAPI (schemaObj.GetPrim(),
        name), as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        name : str
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class MassAPI(pxr.Usd.APISchemaBase):
    """
    
    Defines explicit mass properties (mass, density, inertia etc.).
    MassAPI can be applied to any object that has a PhysicsCollisionAPI or
    a PhysicsRigidBodyAPI.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> MassAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"PhysicsMassAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdPhysicsMassAPI object is returned upon success. An invalid
        (or empty) UsdPhysicsMassAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, whyNot) -> bool
        
        
        Returns true if this **single-apply** API schema can be applied to the
        given ``prim`` .
        
        
        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates ``whyNot`` with the reason it can not be
        applied.
        
        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        whyNot : str
        
        
        """
    @staticmethod
    def CreateCenterOfMassAttr(*args, **kwargs):
        """
        
        CreateCenterOfMassAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetCenterOfMassAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateDensityAttr(*args, **kwargs):
        """
        
        CreateDensityAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDensityAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateDiagonalInertiaAttr(*args, **kwargs):
        """
        
        CreateDiagonalInertiaAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDiagonalInertiaAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateMassAttr(*args, **kwargs):
        """
        
        CreateMassAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetMassAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreatePrincipalAxesAttr(*args, **kwargs):
        """
        
        CreatePrincipalAxesAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetPrincipalAxesAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> MassAPI
        
        
        Return a UsdPhysicsMassAPI holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsMassAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetCenterOfMassAttr(*args, **kwargs):
        """
        
        GetCenterOfMassAttr() -> Attribute
        
        
        Center of mass in the prim's local space.
        
        
        Units: distance.
        
        Declaration
        
        ``point3f physics:centerOfMass = (-inf, -inf, -inf)``
        
        C++ Type
        
        GfVec3f
        
        Usd Type
        
        SdfValueTypeNames->Point3f
        
        
        
        """
    @staticmethod
    def GetDensityAttr(*args, **kwargs):
        """
        
        GetDensityAttr() -> Attribute
        
        
        If non-zero, specifies the density of the object.
        
        
        In the context of rigid body physics, density indirectly results in
        setting mass via (mass = density x volume of the object). How the
        volume is computed is up to implementation of the physics system. It
        is generally computed from the collision approximation rather than the
        graphical mesh. In the case where both density and mass are specified
        for the same object, mass has precedence over density. Unlike mass,
        child's prim's density overrides parent prim's density as it is
        accumulative. Note that density of a collisionAPI can be also
        alternatively set through a PhysicsMaterialAPI. The material density
        has the weakest precedence in density definition. Note if density is
        0.0 it is ignored. Units: mass/distance/distance/distance.
        
        Declaration
        
        ``float physics:density = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetDiagonalInertiaAttr(*args, **kwargs):
        """
        
        GetDiagonalInertiaAttr() -> Attribute
        
        
        If non-zero, specifies diagonalized inertia tensor along the principal
        axes.
        
        
        Note if diagonalInertial is (0.0, 0.0, 0.0) it is ignored. Units:
        mass\\*distance\\*distance.
        
        Declaration
        
        ``float3 physics:diagonalInertia = (0, 0, 0)``
        
        C++ Type
        
        GfVec3f
        
        Usd Type
        
        SdfValueTypeNames->Float3
        
        
        
        """
    @staticmethod
    def GetMassAttr(*args, **kwargs):
        """
        
        GetMassAttr() -> Attribute
        
        
        If non-zero, directly specifies the mass of the object.
        
        
        Note that any child prim can also have a mass when they apply massAPI.
        In this case, the precedence rule is'parent mass overrides the
        child's'. This may come as counter-intuitive, but mass is a computed
        quantity and in general not accumulative. For example, if a parent has
        mass of 10, and one of two children has mass of 20, allowing child's
        mass to override its parent results in a mass of -10 for the other
        child. Note if mass is 0.0 it is ignored. Units: mass.
        
        Declaration
        
        ``float physics:mass = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetPrincipalAxesAttr(*args, **kwargs):
        """
        
        GetPrincipalAxesAttr() -> Attribute
        
        
        Orientation of the inertia tensor's principal axes in the prim's local
        space.
        
        
        
        Declaration
        
        ``quatf physics:principalAxes = (0, 0, 0, 0)``
        
        C++ Type
        
        GfQuatf
        
        Usd Type
        
        SdfValueTypeNames->Quatf
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsMassAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsMassAPI::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsMassAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdPhysicsMassAPI (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class MassUnits(Boost.Python.instance):
    """
    
    Container class for static double-precision symbols representing
    common mass units of measure expressed in kilograms.
    
    """
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
    """
    
    Adds simulation material properties to a Material. All collisions that
    have a relationship to this material will have their collision
    response defined through this material.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> MaterialAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"PhysicsMaterialAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdPhysicsMaterialAPI object is returned upon success. An
        invalid (or empty) UsdPhysicsMaterialAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, whyNot) -> bool
        
        
        Returns true if this **single-apply** API schema can be applied to the
        given ``prim`` .
        
        
        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates ``whyNot`` with the reason it can not be
        applied.
        
        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        whyNot : str
        
        
        """
    @staticmethod
    def CreateDensityAttr(*args, **kwargs):
        """
        
        CreateDensityAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDensityAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateDynamicFrictionAttr(*args, **kwargs):
        """
        
        CreateDynamicFrictionAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDynamicFrictionAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateRestitutionAttr(*args, **kwargs):
        """
        
        CreateRestitutionAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetRestitutionAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateStaticFrictionAttr(*args, **kwargs):
        """
        
        CreateStaticFrictionAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetStaticFrictionAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> MaterialAPI
        
        
        Return a UsdPhysicsMaterialAPI holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsMaterialAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetDensityAttr(*args, **kwargs):
        """
        
        GetDensityAttr() -> Attribute
        
        
        If non-zero, defines the density of the material.
        
        
        This can be used for body mass computation, see PhysicsMassAPI. Note
        that if the density is 0.0 it is ignored. Units:
        mass/distance/distance/distance.
        
        Declaration
        
        ``float physics:density = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetDynamicFrictionAttr(*args, **kwargs):
        """
        
        GetDynamicFrictionAttr() -> Attribute
        
        
        Dynamic friction coefficient.
        
        
        Unitless.
        
        Declaration
        
        ``float physics:dynamicFriction = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetRestitutionAttr(*args, **kwargs):
        """
        
        GetRestitutionAttr() -> Attribute
        
        
        Restitution coefficient.
        
        
        Unitless.
        
        Declaration
        
        ``float physics:restitution = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def GetStaticFrictionAttr(*args, **kwargs):
        """
        
        GetStaticFrictionAttr() -> Attribute
        
        
        Static friction coefficient.
        
        
        Unitless.
        
        Declaration
        
        ``float physics:staticFriction = 0``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsMaterialAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsMaterialAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsMaterialAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdPhysicsMaterialAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class MeshCollisionAPI(pxr.Usd.APISchemaBase):
    """
    
    Attributes to control how a Mesh is made into a collider. Can be
    applied to only a USDGeomMesh in addition to its PhysicsCollisionAPI.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdPhysicsTokens. So to set an attribute to the value"rightHanded",
    use UsdPhysicsTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> MeshCollisionAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"PhysicsMeshCollisionAPI"to the
        token-valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdPhysicsMeshCollisionAPI object is returned upon success. An
        invalid (or empty) UsdPhysicsMeshCollisionAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, whyNot) -> bool
        
        
        Returns true if this **single-apply** API schema can be applied to the
        given ``prim`` .
        
        
        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates ``whyNot`` with the reason it can not be
        applied.
        
        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        whyNot : str
        
        
        """
    @staticmethod
    def CreateApproximationAttr(*args, **kwargs):
        """
        
        CreateApproximationAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetApproximationAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> MeshCollisionAPI
        
        
        Return a UsdPhysicsMeshCollisionAPI holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsMeshCollisionAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetApproximationAttr(*args, **kwargs):
        """
        
        GetApproximationAttr() -> Attribute
        
        
        Determines the mesh's collision approximation:"none"- The mesh
        geometry is used directly as a collider without any approximation.
        
        
        "convexDecomposition"- A convex mesh decomposition is performed. This
        results in a set of convex mesh colliders."convexHull"- A convex hull
        of the mesh is generated and used as the collider."boundingSphere"- A
        bounding sphere is computed around the mesh and used as a
        collider."boundingCube"- An optimally fitting box collider is computed
        around the mesh."meshSimplification"- A mesh simplification step is
        performed, resulting in a simplified triangle mesh collider.
        
        Declaration
        
        ``uniform token physics:approximation ="none"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        none, convexDecomposition, convexHull, boundingSphere, boundingCube,
        meshSimplification
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsMeshCollisionAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsMeshCollisionAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsMeshCollisionAPI on the prim held by
        ``schemaObj`` .
        
        
        Should be preferred over UsdPhysicsMeshCollisionAPI
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class PrismaticJoint(Joint):
    """
    
    Predefined prismatic joint type (translation along prismatic joint
    axis is permitted.)
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdPhysicsTokens. So to set an attribute to the value"rightHanded",
    use UsdPhysicsTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateAxisAttr(*args, **kwargs):
        """
        
        CreateAxisAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetAxisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateLowerLimitAttr(*args, **kwargs):
        """
        
        CreateLowerLimitAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetLowerLimitAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateUpperLimitAttr(*args, **kwargs):
        """
        
        CreateUpperLimitAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetUpperLimitAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> PrismaticJoint
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> PrismaticJoint
        
        
        Return a UsdPhysicsPrismaticJoint holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsPrismaticJoint(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetAxisAttr(*args, **kwargs):
        """
        
        GetAxisAttr() -> Attribute
        
        
        Joint axis.
        
        
        
        Declaration
        
        ``uniform token physics:axis ="X"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        X, Y, Z
        
        
        
        """
    @staticmethod
    def GetLowerLimitAttr(*args, **kwargs):
        """
        
        GetLowerLimitAttr() -> Attribute
        
        
        Lower limit.
        
        
        Units: distance. -inf means not limited in negative direction.
        
        Declaration
        
        ``float physics:lowerLimit = -inf``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def GetUpperLimitAttr(*args, **kwargs):
        """
        
        GetUpperLimitAttr() -> Attribute
        
        
        Upper limit.
        
        
        Units: distance. inf means not limited in positive direction.
        
        Declaration
        
        ``float physics:upperLimit = inf``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsPrismaticJoint on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsPrismaticJoint::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsPrismaticJoint on the prim held by ``schemaObj``
        .
        
        
        Should be preferred over UsdPhysicsPrismaticJoint
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class RevoluteJoint(Joint):
    """
    
    Predefined revolute joint type (rotation along revolute joint axis is
    permitted.)
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdPhysicsTokens. So to set an attribute to the value"rightHanded",
    use UsdPhysicsTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateAxisAttr(*args, **kwargs):
        """
        
        CreateAxisAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetAxisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateLowerLimitAttr(*args, **kwargs):
        """
        
        CreateLowerLimitAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetLowerLimitAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateUpperLimitAttr(*args, **kwargs):
        """
        
        CreateUpperLimitAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetUpperLimitAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> RevoluteJoint
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> RevoluteJoint
        
        
        Return a UsdPhysicsRevoluteJoint holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsRevoluteJoint(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetAxisAttr(*args, **kwargs):
        """
        
        GetAxisAttr() -> Attribute
        
        
        Joint axis.
        
        
        
        Declaration
        
        ``uniform token physics:axis ="X"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        X, Y, Z
        
        
        
        """
    @staticmethod
    def GetLowerLimitAttr(*args, **kwargs):
        """
        
        GetLowerLimitAttr() -> Attribute
        
        
        Lower limit.
        
        
        Units: degrees. -inf means not limited in negative direction.
        
        Declaration
        
        ``float physics:lowerLimit = -inf``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def GetUpperLimitAttr(*args, **kwargs):
        """
        
        GetUpperLimitAttr() -> Attribute
        
        
        Upper limit.
        
        
        Units: degrees. inf means not limited in positive direction.
        
        Declaration
        
        ``float physics:upperLimit = inf``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsRevoluteJoint on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsRevoluteJoint::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsRevoluteJoint on the prim held by ``schemaObj``
        .
        
        
        Should be preferred over UsdPhysicsRevoluteJoint
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class RigidBodyAPI(pxr.Usd.APISchemaBase):
    """
    
    Applies physics body attributes to any UsdGeomXformable prim and marks
    that prim to be driven by a simulation. If a simulation is running it
    will update this prim's pose. All prims in the hierarchy below this
    prim should move accordingly.
    
    """
    class MassInformation(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 96
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
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> RigidBodyAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"PhysicsRigidBodyAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdPhysicsRigidBodyAPI object is returned upon success. An
        invalid (or empty) UsdPhysicsRigidBodyAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, whyNot) -> bool
        
        
        Returns true if this **single-apply** API schema can be applied to the
        given ``prim`` .
        
        
        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates ``whyNot`` with the reason it can not be
        applied.
        
        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        whyNot : str
        
        
        """
    @staticmethod
    def ComputeMassProperties(*args, **kwargs):
        """
        
        ComputeMassProperties(diagonalInertia, com, principalAxes, massInfoFn) -> float
        
        
        Compute mass properties of the rigid body ``diagonalInertia`` Computed
        diagonal of the inertial tensor for the rigid body.
        
        
        ``com`` Computed center of mass for the rigid body. ``principalAxes``
        Inertia tensor's principal axes orienttion for the rigid body.
        ``massInfoFn`` Callback function to get collision mass information.
        
        Computed mass of the rigid body
        
        
        Parameters
        ----------
        diagonalInertia : Vec3f
        
        com : Vec3f
        
        principalAxes : Quatf
        
        massInfoFn : MassInformationFn
        
        
        """
    @staticmethod
    def CreateAngularVelocityAttr(*args, **kwargs):
        """
        
        CreateAngularVelocityAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetAngularVelocityAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateKinematicEnabledAttr(*args, **kwargs):
        """
        
        CreateKinematicEnabledAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetKinematicEnabledAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateRigidBodyEnabledAttr(*args, **kwargs):
        """
        
        CreateRigidBodyEnabledAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetRigidBodyEnabledAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateSimulationOwnerRel(*args, **kwargs):
        """
        
        CreateSimulationOwnerRel() -> Relationship
        
        
        See GetSimulationOwnerRel() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        
        """
    @staticmethod
    def CreateStartsAsleepAttr(*args, **kwargs):
        """
        
        CreateStartsAsleepAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetStartsAsleepAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateVelocityAttr(*args, **kwargs):
        """
        
        CreateVelocityAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetVelocityAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> RigidBodyAPI
        
        
        Return a UsdPhysicsRigidBodyAPI holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsRigidBodyAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetAngularVelocityAttr(*args, **kwargs):
        """
        
        GetAngularVelocityAttr() -> Attribute
        
        
        Angular velocity in the same space as the node's xform.
        
        
        Units: degrees/second.
        
        Declaration
        
        ``vector3f physics:angularVelocity = (0, 0, 0)``
        
        C++ Type
        
        GfVec3f
        
        Usd Type
        
        SdfValueTypeNames->Vector3f
        
        
        
        """
    @staticmethod
    def GetKinematicEnabledAttr(*args, **kwargs):
        """
        
        GetKinematicEnabledAttr() -> Attribute
        
        
        Determines whether the body is kinematic or not.
        
        
        A kinematic body is a body that is moved through animated poses or
        through user defined poses. The simulation derives velocities for the
        kinematic body based on the external motion. When a continuous motion
        is not desired, this kinematic flag should be set to false.
        
        Declaration
        
        ``bool physics:kinematicEnabled = 0``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        
        
        """
    @staticmethod
    def GetRigidBodyEnabledAttr(*args, **kwargs):
        """
        
        GetRigidBodyEnabledAttr() -> Attribute
        
        
        Determines if this PhysicsRigidBodyAPI is enabled.
        
        
        
        Declaration
        
        ``bool physics:rigidBodyEnabled = 1``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def GetSimulationOwnerRel(*args, **kwargs):
        """
        
        GetSimulationOwnerRel() -> Relationship
        
        
        Single PhysicsScene that will simulate this body.
        
        
        By default this is the first PhysicsScene found in the stage using
        UsdStage::Traverse() .
        
        
        
        """
    @staticmethod
    def GetStartsAsleepAttr(*args, **kwargs):
        """
        
        GetStartsAsleepAttr() -> Attribute
        
        
        Determines if the body is asleep when the simulation starts.
        
        
        
        Declaration
        
        ``uniform bool physics:startsAsleep = 0``
        
        C++ Type
        
        bool
        
        Usd Type
        
        SdfValueTypeNames->Bool
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetVelocityAttr(*args, **kwargs):
        """
        
        GetVelocityAttr() -> Attribute
        
        
        Linear velocity in the same space as the node's xform.
        
        
        Units: distance/second.
        
        Declaration
        
        ``vector3f physics:velocity = (0, 0, 0)``
        
        C++ Type
        
        GfVec3f
        
        Usd Type
        
        SdfValueTypeNames->Vector3f
        
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsRigidBodyAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsRigidBodyAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsRigidBodyAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdPhysicsRigidBodyAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Scene(pxr.Usd.Typed):
    """
    
    General physics simulation properties, required for simulation.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateGravityDirectionAttr(*args, **kwargs):
        """
        
        CreateGravityDirectionAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetGravityDirectionAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateGravityMagnitudeAttr(*args, **kwargs):
        """
        
        CreateGravityMagnitudeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetGravityMagnitudeAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> Scene
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> Scene
        
        
        Return a UsdPhysicsScene holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsScene(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetGravityDirectionAttr(*args, **kwargs):
        """
        
        GetGravityDirectionAttr() -> Attribute
        
        
        Gravity direction vector in simulation world space.
        
        
        Will be normalized before use. A zero vector is a request to use the
        negative upAxis. Unitless.
        
        Declaration
        
        ``vector3f physics:gravityDirection = (0, 0, 0)``
        
        C++ Type
        
        GfVec3f
        
        Usd Type
        
        SdfValueTypeNames->Vector3f
        
        
        
        """
    @staticmethod
    def GetGravityMagnitudeAttr(*args, **kwargs):
        """
        
        GetGravityMagnitudeAttr() -> Attribute
        
        
        Gravity acceleration magnitude in simulation world space.
        
        
        A negative value is a request to use a value equivalent to earth
        gravity regardless of the metersPerUnit scaling used by this scene.
        Units: distance/second/second.
        
        Declaration
        
        ``float physics:gravityMagnitude = -inf``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsScene on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsScene::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsScene on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdPhysicsScene (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class SphericalJoint(Joint):
    """
    
    Predefined spherical joint type (Removes linear degrees of freedom,
    cone limit may restrict the motion in a given range.) It allows two
    limit values, which when equal create a circular, else an elliptic
    cone limit around the limit axis.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdPhysicsTokens. So to set an attribute to the value"rightHanded",
    use UsdPhysicsTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateAxisAttr(*args, **kwargs):
        """
        
        CreateAxisAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetAxisAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateConeAngle0LimitAttr(*args, **kwargs):
        """
        
        CreateConeAngle0LimitAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetConeAngle0LimitAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateConeAngle1LimitAttr(*args, **kwargs):
        """
        
        CreateConeAngle1LimitAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetConeAngle1LimitAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> SphericalJoint
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> SphericalJoint
        
        
        Return a UsdPhysicsSphericalJoint holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdPhysicsSphericalJoint(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetAxisAttr(*args, **kwargs):
        """
        
        GetAxisAttr() -> Attribute
        
        
        Cone limit axis.
        
        
        
        Declaration
        
        ``uniform token physics:axis ="X"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        X, Y, Z
        
        
        
        """
    @staticmethod
    def GetConeAngle0LimitAttr(*args, **kwargs):
        """
        
        GetConeAngle0LimitAttr() -> Attribute
        
        
        Cone limit from the primary joint axis in the local0 frame toward the
        next axis.
        
        
        (Next axis of X is Y, and of Z is X.) A negative value means not
        limited. Units: degrees.
        
        Declaration
        
        ``float physics:coneAngle0Limit = -1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetConeAngle1LimitAttr(*args, **kwargs):
        """
        
        GetConeAngle1LimitAttr() -> Attribute
        
        
        Cone limit from the primary joint axis in the local0 frame toward the
        second to next axis.
        
        
        A negative value means not limited. Units: degrees.
        
        Declaration
        
        ``float physics:coneAngle1Limit = -1``
        
        C++ Type
        
        float
        
        Usd Type
        
        SdfValueTypeNames->Float
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdPhysicsSphericalJoint on UsdPrim ``prim`` .
        
        
        Equivalent to UsdPhysicsSphericalJoint::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdPhysicsSphericalJoint on the prim held by ``schemaObj``
        .
        
        
        Should be preferred over UsdPhysicsSphericalJoint
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Tokens(Boost.Python.instance):
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
__MFB_FULL_PACKAGE_NAME: str = 'usdPhysics'
