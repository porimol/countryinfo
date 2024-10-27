from typing import Any, Dict, Literal, Optional, Sequence, Union

from countryinfo.schemas.countryinfo import IsoDict


class IdentityInfo:
    """Identity information about a country."""

    def __init__(self, country_data: Dict[str, Any]):
        self.__country_data = country_data

    def iso(self, alpha: Literal[2, 3, None] = None) -> Union[str, IsoDict, None]:
        """Returns ISO codes for a specified country

        Args:
            alpha (Literal[2, 3, None], optional): _description_. Defaults to None.

        Returns:
            Union[str, IsoDict, None]: _description_
        """
        iso_codes = self.__country_data.get("ISO")
        if iso_codes:
            if alpha == 2:
                return iso_codes.get("alpha2")
            if alpha == 3:
                return iso_codes.get("alpha3")
            return iso_codes
        return None

    def native_name(self) -> Optional[str]:
        """Returns native name for a specified country

        Returns:
            Optional[str]: _description_
        """
        return self.__country_data.get("nativeName")

    def languages(self) -> Optional[Sequence[str]]:
        """Returns languages spoken in a specified country

        Returns:
            Optional[Sequence[str]]: _description_
        """
        return self.__country_data.get("languages")

    def flag(self) -> Optional[str]:
        """Returns flag for a specified country

        Returns:
            Optional[str]: _description_
        """
        return self.__country_data.get("flag")

    def demonym(self) -> Optional[str]:
        """Returns demonym for a specified country

        Returns:
            Optional[str]: _description_
        """
        return self.__country_data.get("demonym")
