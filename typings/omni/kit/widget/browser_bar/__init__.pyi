"""

The :obj:`PathField` widget supes up tree navigation via keyboard entry. This widget extends that
experience further by queuing up the user's navigation history. As in any modern day browser, the
user can then directly jump to any previously visited path.

Example:

.. code-block:: python

    browser_bar = BrowserBar(
        visited_history_size=20,
        branching_options_provider=branching_options_provider,
        apply_path_handler=apply_path_handler,
    )

"""
from __future__ import annotations
from omni.kit.widget.browser_bar.widget import BrowserBar
from . import model
from . import style
from . import widget
__all__: list = ['BrowserBar']
