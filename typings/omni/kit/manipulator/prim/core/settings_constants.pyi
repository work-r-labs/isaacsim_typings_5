"""
This module defines constants and enums for manipulator placement settings and data registry event types in the omni.kit.manipulator.prim.core extension.
"""
from __future__ import annotations
import enum
from enum import IntEnum
from enum import auto
import typing
__all__: list = ['Constants', 'DataRegistryEventTypes', 'DataAccessorConstants']
class Constants:
    """
    A class containing constants related to manipulator settings.
    
        This class stores various constants used to configure the placement settings of manipulators in the application. These settings allow users to specify how manipulators are positioned relative to the selected objects. The constants include options for placing manipulators based on authored pivot points, selection centers, bounding box bases, bounding box centers, and reference primitives.
        
    """
    MANIPULATOR_PLACEMENT_BBOX_BASE: typing.ClassVar[str] = 'Bounding Box Base'
    MANIPULATOR_PLACEMENT_BBOX_CENTER: typing.ClassVar[str] = 'Bounding Box Center'
    MANIPULATOR_PLACEMENT_LAST_PRIM_PIVOT: typing.ClassVar[str] = 'Authored Pivot'
    MANIPULATOR_PLACEMENT_PICK_REF_PRIM: typing.ClassVar[str] = 'Pick Reference Prim'
    MANIPULATOR_PLACEMENT_SELECTION_CENTER: typing.ClassVar[str] = 'Selection Center'
    MANIPULATOR_PLACEMENT_SETTING: typing.ClassVar[str] = '/persistent/exts/omni.kit.manipulator.prim.core/manipulator/placement'
class DataAccessorConstants:
    """
    A class for defining constants related to data access priorities.
    
        This class contains class attributes that represent the priority levels for different types of data accessors within the system. The attributes define unique string paths used to identify and categorize the accessors based on their intended usage or the data type they handle, such as 'fabric' and 'usd'. These constants are utilized to manage the order of operations and precedence among various data manipulation tasks.
        
    """
    DATA_ACCESSOR_PRIORITY_FABRIC: typing.ClassVar[str] = '/exts/omni.kit.manipulator.prim.core/accessor/priority/fabric'
    DATA_ACCESSOR_PRIORITY_USD: typing.ClassVar[str] = '/exts/omni.kit.manipulator.prim.core/accessor/priority/usd'
    DATA_ACCESSOR_PRIORITY_WRITE_FABRIC: typing.ClassVar[str] = '/exts/omni.kit.manipulator.prim.core/accessor/prioritywrite/fabric'
    DATA_ACCESSOR_PRIORITY_WRITE_USD: typing.ClassVar[str] = '/exts/omni.kit.manipulator.prim.core/accessor/prioritywrite/usd'
class DataRegistryEventTypes(enum.IntEnum):
    """
    An enumeration for the types of events related to data registry.
    
        This enumeration defines the types of events that can be raised in relation to the data registry, such as when a data accessor is added or removed.
        
    """
    DATA_ACCESSOR_ADDED: typing.ClassVar[DataRegistryEventTypes]  # value = <DataRegistryEventTypes.DATA_ACCESSOR_ADDED: 1>
    DATA_ACCESSOR_REMOVED: typing.ClassVar[DataRegistryEventTypes]  # value = <DataRegistryEventTypes.DATA_ACCESSOR_REMOVED: 2>
