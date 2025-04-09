"""

A set of simple popup dialogs with optional input fields and two buttons, OK and Cancel.

Example:

.. code-block:: python

    dialog = InputDialog(
        width=450,
        pre_label="prefix",
        post_label="postfix",
        ok_handler=on_okay,
        cancel_handler=on_cancel,
    )

"""
from __future__ import annotations
from omni.kit.window.popup_dialog.dialog import PopupDialog
from omni.kit.window.popup_dialog.form_dialog import FormDialog
from omni.kit.window.popup_dialog.form_dialog import FormWidget
from omni.kit.window.popup_dialog.input_dialog import InputDialog
from omni.kit.window.popup_dialog.input_dialog import InputWidget
from omni.kit.window.popup_dialog.message_dialog import MessageDialog
from omni.kit.window.popup_dialog.message_dialog import MessageWidget
from omni.kit.window.popup_dialog.options_dialog import OptionsDialog
from omni.kit.window.popup_dialog.options_dialog import OptionsWidget
from omni.kit.window.popup_dialog.options_menu import OptionsMenu
from omni.kit.window.popup_dialog.options_menu import OptionsMenuWidget
from . import dialog
from . import form_dialog
from . import input_dialog
from . import message_dialog
from . import options_dialog
from . import options_menu
from . import style
__all__: list = ['MessageDialog', 'MessageWidget', 'InputDialog', 'InputWidget', 'FormDialog', 'FormWidget', 'OptionsDialog', 'OptionsWidget', 'OptionsMenu', 'OptionsMenuWidget', 'PopupDialog']
