"""
This module provides the MarkdownText class to render markdown-formatted text within a UI context using omni.ui.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import contextlib as contextlib
from omni.kit.window.extensions.common import build_doc_urls
from omni.kit.window.extensions.common import get_icons_path
from omni.kit.window.extensions.styles import get_style
from omni.kit.window.extensions.utils import open_url
from omni import ui
import os as os
import re as re
__all__: list = ['MarkdownText']
class MarkdownText:
    """
    A class for rendering markdown text within a UI context.
    
        This class takes a markdown-formatted string and displays it using
        the appropriate styles for headings and regular text lines.
    
        Args:
            content (str): Markdown-formatted string to be rendered.
    """
    def __init__(self, content, ext_info, ext_item):
        """
        Initializes a new instance of the MarkdownText class, which parses markdown content and creates a styled UI representation.
        """
    def _add_codeblock_data(self, line):
        ...
    def _add_table_data(self, line):
        ...
    def _build_blockquote(self, style_name, line):
        ...
    def _build_bullet(self, style_name, indent, code, line):
        ...
    def _build_codeblock(self, style_name, block_type):
        ...
    def _build_hyperlink(self, style_name, line):
        ...
    def _build_imagelink(self, style_name, line):
        ...
    def _build_info_text(self):
        ...
    def _build_label(self, style_name, line, width = None, height = None):
        ...
    def _build_table(self, style_name):
        ...
    def _consume_heading(self, line, code_block, ext_item):
        ...
    def _is_bullet(self, line):
        ...
    def _show_info_text(self, ext_item):
        ...
CODEBLOCK_ID: str = '$$_C_O_D_E_$$'
STAR_ID: str = '$$_S_T_A_R_$$'
