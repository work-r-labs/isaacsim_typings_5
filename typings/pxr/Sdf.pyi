from __future__ import annotations
import pxr.Tf
import typing
__all__ = ['AngularUnit', 'AngularUnitDegrees', 'AngularUnitRadians', 'AssetPath', 'AssetPathArray', 'AttributeSpec', 'AuthoringError', 'AuthoringErrorUnrecognizedFields', 'AuthoringErrorUnrecognizedSpecType', 'BatchNamespaceEdit', 'ChangeBlock', 'ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate', 'ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec___', 'ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec___', 'ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec___', 'ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate', 'ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec___', 'ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec___', 'CleanupEnabler', 'DimensionlessUnit', 'DimensionlessUnitDefault', 'DimensionlessUnitPercent', 'FastUpdateList', 'FileFormat', 'Find', 'Int64ListOp', 'IntListOp', 'Layer', 'LayerOffset', 'LayerTree', 'LengthUnit', 'LengthUnitCentimeter', 'LengthUnitDecimeter', 'LengthUnitFoot', 'LengthUnitInch', 'LengthUnitKilometer', 'LengthUnitMeter', 'LengthUnitMile', 'LengthUnitMillimeter', 'LengthUnitYard', 'ListEditorProxy_SdfNameKeyPolicy', 'ListEditorProxy_SdfPathKeyPolicy', 'ListEditorProxy_SdfPayloadTypePolicy', 'ListEditorProxy_SdfReferenceTypePolicy', 'ListOpType', 'ListOpTypeAdded', 'ListOpTypeAppended', 'ListOpTypeDeleted', 'ListOpTypeExplicit', 'ListOpTypeOrdered', 'ListOpTypePrepended', 'ListProxy_SdfNameKeyPolicy', 'ListProxy_SdfNameTokenKeyPolicy', 'ListProxy_SdfPathKeyPolicy', 'ListProxy_SdfPayloadTypePolicy', 'ListProxy_SdfReferenceTypePolicy', 'ListProxy_SdfSubLayerTypePolicy', 'MapEditProxy_VtDictionary', 'MapEditProxy_map_SdfPath__SdfPath__less_SdfPath___allocator_pair_SdfPath_const__SdfPath_____', 'MapEditProxy_map_string__string__less_string___allocator_pair_stringconst__string_____', 'NamespaceEdit', 'NamespaceEditDetail', 'Notice', 'Path', 'PathArray', 'PathListOp', 'Payload', 'PayloadListOp', 'Permission', 'PermissionPrivate', 'PermissionPublic', 'PrimSpec', 'PropertySpec', 'PseudoRootSpec', 'Reference', 'ReferenceListOp', 'RelationshipSpec', 'Spec', 'SpecType', 'SpecTypeAttribute', 'SpecTypeConnection', 'SpecTypeExpression', 'SpecTypeMapper', 'SpecTypeMapperArg', 'SpecTypePrim', 'SpecTypePseudoRoot', 'SpecTypeRelationship', 'SpecTypeRelationshipTarget', 'SpecTypeUnknown', 'SpecTypeVariant', 'SpecTypeVariantSet', 'Specifier', 'SpecifierClass', 'SpecifierDef', 'SpecifierOver', 'StringListOp', 'TimeCode', 'TimeCodeArray', 'TokenListOp', 'UInt64ListOp', 'UIntListOp', 'UnregisteredValue', 'UnregisteredValueListOp', 'ValueBlock', 'ValueRoleNames', 'ValueTypeName', 'ValueTypeNames', 'Variability', 'VariabilityUniform', 'VariabilityVarying', 'VariantSetSpec', 'VariantSpec']
class AngularUnit(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Sdf.AngularUnitDegrees, Sdf.AngularUnitRadians)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class AssetPath(Boost.Python.instance):
    """
    
    Contains an asset path and an optional resolved path. Asset paths may
    contain non-control UTF-8 encoded characters. Specifically,
    U+0000\\.\\.U+001F (C0 controls), U+007F (delete), and
    U+0080\\.\\.U+009F (C1 controls) are disallowed. Attempts to construct
    asset paths with such characters will issue a TfError and produce the
    default-constructed empty asset path.
    
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct an empty asset path.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(path)
        
        
        Construct an asset path with ``path`` and no associated resolved path.
        
        
        If the passed ``path`` is not valid UTF-8 or contains C0 or C1 control
        characters, raise a TfError and return the default-constructed empty
        asset path.
        
        
        Parameters
        ----------
        path : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__(path, resolvedPath)
        
        
        Construct an asset path with ``path`` and an associated
        ``resolvedPath`` .
        
        
        If either the passed \\path or ``resolvedPath`` are not valid UTF-8 or
        either contain C0 or C1 control characters, raise a TfError and return
        the default-constructed empty asset path.
        
        
        Parameters
        ----------
        path : str
        
        resolvedPath : str
        
        
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def path(*args, **kwargs):
        ...
    @property
    def resolvedPath(*args, **kwargs):
        """
        type : str
        
        
        Return the resolved asset path, if any.
        
        
        Note that SdfAssetPath carries a resolved path only if its creator
        passed one to the constructor. SdfAssetPath never performs resolution
        itself.
        
        
        ----------------------------------------------------------------------
        
        type : str
        
        
        Overload for rvalues, move out the asset path.
        """
class AssetPathArray(Boost.Python.instance):
    """
    An array of type SdfAssetPath.
    """
    _isVtArray: typing.ClassVar[bool] = True
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        
        __init__(values)
        
        values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)
        
        
        
        __init__(values)
        
        values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)
        
        
        
        __init__(values)
        
        values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)
        
        """
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
class AttributeSpec(PropertySpec):
    """
    
    A subclass of SdfPropertySpec that holds typed data.
    
    Attributes are typed data containers that can optionally hold any and
    all of the following:
    
       - A single default value.
    
       - An array of knot values describing how the value varies over
         time.
    
       - A dictionary of posed values, indexed by name.
         The values contained in an attribute must all be of the same type. In
         the Python API the ``typeName`` property holds the attribute type. In
         the C++ API, you can get the attribute type using the GetTypeName()
         method. In addition, all values, including all knot values, must be
         the same shape. For information on shapes, see the VtShape class
         reference in the C++ documentation.
    
    """
    ConnectionPathsKey: typing.ClassVar[str] = 'connectionPaths'
    DefaultValueKey: typing.ClassVar[str] = 'default'
    DisplayUnitKey: typing.ClassVar[str] = 'displayUnit'
    @staticmethod
    def ClearColorSpace(*args, **kwargs):
        """
        
        ClearColorSpace() -> None
        
        
        Clears the colorSpace metadata value set on this attribute.
        
        
        
        """
    @staticmethod
    def HasColorSpace(*args, **kwargs):
        """
        
        HasColorSpace() -> bool
        
        
        Returns true if this attribute has a colorSpace value authored.
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __new__(*args, **kwargs):
        """
        
        
        __init__(ownerPrimSpec, name, typeName, variability = Sd.VariabilityVarying, declaresCustom = False)
        ownerPrimSpec : PrimSpec
        name : string
        typeName : SdfValueTypeName
        variability : SdfVariability
        declaresCustom : bool
        
        Create a custom attribute spec that is an attribute of ownerPrimSpec with the given name and type.
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def allowedTokens(*args, **kwargs):
        """
        The allowed value tokens for this property
        """
    @allowedTokens.setter
    def allowedTokens(*args, **kwargs):
        ...
    @property
    def colorSpace(*args, **kwargs):
        """
        The color-space in which the attribute value is authored.
        """
    @colorSpace.setter
    def colorSpace(*args, **kwargs):
        ...
    @property
    def connectionPathList(*args, **kwargs):
        """
        A PathListEditor for the attribute's connection paths.
        
        The list of the connection paths for this attribute may be modified with this PathListEditor.
        
        A PathListEditor may express a list either as an explicit value or as a set of list editing operations.  See GdListEditor for more information.
        """
    @property
    def displayUnit(*args, **kwargs):
        """
        The display unit for this attribute.
        """
    @displayUnit.setter
    def displayUnit(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
    @property
    def roleName(*args, **kwargs):
        """
        The roleName for this attribute's typeName.
        """
    @property
    def typeName(*args, **kwargs):
        """
        The typename of this attribute.
        """
    @property
    def valueType(*args, **kwargs):
        """
        The value type of this attribute.
        """
class AuthoringError(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Sdf.AuthoringErrorUnrecognizedFields, Sdf.AuthoringErrorUnrecognizedSpecType)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class BatchNamespaceEdit(Boost.Python.instance):
    """
    
    A description of an arbitrarily complex namespace edit.
    
    A ``SdfBatchNamespaceEdit`` object describes zero or more namespace
    edits. Various types providing a namespace will allow the edits to be
    applied in a single operation and also allow testing if this will
    work.
    
    Clients are encouraged to group several edits into one object because
    that may allow more efficient processing of the edits. If, for
    example, you need to reparent several prims it may be faster to add
    all of the reparents to a single ``SdfBatchNamespaceEdit`` and apply
    them at once than to apply each separately.
    
    Objects that allow applying edits are free to apply the edits in any
    way and any order they see fit but they should guarantee that the
    resulting namespace will be as if each edit was applied one at a time
    in the order they were added.
    
    Note that the above rule permits skipping edits that have no effect or
    generate a non-final state. For example, if renaming A to B then to C
    we could just rename A to C. This means notices may be elided.
    However, implementations must not elide notices that contain
    information about any edit that clients must be able to know but
    otherwise cannot determine.
    
    """
    @staticmethod
    def Add(*args, **kwargs):
        """
        
        Add(edit) -> None
        
        
        Add a namespace edit.
        
        
        Parameters
        ----------
        edit : NamespaceEdit
        
        
        
        ----------------------------------------------------------------------
        
        Add(currentPath, newPath, index) -> None
        
        
        Add a namespace edit.
        
        
        Parameters
        ----------
        currentPath : NamespaceEdit.Path
        
        newPath : NamespaceEdit.Path
        
        index : NamespaceEdit.Index
        
        
        """
    @staticmethod
    def Process(*args, **kwargs):
        """
        
        Process(processedEdits, hasObjectAtPath, canEdit, details, fixBackpointers) -> bool
        
        
        Validate the edits and generate a possibly more efficient edit
        sequence.
        
        
        Edits are treated as if they were performed one at time in sequence,
        therefore each edit occurs in the namespace resulting from all
        previous edits.
        
        Editing the descendants of the object in each edit is implied. If an
        object is removed then the new path will be empty. If an object is
        removed after being otherwise edited, the other edits will be
        processed and included in ``processedEdits`` followed by the removal.
        This allows clients to fixup references to point to the object's final
        location prior to removal.
        
        This function needs help to determine if edits are allowed. The
        callbacks provide that help. ``hasObjectAtPath`` returns ``true`` iff
        there's an object at the given path. This path will be in the original
        namespace not any intermediate or final namespace. ``canEdit`` returns
        ``true`` iff the object at the current path can be namespace edited to
        the new path, ignoring whether an object already exists at the new
        path. Both paths are in the original namespace. If it returns
        ``false`` it should set the string to the reason why the edit isn't
        allowed. It should not write either path to the string.
        
        If ``hasObjectAtPath`` is invalid then this assumes objects exist
        where they should and don't exist where they shouldn't. Use this with
        care. If ``canEdit`` in invalid then it's assumed all edits are valid.
        
        If ``fixBackpointers`` is ``true`` then target/connection paths are
        expected to be in the intermediate namespace resulting from all
        previous edits. If ``false`` and any current or new path contains a
        target or connection path that has been edited then this will generate
        an error.
        
        This method returns ``true`` if the edits are allowed and sets
        ``processedEdits`` to a new edit sequence at least as efficient as the
        input sequence. If not allowed it returns ``false`` and appends
        reasons why not to ``details`` .
        
        
        Parameters
        ----------
        processedEdits : list[NamespaceEdit]
        
        hasObjectAtPath : HasObjectAtPath
        
        canEdit : CanEdit
        
        details : list[NamespaceEditDetail]
        
        fixBackpointers : bool
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Create an empty sequence of edits.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : BatchNamespaceEdit
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : list[NamespaceEdit]
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def edits(*args, **kwargs):
        """
        type : list[NamespaceEdit]
        
        
        Returns the edits.
        """
class ChangeBlock(Boost.Python.instance):
    """
    
    **DANGER DANGER DANGER**
    
    Please make sure you have read and fully understand the issues below
    before using a changeblock! They are very easy to use in an unsafe way
    that could make the system crash or corrupt data. If you have any
    questions, please contact the USD team, who would be happy to help!
    
    SdfChangeBlock provides a way to group a round of related changes to
    scene description in order to process them more efficiently.
    
    Normally, Sdf sends notification immediately as changes are made so
    that downstream representations like UsdStage can update accordingly.
    
    However, sometimes it can be advantageous to group a series of Sdf
    changes into a batch so that they can be processed more efficiently,
    with a single round of change processing. An example might be when
    setting many avar values on a model at the same time.
    
    Opening a changeblock tells Sdf to delay sending notification about
    changes until the outermost changeblock is exited. Until then, Sdf
    internally queues up the notification it needs to send.
    
    It is *not* safe to use Usd or other downstream API while a
    changeblock is open!! This is because those derived representations
    will not have had a chance to update while the changeblock is open.
    Not only will their view of the world be stale, it could be unsafe to
    even make queries from, since they may be holding onto expired handles
    to Sdf objects that no longer exist. If you need to make a bunch of
    changes to scene description, the best approach is to build a list of
    necessary changes that can be performed directly via the Sdf API, then
    submit those all inside a changeblock without talking to any
    downstream modules. For example, this is how many mutators in Usd
    that operate on more than one field or Spec work.
    
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate(Boost.Python.instance):
    class ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate_Iterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate_KeyIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate_ValueIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def get(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
class ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec___(Boost.Python.instance):
    class ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec____Iterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec____KeyIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec____ValueIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def get(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
class ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec___(Boost.Python.instance):
    class ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec____Iterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec____KeyIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec____ValueIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def get(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
class ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec___(Boost.Python.instance):
    class ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec____Iterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec____KeyIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec____ValueIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def get(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
class ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate(Boost.Python.instance):
    class ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate_Iterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate_KeyIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate_ValueIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def get(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
class ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec___(Boost.Python.instance):
    class ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec____Iterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec____KeyIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec____ValueIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def get(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
class ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec___(Boost.Python.instance):
    class ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec____Iterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec____KeyIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec____ValueIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def get(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
class CleanupEnabler(Boost.Python.instance):
    """
    
    An RAII class which, when an instance is alive, enables scheduling of
    automatic cleanup of SdfLayers.
    
    Any affected specs which no longer contribute to the scene will be
    removed when the last SdfCleanupEnabler instance goes out of scope.
    Note that for this purpose, SdfPropertySpecs are removed if they have
    only required fields (see SdfPropertySpecs::HasOnlyRequiredFields),
    but only if the property spec itself was affected by an edit that left
    it with only required fields. This will have the effect of
    uninstantiating on-demand attributes. For example, if its parent prim
    was affected by an edit that left it otherwise inert, it will not be
    removed if it contains an SdfPropertySpec with only required fields,
    but if the property spec itself is edited leaving it with only
    required fields, it will be removed, potentially uninstantiating it if
    it's an on-demand property.
    
    SdfCleanupEnablers are accessible in both C++ and Python.
    
    /// SdfCleanupEnabler can be used in the following manner:
    
    .. code-block:: text
    
      {
          SdfCleanupEnabler enabler;
          
          // Perform any action that might otherwise leave inert specs around, 
          // such as removing info from properties or prims, or removing name 
          // children. i.e:
          primSpec->ClearInfo(SdfFieldKeys->Default);
      
          // When enabler goes out of scope on the next line, primSpec will 
          // be removed if it has been left as an empty over.
      }
    
    
    """
    __instance_size__: typing.ClassVar[int] = 24
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class DimensionlessUnit(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Sdf.DimensionlessUnitPercent, Sdf.DimensionlessUnitDefault)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class FastUpdateList(Boost.Python.instance):
    """
    """
    class FastUpdate(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @property
        def path(*args, **kwargs):
            ...
        @property
        def value(*args, **kwargs):
            ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def fastUpdates(*args, **kwargs):
        ...
    @property
    def hasCompositionDependents(*args, **kwargs):
        ...
class FileFormat(Boost.Python.instance):
    """
    
    Base class for file format implementations.
    
    """
    class Tokens(Boost.Python.instance):
        TargetArg: typing.ClassVar[str] = 'target'
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
    def CanRead(*args, **kwargs):
        """
        
        CanRead(file) -> bool
        
        
        Returns true if ``file`` can be read by this format.
        
        
        Parameters
        ----------
        file : str
        
        
        """
    @staticmethod
    def FindAllFileFormatExtensions(*args, **kwargs):
        """
        
        **classmethod** FindAllFileFormatExtensions() -> set[str]
        
        
        Returns a set containing the extension(s) corresponding to all
        registered file formats.
        
        
        
        """
    @staticmethod
    def FindByExtension(*args, **kwargs):
        """
        
        **classmethod** FindByExtension(path, target) -> FileFormat
        
        
        Returns the file format instance that supports the extension for
        ``path`` .
        
        
        If a format with a matching extension is not found, this returns a
        null file format pointer.
        
        An extension may be handled by multiple file formats, but each with a
        different target. In such cases, if no ``target`` is specified, the
        file format that is registered as the primary plugin will be returned.
        Otherwise, the file format whose target matches ``target`` will be
        returned.
        
        
        Parameters
        ----------
        path : str
        
        target : str
        
        
        
        ----------------------------------------------------------------------
        
        FindByExtension(path, args) -> FileFormat
        
        
        Returns a file format instance that supports the extension for
        ``path`` and whose target matches one of those specified by the given
        ``args`` .
        
        
        If the ``args`` specify no target, then the file format that is
        registered as the primary plugin will be returned. If a format with a
        matching extension is not found, this returns a null file format
        pointer.
        
        
        Parameters
        ----------
        path : str
        
        args : FileFormatArguments
        
        
        """
    @staticmethod
    def FindById(*args, **kwargs):
        """
        
        **classmethod** FindById(formatId) -> FileFormat
        
        
        Returns the file format instance with the specified ``formatId``
        identifier.
        
        
        If a format with a matching identifier is not found, this returns a
        null file format pointer.
        
        
        Parameters
        ----------
        formatId : str
        
        
        """
    @staticmethod
    def GetFileExtension(*args, **kwargs):
        """
        
        **classmethod** GetFileExtension(s) -> str
        
        
        Returns the file extension for path or file name ``s`` , without the
        leading dot character.
        
        
        Parameters
        ----------
        s : str
        
        
        """
    @staticmethod
    def GetFileExtensions(*args, **kwargs):
        """
        
        GetFileExtensions() -> list[str]
        
        
        Returns a list of extensions that this format supports.
        
        
        
        """
    @staticmethod
    def IsPackage(*args, **kwargs):
        """
        
        IsPackage() -> bool
        
        
        Returns true if this file format is a package containing other assets.
        
        
        
        """
    @staticmethod
    def IsSupportedExtension(*args, **kwargs):
        """
        
        IsSupportedExtension(extension) -> bool
        
        
        Returns true if ``extension`` matches one of the extensions returned
        by GetFileExtensions.
        
        
        Parameters
        ----------
        extension : str
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        
        
        True if this object has not expired.  False otherwise.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        """
        
        
        Equality operator:  x == y
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __lt__(*args, **kwargs):
        """
        
        
        Less than operator: x < y
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        """
        
        
        Non-equality operator: x != y
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
    @property
    def fileCookie(*args, **kwargs):
        """
        type : str
        
        
        Returns the cookie to be used when writing files with this format.
        """
    @property
    def formatId(*args, **kwargs):
        """
        type : str
        
        
        Returns the format identifier.
        """
    @property
    def primaryFileExtension(*args, **kwargs):
        """
        type : str
        
        
        Returns the primary file extension for this format.
        
        
        This is the extension that is reported for layers using this file
        format.
        """
    @property
    def target(*args, **kwargs):
        """
        type : str
        
        
        Returns the target for this file format.
        """
class Int64ListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 168
    @staticmethod
    def ApplyOperations(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def Create(*args, **kwargs):
        ...
    @staticmethod
    def CreateExplicit(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class IntListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 168
    @staticmethod
    def ApplyOperations(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def Create(*args, **kwargs):
        ...
    @staticmethod
    def CreateExplicit(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class Layer(Boost.Python.instance):
    """
    
    A scene description container that can combine with other such
    containers to form simple component assets, and successively larger
    aggregates. The contents of an SdfLayer adhere to the SdfData data
    model. A layer can be ephemeral, or be an asset accessed and
    serialized through the ArAsset and ArResolver interfaces.
    
    The SdfLayer class provides a consistent API for accesing and
    serializing scene description, using any data store provided by Ar
    plugins. Sdf itself provides a UTF-8 text format for layers identified
    by the".sdf"identifier extension, but via the SdfFileFormat
    abstraction, allows downstream modules and plugins to adapt arbitrary
    data formats to the SdfData/SdfLayer model.
    
    The FindOrOpen() method returns a new SdfLayer object with scene
    description from any supported asset format. Once read, a layer
    remembers which asset it was read from. The Save() method saves the
    layer back out to the original asset. You can use the Export() method
    to write the layer to a different location. You can use the
    GetIdentifier() method to get the layer's Id or GetRealPath() to get
    the resolved, full URI.
    
    Layers can have a timeCode range (startTimeCode and endTimeCode). This
    range represents the suggested playback range, but has no impact on
    the extent of the animation data that may be stored in the layer. The
    metadatum"timeCodesPerSecond"is used to annotate how the time ordinate
    for samples contained in the file scales to seconds. For example, if
    timeCodesPerSecond is 24, then a sample at time ordinate 24 should be
    viewed exactly one second after the sample at time ordinate 0.
    
    """
    class DetachedLayerRules(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 72
        @staticmethod
        def Exclude(*args, **kwargs):
            ...
        @staticmethod
        def GetExcluded(*args, **kwargs):
            ...
        @staticmethod
        def GetIncluded(*args, **kwargs):
            ...
        @staticmethod
        def Include(*args, **kwargs):
            ...
        @staticmethod
        def IncludeAll(*args, **kwargs):
            ...
        @staticmethod
        def IncludedAll(*args, **kwargs):
            ...
        @staticmethod
        def IsIncluded(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    ColorConfigurationKey: typing.ClassVar[str] = 'colorConfiguration'
    ColorManagementSystemKey: typing.ClassVar[str] = 'colorManagementSystem'
    CommentKey: typing.ClassVar[str] = 'comment'
    DocumentationKey: typing.ClassVar[str] = 'documentation'
    EndFrameKey: typing.ClassVar[str] = 'endFrame'
    EndTimeCodeKey: typing.ClassVar[str] = 'endTimeCode'
    FramePrecisionKey: typing.ClassVar[str] = 'framePrecision'
    FramesPerSecondKey: typing.ClassVar[str] = 'framesPerSecond'
    HasOwnedSubLayers: typing.ClassVar[str] = 'hasOwnedSubLayers'
    OwnerKey: typing.ClassVar[str] = 'owner'
    SessionOwnerKey: typing.ClassVar[str] = 'sessionOwner'
    StartFrameKey: typing.ClassVar[str] = 'startFrame'
    StartTimeCodeKey: typing.ClassVar[str] = 'startTimeCode'
    TimeCodesPerSecondKey: typing.ClassVar[str] = 'timeCodesPerSecond'
    @staticmethod
    def AddToMutedLayers(*args, **kwargs):
        """
        
        **classmethod** AddToMutedLayers(mutedPath) -> None
        
        
        Add the specified path to the muted layers set.
        
        
        Parameters
        ----------
        mutedPath : str
        
        
        """
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        Apply(arg1) -> bool
        
        
        Performs a batch of namespace edits.
        
        
        Returns ``true`` on success and ``false`` on failure. On failure, no
        namespace edits will have occurred.
        
        
        Parameters
        ----------
        arg1 : BatchNamespaceEdit
        
        
        """
    @staticmethod
    def ApplyRootPrimOrder(*args, **kwargs):
        """
        
        ApplyRootPrimOrder(vec) -> None
        
        
        Reorders the given list of prim names according to the reorder
        rootPrims statement for this layer.
        
        
        This routine employs the standard list editing operations for ordered
        items in a ListEditor.
        
        
        Parameters
        ----------
        vec : list[str]
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        CanApply(arg1, details) -> NamespaceEditDetail.Result
        
        
        Check if a batch of namespace edits will succeed.
        
        
        This returns ``SdfNamespaceEditDetail::Okay`` if they will succeed as
        a batch, ``SdfNamespaceEditDetail::Unbatched`` if the edits will
        succeed but will be applied unbatched, and
        ``SdfNamespaceEditDetail::Error`` if they will not succeed. No edits
        will be performed in any case.
        
        If ``details`` is not ``None`` and the method does not return ``Okay``
        then details about the problems will be appended to ``details`` . A
        problem may cause the method to return early, so ``details`` may not
        list every problem.
        
        Note that Sdf does not track backpointers so it's unable to fix up
        targets/connections to namespace edited objects. Clients must fix
        those to prevent them from falling off. In addition, this method will
        report failure if any relational attribute with a target to a
        namespace edited object is subsequently edited (in the same batch).
        Clients should perform edits on relational attributes first.
        
        Clients may wish to report unbatch details to the user to confirm that
        the edits should be applied unbatched. This will give the user a
        chance to correct any problems that cause batching to fail and try
        again.
        
        
        Parameters
        ----------
        arg1 : BatchNamespaceEdit
        
        details : list[NamespaceEditDetail]
        
        
        """
    @staticmethod
    def Clear(*args, **kwargs):
        """
        
        Clear() -> None
        
        
        Clears the layer of all content.
        
        
        This restores the layer to a state as if it had just been created with
        CreateNew() . This operation is Undo-able.
        
        The fileName and whether journaling is enabled are not affected by
        this method.
        
        
        
        """
    @staticmethod
    def ClearColorConfiguration(*args, **kwargs):
        """
        
        ClearColorConfiguration() -> None
        
        
        Clears the color configuration metadata authored in this layer.
        
        
        
        HasColorConfiguration() , SetColorConfiguration()
        
        
        
        """
    @staticmethod
    def ClearColorManagementSystem(*args, **kwargs):
        """
        
        ClearColorManagementSystem() -> None
        
        
        Clears the'colorManagementSystem'metadata authored in this layer.
        
        
        
        HascolorManagementSystem(), SetColorManagementSystem()
        
        
        
        """
    @staticmethod
    def ClearCustomLayerData(*args, **kwargs):
        """
        
        ClearCustomLayerData() -> None
        
        
        Clears out the CustomLayerData dictionary associated with this layer.
        
        
        
        """
    @staticmethod
    def ClearDefaultPrim(*args, **kwargs):
        """
        
        ClearDefaultPrim() -> None
        
        
        Clear the default prim metadata for this layer.
        
        
        See GetDefaultPrim() and SetDefaultPrim() .
        
        
        
        """
    @staticmethod
    def ClearEndTimeCode(*args, **kwargs):
        """
        
        ClearEndTimeCode() -> None
        
        
        Clear the endTimeCode opinion.
        
        
        
        """
    @staticmethod
    def ClearFramePrecision(*args, **kwargs):
        """
        
        ClearFramePrecision() -> None
        
        
        Clear the framePrecision opinion.
        
        
        
        """
    @staticmethod
    def ClearFramesPerSecond(*args, **kwargs):
        """
        
        ClearFramesPerSecond() -> None
        
        
        Clear the framesPerSecond opinion.
        
        
        
        """
    @staticmethod
    def ClearOwner(*args, **kwargs):
        """
        
        ClearOwner() -> None
        
        
        Clear the owner opinion.
        
        
        
        """
    @staticmethod
    def ClearSessionOwner(*args, **kwargs):
        """
        
        ClearSessionOwner() -> None
        
        
        
        """
    @staticmethod
    def ClearStartTimeCode(*args, **kwargs):
        """
        
        ClearStartTimeCode() -> None
        
        
        Clear the startTimeCode opinion.
        
        
        
        """
    @staticmethod
    def ClearTimeCodesPerSecond(*args, **kwargs):
        """
        
        ClearTimeCodesPerSecond() -> None
        
        
        Clear the timeCodesPerSecond opinion.
        
        
        
        """
    @staticmethod
    def ComputeAbsolutePath(*args, **kwargs):
        """
        
        ComputeAbsolutePath(assetPath) -> str
        
        
        Returns the path to the asset specified by ``assetPath`` using this
        layer to anchor the path if necessary.
        
        
        Returns ``assetPath`` if it's empty or an anonymous layer identifier.
        
        This method can be used on asset paths that are authored in this layer
        to create new asset paths that can be copied to other layers. These
        new asset paths should refer to the same assets as the original asset
        paths. For example, if the underlying ArResolver is filesystem-based
        and ``assetPath`` is a relative filesystem path, this method might
        return the absolute filesystem path using this layer's location as the
        anchor.
        
        The returned path should in general not be assumed to be an absolute
        filesystem path or any other specific form. It is"absolute"in that it
        should resolve to the same asset regardless of what layer it's
        authored in.
        
        
        Parameters
        ----------
        assetPath : str
        
        
        """
    @staticmethod
    def CreateAnonymous(*args, **kwargs):
        """
        
        **classmethod** CreateAnonymous(tag, args) -> Layer
        
        
        Creates a new *anonymous* layer with an optional ``tag`` .
        
        
        An anonymous layer is a layer with a system assigned identifier, that
        cannot be saved to disk via Save() . Anonymous layers have an
        identifier, but no real path or other asset information fields.
        
        Anonymous layers may be tagged, which can be done to aid debugging
        subsystems that make use of anonymous layers. The tag becomes the
        display name of an anonymous layer, and is also included in the
        generated identifier. Untagged anonymous layers have an empty display
        name.
        
        Additional arguments may be supplied via the ``args`` parameter. These
        arguments may control behavior specific to the layer's file format.
        
        
        Parameters
        ----------
        tag : str
        
        args : FileFormatArguments
        
        
        
        ----------------------------------------------------------------------
        
        CreateAnonymous(tag, format, args) -> Layer
        
        
        Create an anonymous layer with a specific ``format`` .
        
        
        Parameters
        ----------
        tag : str
        
        format : FileFormat
        
        args : FileFormatArguments
        
        
        """
    @staticmethod
    def CreateIdentifier(*args, **kwargs):
        """
        
        **classmethod** CreateIdentifier(layerPath, arguments) -> str
        
        
        Joins the given layer path and arguments into an identifier.
        
        
        Parameters
        ----------
        layerPath : str
        
        arguments : FileFormatArguments
        
        
        """
    @staticmethod
    def CreateNew(*args, **kwargs):
        """
        
        **classmethod** CreateNew(identifier, args) -> Layer
        
        
        Creates a new empty layer with the given identifier.
        
        
        Additional arguments may be supplied via the ``args`` parameter. These
        arguments may control behavior specific to the layer's file format.
        
        
        Parameters
        ----------
        identifier : str
        
        args : FileFormatArguments
        
        
        
        ----------------------------------------------------------------------
        
        CreateNew(fileFormat, identifier, args) -> Layer
        
        
        Creates a new empty layer with the given identifier for a given file
        format class.
        
        
        This function has the same behavior as the other CreateNew function,
        but uses the explicitly-specified ``fileFormat`` instead of attempting
        to discern the format from ``identifier`` .
        
        
        Parameters
        ----------
        fileFormat : FileFormat
        
        identifier : str
        
        args : FileFormatArguments
        
        
        """
    @staticmethod
    def DumpLayerInfo(*args, **kwargs):
        """
        
        
        Debug helper to examine content of the current layer registry and
        the asset/real path of all layers in the registry.
        """
    @staticmethod
    def EraseTimeSample(*args, **kwargs):
        """
        
        EraseTimeSample(path, time) -> None
        
        
        Parameters
        ----------
        path : Path
        
        time : float
        
        
        """
    @staticmethod
    def Export(*args, **kwargs):
        """
        
        Export(filename, comment, args) -> bool
        
        
        Exports this layer to a file.
        
        
        Returns ``true`` if successful, ``false`` if an error occurred.
        
        If ``comment`` is not empty, the layer gets exported with the given
        comment. Additional arguments may be supplied via the ``args``
        parameter. These arguments may control behavior specific to the
        exported layer's file format.
        
        Note that the file name or comment of the original layer is not
        updated. This only saves a copy of the layer to the given filename.
        Subsequent calls to Save() will still save the layer to it's
        previously remembered file name.
        
        
        Parameters
        ----------
        filename : str
        
        comment : str
        
        args : FileFormatArguments
        
        
        """
    @staticmethod
    def ExportToString(*args, **kwargs):
        """
        
        
        Returns the string representation of the layer.
        """
    @staticmethod
    def Find(*args, **kwargs):
        """
        
        
        Find(filename) -> LayerPtr
        
        filename : string
        
        Returns the open layer with the given filename, or None.  Note that this is a static class method.
        """
    @staticmethod
    def FindOrOpen(*args, **kwargs):
        """
        
        **classmethod** FindOrOpen(identifier, args) -> Layer
        
        
        Return an existing layer with the given ``identifier`` and ``args`` ,
        or else load it.
        
        
        If the layer can't be found or loaded, an error is posted and a null
        layer is returned.
        
        Arguments in ``args`` will override any arguments specified in
        ``identifier`` .
        
        
        Parameters
        ----------
        identifier : str
        
        args : FileFormatArguments
        
        
        """
    @staticmethod
    def FindOrOpenRelativeToLayer(*args, **kwargs):
        """
        
        **classmethod** FindOrOpenRelativeToLayer(anchor, identifier, args) -> Layer
        
        
        Return an existing layer with the given ``identifier`` and ``args`` ,
        or else load it.
        
        
        The given ``identifier`` will be resolved relative to the ``anchor``
        layer. If the layer can't be found or loaded, an error is posted and a
        null layer is returned.
        
        If the ``anchor`` layer is invalid, issues a coding error and returns
        a null handle.
        
        Arguments in ``args`` will override any arguments specified in
        ``identifier`` .
        
        
        Parameters
        ----------
        anchor : Layer
        
        identifier : str
        
        args : FileFormatArguments
        
        
        """
    @staticmethod
    def FindRelativeToLayer(*args, **kwargs):
        """
        
        
        Returns the open layer with the given filename, or None.  If the filename is a relative path then it's found relative to the given layer.  Note that this is a static class method.
        """
    @staticmethod
    def GetAssetInfo(*args, **kwargs):
        """
        
        GetAssetInfo() -> VtValue
        
        
        Returns resolve information from the last time the layer identifier
        was resolved.
        
        
        
        """
    @staticmethod
    def GetAssetName(*args, **kwargs):
        """
        
        GetAssetName() -> str
        
        
        Returns the asset name associated with this layer.
        
        
        
        """
    @staticmethod
    def GetAttributeAtPath(*args, **kwargs):
        """
        
        GetAttributeAtPath(path) -> AttributeSpec
        
        
        Returns an attribute at the given ``path`` .
        
        
        Returns ``None`` if there is no attribute at ``path`` . This is simply
        a more specifically typed version of ``GetObjectAtPath()`` .
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetBracketingTimeSamples(*args, **kwargs):
        """
        
        GetBracketingTimeSamples(time, tLower, tUpper) -> bool
        
        
        Parameters
        ----------
        time : float
        
        tLower : float
        
        tUpper : float
        
        
        """
    @staticmethod
    def GetBracketingTimeSamplesForPath(*args, **kwargs):
        """
        
        GetBracketingTimeSamplesForPath(path, time, tLower, tUpper) -> bool
        
        
        Parameters
        ----------
        path : Path
        
        time : float
        
        tLower : float
        
        tUpper : float
        
        
        """
    @staticmethod
    def GetCompositionAssetDependencies(*args, **kwargs):
        """
        
        GetCompositionAssetDependencies() -> set[str]
        
        
        Return paths of all assets this layer depends on due to composition
        fields.
        
        
        This includes the paths of all layers referred to by reference,
        payload, and sublayer fields in this layer. This function only returns
        direct composition dependencies of this layer, i.e. it does not
        recurse to find composition dependencies from its dependent layer
        assets.
        
        
        
        """
    @staticmethod
    def GetDetachedLayerRules(*args, **kwargs):
        """
        
        **classmethod** GetDetachedLayerRules() -> DetachedLayerRules
        
        
        Returns the current rules for the detached layer set.
        
        
        
        """
    @staticmethod
    def GetDisplayName(*args, **kwargs):
        """
        
        GetDisplayName() -> str
        
        
        Returns the layer's display name.
        
        
        The display name is the base filename of the identifier.
        
        
        
        """
    @staticmethod
    def GetDisplayNameFromIdentifier(*args, **kwargs):
        """
        
        **classmethod** GetDisplayNameFromIdentifier(identifier) -> str
        
        
        Returns the display name for the given ``identifier`` , using the same
        rules as GetDisplayName.
        
        
        Parameters
        ----------
        identifier : str
        
        
        """
    @staticmethod
    def GetExternalAssetDependencies(*args, **kwargs):
        """
        
        GetExternalAssetDependencies() -> set[str]
        
        
        Returns a set of resolved paths to all external asset dependencies the
        layer needs to generate its contents.
        
        
        These are additional asset dependencies that are determined by the
        layer's file format and will be consulted during Reload() when
        determining if the layer needs to be reloaded. This specifically does
        not include dependencies related to composition, i.e. this will not
        include assets from references, payloads, and sublayers.
        
        
        
        """
    @staticmethod
    def GetExternalReferences(*args, **kwargs):
        """
        
        
        Return a list of asset paths for
        this layer.
        """
    @staticmethod
    def GetFileFormat(*args, **kwargs):
        """
        
        GetFileFormat() -> FileFormat
        
        
        Returns the file format used by this layer.
        
        
        
        """
    @staticmethod
    def GetFileFormatArguments(*args, **kwargs):
        """
        
        GetFileFormatArguments() -> FileFormatArguments
        
        
        Returns the file format-specific arguments used during the
        construction of this layer.
        
        
        
        """
    @staticmethod
    def GetLoadedLayers(*args, **kwargs):
        """
        
        
        Return list of loaded layers.
        """
    @staticmethod
    def GetMutedLayers(*args, **kwargs):
        """
        
        
        Return list of muted layers.
        """
    @staticmethod
    def GetNumTimeSamplesForPath(*args, **kwargs):
        """
        
        GetNumTimeSamplesForPath(path) -> int
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetObjectAtPath(*args, **kwargs):
        """
        
        GetObjectAtPath(path) -> Spec
        
        
        Returns the object at the given ``path`` .
        
        
        There is no distinction between an absolute and relative path at the
        SdLayer level.
        
        Returns ``None`` if there is no object at ``path`` .
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetPrimAtPath(*args, **kwargs):
        """
        
        GetPrimAtPath(path) -> PrimSpec
        
        
        Returns the prim at the given ``path`` .
        
        
        Returns ``None`` if there is no prim at ``path`` . This is simply a
        more specifically typed version of ``GetObjectAtPath()`` .
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetPropertyAtPath(*args, **kwargs):
        """
        
        GetPropertyAtPath(path) -> PropertySpec
        
        
        Returns a property at the given ``path`` .
        
        
        Returns ``None`` if there is no property at ``path`` . This is simply
        a more specifically typed version of ``GetObjectAtPath()`` .
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetRelationshipAtPath(*args, **kwargs):
        """
        
        GetRelationshipAtPath(path) -> RelationshipSpec
        
        
        Returns a relationship at the given ``path`` .
        
        
        Returns ``None`` if there is no relationship at ``path`` . This is
        simply a more specifically typed version of ``GetObjectAtPath()`` .
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def HasColorConfiguration(*args, **kwargs):
        """
        
        HasColorConfiguration() -> bool
        
        
        Returns true if color configuration metadata is set in this layer.
        
        
        
        GetColorConfiguration() , SetColorConfiguration()
        
        
        
        """
    @staticmethod
    def HasColorManagementSystem(*args, **kwargs):
        """
        
        HasColorManagementSystem() -> bool
        
        
        Returns true if colorManagementSystem metadata is set in this layer.
        
        
        
        GetColorManagementSystem() , SetColorManagementSystem()
        
        
        
        """
    @staticmethod
    def HasCustomLayerData(*args, **kwargs):
        """
        
        HasCustomLayerData() -> bool
        
        
        Returns true if CustomLayerData is authored on the layer.
        
        
        
        """
    @staticmethod
    def HasDefaultPrim(*args, **kwargs):
        """
        
        HasDefaultPrim() -> bool
        
        
        Return true if the default prim metadata is set in this layer.
        
        
        See GetDefaultPrim() and SetDefaultPrim() .
        
        
        
        """
    @staticmethod
    def HasEndTimeCode(*args, **kwargs):
        """
        
        HasEndTimeCode() -> bool
        
        
        Returns true if the layer has an endTimeCode opinion.
        
        
        
        """
    @staticmethod
    def HasFramePrecision(*args, **kwargs):
        """
        
        HasFramePrecision() -> bool
        
        
        Returns true if the layer has a frames precision opinion.
        
        
        
        """
    @staticmethod
    def HasFramesPerSecond(*args, **kwargs):
        """
        
        HasFramesPerSecond() -> bool
        
        
        Returns true if the layer has a frames per second opinion.
        
        
        
        """
    @staticmethod
    def HasOwner(*args, **kwargs):
        """
        
        HasOwner() -> bool
        
        
        Returns true if the layer has an owner opinion.
        
        
        
        """
    @staticmethod
    def HasSessionOwner(*args, **kwargs):
        """
        
        HasSessionOwner() -> bool
        
        
        Returns true if the layer has a session owner opinion.
        
        
        
        """
    @staticmethod
    def HasStartTimeCode(*args, **kwargs):
        """
        
        HasStartTimeCode() -> bool
        
        
        Returns true if the layer has a startTimeCode opinion.
        
        
        
        """
    @staticmethod
    def HasTimeCodesPerSecond(*args, **kwargs):
        """
        
        HasTimeCodesPerSecond() -> bool
        
        
        Returns true if the layer has a timeCodesPerSecond opinion.
        
        
        
        """
    @staticmethod
    def Import(*args, **kwargs):
        """
        
        Import(layerPath) -> bool
        
        
        Imports the content of the given layer path, replacing the content of
        the current layer.
        
        
        Note: If the layer path is the same as the current layer's real path,
        no action is taken (and a warning occurs). For this case use Reload()
        .
        
        
        Parameters
        ----------
        layerPath : str
        
        
        """
    @staticmethod
    def ImportFromString(*args, **kwargs):
        """
        
        ImportFromString(string) -> bool
        
        
        Reads this layer from the given string.
        
        
        Returns ``true`` if successful, otherwise returns ``false`` .
        
        
        Parameters
        ----------
        string : str
        
        
        """
    @staticmethod
    def IsAnonymousLayerIdentifier(*args, **kwargs):
        """
        
        **classmethod** IsAnonymousLayerIdentifier(identifier) -> bool
        
        
        Returns true if the ``identifier`` is an anonymous layer unique
        identifier.
        
        
        Parameters
        ----------
        identifier : str
        
        
        """
    @staticmethod
    def IsDetached(*args, **kwargs):
        """
        
        IsDetached() -> bool
        
        
        Returns true if this layer is detached from its serialized data store,
        false otherwise.
        
        
        Detached layers are isolated from external changes to their serialized
        data.
        
        
        
        """
    @staticmethod
    def IsIncludedByDetachedLayerRules(*args, **kwargs):
        """
        
        **classmethod** IsIncludedByDetachedLayerRules(identifier) -> bool
        
        
        Returns whether the given layer identifier is included in the current
        rules for the detached layer set.
        
        
        This is equivalent to GetDetachedLayerRules() .IsIncluded(identifier).
        
        
        Parameters
        ----------
        identifier : str
        
        
        """
    @staticmethod
    def IsMuted(*args, **kwargs):
        """
        
        **classmethod** IsMuted() -> bool
        
        
        Returns ``true`` if the current layer is muted.
        
        
        
        
        ----------------------------------------------------------------------
        
        IsMuted(path) -> bool
        
        
        Returns ``true`` if the specified layer path is muted.
        
        
        Parameters
        ----------
        path : str
        
        
        """
    @staticmethod
    def ListAllTimeSamples(*args, **kwargs):
        """
        
        ListAllTimeSamples() -> set[float]
        
        
        
        """
    @staticmethod
    def ListTimeSamplesForPath(*args, **kwargs):
        """
        
        ListTimeSamplesForPath(path) -> set[float]
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def New(*args, **kwargs):
        """
        
        **classmethod** New(fileFormat, identifier, args) -> Layer
        
        
        Creates a new empty layer with the given identifier for a given file
        format class.
        
        
        The new layer will not be dirty and will not be saved.
        
        Additional arguments may be supplied via the ``args`` parameter. These
        arguments may control behavior specific to the layer's file format.
        
        
        Parameters
        ----------
        fileFormat : FileFormat
        
        identifier : str
        
        args : FileFormatArguments
        
        
        """
    @staticmethod
    def OpenAsAnonymous(*args, **kwargs):
        """
        
        **classmethod** OpenAsAnonymous(layerPath, metadataOnly, tag) -> Layer
        
        
        Load the given layer from disk as a new anonymous layer.
        
        
        If the layer can't be found or loaded, an error is posted and a null
        layer is returned.
        
        The anonymous layer does not retain any knowledge of the backing file
        on the filesystem.
        
        ``metadataOnly`` is a flag that asks for only the layer metadata to be
        read in, which can be much faster if that is all that is required.
        Note that this is just a hint: some FileFormat readers may disregard
        this flag and still fully populate the layer contents.
        
        An optional ``tag`` may be specified. See CreateAnonymous for details.
        
        
        Parameters
        ----------
        layerPath : str
        
        metadataOnly : bool
        
        tag : str
        
        
        """
    @staticmethod
    def QueryTimeSample(*args, **kwargs):
        """
        
        QueryTimeSample(path, time, value) -> bool
        
        
        Parameters
        ----------
        path : Path
        
        time : float
        
        value : VtValue
        
        
        
        ----------------------------------------------------------------------
        
        QueryTimeSample(path, time, value) -> bool
        
        
        Parameters
        ----------
        path : Path
        
        time : float
        
        value : SdfAbstractDataValue
        
        
        
        ----------------------------------------------------------------------
        
        QueryTimeSample(path, time, data) -> bool
        
        
        Parameters
        ----------
        path : Path
        
        time : float
        
        data : T
        
        
        """
    @staticmethod
    def Reload(*args, **kwargs):
        """
        
        Reload(force) -> bool
        
        
        Reloads the layer from its persistent representation.
        
        
        This restores the layer to a state as if it had just been created with
        FindOrOpen() . This operation is Undo-able.
        
        The fileName and whether journaling is enabled are not affected by
        this method.
        
        When called with force = false (the default), Reload attempts to avoid
        reloading layers that have not changed on disk. It does so by
        comparing the file's modification time (mtime) to when the file was
        loaded. If the layer has unsaved modifications, this mechanism is not
        used, and the layer is reloaded from disk. If the layer has any
        external asset dependencies their modification state will also be
        consulted when determining if the layer needs to be reloaded.
        
        Passing true to the ``force`` parameter overrides this behavior,
        forcing the layer to be reloaded from disk regardless of whether it
        has changed.
        
        
        Parameters
        ----------
        force : bool
        
        
        """
    @staticmethod
    def ReloadLayers(*args, **kwargs):
        """
        
        **classmethod** ReloadLayers(layers, force) -> bool
        
        
        Reloads the specified layers.
        
        
        Returns ``false`` if one or more layers failed to reload.
        
        See ``Reload()`` for a description of the ``force`` flag.
        
        
        Parameters
        ----------
        layers : set[Layer]
        
        force : bool
        
        
        """
    @staticmethod
    def RemoveFromMutedLayers(*args, **kwargs):
        """
        
        **classmethod** RemoveFromMutedLayers(mutedPath) -> None
        
        
        Remove the specified path from the muted layers set.
        
        
        Parameters
        ----------
        mutedPath : str
        
        
        """
    @staticmethod
    def RemoveInertSceneDescription(*args, **kwargs):
        """
        
        RemoveInertSceneDescription() -> None
        
        
        Removes all scene description in this layer that does not affect the
        scene.
        
        
        This method walks the layer namespace hierarchy and removes any prims
        and that are not contributing any opinions.
        
        
        
        """
    @staticmethod
    def Save(*args, **kwargs):
        """
        
        Save(force) -> bool
        
        
        Returns ``true`` if successful, ``false`` if an error occurred.
        
        
        Returns ``false`` if the layer has no remembered file name or the
        layer type cannot be saved. The layer will not be overwritten if the
        file exists and the layer is not dirty unless ``force`` is true.
        
        
        Parameters
        ----------
        force : bool
        
        
        """
    @staticmethod
    def ScheduleRemoveIfInert(*args, **kwargs):
        """
        
        ScheduleRemoveIfInert(spec) -> None
        
        
        Cause ``spec`` to be removed if it no longer affects the scene when
        the last change block is closed, or now if there are no change blocks.
        
        
        Parameters
        ----------
        spec : Spec
        
        
        """
    @staticmethod
    def SetDetachedLayerRules(*args, **kwargs):
        """
        
        **classmethod** SetDetachedLayerRules(mask) -> None
        
        
        Sets the rules specifying detached layers.
        
        
        Newly-created or opened layers whose identifiers are included in
        ``rules`` will be opened as detached layers. Existing layers that are
        now included or no longer included will be reloaded. Any unsaved
        modifications to those layers will be lost.
        
        This function is not thread-safe. It may not be run concurrently with
        any other functions that open, close, or read from any layers.
        
        The detached layer rules are initially set to exclude all layers. This
        may be overridden by setting the environment variables
        SDF_LAYER_INCLUDE_DETACHED and SDF_LAYER_EXCLUDE_DETACHED to specify
        the initial set of include and exclude patterns in the rules. These
        variables can be set to a comma-delimited list of patterns.
        SDF_LAYER_INCLUDE_DETACHED may also be set to"\\*"to include all
        layers. Note that these environment variables only set the initial
        state of the detached layer rules; these values may be overwritten by
        subsequent calls to this function.
        
        See SdfLayer::DetachedLayerRules::IsIncluded for details on how the
        rules are applied to layer identifiers.
        
        
        Parameters
        ----------
        mask : DetachedLayerRules
        
        
        """
    @staticmethod
    def SetMuted(*args, **kwargs):
        """
        
        SetMuted(muted) -> None
        
        
        Mutes the current layer if ``muted`` is ``true`` , and unmutes it
        otherwise.
        
        
        Parameters
        ----------
        muted : bool
        
        
        """
    @staticmethod
    def SetPermissionToEdit(*args, **kwargs):
        """
        
        SetPermissionToEdit(allow) -> None
        
        
        Sets permission to edit.
        
        
        Parameters
        ----------
        allow : bool
        
        
        """
    @staticmethod
    def SetPermissionToSave(*args, **kwargs):
        """
        
        SetPermissionToSave(allow) -> None
        
        
        Sets permission to save.
        
        
        Parameters
        ----------
        allow : bool
        
        
        """
    @staticmethod
    def SetTimeSample(*args, **kwargs):
        """
        
        SetTimeSample(path, time, value) -> None
        
        
        Parameters
        ----------
        path : Path
        
        time : float
        
        value : VtValue
        
        
        
        ----------------------------------------------------------------------
        
        SetTimeSample(path, time, value) -> None
        
        
        Parameters
        ----------
        path : Path
        
        time : float
        
        value : SdfAbstractDataConstValue
        
        
        
        ----------------------------------------------------------------------
        
        SetTimeSample(path, time, value) -> None
        
        
        Parameters
        ----------
        path : Path
        
        time : float
        
        value : T
        
        
        """
    @staticmethod
    def SplitIdentifier(*args, **kwargs):
        """
        
        **classmethod** SplitIdentifier(identifier, layerPath, arguments) -> bool
        
        
        Splits the given layer identifier into its constituent layer path and
        arguments.
        
        
        Parameters
        ----------
        identifier : str
        
        layerPath : str
        
        arguments : FileFormatArguments
        
        
        """
    @staticmethod
    def StreamsData(*args, **kwargs):
        """
        
        StreamsData() -> bool
        
        
        Returns true if this layer streams data from its serialized data store
        on demand, false otherwise.
        
        
        Layers with streaming data are treated differently to avoid pulling in
        data unnecessarily. For example, reloading a streaming layer will not
        perform fine-grained change notification, since doing so would require
        the full contents of the layer to be loaded.
        
        
        
        """
    @staticmethod
    def TransferContent(*args, **kwargs):
        """
        
        TransferContent(layer) -> None
        
        
        Copies the content of the given layer into this layer.
        
        
        Source layer is unmodified.
        
        
        Parameters
        ----------
        layer : Layer
        
        
        """
    @staticmethod
    def Traverse(*args, **kwargs):
        """
        
        Traverse(path, func) -> None
        
        
        Parameters
        ----------
        path : Path
        
        func : TraversalFunction
        
        
        """
    @staticmethod
    def UpdateAssetInfo(*args, **kwargs):
        """
        
        UpdateAssetInfo() -> None
        
        
        Update layer asset information.
        
        
        Calling this method re-resolves the layer identifier, which updates
        asset information such as the layer's resolved path and other asset
        info. This may be used to update the layer after external changes to
        the underlying asset system.
        
        
        
        """
    @staticmethod
    def UpdateCompositionAssetDependency(*args, **kwargs):
        """
        
        UpdateCompositionAssetDependency(oldAssetPath, newAssetPath) -> bool
        
        
        Updates the asset path of a composation dependency in this layer.
        
        
        If ``newAssetPath`` is supplied, the update works as"rename", updating
        any occurrence of ``oldAssetPath`` to ``newAssetPath`` in all
        reference, payload, and sublayer fields.
        
        If ``newAssetPath`` is not given, this update behaves as a"delete",
        removing all occurrences of ``oldAssetPath`` from all reference,
        payload, and sublayer fields.
        
        
        Parameters
        ----------
        oldAssetPath : str
        
        newAssetPath : str
        
        
        """
    @staticmethod
    def UpdateExternalReference(*args, **kwargs):
        """
        
        UpdateExternalReference(oldAssetPath, newAssetPath) -> bool
        
        
        Deprecated
        
        Use UpdateCompositionAssetDependency instead.
        
        
        Parameters
        ----------
        oldAssetPath : str
        
        newAssetPath : str
        
        
        """
    @staticmethod
    def _WriteDataFile(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        
        
        True if this object has not expired.  False otherwise.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        """
        
        
        Equality operator:  x == y
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __lt__(*args, **kwargs):
        """
        
        
        Less than operator: x < y
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        """
        
        
        Non-equality operator: x != y
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def anonymous(*args, **kwargs):
        """
        type : bool
        
        
        Returns true if this layer is an anonymous layer.
        """
    @property
    def colorConfiguration(*args, **kwargs):
        """
        The color configuration asset-path of this layer.
        """
    @colorConfiguration.setter
    def colorConfiguration(*args, **kwargs):
        ...
    @property
    def colorManagementSystem(*args, **kwargs):
        """
        The name of the color management system used to interpret the colorConfiguration asset.
        """
    @colorManagementSystem.setter
    def colorManagementSystem(*args, **kwargs):
        ...
    @property
    def comment(*args, **kwargs):
        """
        The layer's comment string.
        """
    @comment.setter
    def comment(*args, **kwargs):
        ...
    @property
    def customLayerData(*args, **kwargs):
        """
        The customLayerData dictionary associated with this layer.
        """
    @customLayerData.setter
    def customLayerData(*args, **kwargs):
        ...
    @property
    def defaultPrim(*args, **kwargs):
        """
        The layer's default reference target token.
        """
    @defaultPrim.setter
    def defaultPrim(*args, **kwargs):
        ...
    @property
    def dirty(*args, **kwargs):
        """
        type : bool
        
        
        Returns ``true`` if the layer is dirty, i.e.
        
        
        has changed from its persistent representation.
        """
    @property
    def documentation(*args, **kwargs):
        """
        The layer's documentation string.
        """
    @documentation.setter
    def documentation(*args, **kwargs):
        ...
    @property
    def empty(*args, **kwargs):
        """
        type : bool
        
        
        Returns whether this layer has no significant data.
        """
    @property
    def endTimeCode(*args, **kwargs):
        """
        The end timeCode of this layer.
        
        The end timeCode of a layer is not a hard limit, but is 
        more of a hint. A layer's time-varying content is not limited to
        the timeCode range of the layer.
        """
    @endTimeCode.setter
    def endTimeCode(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
    @property
    def externalReferences(*args, **kwargs):
        """
        Return unique list of asset paths of external references for
        given layer.
        """
    @property
    def fileExtension(*args, **kwargs):
        """
        The layer's file extension.
        """
    @property
    def framePrecision(*args, **kwargs):
        """
        The number of digits of precision used in times in this layer.
        """
    @framePrecision.setter
    def framePrecision(*args, **kwargs):
        ...
    @property
    def framesPerSecond(*args, **kwargs):
        """
        The frames per second used in this layer.
        """
    @framesPerSecond.setter
    def framesPerSecond(*args, **kwargs):
        ...
    @property
    def hasOwnedSubLayers(*args, **kwargs):
        """
        Whether this layer's sub layers are expected to have owners.
        """
    @hasOwnedSubLayers.setter
    def hasOwnedSubLayers(*args, **kwargs):
        ...
    @property
    def identifier(*args, **kwargs):
        """
        The layer's identifier.
        """
    @identifier.setter
    def identifier(*args, **kwargs):
        ...
    @property
    def owner(*args, **kwargs):
        """
        The owner of this layer.
        """
    @owner.setter
    def owner(*args, **kwargs):
        ...
    @property
    def permissionToEdit(*args, **kwargs):
        """
        Return true if permitted to be edited (modified), false otherwise.
        """
    @property
    def permissionToSave(*args, **kwargs):
        """
        Return true if permitted to be saved, false otherwise.
        """
    @property
    def pseudoRoot(*args, **kwargs):
        """
        The pseudo-root of the layer.
        """
    @property
    def realPath(*args, **kwargs):
        """
        The layer's resolved path.
        """
    @property
    def repositoryPath(*args, **kwargs):
        """
        The layer's associated repository path
        """
    @property
    def resolvedPath(*args, **kwargs):
        """
        The layer's resolved path.
        """
    @property
    def rootPrimOrder(*args, **kwargs):
        """
        Get/set the list of root prim names for this layer's 'reorder rootPrims' statement.
        """
    @rootPrimOrder.setter
    def rootPrimOrder(*args, **kwargs):
        ...
    @property
    def rootPrims(*args, **kwargs):
        """
        The root prims of this layer, as an ordered dictionary.
        
        The prims may be accessed by index or by name.
        Although this property claims it is read only, you can modify the contents of this dictionary to add, remove, or reorder the contents.
        """
    @property
    def sessionOwner(*args, **kwargs):
        """
        The session owner of this layer. Only intended for use with session layers.
        """
    @sessionOwner.setter
    def sessionOwner(*args, **kwargs):
        ...
    @property
    def startTimeCode(*args, **kwargs):
        """
        The start timeCode of this layer.
        
        The start timeCode of a layer is not a hard limit, but is 
        more of a hint.  A layer's time-varying content is not limited to 
        the timeCode range of the layer.
        """
    @startTimeCode.setter
    def startTimeCode(*args, **kwargs):
        ...
    @property
    def subLayerOffsets(*args, **kwargs):
        """
        The sublayer offsets of this layer, as a list.  Although this property is claimed to be read only, you can modify the contents of this list by assigning new layer offsets to specific indices.
        """
    @property
    def subLayerPaths(*args, **kwargs):
        """
        The sublayer paths of this layer, as a list.  Although this property is claimed to be read only, you can modify the contents of this list.
        """
    @subLayerPaths.setter
    def subLayerPaths(*args, **kwargs):
        ...
    @property
    def timeCodesPerSecond(*args, **kwargs):
        """
        The timeCodes per second used in this layer.
        """
    @timeCodesPerSecond.setter
    def timeCodesPerSecond(*args, **kwargs):
        ...
    @property
    def version(*args, **kwargs):
        """
        The layer's version.
        """
class LayerOffset(Boost.Python.instance):
    """
    
    Represents a time offset and scale between layers.
    
    The SdfLayerOffset class is an affine transform, providing both a
    scale and a translate. It supports vector algebra semantics for
    composing SdfLayerOffsets together via multiplication. The
    SdfLayerOffset class is unitless: it does not refer to seconds or
    frames.
    
    For example, suppose layer A uses layer B, with an offset of X:  when
    bringing animation from B into A, you first apply the scale of X, and
    then the offset. Suppose you have a scale of 2 and an offset of 24:
    first multiply B's frame numbers by 2, and then add 24. The animation
    from B as seen in A will take twice as long and start 24 frames later.
    
    Offsets are typically used in either sublayers or prim references. For
    more information, see the SetSubLayerOffset() method of the SdfLayer
    class (the subLayerOffsets property in Python), as well as the
    SetReference() and GetReferenceLayerOffset() methods (the latter is
    the referenceLayerOffset property in Python) of the SdfPrimSpec class.
    
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse() -> LayerOffset
        
        
        Gets the inverse offset, which performs the opposite transformation.
        
        
        
        """
    @staticmethod
    def IsIdentity(*args, **kwargs):
        """
        
        IsIdentity() -> bool
        
        
        Returns ``true`` if this is an identity transformation, with an offset
        of 0.0 and a scale of 1.0.
        
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(offset, scale)
        
        
        Constructs a new SdfLayerOffset instance.
        
        
        Parameters
        ----------
        offset : float
        
        scale : float
        
        
        """
    @staticmethod
    def __mul__(*args, **kwargs):
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
    def offset(*args, **kwargs):
        """
        type : None
        
        
        Sets the time offset.
        
        ----------------------------------------------------------------------
        
        type : float
        
        
        Returns the time offset.
        """
    @property
    def scale(*args, **kwargs):
        """
        type : None
        
        
        Sets the time scale factor.
        
        ----------------------------------------------------------------------
        
        type : float
        
        
        Returns the time scale factor.
        """
class LayerTree(Boost.Python.instance):
    """
    
    A SdfLayerTree is an immutable tree structure representing a sublayer
    stack and its recursive structure.
    
    Layers can have sublayers, which can in turn have sublayers of their
    own. Clients that want to represent that hierarchical structure in
    memory can build a SdfLayerTree for that purpose.
    
    We use TfRefPtr<SdfLayerTree> as handles to LayerTrees, as a simple
    way to pass them around as immutable trees without worrying about
    lifetime.
    
    """
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        
        
        True if this object has not expired.  False otherwise.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        """
        
        
        Equality operator:  x == y
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(layer, childTrees, cumulativeOffset)
        
        
        Parameters
        ----------
        layer : Layer
        
        childTrees : list[LayerTree]
        
        cumulativeOffset : LayerOffset
        
        
        """
    @staticmethod
    def __lt__(*args, **kwargs):
        """
        
        
        Less than operator: x < y
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        """
        
        
        Non-equality operator: x != y
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def childTrees(*args, **kwargs):
        """
        type : list[LayerTree]
        
        
        Returns the children of this tree node.
        """
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
    @property
    def layer(*args, **kwargs):
        """
        type : Layer
        
        
        Returns the layer handle this tree node represents.
        """
    @property
    def offset(*args, **kwargs):
        """
        type : LayerOffset
        
        
        Returns the cumulative layer offset from the root of the tree.
        """
class LengthUnit(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Sdf.LengthUnitMillimeter, Sdf.LengthUnitCentimeter, Sdf.LengthUnitDecimeter, Sdf.LengthUnitMeter, Sdf.LengthUnitKilometer, Sdf.LengthUnitInch, Sdf.LengthUnitFoot, Sdf.LengthUnitYard, Sdf.LengthUnitMile)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ListEditorProxy_SdfNameKeyPolicy(Boost.Python.instance):
    @staticmethod
    def Add(*args, **kwargs):
        ...
    @staticmethod
    def Append(*args, **kwargs):
        ...
    @staticmethod
    def ApplyEditsToList(*args, **kwargs):
        ...
    @staticmethod
    def ClearEdits(*args, **kwargs):
        ...
    @staticmethod
    def ClearEditsAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def ContainsItemEdit(*args, **kwargs):
        ...
    @staticmethod
    def CopyItems(*args, **kwargs):
        ...
    @staticmethod
    def Erase(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def ModifyItemEdits(*args, **kwargs):
        ...
    @staticmethod
    def Prepend(*args, **kwargs):
        ...
    @staticmethod
    def Remove(*args, **kwargs):
        ...
    @staticmethod
    def RemoveItemEdits(*args, **kwargs):
        ...
    @staticmethod
    def ReplaceItemEdits(*args, **kwargs):
        ...
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExpired(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def isOrderedOnly(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class ListEditorProxy_SdfPathKeyPolicy(Boost.Python.instance):
    @staticmethod
    def Add(*args, **kwargs):
        ...
    @staticmethod
    def Append(*args, **kwargs):
        ...
    @staticmethod
    def ApplyEditsToList(*args, **kwargs):
        ...
    @staticmethod
    def ClearEdits(*args, **kwargs):
        ...
    @staticmethod
    def ClearEditsAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def ContainsItemEdit(*args, **kwargs):
        ...
    @staticmethod
    def CopyItems(*args, **kwargs):
        ...
    @staticmethod
    def Erase(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def ModifyItemEdits(*args, **kwargs):
        ...
    @staticmethod
    def Prepend(*args, **kwargs):
        ...
    @staticmethod
    def Remove(*args, **kwargs):
        ...
    @staticmethod
    def RemoveItemEdits(*args, **kwargs):
        ...
    @staticmethod
    def ReplaceItemEdits(*args, **kwargs):
        ...
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExpired(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def isOrderedOnly(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class ListEditorProxy_SdfPayloadTypePolicy(Boost.Python.instance):
    @staticmethod
    def Add(*args, **kwargs):
        ...
    @staticmethod
    def Append(*args, **kwargs):
        ...
    @staticmethod
    def ApplyEditsToList(*args, **kwargs):
        ...
    @staticmethod
    def ClearEdits(*args, **kwargs):
        ...
    @staticmethod
    def ClearEditsAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def ContainsItemEdit(*args, **kwargs):
        ...
    @staticmethod
    def CopyItems(*args, **kwargs):
        ...
    @staticmethod
    def Erase(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def ModifyItemEdits(*args, **kwargs):
        ...
    @staticmethod
    def Prepend(*args, **kwargs):
        ...
    @staticmethod
    def Remove(*args, **kwargs):
        ...
    @staticmethod
    def RemoveItemEdits(*args, **kwargs):
        ...
    @staticmethod
    def ReplaceItemEdits(*args, **kwargs):
        ...
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExpired(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def isOrderedOnly(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class ListEditorProxy_SdfReferenceTypePolicy(Boost.Python.instance):
    @staticmethod
    def Add(*args, **kwargs):
        ...
    @staticmethod
    def Append(*args, **kwargs):
        ...
    @staticmethod
    def ApplyEditsToList(*args, **kwargs):
        ...
    @staticmethod
    def ClearEdits(*args, **kwargs):
        ...
    @staticmethod
    def ClearEditsAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def ContainsItemEdit(*args, **kwargs):
        ...
    @staticmethod
    def CopyItems(*args, **kwargs):
        ...
    @staticmethod
    def Erase(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def ModifyItemEdits(*args, **kwargs):
        ...
    @staticmethod
    def Prepend(*args, **kwargs):
        ...
    @staticmethod
    def Remove(*args, **kwargs):
        ...
    @staticmethod
    def RemoveItemEdits(*args, **kwargs):
        ...
    @staticmethod
    def ReplaceItemEdits(*args, **kwargs):
        ...
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExpired(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def isOrderedOnly(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class ListOpType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Sdf.ListOpTypeExplicit, Sdf.ListOpTypeAdded, Sdf.ListOpTypePrepended, Sdf.ListOpTypeAppended, Sdf.ListOpTypeDeleted, Sdf.ListOpTypeOrdered)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ListProxy_SdfNameKeyPolicy(Boost.Python.instance):
    @staticmethod
    def ApplyEditsToList(*args, **kwargs):
        ...
    @staticmethod
    def ApplyList(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def replace(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
class ListProxy_SdfNameTokenKeyPolicy(Boost.Python.instance):
    @staticmethod
    def ApplyEditsToList(*args, **kwargs):
        ...
    @staticmethod
    def ApplyList(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def replace(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
class ListProxy_SdfPathKeyPolicy(Boost.Python.instance):
    @staticmethod
    def ApplyEditsToList(*args, **kwargs):
        ...
    @staticmethod
    def ApplyList(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def replace(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
class ListProxy_SdfPayloadTypePolicy(Boost.Python.instance):
    @staticmethod
    def ApplyEditsToList(*args, **kwargs):
        ...
    @staticmethod
    def ApplyList(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def replace(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
class ListProxy_SdfReferenceTypePolicy(Boost.Python.instance):
    @staticmethod
    def ApplyEditsToList(*args, **kwargs):
        ...
    @staticmethod
    def ApplyList(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def replace(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
class ListProxy_SdfSubLayerTypePolicy(Boost.Python.instance):
    @staticmethod
    def ApplyEditsToList(*args, **kwargs):
        ...
    @staticmethod
    def ApplyList(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def replace(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
class MapEditProxy_VtDictionary(Boost.Python.instance):
    class MapEditProxy_VtDictionary_Iterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class MapEditProxy_VtDictionary_KeyIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class MapEditProxy_VtDictionary_ValueIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
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
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def get(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def pop(*args, **kwargs):
        ...
    @staticmethod
    def popitem(*args, **kwargs):
        ...
    @staticmethod
    def setdefault(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
class MapEditProxy_map_SdfPath__SdfPath__less_SdfPath___allocator_pair_SdfPath_const__SdfPath_____(Boost.Python.instance):
    class MapEditProxy_map_SdfPath__SdfPath__less_SdfPath___allocator_pair_SdfPath_const__SdfPath______Iterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class MapEditProxy_map_SdfPath__SdfPath__less_SdfPath___allocator_pair_SdfPath_const__SdfPath______KeyIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class MapEditProxy_map_SdfPath__SdfPath__less_SdfPath___allocator_pair_SdfPath_const__SdfPath______ValueIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
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
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def get(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def pop(*args, **kwargs):
        ...
    @staticmethod
    def popitem(*args, **kwargs):
        ...
    @staticmethod
    def setdefault(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
class MapEditProxy_map_string__string__less_string___allocator_pair_stringconst__string_____(Boost.Python.instance):
    class MapEditProxy_map_string__string__less_string___allocator_pair_stringconst__string______Iterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class MapEditProxy_map_string__string__less_string___allocator_pair_stringconst__string______KeyIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class MapEditProxy_map_string__string__less_string___allocator_pair_stringconst__string______ValueIterator(Boost.Python.instance):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __next__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
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
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def get(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def pop(*args, **kwargs):
        ...
    @staticmethod
    def popitem(*args, **kwargs):
        ...
    @staticmethod
    def setdefault(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
class NamespaceEdit(Boost.Python.instance):
    """
    
    A single namespace edit. It supports renaming, reparenting,
    reparenting with a rename, reordering, and removal.
    
    """
    atEnd: typing.ClassVar[int] = -1
    same: typing.ClassVar[int] = -2
    @staticmethod
    def Remove(*args, **kwargs):
        """
        
        **classmethod** Remove(currentPath) -> This
        
        
        Returns a namespace edit that removes the object at ``currentPath`` .
        
        
        Parameters
        ----------
        currentPath : Path
        
        
        """
    @staticmethod
    def Rename(*args, **kwargs):
        """
        
        **classmethod** Rename(currentPath, name) -> This
        
        
        Returns a namespace edit that renames the prim or property at
        ``currentPath`` to ``name`` .
        
        
        Parameters
        ----------
        currentPath : Path
        
        name : str
        
        
        """
    @staticmethod
    def Reorder(*args, **kwargs):
        """
        
        **classmethod** Reorder(currentPath, index) -> This
        
        
        Returns a namespace edit to reorder the prim or property at
        ``currentPath`` to index ``index`` .
        
        
        Parameters
        ----------
        currentPath : Path
        
        index : Index
        
        
        """
    @staticmethod
    def Reparent(*args, **kwargs):
        """
        
        **classmethod** Reparent(currentPath, newParentPath, index) -> This
        
        
        Returns a namespace edit to reparent the prim or property at
        ``currentPath`` to be under ``newParentPath`` at index ``index`` .
        
        
        Parameters
        ----------
        currentPath : Path
        
        newParentPath : Path
        
        index : Index
        
        
        """
    @staticmethod
    def ReparentAndRename(*args, **kwargs):
        """
        
        **classmethod** ReparentAndRename(currentPath, newParentPath, name, index) -> This
        
        
        Returns a namespace edit to reparent the prim or property at
        ``currentPath`` to be under ``newParentPath`` at index ``index`` with
        the name ``name`` .
        
        
        Parameters
        ----------
        currentPath : Path
        
        newParentPath : Path
        
        name : str
        
        index : Index
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        The default edit maps the empty path to the empty path.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(currentPath_, newPath_, index_)
        
        
        The fully general edit.
        
        
        Parameters
        ----------
        currentPath_ : Path
        
        newPath_ : Path
        
        index_ : Index
        
        
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def currentPath(*args, **kwargs):
        ...
    @currentPath.setter
    def currentPath(*args, **kwargs):
        ...
    @property
    def index(*args, **kwargs):
        ...
    @index.setter
    def index(*args, **kwargs):
        ...
    @property
    def newPath(*args, **kwargs):
        ...
    @newPath.setter
    def newPath(*args, **kwargs):
        ...
class NamespaceEditDetail(Boost.Python.instance):
    """
    
    Detailed information about a namespace edit.
    
    """
    class Result(pxr.Tf.Tf_PyEnumWrapper):
        """
        
        Validity of an edit.
        
        """
        _baseName: typing.ClassVar[str] = 'NamespaceEditDetail'
        allValues: typing.ClassVar[tuple]  # value = (Sdf.NamespaceEditDetail.Error, Sdf.NamespaceEditDetail.Unbatched, Sdf.NamespaceEditDetail.Okay)
        @staticmethod
        def GetValueFromName(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    Error: typing.ClassVar[Result]  # value = Sdf.NamespaceEditDetail.Error
    Okay: typing.ClassVar[Result]  # value = Sdf.NamespaceEditDetail.Okay
    Unbatched: typing.ClassVar[Result]  # value = Sdf.NamespaceEditDetail.Unbatched
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1, edit, reason)
        
        
        Parameters
        ----------
        arg1 : Result
        
        edit : NamespaceEdit
        
        reason : str
        
        
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def edit(*args, **kwargs):
        ...
    @edit.setter
    def edit(*args, **kwargs):
        ...
    @property
    def reason(*args, **kwargs):
        ...
    @reason.setter
    def reason(*args, **kwargs):
        ...
    @property
    def result(*args, **kwargs):
        ...
    @result.setter
    def result(*args, **kwargs):
        ...
class Notice(Boost.Python.instance):
    """
    
    Wrapper class for Sdf notices.
    
    """
    class Base(pxr.Tf.Notice):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class LayerDidReloadContent(LayerDidReplaceContent):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class LayerDidReplaceContent(Base):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class LayerDirtinessChanged(Base):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class LayerIdentifierDidChange(Base):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @property
        def newIdentifier(*args, **kwargs):
            ...
        @property
        def oldIdentifier(*args, **kwargs):
            ...
    class LayerInfoDidChange(Base):
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
        def key(*args, **kwargs):
            ...
    class LayerMutenessChanged(Base):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
        @property
        def layerPath(*args, **kwargs):
            ...
        @property
        def wasMuted(*args, **kwargs):
            ...
    class LayersDidChange(Base):
        @staticmethod
        def GetLayers(*args, **kwargs):
            ...
        @staticmethod
        def GetSerialNumber(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class LayersDidChangeSentPerLayer(Base):
        @staticmethod
        def GetLayers(*args, **kwargs):
            ...
        @staticmethod
        def GetSerialNumber(*args, **kwargs):
            ...
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
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Path(Boost.Python.instance):
    """
    
    A path value used to locate objects in layers or scenegraphs.
    
    Overview
    ========
    
    SdfPath is used in several ways:
    
       - As a storage key for addressing and accessing values held in a
         SdfLayer
    
       - As a namespace identity for scenegraph objects
    
       - As a way to refer to other scenegraph objects through relative
         paths
         The paths represented by an SdfPath class may be either relative or
         absolute. Relative paths are relative to the prim object that contains
         them (that is, if an SdfRelationshipSpec target is relative, it is
         relative to the SdfPrimSpec object that owns the SdfRelationshipSpec
         object).
    
    SdfPath objects can be readily created from and converted back to
    strings, but as SdfPath objects, they have behaviors that make it easy
    and efficient to work with them. The SdfPath class provides a full
    range of methods for manipulating scene paths by appending a namespace
    child, appending a relationship target, getting the parent path, and
    so on. Since the SdfPath class uses a node-based representation
    internally, you should use the editing functions rather than
    converting to and from strings if possible.
    
    Path Syntax
    ===========
    
    Like a filesystem path, an SdfPath is conceptually just a sequence of
    path components. Unlike a filesystem path, each component has a type,
    and the type is indicated by the syntax.
    
    Two separators are used between parts of a path. A slash ("/")
    following an identifier is used to introduce a namespace child. A
    period (".") following an identifier is used to introduce a property.
    A property may also have several non-sequential colons (':') in its
    name to provide a rudimentary namespace within properties but may not
    end or begin with a colon.
    
    A leading slash in the string representation of an SdfPath object
    indicates an absolute path. Two adjacent periods indicate the parent
    namespace.
    
    Brackets ("["and"]") are used to indicate relationship target paths
    for relational attributes.
    
    The first part in a path is assumed to be a namespace child unless it
    is preceded by a period. That means:
    
       - ``/Foo`` is an absolute path specifying the root prim Foo.
    
       - ``/Foo/Bar`` is an absolute path specifying namespace child Bar
         of root prim Foo.
    
       - ``/Foo/Bar.baz`` is an absolute path specifying property ``baz``
         of namespace child Bar of root prim Foo.
    
       - ``Foo`` is a relative path specifying namespace child Foo of the
         current prim.
    
       - ``Foo/Bar`` is a relative path specifying namespace child Bar of
         namespace child Foo of the current prim.
    
       - ``Foo/Bar.baz`` is a relative path specifying property ``baz`` of
         namespace child Bar of namespace child Foo of the current prim.
    
       - ``.foo`` is a relative path specifying the property ``foo`` of
         the current prim.
    
       - ``/Foo.bar[/Foo.baz].attrib`` is a relational attribute path. The
         relationship ``/Foo.bar`` has a target ``/Foo.baz`` . There is a
         relational attribute ``attrib`` on that relationship->target pair.
    
    A Note on Thread-Safety
    =======================
    
    SdfPath is strongly thread-safe, in the sense that zero additional
    synchronization is required between threads creating or using SdfPath
    values. Just like TfToken, SdfPath values are immutable. Internally,
    SdfPath uses a global prefix tree to efficiently share representations
    of paths, and provide fast equality/hashing operations, but
    modifications to this table are internally synchronized. Consequently,
    as with TfToken, for best performance it is important to minimize the
    number of values created (since it requires synchronized access to
    this table) or copied (since it requires atomic ref-counting
    operations).
    
    """
    class AncestorsRange(Boost.Python.instance):
        class _iterator(Boost.Python.instance):
            @staticmethod
            def __init__(*args, **kwargs):
                """
                Raises an exception
                This class cannot be instantiated from Python
                """
            @staticmethod
            def __next__(*args, **kwargs):
                ...
            @staticmethod
            def __reduce__(*args, **kwargs):
                ...
        __instance_size__: typing.ClassVar[int] = 24
        @staticmethod
        def GetPath(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class _IsValidPathStringResult(Boost.Python.instance):
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
        def errorMessage(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 24
    absoluteIndicator: typing.ClassVar[str] = '/'
    absoluteRootPath: typing.ClassVar[Path]  # value = Sdf.Path('/')
    childDelimiter: typing.ClassVar[str] = '/'
    emptyPath: typing.ClassVar[Path]  # value = Sdf.Path.emptyPath
    expressionIndicator: typing.ClassVar[str] = 'expression'
    mapperArgDelimiter: typing.ClassVar[str] = '.'
    mapperIndicator: typing.ClassVar[str] = 'mapper'
    namespaceDelimiter: typing.ClassVar[str] = ':'
    parentPathElement: typing.ClassVar[str] = '..'
    propertyDelimiter: typing.ClassVar[str] = '.'
    reflexiveRelativePath: typing.ClassVar[Path]  # value = Sdf.Path('.')
    relationshipTargetEnd: typing.ClassVar[str] = ']'
    relationshipTargetStart: typing.ClassVar[str] = '['
    @staticmethod
    def AppendChild(*args, **kwargs):
        """
        
        AppendChild(childName) -> Path
        
        
        Creates a path by appending an element for ``childName`` to this path.
        
        
        This path must be a prim path, the AbsoluteRootPath or the
        ReflexiveRelativePath.
        
        
        Parameters
        ----------
        childName : str
        
        
        """
    @staticmethod
    def AppendElementString(*args, **kwargs):
        """
        
        AppendElementString(element) -> Path
        
        
        Creates a path by extracting and appending an element from the given
        ascii element encoding.
        
        
        Attempting to append a root or empty path (or malformed path) or
        attempting to append *to* the EmptyPath will raise an error and return
        the EmptyPath.
        
        May also fail and return EmptyPath if this path's type cannot possess
        a child of the type encoded in ``element`` .
        
        
        Parameters
        ----------
        element : str
        
        
        """
    @staticmethod
    def AppendExpression(*args, **kwargs):
        """
        
        AppendExpression() -> Path
        
        
        Creates a path by appending an expression element.
        
        
        This path must be a prim property or relational attribute path.
        
        
        
        """
    @staticmethod
    def AppendMapper(*args, **kwargs):
        """
        
        AppendMapper(targetPath) -> Path
        
        
        Creates a path by appending a mapper element for ``targetPath`` .
        
        
        This path must be a prim property or relational attribute path.
        
        
        Parameters
        ----------
        targetPath : Path
        
        
        """
    @staticmethod
    def AppendMapperArg(*args, **kwargs):
        """
        
        AppendMapperArg(argName) -> Path
        
        
        Creates a path by appending an element for ``argName`` .
        
        
        This path must be a mapper path.
        
        
        Parameters
        ----------
        argName : str
        
        
        """
    @staticmethod
    def AppendPath(*args, **kwargs):
        """
        
        AppendPath(newSuffix) -> Path
        
        
        Creates a path by appending a given relative path to this path.
        
        
        If the newSuffix is a prim path, then this path must be a prim path or
        a root path.
        
        If the newSuffix is a prim property path, then this path must be a
        prim path or the ReflexiveRelativePath.
        
        
        Parameters
        ----------
        newSuffix : Path
        
        
        """
    @staticmethod
    def AppendProperty(*args, **kwargs):
        """
        
        AppendProperty(propName) -> Path
        
        
        Creates a path by appending an element for ``propName`` to this path.
        
        
        This path must be a prim path or the ReflexiveRelativePath.
        
        
        Parameters
        ----------
        propName : str
        
        
        """
    @staticmethod
    def AppendRelationalAttribute(*args, **kwargs):
        """
        
        AppendRelationalAttribute(attrName) -> Path
        
        
        Creates a path by appending an element for ``attrName`` to this path.
        
        
        This path must be a target path.
        
        
        Parameters
        ----------
        attrName : str
        
        
        """
    @staticmethod
    def AppendTarget(*args, **kwargs):
        """
        
        AppendTarget(targetPath) -> Path
        
        
        Creates a path by appending an element for ``targetPath`` .
        
        
        This path must be a prim property or relational attribute path.
        
        
        Parameters
        ----------
        targetPath : Path
        
        
        """
    @staticmethod
    def AppendVariantSelection(*args, **kwargs):
        """
        
        AppendVariantSelection(variantSet, variant) -> Path
        
        
        Creates a path by appending an element for ``variantSet`` and
        ``variant`` to this path.
        
        
        This path must be a prim path.
        
        
        Parameters
        ----------
        variantSet : str
        
        variant : str
        
        
        """
    @staticmethod
    def ContainsPrimVariantSelection(*args, **kwargs):
        """
        
        ContainsPrimVariantSelection() -> bool
        
        
        Returns whether the path or any of its parent paths identifies a
        variant selection for a prim.
        
        
        
        """
    @staticmethod
    def ContainsPropertyElements(*args, **kwargs):
        """
        
        ContainsPropertyElements() -> bool
        
        
        Return true if this path contains any property elements, false
        otherwise.
        
        
        A false return indicates a prim-like path, specifically a root path, a
        prim path, or a prim variant selection path. A true return indicates a
        property-like path: a prim property path, a target path, a relational
        attribute path, etc.
        
        
        
        """
    @staticmethod
    def ContainsTargetPath(*args, **kwargs):
        """
        
        ContainsTargetPath() -> bool
        
        
        Return true if this path is or has a prefix that's a target path or a
        mapper path.
        
        
        
        """
    @staticmethod
    def FindLongestPrefix(*args, **kwargs):
        ...
    @staticmethod
    def FindLongestStrictPrefix(*args, **kwargs):
        ...
    @staticmethod
    def FindPrefixedRange(*args, **kwargs):
        ...
    @staticmethod
    def GetAbsoluteRootOrPrimPath(*args, **kwargs):
        """
        
        GetAbsoluteRootOrPrimPath() -> Path
        
        
        Creates a path by stripping all properties and relational attributes
        from this path, leaving the path to the containing prim.
        
        
        If the path is already a prim or absolute root path, the same path is
        returned.
        
        
        
        """
    @staticmethod
    def GetAllTargetPathsRecursively(*args, **kwargs):
        """
        
        GetAllTargetPathsRecursively(result) -> None
        
        
        Returns all the relationship target or connection target paths
        contained in this path, and recursively all the target paths contained
        in those target paths in reverse depth-first order.
        
        
        For example, given the
        path:'/A/B.a[/C/D.a[/E/F.a]].a[/A/B.a[/C/D.a]]'this method
        produces:'/A/B.a[/C/D.a]','/C/D.a','/C/D.a[/E/F.a]','/E/F.a'
        
        
        Parameters
        ----------
        result : list[Path]
        
        
        """
    @staticmethod
    def GetAncestorsRange(*args, **kwargs):
        """
        
        GetAncestorsRange() -> SdfPathAncestorsRange
        
        
        Return a range for iterating over the ancestors of this path.
        
        
        The range provides iteration over the prefixes of a path, ordered from
        longest to shortest (the opposite of the order of the prefixes
        returned by GetPrefixes).
        
        
        
        """
    @staticmethod
    def GetCommonPrefix(*args, **kwargs):
        """
        
        GetCommonPrefix(path) -> Path
        
        
        Returns a path with maximal length that is a prefix path of both this
        path and ``path`` .
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetConciseRelativePaths(*args, **kwargs):
        """
        
        **classmethod** GetConciseRelativePaths(paths) -> list[Path]
        
        
        Given some vector of paths, get a vector of concise unambiguous
        relative paths.
        
        
        GetConciseRelativePaths requires a vector of absolute paths. It finds
        a set of relative paths such that each relative path is unique.
        
        
        Parameters
        ----------
        paths : list[Path]
        
        
        """
    @staticmethod
    def GetParentPath(*args, **kwargs):
        """
        
        GetParentPath() -> Path
        
        
        Return the path that identifies this path's namespace parent.
        
        
        For a prim path (like'/foo/bar'), return the prim's parent's path
        ('/foo'). For a prim property path (like'/foo/bar.property'), return
        the prim's path ('/foo/bar'). For a target path
        (like'/foo/bar.property[/target]') return the property path
        ('/foo/bar.property'). For a mapper path
        (like'/foo/bar.property.mapper[/target]') return the property path
        ('/foo/bar.property). For a relational attribute path
        (like'/foo/bar.property[/target].relAttr') return the relationship
        target's path ('/foo/bar.property[/target]'). For a prim variant
        selection path (like'/foo/bar{var=sel}') return the prim path
        ('/foo/bar'). For a root prim path (like'/rootPrim'), return
        AbsoluteRootPath() ('/'). For a single element relative prim path
        (like'relativePrim'), return ReflexiveRelativePath() ('.'). For
        ReflexiveRelativePath() , return the relative parent path ('\\.\\.').
        
        Note that the parent path of a relative parent path ('\\.\\.') is a
        relative grandparent path ('\\.\\./\\.\\.'). Use caution writing loops
        that walk to parent paths since relative paths have infinitely many
        ancestors. To more safely traverse ancestor paths, consider iterating
        over an SdfPathAncestorsRange instead, as returend by
        GetAncestorsRange() .
        
        
        
        """
    @staticmethod
    def GetPrefixes(*args, **kwargs):
        """
        
        
        Returns the prefix paths of this path.
        """
    @staticmethod
    def GetPrimOrPrimVariantSelectionPath(*args, **kwargs):
        """
        
        GetPrimOrPrimVariantSelectionPath() -> Path
        
        
        Creates a path by stripping all relational attributes, targets, and
        properties, leaving the nearest path for which
        *IsPrimOrPrimVariantSelectionPath()* returns true.
        
        
        See *GetPrimPath* also.
        
        If the path is already a prim or a prim variant selection path, the
        same path is returned.
        
        
        
        """
    @staticmethod
    def GetPrimPath(*args, **kwargs):
        """
        
        GetPrimPath() -> Path
        
        
        Creates a path by stripping all relational attributes, targets,
        properties, and variant selections from the leafmost prim path,
        leaving the nearest path for which *IsPrimPath()* returns true.
        
        
        See *GetPrimOrPrimVariantSelectionPath* also.
        
        If the path is already a prim path, the same path is returned.
        
        
        
        """
    @staticmethod
    def GetVariantSelection(*args, **kwargs):
        """
        
        GetVariantSelection() -> tuple[str, str]
        
        
        Returns the variant selection for this path, if this is a variant
        selection path.
        
        
        Returns a pair of empty strings if this path is not a variant
        selection path.
        
        
        
        """
    @staticmethod
    def HasPrefix(*args, **kwargs):
        """
        
        HasPrefix(prefix) -> bool
        
        
        Return true if both this path and *prefix* are not the empty path and
        this path has *prefix* as a prefix.
        
        
        Return false otherwise.
        
        
        Parameters
        ----------
        prefix : Path
        
        
        """
    @staticmethod
    def IsAbsolutePath(*args, **kwargs):
        """
        
        IsAbsolutePath() -> bool
        
        
        Returns whether the path is absolute.
        
        
        
        """
    @staticmethod
    def IsAbsoluteRootOrPrimPath(*args, **kwargs):
        """
        
        IsAbsoluteRootOrPrimPath() -> bool
        
        
        Returns whether the path identifies a prim or the absolute root.
        
        
        
        """
    @staticmethod
    def IsAbsoluteRootPath(*args, **kwargs):
        """
        
        IsAbsoluteRootPath() -> bool
        
        
        Return true if this path is the AbsoluteRootPath() .
        
        
        
        """
    @staticmethod
    def IsExpressionPath(*args, **kwargs):
        """
        
        IsExpressionPath() -> bool
        
        
        Returns whether the path identifies a connection expression.
        
        
        
        """
    @staticmethod
    def IsMapperArgPath(*args, **kwargs):
        """
        
        IsMapperArgPath() -> bool
        
        
        Returns whether the path identifies a connection mapper arg.
        
        
        
        """
    @staticmethod
    def IsMapperPath(*args, **kwargs):
        """
        
        IsMapperPath() -> bool
        
        
        Returns whether the path identifies a connection mapper.
        
        
        
        """
    @staticmethod
    def IsNamespacedPropertyPath(*args, **kwargs):
        """
        
        IsNamespacedPropertyPath() -> bool
        
        
        Returns whether the path identifies a namespaced property.
        
        
        A namespaced property has colon embedded in its name.
        
        
        
        """
    @staticmethod
    def IsPrimPath(*args, **kwargs):
        """
        
        IsPrimPath() -> bool
        
        
        Returns whether the path identifies a prim.
        
        
        
        """
    @staticmethod
    def IsPrimPropertyPath(*args, **kwargs):
        """
        
        IsPrimPropertyPath() -> bool
        
        
        Returns whether the path identifies a prim's property.
        
        
        A relational attribute is not a prim property.
        
        
        
        """
    @staticmethod
    def IsPrimVariantSelectionPath(*args, **kwargs):
        """
        
        IsPrimVariantSelectionPath() -> bool
        
        
        Returns whether the path identifies a variant selection for a prim.
        
        
        
        """
    @staticmethod
    def IsPropertyPath(*args, **kwargs):
        """
        
        IsPropertyPath() -> bool
        
        
        Returns whether the path identifies a property.
        
        
        A relational attribute is considered to be a property, so this method
        will return true for relational attributes as well as properties of
        prims.
        
        
        
        """
    @staticmethod
    def IsRelationalAttributePath(*args, **kwargs):
        """
        
        IsRelationalAttributePath() -> bool
        
        
        Returns whether the path identifies a relational attribute.
        
        
        If this is true, IsPropertyPath() will also be true.
        
        
        
        """
    @staticmethod
    def IsRootPrimPath(*args, **kwargs):
        """
        
        IsRootPrimPath() -> bool
        
        
        Returns whether the path identifies a root prim.
        
        
        the path must be absolute and have a single element (for example
        ``/foo`` ).
        
        
        
        """
    @staticmethod
    def IsTargetPath(*args, **kwargs):
        """
        
        IsTargetPath() -> bool
        
        
        Returns whether the path identifies a relationship or connection
        target.
        
        
        
        """
    @staticmethod
    def IsValidIdentifier(*args, **kwargs):
        """
        
        **classmethod** IsValidIdentifier(name) -> bool
        
        
        Returns whether ``name`` is a legal identifier for any path component.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def IsValidNamespacedIdentifier(*args, **kwargs):
        """
        
        **classmethod** IsValidNamespacedIdentifier(name) -> bool
        
        
        Returns whether ``name`` is a legal namespaced identifier.
        
        
        This returns ``true`` if IsValidIdentifier() does.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def IsValidPathString(*args, **kwargs):
        """
        
        **classmethod** IsValidPathString(pathString, errMsg) -> bool
        
        
        Return true if ``pathString`` is a valid path string, meaning that
        passing the string to the *SdfPath* constructor will result in a
        valid, non-empty SdfPath.
        
        
        Otherwise, return false and if ``errMsg`` is not None, set the
        pointed-to string to the parse error.
        
        
        Parameters
        ----------
        pathString : str
        
        errMsg : str
        
        
        """
    @staticmethod
    def JoinIdentifier(*args, **kwargs):
        """
        
        **classmethod** JoinIdentifier(names) -> str
        
        
        Join ``names`` into a single identifier using the namespace delimiter.
        
        
        Any empty strings present in ``names`` are ignored when joining.
        
        
        Parameters
        ----------
        names : list[str]
        
        
        
        ----------------------------------------------------------------------
        
        JoinIdentifier(names) -> str
        
        
        Join ``names`` into a single identifier using the namespace delimiter.
        
        
        Any empty strings present in ``names`` are ignored when joining.
        
        
        Parameters
        ----------
        names : list[str]
        
        
        
        ----------------------------------------------------------------------
        
        JoinIdentifier(lhs, rhs) -> str
        
        
        Join ``lhs`` and ``rhs`` into a single identifier using the namespace
        delimiter.
        
        
        Returns ``lhs`` if ``rhs`` is empty and vice verse. Returns an empty
        string if both ``lhs`` and ``rhs`` are empty.
        
        
        Parameters
        ----------
        lhs : str
        
        rhs : str
        
        
        
        ----------------------------------------------------------------------
        
        JoinIdentifier(lhs, rhs) -> str
        
        
        Join ``lhs`` and ``rhs`` into a single identifier using the namespace
        delimiter.
        
        
        Returns ``lhs`` if ``rhs`` is empty and vice verse. Returns an empty
        string if both ``lhs`` and ``rhs`` are empty.
        
        
        Parameters
        ----------
        lhs : str
        
        rhs : str
        
        
        """
    @staticmethod
    def MakeAbsolutePath(*args, **kwargs):
        """
        
        MakeAbsolutePath(anchor) -> Path
        
        
        Returns the absolute form of this path using ``anchor`` as the
        relative basis.
        
        
        ``anchor`` must be an absolute prim path.
        
        If this path is a relative path, resolve it using ``anchor`` as the
        relative basis.
        
        If this path is already an absolute path, just return a copy.
        
        
        Parameters
        ----------
        anchor : Path
        
        
        """
    @staticmethod
    def MakeRelativePath(*args, **kwargs):
        """
        
        MakeRelativePath(anchor) -> Path
        
        
        Returns the relative form of this path using ``anchor`` as the
        relative basis.
        
        
        ``anchor`` must be an absolute prim path.
        
        If this path is an absolute path, return the corresponding relative
        path that is relative to the absolute path given by ``anchor`` .
        
        If this path is a relative path, return the optimal relative path to
        the absolute path given by ``anchor`` . (The optimal relative path
        from a given prim path is the relative path with the least leading
        dot-dots.
        
        
        Parameters
        ----------
        anchor : Path
        
        
        """
    @staticmethod
    def RemoveAncestorPaths(*args, **kwargs):
        """
        
        **classmethod** RemoveAncestorPaths(paths) -> None
        
        
        Remove all elements of *paths* that prefix other elements in *paths*.
        
        
        As a side-effect, the result is left in sorted order.
        
        
        Parameters
        ----------
        paths : list[Path]
        
        
        """
    @staticmethod
    def RemoveCommonSuffix(*args, **kwargs):
        """
        
        RemoveCommonSuffix(otherPath, stopAtRootPrim) -> tuple[Path, Path]
        
        
        Find and remove the longest common suffix from two paths.
        
        
        Returns this path and ``otherPath`` with the longest common suffix
        removed (first and second, respectively). If the two paths have no
        common suffix then the paths are returned as-is. If the paths are
        equal then this returns empty paths for relative paths and absolute
        roots for absolute paths. The paths need not be the same length.
        
        If ``stopAtRootPrim`` is ``true`` then neither returned path will be
        the root path. That, in turn, means that some common suffixes will not
        be removed. For example, if ``stopAtRootPrim`` is ``true`` then the
        paths /A/B and /B will be returned as is. Were it ``false`` then the
        result would be /A and /. Similarly paths /A/B/C and /B/C would return
        /A/B and /B if ``stopAtRootPrim`` is ``true`` but /A and / if it's
        ``false`` .
        
        
        Parameters
        ----------
        otherPath : Path
        
        stopAtRootPrim : bool
        
        
        """
    @staticmethod
    def RemoveDescendentPaths(*args, **kwargs):
        """
        
        **classmethod** RemoveDescendentPaths(paths) -> None
        
        
        Remove all elements of *paths* that are prefixed by other elements in
        *paths*.
        
        
        As a side-effect, the result is left in sorted order.
        
        
        Parameters
        ----------
        paths : list[Path]
        
        
        """
    @staticmethod
    def ReplaceName(*args, **kwargs):
        """
        
        ReplaceName(newName) -> Path
        
        
        Return a copy of this path with its final component changed to
        *newName*.
        
        
        This path must be a prim or property path.
        
        This method is shorthand for path.GetParentPath().AppendChild(newName)
        for prim paths, path.GetParentPath().AppendProperty(newName) for prim
        property paths, and
        path.GetParentPath().AppendRelationalAttribute(newName) for relational
        attribute paths.
        
        Note that only the final path component is ever changed. If the name
        of the final path component appears elsewhere in the path, it will not
        be modified.
        
        Some examples:
        
        ReplaceName('/chars/MeridaGroup','AngusGroup')
        \\->'/chars/AngusGroup'ReplaceName('/Merida.tx','ty')
        \\->'/Merida.ty'ReplaceName('/Merida.tx[targ].tx','ty')
        \\->'/Merida.tx[targ].ty'
        
        
        Parameters
        ----------
        newName : str
        
        
        """
    @staticmethod
    def ReplacePrefix(*args, **kwargs):
        """
        
        ReplacePrefix(oldPrefix, newPrefix, fixTargetPaths) -> Path
        
        
        Returns a path with all occurrences of the prefix path ``oldPrefix``
        replaced with the prefix path ``newPrefix`` .
        
        
        If fixTargetPaths is true, any embedded target paths will also have
        their paths replaced. This is the default.
        
        If this is not a target, relational attribute or mapper path this will
        do zero or one path prefix replacements, if not the number of
        replacements can be greater than one.
        
        
        Parameters
        ----------
        oldPrefix : Path
        
        newPrefix : Path
        
        fixTargetPaths : bool
        
        
        """
    @staticmethod
    def ReplaceTargetPath(*args, **kwargs):
        """
        
        ReplaceTargetPath(newTargetPath) -> Path
        
        
        Replaces the relational attribute's target path.
        
        
        The path must be a relational attribute path.
        
        
        Parameters
        ----------
        newTargetPath : Path
        
        
        """
    @staticmethod
    def StripAllVariantSelections(*args, **kwargs):
        """
        
        StripAllVariantSelections() -> Path
        
        
        Create a path by stripping all variant selections from all components
        of this path, leaving a path with no embedded variant selections.
        
        
        
        """
    @staticmethod
    def StripNamespace(*args, **kwargs):
        """
        
        **classmethod** StripNamespace(name) -> str
        
        
        Returns ``name`` stripped of any namespaces.
        
        
        This does not check the validity of the name; it just attempts to
        remove anything that looks like a namespace.
        
        
        Parameters
        ----------
        name : str
        
        
        
        ----------------------------------------------------------------------
        
        StripNamespace(name) -> str
        
        
        Returns ``name`` stripped of any namespaces.
        
        
        This does not check the validity of the name; it just attempts to
        remove anything that looks like a namespace.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def StripPrefixNamespace(*args, **kwargs):
        """
        
        **classmethod** StripPrefixNamespace(name, matchNamespace) -> tuple[str, bool]
        
        
        Returns ( ``name`` , ``true`` ) where ``name`` is stripped of the
        prefix specified by ``matchNamespace`` if ``name`` indeed starts with
        ``matchNamespace`` .
        
        
        Returns ( ``name`` , ``false`` ) otherwise, with ``name`` unmodified.
        
        This function deals with both the case where ``matchNamespace``
        contains the trailing namespace delimiter':'or not.
        
        
        Parameters
        ----------
        name : str
        
        matchNamespace : str
        
        
        """
    @staticmethod
    def TokenizeIdentifier(*args, **kwargs):
        """
        
        **classmethod** TokenizeIdentifier(name) -> list[str]
        
        
        Tokenizes ``name`` by the namespace delimiter.
        
        
        Returns the empty vector if ``name`` is not a valid namespaced
        identifier.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Constructs the default, empty path.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(path)
        
        
        Creates a path from the given string.
        
        
        If the given string is not a well-formed path, this will raise a Tf
        error. Note that passing an empty std::string() will also raise an
        error; the correct way to get the empty path is SdfPath() .
        
        Internal dot-dots will be resolved by removing the first dot-dot, the
        element preceding it, and repeating until no internal dot-dots remain.
        
        Note that most often new paths are expected to be created by asking
        existing paths to return modified versions of themselves.
        
        
        Parameters
        ----------
        path : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__(primNode)
        
        
        Parameters
        ----------
        primNode : Sdf_PathPrimNode
        
        
        
        ----------------------------------------------------------------------
        
        __init__(primPart, propPart)
        
        
        Parameters
        ----------
        primPart : Sdf_PathPrimNode
        
        propPart : Sdf_PathPropNode
        
        
        
        ----------------------------------------------------------------------
        
        __init__(primPart, propPart)
        
        
        Parameters
        ----------
        primPart : Sdf_PathNode
        
        propPart : Sdf_PathNode
        
        
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def elementString(*args, **kwargs):
        """
        The string representation of the terminal component of this path.
        This path can be reconstructed via 
        thisPath.GetParentPath().AppendElementString(thisPath.element).
        None of absoluteRootPath, reflexiveRelativePath, nor emptyPath
        possess the above quality; their .elementString is the empty string.
        """
    @property
    def isEmpty(*args, **kwargs):
        """
        type : bool
        
        
        Returns true if this is the empty path ( SdfPath::EmptyPath() ).
        """
    @property
    def name(*args, **kwargs):
        """
        The name of the prim, property or relational
        attribute identified by the path.
        
        '' for EmptyPath.  '.' for ReflexiveRelativePath.
        '..' for a path ending in ParentPathElement.
        """
    @property
    def pathElementCount(*args, **kwargs):
        """
        The number of path elements in this path.
        """
    @property
    def pathString(*args, **kwargs):
        """
        The string representation of this path.
        """
    @property
    def targetPath(*args, **kwargs):
        """
        The relational attribute target path for this path.
        
        EmptyPath if this is not a relational attribute path.
        """
class PathArray(Boost.Python.instance):
    """
    An array of type SdfPath.
    """
    _isVtArray: typing.ClassVar[bool] = True
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        
        __init__(values)
        
        values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)
        
        
        
        __init__(values)
        
        values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)
        
        
        
        __init__(values)
        
        values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)
        
        """
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
class PathListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 168
    @staticmethod
    def ApplyOperations(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def Create(*args, **kwargs):
        ...
    @staticmethod
    def CreateExplicit(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class Payload(Boost.Python.instance):
    """
    
    Represents a payload and all its meta data.
    
    A payload represents a prim reference to an external layer. A payload
    is similar to a prim reference (see SdfReference) with the major
    difference that payloads are explicitly loaded by the user.
    
    Unloaded payloads represent a boundary that lazy composition and
    system behaviors will not traverse across, providing a user-visible
    way to manage the working set of the scene.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(assetPath, primPath, layerOffset)
        
        
        Create a payload.
        
        
        See SdfAssetPath for what characters are valid in ``assetPath`` . If
        ``assetPath`` contains invalid characters, issue an error and set this
        payload's asset path to the empty asset path.
        
        
        Parameters
        ----------
        assetPath : str
        
        primPath : Path
        
        layerOffset : LayerOffset
        
        
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
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
    def assetPath(*args, **kwargs):
        """
        type : None
        
        
        Sets a new asset path for the layer the payload uses.
        
        
        See SdfAssetPath for what characters are valid in ``assetPath`` . If
        ``assetPath`` contains invalid characters, issue an error and set this
        payload's asset path to the empty asset path.
        
        ----------------------------------------------------------------------
        
        type : str
        
        
        Returns the asset path of the layer that the payload uses.
        """
    @assetPath.setter
    def assetPath(*args, **kwargs):
        ...
    @property
    def layerOffset(*args, **kwargs):
        """
        type : None
        
        
        Sets a new layer offset.
        
        ----------------------------------------------------------------------
        
        type : LayerOffset
        
        
        Returns the layer offset associated with the payload.
        """
    @layerOffset.setter
    def layerOffset(*args, **kwargs):
        ...
    @property
    def primPath(*args, **kwargs):
        """
        type : None
        
        
        Sets a new prim path for the prim that the payload uses.
        
        ----------------------------------------------------------------------
        
        type : Path
        
        
        Returns the scene path of the prim for the payload.
        """
    @primPath.setter
    def primPath(*args, **kwargs):
        ...
class PayloadListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 168
    @staticmethod
    def ApplyOperations(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def Create(*args, **kwargs):
        ...
    @staticmethod
    def CreateExplicit(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class Permission(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Sdf.PermissionPublic, Sdf.PermissionPrivate)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class PrimSpec(Spec):
    """
    
    Represents a prim description in an SdfLayer object.
    
    Every SdfPrimSpec object is defined in a layer. It is identified by
    its path (SdfPath class) in the namespace hierarchy of its layer.
    SdfPrimSpecs can be created using the New() method as children of
    either the containing SdfLayer itself (for"root level"prims), or as
    children of other SdfPrimSpec objects to extend a hierarchy. The
    helper function SdfCreatePrimInLayer() can be used to quickly create a
    hierarchy of primSpecs.
    
    SdfPrimSpec objects have properties of two general types: attributes
    (containing values) and relationships (different types of connections
    to other prims and attributes). Attributes are represented by the
    SdfAttributeSpec class and relationships by the SdfRelationshipSpec
    class. Each prim has its own namespace of properties. Properties are
    stored and accessed by their name.
    
    SdfPrimSpec objects have a typeName, permission restriction, and they
    reference and inherit prim paths. Permission restrictions control
    which other layers may refer to, or express opinions about a prim. See
    the SdfPermission class for more information.
    
       - Insert doc about references and inherits here.
    
       - Should have validate\\.\\.\\. methods for name, children,
         properties
    
    
    """
    ActiveKey: typing.ClassVar[str] = 'active'
    AnyTypeToken: typing.ClassVar[str] = '__AnyType__'
    CommentKey: typing.ClassVar[str] = 'comment'
    CustomDataKey: typing.ClassVar[str] = 'customData'
    DocumentationKey: typing.ClassVar[str] = 'documentation'
    HiddenKey: typing.ClassVar[str] = 'hidden'
    InheritPathsKey: typing.ClassVar[str] = 'inheritPaths'
    KindKey: typing.ClassVar[str] = 'kind'
    PayloadKey: typing.ClassVar[str] = 'payload'
    PermissionKey: typing.ClassVar[str] = 'permission'
    PrefixKey: typing.ClassVar[str] = 'prefix'
    PrefixSubstitutionsKey: typing.ClassVar[str] = 'prefixSubstitutions'
    PrimOrderKey: typing.ClassVar[str] = 'primOrder'
    PropertyOrderKey: typing.ClassVar[str] = 'propertyOrder'
    ReferencesKey: typing.ClassVar[str] = 'references'
    RelocatesKey: typing.ClassVar[str] = 'relocates'
    SpecializesKey: typing.ClassVar[str] = 'specializes'
    SpecifierKey: typing.ClassVar[str] = 'specifier'
    SymmetricPeerKey: typing.ClassVar[str] = 'symmetricPeer'
    SymmetryArgumentsKey: typing.ClassVar[str] = 'symmetryArguments'
    SymmetryFunctionKey: typing.ClassVar[str] = 'symmetryFunction'
    TypeNameKey: typing.ClassVar[str] = 'typeName'
    VariantSelectionKey: typing.ClassVar[str] = 'variantSelection'
    VariantSetNamesKey: typing.ClassVar[str] = 'variantSetNames'
    @staticmethod
    def ApplyNameChildrenOrder(*args, **kwargs):
        """
        
        ApplyNameChildrenOrder(vec) -> None
        
        
        Reorders the given list of child names according to the reorder
        nameChildren statement for this prim.
        
        
        This routine employs the standard list editing operation for ordered
        items in a ListEditor.
        
        
        Parameters
        ----------
        vec : list[str]
        
        
        """
    @staticmethod
    def ApplyPropertyOrder(*args, **kwargs):
        """
        
        ApplyPropertyOrder(vec) -> None
        
        
        Reorders the given list of property names according to the reorder
        properties statement for this prim.
        
        
        This routine employs the standard list editing operation for ordered
        items in a ListEditor.
        
        
        Parameters
        ----------
        vec : list[str]
        
        
        """
    @staticmethod
    def BlockVariantSelection(*args, **kwargs):
        """
        
        BlockVariantSelection(variantSetName) -> None
        
        
        Blocks the variant selected for the given variant set by setting the
        variant selection to empty.
        
        
        Parameters
        ----------
        variantSetName : str
        
        
        """
    @staticmethod
    def CanSetName(*args, **kwargs):
        """
        
        CanSetName(newName, whyNot) -> bool
        
        
        Returns true if setting the prim spec's name to ``newName`` will
        succeed.
        
        
        Returns false if it won't, and sets ``whyNot`` with a string
        describing why not.
        
        
        Parameters
        ----------
        newName : str
        
        whyNot : str
        
        
        """
    @staticmethod
    def ClearActive(*args, **kwargs):
        """
        
        ClearActive() -> None
        
        
        Removes the active opinion in this prim spec if there is one.
        
        
        
        """
    @staticmethod
    def ClearInstanceable(*args, **kwargs):
        """
        
        ClearInstanceable() -> None
        
        
        Clears the value for the prim's instanceable flag.
        
        
        
        """
    @staticmethod
    def ClearKind(*args, **kwargs):
        """
        
        ClearKind() -> None
        
        
        Remove the kind opinion from this prim spec if there is one.
        
        
        
        """
    @staticmethod
    def ClearPayloadList(*args, **kwargs):
        """
        
        
        Clears the payloads for this prim.
        """
    @staticmethod
    def ClearReferenceList(*args, **kwargs):
        """
        
        
        Clears the references for this prim.
        """
    @staticmethod
    def GetAttributeAtPath(*args, **kwargs):
        """
        
        GetAttributeAtPath(path) -> AttributeSpec
        
        
        Returns an attribute given its ``path`` .
        
        
        Returns invalid handle if there is no attribute at ``path`` . This is
        simply a more specifically typed version of GetObjectAtPath.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetObjectAtPath(*args, **kwargs):
        """
        
        
        GetObjectAtPath(path) -> object
        
        path: Path
        
        Returns a prim or property given its namespace path.
        
        If path is relative then it will be interpreted as relative to this prim.  If it is absolute then it will be interpreted as absolute in this prim's layer. The return type can be either PrimSpecPtr or PropertySpecPtr.
        """
    @staticmethod
    def GetPrimAtPath(*args, **kwargs):
        """
        
        GetPrimAtPath(path) -> PrimSpec
        
        
        Returns a prim given its ``path`` .
        
        
        Returns invalid handle if there is no prim at ``path`` . This is
        simply a more specifically typed version of GetObjectAtPath.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetPropertyAtPath(*args, **kwargs):
        """
        
        GetPropertyAtPath(path) -> PropertySpec
        
        
        Returns a property given its ``path`` .
        
        
        Returns invalid handle if there is no property at ``path`` . This is
        simply a more specifically typed version of GetObjectAtPath.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetRelationshipAtPath(*args, **kwargs):
        """
        
        GetRelationshipAtPath(path) -> RelationshipSpec
        
        
        Returns a relationship given its ``path`` .
        
        
        Returns invalid handle if there is no relationship at ``path`` . This
        is simply a more specifically typed version of GetObjectAtPath.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def GetVariantNames(*args, **kwargs):
        """
        
        GetVariantNames(name) -> list[str]
        
        
        Returns list of variant names for the given variant set.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def HasActive(*args, **kwargs):
        """
        
        HasActive() -> bool
        
        
        Returns true if this prim spec has an opinion about active.
        
        
        
        """
    @staticmethod
    def HasInstanceable(*args, **kwargs):
        """
        
        HasInstanceable() -> bool
        
        
        Returns true if this prim spec has a value authored for its
        instanceable flag, false otherwise.
        
        
        
        """
    @staticmethod
    def HasKind(*args, **kwargs):
        """
        
        HasKind() -> bool
        
        
        Returns true if this prim spec has an opinion about kind.
        
        
        
        """
    @staticmethod
    def RemoveProperty(*args, **kwargs):
        """
        
        RemoveProperty(property) -> None
        
        
        Removes the property.
        
        
        Parameters
        ----------
        property : PropertySpec
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __new__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def active(*args, **kwargs):
        """
        Whether this prim spec is active.
        The default value is true.
        """
    @active.setter
    def active(*args, **kwargs):
        ...
    @property
    def assetInfo(*args, **kwargs):
        """
        Returns the asset info dictionary for this prim.
        
        The default value is an empty dictionary.
        
        The asset info dictionary is used to annotate prims representing the root-prims of assets (generally organized as models) with various data related to asset management. For example, asset name, root layer identifier, asset version etc.
        """
    @assetInfo.setter
    def assetInfo(*args, **kwargs):
        ...
    @property
    def attributes(*args, **kwargs):
        """
        The attributes of this prim, as an ordered dictionary.
        """
    @property
    def comment(*args, **kwargs):
        """
        The prim's comment string.
        """
    @comment.setter
    def comment(*args, **kwargs):
        ...
    @property
    def customData(*args, **kwargs):
        """
        The custom data for this prim.
        
        The default value for custom data is an empty dictionary.
        
        Custom data is for use by plugins or other non-tools supplied 
        extensions that need to be able to store data attached to arbitrary
        scene objects.  Note that if the only objects you want to store data
        on are prims, using custom attributes is probably a better choice.
        But if you need to possibly store this data on attributes or 
        relationships or as annotations on reference arcs, then custom data
        is an appropriate choice.
        """
    @customData.setter
    def customData(*args, **kwargs):
        ...
    @property
    def documentation(*args, **kwargs):
        """
        The prim's documentation string.
        """
    @documentation.setter
    def documentation(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
    @property
    def hasPayloads(*args, **kwargs):
        """
        Returns true if this prim has payloads set.
        """
    @property
    def hasReferences(*args, **kwargs):
        """
        Returns true if this prim has references set.
        """
    @property
    def hidden(*args, **kwargs):
        """
        Whether this prim spec will be hidden in browsers.
        The default value is false.
        """
    @hidden.setter
    def hidden(*args, **kwargs):
        ...
    @property
    def inheritPathList(*args, **kwargs):
        """
        A PathListEditor for the prim's inherit paths.
        
        The list of the inherit paths for this prim may be modified with this PathListEditor.
        
        A PathListEditor may express a list either as an explicit value or as a set of list editing operations.  See PathListEditor for more information.
        """
    @property
    def instanceable(*args, **kwargs):
        """
        Whether this prim spec is flagged as instanceable.
        The default value is false.
        """
    @instanceable.setter
    def instanceable(*args, **kwargs):
        ...
    @property
    def kind(*args, **kwargs):
        """
        What kind of model this prim spec represents, if any.
        The default is an empty string
        """
    @kind.setter
    def kind(*args, **kwargs):
        ...
    @property
    def name(*args, **kwargs):
        """
        The prim's name.
        """
    @name.setter
    def name(*args, **kwargs):
        ...
    @property
    def nameChildren(*args, **kwargs):
        """
        The prim name children of this prim, as an ordered dictionary.
        
        Note that although this property is described as being read-only, you can modify the contents to add, remove, or reorder children.
        """
    @property
    def nameChildrenOrder(*args, **kwargs):
        """
        Get/set the list of child names for this prim's 'reorder nameChildren' statement.
        """
    @nameChildrenOrder.setter
    def nameChildrenOrder(*args, **kwargs):
        ...
    @property
    def nameParent(*args, **kwargs):
        """
        The name parent of this prim.
        """
    @property
    def nameRoot(*args, **kwargs):
        """
        The name pseudo-root of this prim.
        """
    @property
    def payloadList(*args, **kwargs):
        """
        A PayloadListEditor for the prim's payloads.
        
        The list of the payloads for this prim may be modified with this PayloadListEditor.
        
        A PayloadListEditor may express a list either as an explicit value or as a set of list editing operations.  See PayloadListEditor for more information.
        """
    @property
    def permission(*args, **kwargs):
        """
        The prim's permission restriction.
        The default value is SdfPermissionPublic.
        """
    @permission.setter
    def permission(*args, **kwargs):
        ...
    @property
    def prefix(*args, **kwargs):
        """
        The prim's prefix.
        """
    @prefix.setter
    def prefix(*args, **kwargs):
        ...
    @property
    def prefixSubstitutions(*args, **kwargs):
        """
        Dictionary of prefix substitutions.
        """
    @prefixSubstitutions.setter
    def prefixSubstitutions(*args, **kwargs):
        ...
    @property
    def properties(*args, **kwargs):
        """
        The properties of this prim, as an ordered dictionary.
        
        Note that although this property is described as being read-only, you can modify the contents to add, remove, or reorder properties.
        """
    @property
    def propertyOrder(*args, **kwargs):
        """
        Get/set the list of property names for this prim's 'reorder properties' statement.
        """
    @propertyOrder.setter
    def propertyOrder(*args, **kwargs):
        ...
    @property
    def realNameParent(*args, **kwargs):
        """
        The name parent of this prim.
        """
    @property
    def referenceList(*args, **kwargs):
        """
        A ReferenceListEditor for the prim's references.
        
        The list of the references for this prim may be modified with this ReferenceListEditor.
        
        A ReferenceListEditor may express a list either as an explicit value or as a set of list editing operations.  See ReferenceListEditor for more information.
        """
    @property
    def relationships(*args, **kwargs):
        """
        The relationships of this prim, as an ordered dictionary.
        """
    @property
    def relocates(*args, **kwargs):
        """
        An editing proxy for the prim's map of relocation paths.
        
        The map of source-to-target paths specifying namespace relocation may be set or cleared whole, or individual map entries may be added, removed, or edited.
        """
    @relocates.setter
    def relocates(*args, **kwargs):
        ...
    @property
    def specializesList(*args, **kwargs):
        """
        A PathListEditor for the prim's specializes.
        
        The list of the specializes for this prim may be modified with this PathListEditor.
        
        A PathListEditor may express a list either as an explicit value or as a set of list editing operations.  See PathListEditor for more information.
        """
    @property
    def specifier(*args, **kwargs):
        """
        The prim's specifier (SpecifierDef or SpecifierOver).
        The default value is SpecifierOver.
        """
    @specifier.setter
    def specifier(*args, **kwargs):
        ...
    @property
    def suffix(*args, **kwargs):
        """
        The prim's suffix.
        """
    @suffix.setter
    def suffix(*args, **kwargs):
        ...
    @property
    def suffixSubstitutions(*args, **kwargs):
        """
        Dictionary of prefix substitutions.
        """
    @suffixSubstitutions.setter
    def suffixSubstitutions(*args, **kwargs):
        ...
    @property
    def symmetricPeer(*args, **kwargs):
        """
        The prims's symmetric peer.
        """
    @symmetricPeer.setter
    def symmetricPeer(*args, **kwargs):
        ...
    @property
    def symmetryArguments(*args, **kwargs):
        """
        Dictionary with prim symmetry arguments.
        
        Although this property is marked read-only, you can modify the contents to add, change, and clear symmetry arguments.
        """
    @symmetryArguments.setter
    def symmetryArguments(*args, **kwargs):
        ...
    @property
    def symmetryFunction(*args, **kwargs):
        """
        The prim's symmetry function.
        """
    @symmetryFunction.setter
    def symmetryFunction(*args, **kwargs):
        ...
    @property
    def typeName(*args, **kwargs):
        """
        The type of this prim.
        """
    @typeName.setter
    def typeName(*args, **kwargs):
        ...
    @property
    def variantSelections(*args, **kwargs):
        """
        Dictionary whose keys are variant set names and whose values are the variants chosen for each set.
        
        Although this property is marked read-only, you can modify the contents to add, change, and clear variants.
        """
    @property
    def variantSetNameList(*args, **kwargs):
        """
        A StringListEditor for the names of the variant 
        sets for this prim.
        
        The list of the names of the variants sets of this prim may be
        modified with this StringListEditor.
        
        A StringListEditor may express a list either as an explicit value or as a set of list editing operations.  See StringListEditor for more information.
        
        Although this property is marked as read-only, the returned object is modifiable.
        """
    @property
    def variantSets(*args, **kwargs):
        """
        The VariantSetSpecs for this prim indexed by name.
        
        Although this property is marked as read-only, you can 
        modify the contents to remove variant sets.  New variant sets 
        are created by creating them with the prim as the owner.
        
        Although this property is marked as read-only, the returned object
        is modifiable.
        """
class PropertySpec(Spec):
    """
    
    Base class for SdfAttributeSpec and SdfRelationshipSpec.
    
    Scene Spec Attributes (SdfAttributeSpec) and Relationships
    (SdfRelationshipSpec) are the basic properties that make up Scene Spec
    Prims (SdfPrimSpec). They share many qualities and can sometimes be
    treated uniformly. The common qualities are provided by this base
    class.
    
    NOTE: Do not use Python reserved words and keywords as attribute
    names. This will cause attribute resolution to fail.
    
    """
    AssetInfoKey: typing.ClassVar[str] = 'assetInfo'
    CommentKey: typing.ClassVar[str] = 'comment'
    CustomDataKey: typing.ClassVar[str] = 'customData'
    CustomKey: typing.ClassVar[str] = 'custom'
    DisplayGroupKey: typing.ClassVar[str] = 'displayGroup'
    DisplayNameKey: typing.ClassVar[str] = 'displayName'
    DocumentationKey: typing.ClassVar[str] = 'documentation'
    HiddenKey: typing.ClassVar[str] = 'hidden'
    PermissionKey: typing.ClassVar[str] = 'permission'
    PrefixKey: typing.ClassVar[str] = 'prefix'
    SymmetricPeerKey: typing.ClassVar[str] = 'symmetricPeer'
    SymmetryArgumentsKey: typing.ClassVar[str] = 'symmetryArguments'
    SymmetryFunctionKey: typing.ClassVar[str] = 'symmetryFunction'
    @staticmethod
    def ClearDefaultValue(*args, **kwargs):
        """
        
        ClearDefaultValue() -> None
        
        
        Clear the attribute's default value.
        
        
        
        """
    @staticmethod
    def HasDefaultValue(*args, **kwargs):
        """
        
        HasDefaultValue() -> bool
        
        
        Returns true if a default value is set for this attribute.
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
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
    def assetInfo(*args, **kwargs):
        """
        Returns the asset info dictionary for this property.
        
        The default value is an empty dictionary.
        
        The asset info dictionary is used to annotate SdfAssetPath-valued attributes pointing to the root-prims of assets (generally organized as models) with various data related to asset management. For example, asset name, root layer identifier, asset version etc.
        
        Note: It is only valid to author assetInfo on attributes that are of type SdfAssetPath.
        """
    @assetInfo.setter
    def assetInfo(*args, **kwargs):
        ...
    @property
    def comment(*args, **kwargs):
        """
        A comment describing the property.
        """
    @comment.setter
    def comment(*args, **kwargs):
        ...
    @property
    def custom(*args, **kwargs):
        """
        Whether this property spec declares a custom attribute.
        """
    @custom.setter
    def custom(*args, **kwargs):
        ...
    @property
    def customData(*args, **kwargs):
        """
        The property's custom data.
        
        The default value for custom data is an empty dictionary.
        
        Custom data is for use by plugins or other non-tools supplied 
        extensions that need to be able to store data attached to arbitrary
        scene objects.  Note that if the only objects you want to store data
        on are prims, using custom attributes is probably a better choice.
        But if you need to possibly store this data on attributes or 
        relationships or as annotations on reference arcs, then custom data
        is an appropriate choice.
        """
    @customData.setter
    def customData(*args, **kwargs):
        ...
    @property
    def default(*args, **kwargs):
        """
        The default value of this property.
        """
    @default.setter
    def default(*args, **kwargs):
        ...
    @property
    def displayGroup(*args, **kwargs):
        """
        DisplayGroup for the property.
        """
    @displayGroup.setter
    def displayGroup(*args, **kwargs):
        ...
    @property
    def displayName(*args, **kwargs):
        """
        DisplayName for the property.
        """
    @displayName.setter
    def displayName(*args, **kwargs):
        ...
    @property
    def documentation(*args, **kwargs):
        """
        Documentation for the property.
        """
    @documentation.setter
    def documentation(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
    @property
    def hasOnlyRequiredFields(*args, **kwargs):
        """
        Indicates whether this spec has any significant data other 
        than just what is necessary for instantiation.
        
        This is a less strict version of isInert, returning True if 
        the spec contains as much as the type and name.
        """
    @property
    def hidden(*args, **kwargs):
        """
        Whether this property will be hidden in browsers.
        """
    @hidden.setter
    def hidden(*args, **kwargs):
        ...
    @property
    def name(*args, **kwargs):
        """
        The name of the property.
        """
    @name.setter
    def name(*args, **kwargs):
        ...
    @property
    def owner(*args, **kwargs):
        """
        The owner of this property.  Either a relationship or a prim.
        """
    @property
    def permission(*args, **kwargs):
        """
        The property's permission restriction.
        """
    @permission.setter
    def permission(*args, **kwargs):
        ...
    @property
    def prefix(*args, **kwargs):
        """
        Prefix for the property.
        """
    @prefix.setter
    def prefix(*args, **kwargs):
        ...
    @property
    def symmetricPeer(*args, **kwargs):
        """
        The property's symmetric peer.
        """
    @symmetricPeer.setter
    def symmetricPeer(*args, **kwargs):
        ...
    @property
    def symmetryArguments(*args, **kwargs):
        """
        Dictionary with property symmetry arguments.
        
        Although this property is marked read-only, you can modify the contents to add, change, and clear symmetry arguments.
        """
    @symmetryArguments.setter
    def symmetryArguments(*args, **kwargs):
        ...
    @property
    def symmetryFunction(*args, **kwargs):
        """
        The property's symmetry function.
        """
    @symmetryFunction.setter
    def symmetryFunction(*args, **kwargs):
        ...
    @property
    def variability(*args, **kwargs):
        """
        Returns the variability of the property.
        
        An attribute's variability may be Varying
        Uniform, Config or Computed.
        For an attribute, the default is Varying, for a relationship the default is Uniform.
        
        Varying relationships may be directly authored 'animating' targetpaths over time.
        Varying attributes may be directly authored, animated and 
        affected on by Actions.  They are the most flexible.
        
        Uniform attributes may be authored only with non-animated values
        (default values).  They cannot be affected by Actions, but they
        can be connected to other Uniform attributes.
        
        Config attributes are the same as Uniform except that a Prim
        can choose to alter its collection of built-in properties based
        on the values of its Config attributes.
        
        Computed attributes may not be authored in scene description.
        Prims determine the values of their Computed attributes through
        Prim-specific computation.  They may not be connected.
        """
class PseudoRootSpec(PrimSpec):
    """
    """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
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
    def expired(*args, **kwargs):
        ...
class Reference(Boost.Python.instance):
    """
    
    Represents a reference and all its meta data.
    
    A reference is expressed on a prim in a given layer and it identifies
    a prim in a layer stack. All opinions in the namespace hierarchy under
    the referenced prim will be composed with the opinions in the
    namespace hierarchy under the referencing prim.
    
    The asset path specifies the layer stack being referenced. If this
    asset path is non-empty, this reference is considered
    an'external'reference to the layer stack rooted at the specified
    layer. If this is empty, this reference is considered
    an'internal'reference to the layer stack containing (but not
    necessarily rooted at) the layer where the reference is authored.
    
    The prim path specifies the prim in the referenced layer stack from
    which opinions will be composed. If this prim path is empty, it will
    be considered a reference to the default prim specified in the root
    layer of the referenced layer stack  see SdfLayer::GetDefaultPrim.
    
    The meta data for a reference is its layer offset and custom data. The
    layer offset is an affine transformation applied to all anim splines
    in the referenced prim's namespace hierarchy, see SdfLayerOffset for
    details. Custom data is for use by plugins or other non-tools supplied
    extensions that need to be able to store data associated with
    references.
    
    """
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def IsInternal(*args, **kwargs):
        """
        
        IsInternal() -> bool
        
        
        Returns ``true`` in the case of an internal reference.
        
        
        An internal reference is a reference with an empty asset path.
        
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(assetPath, primPath, layerOffset, customData)
        
        
        Creates a reference with all its meta data.
        
        
        The default reference is an internal reference to the default prim.
        See SdfAssetPath for what characters are valid in ``assetPath`` . If
        ``assetPath`` contains invalid characters, issue an error and set this
        reference's asset path to the empty asset path.
        
        
        Parameters
        ----------
        assetPath : str
        
        primPath : Path
        
        layerOffset : LayerOffset
        
        customData : VtDictionary
        
        
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
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
    def assetPath(*args, **kwargs):
        """
        type : None
        
        
        Sets the asset path for the root layer of the referenced layer stack.
        
        
        This may be set to an empty string to specify an internal reference.
        See SdfAssetPath for what characters are valid in ``assetPath`` . If
        ``assetPath`` contains invalid characters, issue an error and set this
        reference's asset path to the empty asset path.
        
        ----------------------------------------------------------------------
        
        type : str
        
        
        Returns the asset path to the root layer of the referenced layer
        stack.
        
        
        This will be empty in the case of an internal reference.
        """
    @property
    def customData(*args, **kwargs):
        """
        type : None
        
        
        Sets the custom data associated with the reference.
        
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Sets a custom data entry for the reference.
        
        
        If *value* is empty, then this removes the given custom data entry.
        
        ----------------------------------------------------------------------
        
        type : VtDictionary
        
        
        Returns the custom data associated with the reference.
        """
    @property
    def layerOffset(*args, **kwargs):
        """
        type : None
        
        
        Sets a new layer offset.
        
        ----------------------------------------------------------------------
        
        type : LayerOffset
        
        
        Returns the layer offset associated with the reference.
        """
    @property
    def primPath(*args, **kwargs):
        """
        type : None
        
        
        Sets the path of the referenced prim.
        
        
        This may be set to an empty path to specify a reference to the default
        prim in the referenced layer stack.
        
        ----------------------------------------------------------------------
        
        type : Path
        
        
        Returns the path of the referenced prim.
        
        
        This will be empty if the referenced prim is the default prim
        specified in the referenced layer stack.
        """
class ReferenceListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 168
    @staticmethod
    def ApplyOperations(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def Create(*args, **kwargs):
        ...
    @staticmethod
    def CreateExplicit(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class RelationshipSpec(PropertySpec):
    """
    
    A property that contains a reference to one or more SdfPrimSpec
    instances.
    
    A relationship may refer to one or more target prims or attributes.
    All targets of a single relationship are considered to be playing the
    same role. Note that ``role`` does not imply that the target prims or
    attributes are of the same ``type`` .
    
    Relationships may be annotated with relational attributes. Relational
    attributes are named SdfAttributeSpec objects containing values that
    describe the relationship. For example, point weights are commonly
    expressed as relational attributes.
    
    """
    TargetsKey: typing.ClassVar[str] = 'targetPaths'
    @staticmethod
    def RemoveTargetPath(*args, **kwargs):
        """
        
        RemoveTargetPath(path, preserveTargetOrder) -> None
        
        
        Removes the specified target path.
        
        
        Removes the given target path and any relational attributes for the
        given target path. If ``preserveTargetOrder`` is ``true`` , Erase() is
        called on the list editor instead of RemoveItemEdits(). This preserves
        the ordered items list.
        
        
        Parameters
        ----------
        path : Path
        
        preserveTargetOrder : bool
        
        
        """
    @staticmethod
    def ReplaceTargetPath(*args, **kwargs):
        """
        
        ReplaceTargetPath(oldPath, newPath) -> None
        
        
        Updates the specified target path.
        
        
        Replaces the path given by ``oldPath`` with the one specified by
        ``newPath`` . Relational attributes are updated if necessary.
        
        
        Parameters
        ----------
        oldPath : Path
        
        newPath : Path
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __new__(*args, **kwargs):
        """
        
        
        __init__(ownerPrimSpec, name, custom = True, variability = Sd.VariabilityUniform)
        ownerPrimSpec: PrimSpec
        name : string
        custom : bool
        varibility : Sd.Variability
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
    @property
    def noLoadHint(*args, **kwargs):
        """
        whether the target must be loaded to load the prim this
        relationship is attached to.
        """
    @noLoadHint.setter
    def noLoadHint(*args, **kwargs):
        ...
    @property
    def targetPathList(*args, **kwargs):
        """
        A PathListEditor for the relationship's target paths.
        
        The list of the target paths for this relationship may be
        modified with this PathListEditor.
        
        A PathListEditor may express a list either as an explicit 
        value or as a set of list editing operations.  See PathListEditor 
        for more information.
        """
class Spec(Boost.Python.instance):
    """
    
    Base class for all Sdf spec classes.
    
    """
    @staticmethod
    def ClearInfo(*args, **kwargs):
        """
        
        
        ClearInfo(key)
        
        key : string
        nClears the value for scene spec info with the given key. After calling this, HasInfo() will return false. To make HasInfo() return true, set a value for that scene spec info.
        """
    @staticmethod
    def GetAsText(*args, **kwargs):
        ...
    @staticmethod
    def GetFallbackForInfo(*args, **kwargs):
        """
        
        
        GetFallbackForInfo(key)
        
        key : string
        
        Returns the fallback value for the given key. 
        """
    @staticmethod
    def GetInfo(*args, **kwargs):
        """
        
        GetInfo(key) -> VtValue
        
        
        Gets the value for the given metadata key.
        
        
        This is interim API which is likely to change. Only editors with an
        immediate specific need (like the Inspector) should use this API.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def GetMetaDataDisplayGroup(*args, **kwargs):
        """
        
        GetMetaDataDisplayGroup(key) -> str
        
        
        Returns this metadata key's displayGroup.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def GetMetaDataInfoKeys(*args, **kwargs):
        """
        
        GetMetaDataInfoKeys() -> list[str]
        
        
        Returns the list of metadata info keys for this object.
        
        
        This is not the complete list of keys, it is only those that should be
        considered to be metadata by inspectors or other presentation UI.
        
        This is interim API which is likely to change. Only editors with an
        immediate specific need (like the Inspector) should use this API.
        
        
        
        """
    @staticmethod
    def GetTypeForInfo(*args, **kwargs):
        """
        
        
        GetTypeForInfo(key)
        
        key : string
        
        Returns the type of value for the given key. 
        """
    @staticmethod
    def HasInfo(*args, **kwargs):
        """
        
        
        HasInfo(key) -> bool
        
        key : string
        
        Returns whether there is a setting for the scene spec info with the given key.
        
        When asked for a value for one of its scene spec info, a valid value will always be returned. But if this API returns false for a scene spec info, the value of that info will be the defined default value. 
        
        (XXX: This may change such that it is an error to ask for a value when there is none).
        
        When dealing with a composedLayer, it is not necessary to worry about whether a scene spec info 'has a value' because the composed layer will always have a valid value, even if it is the default.
        
        A spec may or may not have an expressed value for some of its scene spec info.
        """
    @staticmethod
    def IsInert(*args, **kwargs):
        """
        
        
        Indicates whether this spec has any significant data. If ignoreChildren is true, child scenegraph objects will be ignored.
        """
    @staticmethod
    def ListInfoKeys(*args, **kwargs):
        """
        
        ListInfoKeys() -> list[str]
        
        
        Returns the full list of info keys currently set on this object.
        
        
        
        This does not include fields that represent names of children.
        
        
        
        """
    @staticmethod
    def SetInfo(*args, **kwargs):
        """
        
        SetInfo(key, value) -> None
        
        
        Sets the value for the given metadata key.
        
        
        It is an error to pass a value that is not the correct type for that
        given key.
        
        This is interim API which is likely to change. Only editors with an
        immediate specific need (like the Inspector) should use this API.
        
        
        Parameters
        ----------
        key : str
        
        value : VtValue
        
        
        """
    @staticmethod
    def SetInfoDictionaryValue(*args, **kwargs):
        """
        
        SetInfoDictionaryValue(dictionaryKey, entryKey, value) -> None
        
        
        Sets the value for ``entryKey`` to ``value`` within the dictionary
        with the given metadata key ``dictionaryKey`` .
        
        
        Parameters
        ----------
        dictionaryKey : str
        
        entryKey : str
        
        value : VtValue
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
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
    def expired(*args, **kwargs):
        ...
    @property
    def isInert(*args, **kwargs):
        """
        Indicates whether this spec has any significant data. This is for backwards compatibility, use IsInert instead.
        
        Compatibility note: prior to presto 1.9, isInert (then isEmpty) was true for otherwise inert PrimSpecs with inert inherits, references, or variant sets. isInert is now false in such conditions.
        """
    @property
    def layer(*args, **kwargs):
        """
        The owning layer.
        """
    @property
    def path(*args, **kwargs):
        """
        The absolute scene path.
        """
class SpecType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Sdf.SpecTypeUnknown, Sdf.SpecTypeAttribute, Sdf.SpecTypeConnection, Sdf.SpecTypeExpression, Sdf.SpecTypeMapper, Sdf.SpecTypeMapperArg, Sdf.SpecTypePrim, Sdf.SpecTypePseudoRoot, Sdf.SpecTypeRelationship, Sdf.SpecTypeRelationshipTarget, Sdf.SpecTypeVariant, Sdf.SpecTypeVariantSet)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Specifier(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Sdf.SpecifierDef, Sdf.SpecifierOver, Sdf.SpecifierClass)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class StringListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 168
    @staticmethod
    def ApplyOperations(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def Create(*args, **kwargs):
        ...
    @staticmethod
    def CreateExplicit(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class TimeCode(Boost.Python.instance):
    """
    
    Value type that represents a time code. It's equivalent to a double
    type value but is used to indicate that this value should be resolved
    by any time based value resolution.
    
    """
    __instance_size__: typing.ClassVar[int] = 24
    @staticmethod
    def GetValue(*args, **kwargs):
        """
        
        GetValue() -> float
        
        
        Return the time value.
        
        
        
        """
    @staticmethod
    def __add__(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __float__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(time)
        
        
        Construct a time code with the given time.
        
        
        A default constructed SdfTimeCode has a time of 0.0. A double value
        can implicitly cast to SdfTimeCode.
        
        
        Parameters
        ----------
        time : float
        
        
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __mul__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __radd__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @staticmethod
    def __rmul__(*args, **kwargs):
        ...
    @staticmethod
    def __rsub__(*args, **kwargs):
        ...
    @staticmethod
    def __rtruediv__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @staticmethod
    def __sub__(*args, **kwargs):
        ...
    @staticmethod
    def __truediv__(*args, **kwargs):
        ...
class TimeCodeArray(Boost.Python.instance):
    """
    An array of type SdfTimeCode.
    """
    _isVtArray: typing.ClassVar[bool] = True
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        
        __init__(values)
        
        values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)
        
        
        
        __init__(values)
        
        values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)
        
        
        
        __init__(values)
        
        values: a sequence (tuple, list, or another VtArray with element type convertible to the new array's element type)
        
        """
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
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
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
class TokenListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 168
    @staticmethod
    def ApplyOperations(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def Create(*args, **kwargs):
        ...
    @staticmethod
    def CreateExplicit(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class UInt64ListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 168
    @staticmethod
    def ApplyOperations(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def Create(*args, **kwargs):
        ...
    @staticmethod
    def CreateExplicit(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class UIntListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 168
    @staticmethod
    def ApplyOperations(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def Create(*args, **kwargs):
        ...
    @staticmethod
    def CreateExplicit(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class UnregisteredValue(Boost.Python.instance):
    """
    
    Stores a representation of the value for an unregistered metadata
    field encountered during text layer parsing.
    
    This provides the ability to serialize this data to a layer, as well
    as limited inspection and editing capabilities (e.g., moving this data
    to a different spec or field) even when the data type of the value
    isn't known.
    
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Wraps an empty VtValue.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Wraps a std::string.
        
        
        Parameters
        ----------
        value : str
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Wraps a VtDictionary.
        
        
        Parameters
        ----------
        value : VtDictionary
        
        
        
        ----------------------------------------------------------------------
        
        __init__(value)
        
        
        Wraps a SdfUnregisteredValueListOp.
        
        
        Parameters
        ----------
        value : UnregisteredValueListOp
        
        
        """
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
    def value(*args, **kwargs):
        """
        type : VtValue
        
        
        Returns the wrapped VtValue specified in the constructor.
        """
class UnregisteredValueListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 168
    @staticmethod
    def ApplyOperations(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearAndMakeExplicit(*args, **kwargs):
        ...
    @staticmethod
    def Create(*args, **kwargs):
        ...
    @staticmethod
    def CreateExplicit(*args, **kwargs):
        ...
    @staticmethod
    def GetAddedOrExplicitItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
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
    def __str__(*args, **kwargs):
        ...
    @property
    def addedItems(*args, **kwargs):
        ...
    @addedItems.setter
    def addedItems(*args, **kwargs):
        ...
    @property
    def appendedItems(*args, **kwargs):
        ...
    @appendedItems.setter
    def appendedItems(*args, **kwargs):
        ...
    @property
    def deletedItems(*args, **kwargs):
        ...
    @deletedItems.setter
    def deletedItems(*args, **kwargs):
        ...
    @property
    def explicitItems(*args, **kwargs):
        ...
    @explicitItems.setter
    def explicitItems(*args, **kwargs):
        ...
    @property
    def isExplicit(*args, **kwargs):
        ...
    @property
    def orderedItems(*args, **kwargs):
        ...
    @orderedItems.setter
    def orderedItems(*args, **kwargs):
        ...
    @property
    def prependedItems(*args, **kwargs):
        ...
    @prependedItems.setter
    def prependedItems(*args, **kwargs):
        ...
class ValueBlock(Boost.Python.instance):
    """
    
    A special value type that can be used to explicitly author an opinion
    for an attribute's default value or time sample value that represents
    having no value. Note that this is different from not having a value
    authored.
    
    One could author such a value in two ways.
    
    .. code-block:: text
    
      attribute->SetDefaultValue(VtValue(SdfValueBlock());
      \\.\\.\\.
      layer->SetTimeSample(attribute->GetPath(), 101, VtValue(SdfValueBlock()));
    
    
    """
    __instance_size__: typing.ClassVar[int] = 24
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
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
class ValueRoleNames(Boost.Python.instance):
    Color: typing.ClassVar[str] = 'Color'
    EdgeIndex: typing.ClassVar[str] = 'EdgeIndex'
    FaceIndex: typing.ClassVar[str] = 'FaceIndex'
    Frame: typing.ClassVar[str] = 'Frame'
    Normal: typing.ClassVar[str] = 'Normal'
    Point: typing.ClassVar[str] = 'Point'
    PointIndex: typing.ClassVar[str] = 'PointIndex'
    TextureCoordinate: typing.ClassVar[str] = 'TextureCoordinate'
    Transform: typing.ClassVar[str] = 'Transform'
    Vector: typing.ClassVar[str] = 'Vector'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ValueTypeName(Boost.Python.instance):
    """
    
    Represents a value type name, i.e. an attribute's type name. Usually,
    a value type name associates a string with a ``TfType`` and an
    optional role, along with additional metadata. A schema registers all
    known value type names and may register multiple names for the same
    TfType and role pair. All name strings for a given pair are
    collectively called its aliases.
    
    A value type name may also represent just a name string, without a
    ``TfType`` , role or other metadata. This is currently used
    exclusively to unserialize and re-serialize an attribute's type name
    where that name is not known to the schema.
    
    Because value type names can have aliases and those aliases may change
    in the future, clients should avoid using the value type name's string
    representation except to report human readable messages and when
    serializing. Clients can look up a value type name by string using
    ``SdfSchemaBase::FindType()`` and shouldn't otherwise need the string.
    Aliases compare equal, even if registered by different schemas.
    
    """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Constructs an invalid type name.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : Sdf_ValueTypeImpl
        
        
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def aliasesAsStrings(*args, **kwargs):
        ...
    @property
    def arrayType(*args, **kwargs):
        """
        type : ValueTypeName
        
        
        Returns the array version of this type name if it's an scalar type
        name, otherwise returns this type name.
        
        
        If there is no array type name then this returns the invalid type
        name.
        """
    @property
    def cppTypeName(*args, **kwargs):
        ...
    @property
    def defaultUnit(*args, **kwargs):
        """
        type : Enum
        
        
        Returns the default unit enum for the type.
        """
    @property
    def defaultValue(*args, **kwargs):
        """
        type : VtValue
        
        
        Returns the default value for the type.
        """
    @property
    def isArray(*args, **kwargs):
        """
        type : bool
        
        
        Returns ``true`` iff this type is an array.
        
        
        The invalid type is considered neither scalar nor array.
        """
    @property
    def isScalar(*args, **kwargs):
        """
        type : bool
        
        
        Returns ``true`` iff this type is a scalar.
        
        
        The invalid type is considered neither scalar nor array.
        """
    @property
    def role(*args, **kwargs):
        """
        type : str
        
        
        Returns the type's role.
        """
    @property
    def scalarType(*args, **kwargs):
        """
        type : ValueTypeName
        
        
        Returns the scalar version of this type name if it's an array type
        name, otherwise returns this type name.
        
        
        If there is no scalar type name then this returns the invalid type
        name.
        """
    @property
    def type(*args, **kwargs):
        """
        type : Type
        
        
        Returns the ``TfType`` of the type.
        """
class ValueTypeNames(Boost.Python.instance):
    Asset: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    AssetArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Bool: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    BoolArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Color3d: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Color3dArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Color3f: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Color3fArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Color3h: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Color3hArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Color4d: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Color4dArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Color4f: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Color4fArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Color4h: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Color4hArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Double: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Double2: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Double2Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Double3: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Double3Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Double4: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Double4Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    DoubleArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Float: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Float2: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Float2Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Float3: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Float3Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Float4: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Float4Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    FloatArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Frame4d: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Frame4dArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Half: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Half2: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Half2Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Half3: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Half3Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Half4: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Half4Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    HalfArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Int: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Int2: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Int2Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Int3: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Int3Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Int4: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Int4Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Int64: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Int64Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    IntArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Matrix2d: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Matrix2dArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Matrix3d: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Matrix3dArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Matrix4d: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Matrix4dArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Normal3d: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Normal3dArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Normal3f: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Normal3fArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Normal3h: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Normal3hArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Point3d: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Point3dArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Point3f: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Point3fArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Point3h: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Point3hArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Quatd: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    QuatdArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Quatf: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    QuatfArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Quath: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    QuathArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    String: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    StringArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TexCoord2d: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TexCoord2dArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TexCoord2f: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TexCoord2fArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TexCoord2h: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TexCoord2hArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TexCoord3d: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TexCoord3dArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TexCoord3f: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TexCoord3fArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TexCoord3h: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TexCoord3hArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TimeCode: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TimeCodeArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Token: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    TokenArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    UChar: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    UCharArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    UInt: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    UInt64: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    UInt64Array: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    UIntArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Vector3d: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Vector3dArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Vector3f: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Vector3fArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Vector3h: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    Vector3hArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    @staticmethod
    def Find(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Variability(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Sdf.VariabilityVarying, Sdf.VariabilityUniform)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class VariantSetSpec(Spec):
    """
    
    Represents a coherent set of alternate representations for part of a
    scene.
    
    An SdfPrimSpec object may contain one or more named SdfVariantSetSpec
    objects that define variations on the prim.
    
    An SdfVariantSetSpec object contains one or more named SdfVariantSpec
    objects. It may also define the name of one of its variants to be used
    by default.
    
    When a prim references another prim, the referencing prim may specify
    one of the variants from each of the variant sets of the target prim.
    The chosen variant from each set (or the default variant from those
    sets that the referencing prim does not explicitly specify) is
    composited over the target prim, and then the referencing prim is
    composited over the result.
    
    """
    @staticmethod
    def RemoveVariant(*args, **kwargs):
        """
        
        RemoveVariant(variant) -> None
        
        
        Removes ``variant`` from the list of variants.
        
        
        If the variant set does not currently own ``variant`` , no action is
        taken.
        
        
        Parameters
        ----------
        variant : VariantSpec
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __new__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
    @property
    def name(*args, **kwargs):
        """
        The variant set's name.
        """
    @property
    def owner(*args, **kwargs):
        """
        The prim that this variant set belongs to.
        """
    @property
    def variantList(*args, **kwargs):
        """
        The variants in this variant set as a list.
        """
    @property
    def variants(*args, **kwargs):
        """
        The variants in this variant set as a dict.
        """
class VariantSpec(Spec):
    """
    
    Represents a single variant in a variant set.
    
    A variant contains a prim. This prim is the root prim of the variant.
    
    SdfVariantSpecs are value objects. This means they are immutable once
    created and they are passed by copy-in APIs. To change a variant spec,
    you make a new one and replace the existing one.
    
    """
    @staticmethod
    def GetVariantNames(*args, **kwargs):
        """
        
        GetVariantNames(name) -> list[str]
        
        
        Returns list of variant names for the given variant set.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __new__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        ...
    @property
    def name(*args, **kwargs):
        """
        The variant's name.
        """
    @property
    def owner(*args, **kwargs):
        """
        The variant set that this variant belongs to.
        """
    @property
    def primSpec(*args, **kwargs):
        """
        The root prim of this variant.
        """
    @property
    def variantSets(*args, **kwargs):
        """
        type : SdfVariantSetsProxy
        
        
        Returns the nested variant sets.
        
        
        The result maps variant set names to variant sets. Variant sets may be
        removed through the proxy.
        """
def Find(layerFileName, scenePath = None):
    """
    Find(layerFileName, scenePath) -> object
    
    layerFileName: string
    scenePath: Path
    
    If given a single string argument, returns the menv layer with 
    the given filename.  If given two arguments (a string and a Path), finds 
    the menv layer with the given filename and returns the scene object 
    within it at the given path.
    """
def _PathElemsToPrefixes(absolute, elements):
    ...
AngularUnitDegrees: AngularUnit  # value = Sdf.AngularUnitDegrees
AngularUnitRadians: AngularUnit  # value = Sdf.AngularUnitRadians
AuthoringErrorUnrecognizedFields: AuthoringError  # value = Sdf.AuthoringErrorUnrecognizedFields
AuthoringErrorUnrecognizedSpecType: AuthoringError  # value = Sdf.AuthoringErrorUnrecognizedSpecType
DimensionlessUnitDefault: DimensionlessUnit  # value = Sdf.DimensionlessUnitDefault
DimensionlessUnitPercent: DimensionlessUnit  # value = Sdf.DimensionlessUnitPercent
LengthUnitCentimeter: LengthUnit  # value = Sdf.LengthUnitCentimeter
LengthUnitDecimeter: LengthUnit  # value = Sdf.LengthUnitDecimeter
LengthUnitFoot: LengthUnit  # value = Sdf.LengthUnitFoot
LengthUnitInch: LengthUnit  # value = Sdf.LengthUnitInch
LengthUnitKilometer: LengthUnit  # value = Sdf.LengthUnitKilometer
LengthUnitMeter: LengthUnit  # value = Sdf.LengthUnitMeter
LengthUnitMile: LengthUnit  # value = Sdf.LengthUnitMile
LengthUnitMillimeter: LengthUnit  # value = Sdf.LengthUnitMillimeter
LengthUnitYard: LengthUnit  # value = Sdf.LengthUnitYard
ListOpTypeAdded: ListOpType  # value = Sdf.ListOpTypeAdded
ListOpTypeAppended: ListOpType  # value = Sdf.ListOpTypeAppended
ListOpTypeDeleted: ListOpType  # value = Sdf.ListOpTypeDeleted
ListOpTypeExplicit: ListOpType  # value = Sdf.ListOpTypeExplicit
ListOpTypeOrdered: ListOpType  # value = Sdf.ListOpTypeOrdered
ListOpTypePrepended: ListOpType  # value = Sdf.ListOpTypePrepended
PermissionPrivate: Permission  # value = Sdf.PermissionPrivate
PermissionPublic: Permission  # value = Sdf.PermissionPublic
SpecTypeAttribute: SpecType  # value = Sdf.SpecTypeAttribute
SpecTypeConnection: SpecType  # value = Sdf.SpecTypeConnection
SpecTypeExpression: SpecType  # value = Sdf.SpecTypeExpression
SpecTypeMapper: SpecType  # value = Sdf.SpecTypeMapper
SpecTypeMapperArg: SpecType  # value = Sdf.SpecTypeMapperArg
SpecTypePrim: SpecType  # value = Sdf.SpecTypePrim
SpecTypePseudoRoot: SpecType  # value = Sdf.SpecTypePseudoRoot
SpecTypeRelationship: SpecType  # value = Sdf.SpecTypeRelationship
SpecTypeRelationshipTarget: SpecType  # value = Sdf.SpecTypeRelationshipTarget
SpecTypeUnknown: SpecType  # value = Sdf.SpecTypeUnknown
SpecTypeVariant: SpecType  # value = Sdf.SpecTypeVariant
SpecTypeVariantSet: SpecType  # value = Sdf.SpecTypeVariantSet
SpecifierClass: Specifier  # value = Sdf.SpecifierClass
SpecifierDef: Specifier  # value = Sdf.SpecifierDef
SpecifierOver: Specifier  # value = Sdf.SpecifierOver
VariabilityUniform: Variability  # value = Sdf.VariabilityUniform
VariabilityVarying: Variability  # value = Sdf.VariabilityVarying
__MFB_FULL_PACKAGE_NAME: str = 'sdf'
