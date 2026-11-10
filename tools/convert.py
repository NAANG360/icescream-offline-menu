#!/usr/bin/env python3
"""Rebuild IceScream-1.0.1.apk from ordered Base64 text parts."""
from pathlib import Path
import argparse, base64, hashlib, re, sys

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("parts", nargs="+", help="Base64 part files, in part order")
    p.add_argument("-o", "--output", default="IceScream-1.0.1.apk")
    p.add_argument("--sha256", help="Optional expected SHA-256 checksum")
    args = p.parse_args()
    digest, total = hashlib.sha256(), 0
    try:
        with open(args.output, "wb") as out:
            for part in args.parts:
                compact = re.sub(r"\\s+", "", Path(part).read_text(encoding="ascii"))
                data = base64.b64decode(compact, validate=True)
                out.write(data)
                digest.update(data)
                total += len(data)
    except Exception as exc:
        print(f"Conversion failed: {exc}", file=sys.stderr)
        return 2
    actual = digest.hexdigest()
    print(f"Wrote {args.output} ({total:,} bytes)")
    print(f"SHA-256: {actual}")
    if args.sha256 and actual.lower() != args.sha256.lower():
        print("ERROR: checksum mismatch", file=sys.stderr)
        return 3
    print("Checksum verified." if args.sha256 else "No expected checksum supplied.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
