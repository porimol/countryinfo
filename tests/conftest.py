import pytest

@pytest.fixture
def sample_country_data():
    data ={
        "name": "Testland",
        "altSpellings": ["Testlandia", "Republic of Testland"],
        "area": 12345,
        "population": 678910,
        "currencies": [{"code": "TLC", "name": "Testland Currency", "symbol": "T$"}],
        "languages": [{"iso639_1": "tl", "iso639_2": "tlc", "name": "Testlandic", "nativeName": "Testlandiko"}],
        "timezones": ["UTC+01:00"],
        "wiki": "https://en.wikipedia.org/wiki/Testland",
        "callingCodes": ["+123", "+456"],
        "tld": [".test", ".example"],
        "geoJSON": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [102.0, 0.5]
                    },
                    "properties": {
                        "prop0": "value0"
                    }
                }
            ]
        },
        "ISO": {
            "alpha2": "TL",
            "alpha3": "TST"
        },
        "nativeName": "Testlandiko",
        "flag": "🏳️",
        "demonym": "Testlander",
        "capital": "Testville",
        "province": "Test Province",
        "capital_latlng": [34.56, 78.90],
        "latlng": [12.34, 56.78],
        "borders": ["Testlandia", "Examplestan"],
        "region": "Test Region",
        "subregion": "Test Subregion"
    }
    return data