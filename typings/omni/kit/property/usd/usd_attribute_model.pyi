from __future__ import annotations
import copy as copy
import omni as omni
from omni.kit.property.adapter.core.scripts.core_adapter import StageAdapter
from omni.kit.property.usd.placeholder_attribute import PlaceholderAttribute
from omni.kit.property.usd.usd_model_base import UsdBase
from omni.kit.property.usd.usd_model_items import AllowedTokenItem
from omni.kit.property.usd.usd_model_items import OptionItem
from omni.kit.property.usd.usd_model_items import SdfAssetPathItem
from omni.kit.property.usd.usd_model_items import UsdFloatItem
from omni.kit.property.usd.usd_model_items import UsdMatrixItem
from omni.kit.property.usd.usd_model_items import UsdQuatItem
from omni.kit.property.usd.usd_model_items import UsdVectorItem
from omni import ui
from pxr import Ar
from pxr import Gf
import pxr.Sdf
from pxr import Sdf
import pxr.Tf
from pxr import Tf
from pxr import Usd
import pxr.Usd
from pxr import UsdShade
import typing
from urllib.parse import unquote
import weakref as weakref
__all__: list = ['IntModel', 'FloatModel', 'UsdAttributeModel', 'GfVecAttributeSingleChannelModel', 'TfTokenAttributeModel', 'MdlEnumAttributeModel', 'GfVecAttributeModel', 'SdfAssetPathAttributeModel', 'SdfAssetPathArrayAttributeSingleEntryModel', 'SdfAssetPathArrayAttributeItemModel', 'GfQuatAttributeModel', 'GfQuatEulerAttributeModel', 'GfMatrixAttributeModel', 'UsdAttributeInvertedModel', 'SdfTimeCodeModel']
class BoolArrayAttributeSingleChannelModel(GfVecAttributeSingleChannelModel):
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], channel_index: int, self_refresh: bool, metadata: dict, change_on_edit_end = True, **kwargs):
        ...
    def set_value(self, value, comp: int = -1):
        ...
class BoolModel(omni.ui._ui.SimpleBoolModel):
    """
    A model providing a simple interface for a boolean value.
    
        This model is a thin wrapper around a float, allowing for easy integration with UI components that require a model to represent and manipulate floating-point numbers. It is particularly useful for scenarios where a float value needs to be observed or edited within a user interface.
    
        Args:
            parent: A weak reference to the parent of this model, allowing this model to notify the parent about changes to the value.
        
    """
    def __init__(self, parent):
        ...
    def begin_edit(self):
        """
        Begins editing the value.
        """
    def end_edit(self):
        """
        Ends editing the value.
        """
class FloatModel(omni.ui._ui.SimpleFloatModel):
    """
    A model providing a simple interface for a floating-point value.
    
        This model is a thin wrapper around a float, allowing for easy integration with UI components that require a model to represent and manipulate floating-point numbers. It is particularly useful for scenarios where a float value needs to be observed or edited within a user interface.
    
        Args:
            parent: A weak reference to the parent of this model, allowing this model to notify the parent about changes to the value.
        
    """
    def __init__(self, parent):
        """
        Initializes a new instance of the FloatModel.
        """
    def begin_edit(self):
        """
        Begins editing the value.
        """
    def end_edit(self):
        """
        Ends editing the value.
        """
class GfMatrixAttributeModel(MatrixBaseAttributeModel):
    """
    A model for representing and manipulating GfMatrix attributes in USD.
    
        This model supports various matrix sizes as defined by the composition count and type. It provides functionality to edit individual matrix components and handles their synchronization with the USD attributes.
    
        Args:
            stage (:obj:`Usd.Stage`): The stage where the USD attributes are defined.
            attribute_paths (List[:obj:`Sdf.Path`]): A list of USD attribute paths to be managed by this model.
            comp_count (int): The number of components in each row or column of the matrix.
            tf_type (:obj:`Tf.Type`): The type of the matrix, typically representing the data precision (e.g., GfMatrix4f for a 4x4 float matrix).
            self_refresh (bool): Whether the model should automatically refresh its data when the USD stage changes.
            metadata (dict): A dictionary containing metadata for the matrix attributes.
    """
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], comp_count: int, tf_type: pxr.Tf.Type, self_refresh: bool, metadata: dict):
        """
        Constructor for GfMatrixAttributeModel.
        
                Initializes a new instance of GfMatrixAttributeModel.
        """
    def _construct_matrix_from_item(self):
        ...
    def _on_value_changed(self, item):
        """
        Called when the submodel is chaged
        """
    def _update_value(self, force = False):
        ...
