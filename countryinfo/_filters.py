"""Module-level filter and query functions.

These are exported from the package root so users can write::

    from countryinfo import all_countries, filter_countries
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ._cache import load_countries

if TYPE_CHECKING:
    from .countryinfo import CountryInfo


def all_countries() -> list[CountryInfo]:
    """Return all countries as a list of CountryInfo objects.

    Example::

        countries = all_countries()
        capitals = [c.capital() for c in countries]
    """
    from .countryinfo import CountryInfo  # local import avoids circular dep

    cache = load_countries()
    return [CountryInfo(data["name"]) for data in cache["countries"].values()]


def filter_countries(**kwargs: str) -> list[CountryInfo]:
    """Return countries matching all supplied field criteria.

    Supported keyword arguments:

    - ``region`` — e.g. ``"Asia"``, ``"Europe"``
    - ``subregion`` — e.g. ``"South-eastern Asia"``
    - ``language`` — ISO 639-1 code, e.g. ``"ar"`` (checks languages list)
    - ``currency`` — ISO 4217 code, e.g. ``"EUR"`` (checks currencies list)
    - ``border`` — ISO alpha-3 code, e.g. ``"FRA"`` (countries that border it)
    - ``calling_code`` — e.g. ``"65"``
    - ``tld`` — e.g. ``".sg"``

    Multiple kwargs are ANDed together.

    Example::

        # All Arabic-speaking countries in Asia
        results = filter_countries(language="ar", region="Asia")

        # All countries using the Euro
        results = filter_countries(currency="EUR")
    """
    from .countryinfo import CountryInfo  # local import avoids circular dep

    cache = load_countries()
    results = []

    normalised: dict[str, str] = dict(kwargs)

    for data in cache["countries"].values():
        if _matches(data, normalised):
            results.append(CountryInfo(data["name"]))

    return results


# ---------------------------------------------------------------------------
# Internal matching helpers
# ---------------------------------------------------------------------------

_LIST_FIELDS: dict[str, str] = {
    "language": "languages",
    "currency": "currencies",
    "border": "borders",
    "calling_code": "callingCodes",
    "tld": "tld",
}

_SCALAR_FIELDS: dict[str, str] = {
    "region": "region",
    "subregion": "subregion",
}


def _matches(data: dict[str, Any], criteria: dict[str, str]) -> bool:
    for key, value in criteria.items():
        if key in _SCALAR_FIELDS:
            field = _SCALAR_FIELDS[key]
            if (data.get(field) or "").lower() != value.lower():
                return False
        elif key in _LIST_FIELDS:
            field = _LIST_FIELDS[key]
            items = [str(i).lower() for i in data.get(field, [])]
            if value.lower() not in items:
                return False
        # Unknown keys are silently ignored so callers can be forward-compatible
    return True
