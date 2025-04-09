from __future__ import annotations
from pxr import Sdf
from pxr import Sdr
from pxr import Tf
from pxr import Usd
from pxr import UsdShade
import pxr.UsdUtils.constantsGroup
from pxr.UsdUtils.constantsGroup import ConstantsGroup
from pxr import Vt
import typing
__all__ = ['ConstantsGroup', 'PropertyDefiningKeys', 'SchemaDefiningKeys', 'SchemaDefiningMiscConstants', 'Sdf', 'Sdr', 'Tf', 'UpdateSchemaWithSdrNode', 'Usd', 'UsdShade', 'Vt']
class PropertyDefiningKeys(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    CONNECTABILITY: typing.ClassVar[str] = 'connectability'
    INTERNAL_DISPLAY_GROUP: typing.ClassVar[str] = 'Internal'
    NULL_VALUE: typing.ClassVar[str] = 'null'
    PROPERTY_NS_PREFIX_OVERRIDE: typing.ClassVar[str] = 'propertyNSPrefixOverride'
    SDF_VARIABILITY_UNIFORM_STRING: typing.ClassVar[str] = 'Uniform'
    SHADER_ID: typing.ClassVar[str] = 'shaderId'
    USD_SUPPRESS_PROPERTY: typing.ClassVar[str] = 'usdSuppressProperty'
    USD_VARIABILITY: typing.ClassVar[str] = 'usdVariability'
    WIDGET: typing.ClassVar[str] = 'widget'
    _all: typing.ClassVar[tuple] = ('connectability', 'Internal', 'null', 'propertyNSPrefixOverride', 'Uniform', 'shaderId', 'usdSuppressProperty', 'usdVariability', 'widget')
class SchemaDefiningKeys(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    API_SCHEMAS_FOR_ATTR_PRUNING: typing.ClassVar[str] = 'apiSchemasForAttrPruning'
    API_SCHEMA_AUTO_APPLY_TO: typing.ClassVar[str] = 'apiSchemaAutoApplyTo'
    API_SCHEMA_CAN_ONLY_APPLY_TO: typing.ClassVar[str] = 'apiSchemaCanOnlyApplyTo'
    IS_USD_SHADE_CONTAINER: typing.ClassVar[str] = 'isUsdShadeContainer'
    PROVIDES_USD_SHADE_CONNECTABLE_API_BEHAVIOR: typing.ClassVar[str] = 'providesUsdShadeConnectableAPIBehavior'
    REQUIRES_USD_SHADE_ENCAPSULATION: typing.ClassVar[str] = 'requiresUsdShadeEncapsulation'
    SCHEMA_BASE: typing.ClassVar[str] = 'schemaBase'
    SCHEMA_KIND: typing.ClassVar[str] = 'schemaKind'
    SCHEMA_NAME: typing.ClassVar[str] = 'schemaName'
    SCHEMA_PROPERTY_NS_PREFIX_OVERRIDE: typing.ClassVar[str] = 'schemaPropertyNSPrefixOverride'
    TF_TYPENAME_SUFFIX: typing.ClassVar[str] = 'tfTypeNameSuffix'
    TYPED_SCHEMA_FOR_ATTR_PRUNING: typing.ClassVar[str] = 'typedSchemaForAttrPruning'
    _all: typing.ClassVar[tuple] = ('apiSchemasForAttrPruning', 'apiSchemaAutoApplyTo', 'apiSchemaCanOnlyApplyTo', 'isUsdShadeContainer', 'schemaPropertyNSPrefixOverride', 'providesUsdShadeConnectableAPIBehavior', 'requiresUsdShadeEncapsulation', 'schemaBase', 'schemaKind', 'schemaName', 'tfTypeNameSuffix', 'typedSchemaForAttrPruning')
class SchemaDefiningMiscConstants(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    API_SCHEMA_BASE: typing.ClassVar[str] = 'APISchemaBase'
    API_STRING: typing.ClassVar[str] = 'API'
    NodeDefAPI: typing.ClassVar[str] = 'NodeDefAPI'
    SINGLE_APPLY_SCHEMA: typing.ClassVar[str] = 'singleApply'
    TYPED_SCHEMA: typing.ClassVar[str] = 'Typed'
    USD_SOURCE_TYPE: typing.ClassVar[str] = 'USD'
    _all: typing.ClassVar[tuple] = ('APISchemaBase', 'API', 'NodeDefAPI', 'singleApply', 'Typed', 'USD')
def UpdateSchemaWithSdrNode(schemaLayer, sdrNode, renderContext = '', overrideIdentifier = ''):
    """
    
        Updates the given schemaLayer with primSpec and propertySpecs from sdrNode
        metadata. 
    
        A renderContext can be provided which is used in determining the
        shaderId namespace, which follows the pattern: 
        "<renderContext>:<SdrShaderNodeContext>:shaderId". Note that we are using a
        node's context (SDR_NODE_CONTEXT_TOKENS) here to construct the shaderId
        namespace, so shader parsers should make sure to use appropriate
        SDR_NODE_CONTEXT_TOKENS in the node definitions.
    
        overrideIdentifier parameter is the identifier which should be used when 
        the identifier of the node being processed differs from the one Sdr will 
        discover at runtime, such as when this function is def a node constructed 
        from an explicit asset path. This should only be used when clients know the 
        identifier being passed is the true identifier which sdr Runtime will 
        provide when querying using GetShaderNodeByIdentifierAndType, etc.
    
        It consumes the following attributes (that manifest as Sdr 
        metadata) in addition to many of the standard Sdr metadata
        specified and parsed (via its parser plugin).
    
        Node Level Metadata:
            - "schemaName": Name of the new schema populated from the given sdrNode
              (Required)
            - "schemaKind": Specifies the UsdSchemaKind for the schema being
              populated from the sdrNode. (Note that this does not support
              multiple apply schema kinds).
            - "schemaBase": Base schema from which the new schema should inherit
              from. Note this defaults to "APISchemaBase" for an API schema or 
              "Typed" for a concrete scheme.
            - "apiSchemasForAttrPruning": A list of core API schemas which will be
              composed together and any shared shader property from this prim
              definition is pruned from the resultant schema. 
            - "typedSchemaForAttrPruning": A core typed schema which will be
              composed together with the apiSchemasForAttrPruning and any shared 
              shader property from this prim definition is pruned from the 
              resultant schema. If no typedSchemaForAttrPruning is provided then 
              only the apiSchemasForAttrPruning are composed to create a prim 
              definition. This will only be used when creating an APISchema.
            - "apiSchemaAutoApplyTo": The schemas to which the sdrNode populated 
              API schema will autoApply to.
            - "apiSchemaCanOnlyApplyTo": If specified, the API schema generated 
              from the sdrNode can only be validly applied to this set of schemas.
            - "providesUsdShadeConnectableAPIBehavior": Used to enable a 
              connectability behavior for an API schema.
            - "isUsdShadeContainer": Only used when
              providesUsdShadeConnectableAPIBehavior is set to true. Marks the
              connectable prim as a UsdShade container type.
            - "requiresUsdShadeEncapsulation": Only used when
              providesUsdShadeConnectableAPIBehavior is set to true. Configures the
              UsdShade encapsulation rules governing its connectableBehavior.
            - "tfTypeNameSuffix": Class name which will get registered with TfType 
              system. This gets appended to the domain name to register with TfType.
            - "schemaPropertyNSPrefixOverride": Node level metadata which can drive
              all node's properties namespace prefix. This can be useful for
              non connectable nodes which should not get UsdShade inputs and outputs
              namespace prefix.
    
        Property Level Metadata:
            - "usdVariability": Property level metadata which specifies a specific 
              sdrNodeProperty should have its USD variability set to Uniform or 
              Varying
            - "usdSuppressProperty": A property level metadata which determines if 
              the property should be suppressed from translation from args to 
              property spec.
            - "propertyNSPrefixOverride": Provides a way to override a property's
              namespace from the default (inputs:/outputs:) or from a node's
              schemaPropertyNSPrefixOverride metadata.
    
        Sdr Property Metadata to SdfPropertySpec Translations
            - A "null" value for Widget sdrProperty metadata translates to 
              SdfPropertySpec Hidden metadata.
            - SdrProperty's Help metadata (Label metadata if Help metadata not 
              provided) translates to SdfPropertySpec's Documentation string 
              metadata.
            - SdrProperty's Page metadata translates to SdfPropertySpec's
              DisplayGroup metadata.
            - SdrProperty's Label metadata translates to SdfPropertySpec's
              DisplayName metadata.
            - SdrProperty's Options translates to SdfPropertySpec's AllowedTokens.
            - SdrProperty's Default value translates to SdfPropertySpec's Default
              value.
            - Connectable input properties translates to InterfaceOnly
              SdfPropertySpec's CONNECTABILITY.
        
    """
def _CreateAttrSpecFromNodeAttribute(primSpec, prop, primDefForAttrPruning, schemaPropertyNSPrefixOverride, isSdrInput = True):
    ...
def _IsNSPrefixConnectableAPICompliant(nsPrefix):
    ...
