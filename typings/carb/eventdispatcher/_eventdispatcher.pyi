from __future__ import annotations
import typing
__all__: list[str] = ['Event', 'IEventDispatcher', 'IMessageQueue', 'IMessageQueueFactory', 'Observer', 'ObserverGuard', 'acquire_eventdispatcher_interface', 'acquire_messagequeue_factory_interface']
class Event:
    """
    Event.
    
            Contains the event_name and payload for a dispatched event.
        
    """
    def __contains__(self, item: typing.Any) -> bool:
        """
        Membership test operator.
        
        Returns:
            True if the event arguments contain `item`; False otherwise.
        """
    def __getitem__(self, key_name: str) -> typing.Any:
        """
        Accesses a payload item by key name.
        
        Args:
            key_name: The name of a key to find in the payload.
        
        Returns:
            None if the key is not present, otherwise returns an object representative of the type in the payload.
        """
    def __len__(self) -> int:
        """
        Length operator.
        
        Returns:
            The number of event arguments contained by `self`.
        """
    def get(self, key_name: str) -> typing.Any:
        """
        Accesses a payload item by key name.
        
        Args:
            key_name: The name of a key to find in the payload.
        
        Returns:
            None if the key is not present, otherwise returns an object representative of the type in the payload.
        """
    def has_key(self, key_name: str) -> bool:
        """
        Returns True if a given key name is present in the payload.
        
        Args:
            key_name: The name of a key to check against the payload.
        
        Returns:
            `True` if the key is present in the payload; `False` otherwise.
        """
    @property
    def event_name(self) -> str:
        """
        The name of the event
        """
    @property
    def payload(self) -> dict:
        """
        Returns the event parameters as a dict.
        
        NOTE: The return value is built on demand, so the first call to this property is more expensive. Instead, consider using
        `self` directly since it supports __getitem__ and __contains__.
        
        Returns:
            A dict of the event arguments.
        """
