#!/usr/bin/env python3
"""
No-health wrapper for realistify_mchelio_planes.py.

Use this instead of realistify_mchelio_planes.py when you want the plane
realistification pass to leave MaxHp/MaxHP untouched:

  python tools/realistify_mchelio_planes_nohp.py --dry-run
  python tools/realistify_mchelio_planes_nohp.py --apply

It imports the main plane script and monkey-patches insert_or_replace so any
attempt to write MaxHp is ignored. Everything else still runs normally.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

SCRIPT_PATH = Path(__file__).with_name("realistify_mchelio_planes.py")

spec = importlib.util.spec_from_file_location("realistify_mchelio_planes", SCRIPT_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load {SCRIPT_PATH}")

module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

_original_insert_or_replace = module.insert_or_replace


def insert_or_replace_no_health(text, key, value, after=None):
    if str(key).lower() == "maxhp":
        return text
    return _original_insert_or_replace(text, key, value, after)


module.insert_or_replace = insert_or_replace_no_health

if __name__ == "__main__":
    raise SystemExit(module.main())
