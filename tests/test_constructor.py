# coding=utf-8
"""Multi-strategy constructor lookup tests (#15, #36, #54)."""
import pytest
from countryinfo import CountryInfo


@pytest.mark.parametrize("identifier,expected", [
    ("Singapore",                    "Singapore"),  # exact name
    ("singapore",                    "Singapore"),  # lowercase
    ("SINGAPORE",                    "Singapore"),  # uppercase
    ("SG",                           "Singapore"),  # alpha-2
    ("SGP",                          "Singapore"),  # alpha-3
    ("702",                          "Singapore"),  # numeric string
    (702,                            "Singapore"),  # numeric int
    ("Republic of Singapore",        "Singapore"),  # altSpelling
    ("Singapura",                    "Singapore"),  # native name
    ("PK",                           "Pakistan"),   # alpha-2
    ("GBR",                          "United Kingdom"),  # alpha-3 (not Wales)
    ("276",                          "Germany"),    # numeric
    ("Czechia",                      "Czech Republic"),  # altSpelling
    ("Holland",                      "Netherlands"),     # altSpelling
])
def test_lookup(identifier, expected):
    assert CountryInfo(identifier).name() == expected
