from __future__ import annotations
import dataclasses
from dataclasses import dataclass
import omni.kit.widget.filebrowser.model
from omni.kit.widget.filebrowser.model import FileBrowserModel
import typing
__all__: list = ['CollectionData']
class CollectionData:
    """
    
        CollectionData holds data and callbacks used to contruct a registered collection type with the content browser.
            identifier:         Key identifier for the collection type
            title:              Title to display for the collection type in the content browser tree view
            path_to_icon:       Path to the (svg) icon used in the content browser tree view for the registered collection type
            model:              Data model inheriting FileBrowserModel for the collection
            populate_fn:        Callback function that populates the model with pre-existing content items
        
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'identifier': Field(name='identifier',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'title': Field(name='title',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'path_to_icon': Field(name='path_to_icon',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'model': Field(name='model',type=<class 'omni.kit.widget.filebrowser.model.FileBrowserModel'>,default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'populate_fn': Field(name='populate_fn',type=typing.Callable[[], NoneType],default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('identifier', 'title', 'path_to_icon', 'model', 'populate_fn')
    def __eq__(self, other):
        ...
    def __init__(self, identifier: str, title: str, path_to_icon: str, model: omni.kit.widget.filebrowser.model.FileBrowserModel, populate_fn: typing.Callable[[], NoneType]) -> None:
        ...
    def __repr__(self):
        ...