class IEventDispatcher:
    """
    """
    def add_event_alias(self, target_name: str, alias_name: str) -> bool:
        """
        Adds an alias that can be used to observe and dispatch as a different event.
        
        Event aliases are a powerful tool. An *alias target* may have as many aliases as necessary, but an *alias* may
        not have any aliases of its own. Similarly, an *alias target* may not function as an *alias* for any other
        *alias target*.
        
        Thus an *alias target* is considered a primary event, and any *aliases* that it is known by can also be used to
        dispatch or receive events.
        
        Dispatching to an *alias* acts the same as dispatching to an *alias target* directly: Any observers of any
        *aliases* for that *alias target* will observe the event, as well as the *alias target* itself. However, the
        `Event.event_name` property will be the same as the *alias* they're observing, **not** the *alias target* and
        potentially not even the *alias* that was dispatched. See `observe_event()` for more information.
        
        Aliases can be removed with `remove_event_alias()` or `remove_all_event_aliases_for()`.
        
        While it is possible to add or remove an alias from an observer callback, it will not affect the current event
        dispatch.
        
        Args:
            target_name: (str) The target event to create an alias for.
            alias_name: (str) The alias that will refer to `target_name`.
        
        Returns:
            `True` if a new alias was created, or `False` for one of the following reasons: `target_name` and `alias_name` are
            the same, `target_name` or `alias_name` are already used as aliases or targets respectively, or `alias_name` already
            exists as a target of `target_name`.
        """
    def dispatch_event(self, event_name: str, payload: typing.Any = None) -> int:
        """
        Dispatches an event and immediately calls all observers that would observe this particular event.
        
        Finds and calls all observers (in the current thread) that observe the given event signature.
        
        It is safe to recursively dispatch events (i.e. call `dispatch_event()` from within a called observer), but care must be
        taken to avoid endless recursion. See the rules in :func:`.observe_event()` for observers added during a
        `dispatch_event()` call.
        
        Args:
            event_name: (str) The name of the event to dispatch
            payload: (dict) If present, must be a dict of key(str)/value(any) pairs.
        
        Returns:
            The number of observers that were called, excluding those from recursive calls.
        """
    def get_observers(self, event_names: list[str], filter: typing.Any = None) -> list[Observer]:
        """
        Read-only: gets a list of all the registered observer.
        """
    def has_observers(self, event_name: str, filter: typing.Any = None) -> bool:
        """
        Queries the Event Dispatcher whether any observers are listening to a specific event signature.
        
        Emulates a call to :func:`.dispatch_event()` (without actually calling any observers) and returns `True` if any
        observers would be called.
        
        Args:
            event_name: (str) The event name to query
            filter: [optional] (dict) If present, must be a dict of key(str)/value(any) pairs.
        
        Returns:
            `True` if at least one observer would be called with the given `filter` arguments; `False` otherwise.
        """
    def next_event(self, event_name: str, order: int = 0, filter: dict | None = None, observer_name: str | None = None):
        """
        Async wait for next event
        """
    def observe_event(self, order: int = 0, event_name: str, on_event: typing.Callable[[Event], None], filter: typing.Any = None, observer_name: str = '<python>') -> ObserverGuard:
        """
        Registers an observer with the Event Dispatcher system.
        
        An observer is a callback that is called whenever :func:`.dispatch_event` is called. The observers are invoked in the
        thread that calls `dispatch_event()`, and multiple threads may be calling `dispatch_event()` simultaneously, so
        observers must be thread-safe unless the application can ensure synchronization around `dispatch_event()` calls.
        
        Observers can pass an optional dictionary of `filter` arguments. The key/value pairs of `filter` arguments cause an
        observer to only be invoked for a `dispatch_event()` call that contains at least the same values. For instance, having a
        filter dictionary of `{"WindowID": 1234}` will only cause the observer to be called if `dispatch_event()` is given the
        same value as a `"WindowID"` parameter.
        
        Observers can be added inside of an observer notification (i.e. during a call to `dispatch_event()`), however these new
        observers will not be called for currently the dispatching event. A subsequent recursive call to `dispatch_event()` (on
        the current thread only) will also call the new observer. The new observer will be available to all other threads once
        the `dispatch_event()` call (in which it was added) completes.
        
        Args:
            order: (int) A value determining call order. Observers with lower order values are called earlier. Observers with
                the same order value and same filter argument values will be called in the order they are registered. Observers
                with the same order value with different filter arguments are called in an indeterminate order.
            event_name: (str) The event name to observe
            on_event: (function) A function that is invoked when an event matching `event_name` and any `filter` arguments is
                dispatched.
            filter: [optional] (dict) If present, must be a dict of key(str)/value(any) pairs.
            observer_name: [optional] (str) If present, the name of the observer for debugging and profiling. If omitted,
                "<python>" is used instead.
        
        Returns:
            An ObserverGuard object that, when collected, removes the observer from the Event Dispatcher system.
        """
    def remove_all_event_aliases_for(self, target_name: str) -> int:
        """
        Removes **all** aliases for a given event target.
        
        Aliases are added with `add_event_alias()`.
        
        Once an alias is removed from a target, any former alias event can be added as an alias for a different target,
        or used as a target itself. Similarly, once `target_name` has all aliases removed, it can be used as an alias or as a
        target in the future.
        
        While it is possible to add or remove an alias from an observer callback, it will not affect the current event
        dispatch.
        
        Args:
            target_name: (str) The target event to remove all aliases from.
        
        Returns:
            The number of aliases removed. A value of 0 indicates that `target_name` is not actually an event target or
            currently has no aliases.
        """
    def remove_all_observers_for(self, event_name: str) -> int:
        """
        Removes all observers for the given event.
        
        Typically a system might do this when it will never send a particular event again, such at shutdown. After
        calling this, `has_observers()` for `event_name` will return `false`. Observers with filter arguments for
        `event_name` will also be removed. Observers are removed in the reverse of the registration order.
        
        Any existing `ObserverGuard` objects may be destroyed but will not have an effect.
        
        **WARNING:** This will forcibly remove all observers, which will receive no notification that they have been removed.
        
        Args:
            event_name: (str) The event to remove all observers for.
        
        Returns:
            The number of observers that were removed.
        """
    def remove_event_alias(self, target_name: str, alias_name: str) -> bool:
        """
        Removes a previously-added alias.
        
        Aliases are added with `add_event_alias()`.
        
        Once `alias_name` is removed as an alias, the `alias_name` event can be added as an alias for a different target, or
        used as a target itself. Similarly, once `target_name` has all aliases removed, it can be used as an alias or as a
        target in the future.
        
        While it is possible to add or remove an alias from an observer callback, it will not affect the current event
        dispatch.
        
        Args:
            target_name: (str) The target event to remove an alias from.
            alias_name: (str) The alias to remove from @p target.
        
        Returns:
            `True` if an existing alias was found and removed, or `False` for one of the following reasons: `target_name` and 
            `alias_name` are the same, `target_name` is not an event target, or `alias_name` is not an event alias, or
            `target_name` does not have an alias `alias_name`.
        """
