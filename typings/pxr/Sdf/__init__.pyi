from __future__ import annotations
import pxr.Tf
import typing
__all__: list[str] = ['AngularUnit', 'AngularUnitDegrees', 'AngularUnitRadians', 'AssetPath', 'AssetPathArray', 'AttributeSpec', 'AuthoringError', 'AuthoringErrorUnrecognizedFields', 'AuthoringErrorUnrecognizedSpecType', 'BatchNamespaceEdit', 'ChangeBlock', 'ChildrenView_Sdf_AttributeChildPolicy_SdfAttributeViewPredicate', 'ChildrenView_Sdf_AttributeChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfAttributeSpec___', 'ChildrenView_Sdf_PrimChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPrimSpec___', 'ChildrenView_Sdf_PropertyChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfPropertySpec___', 'ChildrenView_Sdf_RelationshipChildPolicy_SdfRelationshipViewPredicate', 'ChildrenView_Sdf_VariantChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSpec___', 'ChildrenView_Sdf_VariantSetChildPolicy_SdfChildrenViewTrivialPredicate_SdfHandle_SdfVariantSetSpec___', 'CleanupEnabler', 'DimensionlessUnit', 'DimensionlessUnitDefault', 'DimensionlessUnitPercent', 'FileFormat', 'Find', 'Int64ListOp', 'IntListOp', 'Layer', 'LayerOffset', 'LayerTree', 'LengthUnit', 'LengthUnitCentimeter', 'LengthUnitDecimeter', 'LengthUnitFoot', 'LengthUnitInch', 'LengthUnitKilometer', 'LengthUnitMeter', 'LengthUnitMile', 'LengthUnitMillimeter', 'LengthUnitYard', 'ListEditorProxy_SdfNameKeyPolicy', 'ListEditorProxy_SdfPathKeyPolicy', 'ListEditorProxy_SdfPayloadTypePolicy', 'ListEditorProxy_SdfReferenceTypePolicy', 'ListOpType', 'ListOpTypeAdded', 'ListOpTypeAppended', 'ListOpTypeDeleted', 'ListOpTypeExplicit', 'ListOpTypeOrdered', 'ListOpTypePrepended', 'ListProxy_SdfNameKeyPolicy', 'ListProxy_SdfNameTokenKeyPolicy', 'ListProxy_SdfPathKeyPolicy', 'ListProxy_SdfPayloadTypePolicy', 'ListProxy_SdfReferenceTypePolicy', 'ListProxy_SdfSubLayerTypePolicy', 'MapEditProxy_VtDictionary', 'MapEditProxy_map_SdfPath__SdfPath__less_SdfPath___allocator_pair_SdfPath_const__SdfPath_____', 'MapEditProxy_map_string__string__less_string___allocator_pair_stringconst__string_____', 'NamespaceEdit', 'NamespaceEditDetail', 'Notice', 'OpaqueValue', 'Path', 'PathArray', 'PathExpression', 'PathListOp', 'Payload', 'PayloadListOp', 'Permission', 'PermissionPrivate', 'PermissionPublic', 'PredicateExpression', 'PredicateFunctionResult', 'PrimSpec', 'PropertySpec', 'PseudoRootSpec', 'Reference', 'ReferenceListOp', 'RelationshipSpec', 'Spec', 'SpecType', 'SpecTypeAttribute', 'SpecTypeConnection', 'SpecTypeExpression', 'SpecTypeMapper', 'SpecTypeMapperArg', 'SpecTypePrim', 'SpecTypePseudoRoot', 'SpecTypeRelationship', 'SpecTypeRelationshipTarget', 'SpecTypeUnknown', 'SpecTypeVariant', 'SpecTypeVariantSet', 'Specifier', 'SpecifierClass', 'SpecifierDef', 'SpecifierOver', 'StringListOp', 'TimeCode', 'TimeCodeArray', 'TokenListOp', 'UInt64ListOp', 'UIntListOp', 'UnregisteredValue', 'UnregisteredValueListOp', 'ValueBlock', 'ValueRoleNames', 'ValueTypeName', 'ValueTypeNames', 'Variability', 'VariabilityUniform', 'VariabilityVarying', 'VariableExpression', 'VariantSetSpec', 'VariantSpec']
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
    __instance_size__: typing.ClassVar[int] = 88
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
        ...
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
    ConnectionPathsKey: typing.ClassVar[str] = 'connectionPaths'
    DefaultValueKey: typing.ClassVar[str] = 'default'
    DisplayUnitKey: typing.ClassVar[str] = 'displayUnit'
    @staticmethod
    def ClearColorSpace(*args, **kwargs):
        ...
    @staticmethod
    def HasColorSpace(*args, **kwargs):
        ...
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
    @staticmethod
    def Add(*args, **kwargs):
        ...
    @staticmethod
    def Process(*args, **kwargs):
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def edits(*args, **kwargs):
        ...
