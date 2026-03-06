# coding=utf-8
import pytest
from countryinfo import all_countries


@pytest.fixture(scope="session")
def countries():
    """Load all CountryInfo objects once for the entire test session."""
    return all_countries()
