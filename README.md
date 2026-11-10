# IceScream Offline Menu — temporary workspace

This repository is a temporary build workspace for a personal, offline modification of the Unity Mono game APK.

## Target behavior

- Remove the obsolete online token-verification dependency from the mod-menu flow.
- Tapping the mod-menu button opens the menu immediately.
- Keep the result local/offline; do not add telemetry or remote authentication.

## Input handling

**Do not commit the original APK, extracted game assets, signing keys, or personal data to this public repository.** The original APK is approximately 103.5 MB and remains outside this repository.

## Current inspection findings

- Unity Mono managed assembly: `assets/bin/Data/Managed/Assembly-CSharp.dll`
- Relevant symbols found: `Menu.VerifyToken`, `Menu.UpdateToken`, and `Menu.ToggleMenu`
- The APK itself has not yet been modified or rebuilt. A valid output must be patched, repackaged, signed, and install-tested before it is called complete.

## Temporary-repository lifecycle

Delete this repository after the user confirms the finished APK has been downloaded and verified.