from __future__ import annotations
import pxr.Usd
import typing
__all__ = ['Backdrop', 'NodeGraphNodeAPI', 'SceneGraphPrimAPI', 'Tokens']
class Backdrop(pxr.Usd.Typed):
    """
    
    Provides a'group-box'for the purpose of node graph organization.
    
    Unlike containers, backdrops do not store the Shader nodes inside of
    them. Backdrops are an organizational tool that allows Shader nodes to
    be visually grouped together in a node-graph UI, but there is no
    direct relationship between a Shader node and a Backdrop.
    
    The guideline for a node-graph UI is that a Shader node is considered
    part of a Backdrop when the Backdrop is the smallest Backdrop a Shader
    node's bounding-box fits inside.
    
    Backdrop objects are contained inside a NodeGraph, similar to how
    Shader objects are contained inside a NodeGraph.
    
    Backdrops have no shading inputs or outputs that influence the
    rendered results of a NodeGraph. Therefore they can be safely ignored
    during import.
    
    Like Shaders and NodeGraphs, Backdrops subscribe to the
    NodeGraphNodeAPI to specify position and size.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdUITokens. So to set an attribute to the value"rightHanded", use
    UsdUITokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def CreateDescriptionAttr(*args, **kwargs):
        """
        
        CreateDescriptionAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDescriptionAttr() , and also Create vs Get Property Methods for
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
        
        **classmethod** Define(stage, path) -> Backdrop
        
        
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
        
        **classmethod** Get(stage, path) -> Backdrop
        
        
        Return a UsdUIBackdrop holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdUIBackdrop(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetDescriptionAttr(*args, **kwargs):
        """
        
        GetDescriptionAttr() -> Attribute
        
        
        The text label that is displayed on the backdrop in the node graph.
        
        
        This help-description explains what the nodes in a backdrop do.
        
        Declaration
        
        ``uniform token ui:description``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        
        
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
        
        
        Construct a UsdUIBackdrop on UsdPrim ``prim`` .
        
        
        Equivalent to UsdUIBackdrop::Get (prim.GetStage(), prim.GetPath()) for
        a *valid* ``prim`` , but will not immediately throw an error for an
        invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdUIBackdrop on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdUIBackdrop (schemaObj.GetPrim()), as it
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
class NodeGraphNodeAPI(pxr.Usd.APISchemaBase):
    """
    
    This api helps storing information about nodes in node graphs.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdUITokens. So to set an attribute to the value"rightHanded", use
    UsdUITokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> NodeGraphNodeAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"NodeGraphNodeAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdUINodeGraphNodeAPI object is returned upon success. An
        invalid (or empty) UsdUINodeGraphNodeAPI object is returned upon
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
    def CreateDisplayColorAttr(*args, **kwargs):
        """
        
        CreateDisplayColorAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDisplayColorAttr() , and also Create vs Get Property Methods
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
    def CreateExpansionStateAttr(*args, **kwargs):
        """
        
        CreateExpansionStateAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetExpansionStateAttr() , and also Create vs Get Property Methods
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
    def CreateIconAttr(*args, **kwargs):
        """
        
        CreateIconAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetIconAttr() , and also Create vs Get Property Methods for when
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
    def CreatePosAttr(*args, **kwargs):
        """
        
        CreatePosAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetPosAttr() , and also Create vs Get Property Methods for when to
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
    def CreateSizeAttr(*args, **kwargs):
        """
        
        CreateSizeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetSizeAttr() , and also Create vs Get Property Methods for when
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
    def CreateStackingOrderAttr(*args, **kwargs):
        """
        
        CreateStackingOrderAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetStackingOrderAttr() , and also Create vs Get Property Methods
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
        
        **classmethod** Get(stage, path) -> NodeGraphNodeAPI
        
        
        Return a UsdUINodeGraphNodeAPI holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdUINodeGraphNodeAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetDisplayColorAttr(*args, **kwargs):
        """
        
        GetDisplayColorAttr() -> Attribute
        
        
        This hint defines what tint the node should have in the node graph.
        
        
        
        Declaration
        
        ``uniform color3f ui:nodegraph:node:displayColor``
        
        C++ Type
        
        GfVec3f
        
        Usd Type
        
        SdfValueTypeNames->Color3f
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetExpansionStateAttr(*args, **kwargs):
        """
        
        GetExpansionStateAttr() -> Attribute
        
        
        The current expansionState of the node in the ui.
        
        
        'open'= fully expanded'closed'= fully collapsed'minimized'= should
        take the least space possible
        
        Declaration
        
        ``uniform token ui:nodegraph:node:expansionState``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        open, closed, minimized
        
        
        
        """
    @staticmethod
    def GetIconAttr(*args, **kwargs):
        """
        
        GetIconAttr() -> Attribute
        
        
        This points to an image that should be displayed on the node.
        
        
        It is intended to be useful for summary visual classification of
        nodes, rather than a thumbnail preview of the computed result of the
        node in some computational system.
        
        Declaration
        
        ``uniform asset ui:nodegraph:node:icon``
        
        C++ Type
        
        SdfAssetPath
        
        Usd Type
        
        SdfValueTypeNames->Asset
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetPosAttr(*args, **kwargs):
        """
        
        GetPosAttr() -> Attribute
        
        
        Declared relative position to the parent in a node graph.
        
        
        X is the horizontal position. Y is the vertical position. Higher
        numbers correspond to lower positions (coordinates are Qt style, not
        cartesian).
        
        These positions are not explicitly meant in pixel space, but rather
        assume that the size of a node is approximately 1.0x1.0. Where size-x
        is the node width and size-y height of the node. Depending on graph UI
        implementation, the size of a node may vary in each direction.
        
        Example: If a node's width is 300 and it is position is at 1000, we
        store for x-position: 1000 \\* (1.0/300)
        
        Declaration
        
        ``uniform float2 ui:nodegraph:node:pos``
        
        C++ Type
        
        GfVec2f
        
        Usd Type
        
        SdfValueTypeNames->Float2
        
        Variability
        
        SdfVariabilityUniform
        
        
        
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
    def GetSizeAttr(*args, **kwargs):
        """
        
        GetSizeAttr() -> Attribute
        
        
        Optional size hint for a node in a node graph.
        
        
        X is the width. Y is the height.
        
        This value is optional, because node size is often determined based on
        the number of in- and outputs of a node.
        
        Declaration
        
        ``uniform float2 ui:nodegraph:node:size``
        
        C++ Type
        
        GfVec2f
        
        Usd Type
        
        SdfValueTypeNames->Float2
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetStackingOrderAttr(*args, **kwargs):
        """
        
        GetStackingOrderAttr() -> Attribute
        
        
        This optional value is a useful hint when an application cares about
        the visibility of a node and whether each node overlaps another.
        
        
        Nodes with lower stacking order values are meant to be drawn below
        higher ones. Negative values are meant as background. Positive values
        are meant as foreground. Undefined values should be treated as 0.
        
        There are no set limits in these values.
        
        Declaration
        
        ``uniform int ui:nodegraph:node:stackingOrder``
        
        C++ Type
        
        int
        
        Usd Type
        
        SdfValueTypeNames->Int
        
        Variability
        
        SdfVariabilityUniform
        
        
        
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
        
        
        Construct a UsdUINodeGraphNodeAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdUINodeGraphNodeAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdUINodeGraphNodeAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdUINodeGraphNodeAPI (schemaObj.GetPrim()),
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
class SceneGraphPrimAPI(pxr.Usd.APISchemaBase):
    """
    
    Utility schema for display properties of a prim
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdUITokens. So to set an attribute to the value"rightHanded", use
    UsdUITokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> SceneGraphPrimAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"SceneGraphPrimAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdUISceneGraphPrimAPI object is returned upon success. An
        invalid (or empty) UsdUISceneGraphPrimAPI object is returned upon
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
    def CreateDisplayGroupAttr(*args, **kwargs):
        """
        
        CreateDisplayGroupAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDisplayGroupAttr() , and also Create vs Get Property Methods
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
    def CreateDisplayNameAttr(*args, **kwargs):
        """
        
        CreateDisplayNameAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDisplayNameAttr() , and also Create vs Get Property Methods for
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
        
        **classmethod** Get(stage, path) -> SceneGraphPrimAPI
        
        
        Return a UsdUISceneGraphPrimAPI holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdUISceneGraphPrimAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetDisplayGroupAttr(*args, **kwargs):
        """
        
        GetDisplayGroupAttr() -> Attribute
        
        
        When publishing a nodegraph or a material, it can be useful to provide
        an optional display group, for organizational purposes and
        readability.
        
        
        This is because often the usd shading hierarchy is rather flat while
        we want to display it in organized groups.
        
        Declaration
        
        ``uniform token ui:displayGroup``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetDisplayNameAttr(*args, **kwargs):
        """
        
        GetDisplayNameAttr() -> Attribute
        
        
        When publishing a nodegraph or a material, it can be useful to provide
        an optional display name, for readability.
        
        
        
        Declaration
        
        ``uniform token ui:displayName``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        
        
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
        
        
        Construct a UsdUISceneGraphPrimAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdUISceneGraphPrimAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdUISceneGraphPrimAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdUISceneGraphPrimAPI (schemaObj.GetPrim()),
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
class Tokens(Boost.Python.instance):
    closed: typing.ClassVar[str] = 'closed'
    minimized: typing.ClassVar[str] = 'minimized'
    open: typing.ClassVar[str] = 'open'
    uiDescription: typing.ClassVar[str] = 'ui:description'
    uiDisplayGroup: typing.ClassVar[str] = 'ui:displayGroup'
    uiDisplayName: typing.ClassVar[str] = 'ui:displayName'
    uiNodegraphNodeDisplayColor: typing.ClassVar[str] = 'ui:nodegraph:node:displayColor'
    uiNodegraphNodeExpansionState: typing.ClassVar[str] = 'ui:nodegraph:node:expansionState'
    uiNodegraphNodeIcon: typing.ClassVar[str] = 'ui:nodegraph:node:icon'
    uiNodegraphNodePos: typing.ClassVar[str] = 'ui:nodegraph:node:pos'
    uiNodegraphNodeSize: typing.ClassVar[str] = 'ui:nodegraph:node:size'
    uiNodegraphNodeStackingOrder: typing.ClassVar[str] = 'ui:nodegraph:node:stackingOrder'
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
__MFB_FULL_PACKAGE_NAME: str = 'usdUI'
