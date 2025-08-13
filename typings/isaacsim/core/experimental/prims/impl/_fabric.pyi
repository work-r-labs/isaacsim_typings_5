from __future__ import annotations
import usdrt as usdrt
import warp as wp
import warp.context
__all__: list[str] = ['update_fabric_selection', 'usdrt', 'wk_compose_fabric_transformation_matrix_from_warp_arrays', 'wk_decompose_fabric_transformation_matrix_to_warp_arrays', 'wk_write_to_fabric_float', 'wp']
def update_fabric_selection(*, stage: usdrt.Usd._Usd.Stage, data: dict, device: warp.context.Device, attr: str, count: int) -> bool:
    ...
_decompose: warp.context.Function  # value = <Function _decompose(m: mat44(f))>
_wk_selection_mapping: warp.context.Kernel  # value = <warp.context.Kernel object>
wk_compose_fabric_transformation_matrix_from_warp_arrays: warp.context.Kernel  # value = <warp.context.Kernel object>
wk_decompose_fabric_transformation_matrix_to_warp_arrays: warp.context.Kernel  # value = <warp.context.Kernel object>
wk_write_to_fabric_float: warp.context.Kernel  # value = <warp.context.Kernel object>
