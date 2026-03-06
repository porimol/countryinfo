# coding=utf-8
"""Regression tests for every fixed open GitHub issue."""
import pytest
from countryinfo import CountryInfo, CountryNotFoundError


# --- #68/#42/#33 — CountryInfo(None) silently returned Eritrea ---

def test_none_raises_value_error():
    with pytest.raises(ValueError):
        CountryInfo(None)

def test_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        CountryInfo("")

def test_whitespace_raises_value_error():
    with pytest.raises(ValueError):
        CountryInfo("   ")


# --- Unknown country ---

def test_unknown_raises_country_not_found():
    with pytest.raises(CountryNotFoundError):
        CountryInfo("XXXNOTACOUNTRY")

def test_country_not_found_is_lookup_error():
    with pytest.raises(LookupError):
        CountryInfo("XXXNOTACOUNTRY")


# --- #78 — translations() return type consistency ---

def test_translations_returns_dict():
    assert isinstance(CountryInfo("Singapore").translations(), dict)

def test_translations_never_returns_list():
    assert not isinstance(CountryInfo("Singapore").translations(), list)


# --- #74 — Myanmar capital had leading whitespace ---

def test_myanmar_capital_stripped():
    capital = CountryInfo("Myanmar").capital()
    assert capital == capital.strip()
    assert capital == "Naypyidaw"


# --- #79 — "The Netherlands" not findable ---

def test_the_netherlands_lookup():
    assert CountryInfo("The Netherlands").name() == "Netherlands"


# --- name() must return proper-cased string, not lowercase ---

def test_name_returns_proper_case():
    assert CountryInfo("singapore").name() == "Singapore"


# --- #26 — data_no_iso/ territories accessible ---

def test_scotland_findable():
    assert CountryInfo("Scotland").name() == "Scotland"

def test_wales_findable():
    assert CountryInfo("Wales").name() == "Wales"
