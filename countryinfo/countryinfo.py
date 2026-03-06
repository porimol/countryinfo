from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Any, Literal, cast, overload
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from ._cache import load_countries
from ._lookup import resolve
from .exceptions import CountryNotFoundError

# ---------------------------------------------------------------------------
# TypedDicts (kept for backward compat with existing type-annotated consumers)
# ---------------------------------------------------------------------------
try:
    from typing import TypedDict

    class IsoDict(TypedDict):
        alpha2: str
        alpha3: str
        numeric: str | None

    class CountryInfoDict(TypedDict):
        ISO: IsoDict
        altSpellings: list[str]
        area: int
        borders: list[str]
        callingCodes: list[str]
        capital: str
        capital_latlng: list[float]
        currencies: list[str]
        demonym: str
        flag: str
        geoJSON: dict[str, Any]
        languages: list[str]
        latlng: list[float]
        name: str
        nativeName: str
        population: int
        provinces: list[str]
        region: str
        subregion: str
        timezones: list[str]
        timezoneNames: list[str]
        tld: list[str]
        translations: dict[str, str]
        wiki: str

except ImportError:
    pass  # Python <3.8 fallback (shouldn't happen with requires-python >=3.9)


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------


class CountryInfo:
    """Access structured data about a country.

    Example::

        country = CountryInfo("Singapore")
        print(country.capital())   # Singapore
        print(country.iso(2))      # SG

    The constructor accepts:
    - English country name (case-insensitive): ``CountryInfo("singapore")``
    - ISO alpha-2 code: ``CountryInfo("SG")``
    - ISO alpha-3 code: ``CountryInfo("SGP")``
    - Numeric ISO 3166-1: ``CountryInfo("702")`` or ``CountryInfo(702)``
    - Native name: ``CountryInfo("Singapura")``
    - Alternate spelling: ``CountryInfo("Republic of Singapore")``
    - Typo-tolerant (requires ``pip install countryinfo[fuzzy]``)

    Raises:
        ValueError: If no identifier is provided.
        CountryNotFoundError: If the identifier cannot be resolved.
    """

    def __init__(self, country_name: str | int | None = None) -> None:
        if country_name is None or (isinstance(country_name, str) and not country_name.strip()):
            raise ValueError(
                "country_name is required. Pass a country name, ISO alpha-2/alpha-3/numeric code, "
                "or native name. To list all countries use all_countries()."
            )

        cache = load_countries()
        self.__countries: dict[str, Any] = cache["countries"]
        self.__iso_index: dict[str, str] = cache["iso_index"]
        self.__country_key: str = resolve(country_name, self.__countries, self.__iso_index)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _data(self) -> dict[str, Any]:
        return cast(dict[str, Any], self.__countries[self.__country_key])

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def info(self) -> CountryInfoDict:
        """Returns all available information for the country."""
        result: dict[str, Any] = dict(self._data())
        result["google"] = "https://www.google.com/search?q=" + result["name"]
        return cast("CountryInfoDict", result)

    def name(self) -> str:
        """Returns the English country name as registered in the library (proper casing)."""
        return cast(str, self._data()["name"])

    def provinces(self) -> list[str]:
        """Returns provinces/states list."""
        return cast(list[str], self._data().get("provinces", []))

    @overload
    def iso(self, alpha: Literal[2, 3]) -> str: ...
    @overload
    def iso(self, alpha: None = ...) -> IsoDict: ...

    def iso(self, alpha: Literal[2, 3, None] = None) -> str | IsoDict | None:
        """Returns ISO codes for the country.

        :param alpha: 2 for alpha-2, 3 for alpha-3, None for full dict (includes numeric).
        """
        iso_data: dict[str, Any] = self._data().get("ISO", {})
        if alpha == 2:
            return cast(str, iso_data.get("alpha2"))
        if alpha == 3:
            return cast(str, iso_data.get("alpha3"))
        return cast("IsoDict", iso_data)

    def alt_spellings(self) -> list[str]:
        """Returns alternate spellings for the country name."""
        return cast(list[str], self._data().get("altSpellings", []))

    def area(self) -> int | None:
        """Returns area in km²."""
        return cast("int | None", self._data().get("area"))

    def borders(self) -> list[str]:
        """Returns bordering countries as ISO alpha-3 codes."""
        return cast(list[str], self._data().get("borders", []))

    def calling_codes(self) -> list[str]:
        """Returns international calling codes."""
        return cast(list[str], self._data().get("callingCodes", []))

    def capital(self) -> str | None:
        """Returns the capital city name."""
        return cast("str | None", self._data().get("capital"))

    def capital_latlng(self) -> list[float]:
        """Returns capital city [latitude, longitude]."""
        return cast(list[float], self._data().get("capital_latlng", []))

    def currencies(self) -> list[str]:
        """Returns official currency codes (ISO 4217)."""
        return cast(list[str], self._data().get("currencies", []))

    def demonym(self) -> str | None:
        """Returns the demonym (e.g. 'Singaporean')."""
        return cast("str | None", self._data().get("demonym"))

    def flag(self) -> str | None:
        """Returns SVG flag URL (if available)."""
        return cast("str | None", self._data().get("flag"))

    def geo_json(self) -> dict[str, Any]:
        """Returns GeoJSON data."""
        return cast(dict[str, Any], self._data().get("geoJSON", {}))

    def languages(self) -> list[str]:
        """Returns official language codes (ISO 639-1)."""
        return cast(list[str], self._data().get("languages", []))

    def latlng(self) -> list[float]:
        """Returns country centre [latitude, longitude]."""
        return cast(list[float], self._data().get("latlng", []))

    def native_name(self) -> str | None:
        """Returns the country name in its native language."""
        return cast("str | None", self._data().get("nativeName"))

    def population(self) -> int | None:
        """Returns approximate population."""
        return cast("int | None", self._data().get("population"))

    def region(self) -> str | None:
        """Returns the general region (e.g. 'Asia')."""
        return cast("str | None", self._data().get("region"))

    def subregion(self) -> str | None:
        """Returns the specific subregion (e.g. 'South-eastern Asia')."""
        return cast("str | None", self._data().get("subregion"))

    def timezones(self) -> list[str]:
        """Returns UTC offset strings (e.g. ['UTC+08:00'])."""
        return cast(list[str], self._data().get("timezones", []))

    def timezone_names(self) -> list[str]:
        """Returns IANA timezone names (e.g. ['Asia/Singapore'])."""
        return cast(list[str], self._data().get("timezoneNames", []))

    def current_utc_offset(self) -> list[str]:
        """Returns current UTC offset(s) accounting for DST.

        Uses IANA timezone names from the data. Falls back to the static
        ``timezones`` field when IANA names are not available.

        :return: List of offset strings like ['+08:00', '+11:00'].
        """
        iana_names = self.timezone_names()
        if not iana_names:
            return [tz.replace("UTC", "") for tz in self.timezones()]

        now = datetime.now(tz=UTC)
        offsets: list[str] = []
        seen: set[str] = set()
        for name in iana_names:
            try:
                tz = ZoneInfo(name)
                raw_offset: timedelta | None = now.astimezone(tz).utcoffset()
                if raw_offset is None:
                    continue
                total_seconds = int(raw_offset.total_seconds())
                sign = "+" if total_seconds >= 0 else "-"
                total_seconds = abs(total_seconds)
                hours, remainder = divmod(total_seconds, 3600)
                minutes = remainder // 60
                label = f"{sign}{hours:02d}:{minutes:02d}"
                if label not in seen:
                    seen.add(label)
                    offsets.append(label)
            except (ZoneInfoNotFoundError, Exception):
                continue
        return offsets or [tz.replace("UTC", "") for tz in self.timezones()]

    def tld(self) -> list[str]:
        """Returns top-level domain(s) (e.g. ['.sg'])."""
        return cast(list[str], self._data().get("tld", []))

    def translations(self) -> dict[str, str]:
        """Returns country name translations in popular languages."""
        return cast(dict[str, str], self._data().get("translations", {}))

    def wiki(self) -> str | None:
        """Returns Wikipedia URL."""
        return cast("str | None", self._data().get("wiki"))

    def google(self) -> str:
        """Returns Google search URL for the country."""
        return "https://www.google.com/search?q=" + cast(str, self._data()["name"])

    def neighbors(self) -> list[CountryInfo]:
        """Returns bordering countries as CountryInfo objects.

        Resolves ISO alpha-3 border codes to full CountryInfo instances.
        Countries whose ISO code cannot be resolved are silently skipped.
        """
        result = []
        for iso3 in self.borders():
            try:
                result.append(CountryInfo(iso3))
            except (CountryNotFoundError, ValueError):
                continue
        return result

    def model(self) -> Any:
        """Returns a Pydantic model for this country.

        Requires ``pip install countryinfo[pydantic]``.

        :raises ImportError: If pydantic is not installed.
        """
        try:
            from .models import CountryModel
        except ImportError as exc:
            raise ImportError(
                "Pydantic is required for .model(). "
                "Install it with: pip install countryinfo[pydantic]"
            ) from exc
        return CountryModel.model_validate(self.info())

    # ------------------------------------------------------------------
    # Class-level helpers
    # ------------------------------------------------------------------

    @classmethod
    def all(cls) -> dict[str, CountryInfoDict]:
        """Returns raw data for all countries as a dict keyed by lowercase name.

        For a list of CountryInfo objects use ``all_countries()`` instead.
        """
        cache = load_countries()
        result: dict[str, Any] = {}
        for name, data in cache["countries"].items():
            entry = dict(data)
            entry["google"] = "https://www.google.com/search?q=" + data["name"]
            result[name] = entry
        return cast(dict[str, "CountryInfoDict"], result)


if __name__ == "__main__":
    from pprint import pprint

    country = CountryInfo("Singapore")
    pprint(country.info())
