from typing import Optional

from countryinfo.countryinfo_facade import CountryInfoFacade


class CountryInfo(CountryInfoFacade):
    """To access one of the country properties available"""

    def __init__(self, country_name: Optional[str] = None):
        super().__init__(country_name)
