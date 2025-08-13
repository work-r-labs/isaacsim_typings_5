from __future__ import annotations
import carb.dictionary._dictionary
import typing
__all__: list[str] = ['AdapterType', 'IEvent', 'IEventStream', 'IEvents', 'IEventsAdapter', 'ISubscription', 'MappingEntry', 'acquire_events_adapter_interface', 'acquire_events_interface', 'register_event_alias', 'type_from_string', 'unregister_event_alias']
class AdapterType:
    """
    Members:
    
      DISPATCH
    
      PUSH_PUMP
    
      FULL
    
      FULL_ALIAS
    """
    DISPATCH: typing.ClassVar[AdapterType]  # value = <AdapterType.DISPATCH: 0>
    FULL: typing.ClassVar[AdapterType]  # value = <AdapterType.FULL: 2>
    FULL_ALIAS: typing.ClassVar[AdapterType]  # value = <AdapterType.FULL_ALIAS: 3>
    PUSH_PUMP: typing.ClassVar[AdapterType]  # value = <AdapterType.PUSH_PUMP: 1>
    __members__: typing.ClassVar[dict[str, AdapterType]]  # value = {'DISPATCH': <AdapterType.DISPATCH: 0>, 'PUSH_PUMP': <AdapterType.PUSH_PUMP: 1>, 'FULL': <AdapterType.FULL: 2>, 'FULL_ALIAS': <AdapterType.FULL_ALIAS: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class IEvent:
    """
    
            Event.
    
            Event has an Event type, a sender id and a payload. Payload is a dictionary like item with arbitrary data.
            
    """
    def consume(self) -> None:
        """
        Consume event to stop it propagating to other listeners down the line.
        """
    @property
    def payload(self) -> carb.dictionary._dictionary.Item:
        ...
    @property
    def sender(self) -> int:
        ...
    @property
    def type(self) -> int:
        ...
class IEventStream:
    def create_subscription_to_pop(self, fn: typing.Callable[[IEvent], None], order: int = 0, name: str = None) -> ISubscription:
        """
                    Subscribes to event dispatching on the stream.
        
                    See :class:`.Subscription` for more information on subscribing mechanism.
        
                    Args:
                        fn: The callback to be called on event dispatch.
                        order: An integer order specifier. Lower numbers are called first. Negative numbers are allowed. Default is 0.
                        name: The name of the subscription for profiling. If no name is provided one is generated from the traceback of the calling function.
        
                    Returns:
                        The subscription holder.
        """
    def create_subscription_to_pop_by_type(self, event_type: int, fn: typing.Callable[[IEvent], None], order: int = 0, name: str = None) -> ISubscription:
        """
                    Subscribes to event dispatching on the stream.
        
                    See :class:`.Subscription` for more information on subscribing mechanism.
        
                    Args:
                        event_type: Event type to listen to.
                        fn: The callback to be called on event dispatch.
                        order: An integer order specifier. Lower numbers are called first. Negative numbers are allowed. Default is 0.
                        name: The name of the subscription for profiling. If no name is provided one is generated from the traceback of the calling function.
        
                    Returns:
                        The subscription holder.
        """
    def create_subscription_to_push(self, fn: typing.Callable[[IEvent], None], order: int = 0, name: str = None) -> ISubscription:
        """
                    Subscribes to pushing events into stream.
        
                    See :class:`.Subscription` for more information on subscribing mechanism.
        
                    Args:
                        fn: The callback to be called on event push.
                        order: An integer order specifier. Lower numbers are called first. Negative numbers are allowed. Default is 0.
                        name: The name of the subscription for profiling. If no name is provided one is generated from the traceback of the calling function.
        
                    Returns:
                        The subscription holder.
        """
    def create_subscription_to_push_by_type(self, event_type: int, fn: typing.Callable[[IEvent], None], order: int = 0, name: str = None) -> ISubscription:
        """
                    Subscribes to pushing events into stream.
        
                    See :class:`.Subscription` for more information on subscribing mechanism.
        
                    Args:
                        event_type: Event type to listen to.
                        fn: The callback to be called on event push.
                        order: An integer order specifier. Lower numbers are called first. Negative numbers are allowed. Default is 0.
                        name: The name of the subscription for profiling. If no name is provided one is generated from the traceback of the calling function.
        
                    Returns:
                        The subscription holder.
        """
    def dispatch(self, event_type: int = 0, sender: int = 0, payload: dict = {}) -> None:
        """
                    Dispatch :class:`.Event` immediately without putting it into stream.
        
                    Args:
                        event_type (int): :class:`.Event` type.
                        sender (int): Sender id. Unique can be acquired using :func:`.acquire_unique_sender_id`.
                        dict (typing.Dict): :class:`.Event` payload.
        """
    def get_subscription_to_pop_order(self, name: str) -> typing.Any:
        ...
    def get_subscription_to_push_order(self, name: str) -> typing.Any:
        ...
    def get_subscriptions_to_pop(self) -> tuple:
        """
                    Get subscriptions to pop. Return tuple with all subscriptions.
        """
    def get_subscriptions_to_push(self) -> tuple:
        """
                    Get subscriptions to push. Return tuple with all subscriptions.
        """
    def next_event(self, order: int = 0, name: str = ''):
        """
        Async wait for next event.
        """
    def next_event_by_type(self, event_type: int, order: int = 0, name: str = ''):
        """
        Async wait for next event of particular type.
        """
    def pop(self) -> IEvent:
        """
                    Pop event.
        
                    This function blocks execution until there is an event to pop.
        
                    Returns:
                        (:class:`.Event`) object. You own this object, it can be stored.
        """
    def pump(self) -> None:
        """
                    Pump event stream.
        
                    Dispatches all events in a stream.
        """
    def push(self, event_type: int = 0, sender: int = 0, payload: dict = {}) -> None:
        """
                    Push :class:`.Event` into stream.
        
                    Args:
                        event_type (int): :class:`.Event` type.
                        sender (int): Sender id. Unique can be acquired using :func:`.acquire_unique_sender_id`.
                        dict (typing.Dict): :class:`.Event` payload.
        """
    def set_subscription_to_pop_order(self, name: str, order: int) -> bool:
        """
                    Set subscription to pop order by name of subscription.
        """
    def set_subscription_to_push_order(self, name: str, order: int) -> bool:
        """
                    Set subscription to push order by name of subscription.
        """
    def try_pop(self) -> IEvent:
        """
                    Try pop event.
        
                    Returns:
                        Pops (:class:`.Event`) if stream is not empty or return `None`.
        """
    @property
    def event_count(self) -> int:
        ...
    @property
    def name(self) -> str:
        """
                        Gets the name of the :class:`.EventStream`.
        
                        Returns:
                            The name of the event stream.
        """
