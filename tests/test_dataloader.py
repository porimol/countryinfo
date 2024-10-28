import json

import pytest
from py.path import local

from countryinfo.dataloader import DataLoader


@pytest.fixture
def tmp_json_files(tmpdir: local) -> local:
    """Creates temporary JSON files for testing DataLoader"""
    valid_data_1 = {"name": "Testland", "region": "Testregion"}
    valid_data_2 = {"name": "Examplestan", "region": "Exregion"}
    invalid_data = "{bad json}"

    # Create temporary JSON files
    json_file_dir = tmpdir.mkdir("sub")
    valid_file_1 = json_file_dir.join("no_ntestlandame.json")
    valid_file_2 = json_file_dir.join("examplestan.json")
    invalid_file = json_file_dir.join("invalid.json")
    # valid_file_1 = json_file_dir / "testland.json"
    # valid_file_2 = json_file_dir / "examplestan.json"
    # invalid_file = json_file_dir / "invalid.json"
    valid_file_1.write(json.dumps(valid_data_1))
    valid_file_2.write(json.dumps(valid_data_2))
    invalid_file.write(json.dumps(invalid_data))

    # Return the path to the temporary directory
    return tmpdir


def test_load_country_data_valid(tmp_json_files: pytest.TempPathFactory) -> None:
    """Test loading valid JSON files

    Args:
        tmp_json_files (pytest.TempPathFactory): _description_
    """
    # TODO: Implement test
    # data_loader = DataLoader(str(tmp_json_files))
    # country_data = data_loader.load_country_data()

    # assert "Testland" in country_data
    # assert "Examplestan" in country_data
    # assert country_data["testland"]["region"] == "Testregion"
    # assert country_data["examplestan"]["region"] == "Exregion"
    pass


def test_load_country_data_invalid(
    tmp_json_files: pytest.TempPathFactory, capsys: pytest.CaptureFixture
) -> None:
    """Test handling of invalid JSON files

    Args:
        tmp_json_files (pytest.TempPathFactory): _description_
        capsys (pytest.CaptureFixture): _description_
    """
    # TODO: Implement test
    # data_loader = DataLoader(str(tmp_json_files))
    # country_data = data_loader.load_country_data()

    # # Capture printed output
    # captured = capsys.readouterr()

    # # Ensure invalid file was skipped and error message was printed
    # assert "Skipping invalid JSON in file:" in captured.out
    # # Ensure only valid files are loaded
    # assert len(country_data) == 2
    # assert "Testland" in country_data
    # assert "Examplestan" in country_data
    pass


def test_load_country_data_no_name_key(tmpdir: local) -> None:
    """Test handling of JSON files without a "name" key

    Args:
        tmpdir (pytest.TempPathFactory): _description_
    """
    no_name_data = {"region": "Testregion"}

    # Create temporary JSON file without a "name" key
    no_name_dir = tmpdir.mkdir("sub")
    no_name_file = no_name_dir.join("no_name.json")
    no_name_file.write(json.dumps(no_name_data))

    data_loader = DataLoader(str(tmpdir))
    country_data = data_loader.load_country_data()

    # Ensure no data is loaded as the "name" key is missing
    assert len(country_data) == 0


def test_load_country_data_empty_directory(tmpdir: pytest.TempPathFactory) -> None:
    """Test with an empty directory

    Args:
        tmpdir (pytest.TempPathFactory): _description_
    """
    data_loader = DataLoader(str(tmpdir))
    country_data = data_loader.load_country_data()

    # Ensure no data is loaded from an empty directory
    assert len(country_data) == 0
