"""
MainWindow extension
"""
from __future__ import annotations
import omni as omni
from omni.kit.mainwindow.scripts.main_window import MainWindow
__all__ = ['MainWindow', 'MainWindowExtension', 'g_main_window', 'get_main_window', 'omni']
class MainWindowExtension(omni.ext._extensions.IExt):
    """
    An omni.ext.IExt extension to manage the main window of an application.
    
        This extension provides lifecycle management for the `MainWindow` instance, creating it upon startup and destroying it on shutdown. It ensures that there is a global access point to the main window through the `get_main_window` function.
        
    """
    def on_shutdown(self):
        """
        Cleans up resources related to the main window when the extension shuts down.
        
                This method destroys the MainWindow instance if it exists and sets the
                global variable to None, ensuring that all resources are properly
                released.
                
        """
    def on_startup(self, ext_id):
        """
        Initializes the main window when the extension starts up.
        
                This method creates a new instance of the MainWindow class and assigns it
                to a global variable so that it can be accessed from anywhere within
                the application.
        
                Args:
                    ext_id (str): The ID of the current extension.
                
        """
def get_main_window() -> omni.kit.mainwindow.scripts.main_window.MainWindow:
    """
    Returns the global instance of the MainWindow.
    
        This function allows access to the MainWindow instance that is created
        and managed by the MainWindowExtension. It uses a global variable to
        store the instance so it can be retrieved from anywhere within the
        application.
    
        Returns:
            MainWindow: The global MainWindow instance if it has been created,
            otherwise None.
        
    """
g_main_window: omni.kit.mainwindow.scripts.main_window.MainWindow  # value = <omni.kit.mainwindow.scripts.main_window.MainWindow object>
