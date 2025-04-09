from __future__ import annotations
import datetime as datetime
from omni.kit.window.filepicker.datetime.date_widget import DateWidget
from omni.kit.window.filepicker.datetime.time_widget import TimeWidget
from omni.kit.window.filepicker.datetime.timezone_widget import TimezoneWidget
from omni.kit.window.filepicker.style import get_style
from omni import ui
__all__: list = ['TimestampWidget']
class TimestampWidget:
    @staticmethod
    def create_timestamp_widget() -> TimestampWidget:
        """
        
                 Create and return a TimestampWidget. 
                 
                 
                 Returns: 
                      :obj:'TimestampWidget': A TimestampWidget instance.
                
        """
    @staticmethod
    def delete_timestamp_widget(widget: TimestampWidget):
        """
        
                 Delete a TimestampWidget.
                 
                 Args:
                      widget(:obj:'TimestampWidget'): The widget to be deleted. If None is passed no action is taken
                
        """
    @staticmethod
    def on_selection_changed(widget: TimestampWidget, selected: typing.List[str]):
        """
        
                 Callback for when selection changes. 
                 
                 Args:
                      widget (:obj:'TimestampWidget'): TimestampWidget that was toggled.
                      selected (List[str]): List of items that were selected. If None is selected no change is made.
                
        """
    def __del__(self):
        ...
    def __init__(self, **kwargs):
        """
        
                Timestamp Widget.
        
                
        """
    def _build_ui(self):
        ...
    def _on_timestamp_changed(self, model):
        ...
    def _on_timestamp_checked(self, model):
        ...
    def add_on_check_changed_fn(self, fn):
        """
        
                 Add a function to be called when the check changes. The function will be called with the following arguments
                 
                 Args:
                      fn (Callable): The function to be.
                
        """
    def destroy(self):
        """
        
                Destroy and clean up the widget.
                
        """
    def get_timestamp_url(self, url: str) -> str:
        """
        
                 Returns the URL to use for the timestamp. 
                 
                 Args:
                      url (str): The url to use.
                 
                 Returns: 
                      str: The url with the timestamp appended to it if the timestamp checkbox is checked. 
                
        """
    def on_list_checkpoint(self, select):
        """
        
                 Called when user selects a checkpoint. 
                 
                 Args:
                      select(str): selected item.
                
        """
    def rebuild(self, selected: typing.List[str]):
        """
        
                 Rebuild the frame. This is called when the user clicks on the rebuild button. 
                 Args:
                      selected (List[str]): List of items that have been selected. 
                
        """
    def set_checkpoint_widget(self, widget):
        """
        
                 Set the checkpoint widget. This is used to provide feedback to the user when they want to check out the state of the experiment
                 
                 Args:
                      widget(obj): The widget to be
                
        """
    def set_url(self, url: str):
        """
        
                 Set the url.
                 
                 Args:
                      url(str): The URL to set.
                
        """
    @property
    def check(self) -> bool:
        """
        
                 Get check box status of timestamp widget. 
                 Returns: 
                      bool: True if the timestamp is valid False otherwise.
                
        """
    @check.setter
    def check(self, value: bool):
        """
        
                 Set the Check box status for the timestamp. 
                 Args:
                      value (bool): True if the timestamp should be checked False otherwise
                
        """
