"""
This module provides functionality for managing USD stage templates, including registration, creation, and transformation of stages within Omniverse Kit.
"""
from __future__ import annotations
from omni.kit.stage_template.core.stage_core import CoreStageExtension
from omni.kit.stage_template.core.stage_core import get_default_template
from omni.kit.stage_template.core.stage_core import get_stage_template
from omni.kit.stage_template.core.stage_core import get_stage_template_list
from omni.kit.stage_template.core.stage_core import new_stage
from omni.kit.stage_template.core.stage_core import new_stage_async
from omni.kit.stage_template.core.stage_core import new_stage_with_callback
from omni.kit.stage_template.core.stage_core import register_template
from omni.kit.stage_template.core.stage_core import unregister_template
from . import stage_core
__all__: list = ['register_template', 'unregister_template', 'get_stage_template_list', 'get_stage_template', 'get_default_template', 'new_stage', 'new_stage_with_callback', 'new_stage_async']
