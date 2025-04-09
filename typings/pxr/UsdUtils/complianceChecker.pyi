import __future__
from __future__ import annotations
from pxr import Ar
import pxr.UsdUtils.constantsGroup
from pxr.UsdUtils.constantsGroup import ConstantsGroup
import typing
__all__ = ['ARKitFileExtensionChecker', 'ARKitLayerChecker', 'ARKitMaterialBindingChecker', 'ARKitPackageEncapsulationChecker', 'ARKitPrimTypeChecker', 'ARKitRootLayerChecker', 'ARKitShaderChecker', 'Ar', 'BaseRuleChecker', 'ByteAlignmentChecker', 'ComplianceChecker', 'CompressionChecker', 'ConstantsGroup', 'MaterialBindingAPIAppliedChecker', 'MissingReferenceChecker', 'NodeTypes', 'NormalMapTextureChecker', 'PrimEncapsulationChecker', 'ShaderProps', 'StageMetadataChecker', 'TextureChecker', 'print_function']
class ARKitFileExtensionChecker(BaseRuleChecker):
    _allowedFileExtensions: typing.ClassVar[tuple] = ('usd', 'usda', 'usdc', 'usdz', 'jpg', 'png')
    @staticmethod
    def GetDescription():
        ...
    def CheckZipFile(self, zipFile, packagePath):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class ARKitLayerChecker(BaseRuleChecker):
    _allowedLayerFormatIds: typing.ClassVar[tuple] = ('usd', 'usda', 'usdc', 'usdz')
    @staticmethod
    def GetDescription():
        ...
    def CheckLayer(self, layer):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class ARKitMaterialBindingChecker(BaseRuleChecker):
    @staticmethod
    def GetDescription():
        ...
    def CheckPrim(self, prim):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class ARKitPackageEncapsulationChecker(BaseRuleChecker):
    @staticmethod
    def GetDescription():
        ...
    def CheckDependencies(self, usdStage, layerDeps, assetDeps):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class ARKitPrimTypeChecker(BaseRuleChecker):
    _allowedPrimTypeNames: typing.ClassVar[tuple] = ('', 'Scope', 'Xform', 'Camera', 'Shader', 'Material', 'Mesh', 'Sphere', 'Cube', 'Cylinder', 'Cone', 'Capsule', 'GeomSubset', 'Points', 'SkelRoot', 'Skeleton', 'SkelAnimation', 'BlendShape', 'SpatialAudio')
    @staticmethod
    def GetDescription():
        ...
    def CheckPrim(self, prim):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class ARKitRootLayerChecker(BaseRuleChecker):
    @staticmethod
    def GetDescription():
        ...
    def CheckStage(self, usdStage):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class ARKitShaderChecker(BaseRuleChecker):
    @staticmethod
    def GetDescription():
        ...
    def CheckPrim(self, prim):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class BaseRuleChecker:
    """
    This is Base class for all the rule-checkers.
    """
    def CheckDependencies(self, usdStage, layerDeps, assetDeps):
        """
         Check usdStage's layer and asset dependencies that were gathered 
                    using UsdUtils.ComputeAllDependencies().
                
        """
    def CheckDiagnostics(self, diagnostics):
        """
         Check the diagnostic messages that were generated when opening the 
                    USD stage. The diagnostic messages are collected using a 
                    UsdUtilsCoalescingDiagnosticDelegate.
                
        """
    def CheckLayer(self, layer):
        """
         Check the given SdfLayer. 
        """
    def CheckPrim(self, prim):
        """
         Check the given prim, which may only exist is a specific combination
                    of variant selections on the UsdStage.
                
        """
    def CheckStage(self, usdStage):
        """
         Check the given usdStage. 
        """
    def CheckUnresolvedPaths(self, unresolvedPaths):
        """
         Check or process any unresolved asset paths that were found when 
                    analysing the dependencies.
                
        """
    def CheckZipFile(self, zipFile, packagePath):
        """
         Check the zipFile object created by opening the package at path 
                    packagePath.
                
        """
    def GetErrors(self):
        ...
    def GetFailedChecks(self):
        ...
    def GetWarnings(self):
        ...
    def ResetCaches(self):
        """
         Reset any caches the rule owns.  Called whenever stage authoring
                occurs, such as when we iterate through VariantSet combinations.
                
        """
    def _AddError(self, msg):
        ...
    def _AddFailedCheck(self, msg):
        ...
    def _AddWarning(self, msg):
        ...
    def _Msg(self, msg):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class ByteAlignmentChecker(BaseRuleChecker):
    @staticmethod
    def GetDescription():
        ...
    def CheckZipFile(self, zipFile, packagePath):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class ComplianceChecker:
    """
     A utility class for checking compliance of a given USD asset or a USDZ 
        package.
    
        Since usdz files are zip files, someone could use generic zip tools to 
        create an archive and just change the extension, producing a .usdz file that 
        does not honor the additional constraints that usdz files require.  Even if 
        someone does use our official archive creation tools, though, we 
        intentionally allow creation of usdz files that can be very "permissive" in 
        their contents for internal studio uses, where portability outside the 
        studio is not a concern.  For content meant to be delivered over the web 
        (eg. ARKit assets), however, we must be much more restrictive.
    
        This class provides two levels of compliance checking: 
        * "structural" validation that is represented by a set of base rules. 
        * "ARKit" compatibility validation, which includes many more restrictions.
        
        Calling ComplianceChecker.DumpAllRules() will print an enumeration of the 
        various rules in the two categories of compliance checking.
        
    """
    @staticmethod
    def DumpAllRules():
        ...
    @staticmethod
    def GetARKitRules(skipARKitRootLayerCheck = False):
        ...
    @staticmethod
    def GetBaseRules():
        ...
    @staticmethod
    def GetRules(arkit = False, skipARKitRootLayerCheck = False):
        ...
    def CheckCompliance(self, inputFile):
        ...
    def DumpRules(self):
        ...
    def GetErrors(self):
        ...
    def GetFailedChecks(self):
        ...
    def GetWarnings(self):
        ...
    def _AddError(self, errMsg):
        ...
    def _AddWarning(self, errMsg):
        ...
    def _CheckLayer(self, layer):
        ...
    def _CheckPackage(self, packagePath):
        ...
    def _CheckPrim(self, prim):
        ...
    def _Msg(self, msg):
        ...
    def _TraverseRange(self, primRangeIt, isStageRoot):
        ...
    def _TraverseVariants(self, prim):
        ...
    def __init__(self, arkit = False, skipARKitRootLayerCheck = False, rootPackageOnly = False, skipVariants = False, verbose = False, assetLevelChecks = True):
        ...
