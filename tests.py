import unittest
from countryinfo import CountryInfo

class Tests(unittest.TestCase):

    all_countries = {}

    def setUp(self):
        """Loads all the countries just once for all the tests
        """
        if not self.all_countries:
            print("Loading all countries...")
            country_names = CountryInfo().all()
            for name in country_names:
                country = CountryInfo(name)
                self.all_countries[name] = country

    def test_all_countries_have_name(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                self.assertIsNotNone(country.name())
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(name, err))

    def test_all_countries_have_native_name(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.native_name()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(name, err))

    def test_all_countries_have_iso(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(name, err))

    def test_all_countries_have_alt_spellings(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.alt_spellings()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(name, err))

    def test_all_countries_have_translations(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.translations()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(name, err))

if __name__ == '__main__':
    unittest.main()
