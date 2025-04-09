from __future__ import annotations
import omni.ui.color_utils
__all__ = ['COLOR_FOCAL', 'COLOR_FREE', 'COLOR_SCREEN', 'COLOR_X', 'COLOR_Y', 'COLOR_Z', 'abgr_to_color', 'cl', 'get_default_style', 'get_default_toolbar_style', 'update_style']
def abgr_to_color(abgr: int) -> <omni.ui.color_utils.ColorShade object>:
    """
    Converts an ABGR integer value to a color object.
    
        The function takes an integer that represents a color in ABGR format (alpha, blue, green, red)
        and converts it into a color object with RGBA channels normalized to the range [0, 1].
    
        Args:
            abgr (int): The color value in ABGR format to be converted.
    
        Returns:
            omni.ui.color: The color object with RGBA channels.
    """
def get_default_style():
    """
    Returns the default style settings for the manipulator's visual elements.
    
        These settings include predefined colors for the axes (X, Y, Z), planes, and other components used in
        the manipulator in the context of translation, rotation, and scaling operations. It provides a consistent
        look and feel for the manipulator's visual elements and can be overridden by custom styles.
    
        Returns:
            Dict[str, Dict[str, Union[int, bool]]]: A dictionary with style settings for each manipulator component,
            with keys representing the component names and values containing style information such as color and visibility.
        
    """
def get_default_toolbar_style():
    """
    
        Returns the default style settings for the manipulator's toolbar.
    
        The function provides a set of default style properties for the manipulator's toolbar elements. Each element
        such as collapsable frames, lines, and rectangles has a set of attributes including background color,
        border color, padding, and margins. These default styles can be used to maintain a consistent look and feel
        across the toolbar or be overridden by custom styles.
    
        Returns:
            Dict[str, Dict[str, int]]: A dictionary containing styles for the toolbar elements. Each key represents
            an element type, and the corresponding value is another dictionary with style attributes as keys and
            their values as integers representing colors, widths, and sizes.
        
    """
def update_style(to_style: typing.Dict, from_style: typing.Dict):
    """
    Updates the style dictionary with values from another dictionary.
    
        This function takes two dictionaries: `to_style`, the target dictionary to be updated, and `from_style`, the source dictionary containing new values. It recursively merges the `from_style` into `to_style`, ensuring that nested dictionaries are properly updated. This allows for deep customization of style properties in a structured manner.
    
        Args:
            to_style (Dict): The target style dictionary to update.
            from_style (Dict): The source style dictionary from which to update values.
    
        Returns:
            Dict: The updated target style dictionary with merged values from the source dictionary.
    """
COLOR_FOCAL: int = 3872181452
COLOR_FREE: int = 1077952576
COLOR_SCREEN: int = 2331965070
COLOR_X: int = 4284506282
COLOR_Y: int = 4285965169
COLOR_Z: int = 4288707919
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
