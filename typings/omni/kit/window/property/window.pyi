"""

omni.kit.window.property PropertyWindow class
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import copy as copy
from omni.kit.widget.searchfield.searchfield import SearchField
from omni.kit.window.property.property_filter import PropertyFilter
import omni.kit.window.property.property_scheme_delegate
from omni.kit.window.property.property_scheme_delegate import PropertySchemeDelegate
import omni.kit.window.property.property_widget
from omni.kit.window.property.property_widget import PropertyWidget
from omni import ui
import sys as sys
__all__: list = ['PropertyWindow']
class PropertyWindow:
    """
    
        Property Window framework.
        
    """
    def _PropertyWindow__dock_changed(self, is_docked):
        ...
    def _PropertyWindow__selected_in_dock_changed(self, is_selected):
        ...
    def __init__(self, window_kwargs = None, properties_frame_kwargs = None):
        """
        
                Create a PropertyWindow.
        
                Args:
                    window_kwargs (dict): Additional kwargs to pass to ui.Window.
                    properties_frame_kwargs (dict): Additional kwargs to pass to ui.ScrollingFrame.
                
        """
    def _on_search(self, search_words: typing.Optional[typing.List[str]]) -> None:
        ...
    def _rebuild_window(self):
        ...
    def _visibility_changed_fn(self, visible):
        ...
    def destroy(self):
        """
        Destroy function. Class cleanup function
        """
    def get_payload(self):
        ...
    def get_scheme(self):
        """
        
                Gets the current scheme being displayed in Property Window.
                
        """
    def notify(self, scheme: str, payload: typing.Any):
        """
        
                Notify Property Window of a scheme and/or payload change.
                This is the function to trigger refresh of PropertyWindow.
        
                Args:
                    scheme (str): Scheme of this notification.
                    payload: Payload to refresh the widgets.
                
        """
    def register_scheme_delegate(self, scheme: str, name: str, delegate: omni.kit.window.property.property_scheme_delegate.PropertySchemeDelegate):
        """
        
                Register a PropertySchemeDelegate for a given scheme. A PropertySchemeDelegate tests the payload and determines
                what widgets to be drawn in what order. A scheme can have multiple PropertySchemeDelegate and their result will
                be merged to display all relevant widgets.
        
                PropertySchemeDelegate does not hide widgets that are not returned from its get_widgets function. If you want to
                hide certain widget, return them in PropertySchemeDelegate.get_unwanted_widgets. See PropertySchemeDelegate's
                documentation for details.
        
                Args:
                    scheme (str): Scheme of the PropertySchemeDelegate to be added to.
                    name (str): A unique name to identify the PropertySchemeDelegate under. Delegate with existing name will be
                                overridden.
                    delegate (PropertySchemeDelegate): A PropertySchemeDelegate instance to be added.
                
        """
    def register_widget(self, scheme: str, name: str, property_widget: omni.kit.window.property.property_widget.PropertyWidget, top_stack: bool = True):
        """
        
                Registers a PropertyWidget to PropertyWindow.
        
                Args:
                    scheme (str): Scheme of the PropertyWidget will work with.
                    name (str): A unique name to identify the PropertyWidget under. Widget with existing name will be overridden.
                    property_widget (property_widget.PropertyWidget): A PropertyWidget instance to be added.
                    top_stack (bool): Widgets are managed in double stack:
                                      True to register the widget to "Top" stack which layouts widgets from top to bottom.
                                      False to register the widget to "Button" stack which layouts widgets from bottom to top and always below the "Top" stack.
                
        """
    def request_rebuild(self):
        """
        
                Requests the entire property window to be rebuilt.
                
        """
    def reset_scheme_delegate_layout(self, scheme: str):
        """
        
                Reset the order so PropertySchemeDelegate will be processed in the order of registration when building UI.
        
                Args:
                    scheme (str): Scheme of the PropertySchemeDelegate order to be removed from.
                
        """
    def restore_scroll_pos(self):
        """
        Restore scroll position from previous position. Used when trying to keep scroll position when selecting attributes of same type.
        """
    def save_scroll_pos(self, reset = False):
        """
        Save scroll position to previous position. Used when trying to keep scroll position when selecting attributes of same type.
        
                Args:
                    reset (bool): If True clear old scroll position.
                
        """
    def set_scheme_delegate_layout(self, scheme: str, layout: typing.List[str]):
        """
        
                Register a list of PropertySchemeDelegate's names to finalize the order and visibility of all registered
                PropertySchemeDelegate. Useful if you need a fixed layout of Property Widgets for your Kit experience.
        
                Remark:
                    If you're a Property Widget writer, DO NOT call this function. It should only be called by Kit Experience
                    to tune the final look and layout of the Property Window.
        
                Args:
                    scheme (str): Scheme of the PropertySchemeDelegate order to be added to.
                    layout (List(str)): a list of PropertySchemeDelegate's name, in the order of being processed when building
                        UI. Scheme delegate not in this will be skipped.
                
        """
    def set_visibility_changed_listener(self, listener: callable):
        """
        Adds callback function for when window visibility is changed.
        
                Args:
                    listener (callable): visibility changed callback.
                
        """
    def set_visible(self, visible: bool):
        """
        Set window visibility state.
        
                Args:
                    visible (bool): Visible state of the window.
                
        """
    def unregister_scheme_delegate(self, scheme: str, name: str):
        """
        
                Unregister a PropertySchemeDelegate from PropertyWindow by name.
        
                Args:
                    scheme (str): Scheme of the PropertySchemeDelegate to be removed from.
                    name (str): The name to find the PropertySchemeDelegate and remove.
                
        """
    def unregister_widget(self, scheme: str, name: str, top_stack: bool = True):
        """
        
                Unregister a PropertyWidget from PropertyWindow.
        
                Args:
                    scheme (str): Scheme of the PropertyWidget to be removed from.
                    name (str): The name to find the PropertyWidget and remove.
                    top_stack (bool): see @register_widget
                
        """
    @property
    def paused(self):
        """
        
                Gets if property window refresh is paused.
                
        """
    @paused.setter
    def paused(self, to_pause: bool):
        """
        
                Sets if property window refresh is paused.
                When property window is paused, calling `notify` will not refresh Property Window content.
                When property window is resumed, the window will refresh using the queued schemes and payloads `notified` to Property Window while paused.
        
                Args:
                    to_pause (bool): True to pause property window refresh. False to resume property window refresh.
                
        """
    @property
    def properties_frame(self):
        """
        Gets the ui.ScrollingFrame container of PropertyWidgets
        """
LABEL_HEIGHT: int = 18