class ChangeBlock(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
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
class FileFormat(Boost.Python.instance):
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
        ...
    @staticmethod
    def FindAllDerivedFileFormatExtensions(*args, **kwargs):
        ...
    @staticmethod
    def FindAllFileFormatExtensions(*args, **kwargs):
        ...
    @staticmethod
    def FindByExtension(*args, **kwargs):
        ...
    @staticmethod
    def FindById(*args, **kwargs):
        ...
    @staticmethod
    def FormatSupportsEditing(*args, **kwargs):
        ...
    @staticmethod
    def FormatSupportsReading(*args, **kwargs):
        ...
    @staticmethod
    def FormatSupportsWriting(*args, **kwargs):
        ...
    @staticmethod
    def GetFileExtension(*args, **kwargs):
        ...
    @staticmethod
    def GetFileExtensions(*args, **kwargs):
        ...
    @staticmethod
    def IsPackage(*args, **kwargs):
        ...
    @staticmethod
    def IsSupportedExtension(*args, **kwargs):
        ...
    @staticmethod
    def SupportsEditing(*args, **kwargs):
        ...
    @staticmethod
    def SupportsReading(*args, **kwargs):
        ...
    @staticmethod
    def SupportsWriting(*args, **kwargs):
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
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
    @property
    def fileCookie(*args, **kwargs):
        ...
    @property
    def formatId(*args, **kwargs):
        ...
    @property
    def primaryFileExtension(*args, **kwargs):
        ...
    @property
    def target(*args, **kwargs):
        ...
class Int64ListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 176
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
    def GetAppliedItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 176
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
    def GetAppliedItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
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
    class DetachedLayerRules(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 80
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
    LayerRelocatesKey: typing.ClassVar[str] = 'layerRelocates'
    OwnerKey: typing.ClassVar[str] = 'owner'
    SessionOwnerKey: typing.ClassVar[str] = 'sessionOwner'
    StartFrameKey: typing.ClassVar[str] = 'startFrame'
    StartTimeCodeKey: typing.ClassVar[str] = 'startTimeCode'
    TimeCodesPerSecondKey: typing.ClassVar[str] = 'timeCodesPerSecond'
    @staticmethod
    def AddToMutedLayers(*args, **kwargs):
        ...
    @staticmethod
    def Apply(*args, **kwargs):
        ...
    @staticmethod
    def ApplyRootPrimOrder(*args, **kwargs):
        ...
    @staticmethod
    def CanApply(*args, **kwargs):
        ...
    @staticmethod
    def Clear(*args, **kwargs):
        ...
    @staticmethod
    def ClearColorConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def ClearColorManagementSystem(*args, **kwargs):
        ...
    @staticmethod
    def ClearCustomLayerData(*args, **kwargs):
        ...
    @staticmethod
    def ClearDefaultPrim(*args, **kwargs):
        ...
    @staticmethod
    def ClearEndTimeCode(*args, **kwargs):
        ...
    @staticmethod
    def ClearExpressionVariables(*args, **kwargs):
        ...
    @staticmethod
    def ClearFramePrecision(*args, **kwargs):
        ...
    @staticmethod
    def ClearFramesPerSecond(*args, **kwargs):
        ...
    @staticmethod
    def ClearOwner(*args, **kwargs):
        ...
    @staticmethod
    def ClearRelocates(*args, **kwargs):
        ...
    @staticmethod
    def ClearSessionOwner(*args, **kwargs):
        ...
    @staticmethod
    def ClearStartTimeCode(*args, **kwargs):
        ...
    @staticmethod
    def ClearTimeCodesPerSecond(*args, **kwargs):
        ...
    @staticmethod
    def ComputeAbsolutePath(*args, **kwargs):
        ...
    @staticmethod
    def CreateAnonymous(*args, **kwargs):
        ...
    @staticmethod
    def CreateIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def CreateNew(*args, **kwargs):
        ...
    @staticmethod
    def DumpLayerInfo(*args, **kwargs):
        """
        
        
        Debug helper to examine content of the current layer registry and
        the asset/real path of all layers in the registry.
        """
    @staticmethod
    def EraseTimeSample(*args, **kwargs):
        ...
    @staticmethod
    def Export(*args, **kwargs):
        ...
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
        ...
    @staticmethod
    def FindOrOpenRelativeToLayer(*args, **kwargs):
        ...
    @staticmethod
    def FindRelativeToLayer(*args, **kwargs):
        """
        
        
        Returns the open layer with the given filename, or None.  If the filename is a relative path then it's found relative to the given layer.  Note that this is a static class method.
        """
    @staticmethod
    def GetAssetInfo(*args, **kwargs):
        ...
    @staticmethod
    def GetAssetName(*args, **kwargs):
        ...
    @staticmethod
    def GetAttributeAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetBracketingTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def GetBracketingTimeSamplesForPath(*args, **kwargs):
        ...
    @staticmethod
    def GetCompositionAssetDependencies(*args, **kwargs):
        ...
    @staticmethod
    def GetDetachedLayerRules(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplayName(*args, **kwargs):
        ...
    @staticmethod
    def GetDisplayNameFromIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def GetExternalAssetDependencies(*args, **kwargs):
        ...
    @staticmethod
    def GetExternalReferences(*args, **kwargs):
        """
        
        
        Return a list of asset paths for
        this layer.
        """
    @staticmethod
    def GetFileFormat(*args, **kwargs):
        ...
    @staticmethod
    def GetFileFormatArguments(*args, **kwargs):
        ...
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
        ...
    @staticmethod
    def GetObjectAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetPropertyAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetRelationshipAtPath(*args, **kwargs):
        ...
    @staticmethod
    def HasColorConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def HasColorManagementSystem(*args, **kwargs):
        ...
    @staticmethod
    def HasCustomLayerData(*args, **kwargs):
        ...
    @staticmethod
    def HasDefaultPrim(*args, **kwargs):
        ...
    @staticmethod
    def HasEndTimeCode(*args, **kwargs):
        ...
    @staticmethod
    def HasExpressionVariables(*args, **kwargs):
        ...
    @staticmethod
    def HasFramePrecision(*args, **kwargs):
        ...
    @staticmethod
    def HasFramesPerSecond(*args, **kwargs):
        ...
    @staticmethod
    def HasOwner(*args, **kwargs):
        ...
    @staticmethod
    def HasRelocates(*args, **kwargs):
        ...
    @staticmethod
    def HasSessionOwner(*args, **kwargs):
        ...
    @staticmethod
    def HasStartTimeCode(*args, **kwargs):
        ...
    @staticmethod
    def HasTimeCodesPerSecond(*args, **kwargs):
        ...
    @staticmethod
    def Import(*args, **kwargs):
        ...
    @staticmethod
    def ImportFromString(*args, **kwargs):
        ...
    @staticmethod
    def IsAnonymousLayerIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def IsDetached(*args, **kwargs):
        ...
    @staticmethod
    def IsIncludedByDetachedLayerRules(*args, **kwargs):
        ...
    @staticmethod
    def IsMuted(*args, **kwargs):
        ...
    @staticmethod
    def ListAllTimeSamples(*args, **kwargs):
        ...
    @staticmethod
    def ListTimeSamplesForPath(*args, **kwargs):
        ...
    @staticmethod
    def New(*args, **kwargs):
        ...
    @staticmethod
    def OpenAsAnonymous(*args, **kwargs):
        ...
    @staticmethod
    def QueryTimeSample(*args, **kwargs):
        ...
    @staticmethod
    def Reload(*args, **kwargs):
        ...
    @staticmethod
    def ReloadLayers(*args, **kwargs):
        ...
    @staticmethod
    def RemoveFromMutedLayers(*args, **kwargs):
        ...
    @staticmethod
    def RemoveInertSceneDescription(*args, **kwargs):
        ...
    @staticmethod
    def Save(*args, **kwargs):
        ...
    @staticmethod
    def ScheduleRemoveIfInert(*args, **kwargs):
        ...
    @staticmethod
    def SetDetachedLayerRules(*args, **kwargs):
        ...
    @staticmethod
    def SetMuted(*args, **kwargs):
        ...
    @staticmethod
    def SetPermissionToEdit(*args, **kwargs):
        ...
    @staticmethod
    def SetPermissionToSave(*args, **kwargs):
        ...
    @staticmethod
    def SetTimeSample(*args, **kwargs):
        ...
    @staticmethod
    def SplitIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def StreamsData(*args, **kwargs):
        ...
    @staticmethod
    def TransferContent(*args, **kwargs):
        ...
    @staticmethod
    def Traverse(*args, **kwargs):
        ...
    @staticmethod
    def UpdateAssetInfo(*args, **kwargs):
        ...
    @staticmethod
    def UpdateCompositionAssetDependency(*args, **kwargs):
        ...
    @staticmethod
    def UpdateExternalReference(*args, **kwargs):
        ...
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
        ...
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
        ...
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
        ...
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
    def expressionVariables(*args, **kwargs):
        """
        The expressionVariables dictionary associated with this layer.
        """
    @expressionVariables.setter
    def expressionVariables(*args, **kwargs):
        ...
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
    def relocates(*args, **kwargs):
        ...
    @relocates.setter
    def relocates(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def GetInverse(*args, **kwargs):
        ...
    @staticmethod
    def IsIdentity(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
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
        ...
    @property
    def scale(*args, **kwargs):
        ...
class LayerTree(Boost.Python.instance):
    """
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
        ...
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
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
    @property
    def layer(*args, **kwargs):
        ...
    @property
    def offset(*args, **kwargs):
        ...
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
    def GetAppliedItems(*args, **kwargs):
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
    def GetAppliedItems(*args, **kwargs):
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
    def GetAppliedItems(*args, **kwargs):
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
    def GetAppliedItems(*args, **kwargs):
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
    __instance_size__: typing.ClassVar[int] = 40
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
    __instance_size__: typing.ClassVar[int] = 40
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
    __instance_size__: typing.ClassVar[int] = 40
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
    atEnd: typing.ClassVar[int] = -1
    same: typing.ClassVar[int] = -2
    @staticmethod
    def Remove(*args, **kwargs):
        ...
    @staticmethod
    def Rename(*args, **kwargs):
        ...
    @staticmethod
    def Reorder(*args, **kwargs):
        ...
    @staticmethod
    def Reparent(*args, **kwargs):
        ...
    @staticmethod
    def ReparentAndRename(*args, **kwargs):
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
    class Result(pxr.Tf.Tf_PyEnumWrapper):
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
class OpaqueValue(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
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
class Path(Boost.Python.instance):
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
        __instance_size__: typing.ClassVar[int] = 32
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
        def errorMessage(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 32
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
        ...
    @staticmethod
    def AppendElementString(*args, **kwargs):
        ...
    @staticmethod
    def AppendExpression(*args, **kwargs):
        ...
    @staticmethod
    def AppendMapper(*args, **kwargs):
        ...
    @staticmethod
    def AppendMapperArg(*args, **kwargs):
        ...
    @staticmethod
    def AppendPath(*args, **kwargs):
        ...
    @staticmethod
    def AppendProperty(*args, **kwargs):
        ...
    @staticmethod
    def AppendRelationalAttribute(*args, **kwargs):
        ...
    @staticmethod
    def AppendTarget(*args, **kwargs):
        ...
    @staticmethod
    def AppendVariantSelection(*args, **kwargs):
        ...
    @staticmethod
    def ContainsPrimVariantSelection(*args, **kwargs):
        ...
    @staticmethod
    def ContainsPropertyElements(*args, **kwargs):
        ...
    @staticmethod
    def ContainsTargetPath(*args, **kwargs):
        ...
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
        ...
    @staticmethod
    def GetAllTargetPathsRecursively(*args, **kwargs):
        ...
    @staticmethod
    def GetAncestorsRange(*args, **kwargs):
        ...
    @staticmethod
    def GetCommonPrefix(*args, **kwargs):
        ...
    @staticmethod
    def GetConciseRelativePaths(*args, **kwargs):
        ...
    @staticmethod
    def GetParentPath(*args, **kwargs):
        ...
    @staticmethod
    def GetPrefixes(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimOrPrimVariantSelectionPath(*args, **kwargs):
        ...
    @staticmethod
    def GetPrimPath(*args, **kwargs):
        ...
    @staticmethod
    def GetVariantSelection(*args, **kwargs):
        ...
    @staticmethod
    def HasPrefix(*args, **kwargs):
        ...
    @staticmethod
    def IsAbsolutePath(*args, **kwargs):
        ...
    @staticmethod
    def IsAbsoluteRootOrPrimPath(*args, **kwargs):
        ...
    @staticmethod
    def IsAbsoluteRootPath(*args, **kwargs):
        ...
    @staticmethod
    def IsExpressionPath(*args, **kwargs):
        ...
    @staticmethod
    def IsMapperArgPath(*args, **kwargs):
        ...
    @staticmethod
    def IsMapperPath(*args, **kwargs):
        ...
    @staticmethod
    def IsNamespacedPropertyPath(*args, **kwargs):
        ...
    @staticmethod
    def IsPrimPath(*args, **kwargs):
        ...
    @staticmethod
    def IsPrimPropertyPath(*args, **kwargs):
        ...
    @staticmethod
    def IsPrimVariantSelectionPath(*args, **kwargs):
        ...
    @staticmethod
    def IsPropertyPath(*args, **kwargs):
        ...
    @staticmethod
    def IsRelationalAttributePath(*args, **kwargs):
        ...
    @staticmethod
    def IsRootPrimPath(*args, **kwargs):
        ...
    @staticmethod
    def IsTargetPath(*args, **kwargs):
        ...
    @staticmethod
    def IsValidIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def IsValidNamespacedIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def IsValidPathString(*args, **kwargs):
        ...
    @staticmethod
    def JoinIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def MakeAbsolutePath(*args, **kwargs):
        ...
    @staticmethod
    def MakeRelativePath(*args, **kwargs):
        ...
    @staticmethod
    def RemoveAncestorPaths(*args, **kwargs):
        ...
    @staticmethod
    def RemoveCommonSuffix(*args, **kwargs):
        ...
    @staticmethod
    def RemoveDescendentPaths(*args, **kwargs):
        ...
    @staticmethod
    def ReplaceName(*args, **kwargs):
        ...
    @staticmethod
    def ReplacePrefix(*args, **kwargs):
        ...
    @staticmethod
    def ReplaceTargetPath(*args, **kwargs):
        ...
    @staticmethod
    def StripAllVariantSelections(*args, **kwargs):
        ...
    @staticmethod
    def StripNamespace(*args, **kwargs):
        ...
    @staticmethod
    def StripPrefixNamespace(*args, **kwargs):
        ...
    @staticmethod
    def TokenizeIdentifier(*args, **kwargs):
        ...
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
        ...
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
class PathExpression(Boost.Python.instance):
    class ExpressionReference(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 64
        @staticmethod
        def Weaker(*args, **kwargs):
            ...
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
        @property
        def name(*args, **kwargs):
            ...
        @name.setter
        def name(*args, **kwargs):
            ...
        @property
        def path(*args, **kwargs):
            ...
        @path.setter
        def path(*args, **kwargs):
            ...
    class Op(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'PathExpression'
        allValues: typing.ClassVar[tuple]  # value = (Sdf.PathExpression.Complement, Sdf.PathExpression.ImpliedUnion, Sdf.PathExpression.Union, Sdf.PathExpression.Intersection, Sdf.PathExpression.Difference, Sdf.PathExpression.ExpressionRef, Sdf.PathExpression.Pattern)
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
    class PathPattern(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 88
        @staticmethod
        def AppendChild(*args, **kwargs):
            ...
        @staticmethod
        def AppendProperty(*args, **kwargs):
            ...
        @staticmethod
        def GetPrefix(*args, **kwargs):
            ...
        @staticmethod
        def GetText(*args, **kwargs):
            ...
        @staticmethod
        def SetPrefix(*args, **kwargs):
            ...
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
    Complement: typing.ClassVar[Op]  # value = Sdf.PathExpression.Complement
    Difference: typing.ClassVar[Op]  # value = Sdf.PathExpression.Difference
    ExpressionRef: typing.ClassVar[Op]  # value = Sdf.PathExpression.ExpressionRef
    ImpliedUnion: typing.ClassVar[Op]  # value = Sdf.PathExpression.ImpliedUnion
    Intersection: typing.ClassVar[Op]  # value = Sdf.PathExpression.Intersection
    Pattern: typing.ClassVar[Op]  # value = Sdf.PathExpression.Pattern
    Union: typing.ClassVar[Op]  # value = Sdf.PathExpression.Union
    __instance_size__: typing.ClassVar[int] = 128
    @staticmethod
    def ComposeOver(*args, **kwargs):
        ...
    @staticmethod
    def ContainsExpressionReferences(*args, **kwargs):
        ...
    @staticmethod
    def ContainsWeakerExpressionReference(*args, **kwargs):
        ...
    @staticmethod
    def Everything(*args, **kwargs):
        ...
    @staticmethod
    def GetText(*args, **kwargs):
        ...
    @staticmethod
    def IsAbsolute(*args, **kwargs):
        ...
    @staticmethod
    def IsComplete(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def MakeAbsolute(*args, **kwargs):
        ...
    @staticmethod
    def MakeAtom(*args, **kwargs):
        ...
    @staticmethod
    def MakeComplement(*args, **kwargs):
        ...
    @staticmethod
    def MakeOp(*args, **kwargs):
        ...
    @staticmethod
    def Nothing(*args, **kwargs):
        ...
    @staticmethod
    def ReplacePrefix(*args, **kwargs):
        ...
    @staticmethod
    def ResolveReferences(*args, **kwargs):
        ...
    @staticmethod
    def Walk(*args, **kwargs):
        ...
    @staticmethod
    def WeakerRef(*args, **kwargs):
        ...
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
class PathListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 176
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
    def GetAppliedItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 80
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
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def assetPath(*args, **kwargs):
        ...
    @assetPath.setter
    def assetPath(*args, **kwargs):
        ...
    @property
    def layerOffset(*args, **kwargs):
        ...
    @layerOffset.setter
    def layerOffset(*args, **kwargs):
        ...
    @property
    def primPath(*args, **kwargs):
        ...
    @primPath.setter
    def primPath(*args, **kwargs):
        ...
class PayloadListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 176
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
    def GetAppliedItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
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
class PredicateExpression(Boost.Python.instance):
    class FnArg(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 72
        @staticmethod
        def Keyword(*args, **kwargs):
            ...
        @staticmethod
        def Positional(*args, **kwargs):
            ...
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
        @property
        def argName(*args, **kwargs):
            ...
        @argName.setter
        def argName(*args, **kwargs):
            ...
        @property
        def value(*args, **kwargs):
            ...
        @value.setter
        def value(*args, **kwargs):
            ...
    class FnCall(Boost.Python.instance):
        class Kind(pxr.Tf.Tf_PyEnumWrapper):
            _baseName: typing.ClassVar[str] = 'PredicateExpression.FnCall'
            allValues: typing.ClassVar[tuple]  # value = (Sdf.PredicateExpression.FnCall.BareCall, Sdf.PredicateExpression.FnCall.ColonCall, Sdf.PredicateExpression.FnCall.ParenCall)
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
        BareCall: typing.ClassVar[Kind]  # value = Sdf.PredicateExpression.FnCall.BareCall
        ColonCall: typing.ClassVar[Kind]  # value = Sdf.PredicateExpression.FnCall.ColonCall
        ParenCall: typing.ClassVar[Kind]  # value = Sdf.PredicateExpression.FnCall.ParenCall
        __instance_size__: typing.ClassVar[int] = 88
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
        @property
        def args(*args, **kwargs):
            ...
        @args.setter
        def args(*args, **kwargs):
            ...
        @property
        def funcName(*args, **kwargs):
            ...
        @funcName.setter
        def funcName(*args, **kwargs):
            ...
        @property
        def kind(*args, **kwargs):
            ...
        @kind.setter
        def kind(*args, **kwargs):
            ...
    class Op(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'PredicateExpression'
        allValues: typing.ClassVar[tuple]  # value = (Sdf.PredicateExpression.Call, Sdf.PredicateExpression.Not, Sdf.PredicateExpression.ImpliedAnd, Sdf.PredicateExpression.And, Sdf.PredicateExpression.Or)
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
    class _PredicateExpressionFnArgVector(Boost.Python.instance):
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
    And: typing.ClassVar[Op]  # value = Sdf.PredicateExpression.And
    Call: typing.ClassVar[Op]  # value = Sdf.PredicateExpression.Call
    ImpliedAnd: typing.ClassVar[Op]  # value = Sdf.PredicateExpression.ImpliedAnd
    Not: typing.ClassVar[Op]  # value = Sdf.PredicateExpression.Not
    Or: typing.ClassVar[Op]  # value = Sdf.PredicateExpression.Or
    __instance_size__: typing.ClassVar[int] = 104
    @staticmethod
    def GetParseError(*args, **kwargs):
        ...
    @staticmethod
    def GetText(*args, **kwargs):
        ...
    @staticmethod
    def IsEmpty(*args, **kwargs):
        ...
    @staticmethod
    def MakeCall(*args, **kwargs):
        ...
    @staticmethod
    def MakeNot(*args, **kwargs):
        ...
    @staticmethod
    def MakeOp(*args, **kwargs):
        ...
    @staticmethod
    def Walk(*args, **kwargs):
        ...
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
class PredicateFunctionResult(Boost.Python.instance):
    class Constancy(pxr.Tf.Tf_PyEnumWrapper):
        _baseName: typing.ClassVar[str] = 'PredicateFunctionResult'
        allValues: typing.ClassVar[tuple]  # value = (Sdf.PredicateFunctionResult.ConstantOverDescendants, Sdf.PredicateFunctionResult.MayVaryOverDescendants)
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
    ConstantOverDescendants: typing.ClassVar[Constancy]  # value = Sdf.PredicateFunctionResult.ConstantOverDescendants
    MayVaryOverDescendants: typing.ClassVar[Constancy]  # value = Sdf.PredicateFunctionResult.MayVaryOverDescendants
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def GetConstancy(*args, **kwargs):
        ...
    @staticmethod
    def GetValue(*args, **kwargs):
        ...
    @staticmethod
    def IsConstant(*args, **kwargs):
        ...
    @staticmethod
    def MakeConstant(*args, **kwargs):
        ...
    @staticmethod
    def MakeVarying(*args, **kwargs):
        ...
    @staticmethod
    def SetAndPropagateConstancy(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
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
    def __repr__(*args, **kwargs):
        ...
class PrimSpec(Spec):
    ActiveKey: typing.ClassVar[str] = 'active'
    AnyTypeToken: typing.ClassVar[str] = '__AnyType__'
    CommentKey: typing.ClassVar[str] = 'comment'
    CustomDataKey: typing.ClassVar[str] = 'customData'
    DisplayName: typing.ClassVar[str] = 'displayName'
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
        ...
    @staticmethod
    def ApplyPropertyOrder(*args, **kwargs):
        ...
    @staticmethod
    def BlockVariantSelection(*args, **kwargs):
        ...
    @staticmethod
    def CanSetName(*args, **kwargs):
        ...
    @staticmethod
    def ClearActive(*args, **kwargs):
        ...
    @staticmethod
    def ClearInstanceable(*args, **kwargs):
        ...
    @staticmethod
    def ClearKind(*args, **kwargs):
        ...
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
        ...
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
        ...
    @staticmethod
    def GetPropertyAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetRelationshipAtPath(*args, **kwargs):
        ...
    @staticmethod
    def GetVariantNames(*args, **kwargs):
        ...
    @staticmethod
    def HasActive(*args, **kwargs):
        ...
    @staticmethod
    def HasInstanceable(*args, **kwargs):
        ...
    @staticmethod
    def HasKind(*args, **kwargs):
        ...
    @staticmethod
    def RemoveProperty(*args, **kwargs):
        ...
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
        ...
    @staticmethod
    def HasDefaultValue(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 88
    @staticmethod
    def IsInternal(*args, **kwargs):
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
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def assetPath(*args, **kwargs):
        ...
    @property
    def customData(*args, **kwargs):
        ...
    @property
    def layerOffset(*args, **kwargs):
        ...
    @property
    def primPath(*args, **kwargs):
        ...
class ReferenceListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 176
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
    def GetAppliedItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
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
    TargetsKey: typing.ClassVar[str] = 'targetPaths'
    @staticmethod
    def RemoveTargetPath(*args, **kwargs):
        ...
    @staticmethod
    def ReplaceTargetPath(*args, **kwargs):
        ...
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
        ...
    @staticmethod
    def GetMetaDataDisplayGroup(*args, **kwargs):
        ...
    @staticmethod
    def GetMetaDataInfoKeys(*args, **kwargs):
        ...
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
        ...
    @staticmethod
    def SetInfo(*args, **kwargs):
        ...
    @staticmethod
    def SetInfoDictionaryValue(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 176
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
    def GetAppliedItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def GetValue(*args, **kwargs):
        ...
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
        ...
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
    __instance_size__: typing.ClassVar[int] = 176
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
    def GetAppliedItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 176
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
    def GetAppliedItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 176
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
    def GetAppliedItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 40
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
    @property
    def value(*args, **kwargs):
        ...
class UnregisteredValueListOp(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 176
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
    def GetAppliedItems(*args, **kwargs):
        ...
    @staticmethod
    def HasItem(*args, **kwargs):
        ...
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
    __instance_size__: typing.ClassVar[int] = 32
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
    Group: typing.ClassVar[str] = 'Group'
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
    def aliasesAsStrings(*args, **kwargs):
        ...
    @property
    def arrayType(*args, **kwargs):
        ...
    @property
    def cppTypeName(*args, **kwargs):
        ...
    @property
    def defaultUnit(*args, **kwargs):
        ...
    @property
    def defaultValue(*args, **kwargs):
        ...
    @property
    def isArray(*args, **kwargs):
        ...
    @property
    def isScalar(*args, **kwargs):
        ...
    @property
    def role(*args, **kwargs):
        ...
    @property
    def scalarType(*args, **kwargs):
        ...
    @property
    def type(*args, **kwargs):
        ...
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
    Group: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
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
    Opaque: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    PathExpression: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
    PathExpressionArray: typing.ClassVar[ValueTypeName]  # value = <pxr.Sdf.ValueTypeName object>
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
class VariableExpression(Boost.Python.instance):
    class Result(Boost.Python.instance):
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
        def errors(*args, **kwargs):
            ...
        @property
        def usedVariables(*args, **kwargs):
            ...
        @property
        def value(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 96
    @staticmethod
    def Evaluate(*args, **kwargs):
        ...
    @staticmethod
    def GetErrors(*args, **kwargs):
        ...
    @staticmethod
    def IsExpression(*args, **kwargs):
        ...
    @staticmethod
    def IsValidVariableType(*args, **kwargs):
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
class VariantSetSpec(Spec):
    @staticmethod
    def RemoveVariant(*args, **kwargs):
        ...
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
    @staticmethod
    def GetVariantNames(*args, **kwargs):
        ...
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
        ...
def Find(layerFileName, scenePath = None):
    """
    Find(layerFileName, scenePath) -> object
    
    layerFileName: string
    scenePath: Path
    
    If given a single string argument, returns the layer with 
    the given filename.  If given two arguments (a string and a Path), finds 
    the layer with the given filename and returns the scene object 
    within it at the given path.
    """
def _PathElemsToPrefixes(absolute, elements, numPrefixes = 0):
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
