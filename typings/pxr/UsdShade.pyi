from __future__ import annotations
import pxr.Usd
import typing
__all__ = ['AttributeType', 'ConnectableAPI', 'ConnectionModification', 'ConnectionSourceInfo', 'CoordSysAPI', 'Input', 'Material', 'MaterialBindingAPI', 'NodeDefAPI', 'NodeGraph', 'Output', 'Shader', 'ShaderDefParserPlugin', 'ShaderDefUtils', 'Tokens', 'Utils']
class AttributeType(Boost.Python.enum):
    Input: typing.ClassVar[AttributeType]  # value = pxr.UsdShade.AttributeType.Input
    Invalid: typing.ClassVar[AttributeType]  # value = pxr.UsdShade.AttributeType.Invalid
    Output: typing.ClassVar[AttributeType]  # value = pxr.UsdShade.AttributeType.Output
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'Invalid': pxr.UsdShade.AttributeType.Invalid, 'Input': pxr.UsdShade.AttributeType.Input, 'Output': pxr.UsdShade.AttributeType.Output}
    values: typing.ClassVar[dict]  # value = {0: pxr.UsdShade.AttributeType.Invalid, 1: pxr.UsdShade.AttributeType.Input, 2: pxr.UsdShade.AttributeType.Output}
class ConnectableAPI(pxr.Usd.APISchemaBase):
    """
    
    UsdShadeConnectableAPI is an API schema that provides a common
    interface for creating outputs and making connections between shading
    parameters and outputs. The interface is common to all UsdShade
    schemas that support Inputs and Outputs, which currently includes
    UsdShadeShader, UsdShadeNodeGraph, and UsdShadeMaterial.
    
    One can construct a UsdShadeConnectableAPI directly from a UsdPrim, or
    from objects of any of the schema classes listed above. If it seems
    onerous to need to construct a secondary schema object to interact
    with Inputs and Outputs, keep in mind that any function whose purpose
    is either to walk material/shader networks via their connections, or
    to create such networks, can typically be written entirely in terms of
    UsdShadeConnectableAPI objects, without needing to care what the
    underlying prim type is.
    
    Additionally, the most common UsdShadeConnectableAPI behaviors
    (creating Inputs and Outputs, and making connections) are wrapped as
    convenience methods on the prim schema classes (creation) and
    UsdShadeInput and UsdShadeOutput.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CanConnect(*args, **kwargs):
        """
        
        **classmethod** CanConnect(input, source) -> bool
        
        
        Determines whether the given input can be connected to the given
        source attribute, which can be an input or an output.
        
        
        The result depends on the"connectability"of the input and the source
        attributes. Depending on the prim type, this may require the plugin
        that defines connectability behavior for that prim type be loaded.
        
        UsdShadeInput::SetConnectability
        
        UsdShadeInput::GetConnectability
        
        
        Parameters
        ----------
        input : Input
        
        source : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        CanConnect(input, sourceInput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        sourceInput : Input
        
        
        
        ----------------------------------------------------------------------
        
        CanConnect(input, sourceOutput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        sourceOutput : Output
        
        
        
        ----------------------------------------------------------------------
        
        CanConnect(output, source) -> bool
        
        
        Determines whether the given output can be connected to the given
        source attribute, which can be an input or an output.
        
        
        An output is considered to be connectable only if it belongs to a
        node-graph. Shader outputs are not connectable.
        
        ``source`` is an optional argument. If a valid UsdAttribute is
        supplied for it, this method will return true only if the source
        attribute is owned by a descendant of the node-graph owning the
        output.
        
        
        Parameters
        ----------
        output : Output
        
        source : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        CanConnect(output, sourceInput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        sourceInput : Input
        
        
        
        ----------------------------------------------------------------------
        
        CanConnect(output, sourceOutput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        sourceOutput : Output
        
        
        """
    @staticmethod
    def ClearSource(*args, **kwargs):
        """
        
        **classmethod** ClearSource(shadingAttr) -> bool
        
        
        Deprecated
        
        This is the older version that only referenced a single source. Please
        use ClearSources instead.
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        ClearSource(input) -> bool
        
        
        Deprecated
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        
        
        ----------------------------------------------------------------------
        
        ClearSource(output) -> bool
        
        
        Deprecated
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        
        """
    @staticmethod
    def ClearSources(*args, **kwargs):
        """
        
        **classmethod** ClearSources(shadingAttr) -> bool
        
        
        Clears sources for this shading attribute in the current
        UsdEditTarget.
        
        
        Most of the time, what you probably want is DisconnectSource() rather
        than this function.
        
        DisconnectSource()
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        ClearSources(input) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        
        
        ----------------------------------------------------------------------
        
        ClearSources(output) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        
        """
    @staticmethod
    def ConnectToSource(*args, **kwargs):
        """
        
        **classmethod** ConnectToSource(shadingAttr, source, mod) -> bool
        
        
        Authors a connection for a given shading attribute ``shadingAttr`` .
        
        
        ``shadingAttr`` can represent a parameter, an input or an output.
        ``source`` is a struct that describes the upstream source attribute
        with all the information necessary to make a connection. See the
        documentation for UsdShadeConnectionSourceInfo. ``mod`` describes the
        operation that should be applied to the list of connections. By
        default the new connection will replace any existing connections, but
        it can add to the list of connections to represent multiple input
        connections.
        
        ``true`` if a connection was created successfully. ``false`` if
        ``shadingAttr`` or ``source`` is invalid.
        
        This method does not verify the connectability of the shading
        attribute to the source. Clients must invoke CanConnect() themselves
        to ensure compatibility.
        
        The source shading attribute is created if it doesn't exist already.
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        source : ConnectionSourceInfo
        
        mod : ConnectionModification
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(input, source, mod) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        source : ConnectionSourceInfo
        
        mod : ConnectionModification
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(output, source, mod) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        source : ConnectionSourceInfo
        
        mod : ConnectionModification
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(shadingAttr, source, sourceName, sourceType, typeName) -> bool
        
        
        Deprecated
        
        Please use the versions that take a UsdShadeConnectionSourceInfo to
        describe the upstream source This is an overloaded member function,
        provided for convenience. It differs from the above function only in
        what argument(s) it accepts.
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        source : ConnectableAPI
        
        sourceName : str
        
        sourceType : AttributeType
        
        typeName : ValueTypeName
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(input, source, sourceName, sourceType, typeName) -> bool
        
        
        Deprecated
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        source : ConnectableAPI
        
        sourceName : str
        
        sourceType : AttributeType
        
        typeName : ValueTypeName
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(output, source, sourceName, sourceType, typeName) -> bool
        
        
        Deprecated
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        source : ConnectableAPI
        
        sourceName : str
        
        sourceType : AttributeType
        
        typeName : ValueTypeName
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(shadingAttr, sourcePath) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        Connect the given shading attribute to the source at path,
        ``sourcePath`` .
        
        
        ``sourcePath`` should be the fully namespaced property path.
        
        This overload is provided for convenience, for use in contexts where
        the prim types are unknown or unavailable.
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        sourcePath : Path
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(input, sourcePath) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        sourcePath : Path
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(output, sourcePath) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        sourcePath : Path
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(shadingAttr, sourceInput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        Connect the given shading attribute to the given source input.
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        sourceInput : Input
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(input, sourceInput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        sourceInput : Input
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(output, sourceInput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        sourceInput : Input
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(shadingAttr, sourceOutput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        Connect the given shading attribute to the given source output.
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        sourceOutput : Output
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(input, sourceOutput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        sourceOutput : Output
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(output, sourceOutput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        sourceOutput : Output
        
        
        """
    @staticmethod
    def CreateInput(*args, **kwargs):
        """
        
        CreateInput(name, typeName) -> Input
        
        
        Create an input which can both have a value and be connected.
        
        
        The attribute representing the input is created in
        the"inputs:"namespace.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def CreateOutput(*args, **kwargs):
        """
        
        CreateOutput(name, typeName) -> Output
        
        
        Create an output, which represents and externally computed, typed
        value.
        
        
        Outputs on node-graphs can be connected.
        
        The attribute representing an output is created in
        the"outputs:"namespace.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def DisconnectSource(*args, **kwargs):
        """
        
        **classmethod** DisconnectSource(shadingAttr, sourceAttr) -> bool
        
        
        Disconnect source for this shading attribute.
        
        
        If ``sourceAttr`` is valid it will disconnect the connection to this
        upstream attribute. Otherwise it will disconnect all connections by
        authoring an empty list of connections for the attribute
        ``shadingAttr`` .
        
        This may author more scene description than you might expect - we
        define the behavior of disconnect to be that, even if a shading
        attribute becomes connected in a weaker layer than the current
        UsdEditTarget, the attribute will *still* be disconnected in the
        composition, therefore we must"block"it in the current UsdEditTarget.
        
        ConnectToSource() .
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        sourceAttr : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        DisconnectSource(input, sourceAttr) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        sourceAttr : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        DisconnectSource(output, sourceAttr) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        sourceAttr : Attribute
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> ConnectableAPI
        
        
        Return a UsdShadeConnectableAPI holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdShadeConnectableAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetConnectedSource(*args, **kwargs):
        """
        
        **classmethod** GetConnectedSource(shadingAttr, source, sourceName, sourceType) -> bool
        
        
        Deprecated
        
        Shading attributes can have multiple connections and so using
        GetConnectedSources is needed in general
        
        Finds the source of a connection for the given shading attribute.
        
        ``shadingAttr`` is the shading attribute whose connection we want to
        interrogate. ``source`` is an output parameter which will be set to
        the source connectable prim. ``sourceName`` will be set to the name of
        the source shading attribute, which may be an input or an output, as
        specified by ``sourceType`` ``sourceType`` will have the type of the
        source shading attribute, i.e. whether it is an ``Input`` or
        ``Output``
        
        ``true`` if the shading attribute is connected to a valid, defined
        source attribute. ``false`` if the shading attribute is not connected
        to a single, defined source attribute.
        
        Previously this method would silently return false for multiple
        connections. We are changing the behavior of this method to return the
        result for the first connection and issue a TfWarn about it. We want
        to encourage clients to use GetConnectedSources going forward.
        
        The python wrapping for this method returns a (source, sourceName,
        sourceType) tuple if the parameter is connected, else ``None``
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        source : ConnectableAPI
        
        sourceName : str
        
        sourceType : AttributeType
        
        
        
        ----------------------------------------------------------------------
        
        GetConnectedSource(input, source, sourceName, sourceType) -> bool
        
        
        Deprecated
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        source : ConnectableAPI
        
        sourceName : str
        
        sourceType : AttributeType
        
        
        
        ----------------------------------------------------------------------
        
        GetConnectedSource(output, source, sourceName, sourceType) -> bool
        
        
        Deprecated
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        source : ConnectableAPI
        
        sourceName : str
        
        sourceType : AttributeType
        
        
        """
    @staticmethod
    def GetConnectedSources(*args, **kwargs):
        """
        
        **classmethod** GetConnectedSources(shadingAttr, invalidSourcePaths) -> list[UsdShadeSourceInfo]
        
        
        Finds the valid sources of connections for the given shading
        attribute.
        
        
        ``shadingAttr`` is the shading attribute whose connections we want to
        interrogate. ``invalidSourcePaths`` is an optional output parameter to
        collect the invalid source paths that have not been reported in the
        returned vector.
        
        Returns a vector of ``UsdShadeConnectionSourceInfo`` structs with
        information about each upsteam attribute. If the vector is empty,
        there have been no connections.
        
        A valid connection requires the existence of the source attribute and
        also requires that the source prim is UsdShadeConnectableAPI
        compatible.
        
        The python wrapping returns a tuple with the valid connections first,
        followed by the invalid source paths.
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        invalidSourcePaths : list[Path]
        
        
        
        ----------------------------------------------------------------------
        
        GetConnectedSources(input, invalidSourcePaths) -> list[UsdShadeSourceInfo]
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        invalidSourcePaths : list[Path]
        
        
        
        ----------------------------------------------------------------------
        
        GetConnectedSources(output, invalidSourcePaths) -> list[UsdShadeSourceInfo]
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        invalidSourcePaths : list[Path]
        
        
        """
    @staticmethod
    def GetInput(*args, **kwargs):
        """
        
        GetInput(name) -> Input
        
        
        Return the requested input if it exists.
        
        
        ``name`` is the unnamespaced base name.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetInputs(*args, **kwargs):
        """
        
        GetInputs(onlyAuthored) -> list[Input]
        
        
        Returns all inputs on the connectable prim (i.e.
        
        
        shader or node-graph). Inputs are represented by attributes in
        the"inputs:"namespace. If ``onlyAuthored`` is true (the default), then
        only return authored attributes; otherwise, this also returns un-
        authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
        """
    @staticmethod
    def GetOutput(*args, **kwargs):
        """
        
        GetOutput(name) -> Output
        
        
        Return the requested output if it exists.
        
        
        ``name`` is the unnamespaced base name.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetOutputs(*args, **kwargs):
        """
        
        GetOutputs(onlyAuthored) -> list[Output]
        
        
        Returns all outputs on the connectable prim (i.e.
        
        
        shader or node-graph). Outputs are represented by attributes in
        the"outputs:"namespace. If ``onlyAuthored`` is true (the default),
        then only return authored attributes; otherwise, this also returns un-
        authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
        """
    @staticmethod
    def GetRawConnectedSourcePaths(*args, **kwargs):
        """
        
        **classmethod** GetRawConnectedSourcePaths(shadingAttr, sourcePaths) -> bool
        
        
        Deprecated
        
        Please us GetConnectedSources to retrieve multiple connections
        
        Returns the"raw"(authored) connected source paths for the given
        shading attribute.
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        sourcePaths : list[Path]
        
        
        
        ----------------------------------------------------------------------
        
        GetRawConnectedSourcePaths(input, sourcePaths) -> bool
        
        
        Deprecated
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        sourcePaths : list[Path]
        
        
        
        ----------------------------------------------------------------------
        
        GetRawConnectedSourcePaths(output, sourcePaths) -> bool
        
        
        Deprecated
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        sourcePaths : list[Path]
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def HasConnectableAPI(*args, **kwargs):
        """
        
        **classmethod** HasConnectableAPI(schemaType) -> bool
        
        
        Return true if the ``schemaType`` has a valid connectableAPIBehavior
        registered, false otherwise.
        
        
        To check if a prim's connectableAPI has a behavior defined, use
        UsdSchemaBase::operator bool() .
        
        
        Parameters
        ----------
        schemaType : Type
        
        
        
        ----------------------------------------------------------------------
        
        HasConnectableAPI() -> bool
        
        
        Return true if the schema type ``T`` has a connectableAPIBehavior
        registered, false otherwise.
        
        
        
        """
    @staticmethod
    def HasConnectedSource(*args, **kwargs):
        """
        
        **classmethod** HasConnectedSource(shadingAttr) -> bool
        
        
        Returns true if and only if the shading attribute is currently
        connected to at least one valid (defined) source.
        
        
        If you will be calling GetConnectedSources() afterwards anyways, it
        will be *much* faster to instead check if the returned vector is
        empty:
        
        .. code-block:: text
        
          UsdShadeSourceInfoVector connections =
              UsdShadeConnectableAPI::GetConnectedSources(attribute);
          if (!connections.empty()){
               // process connected attribute
          } else {
               // process unconnected attribute
          }
        
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        HasConnectedSource(input) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        
        
        ----------------------------------------------------------------------
        
        HasConnectedSource(output) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        
        """
    @staticmethod
    def IsContainer(*args, **kwargs):
        """
        
        IsContainer() -> bool
        
        
        Returns true if the prim is a container.
        
        
        The underlying prim type may provide runtime behavior that defines
        whether it is a container.
        
        
        
        """
    @staticmethod
    def IsSourceConnectionFromBaseMaterial(*args, **kwargs):
        """
        
        **classmethod** IsSourceConnectionFromBaseMaterial(shadingAttr) -> bool
        
        
        Returns true if the connection to the given shading attribute's
        source, as returned by UsdShadeConnectableAPI::GetConnectedSource() ,
        is authored across a specializes arc, which is used to denote a base
        material.
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        IsSourceConnectionFromBaseMaterial(input) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        input : Input
        
        
        
        ----------------------------------------------------------------------
        
        IsSourceConnectionFromBaseMaterial(output) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        
        """
    @staticmethod
    def RequiresEncapsulation(*args, **kwargs):
        """
        
        RequiresEncapsulation() -> bool
        
        
        Returns true if container encapsulation rules should be respected when
        evaluating connectibility behavior, false otherwise.
        
        
        The underlying prim type may provide runtime behavior that defines if
        encapsulation rules are respected or not.
        
        
        
        """
    @staticmethod
    def SetConnectedSources(*args, **kwargs):
        """
        
        **classmethod** SetConnectedSources(shadingAttr, sourceInfos) -> bool
        
        
        Authors a list of connections for a given shading attribute
        ``shadingAttr`` .
        
        
        ``shadingAttr`` can represent a parameter, an input or an output.
        ``sourceInfos`` is a vector of structs that describes the upstream
        source attributes with all the information necessary to make all the
        connections. See the documentation for UsdShadeConnectionSourceInfo.
        
        ``true`` if all connection were created successfully. ``false`` if the
        ``shadingAttr`` or one of the sources are invalid.
        
        A valid connection is one that has a valid
        ``UsdShadeConnectionSourceInfo`` , which requires the existence of the
        upstream source prim. It does not require the existence of the source
        attribute as it will be create if necessary.
        
        
        Parameters
        ----------
        shadingAttr : Attribute
        
        sourceInfos : list[ConnectionSourceInfo]
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdShadeConnectableAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdShadeConnectableAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdShadeConnectableAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdShadeConnectableAPI (schemaObj.GetPrim()),
        as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class ConnectionModification(Boost.Python.enum):
    Append: typing.ClassVar[ConnectionModification]  # value = pxr.UsdShade.ConnectionModification.Append
    Prepend: typing.ClassVar[ConnectionModification]  # value = pxr.UsdShade.ConnectionModification.Prepend
    Replace: typing.ClassVar[ConnectionModification]  # value = pxr.UsdShade.ConnectionModification.Replace
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'Replace': pxr.UsdShade.ConnectionModification.Replace, 'Prepend': pxr.UsdShade.ConnectionModification.Prepend, 'Append': pxr.UsdShade.ConnectionModification.Append}
    values: typing.ClassVar[dict]  # value = {0: pxr.UsdShade.ConnectionModification.Replace, 1: pxr.UsdShade.ConnectionModification.Prepend, 2: pxr.UsdShade.ConnectionModification.Append}
class ConnectionSourceInfo(Boost.Python.instance):
    """
    
    A compact struct to represent a bundle of information about an
    upstream source attribute.
    
    """
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        IsValid() -> bool
        
        
        Return true if this source info is valid for setting up a connection.
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(source_, sourceName_, sourceType_, typeName_)
        
        
        Parameters
        ----------
        source_ : ConnectableAPI
        
        sourceName_ : str
        
        sourceType_ : AttributeType
        
        typeName_ : ValueTypeName
        
        
        
        ----------------------------------------------------------------------
        
        __init__(input)
        
        
        Parameters
        ----------
        input : Input
        
        
        
        ----------------------------------------------------------------------
        
        __init__(output)
        
        
        Parameters
        ----------
        output : Output
        
        
        
        ----------------------------------------------------------------------
        
        __init__(stage, sourcePath)
        
        
        Construct the information for this struct from a property path.
        
        
        The source attribute does not have to exist, but the ``sourcePath``
        needs to have a valid prefix to identify the sourceType. The source
        prim needs to exist and be UsdShadeConnectableAPI compatible
        
        
        Parameters
        ----------
        stage : Stage
        
        sourcePath : Path
        
        
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def source(*args, **kwargs):
        ...
    @source.setter
    def source(*args, **kwargs):
        ...
    @property
    def sourceName(*args, **kwargs):
        ...
    @sourceName.setter
    def sourceName(*args, **kwargs):
        ...
    @property
    def sourceType(*args, **kwargs):
        ...
    @sourceType.setter
    def sourceType(*args, **kwargs):
        ...
    @property
    def typeName(*args, **kwargs):
        ...
    @typeName.setter
    def typeName(*args, **kwargs):
        ...
class CoordSysAPI(pxr.Usd.APISchemaBase):
    """
    
    UsdShadeCoordSysAPI provides a way to designate, name, and discover
    coordinate systems.
    
    Coordinate systems are implicitly established by UsdGeomXformable
    prims, using their local space. That coordinate system may be bound
    (i.e., named) from another prim. The binding is encoded as a single-
    target relationship in the"coordSys:"namespace. Coordinate system
    bindings apply to descendants of the prim where the binding is
    expressed, but names may be re-bound by descendant prims.
    
    Named coordinate systems are useful in shading workflows. An example
    is projection paint, which projects a texture from a certain view (the
    paint coordinate system). Using the paint coordinate frame avoids the
    need to assign a UV set to the object, and can be a concise way to
    project paint across a collection of objects with a single shared
    paint coordinate system.
    
    This is a non-applied API schema.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Bind(*args, **kwargs):
        """
        
        Bind(name, path) -> bool
        
        
        Bind the name to the given path.
        
        
        The prim at the given path is expected to be UsdGeomXformable, in
        order for the binding to be succesfully resolved.
        
        
        Parameters
        ----------
        name : str
        
        path : Path
        
        
        """
    @staticmethod
    def BlockBinding(*args, **kwargs):
        """
        
        BlockBinding(name) -> bool
        
        
        Block the indicated coordinate system binding on this prim by blocking
        targets on the underlying relationship.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def CanContainPropertyName(*args, **kwargs):
        """
        
        **classmethod** CanContainPropertyName(name) -> bool
        
        
        Test whether a given ``name`` contains the"coordSys:"prefix.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def ClearBinding(*args, **kwargs):
        """
        
        ClearBinding(name, removeSpec) -> bool
        
        
        Clear the indicated coordinate system binding on this prim from the
        current edit target.
        
        
        Only remove the spec if ``removeSpec`` is true (leave the spec to
        preserve meta-data we may have intentionally authored on the
        relationship)
        
        
        Parameters
        ----------
        name : str
        
        removeSpec : bool
        
        
        """
    @staticmethod
    def FindBindingsWithInheritance(*args, **kwargs):
        """
        
        FindBindingsWithInheritance() -> list[Binding]
        
        
        Find the list of coordinate system bindings that apply to this prim,
        including inherited bindings.
        
        
        This computation examines this prim and ancestors for the strongest
        binding for each name. A binding expressed by a child prim supercedes
        bindings on ancestors.
        
        Note that this API does not validate the prims at the target paths;
        they may be of incorrect type, or missing entirely.
        
        Binding relationships with no resolved targets are skipped.
        
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> CoordSysAPI
        
        
        Return a UsdShadeCoordSysAPI holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdShadeCoordSysAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetCoordSysRelationshipName(*args, **kwargs):
        """
        
        **classmethod** GetCoordSysRelationshipName(coordSysName) -> str
        
        
        Returns the fully namespaced coordinate system relationship name,
        given the coordinate system name.
        
        
        Parameters
        ----------
        coordSysName : str
        
        
        """
    @staticmethod
    def GetLocalBindings(*args, **kwargs):
        """
        
        GetLocalBindings() -> list[Binding]
        
        
        Get the list of coordinate system bindings local to this prim.
        
        
        This does not process inherited bindings. It does not validate that a
        prim exists at the indicated path. If the binding relationship has
        multiple targets, only the first is used.
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def HasLocalBindings(*args, **kwargs):
        """
        
        HasLocalBindings() -> bool
        
        
        Returns true if the prim has local coordinate system binding opinions.
        
        
        Note that the resulting binding list may still be empty.
        
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdShadeCoordSysAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdShadeCoordSysAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdShadeCoordSysAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdShadeCoordSysAPI (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Input(Boost.Python.instance):
    """
    
    This class encapsulates a shader or node-graph input, which is a
    connectable attribute representing a typed value.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CanConnect(*args, **kwargs):
        """
        
        CanConnect(source) -> bool
        
        
        Determines whether this Input can be connected to the given source
        attribute, which can be an input or an output.
        
        
        
        UsdShadeConnectableAPI::CanConnect
        
        
        Parameters
        ----------
        source : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        CanConnect(sourceInput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        sourceInput : Input
        
        
        
        ----------------------------------------------------------------------
        
        CanConnect(sourceOutput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        sourceOutput : Output
        
        
        """
    @staticmethod
    def ClearConnectability(*args, **kwargs):
        """
        
        ClearConnectability() -> bool
        
        
        Clears any authored connectability on the Input.
        
        
        
        """
    @staticmethod
    def ClearSdrMetadata(*args, **kwargs):
        """
        
        ClearSdrMetadata() -> None
        
        
        Clears any"sdrMetadata"value authored on the Input in the current
        EditTarget.
        
        
        
        """
    @staticmethod
    def ClearSdrMetadataByKey(*args, **kwargs):
        """
        
        ClearSdrMetadataByKey(key) -> None
        
        
        Clears the entry corresponding to the given ``key`` in
        the"sdrMetadata"dictionary authored in the current EditTarget.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def ClearSource(*args, **kwargs):
        """
        
        ClearSource() -> bool
        
        
        Deprecated
        
        
        
        """
    @staticmethod
    def ClearSources(*args, **kwargs):
        """
        
        ClearSources() -> bool
        
        
        Clears sources for this Input in the current UsdEditTarget.
        
        
        Most of the time, what you probably want is DisconnectSource() rather
        than this function.
        
        UsdShadeConnectableAPI::ClearSources
        
        
        
        """
    @staticmethod
    def ConnectToSource(*args, **kwargs):
        """
        
        ConnectToSource(source, mod) -> bool
        
        
        Authors a connection for this Input.
        
        
        ``source`` is a struct that describes the upstream source attribute
        with all the information necessary to make a connection. See the
        documentation for UsdShadeConnectionSourceInfo. ``mod`` describes the
        operation that should be applied to the list of connections. By
        default the new connection will replace any existing connections, but
        it can add to the list of connections to represent multiple input
        connections.
        
        ``true`` if a connection was created successfully. ``false`` if this
        input or ``source`` is invalid.
        
        This method does not verify the connectability of the shading
        attribute to the source. Clients must invoke CanConnect() themselves
        to ensure compatibility.
        
        The source shading attribute is created if it doesn't exist already.
        
        UsdShadeConnectableAPI::ConnectToSource
        
        
        Parameters
        ----------
        source : ConnectionSourceInfo
        
        mod : ConnectionModification
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(source, sourceName, sourceType, typeName) -> bool
        
        
        Deprecated
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        source : ConnectableAPI
        
        sourceName : str
        
        sourceType : AttributeType
        
        typeName : ValueTypeName
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(sourcePath) -> bool
        
        
        Authors a connection for this Input to the source at the given path.
        
        
        
        UsdShadeConnectableAPI::ConnectToSource
        
        
        Parameters
        ----------
        sourcePath : Path
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(sourceInput) -> bool
        
        
        Connects this Input to the given input, ``sourceInput`` .
        
        
        
        UsdShadeConnectableAPI::ConnectToSource
        
        
        Parameters
        ----------
        sourceInput : Input
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(sourceOutput) -> bool
        
        
        Connects this Input to the given output, ``sourceOutput`` .
        
        
        
        UsdShadeConnectableAPI::ConnectToSource
        
        
        Parameters
        ----------
        sourceOutput : Output
        
        
        """
    @staticmethod
    def DisconnectSource(*args, **kwargs):
        """
        
        DisconnectSource(sourceAttr) -> bool
        
        
        Disconnect source for this Input.
        
        
        If ``sourceAttr`` is valid, only a connection to the specified
        attribute is disconnected, otherwise all connections are removed.
        
        UsdShadeConnectableAPI::DisconnectSource
        
        
        Parameters
        ----------
        sourceAttr : Attribute
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        Get(value, time) -> bool
        
        
        Convenience wrapper for the templated UsdAttribute::Get() .
        
        
        Parameters
        ----------
        value : T
        
        time : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        Get(value, time) -> bool
        
        
        Convenience wrapper for VtValue version of UsdAttribute::Get() .
        
        
        Parameters
        ----------
        value : VtValue
        
        time : TimeCode
        
        
        """
    @staticmethod
    def GetAttr(*args, **kwargs):
        """
        
        GetAttr() -> Attribute
        
        
        Explicit UsdAttribute extractor.
        
        
        
        """
    @staticmethod
    def GetBaseName(*args, **kwargs):
        """
        
        GetBaseName() -> str
        
        
        Returns the name of the input.
        
        
        We call this the base name since it strips off the"inputs:"namespace
        prefix from the attribute name, and returns it.
        
        
        
        """
    @staticmethod
    def GetConnectability(*args, **kwargs):
        """
        
        GetConnectability() -> str
        
        
        Returns the connectability of the Input.
        
        
        
        SetConnectability()
        
        
        
        """
    @staticmethod
    def GetConnectedSource(*args, **kwargs):
        """
        
        GetConnectedSource(source, sourceName, sourceType) -> bool
        
        
        Deprecated
        
        
        Parameters
        ----------
        source : ConnectableAPI
        
        sourceName : str
        
        sourceType : AttributeType
        
        
        """
    @staticmethod
    def GetConnectedSources(*args, **kwargs):
        """
        
        GetConnectedSources(invalidSourcePaths) -> list[SourceInfo]
        
        
        Finds the valid sources of connections for the Input.
        
        
        ``invalidSourcePaths`` is an optional output parameter to collect the
        invalid source paths that have not been reported in the returned
        vector.
        
        Returns a vector of ``UsdShadeConnectionSourceInfo`` structs with
        information about each upsteam attribute. If the vector is empty,
        there have been no valid connections.
        
        A valid connection requires the existence of the source attribute and
        also requires that the source prim is UsdShadeConnectableAPI
        compatible.
        
        The python wrapping returns a tuple with the valid connections first,
        followed by the invalid source paths.
        
        UsdShadeConnectableAPI::GetConnectedSources
        
        
        Parameters
        ----------
        invalidSourcePaths : list[Path]
        
        
        """
    @staticmethod
    def GetDisplayGroup(*args, **kwargs):
        """
        
        GetDisplayGroup() -> str
        
        
        Get the displayGroup metadata for this Input, i.e.
        
        
        hint for the location and nesting of the attribute.
        
        UsdProperty::GetDisplayGroup() , UsdProperty::GetNestedDisplayGroup()
        
        
        
        """
    @staticmethod
    def GetDocumentation(*args, **kwargs):
        """
        
        GetDocumentation() -> str
        
        
        Get documentation string for this Input.
        
        
        
        UsdObject::GetDocumentation()
        
        
        
        """
    @staticmethod
    def GetFullName(*args, **kwargs):
        """
        
        GetFullName() -> str
        
        
        Get the name of the attribute associated with the Input.
        
        
        
        """
    @staticmethod
    def GetPrim(*args, **kwargs):
        """
        
        GetPrim() -> Prim
        
        
        Get the prim that the input belongs to.
        
        
        
        """
    @staticmethod
    def GetRawConnectedSourcePaths(*args, **kwargs):
        """
        
        GetRawConnectedSourcePaths(sourcePaths) -> bool
        
        
        Deprecated
        
        Returns the"raw"(authored) connected source paths for this Input.
        
        UsdShadeConnectableAPI::GetRawConnectedSourcePaths
        
        
        Parameters
        ----------
        sourcePaths : list[Path]
        
        
        """
    @staticmethod
    def GetRenderType(*args, **kwargs):
        """
        
        GetRenderType() -> str
        
        
        Return this Input's specialized renderType, or an empty token if none
        was authored.
        
        
        
        SetRenderType()
        
        
        
        """
    @staticmethod
    def GetSdrMetadata(*args, **kwargs):
        """
        
        GetSdrMetadata() -> NdrTokenMap
        
        
        Returns this Input's composed"sdrMetadata"dictionary as a NdrTokenMap.
        
        
        
        """
    @staticmethod
    def GetSdrMetadataByKey(*args, **kwargs):
        """
        
        GetSdrMetadataByKey(key) -> str
        
        
        Returns the value corresponding to ``key`` in the composed
        **sdrMetadata** dictionary.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def GetTypeName(*args, **kwargs):
        """
        
        GetTypeName() -> ValueTypeName
        
        
        Get the"scene description"value type name of the attribute associated
        with the Input.
        
        
        
        """
    @staticmethod
    def GetValueProducingAttribute(*args, **kwargs):
        """
        
        GetValueProducingAttribute(attrType) -> Attribute
        
        
        Deprecated
        
        in favor of calling GetValueProducingAttributes
        
        
        Parameters
        ----------
        attrType : AttributeType
        
        
        """
    @staticmethod
    def GetValueProducingAttributes(*args, **kwargs):
        """
        
        GetValueProducingAttributes(shaderOutputsOnly) -> list[UsdShadeAttribute]
        
        
        Find what is connected to this Input recursively.
        
        
        
        UsdShadeUtils::GetValueProducingAttributes
        
        
        Parameters
        ----------
        shaderOutputsOnly : bool
        
        
        """
    @staticmethod
    def HasConnectedSource(*args, **kwargs):
        """
        
        HasConnectedSource() -> bool
        
        
        Returns true if and only if this Input is currently connected to a
        valid (defined) source.
        
        
        
        UsdShadeConnectableAPI::HasConnectedSource
        
        
        
        """
    @staticmethod
    def HasRenderType(*args, **kwargs):
        """
        
        HasRenderType() -> bool
        
        
        Return true if a renderType has been specified for this Input.
        
        
        
        SetRenderType()
        
        
        
        """
    @staticmethod
    def HasSdrMetadata(*args, **kwargs):
        """
        
        HasSdrMetadata() -> bool
        
        
        Returns true if the Input has a non-empty
        composed"sdrMetadata"dictionary value.
        
        
        
        """
    @staticmethod
    def HasSdrMetadataByKey(*args, **kwargs):
        """
        
        HasSdrMetadataByKey(key) -> bool
        
        
        Returns true if there is a value corresponding to the given ``key`` in
        the composed"sdrMetadata"dictionary.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def IsInput(*args, **kwargs):
        """
        
        **classmethod** IsInput(attr) -> bool
        
        
        Test whether a given UsdAttribute represents a valid Input, which
        implies that creating a UsdShadeInput from the attribute will succeed.
        
        
        Success implies that ``attr.IsDefined()`` is true.
        
        
        Parameters
        ----------
        attr : Attribute
        
        
        """
    @staticmethod
    def IsInterfaceInputName(*args, **kwargs):
        """
        
        **classmethod** IsInterfaceInputName(name) -> bool
        
        
        Test if this name has a namespace that indicates it could be an input.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def IsSourceConnectionFromBaseMaterial(*args, **kwargs):
        """
        
        IsSourceConnectionFromBaseMaterial() -> bool
        
        
        Returns true if the connection to this Input's source, as returned by
        GetConnectedSource() , is authored across a specializes arc, which is
        used to denote a base material.
        
        
        
        UsdShadeConnectableAPI::IsSourceConnectionFromBaseMaterial
        
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(value, time) -> bool
        
        
        Set a value for the Input at ``time`` .
        
        
        Parameters
        ----------
        value : VtValue
        
        time : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        Set(value, time) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Set a value of the Input at ``time`` .
        
        
        Parameters
        ----------
        value : T
        
        time : TimeCode
        
        
        """
    @staticmethod
    def SetConnectability(*args, **kwargs):
        """
        
        SetConnectability(connectability) -> bool
        
        
        Set the connectability of the Input.
        
        
        In certain shading data models, there is a need to distinguish which
        inputs **can** vary over a surface from those that must be
        **uniform**. This is accomplished in UsdShade by limiting the
        connectability of the input. This is done by setting
        the"connectability"metadata on the associated attribute.
        
        Connectability of an Input can be set to UsdShadeTokens->full or
        UsdShadeTokens->interfaceOnly.
        
           - **full** implies that the Input can be connected to any other
             Input or Output.
        
           - **interfaceOnly** implies that the Input can only be connected to
             a NodeGraph Input (which represents an interface override, not a
             render-time dataflow connection), or another Input whose
             connectability is also"interfaceOnly".
             The default connectability of an input is UsdShadeTokens->full.
        
        SetConnectability()
        
        
        Parameters
        ----------
        connectability : str
        
        
        """
    @staticmethod
    def SetConnectedSources(*args, **kwargs):
        """
        
        SetConnectedSources(sourceInfos) -> bool
        
        
        Connects this Input to the given sources, ``sourceInfos`` .
        
        
        
        UsdShadeConnectableAPI::SetConnectedSources
        
        
        Parameters
        ----------
        sourceInfos : list[ConnectionSourceInfo]
        
        
        """
    @staticmethod
    def SetDisplayGroup(*args, **kwargs):
        """
        
        SetDisplayGroup(displayGroup) -> bool
        
        
        Set the displayGroup metadata for this Input, i.e.
        
        
        hinting for the location and nesting of the attribute.
        
        Note for an input representing a nested SdrShaderProperty, its
        expected to have the scope delimited by a":".
        
        UsdProperty::SetDisplayGroup() , UsdProperty::SetNestedDisplayGroup()
        
        SdrShaderProperty::GetPage()
        
        
        Parameters
        ----------
        displayGroup : str
        
        
        """
    @staticmethod
    def SetDocumentation(*args, **kwargs):
        """
        
        SetDocumentation(docs) -> bool
        
        
        Set documentation string for this Input.
        
        
        
        UsdObject::SetDocumentation()
        
        
        Parameters
        ----------
        docs : str
        
        
        """
    @staticmethod
    def SetRenderType(*args, **kwargs):
        """
        
        SetRenderType(renderType) -> bool
        
        
        Specify an alternative, renderer-specific type to use when
        emitting/translating this Input, rather than translating based on its
        GetTypeName()
        
        
        For example, we set the renderType to"struct"for Inputs that are of
        renderman custom struct types.
        
        true on success.
        
        
        Parameters
        ----------
        renderType : str
        
        
        """
    @staticmethod
    def SetSdrMetadata(*args, **kwargs):
        """
        
        SetSdrMetadata(sdrMetadata) -> None
        
        
        Authors the given ``sdrMetadata`` value on this Input at the current
        EditTarget.
        
        
        Parameters
        ----------
        sdrMetadata : NdrTokenMap
        
        
        """
    @staticmethod
    def SetSdrMetadataByKey(*args, **kwargs):
        """
        
        SetSdrMetadataByKey(key, value) -> None
        
        
        Sets the value corresponding to ``key`` to the given string ``value``
        , in the Input's"sdrMetadata"dictionary at the current EditTarget.
        
        
        Parameters
        ----------
        key : str
        
        value : str
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(attr)
        
        
        Speculative constructor that will produce a valid UsdShadeInput when
        ``attr`` already represents a shade Input, and produces an *invalid*
        UsdShadeInput otherwise (i.e.
        
        
        the explicit bool conversion operator will return false).
        
        
        Parameters
        ----------
        attr : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        __init__()
        
        
        Default constructor returns an invalid Input.
        
        
        Exists for the sake of container classes
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim, name, typeName)
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Material(NodeGraph):
    """
    
    A Material provides a container into which multiple"render targets"can
    add data that defines a"shading material"for a renderer. Typically
    this consists of one or more UsdRelationship properties that target
    other prims of type *Shader* - though a target/client is free to add
    any data that is suitable. We **strongly advise** that all targets
    adopt the convention that all properties be prefixed with a namespace
    that identifies the target, e.g."rel ri:surface =</Shaders/mySurf>".
    
    In the UsdShading model, geometry expresses a binding to a single
    Material or to a set of Materials partitioned by UsdGeomSubsets
    defined beneath the geometry; it is legal to bind a Material at the
    root (or other sub-prim) of a model, and then bind a different
    Material to individual gprims, but the meaning of inheritance
    and"ancestral overriding"of Material bindings is left to each render-
    target to determine. Since UsdGeom has no concept of shading, we
    provide the API for binding and unbinding geometry on the API schema
    UsdShadeMaterialBindingAPI.
    
    The entire power of USD VariantSets and all the other composition
    operators can leveraged when encoding shading variation.
    UsdShadeMaterial provides facilities for a particular way of
    building"Material variants"in which neither the identity of the
    Materials themselves nor the geometry Material-bindings need to change
    \\- instead we vary the targeted networks, interface values, and even
    parameter values within a single variantSet.  See Authoring Material
    Variations for more details.
    
    UsdShade requires that all of the shaders that"belong"to the Material
    live under the Material in namespace. This supports powerful, easy
    reuse of Materials, because it allows us to *reference* a Material
    from one asset (the asset might be a module of Materials) into
    another asset: USD references compose all descendant prims of the
    reference target into the referencer's namespace, which means that all
    of the referenced Material's shader networks will come along with the
    Material. When referenced in this way, Materials can also be
    instanced, for ease of deduplication and compactness. Finally,
    Material encapsulation also allows us to specialize child materials
    from parent materials.
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdShadeTokens. So to set an attribute to the value"rightHanded",
    use UsdShadeTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def ClearBaseMaterial(*args, **kwargs):
        """
        
        ClearBaseMaterial() -> None
        
        
        Clear the base Material of this Material.
        
        
        
        """
    @staticmethod
    def ComputeDisplacementSource(*args, **kwargs):
        """
        
        ComputeDisplacementSource(renderContext, sourceName, sourceType) -> Shader
        
        
        Deprecated
        
        Use the form that takes a TfTokenVector or renderContexts
        
        
        Parameters
        ----------
        renderContext : str
        
        sourceName : str
        
        sourceType : AttributeType
        
        
        
        ----------------------------------------------------------------------
        
        ComputeDisplacementSource(contextVector, sourceName, sourceType) -> Shader
        
        
        Computes the resolved"displacement"output source for the given
        ``contextVector`` .
        
        
        Using the earliest renderContext in the contextVector that produces a
        valid Shader object.
        
        If a"displacement"output corresponding to each of the renderContexts
        does not exist **or** is not connected to a valid source, then this
        checks the *universal* displacement output.
        
        Returns an empty Shader object if there is no valid *displacement*
        output source for any of the renderContexts in the ``contextVector`` .
        The python version of this method returns a tuple containing three
        elements (the source displacement shader, sourceName, sourceType).
        
        
        Parameters
        ----------
        contextVector : list[str]
        
        sourceName : str
        
        sourceType : AttributeType
        
        
        """
    @staticmethod
    def ComputeSurfaceSource(*args, **kwargs):
        """
        
        ComputeSurfaceSource(renderContext, sourceName, sourceType) -> Shader
        
        
        Deprecated
        
        Use the form that takes a TfTokenVector or renderContexts.
        
        
        Parameters
        ----------
        renderContext : str
        
        sourceName : str
        
        sourceType : AttributeType
        
        
        
        ----------------------------------------------------------------------
        
        ComputeSurfaceSource(contextVector, sourceName, sourceType) -> Shader
        
        
        Computes the resolved"surface"output source for the given
        ``contextVector`` .
        
        
        Using the earliest renderContext in the contextVector that produces a
        valid Shader object.
        
        If a"surface"output corresponding to each of the renderContexts does
        not exist **or** is not connected to a valid source, then this checks
        the *universal* surface output.
        
        Returns an empty Shader object if there is no valid *surface* output
        source for any of the renderContexts in the ``contextVector`` . The
        python version of this method returns a tuple containing three
        elements (the source surface shader, sourceName, sourceType).
        
        
        Parameters
        ----------
        contextVector : list[str]
        
        sourceName : str
        
        sourceType : AttributeType
        
        
        """
    @staticmethod
    def ComputeVolumeSource(*args, **kwargs):
        """
        
        ComputeVolumeSource(renderContext, sourceName, sourceType) -> Shader
        
        
        Deprecated
        
        Use the form that takes a TfTokenVector or renderContexts
        
        
        Parameters
        ----------
        renderContext : str
        
        sourceName : str
        
        sourceType : AttributeType
        
        
        
        ----------------------------------------------------------------------
        
        ComputeVolumeSource(contextVector, sourceName, sourceType) -> Shader
        
        
        Computes the resolved"volume"output source for the given
        ``contextVector`` .
        
        
        Using the earliest renderContext in the contextVector that produces a
        valid Shader object.
        
        If a"volume"output corresponding to each of the renderContexts does
        not exist **or** is not connected to a valid source, then this checks
        the *universal* volume output.
        
        Returns an empty Shader object if there is no valid *volume* output
        output source for any of the renderContexts in the ``contextVector`` .
        The python version of this method returns a tuple containing three
        elements (the source volume shader, sourceName, sourceType).
        
        
        Parameters
        ----------
        contextVector : list[str]
        
        sourceName : str
        
        sourceType : AttributeType
        
        
        """
    @staticmethod
    def CreateDisplacementAttr(*args, **kwargs):
        """
        
        CreateDisplacementAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetDisplacementAttr() , and also Create vs Get Property Methods
        for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateDisplacementOutput(*args, **kwargs):
        """
        
        CreateDisplacementOutput(renderContext) -> Output
        
        
        Creates and returns the"displacement"output on this material for the
        specified ``renderContext`` .
        
        
        If the output already exists on the material, it is returned and no
        authoring is performed. The returned output will always have the
        requested renderContext.
        
        
        Parameters
        ----------
        renderContext : str
        
        
        """
    @staticmethod
    def CreateMasterMaterialVariant(*args, **kwargs):
        """
        
        **classmethod** CreateMasterMaterialVariant(masterPrim, MaterialPrims, masterVariantSetName) -> bool
        
        
        Create a variantSet on ``masterPrim`` that will set the
        MaterialVariant on each of the given *MaterialPrims*.
        
        
        The variantSet, whose name can be specified with
        ``masterVariantSetName`` and defaults to the same MaterialVariant name
        created on Materials by GetEditContextForVariant() , will have the
        same variants as the Materials, and each Master variant will set every
        ``MaterialPrims'`` MaterialVariant selection to the same variant as
        the master. Thus, it allows all Materials to be switched with a single
        variant selection, on ``masterPrim`` .
        
        If ``masterPrim`` is an ancestor of any given member of
        ``MaterialPrims`` , then we will author variant selections directly on
        the MaterialPrims. However, it is often preferable to create a master
        MaterialVariant in a separately rooted tree from the MaterialPrims, so
        that it can be layered more strongly on top of the Materials.
        Therefore, for any MaterialPrim in a different tree than masterPrim,
        we will create"overs"as children of masterPrim that recreate the path
        to the MaterialPrim, substituting masterPrim's full path for the
        MaterialPrim's root path component.
        
        Upon successful completion, the new variantSet we created on
        ``masterPrim`` will have its variant selection authored to
        the"last"variant (determined lexicographically). It is up to the
        calling client to either UsdVariantSet::ClearVariantSelection() on
        ``masterPrim`` , or set the selection to the desired default setting.
        
        Return ``true`` on success. It is an error if any of ``Materials``
        have a different set of variants for the MaterialVariant than the
        others.
        
        
        Parameters
        ----------
        masterPrim : Prim
        
        MaterialPrims : list[Prim]
        
        masterVariantSetName : str
        
        
        """
    @staticmethod
    def CreateSurfaceAttr(*args, **kwargs):
        """
        
        CreateSurfaceAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetSurfaceAttr() , and also Create vs Get Property Methods for
        when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateSurfaceOutput(*args, **kwargs):
        """
        
        CreateSurfaceOutput(renderContext) -> Output
        
        
        Creates and returns the"surface"output on this material for the
        specified ``renderContext`` .
        
        
        If the output already exists on the material, it is returned and no
        authoring is performed. The returned output will always have the
        requested renderContext.
        
        
        Parameters
        ----------
        renderContext : str
        
        
        """
    @staticmethod
    def CreateVolumeAttr(*args, **kwargs):
        """
        
        CreateVolumeAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetVolumeAttr() , and also Create vs Get Property Methods for when
        to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateVolumeOutput(*args, **kwargs):
        """
        
        CreateVolumeOutput(renderContext) -> Output
        
        
        Creates and returns the"volume"output on this material for the
        specified ``renderContext`` .
        
        
        If the output already exists on the material, it is returned and no
        authoring is performed. The returned output will always have the
        requested renderContext.
        
        
        Parameters
        ----------
        renderContext : str
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> Material
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> Material
        
        
        Return a UsdShadeMaterial holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdShadeMaterial(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetBaseMaterial(*args, **kwargs):
        """
        
        GetBaseMaterial() -> Material
        
        
        Get the path to the base Material of this Material.
        
        
        If there is no base Material, an empty Material is returned
        
        
        
        """
    @staticmethod
    def GetBaseMaterialPath(*args, **kwargs):
        """
        
        GetBaseMaterialPath() -> Path
        
        
        Get the base Material of this Material.
        
        
        If there is no base Material, an empty path is returned
        
        
        
        """
    @staticmethod
    def GetDisplacementAttr(*args, **kwargs):
        """
        
        GetDisplacementAttr() -> Attribute
        
        
        Represents the universal"displacement"output terminal of a material.
        
        
        
        Declaration
        
        ``token outputs:displacement``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        
        
        """
    @staticmethod
    def GetDisplacementOutput(*args, **kwargs):
        """
        
        GetDisplacementOutput(renderContext) -> Output
        
        
        Returns the"displacement"output of this material for the specified
        renderContext.
        
        
        The returned output will always have the requested renderContext.
        
        An invalid output is returned if an output corresponding to the
        requested specific-renderContext does not exist.
        
        UsdShadeMaterial::ComputeDisplacementSource()
        
        
        Parameters
        ----------
        renderContext : str
        
        
        """
    @staticmethod
    def GetDisplacementOutputs(*args, **kwargs):
        """
        
        GetDisplacementOutputs() -> list[Output]
        
        
        Returns the"displacement"outputs of this material for all available
        renderContexts.
        
        
        The returned vector will include all authored"displacement"outputs
        with the *universal* renderContext output first, if present. Outputs
        are returned regardless of whether they are connected to a valid
        source.
        
        
        
        """
    @staticmethod
    def GetEditContextForVariant(*args, **kwargs):
        """
        
        GetEditContextForVariant(MaterialVariantName, layer) -> tuple[Stage, EditTarget]
        
        
        Helper function for configuring a UsdStage 's UsdEditTarget to author
        Material variations.
        
        
        Takes care of creating the Material variantSet and specified variant,
        if necessary.
        
        Let's assume that we are authoring Materials into the Stage's current
        UsdEditTarget, and that we are iterating over the variations of a
        UsdShadeMaterial *clothMaterial*, and *currVariant* is the variant we
        are processing (e.g."denim").
        
        In C++, then, we would use the following pattern:
        
        .. code-block:: text
        
          {
              UsdEditContext ctxt(clothMaterial.GetEditContextForVariant(currVariant));
          
              // All USD mutation of the UsdStage on which clothMaterial sits will
              // now go "inside" the currVariant of the "MaterialVariant" variantSet
          }
        
        In python, the pattern is:
        
        .. code-block:: text
        
          with clothMaterial.GetEditContextForVariant(currVariant):
              # Now sending mutations to currVariant
        
        If ``layer`` is specified, then we will use it, rather than the
        stage's current UsdEditTarget 's layer as the destination layer for
        the edit context we are building. If ``layer`` does not actually
        contribute to the Material prim's definition, any editing will have no
        effect on this Material.
        
        **Note:** As just stated, using this method involves authoring a
        selection for the MaterialVariant in the stage's current EditTarget.
        When client is done authoring variations on this prim, they will
        likely want to either UsdVariantSet::SetVariantSelection() to the
        appropriate default selection, or possibly
        UsdVariantSet::ClearVariantSelection() on the
        UsdShadeMaterial::GetMaterialVariant() UsdVariantSet.
        
        UsdVariantSet::GetVariantEditContext()
        
        
        Parameters
        ----------
        MaterialVariantName : str
        
        layer : Layer
        
        
        """
    @staticmethod
    def GetMaterialVariant(*args, **kwargs):
        """
        
        GetMaterialVariant() -> VariantSet
        
        
        Return a UsdVariantSet object for interacting with the Material
        variant variantSet.
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def GetSurfaceAttr(*args, **kwargs):
        """
        
        GetSurfaceAttr() -> Attribute
        
        
        Represents the universal"surface"output terminal of a material.
        
        
        
        Declaration
        
        ``token outputs:surface``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        
        
        """
    @staticmethod
    def GetSurfaceOutput(*args, **kwargs):
        """
        
        GetSurfaceOutput(renderContext) -> Output
        
        
        Returns the"surface"output of this material for the specified
        ``renderContext`` .
        
        
        The returned output will always have the requested renderContext.
        
        An invalid output is returned if an output corresponding to the
        requested specific-renderContext does not exist.
        
        UsdShadeMaterial::ComputeSurfaceSource()
        
        
        Parameters
        ----------
        renderContext : str
        
        
        """
    @staticmethod
    def GetSurfaceOutputs(*args, **kwargs):
        """
        
        GetSurfaceOutputs() -> list[Output]
        
        
        Returns the"surface"outputs of this material for all available
        renderContexts.
        
        
        The returned vector will include all authored"surface"outputs with the
        *universal* renderContext output first, if present. Outputs are
        returned regardless of whether they are connected to a valid source.
        
        
        
        """
    @staticmethod
    def GetVolumeAttr(*args, **kwargs):
        """
        
        GetVolumeAttr() -> Attribute
        
        
        Represents the universal"volume"output terminal of a material.
        
        
        
        Declaration
        
        ``token outputs:volume``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        
        
        """
    @staticmethod
    def GetVolumeOutput(*args, **kwargs):
        """
        
        GetVolumeOutput(renderContext) -> Output
        
        
        Returns the"volume"output of this material for the specified
        renderContext.
        
        
        The returned output will always have the requested renderContext.
        
        An invalid output is returned if an output corresponding to the
        requested specific-renderContext does not exist.
        
        UsdShadeMaterial::ComputeVolumeSource()
        
        
        Parameters
        ----------
        renderContext : str
        
        
        """
    @staticmethod
    def GetVolumeOutputs(*args, **kwargs):
        """
        
        GetVolumeOutputs() -> list[Output]
        
        
        Returns the"volume"outputs of this material for all available
        renderContexts.
        
        
        The returned vector will include all authored"volume"outputs with the
        *universal* renderContext output first, if present. Outputs are
        returned regardless of whether they are connected to a valid source.
        
        
        
        """
    @staticmethod
    def HasBaseMaterial(*args, **kwargs):
        """
        
        HasBaseMaterial() -> bool
        
        
        
        """
    @staticmethod
    def SetBaseMaterial(*args, **kwargs):
        """
        
        SetBaseMaterial(baseMaterial) -> None
        
        
        Set the base Material of this Material.
        
        
        An empty Material is equivalent to clearing the base Material.
        
        
        Parameters
        ----------
        baseMaterial : Material
        
        
        """
    @staticmethod
    def SetBaseMaterialPath(*args, **kwargs):
        """
        
        SetBaseMaterialPath(baseMaterialPath) -> None
        
        
        Set the path to the base Material of this Material.
        
        
        An empty path is equivalent to clearing the base Material.
        
        
        Parameters
        ----------
        baseMaterialPath : Path
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdShadeMaterial on UsdPrim ``prim`` .
        
        
        Equivalent to UsdShadeMaterial::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdShadeMaterial on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdShadeMaterial (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class MaterialBindingAPI(pxr.Usd.APISchemaBase):
    """
    
    UsdShadeMaterialBindingAPI is an API schema that provides an interface
    for binding materials to prims or collections of prims (represented by
    UsdCollectionAPI objects).
    
    In the USD shading model, each renderable gprim computes a single
    **resolved Material** that will be used to shade the gprim
    (exceptions, of course, for gprims that possess UsdGeomSubsets, as
    each subset can be shaded by a different Material). A gprim **and each
    of its ancestor prims** can possess, through the MaterialBindingAPI,
    both a **direct** binding to a Material, and any number of
    **collection-based** bindings to Materials; each binding can be
    generic or declared for a particular **purpose**, and given a specific
    **binding strength**. It is the process of"material resolution"(see
    UsdShadeMaterialBindingAPI_MaterialResolution) that examines all of
    these bindings, and selects the one Material that best matches the
    client's needs.
    
    The intent of **purpose** is that each gprim should be able to resolve
    a Material for any given purpose, which implies it can have
    differently bound materials for different purposes. There are two
    *special* values of **purpose** defined in UsdShade, although the API
    fully supports specifying arbitrary values for it, for the sake of
    extensibility:
    
       - **UsdShadeTokens->full** : to be used when the purpose of the
         render is entirely to visualize the truest representation of a scene,
         considering all lighting and material information, at highest
         fidelity.
    
       - **UsdShadeTokens->preview** : to be used when the render is in
         service of a goal other than a high fidelity"full"render (such as
         scene manipulation, modeling, or realtime playback). Latency and speed
         are generally of greater concern for preview renders, therefore
         preview materials are generally designed to be"lighterweight"compared
         to full materials.
         A binding can also have no specific purpose at all, in which case, it
         is considered to be the fallback or all-purpose binding (denoted by
         the empty-valued token **UsdShadeTokens->allPurpose**).
    
    The **purpose** of a material binding is encoded in the name of the
    binding relationship.
    
       - In the case of a direct binding, the *allPurpose* binding is
         represented by the relationship named **"material:binding"**. Special-
         purpose direct bindings are represented by relationships named
         **"material:binding: *purpose***. A direct binding relationship must
         have a single target path that points to a **UsdShadeMaterial**.
    
       - In the case of a collection-based binding, the *allPurpose*
         binding is represented by a relationship
         named"material:binding:collection:<i>bindingName</i>", where
         **bindingName** establishes an identity for the binding that is unique
         on the prim. Attempting to establish two collection bindings of the
         same name on the same prim will result in the first binding simply
         being overridden. A special-purpose collection-based binding is
         represented by a relationship
         named"material:binding:collection:<i>purpose:bindingName</i>". A
         collection-based binding relationship must have exacly two targets,
         one of which should be a collection-path (see ef
         UsdCollectionAPI::GetCollectionPath() ) and the other should point to
         a **UsdShadeMaterial**. In the future, we may allow a single
         collection binding to target multiple collections, if we can establish
         a reasonable round-tripping pattern for applications that only allow a
         single collection to be associated with each Material.
    
    **Note:** Both **bindingName** and **purpose** must be non-namespaced
    tokens. This allows us to know the role of a binding relationship
    simply from the number of tokens in it.
    
       - **Two tokens** : the fallback,"all purpose", direct binding,
         *material:binding*
    
       - **Three tokens** : a purpose-restricted, direct, fallback
         binding, e.g. material:binding:preview
    
       - **Four tokens** : an all-purpose, collection-based binding, e.g.
         material:binding:collection:metalBits
    
       - **Five tokens** : a purpose-restricted, collection-based binding,
         e.g. material:binding:collection:full:metalBits
    
    A **binding-strength** value is used to specify whether a binding
    authored on a prim should be weaker or stronger than bindings that
    appear lower in namespace. We encode the binding strength with as
    token-valued metadata **'bindMaterialAs'** for future flexibility,
    even though for now, there are only two possible values:
    *UsdShadeTokens->weakerThanDescendants* and
    *UsdShadeTokens->strongerThanDescendants*. When binding-strength is
    not authored (i.e. empty) on a binding-relationship, the default
    behavior matches UsdShadeTokens->weakerThanDescendants.
    
    If a material binding relationship is a built-in property defined as
    part of a typed prim's schema, a fallback value should not be provided
    for it. This is because the"material resolution"algorithm only
    conisders *authored* properties.
    
    """
    class CollectionBinding(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 64
        @staticmethod
        def GetBindingRel(*args, **kwargs):
            ...
        @staticmethod
        def GetCollection(*args, **kwargs):
            ...
        @staticmethod
        def GetCollectionPath(*args, **kwargs):
            ...
        @staticmethod
        def GetMaterial(*args, **kwargs):
            ...
        @staticmethod
        def GetMaterialPath(*args, **kwargs):
            ...
        @staticmethod
        def IsCollectionBindingRel(*args, **kwargs):
            ...
        @staticmethod
        def IsValid(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    class DirectBinding(Boost.Python.instance):
        __instance_size__: typing.ClassVar[int] = 64
        @staticmethod
        def GetBindingRel(*args, **kwargs):
            ...
        @staticmethod
        def GetMaterial(*args, **kwargs):
            ...
        @staticmethod
        def GetMaterialPath(*args, **kwargs):
            ...
        @staticmethod
        def GetMaterialPurpose(*args, **kwargs):
            ...
        @staticmethod
        def __init__(*args, **kwargs):
            ...
        @staticmethod
        def __reduce__(*args, **kwargs):
            ...
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def AddPrimToBindingCollection(*args, **kwargs):
        """
        
        AddPrimToBindingCollection(prim, bindingName, materialPurpose) -> bool
        
        
        Adds the specified ``prim`` to the collection targeted by the binding
        relationship corresponding to given ``bindingName`` and
        ``materialPurpose`` .
        
        
        If the collection-binding relationship doesn't exist or if the
        targeted collection already includes the ``prim`` , then this does
        nothing and returns true.
        
        If the targeted collection does not include ``prim`` (or excludes it
        explicitly), then this modifies the collection by adding the prim to
        it (by invoking UsdCollectionAPI::AddPrim()).
        
        
        Parameters
        ----------
        prim : Prim
        
        bindingName : str
        
        materialPurpose : str
        
        
        """
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> MaterialBindingAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"MaterialBindingAPI"to the token-
        valued, listOp metadata *apiSchemas* on the prim.
        
        A valid UsdShadeMaterialBindingAPI object is returned upon success. An
        invalid (or empty) UsdShadeMaterialBindingAPI object is returned upon
        failure. See UsdPrim::ApplyAPI() for conditions resulting in failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def Bind(*args, **kwargs):
        """
        
        Bind(material, bindingStrength, materialPurpose) -> bool
        
        
        Authors a direct binding to the given ``material`` on this prim.
        
        
        If ``bindingStrength`` is UsdShadeTokens->fallbackStrength, the value
        UsdShadeTokens->weakerThanDescendants is authored sparsely. To stamp
        out the bindingStrength value explicitly, clients can pass in
        UsdShadeTokens->weakerThanDescendants or
        UsdShadeTokens->strongerThanDescendants directly.
        
        If ``materialPurpose`` is specified and isn't equal to
        UsdShadeTokens->allPurpose, the binding only applies to the specified
        material purpose.
        
        Note that UsdShadeMaterialBindingAPI is a SingleAppliedAPI schema
        which when applied updates the prim definition accordingly. This
        information on the prim definition is helpful in multiple queries and
        more performant. Hence its recommended to call
        UsdShadeMaterialBindingAPI::Apply() when Binding a material.
        
        Returns true on success, false otherwise.
        
        
        Parameters
        ----------
        material : Material
        
        bindingStrength : str
        
        materialPurpose : str
        
        
        
        ----------------------------------------------------------------------
        
        Bind(collection, material, bindingName, bindingStrength, materialPurpose) -> bool
        
        
        Authors a collection-based binding, which binds the given ``material``
        to the given ``collection`` on this prim.
        
        
        ``bindingName`` establishes an identity for the binding that is unique
        on the prim. Attempting to establish two collection bindings of the
        same name on the same prim will result in the first binding simply
        being overridden. If ``bindingName`` is empty, it is set to the base-
        name of the collection being bound (which is the collection-name with
        any namespaces stripped out). If there are multiple collections with
        the same base-name being bound at the same prim, clients should pass
        in a unique binding name per binding, in order to preserve all
        bindings. The binding name used in constructing the collection-binding
        relationship name shoud not contain namespaces. Hence, a coding error
        is issued and no binding is authored if the provided value of
        ``bindingName`` is non-empty and contains namespaces.
        
        If ``bindingStrength`` is *UsdShadeTokens->fallbackStrength*, the
        value UsdShadeTokens->weakerThanDescendants is authored sparsely, i.e.
        only when there is an existing binding with a different
        bindingStrength. To stamp out the bindingStrength value explicitly,
        clients can pass in UsdShadeTokens->weakerThanDescendants or
        UsdShadeTokens->strongerThanDescendants directly.
        
        If ``materialPurpose`` is specified and isn't equal to
        UsdShadeTokens->allPurpose, the binding only applies to the specified
        material purpose.
        
        Note that UsdShadeMaterialBindingAPI is a SingleAppliedAPI schema
        which when applied updates the prim definition accordingly. This
        information on the prim definition is helpful in multiple queries and
        more performant. Hence its recommended to call
        UsdShadeMaterialBindingAPI::Apply() when Binding a material.
        
        Returns true on success, false otherwise.
        
        
        Parameters
        ----------
        collection : CollectionAPI
        
        material : Material
        
        bindingName : str
        
        bindingStrength : str
        
        materialPurpose : str
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, whyNot) -> bool
        
        
        Returns true if this **single-apply** API schema can be applied to the
        given ``prim`` .
        
        
        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates ``whyNot`` with the reason it can not be
        applied.
        
        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        whyNot : str
        
        
        """
    @staticmethod
    def CanContainPropertyName(*args, **kwargs):
        """
        
        **classmethod** CanContainPropertyName(name) -> bool
        
        
        Test whether a given ``name`` contains the"material:binding:"prefix.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def ComputeBoundMaterial(*args, **kwargs):
        """
        
        ComputeBoundMaterial(bindingsCache, collectionQueryCache, materialPurpose, bindingRel) -> Material
        
        
        Computes the resolved bound material for this prim, for the given
        material purpose.
        
        
        This overload of ComputeBoundMaterial makes use of the BindingsCache (
        ``bindingsCache`` ) and CollectionQueryCache (
        ``collectionQueryCache`` ) that are passed in, to avoid redundant
        binding computations and computations of MembershipQuery objects for
        collections. It would be beneficial to make use of these when
        resolving bindings for a tree of prims. These caches are populated
        lazily as more and more bindings are resolved.
        
        When the goal is to compute the bound material for a range (or list)
        of prims, it is recommended to use this version of
        ComputeBoundMaterial() . Here's how you could compute the bindings of
        a range of prims efficiently in C++:
        
        .. code-block:: text
        
          std::vector<std::pair<UsdPrim, UsdShadeMaterial> primBindings; 
          UsdShadeMaterialBindingAPI::BindingsCache bindingsCache;
          UsdShadeMaterialBindingAPI::CollectionQueryCache collQueryCache;
          
          for (auto prim : UsdPrimRange(rootPrim)) {
              UsdShadeMaterial boundMaterial = 
                    UsdShadeMaterialBindingAPI(prim).ComputeBoundMaterial(
                     & bindingsCache,  & collQueryCache);
              if (boundMaterial) {
                  primBindings.emplace_back({prim, boundMaterial});
              }
          }
        
        If ``bindingRel`` is not null, then it is set to the"winning"binding
        relationship.
        
        Note the resolved bound material is considered valid if the target
        path of the binding relationship is a valid non-empty prim path. This
        makes sure winning binding relationship and the bound material remain
        consistent consistent irrespective of the presence/absence of prim at
        material path. For ascenario where ComputeBoundMaterial returns a
        invalid UsdShadeMaterial with a valid winning bindingRel, clients can
        use the  static method
        UsdShadeMaterialBindingAPI::GetResolvedTargetPathFromBindingRel to get
        the path of the resolved target identified by the winning bindingRel.
        
        See Bound Material Resolution for details on the material resolution
        process.
        
        The python version of this method returns a tuple containing the bound
        material and the"winning"binding relationship.
        
        
        Parameters
        ----------
        bindingsCache : BindingsCache
        
        collectionQueryCache : CollectionQueryCache
        
        materialPurpose : str
        
        bindingRel : Relationship
        
        
        
        ----------------------------------------------------------------------
        
        ComputeBoundMaterial(materialPurpose, bindingRel) -> Material
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Computes the resolved bound material for this prim, for the given
        material purpose.
        
        
        This overload does not utilize cached MembershipQuery object. However,
        it only computes the MembershipQuery of every collection that bound in
        the ancestor chain at most once.
        
        If ``bindingRel`` is not null, then it is set to the winning binding
        relationship.
        
        See Bound Material Resolution for details on the material resolution
        process.
        
        The python version of this method returns a tuple containing the bound
        material and the"winning"binding relationship.
        
        
        Parameters
        ----------
        materialPurpose : str
        
        bindingRel : Relationship
        
        
        """
    @staticmethod
    def ComputeBoundMaterials(*args, **kwargs):
        """
        
        **classmethod** ComputeBoundMaterials(prims, materialPurpose, bindingRels) -> list[Material]
        
        
        Static API for efficiently and concurrently computing the resolved
        material bindings for a vector of UsdPrims, ``prims`` for the given
        ``materialPurpose`` .
        
        
        The size of the returned vector always matches the size of the input
        vector, ``prims`` . If a prim is not bound to any material, an invalid
        or empty UsdShadeMaterial is returned at the index corresponding to
        it.
        
        If the pointer ``bindingRels`` points to a valid vector, then it is
        populated with the set of all"winning"binding relationships.
        
        The python version of this method returns a tuple containing two lists
        \\- the bound materials and the corresponding"winning"binding
        relationships.
        
        
        Parameters
        ----------
        prims : list[Prim]
        
        materialPurpose : str
        
        bindingRels : list[Relationship]
        
        
        """
    @staticmethod
    def CreateMaterialBindSubset(*args, **kwargs):
        """
        
        CreateMaterialBindSubset(subsetName, indices, elementType) -> Subset
        
        
        Creates a GeomSubset named ``subsetName`` with element type,
        ``elementType`` and familyName **materialBind **below this prim.****
        
        
        If a GeomSubset named ``subsetName`` already exists, then
        its"familyName"is updated to be UsdShadeTokens->materialBind and its
        indices (at *default* timeCode) are updated with the provided
        ``indices`` value before returning.
        
        This method forces the familyType of the"materialBind"family of
        subsets to UsdGeomTokens->nonOverlapping if it's unset or explicitly
        set to UsdGeomTokens->unrestricted.
        
        The default value ``elementType`` is UsdGeomTokens->face, as we expect
        materials to be bound most often to subsets of faces on meshes.
        
        
        Parameters
        ----------
        subsetName : str
        
        indices : IntArray
        
        elementType : str
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> MaterialBindingAPI
        
        
        Return a UsdShadeMaterialBindingAPI holding the prim adhering to this
        schema at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdShadeMaterialBindingAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetCollectionBindingRel(*args, **kwargs):
        """
        
        GetCollectionBindingRel(bindingName, materialPurpose) -> Relationship
        
        
        Returns the collection-based material-binding relationship with the
        given ``bindingName`` and ``materialPurpose`` on this prim.
        
        
        For info on ``bindingName`` , see UsdShadeMaterialBindingAPI::Bind() .
        The material purpose of the relationship that's returned will match
        the specified ``materialPurpose`` .
        
        
        Parameters
        ----------
        bindingName : str
        
        materialPurpose : str
        
        
        """
    @staticmethod
    def GetCollectionBindingRels(*args, **kwargs):
        """
        
        GetCollectionBindingRels(materialPurpose) -> list[Relationship]
        
        
        Returns the list of collection-based material binding relationships on
        this prim for the given material purpose, ``materialPurpose`` .
        
        
        The returned list of binding relationships will be in native property
        order. See UsdPrim::GetPropertyOrder() , UsdPrim::SetPropertyOrder() .
        Bindings that appear earlier in the property order are considered to
        be stronger than the ones that come later. See rule #6 in
        UsdShadeMaterialBindingAPI_MaterialResolution.
        
        
        Parameters
        ----------
        materialPurpose : str
        
        
        """
    @staticmethod
    def GetCollectionBindings(*args, **kwargs):
        """
        
        GetCollectionBindings(materialPurpose) -> list[CollectionBinding]
        
        
        Returns all the collection-based bindings on this prim for the given
        material purpose.
        
        
        The returned CollectionBinding objects always have the specified
        ``materialPurpose`` (i.e. the all-purpose binding is not returned if a
        special purpose binding is requested).
        
        If one or more collection based bindings are to prims that are not
        Materials, this does not generate an error, but the corresponding
        Material(s) will be invalid (i.e. evaluate to false).
        
        The python version of this API returns a tuple containing the vector
        of CollectionBinding objects and the corresponding vector of binding
        relationships.
        
        The returned list of collection-bindings will be in native property
        order of the associated binding relationships. See
        UsdPrim::GetPropertyOrder() , UsdPrim::SetPropertyOrder() . Binding
        relationships that come earlier in the list are considered to be
        stronger than the ones that come later. See rule #6 in
        UsdShadeMaterialBindingAPI_MaterialResolution.
        
        
        Parameters
        ----------
        materialPurpose : str
        
        
        """
    @staticmethod
    def GetDirectBinding(*args, **kwargs):
        """
        
        GetDirectBinding(materialPurpose) -> DirectBinding
        
        
        Computes and returns the direct binding for the given material purpose
        on this prim.
        
        
        The returned binding always has the specified ``materialPurpose``
        (i.e. the all-purpose binding is not returned if a special purpose
        binding is requested).
        
        If the direct binding is to a prim that is not a Material, this does
        not generate an error, but the returned Material will be invalid (i.e.
        evaluate to false).
        
        
        Parameters
        ----------
        materialPurpose : str
        
        
        """
    @staticmethod
    def GetDirectBindingRel(*args, **kwargs):
        """
        
        GetDirectBindingRel(materialPurpose) -> Relationship
        
        
        Returns the direct material-binding relationship on this prim for the
        given material purpose.
        
        
        The material purpose of the relationship that's returned will match
        the specified ``materialPurpose`` .
        
        
        Parameters
        ----------
        materialPurpose : str
        
        
        """
    @staticmethod
    def GetMaterialBindSubsets(*args, **kwargs):
        """
        
        GetMaterialBindSubsets() -> list[Subset]
        
        
        Returns all the existing GeomSubsets with
        familyName=UsdShadeTokens->materialBind below this prim.
        
        
        
        """
    @staticmethod
    def GetMaterialBindSubsetsFamilyType(*args, **kwargs):
        """
        
        GetMaterialBindSubsetsFamilyType() -> str
        
        
        Returns the familyType of the family of"materialBind"GeomSubsets on
        this prim.
        
        
        By default, materialBind subsets have familyType="nonOverlapping", but
        they can also be tagged as a"partition", using
        SetMaterialBindFaceSubsetsFamilyType().
        
        UsdGeomSubset::GetFamilyNameAttr
        
        
        
        """
    @staticmethod
    def GetMaterialBindingStrength(*args, **kwargs):
        """
        
        **classmethod** GetMaterialBindingStrength(bindingRel) -> str
        
        
        Resolves the'bindMaterialAs'token-valued metadata on the given binding
        relationship and returns it.
        
        
        If the resolved value is empty, this returns the fallback value
        UsdShadeTokens->weakerThanDescendants.
        
        UsdShadeMaterialBindingAPI::SetMaterialBindingStrength()
        
        
        Parameters
        ----------
        bindingRel : Relationship
        
        
        """
    @staticmethod
    def GetMaterialPurposes(*args, **kwargs):
        """
        
        **classmethod** GetMaterialPurposes() -> list[str]
        
        
        Returns a vector of the possible values for the'material purpose'.
        
        
        
        """
    @staticmethod
    def GetResolvedTargetPathFromBindingRel(*args, **kwargs):
        """
        
        **classmethod** GetResolvedTargetPathFromBindingRel(bindingRel) -> Path
        
        
        returns the path of the resolved target identified by ``bindingRel`` .
        
        
        Parameters
        ----------
        bindingRel : Relationship
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def RemovePrimFromBindingCollection(*args, **kwargs):
        """
        
        RemovePrimFromBindingCollection(prim, bindingName, materialPurpose) -> bool
        
        
        Removes the specified ``prim`` from the collection targeted by the
        binding relationship corresponding to given ``bindingName`` and
        ``materialPurpose`` .
        
        
        If the collection-binding relationship doesn't exist or if the
        targeted collection does not include the ``prim`` , then this does
        nothing and returns true.
        
        If the targeted collection includes ``prim`` , then this modifies the
        collection by removing the prim from it (by invoking
        UsdCollectionAPI::RemovePrim()). This method can be used in
        conjunction with the Unbind\\*() methods (if desired) to guarantee
        that a prim has no resolved material binding.
        
        
        Parameters
        ----------
        prim : Prim
        
        bindingName : str
        
        materialPurpose : str
        
        
        """
    @staticmethod
    def SetMaterialBindSubsetsFamilyType(*args, **kwargs):
        """
        
        SetMaterialBindSubsetsFamilyType(familyType) -> bool
        
        
        Author the *familyType* of the"materialBind"family of GeomSubsets on
        this prim.
        
        
        The default ``familyType`` is *UsdGeomTokens->nonOverlapping *. It can
        be set to *UsdGeomTokens->partition* to indicate that the entire
        imageable prim is included in the union of all
        the"materialBind"subsets. The family type should never be set to
        UsdGeomTokens->unrestricted, since it is invalid for a single piece of
        geometry (in this case, a subset) to be bound to more than one
        material. Hence, a coding error is issued if ``familyType`` is
        UsdGeomTokens->unrestricted.**
        
        **
        
        UsdGeomSubset::SetFamilyType**
        
        
        Parameters
        ----------
        familyType : str
        
        
        """
    @staticmethod
    def SetMaterialBindingStrength(*args, **kwargs):
        """
        
        **classmethod** SetMaterialBindingStrength(bindingRel, bindingStrength) -> bool
        
        
        Sets the'bindMaterialAs'token-valued metadata on the given binding
        relationship.
        
        
        If ``bindingStrength`` is *UsdShadeTokens->fallbackStrength*, the
        value UsdShadeTokens->weakerThanDescendants is authored sparsely, i.e.
        only when there is a different existing bindingStrength value. To
        stamp out the bindingStrength value explicitly, clients can pass in
        UsdShadeTokens->weakerThanDescendants or
        UsdShadeTokens->strongerThanDescendants directly. Returns true on
        success, false otherwise.
        
        UsdShadeMaterialBindingAPI::GetMaterialBindingStrength()
        
        
        Parameters
        ----------
        bindingRel : Relationship
        
        bindingStrength : str
        
        
        """
    @staticmethod
    def UnbindAllBindings(*args, **kwargs):
        """
        
        UnbindAllBindings() -> bool
        
        
        Unbinds all direct and collection-based bindings on this prim.
        
        
        
        """
    @staticmethod
    def UnbindCollectionBinding(*args, **kwargs):
        """
        
        UnbindCollectionBinding(bindingName, materialPurpose) -> bool
        
        
        Unbinds the collection-based binding with the given ``bindingName`` ,
        for the given ``materialPurpose`` on this prim.
        
        
        It accomplishes this by blocking the targets of the associated binding
        relationship in the current edit target.
        
        If a binding was created without specifying a ``bindingName`` , then
        the correct ``bindingName`` to use for unbinding is the instance name
        of the targetted collection.
        
        
        Parameters
        ----------
        bindingName : str
        
        materialPurpose : str
        
        
        """
    @staticmethod
    def UnbindDirectBinding(*args, **kwargs):
        """
        
        UnbindDirectBinding(materialPurpose) -> bool
        
        
        Unbinds the direct binding for the given material purpose (
        ``materialPurpose`` ) on this prim.
        
        
        It accomplishes this by blocking the targets of the binding
        relationship in the current edit target.
        
        
        Parameters
        ----------
        materialPurpose : str
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdShadeMaterialBindingAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdShadeMaterialBindingAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdShadeMaterialBindingAPI on the prim held by
        ``schemaObj`` .
        
        
        Should be preferred over UsdShadeMaterialBindingAPI
        (schemaObj.GetPrim()), as it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class NodeDefAPI(pxr.Usd.APISchemaBase):
    """
    
    UsdShadeNodeDefAPI is an API schema that provides attributes for a
    prim to select a corresponding Shader Node Definition ("Sdr Node"), as
    well as to look up a runtime entry for that shader node in the form of
    an SdrShaderNode.
    
    UsdShadeNodeDefAPI is intended to be a pre-applied API schema for any
    prim type that wants to refer to the SdrRegistry for further
    implementation details about the behavior of that prim. The primary
    use in UsdShade itself is as UsdShadeShader, which is a basis for
    material shading networks (UsdShadeMaterial), but this is intended to
    be used in other domains that also use the Sdr node mechanism.
    
    This schema provides properties that allow a prim to identify an
    external node definition, either by a direct identifier key into the
    SdrRegistry (info:id), an asset to be parsed by a suitable
    NdrParserPlugin (info:sourceAsset), or an inline source code that must
    also be parsed (info:sourceCode); as well as a selector attribute to
    determine which specifier is active (info:implementationSource).
    
    For any described attribute *Fallback* *Value* or *Allowed* *Values*
    below that are text/tokens, the actual token is published and defined
    in UsdShadeTokens. So to set an attribute to the value"rightHanded",
    use UsdShadeTokens->rightHanded as the value.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Apply(*args, **kwargs):
        """
        
        **classmethod** Apply(prim) -> NodeDefAPI
        
        
        Applies this **single-apply** API schema to the given ``prim`` .
        
        
        This information is stored by adding"NodeDefAPI"to the token-valued,
        listOp metadata *apiSchemas* on the prim.
        
        A valid UsdShadeNodeDefAPI object is returned upon success. An invalid
        (or empty) UsdShadeNodeDefAPI object is returned upon failure. See
        UsdPrim::ApplyAPI() for conditions resulting in failure.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        
        """
    @staticmethod
    def CanApply(*args, **kwargs):
        """
        
        **classmethod** CanApply(prim, whyNot) -> bool
        
        
        Returns true if this **single-apply** API schema can be applied to the
        given ``prim`` .
        
        
        If this schema can not be a applied to the prim, this returns false
        and, if provided, populates ``whyNot`` with the reason it can not be
        applied.
        
        Note that if CanApply returns false, that does not necessarily imply
        that calling Apply will fail. Callers are expected to call CanApply
        before calling Apply if they want to ensure that it is valid to apply
        a schema.
        
        UsdPrim::GetAppliedSchemas()
        
        UsdPrim::HasAPI()
        
        UsdPrim::CanApplyAPI()
        
        UsdPrim::ApplyAPI()
        
        UsdPrim::RemoveAPI()
        
        
        Parameters
        ----------
        prim : Prim
        
        whyNot : str
        
        
        """
    @staticmethod
    def CreateIdAttr(*args, **kwargs):
        """
        
        CreateIdAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetIdAttr() , and also Create vs Get Property Methods for when to
        use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateImplementationSourceAttr(*args, **kwargs):
        """
        
        CreateImplementationSourceAttr(defaultValue, writeSparsely) -> Attribute
        
        
        See GetImplementationSourceAttr() , and also Create vs Get Property
        Methods for when to use Get vs Create.
        
        
        If specified, author ``defaultValue`` as the attribute's default,
        sparsely (when it makes sense to do so) if ``writeSparsely`` is
        ``true`` - the default for ``writeSparsely`` is ``false`` .
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> NodeDefAPI
        
        
        Return a UsdShadeNodeDefAPI holding the prim adhering to this schema
        at ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdShadeNodeDefAPI(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetIdAttr(*args, **kwargs):
        """
        
        GetIdAttr() -> Attribute
        
        
        The id is an identifier for the type or purpose of the shader.
        
        
        E.g.: Texture or FractalFloat. The use of this id will depend on the
        render target: some will turn it into an actual shader path, some will
        use it to generate shader source code dynamically.
        
        SetShaderId()
        
        Declaration
        
        ``uniform token info:id``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        
        
        """
    @staticmethod
    def GetImplementationSource(*args, **kwargs):
        """
        
        GetImplementationSource() -> str
        
        
        Reads the value of info:implementationSource attribute and returns a
        token identifying the attribute that must be consulted to identify the
        shader's source program.
        
        
        This returns
        
           - **id**, to indicate that the"info:id"attribute must be consulted.
        
           - **sourceAsset** to indicate that the asset-
             valued"info:{sourceType}:sourceAsset"attribute associated with the
             desired **sourceType** should be consulted to locate the asset with
             the shader's source.
        
           - **sourceCode** to indicate that the string-
             valued"info:{sourceType}:sourceCode"attribute associated with the
             desired **sourceType** should be read to get shader's source.
        
        This issues a warning and returns **id** if the
        *info:implementationSource* attribute has an invalid value.
        
        *{sourceType}* above is a place holder for a token that identifies the
        type of shader source or its implementation. For example: osl, glslfx,
        riCpp etc. This allows a shader to specify different sourceAsset (or
        sourceCode) values for different sourceTypes. The sourceType tokens
        usually correspond to the sourceType value of the NdrParserPlugin
        that's used to parse the shader source (NdrParserPlugin::SourceType).
        
        When sourceType is empty, the corresponding sourceAsset or sourceCode
        is considered to be"universal"(or fallback), which is represented by
        the empty-valued token UsdShadeTokens->universalSourceType. When the
        sourceAsset (or sourceCode) corresponding to a specific, requested
        sourceType is unavailable, the universal sourceAsset (or sourceCode)
        is returned by GetSourceAsset (and GetSourceCode} API, if present.
        
        GetShaderId()
        
        GetSourceAsset()
        
        GetSourceCode()
        
        
        
        """
    @staticmethod
    def GetImplementationSourceAttr(*args, **kwargs):
        """
        
        GetImplementationSourceAttr() -> Attribute
        
        
        Specifies the attribute that should be consulted to get the shader's
        implementation or its source code.
        
        
        
           - If set to"id", the"info:id"attribute's value is used to determine
             the shader source from the shader registry.
        
           - If set to"sourceAsset", the resolved value of
             the"info:sourceAsset"attribute corresponding to the desired
             implementation (or source-type) is used to locate the shader source. A
             source asset file may also specify multiple shader definitions, so
             there is an optional attribute"info:sourceAsset:subIdentifier"whose
             value should be used to indicate a particular shader definition from a
             source asset file.
        
           - If set to"sourceCode", the value of"info:sourceCode"attribute
             corresponding to the desired implementation (or source type) is used
             as the shader source.
        
        Declaration
        
        ``uniform token info:implementationSource ="id"``
        
        C++ Type
        
        TfToken
        
        Usd Type
        
        SdfValueTypeNames->Token
        
        Variability
        
        SdfVariabilityUniform
        
        Allowed Values
        
        id, sourceAsset, sourceCode
        
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def GetShaderId(*args, **kwargs):
        """
        
        GetShaderId(id) -> bool
        
        
        Fetches the shader's ID value from the *info:id* attribute, if the
        shader's *info:implementationSource* is **id**.
        
        
        Returns **true** if the shader's implementation source is **id** and
        the value was fetched properly into ``id`` . Returns false otherwise.
        
        GetImplementationSource()
        
        
        Parameters
        ----------
        id : str
        
        
        """
    @staticmethod
    def GetShaderNodeForSourceType(*args, **kwargs):
        """
        
        GetShaderNodeForSourceType(sourceType) -> ShaderNode
        
        
        This method attempts to ensure that there is a ShaderNode in the
        shader registry (i.e.
        
        
        SdrRegistry) representing this shader for the given ``sourceType`` .
        It may return a null pointer if none could be found or created.
        
        
        Parameters
        ----------
        sourceType : str
        
        
        """
    @staticmethod
    def GetSourceAsset(*args, **kwargs):
        """
        
        GetSourceAsset(sourceAsset, sourceType) -> bool
        
        
        Fetches the shader's source asset value for the specified
        ``sourceType`` value from the **info: *sourceType*: sourceAsset**
        attribute, if the shader's *info:implementationSource* is
        **sourceAsset**.
        
        
        If the *sourceAsset* attribute corresponding to the requested
        *sourceType* isn't present on the shader, then the *universal*
        *fallback* sourceAsset attribute, i.e. *info:sourceAsset* is
        consulted, if present, to get the source asset path.
        
        Returns **true** if the shader's implementation source is
        **sourceAsset** and the source asset path value was fetched
        successfully into ``sourceAsset`` . Returns false otherwise.
        
        GetImplementationSource()
        
        
        Parameters
        ----------
        sourceAsset : AssetPath
        
        sourceType : str
        
        
        """
    @staticmethod
    def GetSourceAssetSubIdentifier(*args, **kwargs):
        """
        
        GetSourceAssetSubIdentifier(subIdentifier, sourceType) -> bool
        
        
        Fetches the shader's sub-identifier for the source asset with the
        specified ``sourceType`` value from the **info: *sourceType*:
        sourceAsset:subIdentifier** attribute, if the shader's *info:
        implementationSource* is **sourceAsset**.
        
        
        If the *subIdentifier* attribute corresponding to the requested
        *sourceType* isn't present on the shader, then the *universal*
        *fallback* sub-identifier attribute, i.e. *info:sourceAsset:
        subIdentifier* is consulted, if present, to get the sub-identifier
        name.
        
        Returns **true** if the shader's implementation source is
        **sourceAsset** and the sub-identifier for the given source type was
        fetched successfully into ``subIdentifier`` . Returns false otherwise.
        
        
        Parameters
        ----------
        subIdentifier : str
        
        sourceType : str
        
        
        """
    @staticmethod
    def GetSourceCode(*args, **kwargs):
        """
        
        GetSourceCode(sourceCode, sourceType) -> bool
        
        
        Fetches the shader's source code for the specified ``sourceType``
        value by reading the **info: *sourceType*: sourceCode** attribute, if
        the shader's *info:implementationSource* is **sourceCode**.
        
        
        If the *sourceCode* attribute corresponding to the requested
        *sourceType* isn't present on the shader, then the *universal* or
        *fallback* sourceCode attribute (i.e. *info:sourceCode*) is consulted,
        if present, to get the source code.
        
        Returns **true** if the shader's implementation source is
        **sourceCode** and the source code string was fetched successfully
        into ``sourceCode`` . Returns false otherwise.
        
        GetImplementationSource()
        
        
        Parameters
        ----------
        sourceCode : str
        
        sourceType : str
        
        
        """
    @staticmethod
    def SetShaderId(*args, **kwargs):
        """
        
        SetShaderId(id) -> bool
        
        
        Sets the shader's ID value.
        
        
        This also sets the *info:implementationSource* attribute on the shader
        to **UsdShadeTokens->id**, if the existing value is different.
        
        
        Parameters
        ----------
        id : str
        
        
        """
    @staticmethod
    def SetSourceAsset(*args, **kwargs):
        """
        
        SetSourceAsset(sourceAsset, sourceType) -> bool
        
        
        Sets the shader's source-asset path value to ``sourceAsset`` for the
        given source type, ``sourceType`` .
        
        
        This also sets the *info:implementationSource* attribute on the shader
        to **UsdShadeTokens->sourceAsset**.
        
        
        Parameters
        ----------
        sourceAsset : AssetPath
        
        sourceType : str
        
        
        """
    @staticmethod
    def SetSourceAssetSubIdentifier(*args, **kwargs):
        """
        
        SetSourceAssetSubIdentifier(subIdentifier, sourceType) -> bool
        
        
        Set a sub-identifier to be used with a source asset of the given
        source type.
        
        
        This sets the **info: *sourceType*: sourceAsset:subIdentifier**.
        
        This also sets the *info:implementationSource* attribute on the shader
        to **UsdShadeTokens->sourceAsset**
        
        
        Parameters
        ----------
        subIdentifier : str
        
        sourceType : str
        
        
        """
    @staticmethod
    def SetSourceCode(*args, **kwargs):
        """
        
        SetSourceCode(sourceCode, sourceType) -> bool
        
        
        Sets the shader's source-code value to ``sourceCode`` for the given
        source type, ``sourceType`` .
        
        
        This also sets the *info:implementationSource* attribute on the shader
        to **UsdShadeTokens->sourceCode**.
        
        
        Parameters
        ----------
        sourceCode : str
        
        sourceType : str
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdShadeNodeDefAPI on UsdPrim ``prim`` .
        
        
        Equivalent to UsdShadeNodeDefAPI::Get (prim.GetStage(),
        prim.GetPath()) for a *valid* ``prim`` , but will not immediately
        throw an error for an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdShadeNodeDefAPI on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdShadeNodeDefAPI (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class NodeGraph(pxr.Usd.Typed):
    """
    
    A node-graph is a container for shading nodes, as well as other node-
    graphs. It has a public input interface and provides a list of public
    outputs.
    
    **Node Graph Interfaces**
    
    One of the most important functions of a node-graph is to host
    the"interface"with which clients of already-built shading networks
    will interact. Please see Interface Inputs for a detailed explanation
    of what the interface provides, and how to construct and use it, to
    effectively share/instance shader networks.
    
    **Node Graph Outputs**
    
    These behave like outputs on a shader and are typically connected to
    an output on a shader inside the node-graph.
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def ComputeInterfaceInputConsumersMap(*args, **kwargs):
        """
        
        ComputeInterfaceInputConsumersMap(computeTransitiveConsumers) -> InterfaceInputConsumersMap
        
        
        Walks the namespace subtree below the node-graph and computes a map
        containing the list of all inputs on the node-graph and the associated
        vector of consumers of their values.
        
        
        The consumers can be inputs on shaders within the node-graph or on
        nested node-graphs).
        
        If ``computeTransitiveConsumers`` is true, then value consumers
        belonging to **node-graphs** are resolved transitively to compute the
        transitive mapping from inputs on the node-graph to inputs on shaders
        inside the material. Note that inputs on node-graphs that don't have
        value consumers will continue to be included in the result.
        
        This API is provided for use by DCC's that want to present node-graph
        interface / shader connections in the opposite direction than they are
        encoded in USD.
        
        
        Parameters
        ----------
        computeTransitiveConsumers : bool
        
        
        """
    @staticmethod
    def ComputeOutputSource(*args, **kwargs):
        """
        
        ComputeOutputSource(outputName, sourceName, sourceType) -> Shader
        
        
        Deprecated
        
        in favor of GetValueProducingAttributes on UsdShadeOutput Resolves the
        connection source of the requested output, identified by
        ``outputName`` to a shader output.
        
        ``sourceName`` is an output parameter that is set to the name of the
        resolved output, if the node-graph output is connected to a valid
        shader source.
        
        ``sourceType`` is an output parameter that is set to the type of the
        resolved output, if the node-graph output is connected to a valid
        shader source.
        
        Returns a valid shader object if the specified output exists and is
        connected to one. Return an empty shader object otherwise. The python
        version of this method returns a tuple containing three elements (the
        source shader, sourceName, sourceType).
        
        
        Parameters
        ----------
        outputName : str
        
        sourceName : str
        
        sourceType : AttributeType
        
        
        """
    @staticmethod
    def ConnectableAPI(*args, **kwargs):
        """
        
        ConnectableAPI() -> ConnectableAPI
        
        
        Contructs and returns a UsdShadeConnectableAPI object with this node-
        graph.
        
        
        Note that most tasks can be accomplished without explicitly
        constructing a UsdShadeConnectable API, since connection-related API
        such as UsdShadeConnectableAPI::ConnectToSource() are static methods,
        and UsdShadeNodeGraph will auto-convert to a UsdShadeConnectableAPI
        when passed to functions that want to act generically on a connectable
        UsdShadeConnectableAPI object.
        
        
        
        """
    @staticmethod
    def CreateInput(*args, **kwargs):
        """
        
        CreateInput(name, typeName) -> Input
        
        
        Create an Input which can either have a value or can be connected.
        
        
        The attribute representing the input is created in
        the"inputs:"namespace.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def CreateOutput(*args, **kwargs):
        """
        
        CreateOutput(name, typeName) -> Output
        
        
        Create an output which can either have a value or can be connected.
        
        
        The attribute representing the output is created in
        the"outputs:"namespace.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> NodeGraph
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> NodeGraph
        
        
        Return a UsdShadeNodeGraph holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdShadeNodeGraph(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetInput(*args, **kwargs):
        """
        
        GetInput(name) -> Input
        
        
        Return the requested input if it exists.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetInputs(*args, **kwargs):
        """
        
        GetInputs(onlyAuthored) -> list[Input]
        
        
        Returns all inputs present on the node-graph.
        
        
        These are represented by attributes in the"inputs:"namespace. If
        ``onlyAuthored`` is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
        """
    @staticmethod
    def GetInterfaceInputs(*args, **kwargs):
        """
        
        GetInterfaceInputs() -> list[Input]
        
        
        Returns all the"Interface Inputs"of the node-graph.
        
        
        This is the same as GetInputs() , but is provided as a convenience, to
        allow clients to distinguish between inputs on shaders vs. interface-
        inputs on node-graphs.
        
        
        
        """
    @staticmethod
    def GetOutput(*args, **kwargs):
        """
        
        GetOutput(name) -> Output
        
        
        Return the requested output if it exists.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetOutputs(*args, **kwargs):
        """
        
        GetOutputs(onlyAuthored) -> list[Output]
        
        
        Outputs are represented by attributes in the"outputs:"namespace.
        
        
        If ``onlyAuthored`` is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(prim)
        
        
        Construct a UsdShadeNodeGraph on UsdPrim ``prim`` .
        
        
        Equivalent to UsdShadeNodeGraph::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdShadeNodeGraph on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdShadeNodeGraph (schemaObj.GetPrim()), as
        it preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        
        ----------------------------------------------------------------------
        
        __init__(connectable)
        
        
        Constructor that takes a ConnectableAPI object.
        
        
        Allow implicit (auto) conversion of UsdShadeConnectableAPI to
        UsdShadeNodeGraph, so that a ConnectableAPI can be passed into any
        function that accepts a NodeGraph.
        
        that the conversion may produce an invalid NodeGraph object, because
        not all UsdShadeConnectableAPI s are UsdShadeNodeGraph s
        
        
        Parameters
        ----------
        connectable : ConnectableAPI
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Output(Boost.Python.instance):
    """
    
    This class encapsulates a shader or node-graph output, which is a
    connectable attribute representing a typed, externally computed value.
    
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CanConnect(*args, **kwargs):
        """
        
        CanConnect(source) -> bool
        
        
        Determines whether this Output can be connected to the given source
        attribute, which can be an input or an output.
        
        
        An output is considered to be connectable only if it belongs to a
        node-graph. Shader outputs are not connectable.
        
        UsdShadeConnectableAPI::CanConnect
        
        
        Parameters
        ----------
        source : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        CanConnect(sourceInput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        sourceInput : Input
        
        
        
        ----------------------------------------------------------------------
        
        CanConnect(sourceOutput) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        sourceOutput : Output
        
        
        """
    @staticmethod
    def ClearSdrMetadata(*args, **kwargs):
        """
        
        ClearSdrMetadata() -> None
        
        
        Clears any"sdrMetadata"value authored on the Output in the current
        EditTarget.
        
        
        
        """
    @staticmethod
    def ClearSdrMetadataByKey(*args, **kwargs):
        """
        
        ClearSdrMetadataByKey(key) -> None
        
        
        Clears the entry corresponding to the given ``key`` in
        the"sdrMetadata"dictionary authored in the current EditTarget.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def ClearSource(*args, **kwargs):
        """
        
        ClearSource() -> bool
        
        
        Deprecated
        
        
        
        """
    @staticmethod
    def ClearSources(*args, **kwargs):
        """
        
        ClearSources() -> bool
        
        
        Clears sources for this Output in the current UsdEditTarget.
        
        
        Most of the time, what you probably want is DisconnectSource() rather
        than this function.
        
        UsdShadeConnectableAPI::ClearSources
        
        
        
        """
    @staticmethod
    def ConnectToSource(*args, **kwargs):
        """
        
        ConnectToSource(source, mod) -> bool
        
        
        Authors a connection for this Output.
        
        
        ``source`` is a struct that describes the upstream source attribute
        with all the information necessary to make a connection. See the
        documentation for UsdShadeConnectionSourceInfo. ``mod`` describes the
        operation that should be applied to the list of connections. By
        default the new connection will replace any existing connections, but
        it can add to the list of connections to represent multiple input
        connections.
        
        ``true`` if a connection was created successfully. ``false`` if
        ``shadingAttr`` or ``source`` is invalid.
        
        This method does not verify the connectability of the shading
        attribute to the source. Clients must invoke CanConnect() themselves
        to ensure compatibility.
        
        The source shading attribute is created if it doesn't exist already.
        
        UsdShadeConnectableAPI::ConnectToSource
        
        
        Parameters
        ----------
        source : ConnectionSourceInfo
        
        mod : ConnectionModification
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(source, sourceName, sourceType, typeName) -> bool
        
        
        Deprecated
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        source : ConnectableAPI
        
        sourceName : str
        
        sourceType : AttributeType
        
        typeName : ValueTypeName
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(sourcePath) -> bool
        
        
        Authors a connection for this Output to the source at the given path.
        
        
        
        UsdShadeConnectableAPI::ConnectToSource
        
        
        Parameters
        ----------
        sourcePath : Path
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(sourceInput) -> bool
        
        
        Connects this Output to the given input, ``sourceInput`` .
        
        
        
        UsdShadeConnectableAPI::ConnectToSource
        
        
        Parameters
        ----------
        sourceInput : Input
        
        
        
        ----------------------------------------------------------------------
        
        ConnectToSource(sourceOutput) -> bool
        
        
        Connects this Output to the given output, ``sourceOutput`` .
        
        
        
        UsdShadeConnectableAPI::ConnectToSource
        
        
        Parameters
        ----------
        sourceOutput : Output
        
        
        """
    @staticmethod
    def DisconnectSource(*args, **kwargs):
        """
        
        DisconnectSource(sourceAttr) -> bool
        
        
        Disconnect source for this Output.
        
        
        If ``sourceAttr`` is valid, only a connection to the specified
        attribute is disconnected, otherwise all connections are removed.
        
        UsdShadeConnectableAPI::DisconnectSource
        
        
        Parameters
        ----------
        sourceAttr : Attribute
        
        
        """
    @staticmethod
    def GetAttr(*args, **kwargs):
        """
        
        GetAttr() -> Attribute
        
        
        Explicit UsdAttribute extractor.
        
        
        
        """
    @staticmethod
    def GetBaseName(*args, **kwargs):
        """
        
        GetBaseName() -> str
        
        
        Returns the name of the output.
        
        
        We call this the base name since it strips off the"outputs:"namespace
        prefix from the attribute name, and returns it.
        
        
        
        """
    @staticmethod
    def GetConnectedSource(*args, **kwargs):
        """
        
        GetConnectedSource(source, sourceName, sourceType) -> bool
        
        
        Deprecated
        
        Please use GetConnectedSources instead
        
        
        Parameters
        ----------
        source : ConnectableAPI
        
        sourceName : str
        
        sourceType : AttributeType
        
        
        """
    @staticmethod
    def GetConnectedSources(*args, **kwargs):
        """
        
        GetConnectedSources(invalidSourcePaths) -> list[SourceInfo]
        
        
        Finds the valid sources of connections for the Output.
        
        
        ``invalidSourcePaths`` is an optional output parameter to collect the
        invalid source paths that have not been reported in the returned
        vector.
        
        Returns a vector of ``UsdShadeConnectionSourceInfo`` structs with
        information about each upsteam attribute. If the vector is empty,
        there have been no valid connections.
        
        A valid connection requires the existence of the source attribute and
        also requires that the source prim is UsdShadeConnectableAPI
        compatible.
        
        The python wrapping returns a tuple with the valid connections first,
        followed by the invalid source paths.
        
        UsdShadeConnectableAPI::GetConnectedSources
        
        
        Parameters
        ----------
        invalidSourcePaths : list[Path]
        
        
        """
    @staticmethod
    def GetFullName(*args, **kwargs):
        """
        
        GetFullName() -> str
        
        
        Get the name of the attribute associated with the output.
        
        
        
        """
    @staticmethod
    def GetPrim(*args, **kwargs):
        """
        
        GetPrim() -> Prim
        
        
        Get the prim that the output belongs to.
        
        
        
        """
    @staticmethod
    def GetRawConnectedSourcePaths(*args, **kwargs):
        """
        
        GetRawConnectedSourcePaths(sourcePaths) -> bool
        
        
        Deprecated
        
        Returns the"raw"(authored) connected source paths for this Output.
        
        UsdShadeConnectableAPI::GetRawConnectedSourcePaths
        
        
        Parameters
        ----------
        sourcePaths : list[Path]
        
        
        """
    @staticmethod
    def GetRenderType(*args, **kwargs):
        """
        
        GetRenderType() -> str
        
        
        Return this output's specialized renderType, or an empty token if none
        was authored.
        
        
        
        SetRenderType()
        
        
        
        """
    @staticmethod
    def GetSdrMetadata(*args, **kwargs):
        """
        
        GetSdrMetadata() -> NdrTokenMap
        
        
        Returns this Output's composed"sdrMetadata"dictionary as a
        NdrTokenMap.
        
        
        
        """
    @staticmethod
    def GetSdrMetadataByKey(*args, **kwargs):
        """
        
        GetSdrMetadataByKey(key) -> str
        
        
        Returns the value corresponding to ``key`` in the composed
        **sdrMetadata** dictionary.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def GetTypeName(*args, **kwargs):
        """
        
        GetTypeName() -> ValueTypeName
        
        
        Get the"scene description"value type name of the attribute associated
        with the output.
        
        
        
        """
    @staticmethod
    def GetValueProducingAttributes(*args, **kwargs):
        """
        
        GetValueProducingAttributes(shaderOutputsOnly) -> list[UsdShadeAttribute]
        
        
        Find what is connected to this Output recursively.
        
        
        
        UsdShadeUtils::GetValueProducingAttributes
        
        
        Parameters
        ----------
        shaderOutputsOnly : bool
        
        
        """
    @staticmethod
    def HasConnectedSource(*args, **kwargs):
        """
        
        HasConnectedSource() -> bool
        
        
        Returns true if and only if this Output is currently connected to a
        valid (defined) source.
        
        
        
        UsdShadeConnectableAPI::HasConnectedSource
        
        
        
        """
    @staticmethod
    def HasRenderType(*args, **kwargs):
        """
        
        HasRenderType() -> bool
        
        
        Return true if a renderType has been specified for this output.
        
        
        
        SetRenderType()
        
        
        
        """
    @staticmethod
    def HasSdrMetadata(*args, **kwargs):
        """
        
        HasSdrMetadata() -> bool
        
        
        Returns true if the Output has a non-empty
        composed"sdrMetadata"dictionary value.
        
        
        
        """
    @staticmethod
    def HasSdrMetadataByKey(*args, **kwargs):
        """
        
        HasSdrMetadataByKey(key) -> bool
        
        
        Returns true if there is a value corresponding to the given ``key`` in
        the composed"sdrMetadata"dictionary.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def IsOutput(*args, **kwargs):
        """
        
        **classmethod** IsOutput(attr) -> bool
        
        
        Test whether a given UsdAttribute represents a valid Output, which
        implies that creating a UsdShadeOutput from the attribute will
        succeed.
        
        
        Success implies that ``attr.IsDefined()`` is true.
        
        
        Parameters
        ----------
        attr : Attribute
        
        
        """
    @staticmethod
    def IsSourceConnectionFromBaseMaterial(*args, **kwargs):
        """
        
        IsSourceConnectionFromBaseMaterial() -> bool
        
        
        Returns true if the connection to this Output's source, as returned by
        GetConnectedSource() , is authored across a specializes arc, which is
        used to denote a base material.
        
        
        
        UsdShadeConnectableAPI::IsSourceConnectionFromBaseMaterial
        
        
        
        """
    @staticmethod
    def Set(*args, **kwargs):
        """
        
        Set(value, time) -> bool
        
        
        Set a value for the output.
        
        
        It's unusual to be setting a value on an output since it represents an
        externally computed value. The Set API is provided here just for the
        sake of completeness and uniformity with other property schema.
        
        
        Parameters
        ----------
        value : VtValue
        
        time : TimeCode
        
        
        
        ----------------------------------------------------------------------
        
        Set(value, time) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        Set the attribute value of the Output at ``time`` .
        
        
        Parameters
        ----------
        value : T
        
        time : TimeCode
        
        
        """
    @staticmethod
    def SetConnectedSources(*args, **kwargs):
        """
        
        SetConnectedSources(sourceInfos) -> bool
        
        
        Connects this Output to the given sources, ``sourceInfos`` .
        
        
        
        UsdShadeConnectableAPI::SetConnectedSources
        
        
        Parameters
        ----------
        sourceInfos : list[ConnectionSourceInfo]
        
        
        """
    @staticmethod
    def SetRenderType(*args, **kwargs):
        """
        
        SetRenderType(renderType) -> bool
        
        
        Specify an alternative, renderer-specific type to use when
        emitting/translating this output, rather than translating based on its
        GetTypeName()
        
        
        For example, we set the renderType to"struct"for outputs that are of
        renderman custom struct types.
        
        true on success
        
        
        Parameters
        ----------
        renderType : str
        
        
        """
    @staticmethod
    def SetSdrMetadata(*args, **kwargs):
        """
        
        SetSdrMetadata(sdrMetadata) -> None
        
        
        Authors the given ``sdrMetadata`` value on this Output at the current
        EditTarget.
        
        
        Parameters
        ----------
        sdrMetadata : NdrTokenMap
        
        
        """
    @staticmethod
    def SetSdrMetadataByKey(*args, **kwargs):
        """
        
        SetSdrMetadataByKey(key, value) -> None
        
        
        Sets the value corresponding to ``key`` to the given string ``value``
        , in the Output's"sdrMetadata"dictionary at the current EditTarget.
        
        
        Parameters
        ----------
        key : str
        
        value : str
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(attr)
        
        
        Speculative constructor that will produce a valid UsdShadeOutput when
        ``attr`` already represents a shade Output, and produces an *invalid*
        UsdShadeOutput otherwise (i.e.
        
        
        the explicit bool conversion operator will return false).
        
        
        Parameters
        ----------
        attr : Attribute
        
        
        
        ----------------------------------------------------------------------
        
        __init__()
        
        
        Default constructor returns an invalid Output.
        
        
        Exists for container classes
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim, name, typeName)
        
        
        Parameters
        ----------
        prim : Prim
        
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Shader(pxr.Usd.Typed):
    """
    
    Base class for all USD shaders. Shaders are the building blocks of
    shading networks. While UsdShadeShader objects are not target
    specific, each renderer or application target may derive its own
    renderer-specific shader object types from this base, if needed.
    
    Objects of this class generally represent a single shading object,
    whether it exists in the target renderer or not. For example, a
    texture, a fractal, or a mix node.
    
    The UsdShadeNodeDefAPI provides attributes to uniquely identify the
    type of this node. The id resolution into a renderable shader target
    type of this node. The id resolution into a renderable shader target
    is deferred to the consuming application.
    
    The purpose of representing them in Usd is two-fold:
    
       - To represent, via"connections"the topology of the shading network
         that must be reconstructed in the renderer. Facilities for authoring
         and manipulating connections are encapsulated in the API schema
         UsdShadeConnectableAPI.
    
       - To present a (partial or full) interface of typed input
         parameters whose values can be set and overridden in Usd, to be
         provided later at render-time as parameter values to the actual render
         shader objects. Shader input parameters are encapsulated in the
         property schema UsdShadeInput.
    
    
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def ClearSdrMetadata(*args, **kwargs):
        """
        
        ClearSdrMetadata() -> None
        
        
        Clears any"sdrMetadata"value authored on the shader in the current
        EditTarget.
        
        
        
        """
    @staticmethod
    def ClearSdrMetadataByKey(*args, **kwargs):
        """
        
        ClearSdrMetadataByKey(key) -> None
        
        
        Clears the entry corresponding to the given ``key`` in
        the"sdrMetadata"dictionary authored in the current EditTarget.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def ConnectableAPI(*args, **kwargs):
        """
        
        ConnectableAPI() -> ConnectableAPI
        
        
        Contructs and returns a UsdShadeConnectableAPI object with this
        shader.
        
        
        Note that most tasks can be accomplished without explicitly
        constructing a UsdShadeConnectable API, since connection-related API
        such as UsdShadeConnectableAPI::ConnectToSource() are static methods,
        and UsdShadeShader will auto-convert to a UsdShadeConnectableAPI when
        passed to functions that want to act generically on a connectable
        UsdShadeConnectableAPI object.
        
        
        
        """
    @staticmethod
    def CreateIdAttr(*args, **kwargs):
        """
        
        CreateIdAttr(defaultValue, writeSparsely) -> Attribute
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateImplementationSourceAttr(*args, **kwargs):
        """
        
        CreateImplementationSourceAttr(defaultValue, writeSparsely) -> Attribute
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        Parameters
        ----------
        defaultValue : VtValue
        
        writeSparsely : bool
        
        
        """
    @staticmethod
    def CreateInput(*args, **kwargs):
        """
        
        CreateInput(name, typeName) -> Input
        
        
        Create an input which can either have a value or can be connected.
        
        
        The attribute representing the input is created in
        the"inputs:"namespace. Inputs on both shaders and node-graphs are
        connectable.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def CreateOutput(*args, **kwargs):
        """
        
        CreateOutput(name, typeName) -> Output
        
        
        Create an output which can either have a value or can be connected.
        
        
        The attribute representing the output is created in
        the"outputs:"namespace. Outputs on a shader cannot be connected, as
        their value is assumed to be computed externally.
        
        
        Parameters
        ----------
        name : str
        
        typeName : ValueTypeName
        
        
        """
    @staticmethod
    def Define(*args, **kwargs):
        """
        
        **classmethod** Define(stage, path) -> Shader
        
        
        Attempt to ensure a *UsdPrim* adhering to this schema at ``path`` is
        defined (according to UsdPrim::IsDefined() ) on this stage.
        
        
        If a prim adhering to this schema at ``path`` is already defined on
        this stage, return that prim. Otherwise author an *SdfPrimSpec* with
        *specifier* == *SdfSpecifierDef* and this schema's prim type name for
        the prim at ``path`` at the current EditTarget. Author *SdfPrimSpec* s
        with ``specifier`` == *SdfSpecifierDef* and empty typeName at the
        current EditTarget for any nonexistent, or existing but not *Defined*
        ancestors.
        
        The given *path* must be an absolute prim path that does not contain
        any variant selections.
        
        If it is impossible to author any of the necessary PrimSpecs, (for
        example, in case *path* cannot map to the current UsdEditTarget 's
        namespace) issue an error and return an invalid *UsdPrim*.
        
        Note that this method may return a defined prim whose typeName does
        not specify this schema class, in case a stronger typeName opinion
        overrides the opinion at the current EditTarget.
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def Get(*args, **kwargs):
        """
        
        **classmethod** Get(stage, path) -> Shader
        
        
        Return a UsdShadeShader holding the prim adhering to this schema at
        ``path`` on ``stage`` .
        
        
        If no prim exists at ``path`` on ``stage`` , or if the prim at that
        path does not adhere to this schema, return an invalid schema object.
        This is shorthand for the following:
        
        .. code-block:: text
        
          UsdShadeShader(stage->GetPrimAtPath(path));
        
        
        
        Parameters
        ----------
        stage : Stage
        
        path : Path
        
        
        """
    @staticmethod
    def GetIdAttr(*args, **kwargs):
        """
        
        GetIdAttr() -> Attribute
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        
        """
    @staticmethod
    def GetImplementationSource(*args, **kwargs):
        """
        
        GetImplementationSource() -> str
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        
        """
    @staticmethod
    def GetImplementationSourceAttr(*args, **kwargs):
        """
        
        GetImplementationSourceAttr() -> Attribute
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        
        """
    @staticmethod
    def GetInput(*args, **kwargs):
        """
        
        GetInput(name) -> Input
        
        
        Return the requested input if it exists.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetInputs(*args, **kwargs):
        """
        
        GetInputs(onlyAuthored) -> list[Input]
        
        
        Inputs are represented by attributes in the"inputs:"namespace.
        
        
        If ``onlyAuthored`` is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
        """
    @staticmethod
    def GetOutput(*args, **kwargs):
        """
        
        GetOutput(name) -> Output
        
        
        Return the requested output if it exists.
        
        
        Parameters
        ----------
        name : str
        
        
        """
    @staticmethod
    def GetOutputs(*args, **kwargs):
        """
        
        GetOutputs(onlyAuthored) -> list[Output]
        
        
        Outputs are represented by attributes in the"outputs:"namespace.
        
        
        If ``onlyAuthored`` is true (the default), then only return authored
        attributes; otherwise, this also returns un-authored builtins.
        
        
        Parameters
        ----------
        onlyAuthored : bool
        
        
        """
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        """
        
        **classmethod** GetSchemaAttributeNames(includeInherited) -> list[str]
        
        
        Return a vector of names of all pre-declared attributes for this
        schema class and all its ancestor classes.
        
        
        Does not include attributes that may be authored by custom/extended
        methods of the schemas involved.
        
        
        Parameters
        ----------
        includeInherited : bool
        
        
        """
    @staticmethod
    def GetSdrMetadata(*args, **kwargs):
        """
        
        GetSdrMetadata() -> NdrTokenMap
        
        
        Returns this shader's composed"sdrMetadata"dictionary as a
        NdrTokenMap.
        
        
        
        """
    @staticmethod
    def GetSdrMetadataByKey(*args, **kwargs):
        """
        
        GetSdrMetadataByKey(key) -> str
        
        
        Returns the value corresponding to ``key`` in the composed
        **sdrMetadata** dictionary.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def GetShaderId(*args, **kwargs):
        """
        
        GetShaderId(id) -> bool
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        Parameters
        ----------
        id : str
        
        
        """
    @staticmethod
    def GetShaderNodeForSourceType(*args, **kwargs):
        """
        
        GetShaderNodeForSourceType(sourceType) -> ShaderNode
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        Parameters
        ----------
        sourceType : str
        
        
        """
    @staticmethod
    def GetSourceAsset(*args, **kwargs):
        """
        
        GetSourceAsset(sourceAsset, sourceType) -> bool
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        Parameters
        ----------
        sourceAsset : AssetPath
        
        sourceType : str
        
        
        """
    @staticmethod
    def GetSourceAssetSubIdentifier(*args, **kwargs):
        """
        
        GetSourceAssetSubIdentifier(subIdentifier, sourceType) -> bool
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        Parameters
        ----------
        subIdentifier : str
        
        sourceType : str
        
        
        """
    @staticmethod
    def GetSourceCode(*args, **kwargs):
        """
        
        GetSourceCode(sourceCode, sourceType) -> bool
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        Parameters
        ----------
        sourceCode : str
        
        sourceType : str
        
        
        """
    @staticmethod
    def HasSdrMetadata(*args, **kwargs):
        """
        
        HasSdrMetadata() -> bool
        
        
        Returns true if the shader has a non-empty
        composed"sdrMetadata"dictionary value.
        
        
        
        """
    @staticmethod
    def HasSdrMetadataByKey(*args, **kwargs):
        """
        
        HasSdrMetadataByKey(key) -> bool
        
        
        Returns true if there is a value corresponding to the given ``key`` in
        the composed"sdrMetadata"dictionary.
        
        
        Parameters
        ----------
        key : str
        
        
        """
    @staticmethod
    def SetSdrMetadata(*args, **kwargs):
        """
        
        SetSdrMetadata(sdrMetadata) -> None
        
        
        Authors the given ``sdrMetadata`` on this shader at the current
        EditTarget.
        
        
        Parameters
        ----------
        sdrMetadata : NdrTokenMap
        
        
        """
    @staticmethod
    def SetSdrMetadataByKey(*args, **kwargs):
        """
        
        SetSdrMetadataByKey(key, value) -> None
        
        
        Sets the value corresponding to ``key`` to the given string ``value``
        , in the shader's"sdrMetadata"dictionary at the current EditTarget.
        
        
        Parameters
        ----------
        key : str
        
        value : str
        
        
        """
    @staticmethod
    def SetShaderId(*args, **kwargs):
        """
        
        SetShaderId(id) -> bool
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        Parameters
        ----------
        id : str
        
        
        """
    @staticmethod
    def SetSourceAsset(*args, **kwargs):
        """
        
        SetSourceAsset(sourceAsset, sourceType) -> bool
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        Parameters
        ----------
        sourceAsset : AssetPath
        
        sourceType : str
        
        
        """
    @staticmethod
    def SetSourceAssetSubIdentifier(*args, **kwargs):
        """
        
        SetSourceAssetSubIdentifier(subIdentifier, sourceType) -> bool
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        Parameters
        ----------
        subIdentifier : str
        
        sourceType : str
        
        
        """
    @staticmethod
    def SetSourceCode(*args, **kwargs):
        """
        
        SetSourceCode(sourceCode, sourceType) -> bool
        
        
        Forwards to UsdShadeNodeDefAPI(prim).
        
        
        Parameters
        ----------
        sourceCode : str
        
        sourceType : str
        
        
        """
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        """
        
        **classmethod** _GetStaticTfType() -> Type
        
        
        
        """
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(connectable)
        
        
        Constructor that takes a ConnectableAPI object.
        
        
        Allow implicit (auto) conversion of UsdShadeConnectableAPI to
        UsdShadeShader, so that a ConnectableAPI can be passed into any
        function that accepts a Shader.
        
        that the conversion may produce an invalid Shader object, because not
        all UsdShadeConnectableAPI s are Shaders
        
        
        Parameters
        ----------
        connectable : ConnectableAPI
        
        
        
        ----------------------------------------------------------------------
        
        __init__(prim)
        
        
        Construct a UsdShadeShader on UsdPrim ``prim`` .
        
        
        Equivalent to UsdShadeShader::Get (prim.GetStage(), prim.GetPath())
        for a *valid* ``prim`` , but will not immediately throw an error for
        an invalid ``prim``
        
        
        Parameters
        ----------
        prim : Prim
        
        
        
        ----------------------------------------------------------------------
        
        __init__(schemaObj)
        
        
        Construct a UsdShadeShader on the prim held by ``schemaObj`` .
        
        
        Should be preferred over UsdShadeShader (schemaObj.GetPrim()), as it
        preserves SchemaBase state.
        
        
        Parameters
        ----------
        schemaObj : SchemaBase
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class ShaderDefParserPlugin(Boost.Python.instance):
    """
    
    Parses shader definitions represented using USD scene description
    using the schemas provided by UsdShade.
    
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def GetDiscoveryTypes(*args, **kwargs):
        """
        
        GetDiscoveryTypes() -> NdrTokenVec
        
        
        Returns the types of nodes that this plugin can parse.
        
        
        "Type"here is the discovery type (in the case of files, this will
        probably be the file extension, but in other systems will be data that
        can be determined during discovery). This type should only be used to
        match up a ``NdrNodeDiscoveryResult`` to its parser plugin; this value
        is not exposed in the node's API.
        
        
        
        """
    @staticmethod
    def GetSourceType(*args, **kwargs):
        """
        
        GetSourceType() -> str
        
        
        Returns the source type that this parser operates on.
        
        
        A source type is the most general type for a node. The parser plugin
        is responsible for parsing all discovery results that have the types
        declared under ``GetDiscoveryTypes()`` , and those types are
        collectively identified as one"source type".
        
        
        
        """
    @staticmethod
    def Parse(*args, **kwargs):
        """
        
        Parse(discoveryResult) -> NdrNodeUnique
        
        
        Takes the specified ``NdrNodeDiscoveryResult`` instance, which was a
        result of the discovery process, and generates a new ``NdrNode`` .
        
        
        The node's name, source type, and family must match.
        
        
        Parameters
        ----------
        discoveryResult : NodeDiscoveryResult
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class ShaderDefUtils(Boost.Python.instance):
    """
    
    This class contains a set of utility functions used for populating the
    shader registry with shaders definitions specified using UsdShade
    schemas.
    
    """
    @staticmethod
    def GetNodeDiscoveryResults(*args, **kwargs):
        """
        
        **classmethod** GetNodeDiscoveryResults(shaderDef, sourceUri) -> NdrNodeDiscoveryResultVec
        
        
        Returns the list of NdrNodeDiscoveryResult objects that must be added
        to the shader registry for the given shader ``shaderDef`` , assuming
        it is found in a shader definition file found by an Ndr discovery
        plugin.
        
        
        To enable the shaderDef parser to find and parse this shader,
        ``sourceUri`` should have the resolved path to the usd file containing
        this shader prim.
        
        
        Parameters
        ----------
        shaderDef : Shader
        
        sourceUri : str
        
        
        """
    @staticmethod
    def GetPrimvarNamesMetadataString(*args, **kwargs):
        """
        
        **classmethod** GetPrimvarNamesMetadataString(metadata, shaderDef) -> str
        
        
        Collects all the names of valid primvar inputs of the given
        ``metadata`` and the given ``shaderDef`` and returns the string used
        to represent them in SdrShaderNode metadata.
        
        
        Parameters
        ----------
        metadata : NdrTokenMap
        
        shaderDef : ConnectableAPI
        
        
        """
    @staticmethod
    def GetShaderProperties(*args, **kwargs):
        """
        
        **classmethod** GetShaderProperties(shaderDef) -> NdrPropertyUniquePtrVec
        
        
        Gets all input and output properties of the given ``shaderDef`` and
        translates them into NdrProperties that can be used as the properties
        for an SdrShaderNode.
        
        
        Parameters
        ----------
        shaderDef : ConnectableAPI
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Tokens(Boost.Python.instance):
    allPurpose: typing.ClassVar[str] = ''
    bindMaterialAs: typing.ClassVar[str] = 'bindMaterialAs'
    coordSys: typing.ClassVar[str] = 'coordSys:'
    displacement: typing.ClassVar[str] = 'displacement'
    fallbackStrength: typing.ClassVar[str] = 'fallbackStrength'
    full: typing.ClassVar[str] = 'full'
    id: typing.ClassVar[str] = 'id'
    infoId: typing.ClassVar[str] = 'info:id'
    infoImplementationSource: typing.ClassVar[str] = 'info:implementationSource'
    inputs: typing.ClassVar[str] = 'inputs:'
    interfaceOnly: typing.ClassVar[str] = 'interfaceOnly'
    materialBind: typing.ClassVar[str] = 'materialBind'
    materialBinding: typing.ClassVar[str] = 'material:binding'
    materialBindingCollection: typing.ClassVar[str] = 'material:binding:collection'
    materialVariant: typing.ClassVar[str] = 'materialVariant'
    outputs: typing.ClassVar[str] = 'outputs:'
    outputsDisplacement: typing.ClassVar[str] = 'outputs:displacement'
    outputsSurface: typing.ClassVar[str] = 'outputs:surface'
    outputsVolume: typing.ClassVar[str] = 'outputs:volume'
    preview: typing.ClassVar[str] = 'preview'
    sdrMetadata: typing.ClassVar[str] = 'sdrMetadata'
    sourceAsset: typing.ClassVar[str] = 'sourceAsset'
    sourceCode: typing.ClassVar[str] = 'sourceCode'
    strongerThanDescendants: typing.ClassVar[str] = 'strongerThanDescendants'
    subIdentifier: typing.ClassVar[str] = 'subIdentifier'
    surface: typing.ClassVar[str] = 'surface'
    universalRenderContext: typing.ClassVar[str] = ''
    universalSourceType: typing.ClassVar[str] = ''
    volume: typing.ClassVar[str] = 'volume'
    weakerThanDescendants: typing.ClassVar[str] = 'weakerThanDescendants'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Utils(Boost.Python.instance):
    """
    
    This class contains a set of utility functions used when authoring and
    querying shading networks.
    
    """
    @staticmethod
    def GetBaseNameAndType(*args, **kwargs):
        """
        
        **classmethod** GetBaseNameAndType(fullName) -> tuple[str, AttributeType]
        
        
        Given the full name of a shading attribute, returns it's base name and
        shading attribute type.
        
        
        Parameters
        ----------
        fullName : str
        
        
        """
    @staticmethod
    def GetConnectedSourcePath(*args, **kwargs):
        """
        
        **classmethod** GetConnectedSourcePath(srcInfo) -> Path
        
        
        For a valid UsdShadeConnectionSourceInfo, return the complete path to
        the source property; otherwise the empty path.
        
        
        Parameters
        ----------
        srcInfo : ConnectionSourceInfo
        
        
        """
    @staticmethod
    def GetFullName(*args, **kwargs):
        """
        
        **classmethod** GetFullName(baseName, type) -> str
        
        
        Returns the full shading attribute name given the basename and the
        shading attribute type.
        
        
        ``baseName`` is the name of the input or output on the shading node.
        ``type`` is the UsdShadeAttributeType of the shading attribute.
        
        
        Parameters
        ----------
        baseName : str
        
        type : AttributeType
        
        
        """
    @staticmethod
    def GetPrefixForAttributeType(*args, **kwargs):
        """
        
        **classmethod** GetPrefixForAttributeType(sourceType) -> str
        
        
        Returns the namespace prefix of the USD attribute associated with the
        given shading attribute type.
        
        
        Parameters
        ----------
        sourceType : AttributeType
        
        
        """
    @staticmethod
    def GetType(*args, **kwargs):
        """
        
        **classmethod** GetType(fullName) -> AttributeType
        
        
        Given the full name of a shading attribute, returns its shading
        attribute type.
        
        
        Parameters
        ----------
        fullName : str
        
        
        """
    @staticmethod
    def GetValueProducingAttributes(*args, **kwargs):
        """
        
        **classmethod** GetValueProducingAttributes(input, shaderOutputsOnly) -> list[UsdShadeAttribute]
        
        
        Find what is connected to an Input or Output recursively.
        
        
        GetValueProducingAttributes implements the UsdShade connectivity rules
        described in Connection Resolution Utilities.
        
        When tracing connections within networks that contain containers like
        UsdShadeNodeGraph nodes, the actual output(s) or value(s) at the end
        of an input or output might be multiple connections removed. The
        methods below resolves this across multiple physical connections.
        
        An UsdShadeInput is getting its value from one of these sources:
        
           - If the input is not connected the UsdAttribute for this input is
             returned, but only if it has an authored value. The input attribute
             itself carries the value for this input.
        
           - If the input is connected we follow the connection(s) until we
             reach a valid output of a UsdShadeShader node or if we reach a valid
             UsdShadeInput attribute of a UsdShadeNodeGraph or UsdShadeMaterial
             that has an authored value.
        
        An UsdShadeOutput on a container can get its value from the same type
        of sources as a UsdShadeInput on either a UsdShadeShader or
        UsdShadeNodeGraph. Outputs on non-containers (UsdShadeShaders) cannot
        be connected.
        
        This function returns a vector of UsdAttributes. The vector is empty
        if no valid attribute was found. The type of each attribute can be
        determined with the ``UsdShadeUtils::GetType`` function.
        
        If ``shaderOutputsOnly`` is true, it will only report attributes that
        are outputs of non-containers (UsdShadeShaders). This is a bit faster
        and what is need when determining the connections for Material
        terminals.
        
        This will return the last attribute along the connection chain that
        has an authored value, which might not be the last attribute in the
        chain itself.
        
        When the network contains multi-connections, this function can return
        multiple attributes for a single input or output. The list of
        attributes is build by a depth-first search, following the underlying
        connection paths in order. The list can contain both UsdShadeOutput
        and UsdShadeInput attributes. It is up to the caller to decide how to
        process such a mixture.
        
        
        Parameters
        ----------
        input : Input
        
        shaderOutputsOnly : bool
        
        
        
        ----------------------------------------------------------------------
        
        GetValueProducingAttributes(output, shaderOutputsOnly) -> list[UsdShadeAttribute]
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        output : Output
        
        shaderOutputsOnly : bool
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class _CanApplyResult(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
    @property
    def whyNot(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'usdShade'
