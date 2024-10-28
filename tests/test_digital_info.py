import pytest

from countryinfo.digital import DigitalInfo


@pytest.fixture
def digital_info(sample_country_data: dict) -> DigitalInfo:
    """Fixture to instantiate DigitalInfo with sample data"""
    return DigitalInfo(sample_country_data)


def test_calling_codes(digital_info: DigitalInfo) -> None:
    """Test if calling codes are correctly returned

    Args:
        digital_info (_type_): _description_
    """
    assert digital_info.calling_codes() == ["+123", "+456"]


def test_tld(digital_info: DigitalInfo) -> None:
    """Test if top-level domains are correctly returned

    Args:
        digital_info (DigitalInfo): _description_
    """
    assert digital_info.tld() == [".test", ".example"]


def test_geo_json(digital_info: DigitalInfo) -> None:
    """Test if geoJSON data is correctly returned

    Args:
        digital_info (DigitalInfo): _description_
    """
    expected_geo_json = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [102.0, 0.5]},
                "properties": {"prop0": "value0"},
            }
        ],
    }
    assert digital_info.geo_json() == expected_geo_json


@pytest.mark.parametrize("missing_key", ["callingCodes", "tld", "geoJSON"])
def test_missing_key_data(missing_key: str, sample_country_data: dict) -> None:
    """Test a case where sample_country_data can be empty or missing specific keys

    Args:
        missing_key (_type_): _description_
        sample_country_data (_type_): _description_
    """
    # Remove the key to simulate missing data
    sample_country_data.pop(missing_key, None)
    digital_info = DigitalInfo(sample_country_data)

    if missing_key == "callingCodes":
        assert digital_info.calling_codes() is None
    elif missing_key == "tld":
        assert digital_info.tld() is None
    elif missing_key == "geoJSON":
        assert digital_info.geo_json() is None


def test_empty_country_data() -> None:
    """Test empty data for DigitalInfo"""
    empty_data: dict[str, str] = {}
    digital_info = DigitalInfo(empty_data)

    assert digital_info.calling_codes() is None
    assert digital_info.tld() is None
    assert digital_info.geo_json() is None
