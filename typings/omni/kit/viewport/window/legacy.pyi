from __future__ import annotations
import carb as carb
from functools import partial
__all__: list = list()
def _resolve_viewport_setting(viewport_id: str, setting_name: str, isettings: carb.settings._settings.ISettings, legacy_key: typing.Optional[str] = None, set_per_vp_value: bool = False, default_if_not_found: typing.Any = None, usd_context_name: typing.Optional[str] = None):
    ...
def _setup_viewport_options(viewport_id: str, usd_context_name: str, isettings: carb.settings._settings.ISettings):
    ...
