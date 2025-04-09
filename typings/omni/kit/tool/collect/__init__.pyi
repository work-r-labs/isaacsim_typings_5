"""
This module provides functionality for collecting USD assets and their dependencies into a single directory, offering a comprehensive solution for asset collection within Omniverse Kit extensions.
"""
from __future__ import annotations
from omni.kit.tool.collect.extension import PublicExtension
from omni.kit.tool.collect.extension import get_instance
from omni.kit.usd.collect.collector import Collector
from omni.kit.usd.collect.collector import CollectorException
from omni.kit.usd.collect.collector import CollectorTaskType
from . import actions
from . import extension
from . import folder_collect_helper
from . import icons
from . import main_window
from . import progress_popup
from . import singleton
__all__: list = ['PublicExtension', 'get_instance', 'Collector', 'CollectorTaskType', 'CollectorException']
