from __future__ import annotations
import pxr.Tf
import typing
__all__ = ['ArcType', 'ArcTypeInherit', 'ArcTypePayload', 'ArcTypeReference', 'ArcTypeRelocate', 'ArcTypeRoot', 'ArcTypeSpecialize', 'ArcTypeVariant', 'Cache', 'Dependency', 'DependencyType', 'DependencyTypeAncestral', 'DependencyTypeAnyIncludingVirtual', 'DependencyTypeAnyNonVirtual', 'DependencyTypeDirect', 'DependencyTypeNonVirtual', 'DependencyTypeNone', 'DependencyTypePartlyDirect', 'DependencyTypePurelyDirect', 'DependencyTypeRoot', 'DependencyTypeVirtual', 'DynamicFileFormatDependencyData', 'ErrorArcCycle', 'ErrorArcPermissionDenied', 'ErrorBase', 'ErrorCapacityExceeded', 'ErrorInconsistentAttributeType', 'ErrorInconsistentAttributeVariability', 'ErrorInconsistentPropertyType', 'ErrorInvalidAssetPath', 'ErrorInvalidAssetPathBase', 'ErrorInvalidExternalTargetPath', 'ErrorInvalidInstanceTargetPath', 'ErrorInvalidPrimPath', 'ErrorInvalidReferenceOffset', 'ErrorInvalidSublayerOffset', 'ErrorInvalidSublayerOwnership', 'ErrorInvalidSublayerPath', 'ErrorInvalidTargetPath', 'ErrorMutedAssetPath', 'ErrorOpinionAtRelocationSource', 'ErrorPrimPermissionDenied', 'ErrorPropertyPermissionDenied', 'ErrorSublayerCycle', 'ErrorTargetPathBase', 'ErrorTargetPermissionDenied', 'ErrorType', 'ErrorType_ArcCapacityExceeded', 'ErrorType_ArcCycle', 'ErrorType_ArcNamespaceDepthCapacityExceeded', 'ErrorType_ArcPermissionDenied', 'ErrorType_InconsistentAttributeType', 'ErrorType_InconsistentAttributeVariability', 'ErrorType_InconsistentPropertyType', 'ErrorType_IndexCapacityExceeded', 'ErrorType_InternalAssetPath', 'ErrorType_InvalidAssetPath', 'ErrorType_InvalidExternalTargetPath', 'ErrorType_InvalidInstanceTargetPath', 'ErrorType_InvalidPrimPath', 'ErrorType_InvalidReferenceOffset', 'ErrorType_InvalidSublayerOffset', 'ErrorType_InvalidSublayerOwnership', 'ErrorType_InvalidSublayerPath', 'ErrorType_InvalidTargetPath', 'ErrorType_InvalidVariantSelection', 'ErrorType_OpinionAtRelocationSource', 'ErrorType_PrimPermissionDenied', 'ErrorType_PropertyPermissionDenied', 'ErrorType_SublayerCycle', 'ErrorType_TargetPermissionDenied', 'ErrorType_UnresolvedPrimPath', 'ErrorUnresolvedPrimPath', 'InstanceKey', 'LayerStack', 'LayerStackIdentifier', 'LayerStackSite', 'MapExpression', 'MapFunction', 'NodeRef', 'PrimIndex', 'PropertyIndex', 'Site']
class ArcType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Pcp.ArcTypeRoot, Pcp.ArcTypeInherit, Pcp.ArcTypeRelocate, Pcp.ArcTypeVariant, Pcp.ArcTypeReference, Pcp.ArcTypePayload, Pcp.ArcTypeSpecialize)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
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
class Cache(Boost.Python.instance):
    """
    
    PcpCache is the context required to make requests of the Pcp
    composition algorithm and cache the results.
    
    Because the algorithms are recursive  making a request typically makes
    other internal requests to solve subproblems  caching subproblem
    results is required for reasonable performance, and so this cache is
    the only entrypoint to the algorithms.
    
    There is a set of parameters that affect the composition results:
    
       - variant fallbacks: per named variant set, an ordered list of
         fallback values to use when composing a prim that defines a variant
         set but does not specify a selection
    
       - payload inclusion set: an SdfPath set used to identify which
         prims should have their payloads included during composition; this is
         the basis for explicit control over the"working set"of composition
    
       - file format target: the file format target that Pcp will request
         when opening scene description layers
    
       - "USD mode"configures the Pcp composition algorithm to provide
         only a custom, lighter subset of the full feature set, as needed by
         the Universal Scene Description system
         There are a number of different computations that can be requested.
         These include computing a layer stack from a PcpLayerStackIdentifier,
         computing a prim index or prim stack, and computing a property index.
    
    """
    __instance_size__: typing.ClassVar[int] = 328
    @staticmethod
    def ComputeAttributeConnectionPaths(*args, **kwargs):
        """
        
        ComputeAttributeConnectionPaths(attributePath, paths, localOnly, stopProperty, includeStopProperty, deletedPaths, allErrors) -> None
        
        
        Compute the attribute connection paths for the attribute at
        ``attributePath`` into ``paths`` .
        
        
        If ``localOnly`` is ``true`` then this will compose attribute
        connections from local nodes only. If ``stopProperty`` is not ``None``
        then this will stop composing attribute connections at
        ``stopProperty`` , including ``stopProperty`` iff
        ``includeStopProperty`` is ``true`` . If not ``None`` ,
        ``deletedPaths`` will be populated with connection paths whose
        deletion contributed to the computed result. ``allErrors`` will
        contain any errors encountered while performing this operation.
        
        
        Parameters
        ----------
        attributePath : Path
        
        paths : list[Path]
        
        localOnly : bool
        
        stopProperty : Spec
        
        includeStopProperty : bool
        
        deletedPaths : list[Path]
        
        allErrors : list[PcpError]
        
        
        """
    @staticmethod
    def ComputeLayerStack(*args, **kwargs):
        """
        
        ComputeLayerStack(identifier, allErrors) -> LayerStack
        
        
        Returns the layer stack for ``identifier`` if it exists, otherwise
        creates a new layer stack for ``identifier`` .
        
        
        This returns ``None`` if ``identifier`` is invalid (i.e. its root
        layer is ``None`` ). ``allErrors`` will contain any errors encountered
        while creating a new layer stack. It'll be unchanged if the layer
        stack already existed.
        
        
        Parameters
        ----------
        identifier : LayerStackIdentifier
        
        allErrors : list[PcpError]
        
        
        """
    @staticmethod
    def ComputePrimIndex(*args, **kwargs):
        """
        
        ComputePrimIndex(primPath, allErrors) -> PrimIndex
        
        
        Compute and return a reference to the cached result for the prim index
        for the given path.
        
        
        ``allErrors`` will contain any errors encountered while performing
        this operation.
        
        
        Parameters
        ----------
        primPath : Path
        
        allErrors : list[PcpError]
        
        
        """
    @staticmethod
    def ComputePropertyIndex(*args, **kwargs):
        """
        
        ComputePropertyIndex(propPath, allErrors) -> PropertyIndex
        
        
        Compute and return a reference to the cached result for the property
        index for the given path.
        
        
        ``allErrors`` will contain any errors encountered while performing
        this operation.
        
        
        Parameters
        ----------
        propPath : Path
        
        allErrors : list[PcpError]
        
        
        """
    @staticmethod
    def ComputeRelationshipTargetPaths(*args, **kwargs):
        """
        
        ComputeRelationshipTargetPaths(relationshipPath, paths, localOnly, stopProperty, includeStopProperty, deletedPaths, allErrors) -> None
        
        
        Compute the relationship target paths for the relationship at
        ``relationshipPath`` into ``paths`` .
        
        
        If ``localOnly`` is ``true`` then this will compose relationship
        targets from local nodes only. If ``stopProperty`` is not ``None``
        then this will stop composing relationship targets at ``stopProperty``
        , including ``stopProperty`` iff ``includeStopProperty`` is ``true`` .
        If not ``None`` , ``deletedPaths`` will be populated with target paths
        whose deletion contributed to the computed result. ``allErrors`` will
        contain any errors encountered while performing this operation.
        
        
        Parameters
        ----------
        relationshipPath : Path
        
        paths : list[Path]
        
        localOnly : bool
        
        stopProperty : Spec
        
        includeStopProperty : bool
        
        deletedPaths : list[Path]
        
        allErrors : list[PcpError]
        
        
        """
    @staticmethod
    def FindAllLayerStacksUsingLayer(*args, **kwargs):
        """
        
        FindAllLayerStacksUsingLayer(layer) -> list[LayerStack]
        
        
        Returns every computed & cached layer stack that includes ``layer`` .
        
        
        Parameters
        ----------
        layer : Layer
        
        
        """
    @staticmethod
    def FindPrimIndex(*args, **kwargs):
        """
        
        FindPrimIndex(primPath) -> PrimIndex
        
        
        Returns a pointer to the cached computed prim index for the given
        path, or None if it has not been computed.
        
        
        Parameters
        ----------
        primPath : Path
        
        
        """
    @staticmethod
    def FindPropertyIndex(*args, **kwargs):
        """
        
        FindPropertyIndex(propPath) -> PropertyIndex
        
        
        Returns a pointer to the cached computed property index for the given
        path, or None if it has not been computed.
        
        
        Parameters
        ----------
        propPath : Path
        
        
        """
    @staticmethod
    def FindSiteDependencies(*args, **kwargs):
        """
        
        FindSiteDependencies(siteLayerStack, sitePath, depMask, recurseOnSite, recurseOnIndex, filterForExistingCachesOnly) -> list[Dependency]
        
        
        Returns dependencies on the given site of scene description, as
        discovered by the cached index computations.
        
        
        depMask
        
        specifies what classes of dependency to include; see
        PcpDependencyFlags for details recurseOnSite
        
        includes incoming dependencies on children of sitePath recurseOnIndex
        
        extends the result to include all PcpCache child indexes below
        discovered results filterForExistingCachesOnly
        
        filters the results to only paths representing computed prim and
        property index caches; otherwise a recursively-expanded result can
        include un-computed paths that are expected to depend on the site
        
        
        Parameters
        ----------
        siteLayerStack : LayerStack
        
        sitePath : Path
        
        depMask : PcpDependencyFlags
        
        recurseOnSite : bool
        
        recurseOnIndex : bool
        
        filterForExistingCachesOnly : bool
        
        
        
        ----------------------------------------------------------------------
        
        FindSiteDependencies(siteLayer, sitePath, depMask, recurseOnSite, recurseOnIndex, filterForExistingCachesOnly) -> list[Dependency]
        
        
        Returns dependencies on the given site of scene description, as
        discovered by the cached index computations.
        
        
        This method overload takes a site layer rather than a layer stack. It
        will check every layer stack using that layer, and apply any relevant
        sublayer offsets to the map functions in the returned
        PcpDependencyVector.
        
        See the other method for parameter details.
        
        
        Parameters
        ----------
        siteLayer : Layer
        
        sitePath : Path
        
        depMask : PcpDependencyFlags
        
        recurseOnSite : bool
        
        recurseOnIndex : bool
        
        filterForExistingCachesOnly : bool
        
        
        """
    @staticmethod
    def GetDynamicFileFormatArgumentDependencyData(*args, **kwargs):
        """
        
        GetDynamicFileFormatArgumentDependencyData(primIndexPath) -> DynamicFileFormatDependencyData
        
        
        Returns the dynamic file format dependency data object for the prim
        index with the given ``primIndexPath`` .
        
        
        This will return an empty dependency data if either there is no cache
        prim index for the path or if the prim index has no dynamic file
        formats that it depends on.
        
        
        Parameters
        ----------
        primIndexPath : Path
        
        
        """
    @staticmethod
    def GetLayerStackIdentifier(*args, **kwargs):
        """
        
        GetLayerStackIdentifier() -> LayerStackIdentifier
        
        
        Get the identifier of the layerStack used for composition.
        
        
        
        """
    @staticmethod
    def GetMutedLayers(*args, **kwargs):
        """
        
        GetMutedLayers() -> list[str]
        
        
        Returns the list of canonical identifiers for muted layers in this
        cache.
        
        
        See documentation on RequestLayerMuting for more details.
        
        
        
        """
    @staticmethod
    def GetUsedLayers(*args, **kwargs):
        """
        
        GetUsedLayers() -> SdfLayerHandleSet
        
        
        Returns set of all layers used by this cache.
        
        
        
        """
    @staticmethod
    def GetUsedLayersRevision(*args, **kwargs):
        """
        
        GetUsedLayersRevision() -> int
        
        
        Return a number that can be used to determine whether or not the set
        of layers used by this cache may have changed or not.
        
        
        For example, if one calls GetUsedLayers() and saves the
        GetUsedLayersRevision() , and then later calls GetUsedLayersRevision()
        again, if the number is unchanged, then GetUsedLayers() is guaranteed
        to be unchanged as well.
        
        
        
        """
    @staticmethod
    def GetVariantFallbacks(*args, **kwargs):
        """
        
        GetVariantFallbacks() -> PcpVariantFallbackMap
        
        
        Get the list of fallbacks to attempt to use when evaluating variant
        sets that lack an authored selection.
        
        
        
        """
    @staticmethod
    def HasAnyDynamicFileFormatArgumentDependencies(*args, **kwargs):
        """
        
        HasAnyDynamicFileFormatArgumentDependencies() -> bool
        
        
        Returns true if any prim index in this cache has a dependency on a
        dynamic file format argument field.
        
        
        
        
        
        """
    @staticmethod
    def HasRootLayerStack(*args, **kwargs):
        """
        
        HasRootLayerStack(layerStack) -> bool
        
        
        Return true if this cache's root layer stack is ``layerStack`` , false
        otherwise.
        
        
        This is functionally equivalent to comparing against the result of
        GetLayerStack() , but does not require constructing a TfWeakPtr or any
        refcount operations.
        
        
        Parameters
        ----------
        layerStack : LayerStack
        
        
        
        ----------------------------------------------------------------------
        
        HasRootLayerStack(layerStack) -> bool
        
        
        This is an overloaded member function, provided for convenience. It
        differs from the above function only in what argument(s) it accepts.
        
        
        Parameters
        ----------
        layerStack : LayerStack
        
        
        """
    @staticmethod
    def IsInvalidAssetPath(*args, **kwargs):
        """
        
        IsInvalidAssetPath(resolvedAssetPath) -> bool
        
        
        Returns true if ``resolvedAssetPath`` was used by a prim (e.g.
        
        
        in a reference) but did not resolve to a valid asset. This is
        functionally equivalent to examining the values in the map returned by
        GetInvalidAssetPaths, but more efficient.
        
        
        Parameters
        ----------
        resolvedAssetPath : str
        
        
        """
    @staticmethod
    def IsInvalidSublayerIdentifier(*args, **kwargs):
        """
        
        IsInvalidSublayerIdentifier(identifier) -> bool
        
        
        Returns true if ``identifier`` was used as a sublayer path in a layer
        stack but did not identify a valid layer.
        
        
        This is functionally equivalent to examining the values in the vector
        returned by GetInvalidSublayerIdentifiers, but more efficient.
        
        
        Parameters
        ----------
        identifier : str
        
        
        """
    @staticmethod
    def IsLayerMuted(*args, **kwargs):
        """
        
        IsLayerMuted(layerIdentifier) -> bool
        
        
        Returns true if the layer specified by ``layerIdentifier`` is muted in
        this cache, false otherwise.
        
        
        If ``layerIdentifier`` is relative, it is assumed to be relative to
        this cache's root layer. See documentation on RequestLayerMuting for
        more details.
        
        
        Parameters
        ----------
        layerIdentifier : str
        
        
        
        ----------------------------------------------------------------------
        
        IsLayerMuted(anchorLayer, layerIdentifier, canonicalMutedLayerIdentifier) -> bool
        
        
        Returns true if the layer specified by ``layerIdentifier`` is muted in
        this cache, false otherwise.
        
        
        If ``layerIdentifier`` is relative, it is assumed to be relative to
        ``anchorLayer`` . If ``canonicalMutedLayerIdentifier`` is supplied, it
        will be populated with the canonical identifier of the muted layer if
        this function returns true. See documentation on RequestLayerMuting
        for more details.
        
        
        Parameters
        ----------
        anchorLayer : Layer
        
        layerIdentifier : str
        
        canonicalMutedLayerIdentifier : str
        
        
        """
    @staticmethod
    def IsPayloadIncluded(*args, **kwargs):
        """
        
        IsPayloadIncluded(path) -> bool
        
        
        Return true if the payload is included for the given path.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def IsPossibleDynamicFileFormatArgumentField(*args, **kwargs):
        """
        
        IsPossibleDynamicFileFormatArgumentField(field) -> bool
        
        
        Returns true if the given ``field`` is the name of a field that was
        composed while generating dynamic file format arguments for any prim
        index in this cache.
        
        
        
        
        Parameters
        ----------
        field : str
        
        
        """
    @staticmethod
    def PrintStatistics(*args, **kwargs):
        """
        
        PrintStatistics() -> None
        
        
        Prints various statistics about the data stored in this cache.
        
        
        
        """
    @staticmethod
    def Reload(*args, **kwargs):
        """
        
        Reload(changes) -> None
        
        
        Reload the layers of the layer stack, except session layers and
        sublayers of session layers.
        
        
        This will also try to load sublayers in this cache's layer stack that
        could not be loaded previously. It will also try to load any
        referenced or payloaded layer that could not be loaded previously.
        Clients should subsequently ``Apply()`` ``changes`` to use any now-
        valid layers.
        
        
        Parameters
        ----------
        changes : PcpChanges
        
        
        """
    @staticmethod
    def RequestLayerMuting(*args, **kwargs):
        """
        
        RequestLayerMuting(layersToMute, layersToUnmute, changes, newLayersMuted, newLayersUnmuted) -> None
        
        
        Request layers to be muted or unmuted in this cache.
        
        
        Muted layers are ignored during composition and do not appear in any
        layer stacks. The root layer of this stage may not be muted;
        attempting to do so will generate a coding error. If the root layer of
        a reference or payload layer stack is muted, the behavior is as if the
        muted layer did not exist, which means a composition error will be
        generated.
        
        A canonical identifier for each layer in ``layersToMute`` will be
        computed using ArResolver::CreateIdentifier using the cache's root
        layer as the anchoring asset. Any layer encountered during composition
        with the same identifier will be considered muted and ignored.
        
        Note that muting a layer will cause this cache to release all
        references to that layer. If no other client is holding on to
        references to that layer, it will be unloaded. In this case, if there
        are unsaved edits to the muted layer, those edits are lost.  Since
        anonymous layers are not serialized, muting an anonymous layer will
        cause that layer and its contents to be lost in this case.
        
        If ``changes`` is not ``nullptr`` , it is adjusted to reflect the
        changes necessary to see the change in muted layers. Otherwise, those
        changes are applied immediately.
        
        ``newLayersMuted`` and ``newLayersUnmuted`` contains the pruned vector
        of layers which are muted or unmuted by this call to
        RequestLayerMuting.
        
        
        Parameters
        ----------
        layersToMute : list[str]
        
        layersToUnmute : list[str]
        
        changes : PcpChanges
        
        newLayersMuted : list[str]
        
        newLayersUnmuted : list[str]
        
        
        """
    @staticmethod
    def RequestPayloads(*args, **kwargs):
        """
        
        RequestPayloads(pathsToInclude, pathsToExclude, changes) -> None
        
        
        Request payloads to be included or excluded from composition.
        
        
        pathsToInclude
        
        is a set of paths to add to the set for payload inclusion.
        pathsToExclude
        
        is a set of paths to remove from the set for payload inclusion.
        changes
        
        if not ``None`` , is adjusted to reflect the changes necessary to see
        the change in payloads; otherwise those changes are applied
        immediately.
        
        If a path is listed in both pathsToInclude and pathsToExclude, it will
        be treated as an inclusion only.
        
        
        Parameters
        ----------
        pathsToInclude : SdfPathSet
        
        pathsToExclude : SdfPathSet
        
        changes : PcpChanges
        
        
        """
    @staticmethod
    def SetVariantFallbacks(*args, **kwargs):
        """
        
        SetVariantFallbacks(map, changes) -> None
        
        
        Set the list of fallbacks to attempt to use when evaluating variant
        sets that lack an authored selection.
        
        
        If ``changes`` is not ``None`` then it's adjusted to reflect the
        changes necessary to see the change in standin preferences, otherwise
        those changes are applied immediately.
        
        
        Parameters
        ----------
        map : PcpVariantFallbackMap
        
        changes : PcpChanges
        
        
        """
    @staticmethod
    def UsesLayerStack(*args, **kwargs):
        """
        
        UsesLayerStack(layerStack) -> bool
        
        
        Return true if ``layerStack`` is used by this cache in its
        composition, false otherwise.
        
        
        Parameters
        ----------
        layerStack : LayerStack
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__(arg1)
        
        
        Parameters
        ----------
        arg1 : Cache
        
        
        
        ----------------------------------------------------------------------
        
        __init__(layerStackIdentifier, fileFormatTarget, usd)
        
        
        Construct a PcpCache to compose results for the layer stack identified
        by *layerStackIdentifier*.
        
        
        If ``fileFormatTarget`` is given, Pcp will specify
        ``fileFormatTarget`` as the file format target when searching for or
        opening a layer.
        
        If ``usd`` is true, computation of prim indices and composition of
        prim child names are performed without relocates, inherits,
        permissions, symmetry, or payloads, and without populating the prim
        stack and gathering its dependencies.
        
        
        Parameters
        ----------
        layerStackIdentifier : LayerStackIdentifier
        
        fileFormatTarget : str
        
        usd : bool
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def fileFormatTarget(*args, **kwargs):
        """
        type : str
        
        
        Returns the file format target this cache is configured for.
        """
    @property
    def layerStack(*args, **kwargs):
        """
        type : LayerStack
        
        
        Get the layer stack for GetLayerStackIdentifier() .
        
        
        Note that this will neither compute the layer stack nor report errors.
        So if the layer stack has not been computed yet this will return
        ``None`` . Use ComputeLayerStack() if you need to compute the layer
        stack if it hasn't been computed already and/or get errors caused by
        computing the layer stack.
        """
