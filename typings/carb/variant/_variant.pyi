from __future__ import annotations
__all__ = ['IVariant', 'acquire_variant_interface']
class IVariant:
    pass
def acquire_variant_interface(plugin_name: str = None, library_path: str = None) -> IVariant:
    ...
