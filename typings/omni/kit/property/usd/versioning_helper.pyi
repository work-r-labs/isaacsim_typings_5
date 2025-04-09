from __future__ import annotations
import asyncio as asyncio
import omni as omni
import typing
__all__: list = ['VersioningHelper']
class VersioningHelper:
    server_cache: typing.ClassVar[dict] = {}
    @staticmethod
    def check_server_checkpoint_support(server: str, on_complete: callable):
        ...
    @staticmethod
    def extract_server_from_url(url):
        ...
    @staticmethod
    def is_versioning_enabled():
        ...
