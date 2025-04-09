from __future__ import annotations
from omni.kit.viewport.menubar.core.preference.menubar_treeview_delegate import MenubarTreeViewDelegate
from omni.kit.viewport.menubar.core.preference.model import PreferenceModel
import omni.kit.window.preferences.scripts.preference_builder
from omni.kit.window.preferences.scripts.preference_builder import PreferenceBuilder
from omni import ui
__all__: list = ['ViewportMenubarPage']
class ViewportMenubarPage(omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder):
    """
    
        Represent a preference page to show and edit viewport menubar settings.
        
    """
    def __init__(self, model: <function singleton.<locals>.getinstance at 0x709ef21dcca0>):
        ...
    def build(self):
        ...
    def destroy(self):
        ...
VIEWPORT_PREFERENCE_STYLE: dict = {'TreeView.Frame': {'background_color': 4281611314, 'padding': 10}, 'TreeView.Item.Label': {'color': 4288585374}, 'TreeView.Item.Line': {'color': 864716663}, 'TreeView.Item.CheckBox': {'font_size': 10, 'background_color': 4288585374, 'color': 4280492319, 'border_radius': 0}, 'TreeView.Item.ComboBox': {'color': 4288585374, 'secondary_color': 4280492319, 'border_radius': 0}, 'TreeView.Item.Alignment::left': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/align_left.svg'}, 'TreeView.Item.Alignment::left:checked': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/align_disabled_left.svg'}, 'TreeView.Item.Alignment::right': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/align_right.svg'}, 'TreeView.Item.Alignment::right:checked': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.viewport.menubar.core-107.1.2+d02c707b/data/icons/align_disabled_right.svg'}, 'TreeView:drop': {'border_color': 4291137818, 'background_selected_color': 0}}
