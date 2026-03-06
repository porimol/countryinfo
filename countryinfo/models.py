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

from typing import Any


class IsoModel(BaseModel):
    alpha2: str | None = None
    alpha3: str | None = None
    numeric: str | None = None


class CountryModel(BaseModel):
    name: str
    native_name: str | None = Field(None, alias="nativeName")
    iso: IsoModel = Field(default_factory=IsoModel, alias="ISO")
    alt_spellings: list[str] = Field(default_factory=list, alias="altSpellings")
    area: int | None = None
    borders: list[str] = Field(default_factory=list)
    calling_codes: list[str] = Field(default_factory=list, alias="callingCodes")
    capital: str | None = None
    capital_latlng: list[float] = Field(default_factory=list)
    currencies: list[str] = Field(default_factory=list)
    demonym: str | None = None
    flag: str | None = None
    geo_json: dict[str, Any] = Field(default_factory=dict, alias="geoJSON")
    languages: list[str] = Field(default_factory=list)
    latlng: list[float] = Field(default_factory=list)
    population: int | None = None
    provinces: list[str] = Field(default_factory=list)
    region: str | None = None
    subregion: str | None = None
    timezones: list[str] = Field(default_factory=list)
    timezone_names: list[str] = Field(default_factory=list, alias="timezoneNames")
    tld: list[str] = Field(default_factory=list)
    translations: dict[str, str] = Field(default_factory=dict)
    wiki: str | None = None
    google: str | None = None

    model_config = {"populate_by_name": True}
