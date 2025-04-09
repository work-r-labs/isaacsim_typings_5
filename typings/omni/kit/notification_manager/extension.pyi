from __future__ import annotations
import omni as omni
from omni.kit.notification_manager.manager import NotificationManager
from omni.kit.notification_manager.notification_info import NotificationInfo
from omni.kit.notification_manager.notification_info import NotificationStatus
import weakref as weakref
__all__: list = ['post_notification', 'destroy_all_notifications', 'get_all_notifications', 'NotificationManagerExtension']
class NotificationManagerExtension(omni.ext._extensions.IExt):
    def destroy_all_notifications(self):
        ...
    def get_all_notifications(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
    def post_notification(self, notification_info: omni.kit.notification_manager.notification_info.NotificationInfo):
        ...
def destroy_all_notifications():
    ...
def get_all_notifications():
    ...
def post_notification(text, hide_after_timeout = True, duration = 3, status = 1, button_infos = list()):
    """
    
        Post notification.
        If viewport is visible, it will be docked to the right-bottom of viewport.
        Otherwise, it will be docked to main window.
    
        Args:
            text (str): The notification text.
    
        Keyword Args:
            hide_after_timeout (bool): If the notification will hide after duration.
                                        If it's False, and button_details are not provided, it will display a default dismiss button.
            duration (int): The duration (in seconds) after which the notification will be hidden.
                            This duration only works if hide_after_timeout is True.
            status (NotificationStatus): The notification type. By default, NotificationStatus.INFO as information.
            button_infos ([NotificationButtonInfo]): Array of buttons.
    
        Returns:
            Notification handler.
        
        Examples:
    
            >>> import omni.kit.notification_manager as nm
            >>> ok_button = nm.NotificationButtonInfo("OK", on_complete=None)
            >>> cancel_button = nm.NotificationButtonInfo("CANCEL", on_complete=None)
            >>> notification = nm.post_notification(
                        "Notification Example",
                        hide_after_timeout=False,
                        duration=0,
                        status=nm.NotificationStatus.WARNING,
                        button_infos=[ok_button, cancel_button]
                    )
    
        
    """
_global_instance: weakref.ReferenceType  # value = <weakref at 0x709fbe765490; to 'NotificationManagerExtension' at 0x709fbe78f380>
