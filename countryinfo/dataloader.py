import json
from glob import glob
from os.path import isfile
from typing import Any, Dict


class DataLoader:
    """Class to load country data from JSON files in a directory."""

    def __init__(self, path: str):
        self.path = path

    def load_country_data(self) -> Dict[str, Any]:
        """Load country data from JSON files in a directory.

        Returns:
            Dict[str, Any]: _description_
        """
        countries = {}
        files_path = list(glob(self.path + "/*.json"))
        for file_path in files_path:
            if isfile(file_path):
                with open(file_path, encoding="utf-8") as file:
                    try:
                        country_info = json.load(file)
                    except json.JSONDecodeError:
                        print(f"Skipping invalid JSON in file: {file_path}")
                        continue
                    if country_info.get("name", None):
                        countries[country_info["name"].lower()] = country_info
        return countries
