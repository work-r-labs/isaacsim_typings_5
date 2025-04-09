from __future__ import annotations
import carb as carb
import omni as omni
__all__ = ['Extension', 'carb', 'omni']
class Extension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    def on_stop_play(self, event: carb.events._events.IEvent):
        ...