class GfQuatAttributeModel(omni.ui._ui.AbstractItemModel, omni.kit.property.usd.usd_model_base.UsdBase):
    """
    A model for managing quaternion attributes in a USD stage.
    
        This model provides an interface to interact with quaternion attributes associated with USD prim paths. It supports updating the attribute values and responding to changes in the stage.
    
        Args:
            stage (:obj:`Usd.Stage`): The USD stage to associate with the model.
            attribute_paths (List[:obj:`Sdf.Path`]): A list of prim paths whose attributes this model will manage.
            tf_type (:obj:`Tf.Type`): The type of transformation (e.g., rotation, scale, translation) that the quaternion represents.
            self_refresh (bool): Whether the model should automatically refresh its data when changes occur in the stage.
            metadata (dict): Additional metadata that may be needed for managing the attributes.
    """
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], tf_type: pxr.Tf.Type, self_refresh: bool, metadata: dict):
        """
        Initializes the GfQuatAttributeModel.
        """
    def _construct_quat_from_item(self):
        ...
    def _on_dirty(self):
        ...
    def _on_value_changed(self, item):
        """
        Called when the submodel is chaged
        """
    def _update_value(self, force = False):
        ...
    def begin_edit(self, item = None):
        """
        Begins the editing process for a given item.
        
                Args:
                    item: The item to start editing.
        """
    def clean(self):
        """
        Cleans up the model, preparing it for deletion.
        """
    def end_edit(self, item = None):
        """
        Ends the editing process for a given item.
        
                Args:
                    item: The item to finish editing.
        """
    def get_item_children(self, item):
        """
        Retrieves children of a given item.
        
                Args:
                    item: The item to get children for.
        """
    def get_item_value_model(self, item, column_id):
        """
        Gets the value model for a specified item and column.
        
                Args:
                    item: The item to get the value model for.
                    column_id: The id of the column.
        """
class GfQuatEulerAttributeModel(omni.ui._ui.AbstractItemModel, omni.kit.property.usd.usd_model_base.UsdBase):
    """
    A class for managing the conversion between quaternion and Euler rotation attributes in USD stages.
    
        This model facilitates the representation and editing of quaternion-based rotation attributes as Euler angles, providing an intuitive interface for animators and artists. It supports updating and retrieving the rotation values in both formats, ensuring seamless integration with USD's quaternion attributes.
    
        Args:
            stage (:obj:`Usd.Stage`): The USD stage where the attribute resides.
            attribute_paths (List[:obj:`Sdf.Path`]): A list of paths to the quaternion attributes in the USD stage.
            tf_type (:obj:`Tf.Type`): The type of the transformation, indicating whether it's a rotation, scale, or translation.
            self_refresh (bool): Indicates whether the model should automatically refresh its value when the USD stage is changed.
            metadata (dict): Additional metadata associated with the quaternion attribute.
    """
    axes: typing.ClassVar[list]  # value = [Gf.Vec3d(1.0, 0.0, 0.0), Gf.Vec3d(0.0, 1.0, 0.0), Gf.Vec3d(0.0, 0.0, 1.0)]
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], tf_type: pxr.Tf.Type, self_refresh: bool, metadata: dict):
        """
        Constructor for GfQuatEulerAttributeModel.
        """
    def _compare_value_by_comp(self, val1, val2, comp: int):
        ...
    def _compose(self, eulers):
        ...
    def _decompose(self, value):
        ...
    def _get_comp_num(self):
        ...
    def _get_value_by_comp(self, value, comp: int):
        ...
    def _on_dirty(self):
        ...
    def _on_value_changed(self, item):
        ...
    def _update_value(self, force = False):
        ...
    def _update_value_by_comp(self, value, comp: int):
        ...
    def begin_edit(self, item = None):
        """
        Begins an edit operation on the model.
        
                Args:
                    item (Optional[:obj:`UsdUIItem`]): The item that is beginning an edit.
        """
    def clean(self):
        """
        Cleans up the model.
        """
    def end_edit(self, item = None):
        """
        Ends an edit operation on the model.
        
                Args:
                    item (Optional[:obj:`UsdUIItem`]): The item that has finished editing.
        """
    def get_item_children(self, item):
        """
        Gets the child items of the given item.
        
                Args:
                    item (Optional[:obj:`UsdUIItem`]): The parent item to retrieve children for.
        """
    def get_item_value_model(self, item, column_id):
        """
        Retrieves the value model for a given item and column.
        
                Args:
                    item (Optional[:obj:`UsdUIItem`]): The item to retrieve the value model for.
                    column_id (int): The column id for which to retrieve the model.
        """
    def update_to_submodels(self):
        """
        Updates submodels with the current quaternion value.
        """
