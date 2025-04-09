from __future__ import annotations
import numpy
import numpy as np
import omni as omni
from omni.graph import core as og
from omni.usd.commands.usd_commands import DeletePrimsCommand
__all__ = ['DeletePrimsCommand', 'ScreenPrinter', 'np', 'og', 'omni']
class ScreenPrinter:
    """
    Print text to the viewport using the omni.graph.visualization.nodes.DrawScreenSpaceText node.
    
        Args:
            screen_pos_x (float): X position of the text on the screen, given as a percent of screen width with 0 refering to the left hand side. (Default: 78)
            screen_pos_y (float): Y position of the text on the screen, given as a percent of screen width with 0 refering to the top. (Default 95)
            text_size (float): Size of text (Default 14.0)
            max_width (float): Maximum width of text before wrapping around and continuing on a new line.  A value of 0 means there is no wraparound (Default 0)
            color (np.array): Color of text, given in a (4x1) np.array of the form [r,g,b,luminocity].  All four values have a minimum of 0.0 and a maximum of 2.0. (Default [1,1,1,1])
        
    """
    def __init__(self, screen_pos_x: float = 78, screen_pos_y: float = 95, text_size: float = 14.0, max_width: int = 0, color: numpy.array = ...) -> None:
        ...
    def clear_text(self) -> None:
        """
        Clear the text from the screen.
        """
    def exit(self) -> None:
        """
        Delete OmniGraph used by this ScreenPrinter.  After calling exit(), all subsequent function calls will fail.
        """
    def set_text(self, text: str) -> None:
        """
        Set the text on the screen
        
                Args:
                    text (str): Text to appear on the screen.
                
        """
    def set_text_color(self, color4f: numpy.array) -> None:
        """
        Set the color of the text
        
                Args:
                    color4f (np.array): Color of text, given in a (4x1) np.array of the form [r,g,b,luminocity].  All four values have a minimum of 0.0 and a maximum of 2.0.
                
        """
    def set_text_max_width(self, max_width: int) -> None:
        """
        Set the maximum text width (in pixels) before wrap-around
        
                Args:
                    max_width (int): Maximum width of text before wrapping around and continuing on a new line.  A value of 0 means there is no wrap-around
                
        """
    def set_text_position(self, screen_pos_x: float, screen_pos_y: float) -> None:
        """
        Set the x,y position of the text on the screen
        
                Args:
                    screen_pos_x (float): X position of the text on the screen, given as a percent of screen width with 0 refering to the left hand side.
                    screen_pos_y (float): Y position of the text on the screen, given as a percent of screen width with 0 refering to the top.
                
        """
    def set_text_size(self, size: float) -> None:
        """
        Set the size of the text.
        
                Args:
                    size (float): Pixel height of a line of text
                
        """
