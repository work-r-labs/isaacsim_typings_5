"""

Manage Registration of column delegates to be used by :obj:`FileBrowserTreeView`.
"""
from __future__ import annotations
import carb as carb
from omni.kit.widget.filebrowser.abstract_column_delegate import AbstractColumnDelegate
from omni.kit.widget.filebrowser.singleton import Singleton
__all__: list = ['ColumnDelegateRegistry']
