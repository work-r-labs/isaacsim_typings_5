"""
This module provides a visual representation of extension dependencies within the Omniverse Kit, including classes for dependency models, views, and widgets.
"""
from __future__ import annotations
import carb as carb
from collections import defaultdict
import enum
from enum import Enum
import omni as omni
from omni.kit.window.extensions.utils import ext_id_to_fullname
from omni import ui
import typing
__all__: list = list()
class DependenciesModel:
    """
    A class representing a dependency model of extension dependencies.
    
        This class constructs a dependency model that represents the dependencies between extensions. It can filter out unreachable nodes based on a specified root extension ID and provides functionalities to copy the dependency as a Graphviz dot representation.
    
        Args:
        ext_id (str): Optional. The root extension ID to filter the dependency for a specific extension.
    """
    class ExpansionState(enum.Enum):
        """
        Enum for node expansion states.
        """
        CLOSED: typing.ClassVar[DependenciesModel.ExpansionState]  # value = <ExpansionState.CLOSED: 2>
        MINIMIZED: typing.ClassVar[DependenciesModel.ExpansionState]  # value = <ExpansionState.MINIMIZED: 1>
        OPEN: typing.ClassVar[DependenciesModel.ExpansionState]  # value = <ExpansionState.OPEN: 0>
    def __init__(self, ext_id: str = None):
        """
        Initialize the dependency model, potentially with a filtered dependency based on an extension ID.
        """
    def _filter_out_unreachable_nodes(self, ext_id):
        ...
    @property
    def expansion_state(self, item = None):
        """
        Gets the expansion state for a given item.
        
                Args:
                    item (str): The identifier of the item whose expansion state to retrieve.
        
                Returns:
                    ExpansionState: The expansion state of the item.
        """
    @property
    def inputs(self, item):
        """
        Gets the input ports dependencies for a given item.
        
                Args:
                    item (str): The identifier of the item whose input ports to retrieve.
        
                Returns:
                    list: A list of input port dependencies for the item.
        """
    @property
    def item(self, item = None):
        """
        Gets the dependency item for a given identifier.
        
                Args:
                    item (str): The identifier of the dependency item to retrieve.
        
                Returns:
                    ExtDependencyItem: The dependency item associated with the identifier.
        """
    @property
    def name(self, item = None):
        """
        Gets the name of the node for a given item.
        
                Args:
                    item (str): The identifier of the item whose name to retrieve.
        
                Returns:
                    str: The name of the item, if it exists.
        """
    @property
    def nodes(self, item = None):
        """
        Gets the node identifiers for a given item.
        
                Args:
                    item (str): The identifier of the item whose nodes to retrieve.
        
                Returns:
                    set: A set of node identifiers related to the item.
        """
    @property
    def outputs(self, item):
        """
        Gets the output ports for a given item.
        
                Args:
                    item (str): The identifier of the item whose output ports to retrieve.
        
                Returns:
                    list: An empty list, since items do not have output ports.
        """
    @property
    def ports(self, item = None):
        """
        Gets the ports for a given item.
        
                Args:
                    item (str): The identifier of the item whose ports to retrieve.
        
                Returns:
                    list: A list containing the input and output ports of the item.
        """
class ExtDependencyItem:
    """
    A dependency item representing an extension in the Extensions dependency.
    
        This class encapsulates information about an extension such as its dependencies, plugins, libraries, and Python modules.
    
        Args:
            manager (:obj:`omni.kit.app.ExtensionManager`): The manager handling extension-related information.
            ext_id (str): The unique identifier for the extension.
    """
    def __init__(self, manager, ext_id):
        """
        Initializes an ExtDependencyItem instance, gathering extension dependencies and information such as plugins, libraries, and modules.
        """
    def __lt__(self, other):
        ...
class ExtsDependenciesWindow:
    """
    A window that visualizes the list of extensions and their interdependencies.
    
        The window includes functionality to refresh its contents based on changes in the extension manager, select specific extensions to focus on, and toggle its visibility.
        
    """
    def __init__(self):
        """
        Initializes the ExtsDependenciesWindow with necessary UI components and subscriptions.
        """
    def _build(self):
        ...
    def _refresh(self):
        ...
    def destroy(self):
        """
        Cleans up the UI components and subscriptions associated with the ExtsDependenciesWindow.
        """
    def select_ext(self, ext_id):
        """
        Selects an extension by its identifier to be displayed or focused on in the dependency.
        
                Args:
                    ext_id (str): The identifier of the extension to select.
        """
    def set_visible(self, visible: bool):
        """
        Sets the visibility of the Extensions Dependencies Window.
        
                Args:
                    visible (bool): A flag to toggle the visibility of the window.
        """
class ExtsDependencyWidget:
    """
    Extensions dependency window
    
        Args:
            ext_id (str): The identifier for the extension whose dependencies are to be visualized.
    """
    def __init__(self, ext_id):
        """
        Initializes the extensions dependency widget with the given extension id.
        """
    def destroy(self):
        """
        Cleans up and releases all the resources used by the extensions dependency widget.
        """
class ExtsListView:
    """
    A view widget to list the dependencies and reverse dependencies of an extension.
    
        This view provides an interface to display direct and indirect dependencies and reverse dependencies of a particular extension within the Omniverse Kit application. The list is presented in a scrolling frame with labels for each category of dependencies.
    
        Args:
            model (:obj:`DependenciesModel`): The dependency model containing node data for dependencies.
            ext_id (str): The identifier of the extension to display dependencies for.
    """
    def __init__(self, model, ext_id):
        """
        Initializes the ExtsListView which provides a UI representation of extension dependencies.
        """
    def _get_reverse_dependencies(self, manager, exts) -> typing.Tuple[typing.List, typing.List]:
        ...
BACKGROUND_COLOR: int = 4281610282
BORDER_DEFAULT: int = 4280492835
BORDER_THICKNESS: float = 3.0
CONNECTION: int = 4286628480
CONNECTION_CURVE: int = 60
HEADER_HEIGHT: float = 25.0
LIBRARIES_COLOR: int = 2856643559
MARGIN_BOTTOM: float = 25.0
MARGIN_TOP: float = 20.0
MARGIN_WIDTH: float = 7.5
MIN_WIDTH: float = 180.0
MODULES_COLOR: int = 4289389508
NODE_BACKGROUND: int = 4279505940
PLUGINS_COLOR: int = 4294960068
