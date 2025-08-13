"""

* Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
*
* NVIDIA CORPORATION and its licensors retain all intellectual property
* and proprietary rights in and to this software, related documentation
* and any modifications thereto.  Any use, reproduction, disclosure or
* distribution of this software and related documentation without an express
* license agreement from NVIDIA CORPORATION is strictly prohibited.
"""
from __future__ import annotations
from pxr import Usd
import pxr.Usd
from pxr import UsdUtils
__all__: list = ['UsdStageHelper']
class UsdStageHelper:
    """
    DEPRECATED: Keeps the stage ID or returns the stage from the current context
    """
    def __init__(self, stage: pxr.Usd.Stage):
        ...
    def _get_stage(self) -> typing.Optional[pxr.Usd.Stage]:
        ...
