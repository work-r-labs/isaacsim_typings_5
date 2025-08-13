from __future__ import annotations
import pxr.UsdGeom
import typing
__all__: list[str] = ['Field3DAsset', 'FieldAsset', 'FieldBase', 'OpenVDBAsset', 'Tokens', 'Volume']
class Field3DAsset(FieldAsset):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateFieldDataTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFieldPurposeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetFieldDataTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFieldPurposeAttr(*args, **kwargs):
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
class FieldAsset(FieldBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateFieldDataTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFieldIndexAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFieldNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFilePathAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateVectorDataRoleHintAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetFieldDataTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFieldIndexAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFieldNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFilePathAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetVectorDataRoleHintAttr(*args, **kwargs):
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
class FieldBase(pxr.UsdGeom.Xformable):
    __instance_size__: typing.ClassVar[int] = 48
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
class OpenVDBAsset(FieldAsset):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateFieldClassAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateFieldDataTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetFieldClassAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetFieldDataTypeAttr(*args, **kwargs):
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
    Color: typing.ClassVar[str] = 'Color'
    Field3DAsset: typing.ClassVar[str] = 'Field3DAsset'
    FieldAsset: typing.ClassVar[str] = 'FieldAsset'
    FieldBase: typing.ClassVar[str] = 'FieldBase'
    None_: typing.ClassVar[str] = 'None'
    Normal: typing.ClassVar[str] = 'Normal'
    OpenVDBAsset: typing.ClassVar[str] = 'OpenVDBAsset'
    Point: typing.ClassVar[str] = 'Point'
    Vector: typing.ClassVar[str] = 'Vector'
    Volume: typing.ClassVar[str] = 'Volume'
    bool_: typing.ClassVar[str] = 'bool'
    double2: typing.ClassVar[str] = 'double2'
    double3: typing.ClassVar[str] = 'double3'
    double_: typing.ClassVar[str] = 'double'
    field: typing.ClassVar[str] = 'field'
    fieldClass: typing.ClassVar[str] = 'fieldClass'
    fieldDataType: typing.ClassVar[str] = 'fieldDataType'
    fieldIndex: typing.ClassVar[str] = 'fieldIndex'
    fieldName: typing.ClassVar[str] = 'fieldName'
    fieldPurpose: typing.ClassVar[str] = 'fieldPurpose'
    filePath: typing.ClassVar[str] = 'filePath'
    float2: typing.ClassVar[str] = 'float2'
    float3: typing.ClassVar[str] = 'float3'
    float_: typing.ClassVar[str] = 'float'
    fogVolume: typing.ClassVar[str] = 'fogVolume'
    half: typing.ClassVar[str] = 'half'
    half2: typing.ClassVar[str] = 'half2'
    half3: typing.ClassVar[str] = 'half3'
    int2: typing.ClassVar[str] = 'int2'
    int3: typing.ClassVar[str] = 'int3'
    int64: typing.ClassVar[str] = 'int64'
    int_: typing.ClassVar[str] = 'int'
    levelSet: typing.ClassVar[str] = 'levelSet'
    mask: typing.ClassVar[str] = 'mask'
    matrix3d: typing.ClassVar[str] = 'matrix3d'
    matrix4d: typing.ClassVar[str] = 'matrix4d'
    quatd: typing.ClassVar[str] = 'quatd'
    staggered: typing.ClassVar[str] = 'staggered'
    string: typing.ClassVar[str] = 'string'
    uint: typing.ClassVar[str] = 'uint'
    unknown: typing.ClassVar[str] = 'unknown'
    vectorDataRoleHint: typing.ClassVar[str] = 'vectorDataRoleHint'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Volume(pxr.UsdGeom.Gprim):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def BlockFieldRelationship(*args, **kwargs):
        ...
    @staticmethod
    def CreateFieldRelationship(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetFieldPath(*args, **kwargs):
        ...
    @staticmethod
    def GetFieldPaths(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def HasFieldRelationship(*args, **kwargs):
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
__MFB_FULL_PACKAGE_NAME: str = 'usdVol'