class GfVecAttributeModel(omni.ui._ui.AbstractItemModel, omni.kit.property.usd.usd_model_base.UsdBase):
    """
    A model for representing and manipulating GfVec typed attributes in USD.
    
        This model handles vector attributes with a specified number of components and a given type from the Gf library. It provides functionality to interact with the attribute's value, including getting and setting the vector components.
    
        Args:
            stage (:obj:`Usd.Stage`): The USD stage containing the attribute.
            attribute_paths (List[:obj:`Sdf.Path`]): A list of attribute paths to be managed by the model.
            comp_count (int): The number of components in the vector.
            tf_type (:obj:`Tf.Type`): The type of the vector from the Gf library.
            self_refresh (bool): Whether the model should refresh itself automatically.
            metadata (dict): Additional metadata associated with the attribute.
    
        Keyword Args:
            change_on_edit_end (bool): Whether to apply changes only when editing is finished.
            treat_array_entry_as_comp (bool): Treat array entries as components of the vector.
    """
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], comp_count: int, tf_type: pxr.Tf.Type, self_refresh: bool, metadata: dict, **kwargs):
        """
        Initializer for GfVecAttributeModel.
        """
    def _construct_vector_from_item(self):
        ...
    def _on_dirty(self):
        ...
    def _on_value_changed(self, item):
        """
        Called when the submodel is changed
        """
    def _update_value(self, force = False):
        ...
    def begin_edit(self, item = None):
        """
        Begins an edit operation on the given item.
        
                Args:
                    item: The item to begin editing.
        """
    def clean(self):
        """
        Cleans up the model removing any stored data.
        """
    def construct_vector_from_item(self):
        ...
    def end_edit(self, item = None):
        """
        Ends an edit operation on the given item.
        
                Args:
                    item: The item to end editing.
        """
    def get_item_children(self, item):
        """
        Returns the child items of the given item.
        
                Args:
                    item: The item whose children to retrieve.
        """
    def get_item_value_model(self, item, column_id):
        """
        Retrieves the value model for the given item and column.
        
                Args:
                    item: The item for which to retrieve the model.
                    column_id: The ID of the column.
        """
    def set_value(self, value, comp: int = -1) -> bool:
        ...
class GfVecAttributeSingleChannelModel(UsdAttributeModel):
    """
    A model for handling single channel vector attributes in USD.
    
        This model is a specialized version of `UsdAttributeModel` that focuses on a single channel of a vector attribute.
        It is designed to be used with vector types such as GfVec3f where only one component of the vector is relevant at a time.
    
        Args:
            stage (:obj:`Usd.Stage`): The USD stage containing the attributes to be managed.
            attribute_paths (List[:obj:`Sdf.Path`]): A list of USD attribute paths for which the model is responsible.
            channel_index (int): The index of the channel in the vector to be managed by this model.
            self_refresh (bool): Whether the model should update itself automatically when changes occur.
            metadata (dict): A dictionary containing metadata information for the attribute.
            change_on_edit_end (bool): Whether the value of the attribute should only change when the user finishes editing.
    
        Keyword Args:
            treat_array_entry_as_comp (bool): Treats the array entry as a separate component if set to True.
        
    """
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], channel_index: int, self_refresh: bool, metadata: dict, change_on_edit_end = True, **kwargs):
        """
        Initializer for GfVecAttributeSingleChannelModel.
        """
    def get_value_as_bool(self) -> bool:
        """
        Retrieves the value as a boolean.
        
                Returns:
                    bool: The value of the attribute as a boolean.
        """
    def get_value_as_float(self) -> float:
        """
        Retrieves the value as a float.
        
                Returns:
                    float: The value of the attribute as a float.
        """
    def get_value_as_int(self) -> int:
        """
        Retrieves the value as an integer.
        
                Returns:
                    int: The value of the attribute as an integer.
        """
    def get_value_as_string(self, elide_big_array = True) -> str:
        """
        Retrieves the value as a string.
        
                Args:
                    elide_big_array (bool): If True, elide arrays that are too large.
        
                Returns:
                    str: The value of the attribute as a string.
        """
    def is_different_from_default(self):
        """
        Checks if the current value is different from the default value.
        
                Returns:
                    bool: True if different, otherwise False.
        """
    def is_value_array(self):
        """
        Indicates if the value is an array.
        
                Returns:
                    bool: True if the value is an array, otherwise False.
        """
    def set_value(self, value, comp: int = -1):
        """
        Sets the value of the attribute.
        
                Args:
                    value: The new value to set.
                    comp (int): The component index to set, -1 if not component-specific.
        """
