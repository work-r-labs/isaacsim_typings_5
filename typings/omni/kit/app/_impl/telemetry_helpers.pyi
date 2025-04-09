from __future__ import annotations
from functools import lru_cache
from omni.kit.app._impl.app_iface import get_app
__all__ = ['get_app', 'lru_cache', 'send_telemetry_event']
def _initialize_telemetry(*args, **kwargs):
    ...
def send_telemetry_event(event_type: str, duration: float = 0, data1: str = '', data2: str = '', value1: float = 0.0, value2: float = 0.0):
    """
    
        Send generic telemetry event.
    
        It is a helper, so that just one liner: `omni.kit.app.send_telemetry_event` can be used anywhere instead of checking
        for telemetry being enabled at each call site.
    
        If telemetry is not enabled this function does nothing.
    
        Args:
            event_type (str): A string describing the event that occurred.  There is no restriction on the content or
                formatting of this value. This should neither be `nullptr` nor an empty string.
            duration (float): A generic duration value that can be optionally included with the event.
            data1 (str): A string data value to be sent with the event. The interpretation of this string depends on event_type.
            data2 (str): A string data value to be sent with the event. The interpretation of this string depends on event_type.
            value1 (float): A float data value to be sent with the event. The interpretation of this string depends on event_type.
            value2 (float): A float data value to be sent with the event. The interpretation of this string depends on event_type.
        
    """
_telemetry_hook = None
_telemetry_module = None
