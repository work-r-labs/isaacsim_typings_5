"""
pybind11 omni.usd bindings
"""
from __future__ import annotations
import carb._carb
import carb.events._events
import omni.timeline._timeline
import pxr.Usd
import pybind11_stubgen.typing_ext
import typing
__all__ = ['AudioManager', 'EngineCreationConfig', 'EngineCreationFlags', 'MOTION_RAYTRACING_ENABLED', 'NONE', 'OpaqueSharedHydraEngineContext', 'PickingMode', 'SKIP_ON_WORKER_PROCESS', 'Selection', 'StageEventType', 'StageRenderingEventType', 'StageState', 'UsdContext', 'UsdContextInitialLoadSet', 'WRITABLE_USD_FILE_EXTS_STR', 'add_hydra_engine', 'attach_all_hydra_engines', 'create_context', 'destroy_context', 'get_context', 'get_context_from_stage_id', 'get_or_create_hydra_engine', 'merge_layers', 'merge_prim_spec', 'release_all_hydra_engines', 'release_hydra_engine', 'resolve_paths', 'resolve_prim_path_references', 'resolve_prim_paths_references', 'shutdown_usd']
class AudioManager:
    """
    Audio manager. See :class:`omni.usd.audio` for wrapped python interfaces that manage audio play/capture.
    """
class EngineCreationConfig:
    """
    
                EngineCreationConfig structure.
            
    """
    device_mask: int
    flags: EngineCreationFlags
    tickrate_in_hz: int
    def __init__(self) -> None:
        ...
class EngineCreationFlags:
    """
    
            Specifies the flags for the hydra engine creation.
            
    
    Members:
    
      NONE
    
      MOTION_RAYTRACING_ENABLED
    
      SKIP_ON_WORKER_PROCESS
    """
    MOTION_RAYTRACING_ENABLED: typing.ClassVar[EngineCreationFlags]  # value = <EngineCreationFlags.MOTION_RAYTRACING_ENABLED: 1>
    NONE: typing.ClassVar[EngineCreationFlags]  # value = <EngineCreationFlags.NONE: 0>
    SKIP_ON_WORKER_PROCESS: typing.ClassVar[EngineCreationFlags]  # value = <EngineCreationFlags.SKIP_ON_WORKER_PROCESS: 2>
    __members__: typing.ClassVar[dict[str, EngineCreationFlags]]  # value = {'NONE': <EngineCreationFlags.NONE: 0>, 'MOTION_RAYTRACING_ENABLED': <EngineCreationFlags.MOTION_RAYTRACING_ENABLED: 1>, 'SKIP_ON_WORKER_PROCESS': <EngineCreationFlags.SKIP_ON_WORKER_PROCESS: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class OpaqueSharedHydraEngineContext:
    pass
