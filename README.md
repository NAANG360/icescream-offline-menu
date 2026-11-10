# IceScream 1.0.1 — offline menu workspace

A temporary workspace for a personal offline modification of the Unity Mono game APK.

## Target behavior

- Remove the obsolete online token-verification dependency from the mod-menu flow.
- Make the mod-menu button open the menu immediately.
- Keep the result local/offline, without telemetry or remote authentication.

## Base64 reconstruction utility

The APK can be represented as ordered Base64 text parts and rebuilt with [tools/convert.py](tools/convert.py).

Example:

```bash
python3 tools/convert.py icescream-1.0.1.part01.b64 icescream-1.0.1.part02.b64 icescream-1.0.1.part03.b64 icescream-1.0.1.part04.b64 --sha256 f9dba7d2babd7804d8296d2636777ae35deca372afb37e16da5086435c714355
```

The source APK is 103,513,528 bytes. Its SHA-256 is:
`f9dba7d2babd7804d8296d2636777ae35deca372afb37e16da5086435c714355`.

The Base64 parts are not committed in this repository yet. The converter is committed; the encoded payload is kept as a separate archive until a supported binary-asset transfer route is available.

## Inspection findings

- Managed assembly path: `assets/bin/Data/Managed/Assembly-CSharp.dll`
- Relevant symbols: `Menu.VerifyToken`, `Menu.UpdateToken`, `Menu.ToggleMenu`
- The APK has not yet been modified or rebuilt. A valid output must be patched, repackaged, signed, and install-tested before it is called complete.

## Temporary-repository lifecycle

This repository is public at the user's request. Once the temporary transfer/build work is finished, restore private visibility or delete the repository as requested.
