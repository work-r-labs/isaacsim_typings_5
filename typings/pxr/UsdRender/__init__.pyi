from __future__ import annotations
import pxr.Usd
import typing
__all__: list[str] = ['DenoisePass', 'Pass', 'Product', 'Settings', 'SettingsBase', 'Tokens', 'Var']
class DenoisePass(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Pass(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateCommandAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDenoiseEnableAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDenoisePassRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateFileNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateInputPassesRel(*args, **kwargs):
        ...
    @staticmethod
    def CreatePassTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateRenderSourceRel(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetCommandAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDenoiseEnableAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDenoisePassRel(*args, **kwargs):
        ...
    @staticmethod
    def GetFileNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetInputPassesRel(*args, **kwargs):
        ...
    @staticmethod
    def GetPassTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetRenderSourceRel(*args, **kwargs):
        ...
    @staticmethod
    def GetRenderVisibilityCollectionAPI(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Product(SettingsBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateOrderedVarsRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateProductNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateProductTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetOrderedVarsRel(*args, **kwargs):
        ...
    @staticmethod
    def GetProductNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetProductTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Settings(SettingsBase):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateIncludedPurposesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateMaterialBindingPurposesAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateProductsRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateRenderingColorSpaceAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetIncludedPurposesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetMaterialBindingPurposesAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetProductsRel(*args, **kwargs):
        ...
    @staticmethod
    def GetRenderingColorSpaceAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetStageRenderSettings(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class SettingsBase(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateAspectRatioConformPolicyAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateCameraRel(*args, **kwargs):
        ...
    @staticmethod
    def CreateDataWindowNDCAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDisableDepthOfFieldAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateDisableMotionBlurAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateInstantaneousShutterAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreatePixelAspectRatioAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetAspectRatioConformPolicyAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetCameraRel(*args, **kwargs):
        ...
    @staticmethod
    def GetDataWindowNDCAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDisableDepthOfFieldAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetDisableMotionBlurAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetInstantaneousShutterAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetPixelAspectRatioAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetResolutionAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
class Tokens(Boost.Python.instance):
    RenderDenoisePass: typing.ClassVar[str] = 'RenderDenoisePass'
    RenderPass: typing.ClassVar[str] = 'RenderPass'
    RenderProduct: typing.ClassVar[str] = 'RenderProduct'
    RenderSettings: typing.ClassVar[str] = 'RenderSettings'
    RenderSettingsBase: typing.ClassVar[str] = 'RenderSettingsBase'
    RenderVar: typing.ClassVar[str] = 'RenderVar'
    adjustApertureHeight: typing.ClassVar[str] = 'adjustApertureHeight'
    adjustApertureWidth: typing.ClassVar[str] = 'adjustApertureWidth'
    adjustPixelAspectRatio: typing.ClassVar[str] = 'adjustPixelAspectRatio'
    aspectRatioConformPolicy: typing.ClassVar[str] = 'aspectRatioConformPolicy'
    camera: typing.ClassVar[str] = 'camera'
    collectionRenderVisibilityIncludeRoot: typing.ClassVar[str] = 'collection:renderVisibility:includeRoot'
    color3f: typing.ClassVar[str] = 'color3f'
    command: typing.ClassVar[str] = 'command'
    cropAperture: typing.ClassVar[str] = 'cropAperture'
    dataType: typing.ClassVar[str] = 'dataType'
    dataWindowNDC: typing.ClassVar[str] = 'dataWindowNDC'
    denoiseEnable: typing.ClassVar[str] = 'denoise:enable'
    denoisePass: typing.ClassVar[str] = 'denoise:pass'
    disableDepthOfField: typing.ClassVar[str] = 'disableDepthOfField'
    disableMotionBlur: typing.ClassVar[str] = 'disableMotionBlur'
    expandAperture: typing.ClassVar[str] = 'expandAperture'
    fileName: typing.ClassVar[str] = 'fileName'
    full: typing.ClassVar[str] = 'full'
    includedPurposes: typing.ClassVar[str] = 'includedPurposes'
    inputPasses: typing.ClassVar[str] = 'inputPasses'
    instantaneousShutter: typing.ClassVar[str] = 'instantaneousShutter'
    intrinsic: typing.ClassVar[str] = 'intrinsic'
    lpe: typing.ClassVar[str] = 'lpe'
    materialBindingPurposes: typing.ClassVar[str] = 'materialBindingPurposes'
    orderedVars: typing.ClassVar[str] = 'orderedVars'
    passType: typing.ClassVar[str] = 'passType'
    pixelAspectRatio: typing.ClassVar[str] = 'pixelAspectRatio'
    preview: typing.ClassVar[str] = 'preview'
    primvar: typing.ClassVar[str] = 'primvar'
    productName: typing.ClassVar[str] = 'productName'
    productType: typing.ClassVar[str] = 'productType'
    products: typing.ClassVar[str] = 'products'
    raster: typing.ClassVar[str] = 'raster'
    raw: typing.ClassVar[str] = 'raw'
    renderSettingsPrimPath: typing.ClassVar[str] = 'renderSettingsPrimPath'
    renderSource: typing.ClassVar[str] = 'renderSource'
    renderVisibility: typing.ClassVar[str] = 'renderVisibility'
    renderingColorSpace: typing.ClassVar[str] = 'renderingColorSpace'
    resolution: typing.ClassVar[str] = 'resolution'
    sourceName: typing.ClassVar[str] = 'sourceName'
    sourceType: typing.ClassVar[str] = 'sourceType'
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
class Var(pxr.Usd.Typed):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def CreateDataTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSourceNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def CreateSourceTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def Define(*args, **kwargs):
        ...
    @staticmethod
    def Get(*args, **kwargs):
        ...
    @staticmethod
    def GetDataTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSchemaAttributeNames(*args, **kwargs):
        ...
    @staticmethod
    def GetSourceNameAttr(*args, **kwargs):
        ...
    @staticmethod
    def GetSourceTypeAttr(*args, **kwargs):
        ...
    @staticmethod
    def _GetStaticTfType(*args, **kwargs):
        ...
    @staticmethod
    def __bool__(*args, **kwargs):
        ...
    @staticmethod
    def __init__(*args, **kwargs):
        ...
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        ...
__MFB_FULL_PACKAGE_NAME: str = 'usdRender'
