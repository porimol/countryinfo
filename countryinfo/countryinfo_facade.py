from os.path import dirname, realpath
from typing import Any, Dict, Optional
from countryinfo.dataloader import DataLoader
from countryinfo.general import GeneralInfo
from countryinfo.identity import IdentityInfo
from countryinfo.location import LocationInfo
from countryinfo.digital import DigitalInfo


class CountryInfoFacade:
    """To access one of the country properties available"""

    def __init__(self, country_name: Optional[str] = None):
        file_dir_path = dirname(realpath(__file__)) + "/data/"
        data_loader = DataLoader(file_dir_path)
        self.countries = data_loader.load_country_data()
        self.country_data = self.__get_country_data(country_name)

    def __get_country_data(self, country_name: Optional[str]) -> Dict[str, Any]:
        country_name = country_name.lower() if country_name else ""
        if country_name in self.countries:
            return self.countries[country_name]
        for country_info in self.countries.values():
            if country_name in map(str.lower, country_info.get("altSpellings", [])):
                return country_info
        return {}

    def get_general_info(self) -> GeneralInfo:
        """Get general information about a country.

        Returns:
            GeneralInfo: _description_
        """
        return GeneralInfo(self.country_data)

    def get_identity_info(self) -> IdentityInfo:
        """Get identity information about a country.

        Returns:
            IdentityInfo: _description_
        """
        return IdentityInfo(self.country_data)
    
    def get_location_info(self) -> LocationInfo:
        """Get location information about a country.

        Returns:
            LocationInfo: _description_
        """
        return LocationInfo(self.country_data)
    
    def get_digital_info(self) -> DigitalInfo:
        """Get digital information about a country.

        Returns:
            DigitalInfo: _description_
        """
        return DigitalInfo(self.country_data)
    