class IntModel(omni.ui._ui.SimpleIntModel):
    """
    A model providing a simple interface for a integer value.
    
        This model is a thin wrapper around a float, allowing for easy integration with UI components that require a model to represent and manipulate floating-point numbers. It is particularly useful for scenarios where a float value needs to be observed or edited within a user interface.
    
        Args:
            parent: A weak reference to the parent of this model, allowing this model to notify the parent about changes to the value.
        
    """
    def __init__(self, parent):
        """
        Initializes a new instance of the IntModel.
        """
    def begin_edit(self):
        """
        Begins editing the value.
        """
    def end_edit(self):
        """
        Ends editing the value.
        """
class MatrixBaseAttributeModel(omni.ui._ui.AbstractItemModel, omni.kit.property.usd.usd_model_base.UsdBase):
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], num_items: int, self_refresh: bool, metadata: dict):
        """
        A specialized model for handling Matrices in USD attributes.
        
                This model extends the capabilities of the UsdAttributeModel by providing additional functionality to manage Matrices values. It is particularly useful for working with attributes that represent Matrix data in USD.
        
                While similar in structure to UsdAttributeModel, this model overrides the method to save the previous real values as Matrix, ensuring proper initialization and handling of Matrix data types.
        
                
        """
    def _on_dirty(self):
        ...
    def _on_value_changed(self, item):
        """
        
                Called when the submodel is changed
                Implement in derived.
                
        """
    def _update_value(self, force = False):
        """
        
                Update child model values
                Implement in derived.
                
        """
    def begin_edit(self, item = None):
        """
        
                Reimplemented from the base class.
                Called when the user starts editing.
                
        """
    def clean(self):
        ...
    def end_edit(self, item = None):
        """
        
                Reimplemented from the base class.
                Called when the user finishes editing.
                
        """
    def get_item_children(self, item):
        """
        Reimplemented from the base class.
        """
    def get_item_value_model(self, item, column_id):
        """
        Reimplemented from the base class.
        """
