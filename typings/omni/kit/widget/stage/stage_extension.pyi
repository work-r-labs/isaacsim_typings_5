from __future__ import annotations
import omni as omni
from omni.kit.widget.stage.delegates import name_column_delegate
from omni.kit.widget.stage.delegates.name_column_delegate import NameColumnDelegate
from omni.kit.widget.stage.delegates import type_column_delegate
from omni.kit.widget.stage.delegates.type_column_delegate import TypeColumnDelegate
from omni.kit.widget.stage.delegates import visibility_column_delegate
from omni.kit.widget.stage.delegates.visibility_column_delegate import VisibilityColumnDelegate
from omni.kit.widget.stage.export_utils import _get_stage_open_sub
from omni.kit.widget.stage.stage_actions import ActionManager
from omni.kit.widget.stage.stage_item import StageItem
from omni.kit.widget.stage.stage_style import Styles as StageStyles
__all__: list = ['StageWidgetExtension']
class StageWidgetExtension(omni.ext._extensions.IExt):
    """
    The entry point for Stage Widget.
    """
    def on_shutdown(self):
        """
        Shutdown handler for the stage widget extension.
        """
    def on_startup(self, ext_id):
        """
        
                Startup handler for the stage widget extension.
        
                Args:
                    ext_id (str): The extension id.
                
        """
