from typing import Any, Dict, Optional, Sequence


class GeneralInfo:
    """General information about a country."""
    def __init__(self, country_data: Dict[str, Any]):
        self.__country_data = country_data
    
    def name(self) -> Optional[str]:
        """Get the name of a country.

        Returns:
            Optional[str]: _description_
        """
        return self.__country_data.get("name")

    def info(self) -> Optional[Dict[str, Any]]:
        """Get general information about a country.

        Returns:
            Optional[Dict[str, Any]]: _description_
        """
        country_info = self.__country_data
        if country_info:
            country_info["google"] = f"https://www.google.com/search?q={country_info['name']}"
        return country_info

    def alt_spellings(self) -> Optional[Sequence[str]]:
        """Get alternative spellings of a country's name.

        Returns:
            Optional[Sequence[str]]: _description_
        """
        return self.__country_data.get("altSpellings")

    def area(self) -> Optional[int]:
        """Returns area (km²) for a specified country

        :return: int
        """
        return self.__country_data.get("area")

    def population(self) -> Optional[int]:
        """Returns approximate population for a specified country

        :return: int
        """
        return self.__country_data.get("population")

    def currencies(self) -> Optional[Sequence[Dict[str, Any]]]:
        """Returns currencies for a specified country

        :return: list
        """
        return self.__country_data.get("currencies")
    
    def languages(self) -> Optional[Sequence[Dict[str, Any]]]:
        """Returns languages for a specified country

        :return: list
        """
        return self.__country_data.get("languages")

    def timezones(self) -> Optional[Sequence[str]]:
        """Returns all timezones for a specified country

        :return: list
        """
        return self.__country_data.get("timezones")
    
    def wiki(self) -> Optional[str]:
        """Returns link to wikipedia page for a specified country

        :return: str
            return wiki url if available
        """
        return self.__country_data.get("wiki")
    
    def google(self) -> Optional[str]:
        """Returns link to google page for a specified country

        :return: str
            return google url if available
        """
        country_name = self.__country_data.get("name")
        if country_name:
            return f"https://www.google.com/search?q={country_name}"
        return None
    
    def all(self) -> Dict[str, Any]:
        """Returns all general information for a specified country

        :return: dict
        """
        return self.__country_data
