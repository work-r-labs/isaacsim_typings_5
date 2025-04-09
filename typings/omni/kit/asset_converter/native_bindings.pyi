from __future__ import annotations
from asset_converter_native_bindings import OmniAssetConverter
import asset_converter_native_bindings._assetconverter
from asset_converter_native_bindings._assetconverter import Content
from asset_converter_native_bindings._assetconverter import MaterialDescription
from asset_converter_native_bindings._assetconverter import MaterialLoaderOutput
from asset_converter_native_bindings._assetconverter import MaterialProperty
from asset_converter_native_bindings._assetconverter import OmniConverterBlob
from asset_converter_native_bindings._assetconverter import OmniConverterFuture
from asset_converter_native_bindings._assetconverter import OmniConverterMDLPropertyType
from asset_converter_native_bindings._assetconverter import OmniConverterStatus
from asset_converter_native_bindings._assetconverter import omniConverterCancelFuture
from asset_converter_native_bindings._assetconverter import omniConverterCheckFutureStatus
from asset_converter_native_bindings._assetconverter import omniConverterCreateAsset
from asset_converter_native_bindings._assetconverter import omniConverterCreateUSD
from asset_converter_native_bindings._assetconverter import omniConverterGetFutureDetailedError
from asset_converter_native_bindings._assetconverter import omniConverterPopulateMaterials
from asset_converter_native_bindings._assetconverter import omniConverterReleaseFuture
from asset_converter_native_bindings._assetconverter import omniConverterSetCacheFolder
from asset_converter_native_bindings._assetconverter import omniConverterSetFileCallbacks
from asset_converter_native_bindings._assetconverter import omniConverterSetLogCallback
from asset_converter_native_bindings._assetconverter import omniConverterSetMaterialCallback
from asset_converter_native_bindings._assetconverter import omniConverterSetNeurayLibCallbacks
from asset_converter_native_bindings._assetconverter import omniConverterSetProgressCallback
__all__ = ['ASSET', 'CANCELLED', 'COLOR3D', 'COLOR4D', 'Content', 'DIRECTORY_CREATE_FAILED', 'FILE_NOT_EXISTED', 'FILE_READ_ERROR', 'FILE_WRITE_ERROR', 'INCOMPLETE_IMPORT_FORMAT', 'IN_PROGRESS', 'MATRIX2D', 'MATRIX3D', 'MATRIX4D', 'MaterialDescription', 'MaterialLoaderOutput', 'MaterialProperty', 'NORMAL3D', 'OK', 'OMNI_CONVERTER_FLAGS_CREATE_WORLD_AS_DEFAULT_PRIM', 'OMNI_CONVERTER_FLAGS_DISABLE_INSTANCING', 'OMNI_CONVERTER_FLAGS_EMBED_FBX_TEXTURES', 'OMNI_CONVERTER_FLAGS_EMBED_MDL', 'OMNI_CONVERTER_FLAGS_EMBED_TEXTURES', 'OMNI_CONVERTER_FLAGS_EXPORT_AS_SHAPENET', 'OMNI_CONVERTER_FLAGS_EXPORT_EMBEDDED_GLTF', 'OMNI_CONVERTER_FLAGS_EXPORT_HIDDEN_PROPS', 'OMNI_CONVERTER_FLAGS_EXPORT_PREVIEW_SURFACE', 'OMNI_CONVERTER_FLAGS_FBX_BAKING_SCALES_INTO_MESH', 'OMNI_CONVERTER_FLAGS_FBX_CONVERT_TO_Y_UP', 'OMNI_CONVERTER_FLAGS_FBX_CONVERT_TO_Z_UP', 'OMNI_CONVERTER_FLAGS_FBX_IGNORE_UNBOUND_BONES', 'OMNI_CONVERTER_FLAGS_GEN_SMOOTH_NORMALS', 'OMNI_CONVERTER_FLAGS_IGNORE_ANIMATION', 'OMNI_CONVERTER_FLAGS_IGNORE_CAMERAS', 'OMNI_CONVERTER_FLAGS_IGNORE_FLIP_ROTATION', 'OMNI_CONVERTER_FLAGS_IGNORE_LIGHTS', 'OMNI_CONVERTER_FLAGS_IGNORE_MATERIALS', 'OMNI_CONVERTER_FLAGS_IGNORE_PIVOTS', 'OMNI_CONVERTER_FLAGS_IMPORT_GLTF_NV_MATERIALS_MDL', 'OMNI_CONVERTER_FLAGS_KEEP_ALL_MATERIALS', 'OMNI_CONVERTER_FLAGS_MERGE_ALL_MESHES', 'OMNI_CONVERTER_FLAGS_SINGLE_MESH_FILE', 'OMNI_CONVERTER_FLAGS_STAGE_UP_Y', 'OMNI_CONVERTER_FLAGS_STAGE_UP_Z', 'OMNI_CONVERTER_FLAGS_SUPPORT_POINTER_INSTANCER', 'OMNI_CONVERTER_FLAGS_USE_DOUBLE_PRECISION_FOR_USD_TRANSFORM_OP', 'OMNI_CONVERTER_FLAGS_USE_METER_PER_UNIT', 'OMNI_CONVERTER_MAJOR_VERSION', 'OMNI_CONVERTER_MINOR_VERSION', 'OmniAssetConverter', 'OmniConverterBlob', 'OmniConverterFuture', 'OmniConverterMDLPropertyType', 'OmniConverterStatus', 'POINT3D', 'QUATD', 'TEXCOORD2D', 'TEXCOORD3D', 'TOKEN', 'UNDEFINED', 'UNKNOWN', 'UNSUPPORTED_EXPORT_FORMAT', 'UNSUPPORTED_IMPORT_FORMAT', 'VECTOR3D', 'omniConverterCancelFuture', 'omniConverterCheckFutureStatus', 'omniConverterCreateAsset', 'omniConverterCreateUSD', 'omniConverterGetFutureDetailedError', 'omniConverterPopulateMaterials', 'omniConverterReleaseFuture', 'omniConverterSetCacheFolder', 'omniConverterSetFileCallbacks', 'omniConverterSetLogCallback', 'omniConverterSetMaterialCallback', 'omniConverterSetNeurayLibCallbacks', 'omniConverterSetProgressCallback']
ASSET: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.ASSET: 12>
CANCELLED: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.CANCELLED: 2>
COLOR3D: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.COLOR3D: 3>
COLOR4D: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.COLOR4D: 4>
DIRECTORY_CREATE_FAILED: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.DIRECTORY_CREATE_FAILED: 9>
FILE_NOT_EXISTED: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.FILE_NOT_EXISTED: 7>
FILE_READ_ERROR: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.FILE_READ_ERROR: 6>
FILE_WRITE_ERROR: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.FILE_WRITE_ERROR: 8>
INCOMPLETE_IMPORT_FORMAT: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.INCOMPLETE_IMPORT_FORMAT: 4>
IN_PROGRESS: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.IN_PROGRESS: 1>
MATRIX2D: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.MATRIX2D: 6>
MATRIX3D: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.MATRIX3D: 7>
MATRIX4D: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.MATRIX4D: 8>
NORMAL3D: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.NORMAL3D: 2>
OK: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.OK: 0>
OMNI_CONVERTER_FLAGS_CREATE_WORLD_AS_DEFAULT_PRIM: int = 1024
OMNI_CONVERTER_FLAGS_DISABLE_INSTANCING: int = 524288
OMNI_CONVERTER_FLAGS_EMBED_FBX_TEXTURES: int = 4096
OMNI_CONVERTER_FLAGS_EMBED_MDL: int = 256
OMNI_CONVERTER_FLAGS_EMBED_TEXTURES: int = 4096
OMNI_CONVERTER_FLAGS_EXPORT_AS_SHAPENET: int = 128
OMNI_CONVERTER_FLAGS_EXPORT_EMBEDDED_GLTF: int = 33554432
OMNI_CONVERTER_FLAGS_EXPORT_HIDDEN_PROPS: int = 1048576
OMNI_CONVERTER_FLAGS_EXPORT_PREVIEW_SURFACE: int = 32
OMNI_CONVERTER_FLAGS_FBX_BAKING_SCALES_INTO_MESH: int = 2097152
OMNI_CONVERTER_FLAGS_FBX_CONVERT_TO_Y_UP: int = 16384
OMNI_CONVERTER_FLAGS_FBX_CONVERT_TO_Z_UP: int = 8192
OMNI_CONVERTER_FLAGS_FBX_IGNORE_UNBOUND_BONES: int = 16777216
OMNI_CONVERTER_FLAGS_GEN_SMOOTH_NORMALS: int = 8
OMNI_CONVERTER_FLAGS_IGNORE_ANIMATION: int = 1
OMNI_CONVERTER_FLAGS_IGNORE_CAMERAS: int = 16
OMNI_CONVERTER_FLAGS_IGNORE_FLIP_ROTATION: int = 8388608
OMNI_CONVERTER_FLAGS_IGNORE_LIGHTS: int = 2048
OMNI_CONVERTER_FLAGS_IGNORE_MATERIALS: int = 2
OMNI_CONVERTER_FLAGS_IGNORE_PIVOTS: int = 262144
OMNI_CONVERTER_FLAGS_IMPORT_GLTF_NV_MATERIALS_MDL: int = 67108864
OMNI_CONVERTER_FLAGS_KEEP_ALL_MATERIALS: int = 32768
OMNI_CONVERTER_FLAGS_MERGE_ALL_MESHES: int = 65536
OMNI_CONVERTER_FLAGS_SINGLE_MESH_FILE: int = 4
OMNI_CONVERTER_FLAGS_STAGE_UP_Y: int = 134217728
OMNI_CONVERTER_FLAGS_STAGE_UP_Z: int = 268435456
OMNI_CONVERTER_FLAGS_SUPPORT_POINTER_INSTANCER: int = 64
OMNI_CONVERTER_FLAGS_USE_DOUBLE_PRECISION_FOR_USD_TRANSFORM_OP: int = 131072
OMNI_CONVERTER_FLAGS_USE_METER_PER_UNIT: int = 512
OMNI_CONVERTER_MAJOR_VERSION: int = 11
OMNI_CONVERTER_MINOR_VERSION: int = 0
POINT3D: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.POINT3D: 0>
QUATD: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.QUATD: 5>
TEXCOORD2D: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.TEXCOORD2D: 9>
TEXCOORD3D: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.TEXCOORD3D: 10>
TOKEN: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.TOKEN: 11>
UNDEFINED: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.UNDEFINED: 13>
UNKNOWN: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.UNKNOWN: 10>
UNSUPPORTED_EXPORT_FORMAT: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.UNSUPPORTED_EXPORT_FORMAT: 5>
UNSUPPORTED_IMPORT_FORMAT: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.UNSUPPORTED_IMPORT_FORMAT: 3>
VECTOR3D: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.VECTOR3D: 1>
