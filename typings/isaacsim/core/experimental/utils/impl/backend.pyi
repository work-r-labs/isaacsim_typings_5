from __future__ import annotations
import _thread
import carb as carb
import contextlib as contextlib
import threading as threading
import typing
__all__: list[str] = ['carb', 'contextlib', 'get_current_backend', 'is_backend_set', 'should_raise_on_fallback', 'should_raise_on_unsupported', 'threading', 'use_backend']
def get_current_backend(supported_backends: list[str], *, raise_on_unsupported: bool | None = None) -> str:
    """
    Get the current backend value if it exists.
    
        Args:
            supported_backends: The list of supported backends.
            raise_on_unsupported: Whether to raise an error if the backend is not supported when requested.
                If set to a value other than ``None``, this parameter has precedence over the context value.
    
        Returns:
            The current backend value or the default value (first supported backend) if no backend is active.
        
    """
def is_backend_set() -> bool:
    """
    Check if a backend is set in the context.
    
        Returns:
            Whether a backend is set in the context.
        
    """
def should_raise_on_fallback() -> bool:
    """
    Check whether an exception should be raised, depending on the context's raise on fallback state.
    
        Returns:
            Whether an exception should be raised on fallback backend.
        
    """
def should_raise_on_unsupported() -> bool:
    """
    Check whether an exception should be raised, depending on the context's raise on unsupported state.
    
        Returns:
            Whether an exception should be raised on unsupported backend.
        
    """
def use_backend(*args, **kwds) -> Generator[None, None, None]:
    """
    Context manager that sets a thread-local backend value.
    
        .. warning::
    
            The :guilabel:`usdrt` and :guilabel:`fabric` backends require Fabric Scene Delegate (FSD) to be enabled.
            FSD can be enabled in *apps/.kit* experience files by setting ``app.useFabricSceneDelegate = true``.
    
        Args:
            backend: The value to set in the context.
            raise_on_unsupported: Whether to raise an exception if the backend is not supported when requested.
            raise_on_fallback: Whether to raise an exception if the backend is supported,
                but a fallback is being used at a particular point in time when requested.
    
        Raises:
            RuntimeError: If the ``usdrt`` or ``fabric`` backend is specified but Fabric Scene Delegate (FSD) is disabled.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.backend as backend_utils
            >>>
            >>> with backend_utils.use_backend("usdrt"):
            ...    # operate on the specified backend
            ...    pass
            >>> # operate on the default backend
        
    """
_context: _thread._local  # value = <_thread._local object>
_fsd_enabled: bool = True
