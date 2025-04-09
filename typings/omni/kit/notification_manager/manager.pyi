from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.notification_manager.notification_info import NotificationInfo
from omni.kit.notification_manager.notification_info import NotificationStatus
from omni.kit.notification_manager.prompt import Prompt
from omni import ui
__all__ = ['Notification', 'NotificationInfo', 'NotificationManager', 'NotificationStatus', 'Prompt', 'SETTINGS_DISABLE_NOTIFICATIONS', 'SETTINGS_LOOP_IDLE_TIME', 'asyncio', 'carb', 'omni', 'ui']
class Notification:
    """
    Handler of notification
    """
    def __init__(self, notification_info: omni.kit.notification_manager.notification_info.NotificationInfo, notification_manager):
        """
        Internal constructor
        """
    def _docking_to(self, window_x, window_y, window_width, window_height, offset_y = 0):
        ...
    def _hide(self):
        ...
    def _pre_warming(self):
        ...
    def _step_and_check(self, dt):
        ...
    def destroy(self):
        ...
    def dismiss(self):
        ...
    @property
    def _dismissed(self):
        ...
    @property
    def _hovered(self):
        ...
    @property
    def dismissed(self):
        ...
    @property
    def info(self):
        ...
class NotificationManager:
    def _on_docking_window_changed(self):
        ...
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
    def remove_notification(self, notification: Notification):
        ...
SETTINGS_DISABLE_NOTIFICATIONS: str = '/exts/omni.kit.notification_manager/disable_notifications'
SETTINGS_LOOP_IDLE_TIME: str = '/exts/omni.kit.notification_manager/loopIdleTimeInSeconds'