class IMessageQueue:
    """
    
    An instance of a message queue.
    
    A message queue is a one-way weak coupling device that allows "messages" to be sent from a variety of senders and
    received by a specific target. A message queue has a push-side and a pop-side. The push-side can be accessed by any
    thread. The pop-side can only be accessed by the owning thread, or a group of threads if no owning thread is
    specified. Violations of this policy are enforced by raising errors.
    
    Can be created with IMessageQueueFactory.create_message_queue(), or an existing message queue can be found with
    IMessageQueueFactory.get_message_queue().
    """
    def _add_message_callback(self, arg0: typing.Callable[[bool], None]) -> None:
        ...
    def _push(self, event_name: str, payload: typing.Any = None, callback: typing.Any = None) -> None:
        ...
    def get_name(self) -> str:
        """
        Retrieves the unique name of this message queue.
        
        Args:
            None
        
        Returns:
            str: The unique name of this message queue.
        """
    def get_owning_thread(self) -> int:
        """
        Retrieves the thread ID of the thread which owns this message queue.
        
        This value should be comparable with threading.get_ident().
        
        Args:
            None
        
        Returns:
            uint: The thread identifier that owns the queue, or 0 if no single thread owns the queue.
        """
    def has_messages(self) -> bool:
        """
        Returns whether this message queue has pending messages.
        
        Args:
            None
        
        Returns:
            bool: True if there are messages in the queue; False if there are no messages in the queue.
        """
    def peek(self, fn: typing.Callable[[Event], None]) -> bool:
        """
        Inspects the message at the front of the queue, if any, without removing it.
        
        The message is not removed when this function is called. Call pop() to process and remove the message.
        
        This function only works in a single-owner-thread situation, otherwise a RuntimeError is raised.
        
        Args:
            fn: (function) A function that is called with a carb.eventdispatcher.Event as the only parameter.
        
        Returns:
            bool: True if the given function was called with a message; False if there are no messages in the queue.
        
        Raises:
            IndexError: The message queue has been stopped.
            RuntimeError: The calling thread is not the owner thread, the queue is not in single-thread mode, or another error.
        """
    def pop(self, fn):
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
    def push(self, event_name, payload: dict = None):
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
    def push_and_wait(self, event_name, payload: dict = None):
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
    def stop(self) -> None:
        """
        Stops the message queue before destruction.
        This is a one-time, irreversible command to a message queue that the queue is no longer processing messages. It
        is not required to call this function before the last reference is removed and `*this` is destroyed.
        
        When stop() returns it is guaranteed that:
        
        * Any future attempts to push messages or pop messages will result in an IndexError being raised.
        * All threads or tasks that are awaiting a message or waiting for a message to be processed have been unblocked.
          The existing function calls and future function calls will raise an IndexError.
        * The message queue is removed from IMessageQueueFactory; attempts to retrieve the message queue by name
          will return None and a new message queue with the same name can be created again.
        
        Subsequent calls to this function will raise IndexError as the message queue has already been stopped.
        
        It is undefined behavior to call this from within the functions passed to pop() or peek(). Instead, it is recommended
        that the handlers for pop() or peek() set a flag that can be checked after the pop() or peek() returns which then calls 
        stop().
        
        Args:
            None
        
        Returns:
            None
        
        Raises:
            IndexError: The message queue has already been stopped.
            RuntimeError: The calling thread does not have permission to stop the queue, or another error.
        """
    def try_pop(self, fn: typing.Callable[[Event], None]) -> bool:
        """
        Pops the message at the front of the queue and calls a function with the message.
        
        The message is removed from the queue atomically before processing. In a single-owner-thread situation, this
        function must be called within the context of the owning thread.
        
        If a task or thread is waiting on the message, the message will be considered 'completed' and unblock the waiting
        task/thread as soon as fn() returns, even if the carb.eventdispatcher.Event passed to the function is retained.
        
        Args:
            fn: (function) A function that is called with a carb.eventdispatcher.Event as the only parameter.
        
        Returns:
            bool: True if the given function was called with a message; False if there are no messages in the queue.
        
        Raises:
            IndexError: The message queue has been stopped.
            RuntimeError: The calling thread is not the owner thread, or another error.
        """
