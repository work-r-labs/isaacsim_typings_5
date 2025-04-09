from __future__ import annotations
import asyncio as asyncio
import carb as carb
import gc as gc
from isaacsim.core.prims.impl.single_articulation import SingleArticulation
from isaacsim.core.utils.prims import get_prim_object_type
from isaacsim.gui.components.menu import make_menu_item_description
from isaacsim.gui.components.style import get_style
from isaacsim.gui.components.ui_utils import add_line_rect_flourish
from isaacsim.gui.components.ui_utils import btn_builder
from isaacsim.gui.components.ui_utils import float_builder
from isaacsim.gui.components.ui_utils import setup_ui_headers
from isaacsim.gui.components.ui_utils import state_btn_builder
from isaacsim.gui.components.ui_utils import str_builder
from isaacsim.gui.components.widgets import DynamicComboBoxModel
from isaacsim.robot_motion.lula_test_widget.test_scenarios import LulaTestScenarios
import numpy as np
import omni as omni
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.utils import add_menu_items
from omni.kit.menu.utils.utils import remove_menu_items
from omni.kit.window.extensions.ext_components import SimpleCheckBox
from omni import physx as _physx
from omni import ui
import os as os
from pxr import Usd
import weakref as weakref
__all__ = ['DynamicComboBoxModel', 'EXTENSION_NAME', 'Extension', 'LABEL_WIDTH', 'LulaTestScenarios', 'MAX_DOF_NUM', 'MenuItemDescription', 'SimpleCheckBox', 'SingleArticulation', 'Usd', 'add_line_rect_flourish', 'add_menu_items', 'asyncio', 'btn_builder', 'carb', 'float_builder', 'gc', 'get_prim_object_type', 'get_style', 'is_urdf_file', 'is_yaml_file', 'make_menu_item_description', 'np', 'omni', 'on_filter_urdf_item', 'on_filter_yaml_item', 'os', 'remove_menu_items', 'setup_ui_headers', 'state_btn_builder', 'str_builder', 'ui', 'weakref']
class Extension(omni.ext._extensions.IExt):
    def _build_info_ui(self):
        ...
    def _build_kinematics_ui(self):
        ...
    def _build_rmpflow_ui(self):
        ...
    def _build_selection_ui(self):
        ...
    def _build_trajectory_generation_ui(self):
        ...
    def _build_ui(self):
        ...
    def _clear_selection_combobox(self):
        ...
    def _disable_lula_dropdowns(self):
        ...
    def _enable_load_button(self):
        ...
    def _enable_lula_dropdowns(self):
        ...
    def _get_next_action(self):
        ...
    def _get_selected_ee_frame(self):
        ...
    def _menu_callback(self):
        ...
    def _on_combobox_selection(self, model = None, val = None):
        ...
    def _on_physics_step(self, step):
        """
        Callback for Physics Step.
        
                Args:
                    step ([type]): [description]
                
        """
    def _on_selection(self, prim_path):
        """
        Creates an Articulation Object from the selected articulation prim path.
                   Updates the UI with the Selected articulation.
        
                Args:
                    prim_path (string): path to selected articulation
                
        """
    def _on_stage_event(self, event):
        """
        Callback for Stage Events
        
                Args:
                    event (omni.usd.StageEventType): Event Type
                
        """
    def _on_timeline_event(self, e):
        """
        Callback for Timeline Events
        
                Args:
                    event (omni.timeline.TimelineEventType): Event Type
                
        """
    def _on_window(self, visible):
        ...
    def _refresh_ee_frame_combobox(self):
        ...
    def _refresh_selection_combobox(self):
        ...
    def _refresh_ui(self, articulation):
        """
        Updates the GUI with a new Articulation's properties.
        
                Args:
                    articulation (SingleArticulation): [description]
                
        """
    def _reset_scenario(self, model = None, value = None):
        ...
    def _reset_ui(self):
        """
        Reset / Hide UI Elements.
        """
    def _set_enable_rmpflow_buttons(self, enable):
        ...
    def _set_enable_trajectory_panel(self, enable):
        ...
    def get_all_articulations(self):
        """
        Get all the articulation objects from the Stage.
        
                Returns:
                    list(str): list of prim_paths as strings
                
        """
    def get_articulation_values(self, articulation):
        """
        Get and store the latest dof_properties from the articulation.
                   Update the Properties UI.
        
                Args:
                    articulation (SingleArticulation): Selected Articulation
                
        """
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id: str):
        """
        Initialize extension and UI elements
        """
def is_urdf_file(path: str):
    ...
def is_yaml_file(path: str):
    ...
def on_filter_urdf_item(item) -> bool:
    ...
def on_filter_yaml_item(item) -> bool:
    ...
EXTENSION_NAME: str = 'Lula Test Widget'
LABEL_WIDTH: int = 160
MAX_DOF_NUM: int = 100
