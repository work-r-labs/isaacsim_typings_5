from __future__ import annotations
import carb as carb
import inspect as inspect
__all__ = ['ViewportManipulator', 'carb', 'inspect']
class ViewportManipulator:
    """
    
        ViewportManipulator is a generic wrapper class on top of normal Manipulator Object. It contains all "instances" of the
        Manipulators exist in each Viewports.
    
        When setting an attribute to the ViewportManipulator Object, it forwards the value to all instances.
    
        Do NOT initialize ViewportManipulator directly. Instead using ManipulatorFactory.create_manipulator(...) instead.
        It adds the functionality to automatically track viewport and create or destory "instance" of Manipulator into
        ViewportManipulator.
        
    """
    def __init__(self, manipulator_class: typing.Type, **kwargs):
        ...
    def __setattr__(self, name, value):
        ...
    def add_instance(self, instance):
        ...
    def clear_all_instances(self):
        ...
    def get_all_instances(self):
        ...
    @property
    def manipulator_class(self):
        ...
