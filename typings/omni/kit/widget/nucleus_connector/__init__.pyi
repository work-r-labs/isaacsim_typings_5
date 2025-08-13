"""
This module provides the NucleusConnectorExtension for connecting to Nucleus servers and managing authentication flows.
"""
from __future__ import annotations
import carb as carb
from omni.kit.app._app import register_event_alias
from omni.kit.widget.nucleus_connector.extension import NucleusConnectorExtension
from omni.kit.widget.nucleus_connector.extension import connect
from omni.kit.widget.nucleus_connector.extension import connect_with_dialog
from omni.kit.widget.nucleus_connector.extension import disconnect
from omni.kit.widget.nucleus_connector.extension import reconnect
from . import connector
from . import device_auth
from . import extension
from . import style
from . import ui
__all__: list = ['NUCLEUS_CONNECTION_SUCCEEDED_EVENT', 'NUCLEUS_CONNECTION_SUCCEEDED_GLOBAL_EVENT', 'connect', 'connect_with_dialog', 'reconnect', 'disconnect']
NUCLEUS_CONNECTION_SUCCEEDED_EVENT: int = 12539978195413966289
NUCLEUS_CONNECTION_SUCCEEDED_GLOBAL_EVENT: str = 'omni.kit.widget.nucleus_connector.CONNECTION_SUCCEEDED'
