from __future__ import annotations
from omni import ui
import typing
__all__: list = ['Styles']
class Styles:
    ICON_DARK = None
    ITEM_BG_SEL: typing.ClassVar[int] = 1720223607
    ITEM_DARK: typing.ClassVar[int] = 1998790943
    ITEM_GRAY: typing.ClassVar[int] = 4287268727
    ITEM_HOVER: typing.ClassVar[int] = 4290493098
    ITEM_SEL: typing.ClassVar[int] = 4292730060
    STAGE_WIDGET: typing.ClassVar[dict]  # value = {'Button.Image::filter': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.stage-2.11.6+d02c707b/icons/filter.svg', 'color': 4287268727}, 'Button.Image::options': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.widget.stage-2.11.6+d02c707b/icons/options.svg', 'color': 4287268727}, 'Button::filter': {'background_color': 0, 'margin': 0}, 'Button::options': {'background_color': 0, 'margin': 0}, 'Label::search': {'color': 4286611584, 'margin_width': 4}, 'TreeView.ScrollingFrame': {'background_color': 4280492319}, 'TreeView.Image:disabled': {'color': 1627389951}, 'TreeView.Item': {'color': 4287268727}, 'TreeView.Item:disabled': {'color': 1619691383}, 'TreeView.Item:hovered': {'color': 4290493098}, 'TreeView.Item:selected': {'color': 4292730060}, 'TreeView:selected': {'background_color': 1720223607}, 'TreeView': {'background_color': 4280492319, 'background_selected_color': 1716473155, 'secondary_color': 4282399547, 'border_width': 1.5}, 'TreeView:drop': {'background_color': 'shade:1006618420', 'background_selected_color': 'shade:1006618420', 'border_color': 'shade:4289365803'}, 'TreeView.Header': {'background_color': 4281611314, 'color': 4291611852, 'font_size': 12}, 'TreeView.Header::drop_down_background': {'background_color': 3766517888}, 'TreeView.Header::drop_down_button': {'background_color': 'white'}, 'TreeView.Header::drop_down_hovered_area': {'background_color': 'transparent'}, 'TreeView.Header::hovering': {'background_color': 0, 'border_radius': 1.5}, 'TreeView.Header::hovering:hovered': {'background_color': 'shade:1006618420', 'border_width': 1.5, 'border_color': 'shade:4289365803'}}
    @staticmethod
    def on_startup():
        ...
