from __future__ import annotations
import typing
import usdrt.helpers._helpers
__all__ = ['AncestorsRange', 'AssetPath', 'Path', 'ValueTypeName', 'ValueTypeNames']
class AncestorsRange:
    def GetPath(self) -> Path:
        ...
    def __init__(self, arg0: Path) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
class AssetPath:
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: AssetPath) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, path: str) -> None:
        ...
    @typing.overload
    def __init__(self, path: str, resolvedPath: str) -> None:
        ...
    def __ne__(self, arg0: AssetPath) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    @property
    def path(self) -> str:
        ...
    @property
    def resolvedPath(self) -> str:
        ...
class Path:
    absoluteRootPath: typing.ClassVar[Path]  # value = Sdf.Path('/')
    emptyPath: typing.ClassVar[Path]  # value = Sdf.Path('')
    @staticmethod
    def IsValidIdentifier(name: str) -> bool:
        ...
    @staticmethod
    def IsValidNamespacedIdentifier(name: str) -> bool:
        ...
    @staticmethod
    def IsValidPathString(pathString: str) -> bool:
        ...
    @staticmethod
    @typing.overload
    def JoinIdentifier(lhs: str, rhs: str) -> str:
        ...
    @staticmethod
    @typing.overload
    def JoinIdentifier(lhs: TfToken, rhs: TfToken) -> str:
        ...
    @staticmethod
    @typing.overload
    def JoinIdentifier(names: list[TfToken]) -> str:
        ...
    @staticmethod
    def StripPrefixNamespace(name: str, matchNamespace: str) -> tuple:
        ...
    @staticmethod
    def TokenizeIdentifier(name: str) -> list[str]:
        ...
    def AppendChild(self, childName: TfToken) -> Path:
        ...
    def AppendPath(self, newSuffix: Path) -> Path:
        ...
    def AppendProperty(self, propName: TfToken) -> Path:
        ...
    def ContainsPropertyElements(self) -> bool:
        ...
    def GetAbsoluteRootOrPrimPath(self) -> Path:
        ...
    def GetAncestorsRange(self) -> ...:
        ...
    def GetCommonPrefix(self, path: Path) -> Path:
        ...
    def GetNameToken(self) -> TfToken:
        ...
    def GetParentPath(self) -> Path:
        ...
    def GetPrefixes(self) -> list[Path]:
        ...
    @typing.overload
    def GetPrimPath(self) -> Path:
        ...
    @typing.overload
    def GetPrimPath(self) -> Path:
        ...
    def GetString(self) -> str:
        ...
    def GetText(self) -> str:
        ...
    def GetToken(self) -> TfToken:
        ...
    def HasPrefix(self, prefix: Path) -> bool:
        ...
    def IsAbsolutePath(self) -> bool:
        ...
    def IsAbsoluteRootOrPrimPath(self) -> bool:
        ...
    def IsAbsoluteRootPath(self) -> bool:
        ...
    def IsEmpty(self) -> bool:
        ...
    def IsNamespacedPropertyPath(self) -> bool:
        ...
    def IsPrimPath(self) -> bool:
        ...
    def IsPrimPropertyPath(self) -> bool:
        ...
    def IsPropertyPath(self) -> bool:
        ...
    def IsRootPrimPath(self) -> bool:
        ...
    def RemoveCommonSuffix(self, otherPath: Path, stopAtRootPrim: bool = False) -> tuple[Path, Path]:
        ...
    def ReplaceName(self, newName: TfToken) -> Path:
        ...
    def ReplacePrefix(self, oldPrefix: Path, newPrefix: Path, fixTargetPaths: bool = True) -> Path:
        ...
    def __eq__(self, arg0: Path) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: Path) -> None:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    def __lt__(self, arg0: Path) -> bool:
        ...
    def __ne__(self, arg0: Path) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    @property
    def isEmpty(self) -> bool:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def pathC(self) -> usdrt.helpers._helpers.PathC:
        ...
    @property
    def pathElementCount(self) -> int:
        ...
    @property
    def pathString(self) -> str:
        ...
class ValueTypeName:
    def GetAsString(self) -> str:
        ...
    def GetAsToken(self) -> TfToken:
        ...
    def GetAsTypeC(self) -> ...:
        ...
    def __eq__(self, arg0: ValueTypeName) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __init__(self) -> None:
        ...
    def __ne__(self, arg0: ValueTypeName) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def arrayType(self) -> ValueTypeName:
        ...
    @property
    def isArray(self) -> bool:
        ...
    @property
    def isScalar(self) -> bool:
        ...
    @property
    def scalarType(self) -> ValueTypeName:
        ...
