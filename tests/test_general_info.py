import pytest
from countryinfo.general import GeneralInfo


@pytest.fixture
def general_info(sample_country_data) -> GeneralInfo:
    """Returns a GeneralInfo object for testing purposes

    Args:
        sample_country_data (_type_): _description_

    Returns:
        _type_: _description_
    """
    return GeneralInfo(sample_country_data)


def test_name(general_info: general_info) -> None:
    """Test the name method of GeneralInfo

    Args:
        general_info (_type_): _description_
    """
    assert general_info.name() == "Testland"


def test_info(general_info, sample_country_data: dict) -> None:
    """Test the info method of GeneralInfo"""
    expected_info = sample_country_data.copy()
    expected_info["google"] = "https://www.google.com/search?q=Testland"
    assert general_info.info() == expected_info


def test_alt_spellings(general_info):
    """Test the alt_spellings method of GeneralInfo"""
    assert general_info.alt_spellings() == ["Testlandia", "Republic of Testland"]


def test_area(general_info):
    """Test the area method of GeneralInfo"""
    assert general_info.area() == 12345


def test_population(general_info):
    """Test the population method of GeneralInfo"""
    assert general_info.population() == 678910


def test_currencies(general_info):
    """Test the currencies method of GeneralInfo"""
    assert general_info.currencies() == [{"code": "TLC", "name": "Testland Currency", "symbol": "T$"}]


def test_languages(general_info):
    """Test the languages method of GeneralInfo"""
    assert general_info.languages() == [{"iso639_1": "tl", "iso639_2": "tlc", "name": "Testlandic", "nativeName": "Testlandiko"}]


def test_timezones(general_info):
    """Test the timezones method of GeneralInfo"""
    assert general_info.timezones() == ["UTC+01:00"]


def test_wiki(general_info):
    """Test the wiki method of GeneralInfo"""
    assert general_info.wiki() == "https://en.wikipedia.org/wiki/Testland"


def test_google(general_info):
    """Test the google method of GeneralInfo"""
    assert general_info.google() == "https://www.google.com/search?q=Testland"


def test_all(general_info, sample_country_data):
    """Test the all method of GeneralInfo"""
    assert general_info.all() == sample_country_data