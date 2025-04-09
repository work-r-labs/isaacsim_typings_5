from __future__ import annotations
import omni.appwindow._appwindow
import omni.gpu_foundation_factory._gpu_foundation_factory
import typing
__all__ = ['IRendererCapture', 'Metadata', 'acquire_renderer_capture_interface', 'convert_raw_bytes_to_list', 'convert_raw_bytes_to_rgba_tuples']
class IRendererCapture:
    """
    Render capture interface.
    """
    def capture_next_frame_rp_resource(self, filepath: str, resource: omni.gpu_foundation_factory._gpu_foundation_factory.RpResource, app_window: omni.appwindow._appwindow.IAppWindow = None, metadata: Metadata = None) -> None:
        """
        Request capture RTX resource manager RpResource and save to a file.
                     Args:
                         filepath (str):
                             The file path where the file is saved to
                         resource (RpResource):
                             requested gpu resources.
                         app_window (omni::kit::IAppWindow):
                             app window. Default to None.
                         metadata (omni.kit.renderer_capture._renderer_capture.Metadata):
                             metadata passed to the capture request. Default to None.
        """
    def capture_next_frame_rp_resource_callback(self, callback: typing.Callable[[capsule, int, int, int, omni.gpu_foundation_factory._gpu_foundation_factory.TextureFormat], None], resource: omni.gpu_foundation_factory._gpu_foundation_factory.RpResource, app_window: omni.appwindow._appwindow.IAppWindow = None, metadata: Metadata = None) -> None:
        """
        Request capture RTX resource manager RpResource and trigger a callback when capture buffer is available.
                    Args:
                        callback (typing.Callable[[capsule, int, int, int, TextureFormat], None]):
                            callback called when capture buffer is available.
                        resource (RpResource):
                            requested gpu resources.
                        app_window (omni::kit::IAppWindow):
                            app window. Default to None.
                        metadata (omni.kit.renderer_capture._renderer_capture.Metadata):
                            metadata passed to the capture request. Default to None.
        """
    def capture_next_frame_rp_resource_list_callback(self, callback: typing.Callable[[list[int], int, int, int, omni.gpu_foundation_factory._gpu_foundation_factory.TextureFormat], None], resource: omni.gpu_foundation_factory._gpu_foundation_factory.RpResource, app_window: omni.appwindow._appwindow.IAppWindow = None, metadata: Metadata = None) -> None:
        """
        Request capture RTX resource manager RpResource and trigger a callback when capture buffer is available.
                    Args:
                        callback (typing.Callable[[typing.List[int], int, int, int, TextureFormat], None]):
                            callback called when capture buffer is available.
                        resource (RpResource):
                            requested gpu resources.
                        app_window (omni::kit::IAppWindow):
                            app window. Default to None.
                        metadata (omni.kit.renderer_capture._renderer_capture.Metadata):
                            metadata passed to the capture request. Default to None.
        """
    def capture_next_frame_rp_resource_to_file(self, filepath: str, resource: omni.gpu_foundation_factory._gpu_foundation_factory.RpResource, app_window: omni.appwindow._appwindow.IAppWindow = None, format_desc: typing.Any = None, metadata: Metadata = None) -> None:
        """
        Request capture RTX resource manager RpResource and save to a file.
        
                    Args:
                        filepath (str):
                            The file path where the file is saved to
                        resource (RpResource):
                            requested gpu resources
                        app_window (omni::kit::IAppWindow):
                            app window. Default to None
                        format_desc (object):
                            a dict of the config of the file, e.g. format, compression etc. Default to None
                        metadata (omni.kit.renderer_capture._renderer_capture.Metadata):
                            metadata passed to the capture request. Default to None.
        """
    def capture_next_frame_swapchain(self, filepath: str, app_window: omni.appwindow._appwindow.IAppWindow = None, metadata: Metadata = None) -> None:
        """
        Request capture swapchain and save to a file.
        
                     Args:
                         filepath (str):
                             The file path where the file is saved to.
                         app_window (omni::kit::IAppWindow):
                             app window. Default to None.
                         metadata (omni.kit.renderer_capture._renderer_capture.Metadata):
                             metadata passed to the capture request. Default to None.
        """
    def capture_next_frame_swapchain_callback(self, callback: typing.Callable[[capsule, int, int, int, omni.gpu_foundation_factory._gpu_foundation_factory.TextureFormat], None], app_window: omni.appwindow._appwindow.IAppWindow = None, metadata: Metadata = None) -> None:
        """
        Request capture swapchain and trigger a callback when capture buffer is available.
                    Args:
                        callback (typing.Callable[[capsule, int, int, int, TextureFormat], None]):
                            callback called when capture buffer is available.
                        app_window (omni::kit::IAppWindow):
                            app window. Default to None.
                        metadata (omni.kit.renderer_capture._renderer_capture.Metadata):
                            metadata passed to the capture request. Default to None.
        """
    def capture_next_frame_swapchain_to_file(self, filepath: str, app_window: omni.appwindow._appwindow.IAppWindow = None, format_desc: typing.Any = None, metadata: Metadata = None) -> None:
        """
        Request capture swapchain and save to a file.
        
                    Args:
                        filepath (str):
                            The file path where the file is saved to
                        app_window (omni::kit::IAppWindow):
                            app window. Default to None
                        format_desc (object):
                            a dict of the config of the file, e.g. format, compression etc. Default to None
                        metadata (omni.kit.renderer_capture._renderer_capture.Metadata):
                            metadata passed to the capture request. Default to None.
        """
    def capture_next_frame_texture(self, filepath: str, texture: omni.gpu_foundation_factory._gpu_foundation_factory.Texture = None, app_window: omni.appwindow._appwindow.IAppWindow = None, metadata: Metadata = None) -> None:
        """
        Request capture texture and save to a file.
        
                     Args:
                         filepath (str):
                             The file path where the file is saved to.
                         texture (carb::graphics::Texture):
                             Captured texture.
                         app_window (omni::kit::IAppWindow):
                             app window. Default to None.
                         metadata (omni.kit.renderer_capture._renderer_capture.Metadata):
                             metadata passed to the capture request. Default to None.
        """
    def capture_next_frame_texture_callback(self, callback: typing.Callable[[capsule, int, int, int, omni.gpu_foundation_factory._gpu_foundation_factory.TextureFormat], None], texture: omni.gpu_foundation_factory._gpu_foundation_factory.Texture = None, app_window: omni.appwindow._appwindow.IAppWindow = None, metadata: Metadata = None) -> None:
        """
        Request capture texture and trigger a callback when capture buffer is available.
        
                    Args:
                        callback (typing.Callable[[typing.List[int], int, int, int, TextureFormat], None]):
                            callback called when capture buffer is available.
                        texture (carb::graphics::Texture):
                            Captured texture.
                        app_window (omni::kit::IAppWindow):
                            app window. Default to None.
                        metadata (omni.kit.renderer_capture._renderer_capture.Metadata):
                            metadata passed to the capture request. Default to None.
        """
    def capture_next_frame_texture_to_file(self, filepath: str, texture: omni.gpu_foundation_factory._gpu_foundation_factory.Texture = None, app_window: omni.appwindow._appwindow.IAppWindow = None, format_desc: typing.Any = None, metadata: Metadata = None) -> None:
        """
        Request capture texture and save to a file.
        
                    Args:
                        filepath (str):
                            The file path where the file is saved to
                        texture (carb::graphics::Texture):
                            Captured texture.
                        app_window (omni::kit::IAppWindow):
                            app window. Default to None
                        format_desc (object):
                            a dict of the config of the file, e.g. format, compression etc. Default to None
                        metadata (omni.kit.renderer_capture._renderer_capture.Metadata):
                            metadata passed to the capture request. Default to None.
        """
    def capture_next_frame_using_render_product(self, viewport_handle: int, filepath: str, render_product: str) -> None:
        """
        Request capture of all resources in render product.
        
                     This is not well supported. Please don't use it.
        """
    def request_callback_memory_ownership(self) -> bool:
        """
        Request memory ownership of a buffer passed into callback. Should be called from within a callback.
        
                     Returns:
                        bool: whether the request is successful.
        """
    def set_capture_sync(self, sync: bool, app_window: omni.appwindow._appwindow.IAppWindow = None) -> bool:
        """
        Set synchronous capture mode.
        
                     Args:
                         sync (bool):
                             Whether to use synchronous capture mode
                         app_window (omni::kit::IAppWindow):
                             app window. Default to None.
                     Returns:
                         bool: previous state of whether to use synchronous capture mode.
        """
    def shutdown(self) -> bool:
        """
        Internal function. Shuts down capture interface.
                    Returns:
                        bool: True.
        """
    def start_frame_updates(self, app_window: omni.appwindow._appwindow.IAppWindow = None) -> bool:
        """
        Starts per frame updates to collect capturing related data during each frame, such as FPS.
        
                     Args:
                         app_window (omni::kit::IAppWindow):
                             app window. Default to None.
                     Returns:
                         bool: whether the app window context is ready.
        """
    def startup(self) -> bool:
        """
        Internal function. Starts up capture interface.
                    Returns:
                        bool: whether the capture interface startups successfully
        """
    def wait_async_capture(self, app_window: omni.appwindow._appwindow.IAppWindow = None) -> None:
        """
        Wait for asynchronous capture to complete.
        
                     Args:
                         app_window (omni::kit::IAppWindow):
                             app window. Default to None.
        """
class Metadata:
    pass
def acquire_renderer_capture_interface(plugin_name: str = None, library_path: str = None) -> ...:
    """
                    Acquire the renderer capture interface, so that it can call its APIs
    
                    Args:
                        plugin_name: The plugin name for binding.
                        library_path: The library path for binding.
                    Return:
                        The renderer capture interface.
    """
def convert_raw_bytes_to_list(arg0: capsule, arg1: int, arg2: int, arg3: int, arg4: omni.gpu_foundation_factory._gpu_foundation_factory.TextureFormat) -> list[int]:
    ...
def convert_raw_bytes_to_rgba_tuples(arg0: capsule, arg1: int, arg2: int, arg3: int, arg4: omni.gpu_foundation_factory._gpu_foundation_factory.TextureFormat) -> list[tuple]:
    ...
