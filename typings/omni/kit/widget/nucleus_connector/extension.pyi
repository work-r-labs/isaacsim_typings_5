"""
This module provides an extension for connecting to Nucleus servers, supporting authentication flows and connection management.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni.kit.widget.nucleus_connector.connector import NucleusConnector
from omni.kit.widget.nucleus_connector.device_auth import DeviceAuthConnector
__all__ = ['DeviceAuthConnector', 'NUCLEUS_CONNECTION_SUCCEEDED_EVENT', 'NucleusConnector', 'NucleusConnectorExtension', 'asyncio', 'carb', 'connect', 'connect_with_dialog', 'disconnect', 'g_singleton', 'get_instance', 'omni', 'partial', 'reconnect']
class NucleusConnectorExtension(omni.ext._extensions.IExt):
    """
    Helper extension for connecting to Nucleus servers.
    
        This extension serves as a utility for managing connections to Nucleus servers, handling both authentication flows and connection management tasks. It provides a convenient interface for initiating and terminating server connections, as well as managing authentication processes through both standard and device auth flows.
        
    """
    @staticmethod
    def connect(*args, **kwargs):
        """
        
                Connects to the named server.
        
                Args:
                    name (str): Name of server
                    url (str): Url of server
                    on_success_fn (Callable): Invoked when successful, on_success_fn(name: str, url: str)
                    on_faild_fn (Callable): Invoked when failed, on_faild_fn(name: str, url: str)
        
                
        """
    @staticmethod
    def connect_with_dialog(*args, **kwargs):
        """
        
                Prompts for server name and Url and proceeds to connect to it.
        
                Args:
                    on_success_fn (Callable): Invoked when successful, on_success_fn(name: str, url: str)
                    on_faild_fn (Callable): Invoked when failed, on_faild_fn(name: str, url: str)
        
                
        """
    @staticmethod
    def disconnect(*args, **kwargs):
        """
        
                Disconnects from the server.
        
                Args:
                    url (str): Url of server
        
                
        """
    @staticmethod
    def reconnect(*args, **kwargs):
        """
        
                Reconnects to the named server.
        
                Args:
                    url (str): Url of server
                    on_success_fn (Callable): Invoked when successful, on_success_fn(url: str)
                    on_faild_fn (Callable): Invoked when failed, on_faild_fn(url: str)
        
                
        """
    def __init__(self):
        """
        Initializes the NucleusConnectorExtension class.
        """
    def _on_authenticate(self, show_alert: bool, host_name: str, auth_handle: int):
        """
        
                This callback is invoked when the application should show a dialog box letting the user know that a
                browser window has opened and to complete signing in using the web browser.
        
                Args:
                    show_alert (bool): True means to start the authentication cycle and False means to end it
                    host_name (str): The server host name that the authentication is for
                    auth_handle (int): An integer handle that should be passed to cancel authentication
        
                
        """
    def _on_connect_failed(self, callback: typing.Callable, name: str, url: str):
        """
        Called when connection fails; invokes the given callback
        """
    def _on_connect_succeeded(self, callback: typing.Callable, name: str, url: str):
        """
        Called when connection is made successfully; invokes the given callback
        """
    def _on_device_auth(self, auth_handle: int, params: omni.client.impl._omniclient.AuthDeviceFlowParams):
        """
        
                This callback is invoked when authentication for device auth flow, instead of auth in the web browser.
        
                Args:
                    auth_handle (int): The auth handle that could be used for canceling.
                    params (omni.client.AuthDeviceFlowParams): An object containing info to display to user to complete the auth.
                        if it is None, it means the auth attempt is finished.
                
        """
    def on_shutdown(self):
        """
        Clears the auth callback and destroy on extension shutdown.
        """
    def on_startup(self, ext_id):
        """
        Build connector and register/set auth callback on extension startup.
        
                Args:
                    ext_id (str): The extension identifier.
                
        """
def connect(name: str, url: str, on_success_fn: typing.Callable = None, on_failed_fn: typing.Callable = None):
    """
    Connects to the named server.
    
        Args:
            name (str): Name of server
            url (str): Url of server
            on_success_fn (Callable): Invoked when successful, on_success_fn(name: str, url: str)
            on_failed_fn (Callable): Invoked when failed, on_failed_fn(name: str, url: str)
        
    """
def connect_with_dialog(on_success_fn: typing.Callable = None, on_failed_fn: typing.Callable = None):
    """
    Prompts for server name and Url and proceeds to connect to it.
    
        Args:
            on_success_fn (Callable): Invoked when successful, on_success_fn(name: str, url: str)
            on_failed_fn (Callable): Invoked when failed, on_failed_fn(name: str, url: str)
        
    """
def disconnect(url: str):
    """
    Disconnects from the server.
    
        Args:
            url (str): Url of server
        
    """
def get_instance():
    """
    Returns the singleton instance of NucleusConnectorExtension.
    
        Returns:
            The singleton instance of NucleusConnectorExtension if it exists, otherwise None.
    """
def reconnect(url: str, on_success_fn: typing.Callable = None, on_failed_fn: typing.Callable = None):
    """
    Reconnects to the named server.
    
        Args:
            url (str): Url of server
            on_success_fn (Callable): Invoked when successful, on_success_fn(url: str)
            on_failed_fn (Callable): Invoked when failed, on_failed_fn(url: str)
        
    """
NUCLEUS_CONNECTION_SUCCEEDED_EVENT: int = 12539978195413966289
g_singleton: NucleusConnectorExtension  # value = <omni.kit.widget.nucleus_connector.extension.NucleusConnectorExtension object>
