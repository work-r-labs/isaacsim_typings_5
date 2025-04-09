"""

Omni Kit Hotkeys Core
---------------------

Omni Kit Hotkeys Core is a framework for creating, registering, and discovering hotkeys.

Here is an example of registering an hokey from Python that execute action "omni.kit.window.file::new" to create a new file when CTRL + N pressed:

.. code-block::

    hotkey_registry = omni.kit.hotkeys.core.get_hotkey_registry()

    hotkey_registry.register_hotkey(
        "your_extension_id",
        "CTRL + N",
        "omni.kit.window.file",
        "new",
        filter=None,
    )

For more examples, please consult the Usage Examples page.
"""
from __future__ import annotations
from omni.kit.hotkeys.core.extension import HotkeysExtension
from omni.kit.hotkeys.core.extension import get_hotkey_context
from omni.kit.hotkeys.core.extension import get_hotkey_registry
from omni.kit.hotkeys.core.filter import HotkeyFilter
from omni.kit.hotkeys.core.hotkey import Hotkey
from omni.kit.hotkeys.core.key_combination import KeyCombination
from omni.kit.hotkeys.core.keyboard_layout import KeyboardLayoutDelegate
from omni.kit.hotkeys.core.registry import HotkeyRegistry
from . import context
from . import event
from . import extension
from . import filter
from . import hotkey
from . import hovered_window
from . import key_combination
from . import keyboard_layout
from . import registry
from . import storage
from . import trigger
__all__: list = ['KeyCombination', 'Hotkey', 'HotkeyRegistry', 'HotkeyFilter', 'KeyboardLayoutDelegate', 'get_hotkey_context', 'get_hotkey_registry', 'HOTKEY_REGISTER_EVENT', 'HOTKEY_DEREGISTER_EVENT', 'HOTKEY_CHANGED_EVENT']
HOTKEY_CHANGED_EVENT: int = 10827232480668153655
HOTKEY_DEREGISTER_EVENT: int = 2474222670972880127
HOTKEY_REGISTER_EVENT: int = 4501832906121664548