class CompressionChecker(BaseRuleChecker):
    @staticmethod
    def GetDescription():
        ...
    def CheckZipFile(self, zipFile, packagePath):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class MaterialBindingAPIAppliedChecker(BaseRuleChecker):
    @staticmethod
    def GetDescription():
        ...
    def CheckPrim(self, prim):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class MissingReferenceChecker(BaseRuleChecker):
    @staticmethod
    def GetDescription():
        ...
    def CheckDiagnostics(self, diagnostics):
        ...
    def CheckUnresolvedPaths(self, unresolvedPaths):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class NodeTypes(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    UsdPreviewSurface: typing.ClassVar[str] = 'UsdPreviewSurface'
    UsdPrimvarReader: typing.ClassVar[str] = 'UsdPrimvarReader'
    UsdTransform2d: typing.ClassVar[str] = 'UsdTransform2d'
    UsdUVTexture: typing.ClassVar[str] = 'UsdUVTexture'
    _all: typing.ClassVar[tuple] = ('UsdPreviewSurface', 'UsdUVTexture', 'UsdTransform2d', 'UsdPrimvarReader')
class NormalMapTextureChecker(BaseRuleChecker):
    @staticmethod
    def GetDescription():
        ...
    def CheckPrim(self, prim):
        ...
    def _GetInputValue(self, shader, inputName):
        ...
    def _GetShaderId(self, shader):
        ...
    def _TextureIs8Bit(self, asset):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class PrimEncapsulationChecker(BaseRuleChecker):
    @staticmethod
    def GetDescription():
        ...
    def CheckPrim(self, prim):
        ...
    def ResetCaches(self):
        ...
    def _FindConnectableAncestor(self, prim):
        ...
    def _HasGprimAncestor(self, prim):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class ShaderProps(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    Bias: typing.ClassVar[str] = 'bias'
    File: typing.ClassVar[str] = 'file'
    Normal: typing.ClassVar[str] = 'normal'
    Scale: typing.ClassVar[str] = 'scale'
    SourceColorSpace: typing.ClassVar[str] = 'sourceColorSpace'
    _all: typing.ClassVar[tuple] = ('bias', 'scale', 'sourceColorSpace', 'normal', 'file')
class StageMetadataChecker(BaseRuleChecker):
    @staticmethod
    def GetDescription():
        ...
    def CheckStage(self, usdStage):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
class TextureChecker(BaseRuleChecker):
    _basicUSDZImageFormats: typing.ClassVar[tuple] = ('jpg', 'png')
    _extraUSDZ_OIIOImageFormats: typing.ClassVar[str] = '.exr'
    _unsupportedImageFormats: typing.ClassVar[list] = ['bmp', 'tga', 'hdr', 'exr', 'tif', 'zfile', 'tx']
    @staticmethod
    def GetDescription():
        ...
    def CheckPrim(self, prim):
        ...
    def CheckStage(self, usdStage):
        ...
    def _CheckTexture(self, texAssetPath, inputPath):
        ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks):
        ...
def _IsPackageOrPackagedLayer(layer):
    ...
print_function: __future__._Feature  # value = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 1048576)
