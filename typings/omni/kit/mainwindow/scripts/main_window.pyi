"""
MainWindow class
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni import ui
__all__ = ['MainWindow', 'asyncio', 'carb', 'omni', 'ui']
class MainWindow:
    """
    A class that represents the main application window in OmniKit.
    
        This class manages the initialization, display, and cleanup of the main window. It provides methods to toggle the
        visibility of the main menu and status bar, as well as to asynchronously dock various application windows at startup.
        The main window is set up with custom settings that are retrieved from the application's settings.
        
    """
    def __init__(self):
        """
        Initializes the main window with customized settings and potentially starts window docking.
        
                The main window is initialized with a gray foreground to hide undocked windows during the first several frames.
                The visibility of the main menu bar is set based on the application's release status. Settings for margins,
                background color, and whether to dock windows on startup are retrieved and applied to the main window.
                If docking is enabled, an asynchronous task is created to dock the windows.
                
        """
    def _dock_windows(self):
        """
        Asynchronously docks the various windows (Stage, Viewport, Property, Toolbar, Console) in the main window.
        
                This method waits for the windows to become available and then docks them in the appropriate positions.
                It also hides the foreground overlay after a few frames to ensure that the windows are visible.
                
        """
    def destroy(self):
        """
        Cleans up the main window by setting its reference and setup window task to None.
        """
    def get_main_menu_bar(self) -> omni.ui._ui.MenuBar:
        """
        Returns the main menu bar.
        
                Returns:
                    ui.MenuBar: The main menu bar.
        """
    def get_status_bar_frame(self) -> omni.ui._ui.Frame:
        """
        Returns the frame containing the status bar.
        
                Returns:
                    ui.Frame: The frame containing the status bar.
        """
    def show_hide_menu(self):
        """
        Toggles the visibility of the main menu bar.
        """
    def show_hide_status_bar(self):
        """
        Toggles the visibility of the status bar.
        """
