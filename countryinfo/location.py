from typing import Optional, Sequence, Dict, Any


class LocationInfo:
    """Location information about a country."""
    def __init__(self, country_data: Dict[str, Any]):
        self.__country_data = country_data

    def capital(self) -> Optional[str]:
        """Returns capital city for a specified country

        Returns:
            Optional[str]: _description_
        """
        return self.__country_data.get("capital")

    def province(self) -> Optional[str]:
        """Returns province for a specified country

        Returns:
            Optional[str]: _description_
        """
        return self.__country_data.get("province")

    def capital_latlng(self) -> Optional[Sequence[float]]:
        """Returns capital city latitude and longitude for a specified country

        Returns:
            Optional[Sequence[float]]: _description_
        """
        return self.__country_data.get("capital_latlng")

    def latlng(self) -> Optional[Sequence[float]]:
        """Returns approx latitude and longitude for a specified country

        Returns:
            Optional[Sequence[float]]: _description_
        """
        return self.__country_data.get("latlng") 

    def borders(self) -> Optional[Sequence[str]]:
        """Returns bordering countries for a specified country

        Returns:
            Optional[Sequence[str]]: _description_
        """
        return self.__country_data.get("borders")

    def region(self) -> Optional[str]:
        """Returns region for a specified country

        Returns:
            Optional[str]: _description_
        """
        return self.__country_data.get("region")

    def subregion(self) -> Optional[str]:
        """Returns subregion for a specified country

        Returns:
            Optional[str]: _description_
        """
        return self.__country_data.get("subregion")
