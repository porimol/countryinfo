from typing import Any, Dict, Optional, Sequence


class DigitalInfo:
    """Digital information about a country"""
    def __init__(self, country_data: Dict[str, Any]):
        self.__country_data = country_data

    def calling_codes(self) -> Optional[Sequence[str]]:
        """Returns calling codes for a specified country

        Returns:
            Optional[Sequence[str]]: _description_
        """
        return self.__country_data.get("callingCodes")

    def tld(self) -> Optional[Sequence[str]]:
        """Returns top-level domain for a specified country

        Returns:
            Optional[Sequence[str]]: _description_
        """
        return self.__country_data.get("tld")

    def geo_json(self) -> Optional[Dict[str, Any]]:
        """Returns geoJSON for a specified country

        Returns:
            Optional[Dict[str, Any]]: _description_
        """
        return self.__country_data.get("geoJSON")
