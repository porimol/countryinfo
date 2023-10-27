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

    def test_all_countries_have_latlng(self):
        for latlng in self.all_countries:
            try:
                country = self.all_countries[latlng]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(latlng, err))

    def test_all_countries_have_area(self):
        for area in self.all_countries:
            try:
                country = self.all_countries[area]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(area, err))

    def test_all_countries_have_callingCodes(self):
        for callingCodes in self.all_countries:
            try:
                country = self.all_countries[callingCodes]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(callingCodes, err))

    def test_all_countries_have_capital(self):
        for capital in self.all_countries:
            try:
                country = self.all_countries[capital]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(capital, err))

    def test_all_countries_have_capital_latlng(self):
        for capital_latlng in self.all_countries:
            try:
                country = self.all_countries[capital_latlng]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(capital_latlng, err))

    def test_all_countries_have_currencies(self):
        for currencies in self.all_countries:
            try:
                country = self.all_countries[currencies]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(currencies, err))

    def test_all_countries_have_demonym(self):
        for demonym in self.all_countries:
            try:
                country = self.all_countries[demonym]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(demonym, err))

    def test_all_countries_have_population(self):
        for population in self.all_countries:
            try:
                country = self.all_countries[population]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(population, err))

    def test_all_countries_have_provinces(self):
        for provinces in self.all_countries:
            try:
                country = self.all_countries[provinces]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(provinces, err))

    def test_all_countries_have_region(self):
        for region in self.all_countries:
            try:
                country = self.all_countries[region]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(region, err))

    def test_all_countries_have_subregion(self):
        for subregion in self.all_countries:
            try:
                country = self.all_countries[subregion]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(subregion, err))

    def test_all_countries_have_timezones(self):
        for timezones in self.all_countries:
            try:
                country = self.all_countries[timezones]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(timezones, err))

    def test_all_countries_have_tld(self):
        for tld in self.all_countries:
            try:
                country = self.all_countries[tld]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(tld, err))

    def test_all_countries_have_wiki(self):
        for wiki in self.all_countries:
            try:
                country = self.all_countries[wiki]
                country.iso()
            except KeyError as err:
                self.fail("Country '{0}' key error: {1}".format(wiki, err))


    def test_select_country_from_alt_name(self):
        country = CountryInfo('PK')
        assert country.name() == 'pakistan'


if __name__ == '__main__':
    unittest.main()
