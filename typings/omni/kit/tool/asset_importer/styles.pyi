from __future__ import annotations
import omni as omni
__all__ = ['OPTIONS_STYLE', 'PATH_EXTENSION', 'TT_EXPORT_BTN', 'TT_EXPORT_SF', 'omni']
OPTIONS_STYLE: dict = {'Button.Image::folder': {'image_url': 'resources/glyphs/folder.svg', 'color': 4288585374, 'image_width': 20, 'image_height': 20, 'background_color': 0}, 'Button.Image::folder:hovered': {'image_url': 'resources/glyphs/folder_open.svg'}, 'Button::folder': {'background_color': 0, 'margin': 0}, 'Field': {'background_color': 4280492319}, 'RadioButton': {'background_color': 0}, 'RadioButton:checked': {'background_color': 0}, 'RadioButton:hovered': {'background_color': 0}, 'RadioButton:pressed': {'background_color': 0}, 'RadioButton.Image': {'image_url': '${omni.kit.tool.asset_importer}/data/icons/radio_off.svg', 'color': 4288585374}, 'RadioButton.Image:checked': {'image_url': '${omni.kit.tool.asset_importer}/data/icons/radio_on.svg'}, 'RadioButton.Image:hovered': {'image_url': '${omni.kit.tool.asset_importer}/data/icons/radio_on.svg'}}
PATH_EXTENSION: str = '${omni.kit.tool.asset_importer}'
TT_EXPORT_BTN: str = 'Choose folder.'
TT_EXPORT_SF: str = 'Left this empty will export USD to the folder that assets are under.'