class IMessageQueueFactory:
    """
    """
    def add_alias(self, target: str, alias: str) -> bool:
        """
        Adds an alias that can be used to refer to a different message queue.
        
        After a successful call, `get_message_queue()` called with `alias` will return the IMessageQueue instance
        created with name `target`. A message queue may have multiple aliases. The target message queue does not have to
        be created yet.
        
        Args:
            target: (str) The target message queue name.
            alias: (str) The alias name.
        
        Returns:
            `True` if the alias was created; `False` if `target` and `alias` are the same, either `target` or `alias` are empty,
            `target` is already an alias, or `alias` is already used.
        """
    def create_message_queue(self, name: str, **kwargs) -> tuple[IMessageQueue, bool]:
        """
        Creates a message queue with the given name and parameters, or returns an existing message queue with the given name.
        
        Args:
            name: (str) The unique name of the message queue. If the name already exists, the message queue will not be
                    created but the previously-created message queue will be returned (params will be ignored). Since names must
                    be unique, a scheme such as reverse-DNS is recommended.
        
        Keyword Args:
            owning_thread: (int, default: 0) The thread that owns the message queue. If zero, the message queue can be popped
                    by multiple threads. If a specific thread owns the message queue then an error will occur if any other
                    thread attempts to pop the message queue, and the message queue will be optimized for the owning thread.
                    Message queues that are created from a task (carb::tasking::ITasking) or thread pool should use zero
                    here instead of using the calling thread. NOTE: This value should be via threading.get_native_id(), NOT
                    threading.get_ident().
        
        Returns:
            Tuple of (IMessageQueue, bool) where the IMessageQueue is the message queue and the bool is whether it was created
            by this call (True), or an existing message queue was found and returned (False).
        
        Raises:
            MemoryError: failed to allocate the message queue
            RuntimeError: an invalid argument was passed
        """
    def get_message_queue(self, name: str) -> IMessageQueue:
        """
        Retrieves a message queue with the given name.
        
        Args:
            name: (str) The unique name of a previously-created message queue.
        
        Returns:
            A message queue found by name.
        """
    def remove_alias(self, target: str, alias: str) -> bool:
        """
        Removes a previously-added message queue alias.
        
        Removes an alias that was previously added with @ref addAlias. Once removed, the @p alias is free to be used
        again as an alias for a different message queue or to create a new message queue.
        
        Args:
            target: (str) The target message queue name.
            alias: (str) The alias name previously added with `add_alias()`.
        
        Returns:
            `True` if the alias was removed successfully; `False` if `target` and `alias` are the same, either `target` or
            `alias` are empty, `target` is not an alias target, or `alias` is not an alias of `target`.
        """
class Observer:
    """
    Observer.
    
    A registered observer.
    """
    @property
    def enabled(self) -> bool:
        """
        Sets or gets the enabled state of an observer.
        """
    @enabled.setter
    def enabled(self, arg1: bool) -> None:
        ...
    @property
    def name(self) -> str:
        """
        Read-only: gets the name of the observer.
        """
    @property
    def order(self) -> int:
        """
        Sets or gets the integer order of the observer.
        """
    @order.setter
    def order(self, arg1: int) -> None:
        ...
class ObserverGuard:
    """
    ObserverGuard.
    
    Lifetime control for a registered observer. Unregister the observer by calling the reset() function or allowing the
    object to be collected.
    """
    def reset(self) -> None:
        """
        Explicitly stops an observer.
        
        Having this object collected has the same effect, implicitly.
        
        This is safe to perform while dispatching.
        
        Since observers can be in use by this thread or any thread, this function is carefully synchronized with all other
        Event Dispatcher operations.
        
        - During `reset()`, further calls to the observer are prevented, even if other threads are currently dispatching an
          event that would be observed by the observer in question.
        - If any other thread is currently calling the observer in question, `reset()` will wait until all other threads have
          left the observer callback function.
        - If the observer function is *not* in the backtrace of the current thread, the observer function is immediately
          released.
        - If the observer function is in the backtrace of the current thread, `reset()` will return without waiting and without
          releasing the observer callback. Instead, releasing the function will be performed when the `dispatch_event()` call
          in the current thread finishes.
        
        When `reset()` returns, it is guaranteed that the observer callback function will no longer be called and all calls to
        it have completed (except if the calling thread is dispatching).
        """
    @property
    def enabled(self) -> bool:
        """
        Sets or gets the enabled state of an observer.
        """
    @enabled.setter
    def enabled(self, arg1: bool) -> None:
        ...
    @property
    def name(self) -> str:
        """
        Read-only: gets the name of the observer.
        """
    @property
    def order(self) -> int:
        """
        Sets or gets the integer order of the observer.
        """
    @order.setter
    def order(self, arg1: int) -> None:
        ...
def acquire_eventdispatcher_interface() -> ...:
    """
    Acquires the Event Dispatcher interface.
    """
def acquire_messagequeue_factory_interface() -> ...:
    """
    Acquires the IMessageQueueFactory interface.
    """
_cleanup: typing.Any  # value = <capsule object>
