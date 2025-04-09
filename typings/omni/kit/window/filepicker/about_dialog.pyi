from __future__ import annotations
from omni.kit.window.filepicker.style import get_style
import omni.kit.window.popup_dialog.dialog
from omni.kit.window.popup_dialog.dialog import PopupDialog
from omni import ui
import pathlib
__all__: list = ['AboutDialog']
class AboutDialog(omni.kit.window.popup_dialog.dialog.PopupDialog):
    """
    Dialog to show the omniverse server info.
    """
    def __init__(self, server_info):
        """
        
                Initialize an AboutDialog.
        
                Args:
                    server_info ([FileBrowserItem]): server's information.
                    title (str): Title of the dialog. Default "Confirm File Deletion".
                    width (int): Dialog width. Default `500`.
                    ok_handler (Callable): Function to execute upon clicking the "Yes" button. Function signature:
                        void ok_handler(dialog: :obj:`PopupDialog`)
                
        """
    def _build_info_item(self, supported: bool, info: str):
        ...
    def _build_ui(self) -> None:
        ...
    def destroy(self) -> None:
        """
        Destructor.
        """
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.filepicker-2.11.7+d02c707b/icons/NvidiaDark')
