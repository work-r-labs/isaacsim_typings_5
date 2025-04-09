from __future__ import annotations
__all__: list = ['EventSubscription', 'Event']
class Event(list):
    """
    
        A list of callable objects. Calling an instance of this will cause a
        call to each item in the list in ascending order by index.
        
    """
    def __call__(self, *args, **kwargs):
        """
        Called when the instance is “called” as a function
        """
    def __repr__(self):
        """
        
                Called by the repr() built-in function to compute the “official”
                string representation of an object.
                
        """
class EventSubscription:
    """
    
        Event subscription.
    
        Event has callback while this object exists.
        
    """
    def __del__(self):
        """
        Called by GC.
        """
    def __init__(self, event, fn):
        """
        
                Save the function, the event, and add the function to the event.
                
        """
    def destroy(self):
        ...
