import pytest
from countryinfo.location import LocationInfo


@pytest.fixture
def location_info(sample_country_data):
    """Fixture to instantiate LocationInfo with sample data"""
    return LocationInfo(sample_country_data)

def test_capital(location_info):
    # Test if capital city is correctly returned
    assert location_info.capital() == "Testville"
    # Test if None is returned for missing capital data
    empty_data = {}
    empty_location_info = LocationInfo(empty_data)
    assert empty_location_info.capital() is None

def test_province(location_info):
    # Test if province is correctly returned
    assert location_info.province() == "Test Province"
    # Test if None is returned for missing province data
    empty_data = {}
    empty_location_info = LocationInfo(empty_data)
    assert empty_location_info.province() is None

def test_capital_latlng(location_info):
    # Test if capital city latitude and longitude are correctly returned
    assert location_info.capital_latlng() == [34.56, 78.90]
    # Test if None is returned for missing capital latitude and longitude data
    empty_data = {}
    empty_location_info = LocationInfo(empty_data)
    assert empty_location_info.capital_latlng() is None

def test_latlng(location_info):
    # Test if country latitude and longitude are correctly returned
    assert location_info.latlng() == [12.34, 56.78]
    # Test if None is returned for missing latitude and longitude data
    empty_data = {}
    empty_location_info = LocationInfo(empty_data)
    assert empty_location_info.latlng() is None

def test_borders(location_info):
    # Test if bordering countries are correctly returned
    assert location_info.borders() == ["Testlandia", "Examplestan"]
    # Test if None is returned for missing borders data
    empty_data = {}
    empty_location_info = LocationInfo(empty_data)
    assert empty_location_info.borders() is None

def test_region(location_info):
    # Test if region is correctly returned
    assert location_info.region() == "Test Region"
    # Test if None is returned for missing region data
    empty_data = {}
    empty_location_info = LocationInfo(empty_data)
    assert empty_location_info.region() is None

def test_subregion(location_info):
    # Test if subregion is correctly returned
    assert location_info.subregion() == "Test Subregion"
    # Test if None is returned for missing subregion data
    empty_data = {}
    empty_location_info = LocationInfo(empty_data)
    assert empty_location_info.subregion() is None