class PickingMode:
    """
    Members:
    
      NONE
    
      RESET_AND_SELECT
    
      MERGE_SELECTION
    
      INVERT_SELECTION
    
      TRACK
    """
    INVERT_SELECTION: typing.ClassVar[PickingMode]  # value = <PickingMode.INVERT_SELECTION: 3>
    MERGE_SELECTION: typing.ClassVar[PickingMode]  # value = <PickingMode.MERGE_SELECTION: 2>
    NONE: typing.ClassVar[PickingMode]  # value = <PickingMode.NONE: 0>
    RESET_AND_SELECT: typing.ClassVar[PickingMode]  # value = <PickingMode.RESET_AND_SELECT: 1>
    TRACK: typing.ClassVar[PickingMode]  # value = <PickingMode.TRACK: 5>
    __members__: typing.ClassVar[dict[str, PickingMode]]  # value = {'NONE': <PickingMode.NONE: 0>, 'RESET_AND_SELECT': <PickingMode.RESET_AND_SELECT: 1>, 'MERGE_SELECTION': <PickingMode.MERGE_SELECTION: 2>, 'INVERT_SELECTION': <PickingMode.INVERT_SELECTION: 3>, 'TRACK': <PickingMode.TRACK: 5>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Selection:
    """
    
                omni.usd.Selection manages all stage selections and provides APIs for querying/setting selections.
            
    """
    class SourceType:
        """
        
                Selection source stage.
                
        
        Members:
        
          USD : Selections from native USD stage.
        
          FABRIC : "Selections from Fabric.
        
          ALL : Selections from both native USD stage and Fabric.
        """
        ALL: typing.ClassVar[Selection.SourceType]  # value = <SourceType.ALL: 3>
        FABRIC: typing.ClassVar[Selection.SourceType]  # value = <SourceType.FABRIC: 2>
        USD: typing.ClassVar[Selection.SourceType]  # value = <SourceType.USD: 1>
        __members__: typing.ClassVar[dict[str, Selection.SourceType]]  # value = {'USD': <SourceType.USD: 1>, 'FABRIC': <SourceType.FABRIC: 2>, 'ALL': <SourceType.ALL: 3>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    def clear_selected_prim_paths(self, source: Selection.SourceType = ...) -> bool:
        """
                    Clears all selections.
        
                    Args:
                        source (omni.usd.Selection.SourceType): The source to be cleared. Selections are stored differently for Fabric. By default, it will check selections from native
                            USD stage.
        """
    def get_selected_prim_paths(self, source: Selection.SourceType = ...) -> list[str]:
        """
                        Gets selected prim paths.
        
                        Args:
                            source (omni.usd.Selection.SourceType): The source to get selections. Selections are stored differently for Fabric. By default, it will check selections from native
                                USD stage.
        
                        Returns:
                            List of selected prim paths.
        """
    def is_prim_path_selected(self, path: str, source: Selection.SourceType = ...) -> bool:
        """
                    Checks if a prim is selected or not.
        
                    Args:
                        path (str): Prim path to be checked.
                        source (omni.usd.Selection.SourceType): The source to be checked. Selections are stored differently for Fabric. By default, it will check selections from native
                            USD stage.
        """
    def select_all_prims(self, type_names: typing.Any = None) -> None:
        """
        Selects all prims with specific prim types.
        """
    def select_inverted_prims(self) -> None:
        """
        Selects all prims without the current selections.
        """
    def set_prim_path_selected(self, path: str, selected: bool, forcePrim: bool, clearSelected: bool, expandInStage: bool = True, source: Selection.SourceType = ...) -> bool:
        """
                    Selects/Unselects single prim.
        
                    Args:
                        path (str): Prim path to be selected.
                        selected (bool): Selected or unselected.
                        forcePrim (bool): Force it to be Prim Mode. When this option is false, it depends on the selection mode to decide the prim to be selected.
                        clearSelected (bool): Clears existing selections or not before selection.
                        expandInStage (bool):  DEPRECATED.
                        source (omni.usd.Selection.SourceType): The source to be set. Selections are stored differently for Fabric. By default, it will check selections from native
                            USD stage.
        """
    def set_selected_prim_paths(self, paths: list[str], expandInStage: bool = True, source: Selection.SourceType = ...) -> bool:
        """
                    Sets selected prim paths.
        
                    Args:
                        paths (List[str]): The list of prim paths to be selected.
                        expandInStage (bool): DEPRECATED.
                        source (omni.usd.Selection.SourceType): The source to be set. Selections are stored differently for Fabric. By default, it will check selections from native
                            USD stage.
        """