class Dependency(Boost.Python.instance):
    """
    
    Description of a dependency.
    
    """
    @staticmethod
    def __eq__(*args, **kwargs):
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
    def indexPath(*args, **kwargs):
        ...
    @indexPath.setter
    def indexPath(*args, **kwargs):
        ...
    @property
    def mapFunc(*args, **kwargs):
        ...
    @mapFunc.setter
    def mapFunc(*args, **kwargs):
        ...
    @property
    def sitePath(*args, **kwargs):
        ...
    @sitePath.setter
    def sitePath(*args, **kwargs):
        ...
class DependencyType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Pcp.DependencyTypeNone, Pcp.DependencyTypeRoot, Pcp.DependencyTypePurelyDirect, Pcp.DependencyTypePartlyDirect, Pcp.DependencyTypeDirect, Pcp.DependencyTypeAncestral, Pcp.DependencyTypeVirtual, Pcp.DependencyTypeNonVirtual, Pcp.DependencyTypeAnyNonVirtual, Pcp.DependencyTypeAnyIncludingVirtual)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
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
class DynamicFileFormatDependencyData(Boost.Python.instance):
    """
    
    Contains the necessary information for storing a prim index's
    dependency on dynamic file format arguments and determining if a field
    change affects the prim index. This data structure does not store the
    prim index or its path itself and is expected to be the data in some
    other data structure that maps prim indexes to its dependencies.
    
    """
    @staticmethod
    def CanFieldChangeAffectFileFormatArguments(*args, **kwargs):
        """
        
        CanFieldChangeAffectFileFormatArguments(fieldName, oldValue, newValue) -> bool
        
        
        Given a ``field`` name and the changed field values in
        ``oldAndNewValues`` this return whether this change can affect any of
        the file format arguments generated by any of the contexts stored in
        this dependency.
        
        
        Parameters
        ----------
        fieldName : str
        
        oldValue : VtValue
        
        newValue : VtValue
        
        
        """
    @staticmethod
    def GetRelevantFieldNames(*args, **kwargs):
        """
        
        GetRelevantFieldNames() -> str.Set
        
        
        Returns a list of field names that were composed for any of the
        dependency contexts that were added to this dependency.
        
        
        
        """
    @staticmethod
    def IsEmpty(*args, **kwargs):
        """
        
        IsEmpty() -> bool
        
        
        Returns whether this dependency data is empty.
        
        
        
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
class ErrorArcCycle(ErrorBase):
    """
    
    Arcs between PcpNodes that form a cycle.
    
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
class ErrorArcPermissionDenied(ErrorBase):
    """
    
    Arcs that were not made between PcpNodes because of permission
    restrictions.
    
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
class ErrorBase(Boost.Python.instance):
    """
    
    Base class for all error types.
    
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def errorType(*args, **kwargs):
        ...
