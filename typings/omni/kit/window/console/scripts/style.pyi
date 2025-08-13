from __future__ import annotations
import carb as carb
from omni import ui
import omni.ui.color_utils
__all__: list[str] = ['CL_LOG_DEFAULT', 'CL_LOG_ERROR', 'CL_LOG_FATAL', 'CL_LOG_INFO', 'CL_LOG_VERBOSE', 'CL_LOG_WARNING', 'CONSOLE_WINDOW_STYLE', 'LOG_LEVEL_ICONS', 'carb', 'cl', 'ui']
CL_LOG_DEFAULT: int = 4286545791
CL_LOG_ERROR: int = 4289376758
CL_LOG_FATAL: int = 4289376758
CL_LOG_INFO: int = 4293638777
CL_LOG_VERBOSE: int = 4290427578
CL_LOG_WARNING: int = 4283091935
CONSOLE_WINDOW_STYLE: dict  # value = {'Toolbar.Frame': {'padding': 0, 'margin_width': 0}, 'Toolbar.Button': {'stack_direction': <Direction.LEFT_TO_RIGHT: 0>, 'background_color': 0, 'padding': 2.5}, 'Toolbar.Button:hovered': {'background_color': 4281808695}, 'Toolbar.Button:checked': {'background_color': 4281808695}, 'Toolbar.Button.Image': {'color': 4291611852}, 'Toolbar.Button.Image::clear': {'image_url': '${glyphs}/Clear_Log.svg'}, 'Toolbar.Button.Image::open_log': {'image_url': '${glyphs}/Open_Log.svg'}, 'Toolbar.Button.Image::open_folder': {'image_url': '${glyphs}/Open_Folder.svg'}, 'Toolbar.Button.Image::verbose': {'image_url': '${glyphs}/asterisk.svg', 'color': 4286545791}, 'Toolbar.Button.Image::verbose:checked': {'color': 4290361785}, 'Toolbar.Button.Image::info': {'image_url': '${glyphs}/Info_Log.svg', 'color': 4286545791}, 'Toolbar.Button.Image::info:checked': {'color': 4293638777}, 'Toolbar.Button.Label::warning': {'color': 4286545791}, 'Toolbar.Button.Label::warning:checked': {'color': 4283091935}, 'Toolbar.Button.Image::warning': {'image_url': '${glyphs}/Warning_Log.svg', 'color': 4286545791}, 'Toolbar.Button.Image::warning:checked': {'color': 4283091935}, 'Toolbar.Button.Label::error': {'color': 4289376758}, 'Toolbar.Button.Image::error': {'image_url': '${glyphs}/Error_Log.svg', 'color': 4286545791}, 'Toolbar.Button.Image::error:checked': {'color': 4286417656}, 'Toolbar.SearchField': {'background_color': 'shade:4280557855'}, 'Toolbar.SearchField.hint': {'margin_width': 8, 'color': 'shade:4285427310'}, 'LogView': {'background_color': 'shade:4280557855', 'background_selected_color': 4281545523}, 'LogView:selected': {'background_color': 4281545523}, 'LogView.Item.Text': {'margin_height': 1}, 'LogView.Item.Text::verbose': {'color': 4293638777}, 'LogView.Item.Text::info': {'color': 4293638777}, 'LogView.Item.Text::warning': {'color': 4283091935}, 'LogView.Item.Text::error': {'color': 4289376758}, 'LogView.Item.Text::fatal': {'color': 4289376758}, 'CommandField.Hint': {'color': 'shade:4283058762'}}
LOG_LEVEL_ICONS: dict = {-2: '${glyphs}/asterisk.svg', -1: '${glyphs}/Info_Log.svg', 0: '${glyphs}/Warning_Log.svg', 1: '${glyphs}/Error_Log.svg', 2: '${glyphs}/Error_Log.svg'}
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
