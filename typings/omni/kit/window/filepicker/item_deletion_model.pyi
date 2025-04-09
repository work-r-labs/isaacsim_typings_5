from __future__ import annotations
import omni.kit.widget.filebrowser.model
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni import ui
import omni.ui._ui
__all__: list = ['ConfirmItemDeletionListItem']
class ConfirmItemDeletionListItem(omni.ui._ui.AbstractItem):
    """
    Single item of the list of `FileBrowserItem`s to delete.
    """
    def __init__(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        """
        
                Single item of the list of `FileBrowserItem`s to delete.
        
                Args:
                    item (FileBrowserItem): The item of the File Browser which should be deleted.
        
                
        """
class ConfirmItemDeletionListModel(omni.ui._ui.AbstractItemModel):
    """
    Model representing a list of `FileBrowserItem`s to delete.
    """
    def __init__(self, items: [omni.kit.widget.filebrowser.model.FileBrowserItem]):
        """
        
                Model representing a list of `FileBrowserItem`s to delete.
        
                Args:
                    items ([FileBrowserItem]): List of File Browser items which should be deleted.
        
                
        """
    def get_item_children(self, item: ConfirmItemDeletionListItem) -> [ConfirmItemDeletionListItem]:
        """
        
                Return the list of all children of the given item to present to the display widget.
        
                Args:
                    item (ConfirmItemDeletionListItem): Item of the model.
        
                Returns:
                    [ConfirmItemDeletionListItem]: The list of all children of the given item to present to the display widget.
        
                
        """
    def get_item_value_model(self, item: ConfirmItemDeletionListItem, column_id: int) -> omni.ui._ui.SimpleStringModel:
        """
        
                Return the value model for the given item at the given column index.
        
                Args:
                    item (ConfirmItemDeletionListItem): Item of the model for which to return the model.
                    column_id (int): Index of the column for which to return the model.
        
                Returns:
                    ui.SimpleStringModel: The model for the given item at the given column index.
        
                
        """
    def get_item_value_model_count(self, item: ConfirmItemDeletionListItem) -> int:
        """
        
                Return the number of columns to display.
        
                Args:
                    item (ConfirmItemDeletionListItem): Item of the model.
        
                Returns:
                    int: The number of columns to display.
        
                
        """