class ErrorCapacityExceeded(ErrorBase):
    """
    
    Exceeded the capacity for composition arcs at a single site.
    
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
class ErrorInconsistentAttributeType(ErrorBase):
    """
    
    Attributes that have specs with conflicting definitions.
    
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
class ErrorInconsistentAttributeVariability(ErrorBase):
    """
    
    Attributes that have specs with conflicting variability.
    
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
class ErrorInconsistentPropertyType(ErrorBase):
    """
    
    Properties that have specs with conflicting definitions.
    
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
class ErrorInvalidAssetPath(ErrorInvalidAssetPathBase):
    """
    
    Invalid asset paths used by references or payloads.
    
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
class ErrorInvalidAssetPathBase(ErrorBase):
    """
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
class ErrorInvalidExternalTargetPath(ErrorTargetPathBase):
    """
    
    Invalid target or connection path in some scope that points to an
    object outside of that scope.
    
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
class ErrorInvalidInstanceTargetPath(ErrorTargetPathBase):
    """
    
    Invalid target or connection path authored in an inherited class that
    points to an instance of that class.
    
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
class ErrorInvalidPrimPath(ErrorBase):
    """
    
    Invalid prim paths used by references or payloads.
    
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
class ErrorInvalidReferenceOffset(ErrorBase):
    """
    
    References or payloads that use invalid layer offsets.
    
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
class ErrorInvalidSublayerOffset(ErrorBase):
    """
    
    Sublayers that use invalid layer offsets.
    
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
class ErrorInvalidSublayerOwnership(ErrorBase):
    """
    
    Sibling layers that have the same owner.
    
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
class ErrorInvalidSublayerPath(ErrorBase):
    """
    
    Asset paths that could not be both resolved and loaded.
    
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
class ErrorInvalidTargetPath(ErrorTargetPathBase):
    """
    
    Invalid target or connection path.
    
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
class ErrorMutedAssetPath(ErrorInvalidAssetPathBase):
    """
    
    Muted asset paths used by references or payloads.
    
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
class ErrorOpinionAtRelocationSource(ErrorBase):
    """
    
    Opinions were found at a relocation source path.
    
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
class ErrorPrimPermissionDenied(ErrorBase):
    """
    
    Layers with illegal opinions about private prims.
    
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
class ErrorPropertyPermissionDenied(ErrorBase):
    """
    
    Layers with illegal opinions about private properties.
    
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
class ErrorSublayerCycle(ErrorBase):
    """
    
    Layers that recursively sublayer themselves.
    
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
class ErrorTargetPathBase(ErrorBase):
    """
    
    Base class for composition errors related to target or connection
    paths.
    
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
class ErrorTargetPermissionDenied(ErrorTargetPathBase):
    """
    
    Paths with illegal opinions about private targets.
    
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
class ErrorType(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: typing.ClassVar[str] = ''
    allValues: typing.ClassVar[tuple]  # value = (Pcp.ErrorType_ArcCycle, Pcp.ErrorType_ArcPermissionDenied, Pcp.ErrorType_IndexCapacityExceeded, Pcp.ErrorType_ArcCapacityExceeded, Pcp.ErrorType_ArcNamespaceDepthCapacityExceeded, Pcp.ErrorType_InconsistentPropertyType, Pcp.ErrorType_InconsistentAttributeType, Pcp.ErrorType_InconsistentAttributeVariability, Pcp.ErrorType_InternalAssetPath, Pcp.ErrorType_InvalidPrimPath, Pcp.ErrorType_InvalidAssetPath, Pcp.ErrorType_InvalidInstanceTargetPath, Pcp.ErrorType_InvalidExternalTargetPath, Pcp.ErrorType_InvalidTargetPath, Pcp.ErrorType_InvalidReferenceOffset, Pcp.ErrorType_InvalidSublayerOffset, Pcp.ErrorType_InvalidSublayerOwnership, Pcp.ErrorType_InvalidSublayerPath, Pcp.ErrorType_InvalidVariantSelection, Pcp.ErrorType_OpinionAtRelocationSource, Pcp.ErrorType_PrimPermissionDenied, Pcp.ErrorType_PropertyPermissionDenied, Pcp.ErrorType_SublayerCycle, Pcp.ErrorType_TargetPermissionDenied, Pcp.ErrorType_UnresolvedPrimPath)
    @staticmethod
    def GetValueFromName(*args, **kwargs):
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
class ErrorUnresolvedPrimPath(ErrorBase):
    """
    
    Asset paths that could not be both resolved and loaded.
    
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
class InstanceKey(Boost.Python.instance):
    """
    
    A PcpInstanceKey identifies instanceable prim indexes that share the
    same set of opinions. Instanceable prim indexes with equal instance
    keys are guaranteed to have the same opinions for name children and
    properties beneath those name children. They are NOT guaranteed to
    have the same opinions for direct properties of the prim indexes
    themselves.
    
    """
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __hash_(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(primIndex)
        
        
        Create an instance key for the given prim index.
        
        
        Parameters
        ----------
        primIndex : PrimIndex
        
        
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
class LayerStack(Boost.Python.instance):
    """
    
    Represents a stack of layers that contribute opinions to composition.
    
    Each PcpLayerStack is identified by a PcpLayerStackIdentifier. This
    identifier contains all of the parameters needed to construct a layer
    stack, such as the root layer, session layer, and path resolver
    context.
    
    PcpLayerStacks are constructed and managed by a
    Pcp_LayerStackRegistry.
    
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
    def identifier(*args, **kwargs):
        """
        type : LayerStackIdentifier
        
        
        Returns the identifier for this layer stack.
        """
    @property
    def incrementalRelocatesSourceToTarget(*args, **kwargs):
        """
        type : SdfRelocatesMap
        
        
        Returns incremental relocation source-to-target mapping for this layer
        stack.
        
        
        This map contains the individual relocation entries found across all
        layers in this layer stack; it does not combine ancestral entries with
        descendant entries. For instance, if this layer stack contains
        relocations { /A: /B} and { /A/C: /A/D}, this map will contain { /A:
        /B} and { /A/C: /A/D}.
        """
    @property
    def incrementalRelocatesTargetToSource(*args, **kwargs):
        """
        type : SdfRelocatesMap
        
        
        Returns incremental relocation target-to-source mapping for this layer
        stack.
        
        
        See GetIncrementalRelocatesTargetToSource for more details.
        """
    @property
    def layerOffsets(*args, **kwargs):
        ...
    @property
    def layerTree(*args, **kwargs):
        """
        type : LayerTree
        
        
        Returns the layer tree representing the structure of this layer stack.
        """
    @property
    def layers(*args, **kwargs):
        """
        type : list[Layer]
        
        
        Returns the layers in this layer stack in strong-to-weak order.
        
        
        Note that this is only the *local* layer stack  it does not include
        any layers brought in by references inside prims.
        """
    @property
    def localErrors(*args, **kwargs):
        """
        type : list[PcpError]
        
        
        Return the list of errors local to this layer stack.
        """
    @property
    def mutedLayers(*args, **kwargs):
        """
        type : set[str]
        
        
        Returns the set of layers that were muted in this layer stack.
        """
    @property
    def pathsToPrimsWithRelocates(*args, **kwargs):
        """
        type : list[Path]
        
        
        Returns a list of paths to all prims across all layers in this layer
        stack that contained relocates.
        """
    @property
    def relocatesSourceToTarget(*args, **kwargs):
        """
        type : SdfRelocatesMap
        
        
        Returns relocation source-to-target mapping for this layer stack.
        
        
        This map combines the individual relocation entries found across all
        layers in this layer stack; multiple entries that affect a single prim
        will be combined into a single entry. For instance, if this layer
        stack contains relocations { /A: /B} and { /A/C: /A/D}, this map will
        contain { /A: /B} and { /B/C: /B/D}. This allows consumers to go from
        unrelocated namespace to relocated namespace in a single step.
        """
    @property
    def relocatesTargetToSource(*args, **kwargs):
        """
        type : SdfRelocatesMap
        
        
        Returns relocation target-to-source mapping for this layer stack.
        
        
        See GetRelocatesSourceToTarget for more details.
        """
class LayerStackIdentifier(Boost.Python.instance):
    """
    
    Arguments used to identify a layer stack.
    
    Objects of this type are immutable.
    
    """
    __instance_size__: typing.ClassVar[int] = 80
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __ge__(*args, **kwargs):
        ...
    @staticmethod
    def __gt__(*args, **kwargs):
        ...
    @staticmethod
    def __hash__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct with all empty pointers.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(rootLayer_, sessionLayer_, pathResolverContext_)
        
        
        Construct with given pointers.
        
        
        If all arguments are ``TfNullPtr`` then the result is identical to the
        default constructed object.
        
        
        Parameters
        ----------
        rootLayer_ : Layer
        
        sessionLayer_ : Layer
        
        pathResolverContext_ : ResolverContext
        
        
        """
    @staticmethod
    def __le__(*args, **kwargs):
        ...
    @staticmethod
    def __lt__(*args, **kwargs):
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
    def pathResolverContext(*args, **kwargs):
        ...
    @property
    def rootLayer(*args, **kwargs):
        ...
    @property
    def sessionLayer(*args, **kwargs):
        ...
class LayerStackSite(Boost.Python.instance):
    """
    
    A site specifies a path in a layer stack of scene description.
    
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def layerStack(*args, **kwargs):
        ...
    @layerStack.setter
    def layerStack(*args, **kwargs):
        ...
    @property
    def path(*args, **kwargs):
        ...
    @path.setter
    def path(*args, **kwargs):
        ...
class MapExpression(Boost.Python.instance):
    """
    
    An expression that yields a PcpMapFunction value.
    
    Expressions comprise constant values, variables, and operators applied
    to sub-expressions. Expressions cache their computed values
    internally. Assigning a new value to a variable automatically
    invalidates the cached values of dependent expressions. Common
    (sub-)expressions are automatically detected and shared.
    
    PcpMapExpression exists solely to support efficient incremental
    handling of relocates edits. It represents a tree of the namespace
    mapping operations and their inputs, so we can narrowly redo the
    computation when one of the inputs changes.
    
    """
    __instance_size__: typing.ClassVar[int] = 24
    @staticmethod
    def AddRootIdentity(*args, **kwargs):
        """
        
        AddRootIdentity() -> MapExpression
        
        
        Return a new expression representing this expression with an added (if
        necessary) mapping from</>to</>.
        
        
        
        """
    @staticmethod
    def Compose(*args, **kwargs):
        """
        
        Compose(f) -> MapExpression
        
        
        Create a new PcpMapExpression representing the application of f's
        value, followed by the application of this expression's value.
        
        
        Parameters
        ----------
        f : MapExpression
        
        
        """
    @staticmethod
    def Constant(*args, **kwargs):
        """
        
        **classmethod** Constant(constValue) -> MapExpression
        
        
        Create a new constant.
        
        
        Parameters
        ----------
        constValue : Value
        
        
        """
    @staticmethod
    def Evaluate(*args, **kwargs):
        """
        
        Evaluate() -> Value
        
        
        Evaluate this expression, yielding a PcpMapFunction value.
        
        
        The computed result is cached. The return value is a reference to the
        internal cached value. The cache is automatically invalidated as
        needed.
        
        
        
        """
    @staticmethod
    def Identity(*args, **kwargs):
        """
        
        **classmethod** Identity() -> MapExpression
        
        
        Return an expression representing PcpMapFunction::Identity() .
        
        
        
        """
    @staticmethod
    def Inverse(*args, **kwargs):
        """
        
        Inverse() -> MapExpression
        
        
        Create a new PcpMapExpression representing the inverse of f.
        
        
        
        """
    @staticmethod
    def MapSourceToTarget(*args, **kwargs):
        """
        
        MapSourceToTarget(path) -> Path
        
        
        Map a path in the source namespace to the target.
        
        
        If the path is not in the domain, returns an empty path.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def MapTargetToSource(*args, **kwargs):
        """
        
        MapTargetToSource(path) -> Path
        
        
        Map a path in the target namespace to the source.
        
        
        If the path is not in the co-domain, returns an empty path.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Default-construct a None expression.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(node)
        
        
        Parameters
        ----------
        node : _Node
        
        
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def isIdentity(*args, **kwargs):
        """
        type : bool
        
        
        Return true if the evaluated map function is the identity function.
        
        
        For identity, MapSourceToTarget() always returns the path unchanged.
        """
    @property
    def isNull(*args, **kwargs):
        """
        type : bool
        
        
        Return true if this is a null expression.
        """
    @property
    def timeOffset(*args, **kwargs):
        """
        type : LayerOffset
        
        
        The time offset of the mapping.
        """
class MapFunction(Boost.Python.instance):
    """
    
    A function that maps values from one namespace (and time domain) to
    another. It represents the transformation that an arc such as a
    reference arc applies as it incorporates values across the arc.
    
    Take the example of a reference arc, where a source path</Model>is
    referenced as a target path,</Model_1>. The source path</Model>is the
    source of the opinions; the target path</Model_1>is where they are
    incorporated in the scene. Values in the model that refer to paths
    relative to</Model>must be transformed to be relative
    to</Model_1>instead. The PcpMapFunction for the arc provides this
    service.
    
    Map functions have a specific *domain*, or set of values they can
    operate on. Any values outside the domain cannot be mapped. The domain
    precisely tracks what areas of namespace can be referred to across
    various forms of arcs.
    
    Map functions can be chained to represent a series of map operations
    applied in sequence. The map function represent the cumulative effect
    as efficiently as possible. For example, in the case of a chained
    reference from</Model>to</Model>to</Model>to</Model_1>, this is
    effectively the same as a mapping directly from</Model>to</Model_1>.
    Representing the cumulative effect of arcs in this way is important
    for handling larger scenes efficiently.
    
    Map functions can be *inverted*. Formally, map functions are
    bijections (one-to-one and onto), which ensures that they can be
    inverted. Put differently, no information is lost by applying a map
    function to set of values within its domain; they retain their
    distinct identities and can always be mapped back.
    
    One analogy that may or may not be helpful: In the same way a
    geometric transform maps a model's points in its rest space into the
    world coordinates for a particular instance, a PcpMapFunction maps
    values about a referenced model into the composed scene for a
    particular instance of that model. But rather than translating and
    rotating points, the map function shifts the values in namespace (and
    time).
    
    """
    __instance_size__: typing.ClassVar[int] = 72
    @staticmethod
    def Compose(*args, **kwargs):
        """
        
        Compose(f) -> MapFunction
        
        
        Compose this map over the given map function.
        
        
        The result will represent the application of f followed by the
        application of this function.
        
        
        Parameters
        ----------
        f : MapFunction
        
        
        """
    @staticmethod
    def ComposeOffset(*args, **kwargs):
        """
        
        ComposeOffset(newOffset) -> MapFunction
        
        
        Compose this map function over a hypothetical map function that has an
        identity path mapping and ``offset`` .
        
        
        This is equivalent to building such a map function and invoking
        Compose() , but is faster.
        
        
        Parameters
        ----------
        newOffset : LayerOffset
        
        
        """
    @staticmethod
    def GetInverse(*args, **kwargs):
        """
        
        GetInverse() -> MapFunction
        
        
        Return the inverse of this map function.
        
        
        This returns a true inverse ``inv:`` for any path p in this function's
        domain that it maps to p', inv(p') ->p.
        
        
        
        """
    @staticmethod
    def Identity(*args, **kwargs):
        """
        
        **classmethod** Identity() -> MapFunction
        
        
        Construct an identity map function.
        
        
        
        """
    @staticmethod
    def IdentityPathMap(*args, **kwargs):
        """
        
        **classmethod** IdentityPathMap() -> PathMap
        
        
        Returns an identity path mapping.
        
        
        
        """
    @staticmethod
    def MapSourceToTarget(*args, **kwargs):
        """
        
        MapSourceToTarget(path) -> Path
        
        
        Map a path in the source namespace to the target.
        
        
        If the path is not in the domain, returns an empty path.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def MapTargetToSource(*args, **kwargs):
        """
        
        MapTargetToSource(path) -> Path
        
        
        Map a path in the target namespace to the source.
        
        
        If the path is not in the co-domain, returns an empty path.
        
        
        Parameters
        ----------
        path : Path
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        
        __init__()
        
        
        Construct a null function.
        
        
        
        
        ----------------------------------------------------------------------
        
        __init__(sourceToTargetBegin, sourceToTargetEnd, offset, hasRootIdentity)
        
        
        Parameters
        ----------
        sourceToTargetBegin : PathPair
        
        sourceToTargetEnd : PathPair
        
        offset : LayerOffset
        
        hasRootIdentity : bool
        
        
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def isIdentity(*args, **kwargs):
        """
        type : bool
        
        
        Return true if the map function is the identity function.
        
        
        The identity function has an identity path mapping and time offset.
        """
    @property
    def isIdentityPathMapping(*args, **kwargs):
        """
        type : bool
        
        
        Return true if the map function uses the identity path mapping.
        
        
        If true, MapSourceToTarget() always returns the path unchanged.
        However, this map function may have a non-identity time offset.
        """
    @property
    def isNull(*args, **kwargs):
        """
        type : bool
        
        
        Return true if this map function is the null function.
        
        
        For a null function, MapSourceToTarget() always returns an empty path.
        """
    @property
    def sourceToTargetMap(*args, **kwargs):
        """
        type : PathMap
        
        
        The set of path mappings, from source to target.
        """
    @property
    def timeOffset(*args, **kwargs):
        """
        type : LayerOffset
        
        
        The time offset of the mapping.
        """
class NodeRef(Boost.Python.instance):
    """
    
    PcpNode represents a node in an expression tree for compositing scene
    description.
    
    A node represents the opinions from a particular site. In addition, it
    may have child nodes, representing nested expressions that are
    composited over/under this node.
    
    Child nodes are stored and composited in strength order.
    
    Each node holds information about the arc to its parent. This captures
    both the relative strength of the sub-expression as well as any value-
    mapping needed, such as to rename opinions from a model to use in a
    particular instance.
    
    """
    @staticmethod
    def CanContributeSpecs(*args, **kwargs):
        """
        
        CanContributeSpecs() -> bool
        
        
        Returns true if this node is allowed to contribute opinions for
        composition, false otherwise.
        
        
        
        """
    @staticmethod
    def GetDepthBelowIntroduction(*args, **kwargs):
        """
        
        GetDepthBelowIntroduction() -> int
        
        
        Return the number of levels of namespace this node's site is below the
        level at which it was introduced by an arc.
        
        
        
        """
    @staticmethod
    def GetIntroPath(*args, **kwargs):
        """
        
        GetIntroPath() -> Path
        
        
        Get the path that introduced this node.
        
        
        Specifically, this is the path the parent node had at the level of
        namespace where this node was added as a child. For a root node, this
        returns the absolute root path. See also GetDepthBelowIntroduction() .
        
        
        
        """
    @staticmethod
    def GetOriginRootNode(*args, **kwargs):
        """
        
        GetOriginRootNode() -> NodeRef
        
        
        Walk up to the root origin node for this node.
        
        
        This is the very first node that caused this node to be added to the
        graph. For instance, the root origin node of an implied inherit is the
        original inherit node.
        
        
        
        """
    @staticmethod
    def GetPathAtIntroduction(*args, **kwargs):
        """
        
        GetPathAtIntroduction() -> Path
        
        
        Returns the path for this node's site when it was introduced.
        
        
        
        """
    @staticmethod
    def GetRootNode(*args, **kwargs):
        """
        
        GetRootNode() -> NodeRef
        
        
        Walk up to the root node of this expression.
        
        
        
        """
    @staticmethod
    def IsDueToAncestor(*args, **kwargs):
        """
        
        IsDueToAncestor() -> bool
        
        
        
        """
    @staticmethod
    def IsRootNode(*args, **kwargs):
        """
        
        IsRootNode() -> bool
        
        
        Returns true if this node is the root node of the prim index graph.
        
        
        
        """
    @staticmethod
    def __eq__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __ne__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def arcType(*args, **kwargs):
        """
        type : ArcType
        
        
        Returns the type of arc connecting this node to its parent node.
        """
    @property
    def children(*args, **kwargs):
        ...
    @property
    def hasSpecs(*args, **kwargs):
        """
        type : None
        
        
        Returns true if this node has opinions authored for composition, false
        otherwise.
        """
    @property
    def hasSymmetry(*args, **kwargs):
        """
        type : None
        
        
        Get/set whether this node provides any symmetry opinions, either
        directly or from a namespace ancestor.
        """
    @property
    def isCulled(*args, **kwargs):
        """
        type : bool
        """
    @property
    def isInert(*args, **kwargs):
        """
        type : bool
        """
    @property
    def isRestricted(*args, **kwargs):
        """
        type : bool
        """
    @property
    def layerStack(*args, **kwargs):
        """
        type : LayerStack
        
        
        Returns the layer stack for the site this node represents.
        """
    @property
    def mapToParent(*args, **kwargs):
        """
        type : MapExpression
        
        
        Returns mapping function used to translate paths and values from this
        node to its parent node.
        """
    @property
    def mapToRoot(*args, **kwargs):
        """
        type : MapExpression
        
        
        Returns mapping function used to translate paths and values from this
        node directly to the root node.
        """
    @property
    def namespaceDepth(*args, **kwargs):
        """
        type : int
        
        
        Returns the absolute namespace depth of the node that introduced this
        node.
        
        
        Note that this does *not* count any variant selections.
        """
    @property
    def origin(*args, **kwargs):
        ...
    @property
    def parent(*args, **kwargs):
        ...
    @property
    def path(*args, **kwargs):
        """
        type : Path
        
        
        Returns the path for the site this node represents.
        """
    @property
    def permission(*args, **kwargs):
        """
        type : Permission
        
        ----------------------------------------------------------------------
        
        type : None
        
        
        Get/set the permission for this node.
        
        
        This indicates whether specs on this node can be accessed from other
        nodes.
        """
    @property
    def siblingNumAtOrigin(*args, **kwargs):
        """
        type : int
        
        
        Returns this node's index among siblings with the same arc type at
        this node's origin.
        """
    @property
    def site(*args, **kwargs):
        """
        type : LayerStackSite
        
        
        Get the site this node represents.
        """
class PrimIndex(Boost.Python.instance):
    """
    
    PcpPrimIndex is an index of the all sites of scene description that
    contribute opinions to a specific prim, under composition semantics.
    
    PcpComputePrimIndex() builds an index ("indexes") the given prim site.
    At any site there may be scene description values expressing arcs that
    represent instructions to pull in further scene description.
    PcpComputePrimIndex() recursively follows these arcs, building and
    ordering the results.
    
    """
    @staticmethod
    def ComposeAuthoredVariantSelections(*args, **kwargs):
        """
        
        ComposeAuthoredVariantSelections() -> SdfVariantSelectionMap
        
        
        Compose the authored prim variant selections.
        
        
        These are the variant selections expressed in scene description. Note
        that these selections may not have actually been applied, if they are
        invalid.
        
        This result is not cached, but computed each time.
        
        
        
        """
    @staticmethod
    def ComputePrimChildNames(*args, **kwargs):
        """
        
        ComputePrimChildNames(nameOrder, prohibitedNameSet) -> None
        
        
        Compute the prim child names for the given path.
        
        
        ``errors`` will contain any errors encountered while performing this
        operation.
        
        
        Parameters
        ----------
        nameOrder : list[str]
        
        prohibitedNameSet : PcpTokenSet
        
        
        """
    @staticmethod
    def ComputePrimPropertyNames(*args, **kwargs):
        """
        
        ComputePrimPropertyNames(nameOrder) -> None
        
        
        Compute the prim property names for the given path.
        
        
        ``errors`` will contain any errors encountered while performing this
        operation. The ``nameOrder`` vector must not contain any duplicate
        entries.
        
        
        Parameters
        ----------
        nameOrder : list[str]
        
        
        """
    @staticmethod
    def DumpToDotGraph(*args, **kwargs):
        """
        
        DumpToDotGraph(filename, includeInheritOriginInfo, includeMaps) -> None
        
        
        Dump the prim index in dot format to the file named ``filename`` .
        
        
        See Dump(\\.\\.\\.) for information regarding arguments.
        
        
        Parameters
        ----------
        filename : str
        
        includeInheritOriginInfo : bool
        
        includeMaps : bool
        
        
        """
    @staticmethod
    def DumpToString(*args, **kwargs):
        """
        
        DumpToString(includeInheritOriginInfo, includeMaps) -> str
        
        
        Dump the prim index contents to a string.
        
        
        If ``includeInheritOriginInfo`` is ``true`` , output for implied
        inherit nodes will include information about the originating inherit
        node. If ``includeMaps`` is ``true`` , output for each node will
        include the mappings to the parent and root node.
        
        
        Parameters
        ----------
        includeInheritOriginInfo : bool
        
        includeMaps : bool
        
        
        """
    @staticmethod
    def GetNodeProvidingSpec(*args, **kwargs):
        """
        
        GetNodeProvidingSpec(primSpec) -> NodeRef
        
        
        Returns the node that brings opinions from ``primSpec`` into this prim
        index.
        
        
        If no such node exists, returns an invalid PcpNodeRef.
        
        
        Parameters
        ----------
        primSpec : PrimSpec
        
        
        
        ----------------------------------------------------------------------
        
        GetNodeProvidingSpec(layer, path) -> NodeRef
        
        
        Returns the node that brings opinions from the Sd prim spec at
        ``layer`` and ``path`` into this prim index.
        
        
        If no such node exists, returns an invalid PcpNodeRef.
        
        
        Parameters
        ----------
        layer : Layer
        
        path : Path
        
        
        """
    @staticmethod
    def GetSelectionAppliedForVariantSet(*args, **kwargs):
        """
        
        GetSelectionAppliedForVariantSet(variantSet) -> str
        
        
        Return the variant selection applied for the named variant set.
        
        
        If none was applied, this returns an empty string. This can be
        different from the authored variant selection; for example, if the
        authored selection is invalid.
        
        
        Parameters
        ----------
        variantSet : str
        
        
        """
    @staticmethod
    def IsInstanceable(*args, **kwargs):
        """
        
        IsInstanceable() -> bool
        
        
        Returns true if this prim index is instanceable.
        
        
        Instanceable prim indexes with the same instance key are guaranteed to
        have the same set of opinions, but may not have local opinions about
        name children.
        
        PcpInstanceKey
        
        
        
        """
    @staticmethod
    def IsValid(*args, **kwargs):
        """
        
        IsValid() -> bool
        
        
        Return true if this index is valid.
        
        
        A default-constructed index is invalid.
        
        
        
        """
    @staticmethod
    def PrintStatistics(*args, **kwargs):
        """
        
        PrintStatistics() -> None
        
        
        Prints various statistics about this prim index.
        
        
        
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
    @property
    def hasAnyPayloads(*args, **kwargs):
        ...
    @property
    def localErrors(*args, **kwargs):
        """
        type : list[PcpError]
        
        
        Return the list of errors local to this prim.
        """
    @property
    def primStack(*args, **kwargs):
        ...
    @property
    def rootNode(*args, **kwargs):
        """
        type : NodeRef
        
        
        Returns the root node of the prim index graph.
        """
