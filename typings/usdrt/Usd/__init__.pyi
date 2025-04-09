from __future__ import annotations
import omni as omni
from usdrt import Sdf
from usdrt.Usd._Usd import APISchemaBase
from usdrt.Usd._Usd import Access
from usdrt.Usd._Usd import AttrSpec
from usdrt.Usd._Usd import Attribute
from usdrt.Usd._Usd import ClipsAPI
from usdrt.Usd._Usd import CollectionAPI
from usdrt.Usd._Usd import ListPosition
from usdrt.Usd._Usd import ModelAPI
from usdrt.Usd._Usd import Prim
from usdrt.Usd._Usd import PrimRange
from usdrt.Usd._Usd import Relationship
from usdrt.Usd._Usd import SchemaBase
from usdrt.Usd._Usd import SchemaRegistry
from usdrt.Usd._Usd import Stage
from usdrt.Usd._Usd import TimeCode
from usdrt.Usd._Usd import Tokens
from usdrt.Usd._Usd import Typed
from usdrt.Usd._Usd import UsdCollectionMembershipQuery
from . import _Usd
__all__ = ['APISchemaBase', 'Access', 'AttrSpec', 'Attribute', 'ClipsAPI', 'CollectionAPI', 'ListPosition', 'ModelAPI', 'Overwrite', 'Prim', 'PrimRange', 'Read', 'ReadWrite', 'Relationship', 'SchemaBase', 'SchemaRegistry', 'Sdf', 'Stage', 'TimeCode', 'Tokens', 'Typed', 'UsdCollectionMembershipQuery', 'omni']
Overwrite: _Usd.Access  # value = <Access.Overwrite: 3>
Read: _Usd.Access  # value = <Access.Read: 1>
ReadWrite: _Usd.Access  # value = <Access.ReadWrite: 2>
__copyright__: str = 'Copyright (c) 2020-2021, NVIDIA CORPORATION. All rights reserved.'
__license__: str = '\nNVIDIA CORPORATION and its licensors retain all intellectual property\nand proprietary rights in and to this software, related documentation\nand any modifications thereto. Any use, reproduction, disclosure or\ndistribution of this software and related documentation without an express\nlicense agreement from NVIDIA CORPORATION is strictly prohibited.\n'