class IEvents:
    def acquire_unique_sender_id(self) -> int:
        """
                    Acquire unique sender id.
        
                    Call :func:`.release_unique_sender_id` when it is not needed anymore. It can be reused then.
        """
    def create_event_stream(self, name: str = None) -> IEventStream:
        """
                    Create new `.EventStream`.
        
                    Args:
                        name: The name of the .EventStream for profiling. If no name is provided one is generated from the traceback of the calling function.
        """
    def release_unique_sender_id(self, arg0: int) -> None:
        ...
class IEventsAdapter:
    def create_adapter(self, type: AdapterType, name: str, mappings: typing.Sequence, **kwargs) -> IEventStream:
        ...
class ISubscription:
    """
    
            Subscription holder.
            
    """
    def unsubscribe(self) -> None:
        """
                    Unsubscribes this subscription.
        """
    @property
    def enabled(self) -> bool:
        """
                    Enable status of this subscription.
        """
    @enabled.setter
    def enabled(self, arg1: bool) -> None:
        ...
    @property
    def name(self) -> str:
        """
                    Returns the name of this subscription.
        
                    Returns:
                        The name of this subscription.
        """
    @property
    def order(self) -> int:
        """
                    Order of this subscription.
        """
    @order.setter
    def order(self, arg1: int) -> None:
        ...
class MappingEntry:
    dispatch_name: str
    push_name: str
    type: int
    def __init__(self, type: int, dispatch_name: str, push_name: str = '') -> None:
        ...
def acquire_events_adapter_interface() -> ...:
    ...
def acquire_events_interface() -> ...:
    ...
def register_event_alias(event_type: int, push_event: str, pop_event: str) -> bool:
    """
    Registers an alias between `event_type` and event names.
    
    This is generally recommended for use with AdapterType.FULL_ALIAS. This allows event adapters created of type
    AdapterType.FULL_ALIAS to map `event_type` with the corresponding `IEventDispatcher` event names for pushing
    (`push_event`) and popping (`pop_event`).
    
    Corresponding with `IEventsAdapter` created from AdapterType.FULL_ALIAS, the following event names will be aliased:
    * f"AdapterAlias:{event_type}:immediate" becomes an alias to `push_event`.
    * f"AdapterAlias:{event_type}" becomes an alias to `pop_event`.
    
    When the aliases are no longer needed, unregister_event_alias() can be used to remove them.
    
    Args:
        event_type: (int) The EventType to use with aliasing. May not be 0.
        push_event: (str) The IEventDispatcher event name to use for push (immediate) events.
        pop_event: (str) The IEventDispatcher event name to use for pop (deferred) events.
    
    Returns:
        True if the aliases were created; False if either alias could not be created or event_type was 0.
    """
def type_from_string(arg0: str) -> int:
    ...
def unregister_event_alias(event_type: int, push_event: str, pop_event: str) -> bool:
    """
    Unregisters an alias between an IEvents `event_type` and IEventDispatcher event names.
    
    This is the opposite behavior from register_event_alias() when called with the same arguments.
    
    Args:
        event_type: (int) The EventType previously used with aliasing. May not be 0.
        push_event: (str) The IEventDispatcher event name used for push (immediate) events.
        pop_event: (str) The IEventDispatcher event name used for pop (deferred) events.
    
    Returns:
        True if the aliases were removed; False if either alias could not be removed or event_type was 0.
    """