class StageEventType:
    """
    
            Stage Event Type. Stage events are sent through event stream of the UsdContext.
            
    
    Members:
    
      SAVING : Starting to save stage.
    
      SAVED : Stage saved successfully.
    
      SAVE_FAILED : Stage save failed.
    
      OPENING : Starting to open stage.
    
      OPENED : Stage open finished.
    
      OPEN_FAILED : Stage open failed.
    
      CLOSING : Starting to close stage.
    
      CLOSED : Stage closed successfully.
    
      SELECTION_CHANGED : Stage selections changed.
    
      ASSETS_LOADED : Assets (textures or materials) loaded successfully.
    
      ASSETS_LOAD_ABORTED : Assets (textures or materials) load aborted .
    
      GIZMO_TRACKING_CHANGED : DEPRECATED.
    
      MDL_PARAM_LOADED : Some MDL materials finish its params loading by material watcher.
    
      SETTINGS_LOADED : Render settings loaded.
    
      SETTINGS_SAVING : Starting to save render settings.
    
      OMNIGRAPH_START_PLAY : OmniGraph is starting to play.
    
      OMNIGRAPH_STOP_PLAY : OmniGraph is stopped to play.
    
      SIMULATION_START_PLAY : Physx Simulation starts playing.
    
      SIMULATION_STOP_PLAY : Physx Simulation stopped.
    
      ANIMATION_START_PLAY : Timeline starts playing.
    
      ANIMATION_STOP_PLAY : Timeline stopped.
    
      DIRTY_STATE_CHANGED : Stage dirtiness state is changed. It's sent when stage adds the first unsaved change, or after stage finishes it saving.
    
      ASSETS_LOADING : Assets are in progress of loading (textures or materials).
    
      ACTIVE_LIGHT_COUNTS_CHANGED : Count of active lights is changed.
    
      HIERARCHY_CHANGED : Some prims are resynced in the stage.
    
      HYDRA_GEOSTREAMING_STARTED
    
      HYDRA_GEOSTREAMING_STOPPED
    
      HYDRA_GEOSTREAMING_STOPPED_NOT_ENOUGH_MEM
    
      HYDRA_GEOSTREAMING_STOPPED_AT_LIMIT
    """
    ACTIVE_LIGHT_COUNTS_CHANGED: typing.ClassVar[StageEventType]  # value = <StageEventType.ACTIVE_LIGHT_COUNTS_CHANGED: 22>
    ANIMATION_START_PLAY: typing.ClassVar[StageEventType]  # value = <StageEventType.ANIMATION_START_PLAY: 18>
    ANIMATION_STOP_PLAY: typing.ClassVar[StageEventType]  # value = <StageEventType.ANIMATION_STOP_PLAY: 19>
    ASSETS_LOADED: typing.ClassVar[StageEventType]  # value = <StageEventType.ASSETS_LOADED: 8>
    ASSETS_LOADING: typing.ClassVar[StageEventType]  # value = <StageEventType.ASSETS_LOADING: 21>
    ASSETS_LOAD_ABORTED: typing.ClassVar[StageEventType]  # value = <StageEventType.ASSETS_LOAD_ABORTED: 9>
    CLOSED: typing.ClassVar[StageEventType]  # value = <StageEventType.CLOSED: 6>
    CLOSING: typing.ClassVar[StageEventType]  # value = <StageEventType.CLOSING: 5>
    DIRTY_STATE_CHANGED: typing.ClassVar[StageEventType]  # value = <StageEventType.DIRTY_STATE_CHANGED: 20>
    GIZMO_TRACKING_CHANGED: typing.ClassVar[StageEventType]  # value = <StageEventType.GIZMO_TRACKING_CHANGED: 10>
    HIERARCHY_CHANGED: typing.ClassVar[StageEventType]  # value = <StageEventType.HIERARCHY_CHANGED: 23>
    HYDRA_GEOSTREAMING_STARTED: typing.ClassVar[StageEventType]  # value = <StageEventType.HYDRA_GEOSTREAMING_STARTED: 24>
    HYDRA_GEOSTREAMING_STOPPED: typing.ClassVar[StageEventType]  # value = <StageEventType.HYDRA_GEOSTREAMING_STOPPED: 25>
    HYDRA_GEOSTREAMING_STOPPED_AT_LIMIT: typing.ClassVar[StageEventType]  # value = <StageEventType.HYDRA_GEOSTREAMING_STOPPED_AT_LIMIT: 27>
    HYDRA_GEOSTREAMING_STOPPED_NOT_ENOUGH_MEM: typing.ClassVar[StageEventType]  # value = <StageEventType.HYDRA_GEOSTREAMING_STOPPED_NOT_ENOUGH_MEM: 26>
    MDL_PARAM_LOADED: typing.ClassVar[StageEventType]  # value = <StageEventType.MDL_PARAM_LOADED: 11>
    OMNIGRAPH_START_PLAY: typing.ClassVar[StageEventType]  # value = <StageEventType.OMNIGRAPH_START_PLAY: 14>
    OMNIGRAPH_STOP_PLAY: typing.ClassVar[StageEventType]  # value = <StageEventType.OMNIGRAPH_STOP_PLAY: 15>
    OPENED: typing.ClassVar[StageEventType]  # value = <StageEventType.OPENED: 3>
    OPENING: typing.ClassVar[StageEventType]  # value = <StageEventType.OPENING: 2>
    OPEN_FAILED: typing.ClassVar[StageEventType]  # value = <StageEventType.OPEN_FAILED: 4>
    SAVED: typing.ClassVar[StageEventType]  # value = <StageEventType.SAVED: 0>
    SAVE_FAILED: typing.ClassVar[StageEventType]  # value = <StageEventType.SAVE_FAILED: 1>
    SAVING: typing.ClassVar[StageEventType]  # value = <StageEventType.SAVING: 28>
    SELECTION_CHANGED: typing.ClassVar[StageEventType]  # value = <StageEventType.SELECTION_CHANGED: 7>
    SETTINGS_LOADED: typing.ClassVar[StageEventType]  # value = <StageEventType.SETTINGS_LOADED: 12>
    SETTINGS_SAVING: typing.ClassVar[StageEventType]  # value = <StageEventType.SETTINGS_SAVING: 13>
    SIMULATION_START_PLAY: typing.ClassVar[StageEventType]  # value = <StageEventType.SIMULATION_START_PLAY: 16>
    SIMULATION_STOP_PLAY: typing.ClassVar[StageEventType]  # value = <StageEventType.SIMULATION_STOP_PLAY: 17>
    __members__: typing.ClassVar[dict[str, StageEventType]]  # value = {'SAVING': <StageEventType.SAVING: 28>, 'SAVED': <StageEventType.SAVED: 0>, 'SAVE_FAILED': <StageEventType.SAVE_FAILED: 1>, 'OPENING': <StageEventType.OPENING: 2>, 'OPENED': <StageEventType.OPENED: 3>, 'OPEN_FAILED': <StageEventType.OPEN_FAILED: 4>, 'CLOSING': <StageEventType.CLOSING: 5>, 'CLOSED': <StageEventType.CLOSED: 6>, 'SELECTION_CHANGED': <StageEventType.SELECTION_CHANGED: 7>, 'ASSETS_LOADED': <StageEventType.ASSETS_LOADED: 8>, 'ASSETS_LOAD_ABORTED': <StageEventType.ASSETS_LOAD_ABORTED: 9>, 'GIZMO_TRACKING_CHANGED': <StageEventType.GIZMO_TRACKING_CHANGED: 10>, 'MDL_PARAM_LOADED': <StageEventType.MDL_PARAM_LOADED: 11>, 'SETTINGS_LOADED': <StageEventType.SETTINGS_LOADED: 12>, 'SETTINGS_SAVING': <StageEventType.SETTINGS_SAVING: 13>, 'OMNIGRAPH_START_PLAY': <StageEventType.OMNIGRAPH_START_PLAY: 14>, 'OMNIGRAPH_STOP_PLAY': <StageEventType.OMNIGRAPH_STOP_PLAY: 15>, 'SIMULATION_START_PLAY': <StageEventType.SIMULATION_START_PLAY: 16>, 'SIMULATION_STOP_PLAY': <StageEventType.SIMULATION_STOP_PLAY: 17>, 'ANIMATION_START_PLAY': <StageEventType.ANIMATION_START_PLAY: 18>, 'ANIMATION_STOP_PLAY': <StageEventType.ANIMATION_STOP_PLAY: 19>, 'DIRTY_STATE_CHANGED': <StageEventType.DIRTY_STATE_CHANGED: 20>, 'ASSETS_LOADING': <StageEventType.ASSETS_LOADING: 21>, 'ACTIVE_LIGHT_COUNTS_CHANGED': <StageEventType.ACTIVE_LIGHT_COUNTS_CHANGED: 22>, 'HIERARCHY_CHANGED': <StageEventType.HIERARCHY_CHANGED: 23>, 'HYDRA_GEOSTREAMING_STARTED': <StageEventType.HYDRA_GEOSTREAMING_STARTED: 24>, 'HYDRA_GEOSTREAMING_STOPPED': <StageEventType.HYDRA_GEOSTREAMING_STOPPED: 25>, 'HYDRA_GEOSTREAMING_STOPPED_NOT_ENOUGH_MEM': <StageEventType.HYDRA_GEOSTREAMING_STOPPED_NOT_ENOUGH_MEM: 26>, 'HYDRA_GEOSTREAMING_STOPPED_AT_LIMIT': <StageEventType.HYDRA_GEOSTREAMING_STOPPED_AT_LIMIT: 27>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class StageRenderingEventType:
    """
    
            Rendering Events.
            
    
    Members:
    
      NEW_FRAME
    """
    NEW_FRAME: typing.ClassVar[StageRenderingEventType]  # value = <StageRenderingEventType.NEW_FRAME: 0>
    __members__: typing.ClassVar[dict[str, StageRenderingEventType]]  # value = {'NEW_FRAME': <StageRenderingEventType.NEW_FRAME: 0>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class StageState:
    """
    
            Stage states. The current stage state of the UsdContext.
            
    
    Members:
    
      CLOSED : Stage closed.
    
      CLOSING : Stage closing.
    
      OPENING : Stage opening.
    
      OPENED : Stage opened.
    """
    CLOSED: typing.ClassVar[StageState]  # value = <StageState.CLOSED: 0>
    CLOSING: typing.ClassVar[StageState]  # value = <StageState.CLOSING: 3>
    OPENED: typing.ClassVar[StageState]  # value = <StageState.OPENED: 2>
    OPENING: typing.ClassVar[StageState]  # value = <StageState.OPENING: 1>
    __members__: typing.ClassVar[dict[str, StageState]]  # value = {'CLOSED': <StageState.CLOSED: 0>, 'CLOSING': <StageState.CLOSING: 3>, 'OPENING': <StageState.OPENING: 1>, 'OPENED': <StageState.OPENED: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UsdContext:
    """
    
                UsdContext is the container for a :cpp:class:`PXR_NS::UsdStage` that manages the lifecycle of a UsdStage instance.
                Because of historical reasons, UsdContext also undertakes extra responsibilities, including managing Hydra Engines selections, and etc.
            
    """
    def attach_stage_async(self, stage: pxr.Usd.Stage) -> typing.Tuple[bool, str]:
        """
        
            Asynchronous version of :func:`omni.usd.UsdContext.attach_stage_with_callback`. Attaches an opened stage to the context.
        
            Args:
                stage (pxr.Usd.Stage): The instance of UsdStage.
        
            Returns:
                (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                    the second one tells the error message if the operation is failed.
            
        """
    def attach_stage_with_callback(self, stage_id: int, on_finish_fn: typing.Callable[[bool, str], None] = None) -> bool:
        """
                        Attaches an existing stage asynchronously.
        
                        Args:
                            stage_id (long int): The stage id that can be queried with pxr.UsdUtils.StageCache.Get().Find.
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
        """
    def can_close_stage(self) -> bool:
        """
        Whether the current stage can be closed or not.
        """
    def can_open_stage(self) -> bool:
        """
        Whether a new stage can be opened or not.
        """
    def can_save_stage(self) -> bool:
        """
        Whether the current stage can be saved or not.
        """
    def close_stage(self, on_finish_fn: typing.Callable[[bool, str], None] = None) -> bool:
        """
                        Closes the current stage synchronously.
        
                        Args:
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
        
                        Returns:
                            Successful or not.
        """
    def close_stage_async(self) -> typing.Tuple[bool, str]:
        """
        
            Asynchronous version of :func:`omni.usd.UsdContext.close_stage_with_callback`. Closes the current stage.
        
            Returns:
                (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                    the second one tells the error message if the operation is failed.
            
        """
    def close_stage_with_callback(self, on_finish_fn: typing.Callable[[bool, str], None]) -> bool:
        """
                        Closes the current stage asynchronously.
        
                        Args:
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
        """
    def compute_path_world_bounding_box(self, arg0: str) -> tuple[carb._carb.Double3, carb._carb.Double3]:
        """
        Compute world bound box for specified prim. Unlike using USD API directly, it speeds up bound box computation with cache or Fabric when it's enabled.
        """
    def compute_path_world_transform(self, arg0: str) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        Compute world transform for specified prim. Unlike using USD API directly, it speeds up transform computation with cache.
        """
    def disable_save_to_recent_files(self) -> None:
        """
        Disable save to recent files for opened stage url.
        """
    def enable_save_to_recent_files(self) -> None:
        """
        Enable save to rencet files for opened stage url.
        """
    def export_as_stage(self, url: str, on_finish_fn: typing.Callable[[bool, str], None] = None) -> bool:
        """
                        Export stage with all prims flattened synchronously, and it will include contents from session layer also.
        
                        Args:
                            url (str): New location to save the exported stage.
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
        
                        Returns:
                            Successful or not.
        """
    def export_as_stage_async(self, url: str) -> typing.Tuple[bool, str]:
        """
        
            Asynchronous version of :func:`omni.usd.UsdContext.export_as_stage_with_callback`. Flattens and exports the current stage.
        
            Returns:
                (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                    the second one tells the error message if the operation is failed.
            
        """
    def export_as_stage_with_callback(self, url: str, on_finish_fn: typing.Callable[[bool, str], None]) -> bool:
        """
                        Export stage with all prims flattened asynchronously, and it will include contents from session layer also.
        
                        Args:
                            url (str): New location to save the exported stage.
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
        """
    def get_attached_hydra_engine_names(self) -> list[str]:
        """
        Gets the attached hydra engine names to the UsdContext.
        """
    def get_geometry_instance_path(self, arg0: int) -> str:
        """
        Gets the geometry instance path with instance id.
        """
    def get_name(self) -> str:
        """
        Gets the name of the context.
        """
    def get_rendering_event_stream(self) -> carb.events._events.IEventStream:
        """
        Gets the rendering event stream. See :class:`.StageRenderingEventType` for more details.
        """
    def get_selection(self) -> ...:
        """
        Gets the selection interface. See :class:`.Selection` for more details.
        """
    def get_stage(self):
        """
        Gets current opened :class:`pxr.Usd.Stage`
        """
    def get_stage_audio_manager(self) -> AudioManager:
        """
        Internal. Gets audio manager handle. See :class:`omni.usd.audio` for wrapped python interfaces that manage audio play/capture.
        """
    def get_stage_event_stream(self) -> carb.events._events.IEventStream:
        """
        Gets the stage event stream. See :class:`.StageEventType` for more details.
        """
    def get_stage_id(self) -> int:
        """
        Gets the UsdStage Id that can be queried with Usd.StageCache.
        """
    def get_stage_loading_status(self) -> tuple[str, int, int]:
        """
                        Gets the stage loading status.
        
                        Returns:
                            (str, int, int): A tuple that the first element tells the current loading message, the second element tells how many files are loaded already, and the third one tells the total files to be loaded.
        """
    def get_stage_state(self) -> StageState:
        """
        Gets the current stage state. See :class:`.StageState` for more details.
        """
    def get_stage_streaming_status(self) -> bool:
        """
                        Gets the status of all stage streaming systems.
                        Returns:
                            bool: whether any of the streaming systems is busy.
        """
    def get_stage_url(self) -> str:
        """
        Gets the Stage url. The URL can be used as layer identifier to query layer handle from USD Layer Registry.
        """
    def get_timeline(self) -> omni.timeline._timeline.Timeline:
        """
        Gets the timeline interface. See :mod:`omni.timeline` for more details.
        """
    def get_timeline_name(self) -> str:
        """
        Gets current timeline used in this context.
        """
    def has_pending_edit(self) -> bool:
        """
        Whether it has unsaved edits or not.
        """
    def is_new_stage(self) -> bool:
        """
        Whether the current stage (root layer) is anonymous or not.
        """
    def is_omni_stage(self) -> bool:
        """
        Whether the URL of the current stage (root layer) is prefixed with 'omniverse:'.
        """
    def is_writable(self) -> bool:
        """
        Whether the current stage is writable or not
        """
    def load_mdl_parameters_for_prim_async(self, prim, recreate: bool = False):
        ...
    def load_render_settings_from_stage(self, arg0: int) -> None:
        """
        Loads render settings from stage.
        """
    def new_stage(self, load_set: UsdContextInitialLoadSet = ...) -> bool:
        ...
    def new_stage_async(self, load_set: UsdContextInitialLoadSet = ...) -> typing.Tuple[bool, str]:
        """
        
            Asynchronous version of :func:`omni.usd.UsdContext.new_stage_with_callback`. Creates a new stage with anonymous root layer.
        
            Args:
                load_set (omni.usd.UsdContextInitialLoadSet): Whether it should open stage with payloads loaded or not. By default, it loads all payloads.
        
            Returns:
                (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                    the second one tells the error message if the operation is failed.
            
        """
    def new_stage_with_callback(self, fn = None, load_set: UsdContextInitialLoadSet = ...):
        """
        Asynchronous version of :func:`omni.usd.UsdContext.new_stage` that supports to customize load set of new stage.
        """
    def next_frame_async(self, inViewportId = 0) -> None:
        """
        Wait for frame complete event from Kit for specific viewport. 
        """
    def next_stage_event_async(self) -> typing.Tuple[omni.usd._usd.StageEventType, typing.Dict[typing.Any, typing.Any]]:
        """
        Wait for next stage event of omni.usd.
        """
    def next_usd_async(self, inViewportId = 0) -> None:
        """
        Wait for frame complete event from Kit for specific viewport. 
        """
    def open_stage(self, url: str, on_finish_fn: typing.Callable[[bool, str], None] = None, load_set: UsdContextInitialLoadSet = ...) -> bool:
        """
                        Opens a stage synchronously.
        
                        Args:
                            url (str): The stage URL that can be resolved.
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
                            load_set (omni.usd.UsdContextInitialLoadSet): Whether it should open stage with payloads loaded or not. By default, it loads all payloads.
        
                        Returns:
                            Successful or not.
        """
    def open_stage_async(self, url: str, load_set: UsdContextInitialLoadSet = ..., session_layer_url: str = None) -> typing.Tuple[bool, str]:
        """
        
            Asynchronous version of :func:`omni.usd.UsdContext.open_stage_with_callback`. Opens a new stage.
        
            Args:
                url (str): Stage URL to open.
                load_set (omni.usd.UsdContextInitialLoadSet): If it's to open all payloads or none.
                session_layer_url (str): Specified session layer.
        
            Returns:
                (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                    the second one tells the error message if the operation is failed.
            
        """
    def open_stage_with_callback(self, url: str, on_finish_fn: typing.Callable[[bool, str], None], load_set: UsdContextInitialLoadSet = ...) -> bool:
        """
                        Opens a stage asynchronously.
        
                        Args:
                            url (str): The stage URL that can be resolved.
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
                            load_set (omni.usd.UsdContextInitialLoadSet): Whether it should open stage with payloads loaded or not. By default, it loads all payloads.
        """
    def open_stage_with_session_layer(self, url: str, session_layer_url: str, on_finish_fn: typing.Callable[[bool, str], None], load_set: UsdContextInitialLoadSet = ...) -> bool:
        """
                        Opens a stage asynchronously with specified session layer.
        
                        Args:
                            url (str): The stage URL that can be resolved.
                            session_layer_url (str): The specified session layer URL.
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
                            load_set (omni.usd.UsdContextInitialLoadSet): Whether it should open stage with payloads loaded or not. By default, it loads all payloads.
        """
    def register_selection_group(self) -> int:
        """
        Registers a selection group. Prims can be assigned to selection group with customized outline colors than the default. It supports 255 selection groups at most.
        """
    def remove_all_hydra_engines(self) -> None:
        """
        Detach all attached hydra engines from the UsdContext.
        """
    def reopen_stage(self, on_finish_fn: typing.Callable[[bool, str], None] = None, load_set: UsdContextInitialLoadSet = ...) -> bool:
        """
                        Re-opens the current stage synchronously.
        
                        Args:
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
                            load_set (omni.usd.UsdContextInitialLoadSet): Whether it should open stage with payloads loaded or not. By default, it loads all payloads.
        
                        Returns:
                            Successful or not.
        """
    def reopen_stage_async(self, load_set: UsdContextInitialLoadSet = ...) -> typing.Tuple[bool, str]:
        """
        
            Asynchronous version of :func:`omni.usd.UsdContext.reopen_stage_with_callback`. Re-opens the current stage.
        
            Args:
                load_set (omni.usd.UsdContextInitialLoadSet): If it's to open all payloads or none.
        
            Returns:
                (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                    the second one tells the error message if the operation is failed.
            
        """
    def reopen_stage_with_callback(self, on_finish_fn: typing.Callable[[bool, str], None], load_set: UsdContextInitialLoadSet = ...) -> bool:
        """
                        Re-opens the current stage asynchronously.
        
                        Args:
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
                            load_set (omni.usd.UsdContextInitialLoadSet): Whether it should open stage with payloads loaded or not. By default, it loads all payloads.
        """
    def reset_renderer_accumulation(self) -> None:
        """
                        Resets all accumulation state inside renderers so that rendering n frames after this point is deterministic independent of prior frame-history.
        """
    def save_as_stage(self, url: str, on_finish_fn: typing.Callable[[bool, str, list[str]], None] = None) -> bool:
        """
                        Saves the current stage to another location synchronously.
        
                        Args:
                            url (str): New location to save the current stage.
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
                        Returns:
                            Successful or not.
        """
    def save_as_stage_async(self, url: str) -> typing.Tuple[bool, str]:
        """
        
            Asynchronous version of :func:`omni.usd.UsdContext.save_as_stage_with_callback`. Saves the current stage to a new location.
        
            Args:
                url (str): New location to save the current stage.
        
            Returns:
                (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                    the second one tells the error message if the operation is failed.
            
        """
    def save_as_stage_with_callback(self, url: str, on_finish_fn: typing.Callable[[bool, str, list[str]], None]) -> bool:
        """
                        Saves the current stage to another location asynchronously.
        
                        Args:
                            url (str): New location to save the current stage.
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
        """
    def save_layers(self, new_root_layer_path: str, layer_identifiers: list[str], on_finish_fn: typing.Callable[[bool, str, list[str]], None] = None) -> bool:
        """
                        Saves specified layers (only ones in the local layer stack) synchronously.
        
                        Args:
                            new_root_layer_path (str): New location for root layer if it's to save-as the current stage. If it's empty, it will save specified layers only.
                            layer_identifiers (List[str]): List of layer identifiers to be saved.
                            on_finish_fn (Callable[[bool, str, List[str]], None]): Finish callback that the first param is to tell if the operation is successful, the second one tells the error message if it's faled and
                                the third param is the list of layer identifiers that are saved successfully.
                        Returns:
                            Successful or not.
        """
    def save_layers_async(self, new_root_layer_path: str, layer_identifiers: typing.List[str]) -> typing.Tuple[bool, str]:
        """
        
            Asynchronous version of :func:`omni.usd.UsdContext.save_layers_with_callback`. Saves specified layers.
        
            Args:
                new_root_layer_path (str): New location for root layer if it's to save-as the current stage. If it's empty, it will save specified layers only.
                layer_identifiers (List[str]): List of layer identifiers to be saved.
        
            Returns:
                (bool, str, List[str]): A tuple where the first element tells whether the operation is successful or not, the second one tells the error message if it's faled and
                    the third param is the list of layer identifiers that are saved successfully.
            
        """
    def save_layers_with_callback(self, new_root_layer_path: str, layer_identifiers: list[str], on_finish_fn: typing.Callable[[bool, str, list[str]], None]) -> bool:
        """
                        Saves specified layers (only ones in the local layer stack) asynchronously.
        
                        Args:
                            new_root_layer_path (str): New location for root layer if it's to save-as the current stage. If it's empty, it will save specified layers only.
                            layer_identifiers (List[str]): List of layer identifiers to be saved.
                            on_finish_fn (Callable[[bool, str, List[str]], None]): Finish callback that the first param is to tell if the operation is successful, the second one tells the error message if it's faled and
                                the third param is the list of layer identifiers that are saved successfully.
        """
    def save_render_settings_to_current_stage(self) -> None:
        """
        Saves render settings into the current stage. Render settings will be serialized into the custom layer data of root layer.
        """
    def save_stage(self, on_finish_fn: typing.Callable[[bool, str, list[str]], None] = None) -> bool:
        """
                        Saves the current stage (only layers in the local layer stack) synchronously.
        
                        Args:
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
        
                        Returns:
                            Successful or not.
        """
    def save_stage_async(self) -> typing.Tuple[bool, str]:
        """
        
            Asynchronous version of :func:`omni.usd.UsdContext.save_stage_with_callback`. Saves the current stage.
        
            Returns:
                (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                    the second one tells the error message if the operation is failed.
            
        """
    def save_stage_with_callback(self, on_finish_fn: typing.Callable[[bool, str, list[str]], None]) -> bool:
        """
                        Saves the current stage asynchronously.
        
                        Args:
                            on_finish_fn (Callable[[bool, str], None]): Finish callback that the first param is to tell if the operation is successful, and the second one tells the error message if it's faled.
        """
    def selection_changed_async(self) -> typing.List[str]:
        """
        Wait for selection to be changed. Return a list of newly selected paths.
        """
    def set_pending_edit(self, arg0: bool) -> None:
        """
        Set or clear the stage dirtiness state manually no matter if it has pending edits to save.
        """
    def set_pickable(self, arg0: str, arg1: bool) -> None:
        """
        Sets the pickable state for a prim.
        """
    def set_selection_group(self, groupId: int, path: str) -> None:
        """
        Assigns the prim to specified selection group.
        """
    def set_selection_group_outline_color(self, groupId: int, color: carb._carb.Float4) -> None:
        """
        Sets the outline color of the selection group.
        """
    def set_selection_group_shade_color(self, groupId: int, color: carb._carb.Float4) -> None:
        """
        Sets the shade color of the selection group.
        """
    def set_timeline(self, name: str = '') -> None:
        """
        Sets the timeline for this context.
        """
    def try_cancel_save(self) -> None:
        """
        Try to cancel the saving process. It only take effects when it's called immediately after receiving event StageEventType::eSaving or StageEventType::eSettingsSaving.
        """
class UsdContextInitialLoadSet:
    """
    
            Specifies the initial set of prims to load when opening a UsdStage.
            
    
    Members:
    
      LOAD_ALL : Load all payloads
    
      LOAD_NONE : Unload all payloads
    """
    LOAD_ALL: typing.ClassVar[UsdContextInitialLoadSet]  # value = <UsdContextInitialLoadSet.LOAD_ALL: 0>
    LOAD_NONE: typing.ClassVar[UsdContextInitialLoadSet]  # value = <UsdContextInitialLoadSet.LOAD_NONE: 1>
    __members__: typing.ClassVar[dict[str, UsdContextInitialLoadSet]]  # value = {'LOAD_ALL': <UsdContextInitialLoadSet.LOAD_ALL: 0>, 'LOAD_NONE': <UsdContextInitialLoadSet.LOAD_NONE: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
def add_hydra_engine(name: str, context: UsdContext) -> OpaqueSharedHydraEngineContext:
    ...
def attach_all_hydra_engines(context: UsdContext) -> None:
    ...
def create_context(name: str = '') -> UsdContext:
    """
    Creates a new UsdContext.
    """
def destroy_context(name: str = '') -> bool:
    """
    Destroys specified UsdContext.
    """
def get_context(name: str = '') -> UsdContext:
    """
    Gets UsdContext instance.
    """
def get_context_from_stage_id(stage_id: int) -> UsdContext:
    """
    Finds UsdContext instance with specified stage id.
    """
def get_or_create_hydra_engine(arg0: str, arg1: UsdContext, arg2: EngineCreationConfig) -> OpaqueSharedHydraEngineContext:
    ...
def merge_layers(dst_layer_identifier: str, src_layer_identifier: str, dst_is_stronger_than_src: bool = True, src_layer_offset: float = 0.0, src_layer_scale: float = 1.0) -> bool:
    """
    Merge source layer into target layer according to the strength order.
    """
def merge_prim_spec(dst_layer_identifier: str, src_layer_identifier: str, prim_spec_path: str, dst_is_stronger_than_src: bool = True, target_prim_path: str = '') -> None:
    """
    Merge prim specs between layers.
    """
def release_all_hydra_engines(context: UsdContext = None) -> None:
    ...
def release_hydra_engine(arg0: UsdContext, arg1: OpaqueSharedHydraEngineContext) -> bool:
    ...
def resolve_paths(src_layer_identifier: str, dst_layer_identifier: str, store_relative_path: bool = True, relative_to_src_layer: bool = False, copy_sublayer_offsets: bool = False) -> None:
    """
    Resolve external paths in dst layer against base layer specified by src_layer_identifier.
    """
def resolve_prim_path_references(layer: str, old_prim_path: str, new_prim_path: str) -> None:
    """
                    Resolve all prim path reference to use new path.
                    This is mainly used to remapping prim path reference after structure change of original prim.
    
                    Args:
                        layer (Sdf.Layer): Layer to resolve.
                        old_prim_path (str): Old prim path.
                        new_prim_path (str): New prim path that all old prim path references will be replaced to.
    """
def resolve_prim_paths_references(layer: str, old_prim_paths: list[str], new_prim_paths: list[str]) -> None:
    """
                    Resolve all prim paths reference to use new path.
                    This is mainly used to remapping prim path reference after structure change of original prim.
    
                    Args:
                        layer (Sdf.Layer): Layer to resolve.
                        old_prim_paths (List[str]): Old prim paths.
                            new_prim_paths (list[str]): New prim paths that all old prim paths references will be replaced to.
    """
def shutdown_usd() -> None:
    """
    Internal.
    """
MOTION_RAYTRACING_ENABLED: EngineCreationFlags  # value = <EngineCreationFlags.MOTION_RAYTRACING_ENABLED: 1>
NONE: EngineCreationFlags  # value = <EngineCreationFlags.NONE: 0>
SKIP_ON_WORKER_PROCESS: EngineCreationFlags  # value = <EngineCreationFlags.SKIP_ON_WORKER_PROCESS: 2>
WRITABLE_USD_FILE_EXTS_STR: str = 'usd|usda|usdc|live'
