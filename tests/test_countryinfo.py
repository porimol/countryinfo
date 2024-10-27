import unittest
from countryinfo import CountryInfo


class Tests(unittest.TestCase):

    all_countries = {}

    def setUp(self):
        self.verificationErrors = [] #Variable used to collect non-fatal errors

        """Loads all the countries just once for all the tests
        """
        if not self.all_countries:
            print("Loading all countries...")
            country_names = CountryInfo().all()
            for name in country_names:
                country = CountryInfo(name)
                self.all_countries[name] = country

    def tearDown(self):
        """Loads and prints all exceptions encountered while running tests
        """
        self.assertEqual([], self.verificationErrors)

    def test_all_countries_have_name(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                self.assertIsNotNone(country.name())
            except KeyError as err:
                self.verificationErrors.append("name: "+ str(name))

    def test_all_countries_have_native_name(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.native_name()
            except KeyError as err:
                self.verificationErrors.append("native_name: "+ str(name))

    def test_all_countries_have_iso(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.iso()
            except KeyError as err:
                self.verificationErrors.append("iso: "+ str(name))

    def test_all_countries_have_alt_spellings(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.alt_spellings()
            except KeyError as err:
                self.verificationErrors.append("alt_spellings: "+ str(name))

    def test_all_countries_have_translations(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.translations()
            except KeyError as err:
                self.verificationErrors.append("translations: "+ str(name))

    def test_all_countries_have_latlng(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.latlng()
            except KeyError as err:
                self.verificationErrors.append("latlng: "+ str(name))

    def test_all_countries_have_area(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.area()
            except KeyError as err:
                self.verificationErrors.append("area: "+ str(name))

    def test_all_countries_have_callingCodes(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.calling_codes()
            except KeyError as err:
                self.verificationErrors.append("callingCodes: "+ str(name))

    def test_all_countries_have_capital(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.capital()
            except KeyError as err:
                self.verificationErrors.append("capital: "+ str(name))

    def test_all_countries_have_capital_latlng(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.capital_latlng()
            except KeyError as err:
                self.verificationErrors.append("capital_latlng: "+ str(name))

    def test_all_countries_have_currencies(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.currencies()
            except KeyError as err:
                self.verificationErrors.append("currencies: "+ str(name))

    def test_all_countries_have_demonym(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.demonym()
            except KeyError as err:
                self.verificationErrors.append("demonym: "+ str(name))

    def test_all_countries_have_population(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.population()
            except KeyError as err:
                self.verificationErrors.append("population: "+ str(name))

    def test_all_countries_have_provinces(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.provinces()
            except KeyError as err:
                self.verificationErrors.append("provinces: "+ str(name))

    def test_all_countries_have_region(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.region()
            except KeyError as err:
                self.verificationErrors.append("region: "+ str(name))

    def test_all_countries_have_subregion(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.subregion()
            except KeyError as err:
                self.verificationErrors.append("subregion: "+ str(name))

    def test_all_countries_have_timezones(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.timezones()
            except KeyError as err:
                self.verificationErrors.append("timezones: "+ str(name))

    def test_all_countries_have_tld(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.tld()
            except KeyError as err:
                self.verificationErrors.append("tld "+ str(name))

    def test_all_countries_have_wiki(self):
        for name in self.all_countries:
            try:
                country = self.all_countries[name]
                country.wiki()
            except KeyError as err:
                self.verificationErrors.append("wiki: "+ str(name))

    def test_select_country_from_alt_name(self):
        country = CountryInfo('PK')
        assert country.name() == 'pakistan'


if __name__ == '__main__':
    unittest.main()
