import functools
import glob
import json
import os
from typing import Any


@functools.cache
def load_countries() -> dict[str, Any]:
    """Load all country JSON files once; result is cached for the process lifetime.

    Builds two indexes:
      - by lowercase name  →  raw dict
      - by ISO alpha2/alpha3/numeric  →  lowercase name (for fast ISO lookup)
    """
    base = os.path.dirname(__file__)
    data_dirs = [
        os.path.join(base, "data"),
        os.path.join(base, "data_no_iso"),
    ]
    countries: dict[str, Any] = {}  # key: lowercase name, value: raw dict
    iso_index: dict[str, str] = {}  # key: ISO code (upper), value: lowercase name

    # data/ is authoritative; data_no_iso/ entries must not overwrite ISO codes
    # that already belong to a sovereign country.
    for pass_no, data_dir in enumerate(data_dirs):
        for path in sorted(glob.glob(os.path.join(data_dir, "*.json"))):
            with open(path, encoding="utf-8") as f:
                try:
                    info = json.load(f)
                except json.JSONDecodeError:
                    continue
            if not info.get("name"):
                continue
            key = info["name"].lower()
            countries[key] = info

            iso = info.get("ISO", {})
            for code_field in ("alpha2", "alpha3", "numeric"):
                code = iso.get(code_field)
                if not code:
                    continue
                code_key = str(code).upper()
                # Only add to the index if not already claimed by a data/ country
                if code_key not in iso_index or pass_no == 0:
                    iso_index[code_key] = key

    return {"countries": countries, "iso_index": iso_index}
