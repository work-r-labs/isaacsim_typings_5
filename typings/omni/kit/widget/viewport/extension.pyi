from __future__ import annotations
import omni as omni
__all__: list = ['ViewportWidgetExtension']
class ViewportWidgetExtension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
