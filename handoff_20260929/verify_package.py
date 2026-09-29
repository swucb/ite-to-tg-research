"""Verify every frozen package payload hash; MANIFEST itself is excluded."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / 'MANIFEST.json').read_text())
for name, digest in manifest['sha256'].items():
    path = ROOT / name
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise SystemExit('FAIL: ' + name)
print('PASS:', len(manifest['sha256']), 'files. Integrity only; not scientific validation.')
