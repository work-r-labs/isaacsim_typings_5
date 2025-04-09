"""
Bindings for `carb::tokens::ITokens` interface. It is used for storing tokens and resolving strings containing them.
"""
from __future__ import annotations
from carb.tokens._tokens import ITokens
from carb.tokens._tokens import acquire_tokens_interface
from . import _tokens
__all__ = ['ITokens', 'RESOLVE_FLAG_LEAVE_TOKEN_IF_NOT_FOUND', 'RESOLVE_FLAG_NONE', 'acquire_tokens_interface', 'get_tokens_interface']
def get_tokens_interface() -> _tokens.ITokens:
    """
    Returns cached :class:`carb.tokens.ITokens` interface
    """
RESOLVE_FLAG_LEAVE_TOKEN_IF_NOT_FOUND: int = 1
RESOLVE_FLAG_NONE: int = 0
__copyright__: str = 'Copyright (c) 2020-2021, NVIDIA CORPORATION. All rights reserved.'
__license__: str = '\nNVIDIA CORPORATION and its licensors retain all intellectual property\nand proprietary rights in and to this software, related documentation\nand any modifications thereto. Any use, reproduction, disclosure or\ndistribution of this software and related documentation without an express\nlicense agreement from NVIDIA CORPORATION is strictly prohibited.\n'