class MdlEnumAttributeModel(omni.ui._ui.AbstractItemModel, omni.kit.property.usd.usd_model_base.UsdBase):
    """
    A model representing an enumeration attribute in USD.
    
        This model provides an abstraction over a USD attribute that represents an enumeration. It allows querying and setting of the enumeration value, as well as observing changes to the enumeration option.
    
        Args:
            stage (:obj:`Usd.Stage`): The stage that the attribute is associated with.
            attribute_paths (List[Sdf.Path]): The list of attribute paths that this model is watching.
            self_refresh (bool): Whether the model should automatically refresh its value when changes occur.
            metadata (dict): A dictionary containing metadata for the model.
    
        Keyword Args:
            change_on_edit_end (bool): Whether to apply changes only when editing ends.
            treat_array_entry_as_comp (bool): Whether to treat array entries as components.
    
        
    """
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], self_refresh: bool, metadata: dict, **kwargs):
        """
        Initializes the MdlEnumAttributeModel with a USD stage and attribute paths.
        """
    def _current_index_changed(self, model):
        ...
    def _on_dirty(self):
        ...
    def _update_option(self):
        ...
    def _update_value(self, force = False):
        ...
    def begin_edit(self, item = None):
        """
        Begins an editing session for the given item.
        
                Args:
                    item: The item to begin editing.
        """
    def clean(self):
        """
        Cleans the internal state of the model.
        """
    def end_edit(self, item = None):
        """
        Ends an editing session for the given item.
        
                Args:
                    item: The item to end editing.
        """
    def get_item_children(self, item):
        """
        Retrieves the child items of the given item.
        
                Args:
                    item: The item to retrieve children for.
        """
    def get_item_value_model(self, item, column_id):
        """
        Gets the value model for the given item and column ID.
        
                Args:
                    item: The item to retrieve the value model for.
                    column_id (int): The ID of the column.
        """
    def get_value_as_string(self):
        """
        Gets the value of the model as a string.
        """
    def is_allowed_enum_string(self, enum_str):
        """
        Checks if the given enum string is allowed.
        
                Args:
                    enum_str (str): The enum string to check.
        """
    def set_from_enum_string(self, enum_str):
        """
        Sets the value of the model from the given enum string.
        
                Args:
                    enum_str (str): The enum string to set.
        """
class SdfAssetPathArrayAttributeItemModel(omni.ui._ui.AbstractItemModel):
    """
    A class for managing a collection of asset paths as attribute items within a USD stage.
    
        This model provides functionality to manipulate and retrieve data for asset paths stored in a USD stage. It supports self-refreshing and holds metadata and a delegate for advanced customization.
    
        Args:
            stage (:obj:`Usd.Stage`): The USD stage where the asset paths are located.
            attribute_paths (List[:obj:`Sdf.Path`]): A list of attribute paths within the USD stage.
            self_refresh (bool): If True, the model will automatically refresh its data when changes occur.
            metadata (dict): A dictionary containing metadata for the asset paths.
            delegate: A delegate object for custom behavior and data handling.
    """
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], self_refresh: bool, metadata: dict, delegate):
        """
        Initializes the SdfAssetPathArrayAttributeItemModel.
        
                This method does not require documentation of its parameters.
        """
    def _on_usd_changed(self, *args, **kwargs):
        ...
    def _repopulate_entries(self, value: pxr.Sdf.AssetPathArray):
        ...
    def _set_dirty(self, *args, **kwargs):
        ...
    def clean(self):
        """
        Cleans up the model, releasing any resources or references.
        """
    def drop(self, target_item, source, drop_location = -1):
        """
        Handles the drop operation.
        
                Args:
                    target_item (:obj:`SdfAssetPathItem`): The target item.
                    source (:obj:`SdfAssetPathItem`): The source item being dropped.
                    drop_location (int): The location where the drop is intended.
        """
    def drop_accepted(self, target_item, source, drop_location = -1):
        """
        Determines if a drop operation is accepted.
        
                Args:
                    target_item (:obj:`SdfAssetPathItem`): The target item.
                    source (:obj:`SdfAssetPathItem`): The source item being dropped.
                    drop_location (int): The location where the drop is intended.
        """
    def get_drag_mime_data(self, item):
        """
        Retrieves the drag mime data for an item.
        
                Args:
                    item (:obj:`SdfAssetPathItem`): The item to get the drag mime data for.
        """
    def get_item_children(self, item):
        """
        Returns the children of a given item.
        
                Args:
                    item (:obj:`SdfAssetPathItem`): The item to retrieve children for.
        """
    def get_item_value_model(self, item, column_id):
        """
        Retrieves the value model for a given item and column ID.
        
                Args:
                    item (:obj:`SdfAssetPathItem`): The item to retrieve the model for.
                    column_id (int): The column ID.
        """
    def get_item_value_model_count(self, item):
        """
        Returns the number of value models for an item.
        
                Args:
                    item (:obj:`SdfAssetPathItem`): The item to get the value model count for.
        """
    def get_value(self, *args, **kwargs):
        """
        Retrieves the current value of the model.
        
                Keyword Args:
                    args (list): Additional arguments for retrieving the value.
        """
    def set_value(self, *args, **kwargs):
        """
        Sets the value of the model.
        
                Args:
                    args (list): The value to set.
        
                Keyword Args:
                    kwargs (dict): Additional keyword arguments.
        """
    @property
    def value_model(self) -> UsdAttributeModel:
        """
        Gets the value model associated with this item model.
        
                Returns:
                    :obj:`UsdAttributeModel`: The value model.
        """
