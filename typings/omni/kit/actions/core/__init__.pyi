"""

Omni Kit Actions Core
---------------------

Omni Kit Actions Core is a framework for creating, registering, and discovering actions.

Here is an example of registering an action that creates a new file when it is executed:

.. code-block::

    action_registry = omni.kit.actions.core.get_action_registry()
    actions_tag = "File Actions"

    action_registry.register_action(
        extension_id,
        "new",
        omni.kit.window.file.new,
        display_name="File->New",
        description="Create a new USD stage.",
        tag=actions_tag,
    )

For more examples, please consult the Python and C++ Usage Example pages.

For Python API documentation, please consult the following subpages.

For C++ API documentation, please consult the API(C++) page.
"""
from __future__ import annotations
import omni as omni
from omni.kit.actions.core._kit_actions_core import Action
from omni.kit.actions.core._kit_actions_core import IActionRegistry
from omni.kit.actions.core._kit_actions_core import acquire_action_registry
from omni.kit.actions.core._kit_actions_core import release_action_registry
from omni.kit.actions.core.actions import ActionsExtension
from omni.kit.actions.core.actions import execute_action
from omni.kit.actions.core.actions import get_action_registry
from . import _kit_actions_core
from . import actions
from . import test_extension_actions_api
__all__: list = ['Action', 'IActionRegistry', 'get_action_registry', 'execute_action']
