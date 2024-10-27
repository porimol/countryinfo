import pytest
import json
from countryinfo.dataloader import DataLoader


@pytest.fixture
def tmp_json_files(tmpdir):
    """Creates temporary JSON files for testing DataLoader"""
    valid_data_1 = {
        "name": "Testland",
        "region": "Testregion"
    }
    valid_data_2 = {
        "name": "Examplestan",
        "region": "Exregion"
    }
    invalid_data = "{bad json}"

    # Create temporary JSON files
    valid_file_1 = tmpdir.join("testland.json")
    valid_file_2 = tmpdir.join("examplestan.json")
    invalid_file = tmpdir.join("invalid.json")

    valid_file_1.write(json.dumps(valid_data_1))
    valid_file_2.write(json.dumps(valid_data_2))
    invalid_file.write(invalid_data)

    # Return the path to the temporary directory
    return tmpdir


def test_load_country_data_valid(tmp_json_files):
    """Test loading valid JSON files"""
    data_loader = DataLoader(str(tmp_json_files))
    country_data = data_loader.load_country_data()
    
    assert "testland" in country_data
    assert "examplestan" in country_data
    assert country_data["testland"]["region"] == "Testregion"
    assert country_data["examplestan"]["region"] == "Exregion"


def test_load_country_data_invalid(tmp_json_files, capsys):
    """Test handling of invalid JSON files"""
    data_loader = DataLoader(str(tmp_json_files))
    country_data = data_loader.load_country_data()
    
    # Capture printed output
    captured = capsys.readouterr()
    
    # Ensure invalid file was skipped and error message was printed
    assert "Skipping invalid JSON in file:" in captured.out
    # Ensure only valid files are loaded
    assert len(country_data) == 2
    assert "testland" in country_data
    assert "examplestan" in country_data


def test_load_country_data_no_name_key(tmpdir):
    """Test handling of JSON files without a "name" key"""
    no_name_data = {
        "region": "Testregion"
    }

    # Create temporary JSON file without a "name" key
    no_name_file = tmpdir.join("no_name.json")
    no_name_file.write(json.dumps(no_name_data))

    data_loader = DataLoader(str(tmpdir))
    country_data = data_loader.load_country_data()
    
    # Ensure no data is loaded as the "name" key is missing
    assert len(country_data) == 0


def test_load_country_data_empty_directory(tmpdir):
    """Test with an empty directory"""
    data_loader = DataLoader(str(tmpdir))
    country_data = data_loader.load_country_data()
    
    # Ensure no data is loaded from an empty directory
    assert len(country_data) == 0
