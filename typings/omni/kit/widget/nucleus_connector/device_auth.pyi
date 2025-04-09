"""
This module provides functionality for device authentication flow with Nucleus servers, including QR code display, user cancellation handling, and maintaining connection status.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni.kit.widget.nucleus_connector.ui import AlertPane
from omni.kit.widget.nucleus_connector.ui import ConnectorDialog
from omni.kit.widget.nucleus_connector.ui import DeviceAuthFlowDialog
__all__ = ['AlertPane', 'ConnectorDialog', 'DeviceAuthConnector', 'DeviceAuthFlowDialog', 'asyncio', 'carb', 'omni', 'partial']
class DeviceAuthConnector:
    """
    DeviceAuthConnector facilitates the connection to Nucleus servers using the device authentication flow.
    
        It manages the authentication process by displaying QR codes, handling user cancellations, and maintaining the connection status.
        
    """
    def __init__(self):
        ...
    def _connection_status_changed(self, server: str, status: omni.client.impl._omniclient.ConnectionStatus) -> None:
        """
        Collect signed in server's service information based upon server status changed.
        """
    def cancel_auth(self, auth_handle: int, server: str, dialog: omni.kit.widget.nucleus_connector.ui.DeviceAuthFlowDialog):
        """
        
                This callback is attached to the dialog's cancel button. It cancels the authentication process.
        
                Args:
                    auth_handle (int): An integer handle that should be passed to cancel authentication
                    server (str): The server url that the auth handle is binding to
        
                
        """
    def connect_server_async(self, name: str, url: str, on_success_fn: typing.Callable = None, on_failed_fn: typing.Callable = None, retry: bool = False, dialog: omni.kit.widget.nucleus_connector.ui.ConnectorDialog = None):
        """
        
                Connects to the named server.
        
                Args:
                    name (str): Name of server
                    url (str): Url of server
                    on_success_fn (Callable): Invoked when successful, on_success_fn(name: str, url: str)
                    on_faild_fn (Callable): Invoked when failed, on_faild_fn(name: str, url: str)
                    retry (bool): True if re-trying for second time.
                    dialog (ConnectorDialog): A dialog instance to re-use from parent operation.
        
                
        """
    def connect_with_callback(self, name: str = None, url: str = None, on_success_fn: typing.Callable = None, on_failed_fn: typing.Callable = None):
        """
        
                Unless specified, prompts for server name and Url and proceeds to connect to it.
        
                Args:
                    name (str): Name of server
                    url (str): Url of server
                    on_success_fn (Callable): Invoked when successful, on_success_fn(name: str, url: str)
                    on_faild_fn (Callable): Invoked when failed, on_faild_fn(name: str, url: str)
        
                
        """
    def destroy(self):
        """
        Destructor.
        """
    def end_auth_flow(self, auth_handle: int):
        """
        Called at the end of the authentication cycle; hides the app dialog
        """
    def reconnect_server_async(self, url: str, on_success_fn: typing.Callable = None, on_failed_fn: typing.Callable = None):
        """
        
                Re-connects to the named server.
        
                Args:
                    url (str): Url of server
                    on_success_fn (Callable): Invoked when successful, on_success_fn(name: str, url: str)
                    on_faild_fn (Callable): Invoked when failed, on_faild_fn(name: str, url: str)
        
                
        """
    def start_auth_flow(self, auth_handle: int, params: omni.client.impl._omniclient.AuthDeviceFlowParams):
        """
        
                Called at the start of the authentication cycle. Shows the user a qrcode of auth url and code that needs to be
                entered in the auth page. User can cancel the process by clicking the cancel button.
        
                Args:
                    auth_handle (int): An integer handle that should be passed to cancel authentication
        
                
        """
