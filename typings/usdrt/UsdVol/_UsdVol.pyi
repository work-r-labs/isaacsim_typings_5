from __future__ import annotations
import typing
import usdrt.Sdf._Sdf
import usdrt.Usd._Usd
import usdrt.UsdGeom._UsdGeom
__all__ = ['Field3DAsset', 'FieldAsset', 'FieldBase', 'OpenVDBAsset', 'Tokens', 'Volume']
class Field3DAsset(FieldAsset):
    @staticmethod
    def Define(stage: usdrt.Usd._Usd.Stage, path: usdrt.Sdf._Sdf.Path) -> Field3DAsset:
        ...
    @staticmethod
    def GetSchemaTypeName() -> TfToken:
        ...
    def CreateFieldDataTypeAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def CreateFieldPurposeAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def GetFieldDataTypeAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def GetFieldPurposeAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def __bool__(self) -> bool:
        ...
    @typing.overload
    def __init__(self, arg0: usdrt.Usd._Usd.Prim) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: usdrt.Usd._Usd.SchemaBase) -> None:
        ...
    def __repr__(self) -> str:
        ...
class FieldAsset(FieldBase):
    @staticmethod
    def GetSchemaTypeName() -> TfToken:
        ...
    def CreateFieldDataTypeAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def CreateFieldIndexAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def CreateFieldNameAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def CreateFilePathAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def CreateVectorDataRoleHintAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def GetFieldDataTypeAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def GetFieldIndexAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def GetFieldNameAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def GetFilePathAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def GetVectorDataRoleHintAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def __bool__(self) -> bool:
        ...
    @typing.overload
    def __init__(self, arg0: usdrt.Usd._Usd.Prim) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: usdrt.Usd._Usd.SchemaBase) -> None:
        ...
    def __repr__(self) -> str:
        ...
class FieldBase(usdrt.UsdGeom._UsdGeom.Xformable):
    @staticmethod
    def GetSchemaTypeName() -> TfToken:
        ...
    def __bool__(self) -> bool:
        ...
    @typing.overload
    def __init__(self, arg0: usdrt.Usd._Usd.Prim) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: usdrt.Usd._Usd.SchemaBase) -> None:
        ...
    def __repr__(self) -> str:
        ...
class OpenVDBAsset(FieldAsset):
    @staticmethod
    def Define(stage: usdrt.Usd._Usd.Stage, path: usdrt.Sdf._Sdf.Path) -> OpenVDBAsset:
        ...
    @staticmethod
    def GetSchemaTypeName() -> TfToken:
        ...
    def CreateFieldClassAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def CreateFieldDataTypeAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def GetFieldClassAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def GetFieldDataTypeAttr(self) -> usdrt.Usd._Usd.Attribute:
        ...
    def __bool__(self) -> bool:
        ...
    @typing.overload
    def __init__(self, arg0: usdrt.Usd._Usd.Prim) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: usdrt.Usd._Usd.SchemaBase) -> None:
        ...
    def __repr__(self) -> str:
        ...
class Tokens:
    bool_: typing.ClassVar[str] = 'bool'
    color: typing.ClassVar[str] = 'Color'
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
    none: typing.ClassVar[str] = 'None'
    normal: typing.ClassVar[str] = 'Normal'
    point: typing.ClassVar[str] = 'Point'
    quatd: typing.ClassVar[str] = 'quatd'
    staggered: typing.ClassVar[str] = 'staggered'
    string: typing.ClassVar[str] = 'string'
    uint: typing.ClassVar[str] = 'uint'
    unknown: typing.ClassVar[str] = 'unknown'
    vector: typing.ClassVar[str] = 'Vector'
    vectorDataRoleHint: typing.ClassVar[str] = 'vectorDataRoleHint'
class Volume(usdrt.UsdGeom._UsdGeom.Gprim):
    @staticmethod
    def Define(stage: usdrt.Usd._Usd.Stage, path: usdrt.Sdf._Sdf.Path) -> Volume:
        ...
    @staticmethod
    def GetSchemaTypeName() -> TfToken:
        ...
    def __bool__(self) -> bool:
        ...
    @typing.overload
    def __init__(self, arg0: usdrt.Usd._Usd.Prim) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: usdrt.Usd._Usd.SchemaBase) -> None:
        ...
    def __repr__(self) -> str:
        ...
