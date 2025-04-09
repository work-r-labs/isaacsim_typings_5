from __future__ import annotations
from isaacsim.core.api.scenes.scene import Scene
from isaacsim.core.api.tasks.base_task import BaseTask
import isaacsim.core.utils.types
from isaacsim.core.utils.types import DataFrame
import json as json
__all__ = ['BaseTask', 'DataFrame', 'DataLogger', 'Scene', 'json']
class DataLogger:
    """
    This class takes care of collecting data as well as reading already saved data in order to replay it for instance.
    """
    def __init__(self) -> None:
        ...
    def add_data(self, data: dict, current_time_step: float, current_time: float) -> None:
        """
        Adds data to the log
        
                Args:
                    data (dict): Dictionary representing the data to be logged at this time index.
                    current_time_step (float): time step corresponding to the data collected.
                    current_time (float): time in seconds corresponding to the data collected.
                
        """
    def add_data_frame_logging_func(self, func: typing.Callable[[typing.List[isaacsim.core.api.tasks.base_task.BaseTask], isaacsim.core.api.scenes.scene.Scene], typing.Dict]) -> None:
        """
        
        
                Args:
                    func (Callable[[list[BaseTask], Scene], None]): function to be called at every step when the logger is started.
                                                                    should follow:
        
                                                                    def dummy_data_collection_fn(tasks, scene):
                                                                        return {"data 1": [data]}
                
        """
    def get_data_frame(self, data_frame_index: int) -> isaacsim.core.utils.types.DataFrame:
        """
        
        
                Args:
                    data_frame_index (int): index of the data frame to retrieve.
        
                Returns:
                    DataFrame: Data Frame collected/ retrieved at the specified data frame index.
                
        """
    def get_num_of_data_frames(self) -> int:
        """
        
        
                Returns:
                    int: the number of data frames collected/ retrieved in the data logger.
                
        """
    def is_started(self) -> bool:
        """
        
                Returns:
                    bool: True if data collection is started/ resumed. False otherwise.
                
        """
    def load(self, log_path: str) -> None:
        """
        Loads data from a json file to read back a previous saved data or to resume recording data from another time step.
        
                Args:
                    log_path (str): path of the json file to be used to load the data.
                
        """
    def pause(self) -> None:
        """
        Pauses data collection.
        """
    def reset(self) -> None:
        """
        Clears the data in the logger.
        """
    def save(self, log_path: str) -> None:
        """
        
                Saves the current data in the logger to a json file
        
                Args:
                    log_path (str): path of the json file to be used to save the data.
                
        """
    def start(self) -> None:
        """
        Resumes/ starts data collection.
        """
