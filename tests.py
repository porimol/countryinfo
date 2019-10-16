import unittest
from countryinfo import CountryInfo

class Tests(unittest.TestCase):

    def test_all_countries_have_names(self):
        allCountries = CountryInfo().all()

if __name__ == '__main__':
    unittest.main()
