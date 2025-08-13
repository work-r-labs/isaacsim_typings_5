from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb.events._events import AdapterType
from carb.events._events import IEvent
from carb.events._events import IEventStream
from carb.events._events import IEvents
from carb.events._events import IEventsAdapter
from carb.events._events import ISubscription
from carb.events._events import MappingEntry
from carb.events._events import acquire_events_adapter_interface
from carb.events._events import acquire_events_interface
from carb.events._events import register_event_alias
from carb.events._events import type_from_string
from carb.events._events import unregister_event_alias
import inspect as inspect
from . import _events
__all__: list[str] = ['AdapterType', 'IEvent', 'IEventStream', 'IEvents', 'IEventsAdapter', 'ISubscription', 'MappingEntry', 'acquire_events_adapter_interface', 'acquire_events_interface', 'asyncio', 'carb', 'get_events_adapter_interface', 'get_events_interface', 'inspect', 'register_event_alias', 'type_from_string', 'unregister_event_alias']
def _next_event(self: _events.IEventStream, order: int = 0, name: str = ''):
    """
    Async wait for next event.
    """
def _next_event_by_type(self: _events.IEventStream, event_type: int, order: int = 0, name: str = ''):
    """
    Async wait for next event of particular type.
    """
def get_events_adapter_interface() -> _events.IEvents:
    """
    Returns cached :class:`carb.events.IEvents` interface
    """
def get_events_interface() -> _events.IEvents:
    """
    Returns cached :class:`carb.events.IEvents` interface
    """
__copyright__: str = 'Copyright (c) 2019-2021, NVIDIA CORPORATION. All rights reserved.'
__license__: str = '\nNVIDIA CORPORATION and its licensors retain all intellectual property\nand proprietary rights in and to this software, related documentation\nand any modifications thereto. Any use, reproduction, disclosure or\ndistribution of this software and related documentation without an express\nlicense agreement from NVIDIA CORPORATION is strictly prohibited.\n'
