#!/usr/bin/env python3
"""
Safe extended plane realistifier.

Use this instead of realistify_mchelio_planes_extended.py if planes are tearing
apart from overspeed/compressibility or if MaxHp must be left untouched.

Run from repo root:
  python tools/realistify_mchelio_planes_extended_safe.py --dry-run
  python tools/realistify_mchelio_planes_extended_safe.py --apply

What this wrapper changes:
  - MaxHp / MaxHP writes are blocked completely.
  - MaxSafeSpeed is forced very high so existing speed*1000 runtime scaling does
    not instantly trigger overspeed.
  - OverspeedDamageRate is forced to 0.
  - CompressibilitySpeed is forced very high so pitch authority is not instantly
    crushed by the same scaling mismatch.

Everything else comes from realistify_mchelio_planes_extended.py.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

EXTENDED_PATH = Path(__file__).with_name("realistify_mchelio_planes_extended.py")

spec = importlib.util.spec_from_file_location("realistify_mchelio_planes_extended", EXTENDED_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load {EXTENDED_PATH}")

extended = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = extended
spec.loader.exec_module(extended)

base = extended.module
_original_insert_or_replace = base.insert_or_replace

# Keep this huge so the in-code speed*1000 scaling cannot instantly overspeed.
SAFE_MAX_SPEED = 9999.0
SAFE_COMPRESSIBILITY_SPEED = 9999.0


def insert_or_replace_safe(text, key, value, after=None):
    key_l = str(key).lower()

    # Absolutely do not touch aircraft health in this runner.
    if key_l in ("maxhp", "max_hp"):
        return text

    # Disable destructive speed-limit effects until the runtime scaling is fixed
    # or a separate config convention is chosen.
    if key_l == "maxsafespeed":
        return _original_insert_or_replace(text, key, SAFE_MAX_SPEED, after)
    if key_l == "overspeeddamagerate":
        return _original_insert_or_replace(text, key, 0.0, after)
    if key_l == "compressibilityspeed":
        return _original_insert_or_replace(text, key, SAFE_COMPRESSIBILITY_SPEED, after)
    if key_l == "compressibilitypitchpenalty":
        return _original_insert_or_replace(text, key, 0.0, after)

    return _original_insert_or_replace(text, key, value, after)


base.insert_or_replace = insert_or_replace_safe

if __name__ == "__main__":
    raise SystemExit(base.main())
