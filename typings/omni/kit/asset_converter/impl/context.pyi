from __future__ import annotations
import typing
__all__: list = ['AssetConverterContext']
class AssetConverterContext:
    bake_mdl_material: typing.ClassVar[bool] = False
    baking_scales: typing.ClassVar[bool] = False
    convert_fbx_to_y_up: typing.ClassVar[bool] = False
    convert_fbx_to_z_up: typing.ClassVar[bool] = False
    convert_stage_up_y: typing.ClassVar[bool] = False
    convert_stage_up_z: typing.ClassVar[bool] = False
    create_world_as_default_root_prim: typing.ClassVar[bool] = True
    disabling_instancing: typing.ClassVar[bool] = False
    embed_mdl_in_usd: typing.ClassVar[bool] = True
    embed_textures: typing.ClassVar[bool] = True
    export_hidden_props: typing.ClassVar[bool] = False
    export_mdl_gltf_extension: typing.ClassVar[bool] = False
    export_preview_surface: typing.ClassVar[bool] = False
    export_separate_gltf: typing.ClassVar[bool] = False
    ignore_animations: typing.ClassVar[bool] = False
    ignore_camera: typing.ClassVar[bool] = False
    ignore_flip_rotations: typing.ClassVar[bool] = False
    ignore_light: typing.ClassVar[bool] = False
    ignore_materials: typing.ClassVar[bool] = False
    ignore_pivots: typing.ClassVar[bool] = False
    ignore_unbound_bones: typing.ClassVar[bool] = False
    keep_all_materials: typing.ClassVar[bool] = False
    merge_all_meshes: typing.ClassVar[bool] = False
    single_mesh: typing.ClassVar[bool] = False
    smooth_normals: typing.ClassVar[bool] = True
    support_point_instancer: typing.ClassVar[bool] = False
    use_double_precision_to_usd_transform_op: typing.ClassVar[bool] = False
    use_meter_as_world_unit: typing.ClassVar[bool] = False
    def to_dict(self):
        ...
