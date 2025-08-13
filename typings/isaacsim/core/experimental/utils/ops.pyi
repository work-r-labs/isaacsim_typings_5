from __future__ import annotations
from isaacsim.core.experimental.utils.impl.ops import broadcast_to
from isaacsim.core.experimental.utils.impl.ops import place
from isaacsim.core.experimental.utils.impl.ops import resolve_indices
import numpy
import numpy as np
import warp as wp
import warp.types
__all__: list[str] = ['broadcast_to', 'np', 'np_dtype_to_warp_type', 'place', 'resolve_indices', 'wp']
np_dtype_to_warp_type: dict  # value = {numpy.bool_: warp.types.bool, numpy.int8: warp.types.int8, numpy.uint8: warp.types.uint8, numpy.int16: warp.types.int16, numpy.uint16: warp.types.uint16, numpy.int32: warp.types.int32, numpy.int64: warp.types.int64, numpy.uint32: warp.types.uint32, numpy.uint64: warp.types.uint64, numpy.float16: warp.types.float16, numpy.float32: warp.types.float32, numpy.float64: warp.types.float64, dtype('bool'): warp.types.bool, dtype('int8'): warp.types.int8, dtype('uint8'): warp.types.uint8, dtype('int16'): warp.types.int16, dtype('uint16'): warp.types.uint16, dtype('int32'): warp.types.int32, dtype('int64'): warp.types.int64, dtype('uint32'): warp.types.uint32, dtype('uint64'): warp.types.uint64, dtype('float16'): warp.types.float16, dtype('float32'): warp.types.float32, dtype('float64'): warp.types.float64}
