# Country Info
A python module for returning data about countries, ISO info and states/provinces within them.

## Table of Contents

* [Install](#install)
* [API Usage](#api-usage)

## APIs
* [.info()](#info)
* [.provinces()](#provinces)
* [.alt_spellings()](#alt_spellings)
* [.area()](#area)
* [.borders()](#borders)
* [.calling_codes()](#calling_codes)
* [.capital()](#capital)
* [.capital_latlng()](#capital_latlng)
* [.currencies()](#currencies)
* [.demonym()](#demonym)
* [.geojson()`](#geo_json)
* [.iso()](#iso)
* [.languages()](#languages)
* [.latlng()](#latlng)
* [.native_name()](#native_name)
* [.population()](#population)
* [.region()](#region)
* [.subregion()](#subregion)
* [.timezones()](#timezones)
* [.tld()](#tld)
* [.translations()](#translations)
* [.wiki()](#wiki)
* [.all()](#all)


## Acknowledgement
* [Special Thanks](#special-thanks)
* [Contributing](#contributing)
* [Changelog](#changelog)
* [Disclaimer](#disclaimer)
* [License (MIT)](#license)

## Install

```python
pip install countryinfo
```

OR, git clone

```python
git clone https://github.com/porimol/countryinfo.git

cd countryinfo
python setup.py install
```

## API Usage
To access one of the country properties available, you'll need to use one of the API methods listed below and pass a country in either way.

### .info()

Returns all available information for a specified country.

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.info()
# returns object,
{
    'ISO': {
        'alpha2': 'SG',
        'alpha3': 'SGP'
    },
    'altSpellings': [
        'SG',
        'Singapura',
        'Republik Singapura',
        '新加坡共和国'
    ],
    'area': 710,
    'borders': [],
    'callingCodes': ['65'],
    'capital': 'Singapore',
    'capital_latlng': [
        1.357107,
        103.819499
    ],
    'currencies': ['SGD'],
    'demonym': 'Singaporean',
    'flag': '',
    'geoJSON': {},
    'languages': [
        'en',
        'ms',
        'ta',
        'zh'
    ],
    'latlng': [
        1.36666666,
        103.8
    ],
    'name': 'Singapore',
    'nativeName': 'Singapore',
    'population': 5469700,
    'provinces': ['Singapore'],
    'region': 'Asia',
    'subregion': 'South-Eastern Asia',
    'timezones': ['UTC+08:00'],
    'tld': ['.sg'],
    'translations': {
        'de': 'Singapur',
        'es': 'Singapur',
        'fr': 'Singapour',
        'it': 'Singapore',
        'ja': 'シンガポール'
    },
    'wiki': 'http://en.wikipedia.org/wiki/singapore'
}

# Similar can also be achieved via country code or any
# alternate name of a country. For example, Singapur
# would be:
country = CountryInfo('SG')
```

### .provinces()
Return provinces list

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.provinces()
# returns object,
['Singapore']
```

### .alt_spellings()

Returns alternate spellings for the name of a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.alt_spellings()
# returns list of strings, alternate names
# ['SG', 'Singapura', 'Republik Singapura', '新加坡共和国']
```

### .area()

Returns area (km²) for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.area()
# returns number of square kilometer area
710
```

### .borders()

Returns bordering countries (ISO3) for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.borders()
# returns array of strings, ISO3 codes of countries that border the given country
[]
```

### .calling_codes()

Returns international calling codes for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.calling_codes()
# returns array of calling code strings
['65']
```

### .capital()

Returns capital city for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.capital()
# returns string
'Singapore'
```

### .capital_latlng()

Returns capital city latitude and longitude for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.capital_latlng()
# returns array, approx latitude and longitude for country capital
[1.357107, 103.819499]
```

### .currencies()

Returns official currencies for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.currencies()
# returns array of strings, currencies
# ['SGD']
```

### .demonym()

Returns the [demonyms](http://en.wikipedia.org/wiki/Demonym) for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.demonym()
# returns string, name of residents
'Singaporean'
```

### .geo_json()

Returns [geoJSON](http://en.wikipedia.org/wiki/GeoJSON) for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Bangladesh')
country.geo_json()
# returns object of GeoJSON data

{
    'features': [
        {
            'geometry': {
                'coordinates': [[[92.672721, 22.041239],
                                             [92.652257, 21.324048],
                                             [92.303234, 21.475485],
                                             [92.368554, 20.670883],
                                             [92.082886, 21.192195],
                                             [92.025215, 21.70157],
                                             [91.834891, 22.182936],
                                             [91.417087, 22.765019],
                                             [90.496006, 22.805017],
                                             [90.586957, 22.392794],
                                             [90.272971, 21.836368],
                                             [89.847467, 22.039146],
                                             [89.70205, 21.857116],
                                             [89.418863, 21.966179],
                                             [89.031961, 22.055708],
                                             [88.876312, 22.879146],
                                             [88.52977, 23.631142],
                                             [88.69994, 24.233715],
                                             [88.084422, 24.501657],
                                             [88.306373, 24.866079],
                                             [88.931554, 25.238692],
                                             [88.209789, 25.768066],
                                             [88.563049, 26.446526],
                                             [89.355094, 26.014407],
                                             [89.832481, 25.965082],
                                             [89.920693, 25.26975],
                                             [90.872211, 25.132601],
                                             [91.799596, 25.147432],
                                             [92.376202, 24.976693],
                                             [91.915093, 24.130414],
                                             [91.46773, 24.072639],
                                             [91.158963, 23.503527],
                                             [91.706475, 22.985264],
                                             [91.869928, 23.624346],
                                             [92.146035, 23.627499],
                                             [92.672721, 22.041239]]],
                            'type': 'Polygon'
                },
               'id': 'BGD',
               'properties': {'name': 'Bangladesh'},
               'type': 'Feature'}],
    'type': 'FeatureCollection'
}

```

### .iso()

Returns ISO codes for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.iso()
# returns object of ISO codes
{'alpha2': 'SG', 'alpha3': 'SGP'}

country.iso(2)
# returns object of ISO codes
'SG'


country.iso(3)
# returns object of ISO codes
'SGP'
```

### .languages()

Returns official languages for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.languages()
# returns array of language codes
['en', 'ms', 'ta', 'zh']
```

### .latlng()

Returns approx latitude and longitude for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.latlng()
# returns array, approx latitude and longitude for country
[1.36666666, 103.8]
```

### .native_name()

Returns the name of the country in its native tongue

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.native_name()
# returns string, name of country in native language
'Singapore'
```

### .population()

Returns approximate population for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.population()
# returns number, approx population
5469700
```

### .region()

Returns general region for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.region()
# returns string
'Asia'
```

### .subregion()

Returns a more specific region for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.subregion()
# returns string
'South-Eastern Asia'
```

### .timezones()

Returns all timezones for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.timezones()
# returns array of timezones
['UTC+08:00']
```

### .tld()

Returns official [top level domains](http://en.wikipedia.org/wiki/Top-level_domain) for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.tld()
# returns array of top level domains specific to the country
['.sg']
```

### .translations()

Returns translations for a specified country name in popular languages

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.translations()
# returns object of translations of country name in major languages
{
    'de': 'Singapur',
    'es': 'Singapur',
    'fr': 'Singapour',
    'it': 'Singapore',
    'ja': 'シンガポール'
}
```

### .wiki()

Returns link to wikipedia page for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.wiki()
# returns string URL of wikipedia article on country
'http://en.wikipedia.org/wiki/singapore'
```

### .all()

Returns array of objects containing all available data for all countries. This will be super big. Not recommended.

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo()
country.all()
# returns array of objects,
{
    'zimbabwe': {'ISO': {'alpha2': 'ZW', 'alpha3': 'ZWE'},
              'altSpellings': ['ZW', 'Republic of Zimbabwe'],
              'area': 390757,
              'borders': ['BWA', 'MOZ', 'ZAF', 'ZMB'],
              'callingCodes': ['263'],
              'capital': 'Harare',
              'capital_latlng': [-17.831773, 31.045686],
              'currencies': ['USD'],
              'demonym': 'Zimbabwean',
              'flag': '',
              'geoJSON': {'features': [{'geometry': {'coordinates': [[[31.191409,
                                                                       -22.25151],
                                                                      [30.659865,
                                                                       -22.151567],
                                                                      [30.322883,
                                                                       -22.271612],
                                                                      [29.839037,
                                                                       -22.102216],
                                                                      [29.432188,
                                                                       -22.091313],
                                                                      [28.794656,
                                                                       -21.639454],
                                                                      [28.02137,
                                                                       -21.485975],
                                                                      [27.727228,
                                                                       -20.851802],
                                                                      [27.724747,
                                                                       -20.499059],
                                                                      [27.296505,
                                                                       -20.39152],
                                                                      [26.164791,
                                                                       -19.293086],
                                                                      [25.850391,
                                                                       -18.714413],
                                                                      [25.649163,
                                                                       -18.536026],
                                                                      [25.264226,
                                                                       -17.73654],
                                                                      [26.381935,
                                                                       -17.846042],
                                                                      [26.706773,
                                                                       -17.961229],
                                                                      [27.044427,
                                                                       -17.938026],
                                                                      [27.598243,
                                                                       -17.290831],
                                                                      [28.467906,
                                                                       -16.4684],
                                                                      [28.825869,
                                                                       -16.389749],
                                                                      [28.947463,
                                                                       -16.043051],
                                                                      [29.516834,
                                                                       -15.644678],
                                                                      [30.274256,
                                                                       -15.507787],
                                                                      [30.338955,
                                                                       -15.880839],
                                                                      [31.173064,
                                                                       -15.860944],
                                                                      [31.636498,
                                                                       -16.07199],
                                                                      [31.852041,
                                                                       -16.319417],
                                                                      [32.328239,
                                                                       -16.392074],
                                                                      [32.847639,
                                                                       -16.713398],
                                                                      [32.849861,
                                                                       -17.979057],
                                                                      [32.654886,
                                                                       -18.67209],
                                                                      [32.611994,
                                                                       -19.419383],
                                                                      [32.772708,
                                                                       -19.715592],
                                                                      [32.659743,
                                                                       -20.30429],
                                                                      [32.508693,
                                                                       -20.395292],
                                                                      [32.244988,
                                                                       -21.116489],
                                                                      [31.191409,
                                                                       -22.25151]]],
                                                     'type': 'Polygon'},
                                        'id': 'ZWE',
                                        'properties': {'name': 'Zimbabwe'},
                                        'type': 'Feature'}],
                          'type': 'FeatureCollection'},
              'languages': ['en', 'sn', 'nd'],
              'latlng': [-20, 30],
              'name': 'Zimbabwe',
              'nativeName': 'Zimbabwe',
              'population': 13061239,
              'provinces': ['Bulawayo',
                            'Harare',
                            'ManicalandMashonaland Central',
                            'Mashonaland East',
                            'Mashonaland'],
              'region': 'Africa',
              'subregion': 'Eastern Africa',
              'timezones': ['UTC+02:00'],
              'tld': ['.zw'],
              'translations': {'de': 'Simbabwe',
                               'es': 'Zimbabue',
                               'fr': 'Zimbabwe',
                               'it': 'Zimbabwe',
                               'ja': 'ジンバブエ'},
              'wiki': 'http://en.wikipedia.org/wiki/zimbabwe'}
}
```

## Special Thanks

Special thanks to johan for his work on [johan/world.geo.json](https://github.com/johan/world.geo.json), who made the geojson portion of this build possible.


## Inspired By
Repo: [countryjs](https://github.com/therebelrobot/countryjs)

Maintainer: [Oz Haven](https://github.com/therebelrobot)


## Contributing
See the list of [contributors](https://github.com/porimol/countryinfo/contributors) who participated in this project.


### How to become a contributor

If you want to contribute to `countryinfo` and make it better, your help is very welcome.
You can make constructive, helpful bug reports, feature requests and the noblest of all contributions.
If like to contribute in a good way, then follow the following guidelines.

#### How to make a clean pull request

* Create a personal fork on Github.
* Clone the fork on your local machine.(Your remote repo on Github is called `origin`.)
* Add the original repository as a remote called `upstream`.
* If you created your fork a while ago be sure to pull upstream changes into your local repository.
* Create a new branch to work on! Branch from `dev`.
* Implement/fix your feature, comment your code.
* Follow `countryinfo`'s code style, including indentation(4 spaces).
* Write or adapt tests as needed.
* Add or change the documentation as needed.
* Push your branch to your fork on Github, the remote `origin`.
* From your fork open a pull request to the `dev` branch.
* Once the pull request is approved and merged, please pull the changes from `upstream` to your local repo and delete your extra branch(es).


## Disclaimer

This is being maintained in the contributor's free time, and as such, may contain minor errors in regards to some countries.
Most of the information included in this library is what is listed on Wikipedia. If there is an error,
please let me know and I will do my best to correct it.

## License

### [The MIT License](LICENSE.txt)

Copyright (c) 2018, Porimol Chandro <porimolchandroroy@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