class SdfAssetPathArrayAttributeSingleEntryModel(SdfAssetPathAttributeModel):
    """
    A model for a single entry in an array of SdfAssetPath attributes.
    
        This model represents an individual asset path entry within a larger array of SdfAssetPath attributes. It provides functionality to get and set the value of the asset path, as well as to check the validity of the path and retrieve the resolved path.
    
        Args:
            stage (:obj:`Usd.Stage`): The stage where the attribute is located.
            attribute_paths (List[:obj:`Sdf.Path`]): The paths to the attributes within the USD stage.
            index (int): The index of the entry in the array this model represents.
            self_refresh (bool): Indicates whether the model should self-refresh.
            metadata (dict): A dictionary containing metadata for the attribute.
    """
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], index: int, self_refresh: bool, metadata: dict):
        """
        Initializes the SdfAssetPathArrayAttributeSingleEntryModel.
        
                Args:
                    stage (:obj:`Usd.Stage`): The USD stage associated with the model.
                    attribute_paths (List[:obj:`Sdf.Path`]): The attribute paths the model is tracking.
                    index (int): The index this model represents in the attribute array.
                    self_refresh (bool): Whether the model should self-refresh on changes.
                    metadata (dict): Additional metadata for the model.
        """
    def _is_prev_same(self):
        ...
    def _save_real_values_as_prev(self):
        ...
    def get_resolved_path(self):
        """
        Gets the resolved filesystem path for the asset at the current index.
        
                Returns:
                    str: The resolved filesystem path.
        """
    def get_value(self):
        """
        Gets the value of the asset path at the current index.
        
                Returns:
                    Any: The asset path value.
        """
    def get_value_as_string(self, elide_big_array = True) -> str:
        """
        Gets the value of the asset path at the current index as a string.
        
                Args:
                    elide_big_array (bool): Whether to elide large arrays for display.
        
                Returns:
                    str: The asset path as a string.
        """
    def is_valid_path(self) -> bool:
        """
        Checks if the asset path at the current index is a valid path.
        
                Returns:
                    bool: True if the path is valid, False otherwise.
        """
    def set_value(self, value, comp: int = -1, resolved_path: str = ''):
        """
        Sets the value of the asset path at the current index.
        
                Args:
                    value (str): The new asset path value.
                    comp (int): The component index for vector types.
                    resolved_path (str): The resolved filesystem path.
        """
    @property
    def index(self):
        """
        Gets the index of the array entry this model represents.
        
                Returns:
                    int: The index of the array entry.
        """
class SdfAssetPathAttributeModel(UsdAttributeModel):
    """
    A value model for monitoring USD asset path attributes.
    
        This model is specifically designed to handle the Sdf.AssetPath attribute type in USD, providing
        additional functionality to resolve and validate asset paths.
    
        Args:
            stage (:obj:`Usd.Stage`): The USD stage associated with the attribute.
            attribute_paths (List[:obj:`Sdf.Path`]): A list of Sdf.Path objects representing the attribute paths to monitor.
            self_refresh (bool): Indicates whether the model should refresh itself when the attribute value changes.
            metadata (dict): Additional metadata that may be needed for the model.
    
        Keyword Args:
            treat_array_entry_as_comp (bool): If True, treat array entries as individual components. Default is False.
    
        
    """
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], self_refresh: bool, metadata: dict, **kwargs):
        """
        Constructor for SdfAssetPathAttributeModel.
        """
    def _change_property(self, path: pxr.Sdf.Path, new_value, old_value):
        ...
    def _get_resolved_path(self, value):
        ...
    def _get_value_as_string(self, value, **kwargs):
        ...
    def _is_prev_same(self):
        ...
    def _is_valid_path(self, value) -> bool:
        ...
    def _save_real_values_as_prev(self):
        ...
    def get_resolved_path(self):
        """
        Gets the resolved path of the asset.
        
                Returns:
                    str: The resolved asset path.
        """
    def get_value_as_string(self, elide_big_array = True) -> str:
        """
        Gets the string representation of the asset path value.
        
                Args:
                    elide_big_array (bool): If True, large arrays will be shortened in the representation.
        
                Returns:
                    str: The string representation of the asset path value.
        """
    def is_valid_path(self) -> bool:
        """
        Determines if the stored asset path is valid.
        
                Returns:
                    bool: True if the path is valid, False otherwise.
        """
    def set_value(self, value, comp: int = -1, resolved_path: str = ''):
        """
        Sets the value of the asset path.
        
                Args:
                    value (str): The new value for the asset path.
                    comp (int): Component index when dealing with array attributes.
                    resolved_path (str): The resolved path corresponding to the value.
        """
