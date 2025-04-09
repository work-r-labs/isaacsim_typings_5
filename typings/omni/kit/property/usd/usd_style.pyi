from __future__ import annotations
import typing
__all__: list = list()
class Styles:
    BACK_DROP: typing.ClassVar[dict] = {'Rectangle::backdrop-live': {'background_color': 3996341555}}
    BROWSE_BTN: typing.ClassVar[dict] = {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/small_folder.png', 'padding': 1, 'margin': 0, 'Button:Image:disabled': {'color': 4281545523}, 'Button.Image::browse': {'color': 4289374890}, 'Button.Image::browse:hovered': {'color': 4294967295}, 'Button:hovered': {'background_color': 0}}
    DEFAULT_BTN: typing.ClassVar[dict] = {'Image': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/Default value.svg'}, 'Image::changed': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/Changed value.svg'}}
    FIND_BTN: typing.ClassVar[dict] = {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/find.png', 'padding': 1, 'margin': 0, 'Button.Image::find:disabled': {'color': 4281545523}, 'Button.Image::find': {'color': 4287137928}, 'Button.Image::find:hovered': {'color': 4294967295}, 'Button:hovered': {'background_color': 0}}
    FIND_BTN_MISSING: typing.ClassVar[dict] = {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/find.png', 'padding': 1, 'margin': 0, 'Button.Image::find:disabled': {'color': 4284900966}, 'Button.Image::find': {'color': 4284900966}}
    LIVE_GREEN: typing.ClassVar[dict] = {'color': 4278237302, 'Tooltip': {'background_color': 3995214370, 'color': 858993459}}
    LIVE_GREEN_DARKER: typing.ClassVar[dict] = {'color': 4278237558, 'Tooltip': {'background_color': 3995214370, 'color': 858993459}}
    LIVE_SEL: typing.ClassVar[dict] = {'color': 4278237558, 'Tooltip': {'background_color': 3995214370, 'color': 858993459}}
    LIVE_STATE_PAYREF: typing.ClassVar[dict] = {'Image::lightning': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/lightning.svg', 'color': 4289374890}, 'Image::lightning:hovered': {'color': 4293848814}, 'Image::lightning-live': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/lightning.svg', 'color': 4278237291}, 'Image::lightning-live:hovered': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/lightning.svg', 'color': 4278253678}, 'Label::label-live': {'color': 4278237291}}
    LIVE_TOOL_TIP: typing.ClassVar[dict] = {'background_color': 3995214370, 'color': 858993459}
    REFERENCE_ERROR: typing.ClassVar[int] = 4285494015
    RELOAD_ORANGE: typing.ClassVar[dict] = {'color': 4278230507, 'Tooltip': {'background_color': 3995214370, 'color': 858993459}}
    RELOAD_SEL: typing.ClassVar[dict] = {'color': 4278233855, 'Tooltip': {'background_color': 3995214370, 'color': 858993459}}
    REMOVE_BTN: typing.ClassVar[dict] = {'image_url': '/home/chris/isaacsim/extscache/omni.kit.property.usd-4.2.16+d02c707b/data/icons/remove.svg', 'margin': 0, 'padding': 0, 'Button:hovered': {'color': 4008636142}, 'Button:disabled': {'color': 300871406}, 'Rectangle': {'background_color': 3996341555}}
    SESSIONS_MENU: typing.ClassVar[dict] = {'Button:hovered': {'color': 0}}
    @staticmethod
    def on_startup():
        ...
