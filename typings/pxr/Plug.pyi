"""

This package defines facilities for dealing with plugins.
"""
from __future__ import annotations
import pxr.Tf
__all__ = ['Notice', 'Plugin', 'Registry']
class Notice(Boost.Python.instance):
    """
    
    Notifications sent by the Plug module.
    
    """
    class Base(pxr.Tf.Notice):
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class DidRegisterPlugins(Base):
        @staticmethod
        def GetNewPlugins(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Raises an exception
            This class cannot be instantiated from Python
            """
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Plugin(Boost.Python.instance):
    """
    
    Defines an interface to registered plugins.
    
    Plugins are registered using the interfaces in ``PlugRegistry`` .
    
    For each registered plugin, there is an instance of ``PlugPlugin``
    which can be used to load and unload the plugin and to retrieve
    information about the classes implemented by the plugin.
    
    """
    @staticmethod
    def DeclaresType(*args, **kwargs):
        """
        
        DeclaresType(type, includeSubclasses) -> bool
        
        
        Returns true if ``type`` is declared by this plugin.
        
        
        If ``includeSubclasses`` is specified, also returns true if any
        subclasses of ``type`` have been declared.
        
        
        Parameters
        ----------
        type : Type
        
        includeSubclasses : bool
        
        
        """
    @staticmethod
    def FindPluginResource(*args, **kwargs):
        """
        
        FindPluginResource(path, verify) -> str
        
        
        Find a plugin resource by absolute or relative path optionally
        verifying that file exists.
        
        
        If verification fails an empty path is returned. Relative paths are
        relative to the plugin's resource path.
        
        
        Parameters
        ----------
        path : str
        
        verify : bool
        
        
        """
    @staticmethod
    def GetMetadataForType(*args, **kwargs):
        """
        
        GetMetadataForType(type) -> JsObject
        
        
        Returns the metadata sub-dictionary for a particular type.
        
        
        Parameters
        ----------
        type : Type
        
        
        """
    @staticmethod
    def Load(*args, **kwargs):
        """
        
        Load() -> bool
        
        
        Loads the plugin.
        
        
        This is a noop if the plugin is already loaded.
        
        
        
        """
    @staticmethod
    def MakeResourcePath(*args, **kwargs):
        """
        
        MakeResourcePath(path) -> str
        
        
        Build a plugin resource path by returning a given absolute path or
        combining the plugin's resource path with a given relative path.
        
        
        Parameters
        ----------
        path : str
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        
        
        True if this object has not expired.  False otherwise.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        """
        
        
        Equality operator:  x == y
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __lt__(*args, **kwargs):
        """
        
        
        Less than operator: x < y
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        """
        
        
        Non-equality operator: x != y
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
    @property
    def isLoaded(*args, **kwargs):
        """
        type : bool
        
        
        Returns ``true`` if the plugin is currently loaded.
        
        
        Resource plugins always report as loaded.
        """
    @property
    def isPythonModule(*args, **kwargs):
        """
        type : bool
        
        
        Returns ``true`` if the plugin is a python module.
        """
    @property
    def isResource(*args, **kwargs):
        """
        type : bool
        
        
        Returns ``true`` if the plugin is resource-only.
        """
    @property
    def metadata(*args, **kwargs):
        """
        type : JsObject
        
        
        Returns the dictionary containing meta-data for the plugin.
        """
    @property
    def name(*args, **kwargs):
        """
        type : str
        
        
        Returns the plugin's name.
        """
    @property
    def path(*args, **kwargs):
        """
        type : str
        
        
        Returns the plugin's filesystem path.
        """
    @property
    def resourcePath(*args, **kwargs):
        """
        type : str
        
        
        Returns the plugin's resources filesystem path.
        """
class Registry(Boost.Python.instance):
    """
    
    Defines an interface for registering plugins.
    
    PlugRegistry maintains a registry of plug-ins known to the system and
    provides an interface for base classes to load any plug-ins required
    to instantiate a subclass of a given type.
    
    Defining a Base Class API
    =========================
    
    In order to use this facility you will generally provide a module
    which defines the API for a plug-in base class. This API will be
    sufficient for the application or framework to make use of custom
    subclasses that will be written by plug-in developers.
    
    For example, if you have an image processing application, you might
    want to support plug-ins that implement image filters. You can define
    an abstract base class for image filters that declares the API your
    application will require image filters to implement; perhaps something
    simple like C++ Code Example 1 (Doxygen only).
    
    People writing custom filters would write a subclass of ImageFilter
    that overrides the two methods, implementing their own special
    filtering behavior.
    
    Enabling Plug-in Loading for the Base Class
    ===========================================
    
    In order for ImageFilter to be able to load plug-ins that implement
    these custom subclasses, it must be registered with the TfType system.
    
    The ImageFilter base class, as was mentioned earlier, should be made
    available in a module that the application links with. This is done
    so that plug-ins that want to provide ImageFilters can also link with
    the module allowing them to subclass ImageFilter.
    
    Registering Plug-ins
    ====================
    
    A plug-in developer can now write plug-ins with ImageFilter
    subclasses. Plug-ins can be implemented either as native dynamic
    modules (either regular dynamic modules or framework bundles) or
    as Python modules.
    
    Plug-ins must be registered with the registry. All plugins are
    registered via RegisterPlugins() . Plug-in Python modules must be
    directly importable (in other words they must be able to be found in
    Python's module path.) Plugins are registered by providing a path or
    paths to JSON files that describe the location, structure and contents
    of the plugin. The standard name for these files in plugInfo.json.
    
    Typically, the application that hosts plug-ins will locate and
    register plug-ins at startup.
    
    The plug-in facility is lazy. It does not dynamically load code from
    plug-in bundles until that code is required.
    
    plugInfo.json
    =============
    
    A plugInfo.json file has the following structure:
    
    .. code-block:: text
    
      {
          # Comments are allowed and indicated by a hash at the start of a
          # line or after spaces and tabs.  They continue to the end of line.
          # Blank lines are okay, too.
      
          # This is optional.  It may contain any number of strings.
          #   Paths may be absolute or relative.
          #   Paths ending with slash have plugInfo.json appended automatically.
          #   '\\*' may be used anywhere to match any character except slash.
          #   '\\*\\*' may be used anywhere to match any character including slash.
          "Includes": [
              "/absolute/path/to/plugInfo.json",
              "/absolute/path/to/custom.filename",
              "/absolute/path/to/directory/with/plugInfo/",
              "relative/path/to/plugInfo.json",
              "relative/path/to/directory/with/plugInfo/",
              "glob\\*/pa\\*th/\\*to\\*/\\*/plugInfo.json",
              "recursive/pa\\*\\*th/\\*\\*/"
          ],
      
          # This is optional.  It may contain any number of objects.
          "Plugins": [
              {
                  # Type is required and may be "module", "python" or "resource".
                  "Type": "module",
      
                  # Name is required.  It should be the Python module name,
                  # the shared module name, or a unique resource name.
                  "Name": "myplugin",
      
                  # Root is optional.  It defaults to ".".
                  # This gives the path to the plugin as a whole if the plugin
                  # has substructure.  For Python it should be the directory
                  # with the __init__.py file.  The path is usually relative.
                  "Root": ".",
      
                  # LibraryPath is required by Type "module" and unused
                  # otherwise.  It gives the path to the shared module
                  # object, either absolute or relative to Root.
                  "LibraryPath": "libmyplugin.so",
      
                  # ResourcePath is option.  It defaults to ".".
                  # This gives the path to the plugin's resources directory.
                  # The path is either absolute or relative to Root.
                  "ResourcePath": "resources",
      
                  # Info is required.  It's described below.
                  "Info": {
                      # Plugin contents.
                  }
              }
          ]
      }
    
    As a special case, if a plugInfo.json contains an object that doesn't
    have either the"Includes"or"Plugins"keys then it's as if the object
    was in a"Plugins"array.
    
    Advertising a Plug-in's Contents
    ================================
    
    Once the plug-ins are registered, the plug-in facility must also be
    able to tell what they contain. Specifically, it must be able to find
    out what subclasses of what plug-in base classes each plug-in
    contains. Plug-ins must advertise this information through their
    plugInfo.json file in the"Info"key. In the"Info"object there should be
    a key"Types"holding an object.
    
    This"Types"object's keys are names of subclasses and its values are
    yet more objects (the subclass meta-data objects). The meta-data
    objects can contain arbitrary key-value pairs. The plug-in mechanism
    will look for a meta-data key called"displayName"whose value should be
    the display name of the subclass. The plug-in mechanism will look for
    a meta-data key called"bases"whose value should be an array of base
    class type names.
    
    For example, a bundle that contains a subclass of ImageFilter might
    have a plugInfo.json that looks like the following example.
    
    .. code-block:: text
    
      {
          "Types": {
              "MyCustomCoolFilter" : {
                  "bases": ["ImageFilter"],
                  "displayName": "Add Coolness to Image"
                  # other arbitrary metadata for MyCustomCoolFilter here
              }
          }
      }
    
    What this says is that the plug-in contains a type called
    MyCustomCoolFilter which has a base class ImageFilter and that this
    subclass should be called"Add Coolness to Image"in user-visible
    contexts.
    
    In addition to the"displayName"meta-data key which is actually known
    to the plug-in facility, you may put whatever other information you
    want into a class'meta-data dictionary. If your plug-in base class
    wants to define custom keys that it requires all subclasses to
    provide, you can do that. Or, if a plug-in writer wants to define
    their own keys that their code will look for at runtime, that is OK as
    well.
    
    Working with Subclasses of a Plug-in Base Class
    ===============================================
    
    Most code with uses types defined in plug-ins doesn't deal with the
    Plug API directly. Instead, the TfType interface is used to lookup
    types and to manufacture instances. The TfType interface will take
    care to load any required plugins.
    
    To wrap up our example, the application that wants to actually use
    ImageFilter plug-ins would probably do a couple of things. First, it
    would get a list of available ImageFilters to present to the user.
    This could be accomplished as shown in Python Code Example 2 (Doxygen
    only).
    
    Then, when the user picks a filter from the list, it would manufacture
    and instance of the filter as shown in Python Code Example 3 (Doxygen
    only).
    
    As was mentioned earlier, this plug-in facility tries to be as lazy as
    possible about loading the code associated with plug-ins. To that end,
    loading of a plugin will be deferred until an instance of a type is
    manufactured which requires the plugin.
    
    Multiple Subclasses of Multiple Plug-in Base Classes
    ====================================================
    
    It is possible for a bundle to implement multiple subclasses for a
    plug-in base class if desired. If you want to package half a dozen
    ImageFilter subclasses in one bundle, that will work fine. All must be
    declared in the plugInfo.json.
    
    It is possible for there to be multiple classes in your application or
    framework that are plug-in base classes. Plug-ins that implement
    subclasses of any of these base classes can all coexist. And, it is
    possible to have subclasses of multiple plug-in base classes in the
    same bundle.
    
    When putting multiple subclasses (of the same or different base
    classes) in a bundle, keep in mind that dynamic loading happens for
    the whole bundle the first time any subclass is needed, the whole
    bundle will be loaded. But this is generally not a big concern.
    
    For example, say the example application also has a plug-in base
    class"ImageCodec"that allows people to add support for reading and
    writing other image formats. Imagine that you want to supply a plug-in
    that has two codecs and a filter all in a single plug-in. Your
    plugInfo.json"Info"object might look something like this example.
    
    .. code-block:: text
    
      {
          "Types": {
              "MyTIFFCodec": {
                  "bases": ["ImageCodec"],
                  "displayName": "TIFF Image"
              },
              "MyJPEGCodec": {
                  "bases": ["ImageCodec"],
                  "displayName": "JPEG Image"
              },
              "MyCustomCoolFilter" : {
                  "bases": ["ImageFilter"],
                  "displayName": "Add Coolness to Image"
              }
          }
      }
    
    Dependencies on Other Plug-ins
    ==============================
    
    If you write a plug-in that has dependencies on another plug-in that
    you cannot (or do not want to) link against statically, you can
    declare the dependencies in your plug-in's plugInfo.json. A plug-in
    declares dependencies on other classes with a PluginDependencies key
    whose value is a dictionary. The keys of the dictionary are plug-in
    base class names and the values are arrays of subclass names.
    
    The following example contains an example of a plug-in that depends on
    two classes from the plug-in in the previous example.
    
    .. code-block:: text
    
      {
          "Types": {
              "UltraCoolFilter": {
                  "bases": ["MyCustomCoolFilter"],
                  "displayName": "Add Unbelievable Coolness to Image"
                  # A subclass of MyCustomCoolFilter that also uses MyTIFFCodec
              }
          },
          "PluginDependencies": {
              "ImageFilter": ["MyCustomCoolFilter"],
              "ImageCodec": ["MyTIFFCodec"]
          }
      }
    
    The ImageFilter provided by the plug-in in this example depends on the
    other ImageFilter MyCoolImageFilter and the ImageCodec MyTIFFCodec.
    Before loading this plug-in, the plug-in facility will ensure that
    those two classes are present, loading the plug-in that contains them
    if needed.
    
    """
    @staticmethod
    def FindDerivedTypeByName(*args, **kwargs):
        """
        
        **classmethod** FindDerivedTypeByName(base, typeName) -> Type
        
        
        Retrieve the ``TfType`` that derives from ``base`` and has the given
        alias or type name ``typeName`` .
        
        
        See the documentation for ``TfType::FindDerivedByName`` for more
        information. Use this function if you expect that the derived type may
        be provided by a plugin. Calling this function will incur plugin
        discovery (but not loading) if plugin discovery has not yet occurred.
        
        Note that additional plugins may be registered during program runtime.
        
        Plug-In Discovery & Registration
        
        
        Parameters
        ----------
        base : Type
        
        typeName : str
        
        
        
        ----------------------------------------------------------------------
        
        FindDerivedTypeByName(typeName) -> Type
        
        
        Retrieve the ``TfType`` that derives from ``Base`` and has the given
        alias or type name ``typeName`` .
        
        
        See the documentation for ``TfType::FindDerivedByName`` for more
        information. Use this function if you expect that the derived type may
        be provided by a plugin. Calling this function will incur plugin
        discovery (but not loading) if plugin discovery has not yet occurred.
        
        Note that additional plugins may be registered during program runtime.
        
        Plug-In Discovery & Registration
        
        
        Parameters
        ----------
        typeName : str
        
        
        """
    @staticmethod
    def FindTypeByName(*args, **kwargs):
        """
        
        **classmethod** FindTypeByName(typeName) -> Type
        
        
        Retrieve the ``TfType`` corresponding to the given ``name`` .
        
        
        See the documentation for ``TfType::FindByName`` for more information.
        Use this function if you expect that ``name`` may name a type provided
        by a plugin. Calling this function will incur plugin discovery (but
        not loading) if plugin discovery has not yet occurred.
        
        Note that additional plugins may be registered during program runtime.
        
        Plug-In Discovery & Registration
        
        
        Parameters
        ----------
        typeName : str
        
        
        """
    @staticmethod
    def GetAllDerivedTypes(*args, **kwargs):
        """
        
        **classmethod** GetAllDerivedTypes(base, result) -> None
        
        
        Return the set of all types derived (directly or indirectly) from
        *base*.
        
        
        Use this function if you expect that plugins may provide types derived
        from *base*. Otherwise, use *TfType::GetAllDerivedTypes*.
        
        Note that additional plugins may be registered during program runtime.
        
        Plug-In Discovery & Registration
        
        
        Parameters
        ----------
        base : Type
        
        result : set[Type]
        
        
        
        ----------------------------------------------------------------------
        
        GetAllDerivedTypes(result) -> None
        
        
        Return the set of all types derived (directly or indirectly) from
        *Base*.
        
        
        Use this function if you expect that plugins may provide types derived
        from *base*. Otherwise, use *TfType::GetAllDerivedTypes*.
        
        Note that additional plugins may be registered during program runtime.
        
        Plug-In Discovery & Registration
        
        
        Parameters
        ----------
        result : set[Type]
        
        
        """
    @staticmethod
    def GetAllPlugins(*args, **kwargs):
        """
        
        GetAllPlugins() -> list[Plugin]
        
        
        Returns all registered plug-ins.
        
        
        Note that additional plugins may be registered during program runtime.
        
        Plug-In Discovery & Registration
        
        
        
        """
    @staticmethod
    def GetDirectlyDerivedTypes(*args, **kwargs):
        """
        
        **classmethod** GetDirectlyDerivedTypes(base) -> list[Type]
        
        
        Return a vector of types derived directly from *base*.
        
        
        Use this function if you expect that plugins may provide types derived
        from *base*. Otherwise, use *TfType::GetDirectlyDerivedTypes*.
        
        
        Parameters
        ----------
        base : Type
        
        
        """
    @staticmethod
    def GetPluginForType(*args, **kwargs):
        """
        
        GetPluginForType(t) -> Plugin
        
        
        Returns the plug-in for the given type, or a null pointer if there is
        no registered plug-in.
        
        
        Parameters
        ----------
        t : Type
        
        
        """
    @staticmethod
    def GetPluginWithName(*args, **kwargs):
        """
        
        GetPluginWithName(name) -> Plugin
        
        
        Returns a plugin with the specified module name.
        
        
        Note that additional plugins may be registered during program runtime.
        
        Plug-In Discovery & Registration
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetStringFromPluginMetaData(*args, **kwargs):
        """
        
        GetStringFromPluginMetaData(type, key) -> str
        
        
        Looks for a string associated with *type* and *key* and returns it, or
        an empty string if *type* or *key* are not found.
        
        
        Parameters
        ----------
        type : Type
        
        key : str
        
        
        """
    @staticmethod
    def RegisterPlugins(*args, **kwargs):
        """
        
        RegisterPlugins(pathToPlugInfo) -> list[Plugin]
        
        
        Registers all plug-ins discovered at *pathToPlugInfo*.
        
        
        Sends PlugNotice::DidRegisterPlugins with any newly registered
        plugins.
        
        
        Parameters
        ----------
        pathToPlugInfo : str
        
        
        
        ----------------------------------------------------------------------
        
        RegisterPlugins(pathsToPlugInfo) -> list[Plugin]
        
        
        Registers all plug-ins discovered in any of *pathsToPlugInfo*.
        
        
        Sends PlugNotice::DidRegisterPlugins with any newly registered
        plugins.
        
        
        Parameters
        ----------
        pathsToPlugInfo : list[str]
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        
        
        True if this object has not expired.  False otherwise.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        """
        
        
        Equality operator:  x == y
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : Registry
        
        
        
        ----------------------------------------------------------------------
        
        __init__() -> PLUG_LOCAL
        
        
        
        """
    @staticmethod
    def __lt__(*args, **kwargs):
        """
        
        
        Less than operator: x < y
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        """
        
        
        Non-equality operator: x != y
        """
    @staticmethod
    def __new__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
class _TestPlugBase1(Boost.Python.instance):
    @staticmethod
    def GetTypeName(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        
        
        True if this object has not expired.  False otherwise.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        """
        
        
        Equality operator:  x == y
        """
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        """
        
        
        Less than operator: x < y
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        """
        
        
        Non-equality operator: x != y
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
class _TestPlugBase2(Boost.Python.instance):
    @staticmethod
    def GetTypeName(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        
        
        True if this object has not expired.  False otherwise.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        """
        
        
        Equality operator:  x == y
        """
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        """
        
        
        Less than operator: x < y
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        """
        
        
        Non-equality operator: x != y
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
class _TestPlugBase3(Boost.Python.instance):
    @staticmethod
    def GetTypeName(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        
        
        True if this object has not expired.  False otherwise.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        """
        
        
        Equality operator:  x == y
        """
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        """
        
        
        Less than operator: x < y
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        """
        
        
        Non-equality operator: x != y
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
class _TestPlugBase4(Boost.Python.instance):
    @staticmethod
    def GetTypeName(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        
        
        True if this object has not expired.  False otherwise.
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        """
        
        
        Equality operator:  x == y
        """
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
        """
        
        
        Less than operator: x < y
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        """
        
        
        Non-equality operator: x != y
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def expired(*args, **kwargs):
        """
        True if this object has expired, False otherwise.
        """
__MFB_FULL_PACKAGE_NAME: str = 'plug'