class SdfTimeCodeModel(UsdAttributeModel):
    """
    A specialized model for handling SDF timecodes in USD attributes.
    
        This model extends the capabilities of the UsdAttributeModel by providing additional functionality to manage SDF timecode values. It is particularly useful for working with attributes that represent time-based data in USD.
    
        While similar in structure to UsdAttributeModel, this model overrides the method to save the previous real values as SDF TimeCodes, ensuring proper initialization and handling of timecode data types.
        
    """
    def _save_real_values_as_prev(self):
        ...
class TfTokenAttributeModel(omni.ui._ui.AbstractItemModel, omni.kit.property.usd.usd_model_base.UsdBase):
    """
    A model for managing USD attributes of type 'TfToken'.
    
        This model allows for the interaction and manipulation of TfToken attributes within a USD stage. It keeps track of
        allowed tokens and provides functionality for selecting and updating the value of the attribute based on the
        allowed set of tokens.
    
        Args:
            stage (:obj:`Usd.Stage`): The USD stage where the attribute is located.
            attribute_paths (List[:obj:`Sdf.Path`]): The list of attribute paths to be managed by the model.
            self_refresh (bool): A flag indicating whether the model should automatically update itself when changes occur.
            metadata (dict): A dictionary containing metadata associated with the attribute.
    
        Keyword Args:
            change_on_edit_end (bool): A flag indicating whether the model should only apply changes when an edit ends.
            ambiguous (bool): A flag indicating whether the attribute has ambiguous values (true for multi-selection).
            treat_as_asset_path (bool): A flag indicating if the attribute should be treated as an asset path.
            treat_array_entry_as_comp (bool): A flag indicating whether array entries should be treated as components.
            allowed_tokens (List[str]): A list of strings representing the allowed tokens for the attribute.
    
        The model is a combination of ui.AbstractItemModel and UsdBase, which allows for both UI interaction and
        underlying USD functionality.
    """
    DUPLICATE_TAG: typing.ClassVar[str] = '** DUPLICATE **'
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], self_refresh: bool, metadata: dict, **kwargs):
        """
        Initializer for TfTokenAttributeModel.
        """
    def _current_index_changed(self, model):
        ...
    def _get_allowed_tokens(self, attr):
        ...
    def _get_value_from_index(self, index):
        ...
    def _on_dirty(self):
        ...
    def _update_allowed_token(self, token_item = omni.kit.property.usd.usd_model_items.AllowedTokenItem):
        ...
    def _update_index(self):
        ...
    def _update_value(self, force = False):
        ...
    def begin_edit(self, item = None):
        """
        Begins an edit operation on the model.
        
                Args:
                    item: The item being edited.
        """
    def clean(self):
        """
        Cleans up the model, removing any cached data.
        """
    def end_edit(self, item = None):
        """
        Ends an edit operation on the model.
        
                Args:
                    item: The item that was edited.
        """
    def get_item_children(self, item):
        """
        Retrieves the children of a given item in the model.
        
                Args:
                    item: The item whose children are to be retrieved.
        
                Returns:
                    list: A list of the allowed tokens.
        """
    def get_item_value_model(self, item, column_id):
        """
        Gets the value model associated with a given item and column.
        
                Args:
                    item: The item for which to retrieve the value model.
                    column_id (int): The column identifier.
        
                Returns:
                    ui.AbstractValueModel: The value model for the specified item and column.
        """
    def get_value_as_token(self):
        """
        Retrieves the current value as a token.
        
                Returns:
                    str: The current value as a token.
        """
    def is_allowed_token(self, token):
        """
        Checks if a token is allowed in the model.
        
                Args:
                    token (str): The token to check.
        
                Returns:
                    bool: True if the token is allowed, False otherwise.
        """
    def set_value(self, value, comp: int = -1) -> bool:
        """
        Sets the value of the model.
        
                Args:
                    value (str): The value to set in the model.
                    comp (int): An optional component index when dealing with vector types.
        """
