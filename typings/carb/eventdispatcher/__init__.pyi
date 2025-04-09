from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb.eventdispatcher._eventdispatcher import Event
from carb.eventdispatcher._eventdispatcher import IEventDispatcher
from carb.eventdispatcher._eventdispatcher import IMessageQueue
from carb.eventdispatcher._eventdispatcher import IMessageQueueFactory
from carb.eventdispatcher._eventdispatcher import ObserverGuard
from carb.eventdispatcher._eventdispatcher import acquire_eventdispatcher_interface
from carb.eventdispatcher._eventdispatcher import acquire_messagequeue_factory_interface
from functools import lru_cache
from . import _eventdispatcher
__all__ = ['Event', 'IEventDispatcher', 'IMessageQueue', 'IMessageQueueFactory', 'ObserverGuard', 'acquire_eventdispatcher_interface', 'acquire_messagequeue_factory_interface', 'asyncio', 'carb', 'get_eventdispatcher', 'get_eventdispatcher_interface', 'get_messagequeue_factory', 'get_messagequeue_factory_interface', 'lru_cache']
def _pop(self, fn):
    """
    Waits until a message has been pushed to the queue and might be available. Returns after the message is handled.
    
        Note, this function must be awaited. The message is removed from the queue atomically before processing. In a
        single-owner-thread situation this function must be called within the context of the owning thread.
    
        If a task or thread is waiting on the message, the message will be considered 'completed' and unblock the waiting
        task/thread as soon as fn() returns, even if the carb.eventdispatcher.Event passed to the function is retained.
    
        This function returns once a message is processed. If the queue is stopped with stop() while awaiting, this function
        will stop waiting and will throw IndexError.
    
        Args:
            fn: (function) A function that is called with a carb.eventdispatcher.Event as the only parameter.
    
        Returns:
            None
    
        Raises:
            IndexError: The message queue has been stopped.
            RuntimeError: The calling thread is not the owner thread, or another error.
    """
def _push(self, event_name, payload: dict = None):
    """
    Posts a message to the message queue without waiting for the message to be processed.
    
        Args:
            event_name: (str) The event name for the message.
            payload: (dict) (optional) A dictionary that functions as the payload for the message.
    
        Returns:
            None
    
        Raises:
            IndexError: The message queue has been stopped.
            MemoryError: Failed to allocate memory for the message.
            RuntimeError: Any other error.)
    """
def _push_and_wait(self, event_name, payload: dict = None):
    """
    Pushes a message to the message queue and does not return until the message is processed.
    
        Note, this function must be awaited. For a function that pushes a message without waiting, use push().
    
        Args:
            event_name: (str) The event name for the message
            payload: (dict) (optional) A dictionary that functions as the payload for the message.
    
        Returns:
            None
    
        Raises:
            IndexError: The message queue has been stopped.
            MemoryError: Failed to allocate memory for the message.
            RuntimeError: Any other error.
    """
def get_eventdispatcher() -> _eventdispatcher.IEventDispatcher:
    """
    Returns cached :class:`carb.eventdispatcher.IEventDispatcher` interface (shorthand).
    """
def get_eventdispatcher_interface(*args, **kwargs):
    """
    Returns cached :class:`carb.eventdispatcher.IEventDispatcher` interface
    """
def get_messagequeue_factory() -> _eventdispatcher.IMessageQueueFactory:
    """
    Returns cached :class:`carb.eventdispatcher.IMessageQueueFactory` interface (shorthand)
    """
def get_messagequeue_factory_interface(*args, **kwargs):
    """
    Returns cached :class:`carb.eventdispatcher.IMessageQueueFactory` interface
    """
__copyright__: str = 'Copyright (c) 2022, NVIDIA CORPORATION. All rights reserved.'
__license__: str = '\nNVIDIA CORPORATION and its licensors retain all intellectual property\nand proprietary rights in and to this software, related documentation\nand any modifications thereto. Any use, reproduction, disclosure or\ndistribution of this software and related documentation without an express\nlicense agreement from NVIDIA CORPORATION is strictly prohibited.\n'
