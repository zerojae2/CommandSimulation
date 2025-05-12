// Copyright HTC Corporation. All Rights Reserved.

using UnrealBuildTool;
using System.IO;

namespace UnrealBuildTool.Rules
{
    public class ViveOpenXRHandInteraction : ModuleRules
    {
        public ViveOpenXRHandInteraction(ReadOnlyTargetRules Target) : base(Target)
        {
            PCHUsage = ModuleRules.PCHUsageMode.UseExplicitOrSharedPCHs;

            var EngineDir = Path.GetFullPath(Target.RelativeEnginePath);
            PrivateIncludePaths.AddRange(
                new string[] {
                        EngineDir + "/Source/ThirdParty/OpenXR/include",
                        EngineDir + "/Plugins/Runtime/OpenXR/Source/OpenXRHMD/Private",
                        EngineDir + "/Plugins/Runtime/OpenXR/Source/OpenXRInput/Private",
                }
                );


            PublicDependencyModuleNames.AddRange(
                new string[]
                {
                    "Core",
                }
                );


            PrivateDependencyModuleNames.AddRange(
                new string[]
                {
                    "CoreUObject",
                    "ApplicationCore",
                    "Engine",
                    "InputDevice",
                    "InputCore",
                    "HeadMountedDisplay",
                    "UMG",
                    "Slate",
                    "SlateCore",
                    "OpenXRHMD",
                    "OpenXRInput",
                    "XRBase"
                }
                );

            PublicDependencyModuleNames.Add("EnhancedInput");

            AddEngineThirdPartyPrivateStaticDependencies(Target, "OpenXR");

            if (Target.bBuildEditor == true)
            {
                PrivateDependencyModuleNames.Add("UnrealEd");
                PrivateDependencyModuleNames.Add("InputEditor");
            }
        }
    }
}