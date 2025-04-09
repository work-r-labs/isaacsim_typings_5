"""

A UI alternative to omni.ui.StringField for navigating tree views with the keyboard. As the user
navigates the tree using TAB, Backspace, and Arrow keys, they are constantly provided branching 
options via auto-filtered tooltips.

Example:

.. code-block:: python

    path_field = PathField(
        apply_path_handler=self._apply_path_handler,
        branching_options_provider=self._branching_options_provider,
    )

"""
from __future__ import annotations
from omni.kit.widget.path_field.widget import PathField
from . import model
from . import style
from . import widget
__all__: list = ['PathField']