class PropertyIndex(Boost.Python.instance):
    """
    
    PcpPropertyIndex is an index of all sites in scene description that
    contribute opinions to a specific property, under composition
    semantics.
    
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
    @property
    def localErrors(*args, **kwargs):
        """
        type : list[PcpError]
        
        
        Return the list of errors local to this property.
        """
    @property
    def localPropertyStack(*args, **kwargs):
        ...
    @property
    def propertyStack(*args, **kwargs):
        ...
class Site(Boost.Python.instance):
    """
    
    A site specifies a path in a layer stack of scene description.
    
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
    @staticmethod
    def __str__(*args, **kwargs):
        ...
    @property
    def layerStack(*args, **kwargs):
        ...
    @layerStack.setter
    def layerStack(*args, **kwargs):
        ...
    @property
    def path(*args, **kwargs):
        ...
    @path.setter
    def path(*args, **kwargs):
        ...
class _TestChangeProcessor(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def GetPrimChanges(*args, **kwargs):
        ...
    @staticmethod
    def GetSignificantChanges(*args, **kwargs):
        ...
    @staticmethod
    def GetSpecChanges(*args, **kwargs):
        ...
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
ArcTypeInherit: ArcType  # value = Pcp.ArcTypeInherit
ArcTypePayload: ArcType  # value = Pcp.ArcTypePayload
ArcTypeReference: ArcType  # value = Pcp.ArcTypeReference
ArcTypeRelocate: ArcType  # value = Pcp.ArcTypeRelocate
ArcTypeRoot: ArcType  # value = Pcp.ArcTypeRoot
ArcTypeSpecialize: ArcType  # value = Pcp.ArcTypeSpecialize
ArcTypeVariant: ArcType  # value = Pcp.ArcTypeVariant
DependencyTypeAncestral: DependencyType  # value = Pcp.DependencyTypeAncestral
DependencyTypeAnyIncludingVirtual: DependencyType  # value = Pcp.DependencyTypeAnyIncludingVirtual
DependencyTypeAnyNonVirtual: DependencyType  # value = Pcp.DependencyTypeAnyNonVirtual
DependencyTypeDirect: DependencyType  # value = Pcp.DependencyTypeDirect
DependencyTypeNonVirtual: DependencyType  # value = Pcp.DependencyTypeNonVirtual
DependencyTypeNone: DependencyType  # value = Pcp.DependencyTypeNone
DependencyTypePartlyDirect: DependencyType  # value = Pcp.DependencyTypePartlyDirect
DependencyTypePurelyDirect: DependencyType  # value = Pcp.DependencyTypePurelyDirect
DependencyTypeRoot: DependencyType  # value = Pcp.DependencyTypeRoot
DependencyTypeVirtual: DependencyType  # value = Pcp.DependencyTypeVirtual
ErrorType_ArcCapacityExceeded: ErrorType  # value = Pcp.ErrorType_ArcCapacityExceeded
ErrorType_ArcCycle: ErrorType  # value = Pcp.ErrorType_ArcCycle
ErrorType_ArcNamespaceDepthCapacityExceeded: ErrorType  # value = Pcp.ErrorType_ArcNamespaceDepthCapacityExceeded
ErrorType_ArcPermissionDenied: ErrorType  # value = Pcp.ErrorType_ArcPermissionDenied
ErrorType_InconsistentAttributeType: ErrorType  # value = Pcp.ErrorType_InconsistentAttributeType
ErrorType_InconsistentAttributeVariability: ErrorType  # value = Pcp.ErrorType_InconsistentAttributeVariability
ErrorType_InconsistentPropertyType: ErrorType  # value = Pcp.ErrorType_InconsistentPropertyType
ErrorType_IndexCapacityExceeded: ErrorType  # value = Pcp.ErrorType_IndexCapacityExceeded
ErrorType_InternalAssetPath: ErrorType  # value = Pcp.ErrorType_InternalAssetPath
ErrorType_InvalidAssetPath: ErrorType  # value = Pcp.ErrorType_InvalidAssetPath
ErrorType_InvalidExternalTargetPath: ErrorType  # value = Pcp.ErrorType_InvalidExternalTargetPath
ErrorType_InvalidInstanceTargetPath: ErrorType  # value = Pcp.ErrorType_InvalidInstanceTargetPath
ErrorType_InvalidPrimPath: ErrorType  # value = Pcp.ErrorType_InvalidPrimPath
ErrorType_InvalidReferenceOffset: ErrorType  # value = Pcp.ErrorType_InvalidReferenceOffset
ErrorType_InvalidSublayerOffset: ErrorType  # value = Pcp.ErrorType_InvalidSublayerOffset
ErrorType_InvalidSublayerOwnership: ErrorType  # value = Pcp.ErrorType_InvalidSublayerOwnership
ErrorType_InvalidSublayerPath: ErrorType  # value = Pcp.ErrorType_InvalidSublayerPath
ErrorType_InvalidTargetPath: ErrorType  # value = Pcp.ErrorType_InvalidTargetPath
ErrorType_InvalidVariantSelection: ErrorType  # value = Pcp.ErrorType_InvalidVariantSelection
ErrorType_OpinionAtRelocationSource: ErrorType  # value = Pcp.ErrorType_OpinionAtRelocationSource
ErrorType_PrimPermissionDenied: ErrorType  # value = Pcp.ErrorType_PrimPermissionDenied
ErrorType_PropertyPermissionDenied: ErrorType  # value = Pcp.ErrorType_PropertyPermissionDenied
ErrorType_SublayerCycle: ErrorType  # value = Pcp.ErrorType_SublayerCycle
ErrorType_TargetPermissionDenied: ErrorType  # value = Pcp.ErrorType_TargetPermissionDenied
ErrorType_UnresolvedPrimPath: ErrorType  # value = Pcp.ErrorType_UnresolvedPrimPath
__MFB_FULL_PACKAGE_NAME: str = 'pcp'
