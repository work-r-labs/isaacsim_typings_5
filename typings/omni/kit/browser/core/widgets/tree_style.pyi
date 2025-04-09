from __future__ import annotations
import omni.ui.color_utils
import typing
__all__ = ['ColorsNew', 'Constants', 'TREE_UI_STYLES', 'cl']
class ColorsNew:
    NewSelected: typing.ClassVar[str] = 'shade:4293105444;light=4291137818'
    NewSelectedBG: typing.ClassVar[str] = 'shade:4280821800'
    NewText: typing.ClassVar[str] = 'shade:4286743170;light=4292927712'
class Constants:
    FramePadding: typing.ClassVar[int] = 8
TREE_UI_STYLES: dict = {'TreeView': {'background_selected_color': 'shade:4280821800'}, 'TreeView.Frame': {'padding': 8}, 'TreeView.Item.Name': {'color': 'shade:4286743170;light=4292927712'}, 'TreeView.Item.Name:selected': {'color': 'shade:4293105444;light=4291137818'}, 'TreeView.Item.Count:selected': {'color': 'shade:4286743170;light=4292927712'}}
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