class ValueTypeNames:
    AncestorPrimTypeTag: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('tag (ancestorPrimTypeName)')
    AppliedSchemaTypeTag: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('tag (appliedSchema)')
    Asset: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('asset')
    AssetArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('asset[]')
    Bool: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('bool')
    BoolArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('bool[]')
    Color3d: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double3 (color)')
    Color3dArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double3[] (color)')
    Color3f: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float3 (color)')
    Color3fArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float3[] (color)')
    Color3h: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half3 (color)')
    Color3hArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half3[] (color)')
    Color4d: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double4 (color)')
    Color4dArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double4[] (color)')
    Color4f: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float4 (color)')
    Color4fArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float4[] (color)')
    Color4h: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half4 (color)')
    Color4hArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half4[] (color)')
    Double: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double')
    Double2: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double2')
    Double2Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double2[]')
    Double3: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double3')
    Double3Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double3[]')
    Double4: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double4')
    Double4Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double4[]')
    DoubleArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double[]')
    Float: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float')
    Float2: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float2')
    Float2Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float2[]')
    Float3: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float3')
    Float3Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float3[]')
    Float4: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float4')
    Float4Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float4[]')
    FloatArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float[]')
    Frame4d: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double16 (frame)')
    Frame4dArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double16[] (frame)')
    Half: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half')
    Half2: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half2')
    Half2Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half2[]')
    Half3: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half3')
    Half3Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half3[]')
    Half4: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half4')
    Half4Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half4[]')
    HalfArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half[]')
    Int: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('int')
    Int2: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('int2')
    Int2Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('int2[]')
    Int3: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('int3')
    Int3Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('int3[]')
    Int4: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('int4')
    Int4Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('int4[]')
    Int64: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('int64')
    Int64Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('int64[]')
    IntArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('int[]')
    Matrix2d: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double4 (matrix)')
    Matrix2dArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double4[] (matrix)')
    Matrix3d: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double9 (matrix)')
    Matrix3dArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double9[] (matrix)')
    Matrix4d: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double16 (matrix)')
    Matrix4dArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double16[] (matrix)')
    Normal3d: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double3 (normal)')
    Normal3dArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double3[] (normal)')
    Normal3f: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float3 (normal)')
    Normal3fArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float3[] (normal)')
    Normal3h: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half3 (normal)')
    Normal3hArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half3[] (normal)')
    Point3d: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double3 (position)')
    Point3dArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double3[] (position)')
    Point3f: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float3 (position)')
    Point3fArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float3[] (position)')
    Point3h: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half3 (position)')
    Point3hArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half3[] (position)')
    PrimTypeTag: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('tag (primTypeName)')
    Quatd: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double4 (quaternion)')
    QuatdArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double4[] (quaternion)')
    Quatf: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float4 (quaternion)')
    QuatfArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float4[] (quaternion)')
    Quath: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half4 (quaternion)')
    QuathArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half4[] (quaternion)')
    Range3d: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double6')
    String: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('uchar[] (text)')
    StringArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('uchar[][] (text)')
    Tag: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('tag')
    TexCoord2d: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double2 (texCoord)')
    TexCoord2dArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double2[] (texCoord)')
    TexCoord2f: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float2 (texCoord)')
    TexCoord2fArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float2[] (texCoord)')
    TexCoord2h: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half2 (texCoord)')
    TexCoord2hArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half2[] (texCoord)')
    TexCoord3d: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double3 (texCoord)')
    TexCoord3dArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double3[] (texCoord)')
    TexCoord3f: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float3 (texCoord)')
    TexCoord3fArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float3[] (texCoord)')
    TexCoord3h: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half3 (texCoord)')
    TexCoord3hArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half3[] (texCoord)')
    TimeCode: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double (timecode)')
    TimeCodeArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double[] (timecode)')
    Token: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('token')
    TokenArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('token[]')
    UChar: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('uchar')
    UCharArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('uchar[]')
    UInt: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('uint')
    UInt64: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('uint64')
    UInt64Array: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('uint64[]')
    UIntArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('uint[]')
    Vector3d: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double3 (vector)')
    Vector3dArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('double3[] (vector)')
    Vector3f: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float3 (vector)')
    Vector3fArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('float3[] (vector)')
    Vector3h: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half3 (vector)')
    Vector3hArray: typing.ClassVar[ValueTypeName]  # value = Sdf.ValueTypeName('half3[] (vector)')
