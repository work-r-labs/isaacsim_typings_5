"""
This module provides classes and functionality for connecting to, authenticating with, and managing connections to Nucleus servers within the Omniverse environment.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni.kit.widget.nucleus_connector.ui import AlertPane
from omni.kit.widget.nucleus_connector.ui import ConnectorDialog
__all__ = ['AlertPane', 'ConnectorDialog', 'NucleusConnector', 'asyncio', 'carb', 'omni', 'partial']
class NucleusConnector:
    """
    NucleusConnector object helps with connecting to Nucleus servers.
    
        This class facilitates the establishment, management, and authentication of connections to Nucleus servers. It provides methods to start and end authentication flows, connect to servers with optional callbacks, and handle server reconnections. Additionally, it manages server connection status updates.
        
    """
    def __init__(self):
        ...
    def _reset_omni_client_retries(self):
        ...
    def _server_status_changed(self, url: str, status: omni.client.impl._omniclient.ConnectionStatus) -> None:
        ...
    def cancel_auth(self, auth_handle: int, dialog: omni.kit.widget.nucleus_connector.ui.ConnectorDialog):
        """
        
                This callback is attached to the dialog's cancel button. It cancels the authentication process.
        
                Args:
                    auth_handle (int): An integer handle that should be passed to cancel authentication
        
                
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
    def start_auth_flow(self, host_name, auth_handle: int):
        """
        
                Called at the start of the authentication cycle. Most importantly, prepares a cancel button
                so that the user can cancel out of the process if it hangs for any reason.
        
                Args:
                    host_name (str): The server host name that the authentication is for
                    auth_handle (int): An integer handle that should be passed to cancel authentication
        
                
        """
