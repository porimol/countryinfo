import pytest
from countryinfo.identity import IdentityInfo


@pytest.fixture
def identity_info(sample_country_data):
    """Fixture to instantiate IdentityInfo with sample data"""
    return IdentityInfo(sample_country_data)

def test_iso(identity_info):
    # Test if ISO code with alpha=2 is correctly returned
    assert identity_info.iso(2) == "TL"
    # Test if ISO code with alpha=3 is correctly returned
    assert identity_info.iso(3) == "TST"
    # Test if all ISO codes are correctly returned
    assert identity_info.iso() == {"alpha2": "TL", "alpha3": "TST"}
    # Test if None is returned for invalid ISO data
    empty_data = {}
    empty_identity_info = IdentityInfo(empty_data)
    assert empty_identity_info.iso() is None

def test_native_name(identity_info):
    # Test if native name is correctly returned
    assert identity_info.native_name() == "Testlandiko"
    # Test if None is returned for missing native name
    empty_data = {}
    empty_identity_info = IdentityInfo(empty_data)
    assert empty_identity_info.native_name() is None

def test_languages(identity_info, sample_country_data):
    # Test if languages are correctly returned
    assert identity_info.languages() == sample_country_data["languages"]
    # Test if None is returned for missing languages
    empty_data = {}
    empty_identity_info = IdentityInfo(empty_data)
    assert empty_identity_info.languages() is None

def test_flag(identity_info):
    # Test if flag is correctly returned
    assert identity_info.flag() == "🏳️"
    # Test if None is returned for missing flag
    empty_data = {}
    empty_identity_info = IdentityInfo(empty_data)
    assert empty_identity_info.flag() is None

def test_demonym(identity_info):
    # Test if demonym is correctly returned
    assert identity_info.demonym() == "Testlander"
    # Test if None is returned for missing demonym
    empty_data = {}
    empty_identity_info = IdentityInfo(empty_data)
    assert empty_identity_info.demonym() is None
