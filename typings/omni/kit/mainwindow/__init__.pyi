"""
The extension manages the main window of the application.
"""
from __future__ import annotations
import omni as omni
from omni.kit.mainwindow.scripts.extension import MainWindowExtension
from omni.kit.mainwindow.scripts.extension import get_main_window
from omni.kit.mainwindow.scripts.main_window import MainWindow
from . import scripts
__all__: list = ['MainWindow', 'get_main_window']
g_main_window = None
