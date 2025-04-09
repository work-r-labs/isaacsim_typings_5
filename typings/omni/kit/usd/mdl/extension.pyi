from __future__ import annotations
import carb as carb
import omni as omni
import os as os
__all__ = ['ENABLE_OMNI_USD_MDL_DISCOVER_ON_STARTUP', 'Ext', 'carb', 'omni', 'os']
class Ext(omni.ext._extensions.IExt):
    def _setup_usd_env_settings(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
ENABLE_OMNI_USD_MDL_DISCOVER_ON_STARTUP: str = '/usd/enableOmniUsdMdlDiscoverOnStartup'
