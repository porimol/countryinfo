# coding=utf-8
"""Reverse/filter query function tests."""
import pytest
from countryinfo import CountryInfo, all_countries, filter_countries


def test_all_countries_returns_list(countries):
    assert isinstance(countries, list)
    assert len(countries) > 200

def test_all_countries_are_country_info(countries):
    assert all(isinstance(c, CountryInfo) for c in countries[:10])

def test_all_classmethod_returns_dict():
    result = CountryInfo.all()
    assert isinstance(result, dict)
    assert all(k == k.lower() for k in list(result.keys())[:10])

def test_all_classmethod_includes_google():
    result = CountryInfo.all()
    assert all("google" in v for v in list(result.values())[:5])


@pytest.mark.parametrize("kwargs,min_count,check_attr,check_value", [
    ({"region": "Asia"},         20, "region",    "Asia"),
    ({"region": "Europe"},       20, "region",    "Europe"),
    ({"language": "ar"},         15, None,        None),
    ({"currency": "EUR"},        10, None,        None),
])
def test_filter_by_field(kwargs, min_count, check_attr, check_value):
    results = filter_countries(**kwargs)
    assert len(results) >= min_count
    if check_attr:
        assert all(getattr(c, check_attr)() == check_value for c in results)

def test_filter_currency_eur_includes_expected():
    names = [c.name() for c in filter_countries(currency="EUR")]
    assert "Germany" in names
    assert "France" in names

def test_filter_multiple_criteria():
    results = filter_countries(region="Europe", currency="EUR")
    assert len(results) > 5
    for c in results:
        assert c.region() == "Europe"
        assert "EUR" in c.currencies()

def test_filter_by_border():
    names = [c.name() for c in filter_countries(border="FRA")]
    assert "Germany" in names
    assert "Spain" in names

def test_filter_no_results():
    assert filter_countries(region="XXNOTAREGION") == []
