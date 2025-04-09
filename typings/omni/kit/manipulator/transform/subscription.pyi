from __future__ import annotations
__all__ = ['Subscription']
class Subscription:
    """
    A class representing a subscription to an event or notification.
    
        This class provides a method to unsubscribe and clean up resources when notifications or updates are no longer needed.
    
        Args:
            unsubscribe_fn (Callable): A callable to unsubscribe from the event or notification.
    """
    def __del__(self):
        """
        Handles the deletion of the Subscription object by calling unsubscribe to clean up resources.
        """
    def __init__(self, unsubscribe_fn: typing.Callable):
        """
        Initializes a new Subscription object with a callable to unsubscribe.
        
                Args:
                    unsubscribe_fn (Callable): A callable that, when called, will unsubscribe this subscription and prevent any further notifications or updates.
                
        """
    def unsubscribe(self):
        """
        Unsubscribes from the event or notification, preventing any further updates.
                If the subscription is already unsubscribed, this method does nothing.
        """
