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
import omni as omni
from omni.kit.asset_converter.impl.context import AssetConverterContext
from omni.kit.asset_converter.impl.task_manager import AssetConverterTaskManager
import weakref as weakref
__all__: list = ['AssetImporterExtension', 'get_instance']
class AssetImporterExtension(omni.ext._extensions.IExt):
    def _create_mdl_module(self, usd_identifier, db_scope_name):
        ...
    def _create_temporary_db_scope(self):
        ...
    def _destroy_mdl_module(self, db_name):
        ...
    def _destroy_temporary_db_scope(self, db_scope_name):
        ...
    def create_converter_task(self, import_path: str, output_path: str, progress_callback: typing.Callable[[int], int] = None, asset_converter_context: omni.kit.asset_converter.impl.context.AssetConverterContext = ..., material_loader = None, close_stage_and_reopen_if_opened: bool = False):
        """
        
                Creates task to convert import_path to output_path. Currently, it supports
                to convert fbx/obj/glTF to USD, or USD to fbx/obj/glTF.
        
                Snippet to use it:
                >>> import asyncio
                >>> importer omni.kit.asset_converter as converter
                >>>
                >>> async def convert(...):
                >>>     task_manger = converter.get_instance()
                >>>     task = task_manger.create_converter_task(...)
                >>>     success = await task.wait_until_finished()
                >>>     if not success:
                >>>         detailed_status_code = task.get_status()
                >>>         detailed_status_error_string = task.get_error_message()
        
                NOTE: It uses FBX SDK for FBX convert and Assimp as fallback backend, so it should support
                all assets that Assimp supports. But only obj/glTF are fully verified.
        
                Args:
                    import_path (str): The source asset to be converted. It could also be stage id that's
                                       cached in UsdUtils.StageCache since it supports to export loaded stage.
        
                    output_path (str): The target asset. Asset format is decided by its extension.
        
                    progress_callback(Callable[[int], int]): Progress callback to monitor the progress of
                                                           conversion. The first param is the progress, and
                                                           the second one is the total steps.
                    asset_converter_context (omni.kit.asset_converter.AssetConverterContext): Context.
        
                    material_loader (Callable[[omni.kit.asset_conerter.native_bindings.MaterialDescription], None]): You
                                                           can set this to intercept the material loading.
        
                    close_stage_and_reopen_if_opened (bool): If the output path has already been opened in the
                                                             current UsdContext, it will close the current stage, then import
                                                             and re-open it after import successfully if this flag is true. Otherwise,
                                                             it will return False and report errors.
                
        """
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
def get_instance():
    ...
ASSET: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.ASSET: 12>
CANCELLED: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.CANCELLED: 2>
COLOR3D: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.COLOR3D: 3>
COLOR4D: asset_converter_native_bindings._assetconverter.OmniConverterMDLPropertyType  # value = <OmniConverterMDLPropertyType.COLOR4D: 4>
DIRECTORY_CREATE_FAILED: asset_converter_native_bindings._assetconverter.OmniConverterStatus  # value = <OmniConverterStatus.DIRECTORY_CREATE_FAILED: 9>
ENABLE_NEURAYLIB_UTILS: bool = True
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
_global_instance: weakref.ReferenceType  # value = <weakref at 0x709fbf39d620; to 'AssetImporterExtension' at 0x709fbe70b290>
