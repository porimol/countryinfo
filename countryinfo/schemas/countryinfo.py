from typing import Any, Dict, Sequence, TypedDict


class IsoDict(TypedDict):
    """ISO country codes

    Args:
        TypedDict (_type_): _description_
    """
    alpha2: str
    alpha3: str


class CountryInfoDict(TypedDict):
    """Country information

    Args:
        TypedDict (_type_): _description_
    """
    ISO: IsoDict
    altSpellings: Sequence[str]
    area: int
    borders: Sequence[str]
    callingCodes: Sequence[str]
    capital: str
    capital_latlng: Sequence[float]
    currencies: Sequence[str]
    demonym: str
    flag: str
    geoJSON: Dict[str, Any]
    languages: Sequence[str]
    latlng: Sequence[float]
    name: str
    nativeName: str
    population: int
    provinces: Sequence[str]
    region: str
    subregion: str
    timezones: Sequence[str]
    tld: Sequence[str]
    translations: Dict[str, str]
    wiki: str