class UsdAttributeInvertedModel(UsdAttributeModel):
    """
    A model that inverts the boolean value from a USD attribute.
    
        This model extends the UsdAttributeModel and provides an inverted boolean representation of the USD attribute value. It can be particularly useful when working with toggles or switches in a user interface that require a reversed logic.
    
        The get_value_as_bool method returns the inverted state of the attribute's original boolean value. The set_value method sets the attribute's value to the opposite of the provided value.
        
    """
    def get_value(self):
        """
        Returns the inverted value of the underlying USD attribute.
        
                Returns:
                    bool: Inverted value of the USD attribute.
        """
    def get_value_as_bool(self) -> bool:
        """
        Returns the inverted boolean value of the underlying USD attribute.
        
                Returns:
                    bool: Inverted value of the USD attribute.
        """
    def get_value_as_string(self, elide_big_array = True) -> str:
        """
        Returns the inverted boolean value as a string.
        
                Args:
                    elide_big_array (bool): If True, large arrays are represented as [...].
        
                Returns:
                    str: 'True' if original value is False, 'False' otherwise.
        """
    def set_value(self, value, comp: int = -1):
        """
        Sets the value of the USD attribute to the opposite of the given value.
        
                Args:
                    value (bool): The value to set, after being inverted.
                    comp (int): Component index for vector types, -1 for scalar.
        """
class UsdAttributeModel(omni.ui._ui.AbstractValueModel, omni.kit.property.usd.usd_model_base.UsdBase):
    """
    A value model that re-implements the AbstractValueModel interface in Python to observe a USD attribute path.
    
        Args:
            stage (:obj:`Usd.Stage`): The stage that contains the USD attribute.
            attribute_paths (List[:obj:`Sdf.Path`]): A list of paths to the USD attributes to be observed.
            self_refresh (bool): Whether the model should automatically refresh its value when changes occur in USD.
            metadata (dict): A dictionary of metadata relevant to the USD attribute.
            change_on_edit_end (bool): Indicates if the value should only change when the edit ends.
    
        Keyword Args:
            treat_array_entry_as_comp (bool): Treat array entries as components of a single value.
            is_normal_attribute (bool): Specify if the attribute is a normal attribute.
    
        This model provides a clean interface to interact with USD attributes, offering functions to begin and end edits, get and set attribute values in various data types, and handle value changes and updates.
        
    """
    def __init__(self, stage: pxr.Usd.Stage, attribute_paths: typing.List[pxr.Sdf.Path], self_refresh: bool, metadata: dict, change_on_edit_end = True, **kwargs):
        """
        Initializes the value model that is reimplemented in Python to watch a USD attribute path.
        """
    def _on_dirty(self):
        ...
    def begin_edit(self):
        """
        Begins an editing session by notifying the USD base and the UI model.
        """
    def clean(self):
        """
        Cleans up the model by delegating to the base clean-up method.
        """
    def end_edit(self):
        """
        Ends an editing session by notifying the USD base and the UI model.
        """
    def get_value_as_bool(self) -> bool:
        """
        Retrieves the value of the USD attribute as a boolean.
        
                Returns:
                    bool: The attribute value as a boolean.
        """
    def get_value_as_float(self) -> float:
        """
        Retrieves the value of the USD attribute as a float.
        
                Returns:
                    float: The attribute value as a float.
        """
    def get_value_as_int(self) -> int:
        """
        Retrieves the value of the USD attribute as an integer.
        
                Returns:
                    int: The attribute value as an integer.
        """
    def get_value_as_string(self, elide_big_array = True) -> str:
        """
        Retrieves the value of the USD attribute as a string.
        
                Args:
                    elide_big_array (bool): If True, elides long array displays.
        
                Returns:
                    str: The attribute value formatted as a string.
        """
    def set_value(self, value, comp: int = -1):
        """
        Sets the value of the USD attribute.
        
                Args:
                    value: New value to set the attribute to.
                    comp (int): Optional index for the component of the value to set.
        """
