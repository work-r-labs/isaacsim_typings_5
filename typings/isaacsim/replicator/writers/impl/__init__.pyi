"""
Import the implementation modules that will be externally visible.

The extension object must be visible so that this module properly starts up and shuts down.
The Python bindings are all imported so that they can be used in the omni.graph.examples.cpp import space.
Everything else is explicitly imported for visibility in the omni.graph.examples.cpp import space.
"""
from __future__ import annotations
from isaacsim.replicator.writers.impl.extension import Extension
from . import extension
__all__ = ['Extension', 'extension']
