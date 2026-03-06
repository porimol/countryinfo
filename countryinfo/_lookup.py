"""Multi-strategy country name resolution.

Priority (first match wins):
  1. Exact lowercase name
  2. altSpellings (case-insensitive)
  3. ISO alpha2 (e.g. "SG")
  4. ISO alpha3 (e.g. "SGP")
  5. Numeric ISO (e.g. "702" or 702)
  6. Native name (nativeName, case-insensitive)
  7. Fuzzy match via rapidfuzz (optional; requires countryinfo[fuzzy])

Returns the canonical lowercase country name on success, or raises
CountryNotFoundError.
"""

from __future__ import annotations

from typing import Any

from .exceptions import CountryNotFoundError


def resolve(
    identifier: str | int,
    countries: dict[str, Any],
    iso_index: dict[str, str],
) -> str:
    """Resolve an identifier to a canonical lowercase country name.

    :param identifier: Country name, ISO code, or numeric ISO.
    :param countries: Dict of {lowercase_name: country_dict} from cache.
    :param iso_index: Dict of {ISO_CODE: lowercase_name} from cache.
    :raises CountryNotFoundError: When no match is found.
    :return: Canonical lowercase country name.
    """
    if isinstance(identifier, int):
        identifier = str(identifier)

    raw = identifier.strip()
    lower = raw.lower()
    upper = raw.upper()

    # 1. Exact name match
    if lower in countries:
        return lower

    # 2. ISO alpha2 / alpha3 / numeric (all stored in iso_index by upper key)
    if upper in iso_index:
        return iso_index[upper]

    # 3. altSpellings + nativeName scan
    for name, info in countries.items():
        alt = [s.lower() for s in info.get("altSpellings", [])]
        if lower in alt:
            return str(name)
        native = info.get("nativeName", "")
        if native and native.lower() == lower:
            return str(name)

    # 4. Fuzzy match (optional dep)
    try:
        from rapidfuzz import fuzz, process

        result = process.extractOne(
            lower,
            list(countries.keys()),
            scorer=fuzz.WRatio,
            score_cutoff=80,
        )
        if result:
            return str(result[0])
    except ImportError:
        pass

    raise CountryNotFoundError(raw)
