"""

Post notification to right-bottom of viewport or main window (if viewport invisible).
"""
from __future__ import annotations
from omni.kit.notification_manager.extension import NotificationManagerExtension
from omni.kit.notification_manager.extension import destroy_all_notifications
from omni.kit.notification_manager.extension import get_all_notifications
from omni.kit.notification_manager.extension import post_notification
from omni.kit.notification_manager.notification_info import NotificationButtonInfo
from omni.kit.notification_manager.notification_info import NotificationStatus
from . import extension
from . import icons
from . import manager
from . import notification_info
from . import prompt
from . import singleton
__all__: list = ['post_notification', 'destroy_all_notifications', 'get_all_notifications', 'NotificationButtonInfo', 'NotificationStatus']
