# coding=utf-8
"""Verify every country exposes all required fields without raising."""
import pytest


METHODS = [
    "name", "native_name", "iso", "alt_spellings", "translations",
    "latlng", "area", "calling_codes", "capital", "capital_latlng",
    "currencies", "demonym", "population", "provinces",
    "region", "subregion", "timezones", "tld", "wiki",
]


@pytest.mark.parametrize("method", METHODS)
def test_all_countries_have_field(countries, method):
    errors = []
    for c in countries:
        try:
            getattr(c, method)()
        except Exception as exc:
            errors.append(f"{c._data()['name']}: {exc}")
    assert not errors, "\n".join(errors)
