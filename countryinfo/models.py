# coding=utf-8
"""Optional Pydantic v2 models for countryinfo.

Requires ``pip install countryinfo[pydantic]``.

Usage::

    from countryinfo import CountryInfo
    country = CountryInfo("Singapore")
    model = country.model()
    print(model.capital)   # Singapore
    print(model.iso.alpha2)  # SG
"""
from __future__ import annotations

try:
    from pydantic import BaseModel, Field
except ImportError as _err:
    raise ImportError(
        "Pydantic is required for countryinfo models. "
        "Install it with: pip install countryinfo[pydantic]"
    ) from _err

from typing import Any, Dict, List, Optional


class IsoModel(BaseModel):
    alpha2: Optional[str] = None
    alpha3: Optional[str] = None
    numeric: Optional[str] = None


class CountryModel(BaseModel):
    name: str
    native_name: Optional[str] = Field(None, alias="nativeName")
    iso: IsoModel = Field(default_factory=IsoModel, alias="ISO")
    alt_spellings: List[str] = Field(default_factory=list, alias="altSpellings")
    area: Optional[int] = None
    borders: List[str] = Field(default_factory=list)
    calling_codes: List[str] = Field(default_factory=list, alias="callingCodes")
    capital: Optional[str] = None
    capital_latlng: List[float] = Field(default_factory=list)
    currencies: List[str] = Field(default_factory=list)
    demonym: Optional[str] = None
    flag: Optional[str] = None
    geo_json: Dict[str, Any] = Field(default_factory=dict, alias="geoJSON")
    languages: List[str] = Field(default_factory=list)
    latlng: List[float] = Field(default_factory=list)
    population: Optional[int] = None
    provinces: List[str] = Field(default_factory=list)
    region: Optional[str] = None
    subregion: Optional[str] = None
    timezones: List[str] = Field(default_factory=list)
    timezone_names: List[str] = Field(default_factory=list, alias="timezoneNames")
    tld: List[str] = Field(default_factory=list)
    translations: Dict[str, str] = Field(default_factory=dict)
    wiki: Optional[str] = None
    google: Optional[str] = None

    model_config = {"populate_by_name": True}
