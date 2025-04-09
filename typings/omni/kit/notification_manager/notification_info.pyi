from __future__ import annotations
import typing
__all__: list = ['NotificationButtonInfo', 'NotificationStatus']
class NotificationButtonInfo:
    """
    
        Represent a button in notification.
    
        Args:
            text (str): The button text.
    
        Keyword Args:
            on_complete (Callable[[None], None]): The button handler when clicked.
        
    """
    def __init__(self, text, on_complete: typing.Callable[[NoneType], NoneType] = None):
        ...
    @property
    def handler(self):
        """
        Button handler when clicked
        """
    @property
    def text(self):
        """
        Button text
        """
class NotificationInfo:
    def __init__(self, text, hide_after_timeout = True, duration = 3, status = 1, button_infos = list()):
        ...
    @property
    def button_infos(self):
        ...
    @property
    def duration(self):
        ...
    @property
    def hide_after_timeout(self):
        ...
    @property
    def status(self):
        ...
    @property
    def text(self):
        ...
class NotificationStatus:
    """
    
        Notification status.
    
        Different status has different icon and background color.
    
        Could be:
            - NotificationStatus.INFO
            - NotificationStatus.WARNING
        
    """
    INFO: typing.ClassVar[int] = 1
    WARNING: typing.ClassVar[int] = 0
