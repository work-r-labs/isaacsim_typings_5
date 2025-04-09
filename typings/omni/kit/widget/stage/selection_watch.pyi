from __future__ import annotations
import carb as carb
import omni as omni
from pxr import Sdf
from pxr import Trace
__all__: list = ['DefaultSelectionWatch']
class DefaultSelectionWatch:
    """
     A watcher object that updates selections in TreeView when scene selections are updated, and vice versa. 
    """
    @staticmethod
    def _DefaultSelectionWatch__on_stage_items_selection_changed(*args, **kwargs):
        ...
    @staticmethod
    def _on_widget_selection_changed(*args, **kwargs):
        """
        Send the selection from TreeView to Kit
        """
    def __init__(self, tree_view = None, usd_context = None):
        """
        
                Creates the selection watch instance associated with the given tree view and usd context.
        
                Keyword Args:
                    tree_view (Optional[omni.ui.TreeView]): The treeview object to update selections from/to.
                    usd_context (Optional[omni.usd.UsdContext]): The current UsdContext.
                
        """
    def destroy(self):
        """
        Destroys the watcher object. Clears out event subscriptions.
        """
    def enable_filtering_checking(self, enable: bool):
        """
        
                When `enable` is True, SelectionWatch should consider filtering when changing Kit's selection.
        
                Args:
                    enable (bool): Whether to enable filtering selections.
                
        """
    def set_filtering(self, filter_string: typing.Optional[str]):
        """
        
                Sets the filter string to the given string (all lower case).
        
                Args:
                    filter_string (Optional[str]): The filter string, can be None.
                
        """
    def set_tree_view(self, tree_view):
        """
        
                Replaces the TreeView that should show the selection with the given TreeView object if they are different.
        
                Args:
                    tree_view (omni.ui.TreeView): The tree view object to update to.
                
        """
