from __future__ import annotations
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.window.filepicker.item_deletion_model import ConfirmItemDeletionListModel
from omni.kit.window.filepicker.style import get_style
import omni.kit.window.popup_dialog.dialog
from omni.kit.window.popup_dialog.dialog import PopupDialog
from omni import ui
import omni.ui._ui
__all__: list = ['ConfirmItemDeletionDialog']
class ConfirmItemDeletionDialog(omni.kit.window.popup_dialog.dialog.PopupDialog):
    """
    Dialog prompting the User to confirm the deletion of the provided list of files and folders.
    """
    def __init__(self, items: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem], title: str = 'Confirm File Deletion', message: str = 'You are about to delete', message_fn: typing.Callable[[NoneType], NoneType] = None, parent: omni.ui._ui.Widget = None, width: int = 500, ok_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.PopupDialog], NoneType] = None, cancel_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.PopupDialog], NoneType] = None):
        """
        
                Dialog prompting the User to confirm the deletion of the provided list of files and folders.
        
                Args:
                    items ([FileBrowserItem]): List of files and folders to delete.
                    title (str): Title of the dialog. Default "Confirm File Deletion".
                    message (str): Basic message. Default "You are about to delete".
                    message_fn (Callable[[None], None]): Message build function.
                    parent (:obj:`omni.ui.Widget`): OBSOLETE. If specified, the dialog position is relative to this widget. Default `None`.
                    width (int): Dialog width. Default `500`.
                    ok_handler (Callable): Function to execute upon clicking the "Yes" button. Function signature:
                        void ok_handler(dialog: :obj:`PopupDialog`)
                    cancel_handler (Callable): Function to execute upon clicking the "No" button. Function signature:
                        void cancel_handler(dialog: :obj:`PopupDialog`)
        
                
        """
    def _build_ui(self) -> None:
        ...
    def destroy(self) -> None:
        """
        Destructor.
        """
    def rebuild_ui(self, message_fn: typing.Callable[[NoneType], NoneType]) -> None:
        """
        
                Rebuild ui widgets with new message
        
                Args:
                    message_fn (Callable[[None], None]): Message build function.
                
        """
