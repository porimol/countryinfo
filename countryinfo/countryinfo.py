# coding=utf-8
import json
from glob import glob
from os.path import dirname, isfile, realpath
from pprint import pprint
from typing import Any, Dict, Literal, Optional, Sequence, TypedDict, Union, overload


class IsoDict(TypedDict):
    alpha2: str
    alpha3: str


class CountryInfoDict(TypedDict):
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


class CountryInfo:
    """To access one of the country properties available

    Example:
        country = CountryInfo('singapore')
        pprint(country.info())
    """

    def __init__(self, country_name: Optional[str] = None) -> None:
        """constructor method

        :param country_name: str
            pass country name
        """
        self.__country_name = country_name.lower() if country_name else ""
        # get the files path
        __file_dir_path = dirname(realpath(__file__))
        __country_files = __file_dir_path + "/data/"
        __files_path = [files for files in glob(__country_files + "*.json")]
        # __files_path = list(glob(__country_files + '*.json'))
        self.__countries = {}
        for file_path in __files_path:
            if isfile(file_path):
                with open(file_path, encoding="utf-8") as file:
                    try:
                        country_info = json.load(file)
                        # Process JSON data here
                    except json.JSONDecodeError:
                        print(f"Skipping invalid JSON in file: {file_path}")
                        continue
                    # country_info = json.load(file)
                    # pprint(country_info)
                    if country_info.get("name", None):
                        self.__countries[country_info["name"].lower()] = country_info
                        # Update country name if it is one of alt spellings.
                        if self.__country_name in map(
                            lambda an: an.lower(), country_info.get("altSpellings", [])
                        ):
                            self.__country_name = country_info["name"].lower()

    def info(self) -> Optional[CountryInfoDict]:
        """Returns all available information for a specified country.

        :return: dict
        """
        if self.__country_name:
            _all = self.__countries[self.__country_name]
            # pprint(_all)
            _all["google"] = (
                "https://www.google.com/search?q="
                + self.__countries[self.__country_name]["name"]
            )

            return _all
        return None

    def provinces(self) -> Optional[Sequence[str]]:
        """return provinces list

        :return: list
        """
        if self.__country_name:
            _provinces = self.__countries[self.__country_name]["provinces"]
            # pprint(_provinces)

            return _provinces
        return None

    @overload
    def iso(self, alpha: Literal[2, 3]) -> str:
        ...

    @overload
    def iso(self, alpha: None = ...) -> IsoDict:
        ...

    def iso(self, alpha: Literal[2, 3, None] = None) -> Union[str, IsoDict, None]:
        """Returns ISO codes for a specified country

        :param alpha: int

        :return: dict or str
            based on param
        """
        if self.__country_name:
            _iso = self.__countries[self.__country_name]["ISO"]
            # pprint(_iso)

            if alpha == 2:
                return _iso.get("alpha2")
            elif alpha == 3:
                return _iso.get("alpha3")

            return _iso
        return None

    def alt_spellings(self) -> Optional[Sequence[str]]:
        """Returns alternate spellings for the name of a specified country

        :return: list
        """
        if self.__country_name:
            try:
                _alt_spellings = self.__countries[self.__country_name]["altSpellings"]
                # pprint(_alt_spellings)

                return _alt_spellings
            except KeyError:
                return []
        return None

    def area(self) -> Optional[int]:
        """Returns area (km²) for a specified country

        :return: int
        """
        if self.__country_name:
            _area = self.__countries[self.__country_name]["area"]
            # pprint(_area)

            return _area
        return None

    def borders(self) -> Optional[Sequence[str]]:
        """Returns bordering countries (ISO3) for a specified country

        :return: list
        """
        if self.__country_name:
            _borders = self.__countries[self.__country_name]["borders"]
            # pprint(_borders)

            return _borders
        return None

    def calling_codes(self) -> Optional[Sequence[str]]:
        """Returns international calling codes for a specified country

        :return: list
        """
        if self.__country_name:
            _calling_codes = self.__countries[self.__country_name]["callingCodes"]
            # pprint(_calling_codes)

            return _calling_codes
        return None

    def capital(self) -> Optional[str]:
        """Returns capital city for a specified country

        :return: str
        """
        if self.__country_name:
            _capital = self.__countries[self.__country_name]["capital"]
            # pprint(_capital)

            return _capital
        return None

    def capital_latlng(self) -> Optional[Sequence[float]]:
        """Returns capital city latitude and longitude for a specified country

        :return: str
        """
        if self.__country_name:
            _capital_latlng = self.__countries[self.__country_name]["capital_latlng"]
            # pprint(_capital)

            return _capital_latlng
        return None

    def currencies(self) -> Optional[Sequence[str]]:
        """Returns official currencies for a specified country

        :return: list
        """
        if self.__country_name:
            _currencies = self.__countries[self.__country_name]["currencies"]
            # pprint(_currencies)

            return _currencies
        return None

    def demonym(self) -> Optional[str]:
        """Returns the demonyms for a specified country

        :return: str
        """
        if self.__country_name:
            _demonym = self.__countries[self.__country_name]["demonym"]
            # pprint(_demonym)

            return _demonym
        return None

    def flag(self) -> Optional[str]:
        """Returns SVG link of the official flag for a specified country

        :return: str
            it will return an URL if available
        """
        if self.__country_name:
            _flag = self.__countries[self.__country_name]["flag"]
            # pprint(_flag)

            return _flag
        return None

    def geo_json(self) -> Optional[Dict[str, Any]]:
        """Returns geoJSON for a specified country

        :return: dict
        """
        if self.__country_name:
            _geo_json = self.__countries[self.__country_name]["geoJSON"]
            # pprint(_geo_json)

            return _geo_json
        return None

    def languages(self) -> Optional[Sequence[str]]:
        """Returns official languages for a specified country

        :return: list
        """
        if self.__country_name:
            _languages = self.__countries[self.__country_name]["languages"]
            # pprint(_languages)

            return _languages
        return None

    def latlng(self) -> Optional[Sequence[float]]:
        """Returns approx latitude and longitude for a specified country

        :return: list
        """
        if self.__country_name:
            _latlng = self.__countries[self.__country_name]["latlng"]
            # pprint(_latlng)

            return _latlng
        return None

    def name(self) -> Optional[str]:
        """Returns the english name of the country as registered in the library

        :return: str
        """
        return self.__country_name

    def native_name(self) -> Optional[str]:
        """Returns the name of the country in its native tongue

        :return: str
        """
        if self.__country_name:
            _native_name = self.__countries[self.__country_name].get("nativeName")
            # pprint(_native_name)

            return _native_name
        return None

    def population(self) -> Optional[int]:
        """Returns approximate population for a specified country

        :return: int
        """
        if self.__country_name:
            _population = self.__countries[self.__country_name]["population"]
            # pprint(_population)

            return _population
        return None

    def region(self) -> Optional[str]:
        """Returns general region for a specified country

        :return: str
        """
        if self.__country_name:
            _region = self.__countries[self.__country_name]["region"]
            # pprint(_region)

            return _region
        return None

    def subregion(self) -> Optional[str]:
        """Returns a more specific region for a specified country

        :return: str
        """
        if self.__country_name:
            _subregion = self.__countries[self.__country_name]["subregion"]
            # pprint(_subregion)

            return _subregion
        return None

    def timezones(self) -> Optional[Sequence[str]]:
        """Returns all timezones for a specified country

        :return: list
        """
        if self.__country_name:
            _timezones = self.__countries[self.__country_name]["timezones"]
            # pprint(_timezones)

            return _timezones
        return None

    def tld(self) -> Optional[Sequence[str]]:
        """Returns official top level domains for a specified country

        :return: list
        """
        if self.__country_name:
            _tld = self.__countries[self.__country_name]["tld"]
            # pprint(_tld)

            return _tld
        return None

    def translations(self) -> Optional[Dict[str, str]]:
        """Returns translations for a specified country name in popular languages

        :return: dict
        """
        if self.__country_name:
            try:
                _translations = self.__countries[self.__country_name]["translations"]
                # pprint(_translations)

                return _translations
            except KeyError:
                return {}
        return None

    def wiki(self) -> Optional[str]:
        """Returns link to wikipedia page for a specified country

        :return: str
            return wiki url if available
        """
        if self.__country_name:
            _wiki = self.__countries[self.__country_name]["wiki"]
            # pprint(_wiki)

            return _wiki
        return None

    def google(self) -> Optional[str]:
        """Returns link to google page for a specified country

        :return: str
            return google url if available
        """
        if self.__country_name:
            _google = (
                "https://www.google.com/search?q="
                + self.__countries[self.__country_name]["name"]
            )
            # pprint(_google)

            return _google
        return None

    def all(self) -> Optional[Dict[str, CountryInfoDict]]:
        """return all of the countries information

        :return: dict
        """
        _all = self.__countries
        for country in _all:
            _all[country]["google"] = (
                "https://www.google.com/search?q=" + self.__countries[country]["name"]
            )

        return _all


if __name__ == "__main__":
    country = CountryInfo("Singapore")
    pprint(country.all())
