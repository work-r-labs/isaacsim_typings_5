from __future__ import annotations
import carb as carb
import functools as functools
import logging as logging
import omni as omni
import os as os
import re as re
import time as time
import uuid as uuid
__all__ = ['CARB_LOG_LEVEL_TO_EVENT_LEVEL', 'DSN', 'carb', 'filter_path_from_string', 'functools', 'logger', 'logging', 'omni', 'os', 're', 'remove_sentry_pii_data', 'should_enable_sentry', 'start_sentry', 'time', 'uuid']
class _Extension(omni.ext._extensions.IExt):
    def _configure_logger(self):
        """
        Subscribe to IApp log listener which outputs carbonite log errors each frame on the main thread
        
                We could have created custom python logger here, but it is known to create deadlocks with GIL because of being
                called from many threads.
                
        """
    def on_startup(self):
        ...
def _get_machine_id():
    """
    Return an identifier that is unique to the machine this is being run on, without any PII
    """
def _get_sentry_logging_integration():
    ...
def _get_sentry_sdk():
    ...
def filter_path_from_string(input_str: str, app_root_path: str | None = None) -> str:
    """
    If there's a path on the string we get rid of everything up to the root path.
    """
def remove_sentry_pii_data(event, hint, app_root_path: str | None = None) -> dict:
    """
    Tries our best to remove PII data from sentry events.
    
        We replace userId by the sessionId (unique integer per whole session) and replace any paths we find in the
            message or stack trace with their last part of the path, e.g: /home/foo/bar.py becomes bar.py
    
        Args:
            event (dict): The event that we filter
            hint (dict): Not used but part of the API
            app_root_path (str or None): the root path of the app. Everything before this is considered PII
    
        Returns:
            dict: The filtered event.
        
    """
def should_enable_sentry(app, settings) -> bool:
    """
    Verifies if we're an external build or disabled via settings.
    
        Args:
            app (omni.App): The application
            settings (carb.settings): Carb dictionary
        
    """
def start_sentry(app, settings) -> bool:
    """
    Starts sentry if it should.
    
        Returns:
            bool: Returns True if sentry started
        
    """
CARB_LOG_LEVEL_TO_EVENT_LEVEL: dict = {-2: 'debug', -1: 'info', 0: 'warning', 1: 'error', 2: 'fatal'}
DSN = None
logger: logging.Logger  # value = <Logger omni.kit.telemetry.impl.sentry_extension (DEBUG)>
