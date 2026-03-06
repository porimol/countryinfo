# coding=utf-8
"""Tests for new v1.0.0 methods: neighbors, timezone DST, numeric ISO, CLI."""
import pytest
from countryinfo import CountryInfo


# --- Numeric ISO (#36) ---

@pytest.mark.parametrize("country,numeric", [
    ("Singapore", "702"),
    ("Germany",   "276"),
    ("France",    "250"),
])
def test_numeric_iso(country, numeric):
    assert CountryInfo(country).iso()["numeric"] == numeric


# --- IANA timezone names ---

def test_timezone_names_returns_list():
    assert isinstance(CountryInfo("Singapore").timezone_names(), list)

def test_singapore_iana_name():
    assert "Asia/Singapore" in CountryInfo("Singapore").timezone_names()

def test_switzerland_iana_name():
    assert "Europe/Zurich" in CountryInfo("Switzerland").timezone_names()


# --- DST-aware current_utc_offset (#7) ---

def test_current_utc_offset_returns_list():
    assert isinstance(CountryInfo("Singapore").current_utc_offset(), list)

def test_singapore_offset_is_plus_eight():
    assert "+08:00" in CountryInfo("Singapore").current_utc_offset()

def test_offset_strings_are_formatted():
    for offset in CountryInfo("United States").current_utc_offset():
        assert offset[0] in ("+", "-")


# --- neighbors() ---

def test_neighbors_returns_country_info_list():
    neighbors = CountryInfo("France").neighbors()
    assert isinstance(neighbors, list)
    assert len(neighbors) > 0
    from countryinfo import CountryInfo as CI
    assert all(isinstance(n, CI) for n in neighbors)

def test_france_neighbors_include_germany():
    names = [n.name() for n in CountryInfo("France").neighbors()]
    assert "Germany" in names

def test_island_has_no_neighbors():
    assert CountryInfo("Singapore").neighbors() == []


# --- info() includes google field ---

def test_info_has_google():
    info = CountryInfo("Singapore").info()
    assert "google" in info
    assert "Singapore" in info["google"]

def test_google_method():
    assert "google.com" in CountryInfo("Singapore").google()
