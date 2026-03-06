# Countryinfo

A lightweight Python library for accessing comprehensive country data — including ISO codes, states/provinces, capital cities, currencies, languages, and other geographic information.

<div align="center">

<a href="https://pypi.org/project/countryinfo/">
  <img src="https://img.shields.io/pypi/v/countryinfo?style=for-the-badge&logo=pypi&logoColor=white&color=blue" alt="PyPI Version" height="30">
</a>
&nbsp;
<a href="https://pypi.org/project/countryinfo/">
  <img src="https://img.shields.io/pypi/pyversions/countryinfo?style=for-the-badge&logo=python&logoColor=white" alt="Python Versions" height="30">
</a>
&nbsp;
<a href="LICENSE">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License: MIT" height="30">
</a>

<h3>☕ Support This Project</h3>

<p>
This project is developed and maintained during the author's free time.
If you find it useful and would like to support its continued development,
consider buying a coffee or sponsoring the project. Every bit of support
helps keep the project maintained and improving ❤️
</p>

<a href="https://pepy.tech/projects/countryinfo">
  <img src="https://static.pepy.tech/badge/countryinfo/week?style=for-the-badge&color=darkgreen" alt="Weekly Downloads" height="30">
</a>
&nbsp;
<a href="https://pepy.tech/projects/countryinfo">
  <img src="https://static.pepy.tech/badge/countryinfo/month?style=for-the-badge&color=green" alt="Monthly Downloads" height="30">
</a>
&nbsp;
<a href="https://pepy.tech/projects/countryinfo">
  <img src="https://static.pepy.tech/badge/countryinfo?style=for-the-badge&color=brightgreen" alt="Total Downloads" height="30">
</a>

<br>

<a href="https://buymeacoffee.com/porimolchad">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="45">
</a>
&nbsp;&nbsp;
<a href="https://github.com/sponsors/porimol">
  <img src="https://img.shields.io/badge/GitHub%20Sponsors-%E2%9D%A4%EF%B8%8F%20Sponsor-ea4aaa?style=for-the-badge&logo=github-sponsors&logoColor=white" alt="GitHub Sponsors" height="45">
</a>
</div>

---

## Table of Contents

- [Countryinfo](#countryinfo)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Quick Start](#quick-start)
  - [Constructor](#constructor)
  - [API Reference](#api-reference)
    - [Country lookup](#country-lookup)
    - [.info()](#info)
    - [.name()](#name)
    - [.iso()](#iso)
    - [.alt\_spellings()](#alt_spellings)
    - [.area()](#area)
    - [.borders()](#borders)
    - [.neighbors()](#neighbors)
    - [.calling\_codes()](#calling_codes)
    - [.capital()](#capital)
    - [.capital\_latlng()](#capital_latlng)
    - [.currencies()](#currencies)
    - [.demonym()](#demonym)
    - [.geo\_json()](#geo_json)
    - [.languages()](#languages)
    - [.latlng()](#latlng)
    - [.native\_name()](#native_name)
    - [.population()](#population)
    - [.provinces()](#provinces)
    - [.region()](#region)
    - [.subregion()](#subregion)
    - [.timezones()](#timezones)
    - [.timezone\_names()](#timezone_names)
    - [.current\_utc\_offset()](#current_utc_offset)
    - [.tld()](#tld)
    - [.translations()](#translations)
    - [.wiki()](#wiki)
    - [.google()](#google)
  - [Filter \& Reverse Queries](#filter--reverse-queries)
    - [all\_countries()](#all_countries)
    - [filter\_countries()](#filter_countries)
    - [CountryInfo.all()](#countryinfoall)
  - [Optional Extras](#optional-extras)
    - [Fuzzy / typo-tolerant lookup](#fuzzy--typo-tolerant-lookup)
    - [Pydantic models](#pydantic-models)
  - [CLI](#cli)
  - [Errors](#errors)
  - [Contributing](#contributing)
    - [How to contribute](#how-to-contribute)
  - [Special Thanks](#special-thanks)
  - [Disclaimer](#disclaimer)
  - [License](#license)

---

## Install

```bash
pip install countryinfo
```

With optional extras:

```bash
pip install "countryinfo[fuzzy]"    # typo-tolerant country lookup
pip install "countryinfo[pydantic]" # Pydantic v2 typed models
pip install "countryinfo[all]"      # everything above
```

Using Poetry:

```bash
poetry add countryinfo
poetry add "countryinfo[fuzzy,pydantic]"
```

Install from source:

```bash
git clone https://github.com/porimol/countryinfo.git
cd countryinfo
poetry install
```

---

## Quick Start

```python
from countryinfo import CountryInfo

country = CountryInfo("Singapore")
print(country.capital())      # Singapore
print(country.iso(2))         # SG
print(country.population())   # 5469700
print(country.neighbors())    # [] — island, no land borders
```

---

## Constructor

`CountryInfo` accepts any of the following identifiers (case-insensitive):

```python
CountryInfo("Singapore")              # English name
CountryInfo("singapore")              # lowercase — OK
CountryInfo("SG")                     # ISO alpha-2
CountryInfo("SGP")                    # ISO alpha-3
CountryInfo("702")                    # ISO numeric (string or int)
CountryInfo(702)                      # ISO numeric (int)
CountryInfo("Singapura")              # native / alternate name
CountryInfo("Republic of Singapore")  # full official name
```

Raises `ValueError` if no identifier is supplied.
Raises `CountryNotFoundError` (a `LookupError`) if the identifier cannot be resolved.

---

## API Reference

To access country details, first create a `CountryInfo` instance using a country name or code. Then, use the methods listed below to retrieve specific properties.

### Country lookup

```python
from countryinfo import CountryInfo

sg = CountryInfo("SG")   # ISO alpha-2
de = CountryInfo("DEU")  # ISO alpha-3
fr = CountryInfo(250)    # ISO numeric
```

---

### .info()

Returns all available data for the country.

```python
CountryInfo("Singapore").info()
# {
#   'name': 'Singapore',
#   'ISO': {'alpha2': 'SG', 'alpha3': 'SGP', 'numeric': '702'},
#   'altSpellings': ['SG', 'Singapura', 'Republic of Singapore', ...],
#   'area': 710,
#   'borders': [],
#   'callingCodes': ['65'],
#   'capital': 'Singapore',
#   'capital_latlng': [1.357107, 103.819499],
#   'currencies': ['SGD'],
#   'demonym': 'Singaporean',
#   'languages': ['en', 'ms', 'ta', 'zh'],
#   'latlng': [1.36666666, 103.8],
#   'nativeName': 'Singapore',
#   'population': 5469700,
#   'provinces': ['Singapore'],
#   'region': 'Asia',
#   'subregion': 'South-eastern Asia',
#   'timezones': ['UTC+08:00'],
#   'timezoneNames': ['Asia/Singapore'],
#   'tld': ['.sg'],
#   'translations': {'de': 'Singapur', 'es': 'Singapur', ...},
#   'wiki': 'http://en.wikipedia.org/wiki/singapore',
#   'google': 'https://www.google.com/search?q=Singapore',
# }

# Similar can also be achieved via country code or any
# alternate name of a country. For example, Singapur
# would be:
country = CountryInfo('SG')
country.info()
```

---

### .name()

Returns the English country name (proper casing).

```python
CountryInfo("SG").name()   # 'Singapore'
CountryInfo("SGP").name()  # 'Singapore'
```

---

### .iso()

Returns ISO 3166-1 codes. Now includes numeric code.

```python
country = CountryInfo("Singapore")
country.iso()   # {'alpha2': 'SG', 'alpha3': 'SGP', 'numeric': '702'}
country.iso(2)  # 'SG'
country.iso(3)  # 'SGP'
```

---

### .alt_spellings()

Returns alternate spellings for the name of a specified country

```python
CountryInfo("Singapore").alt_spellings()
# ['SG', 'Singapura', 'Republic of Singapore', ...]
```

---

### .area()

Returns area (km²) for a specified country

```python
CountryInfo("Singapore").area()  # 710

# or
country = CountryInfo("Singapore")
country.area()  # 710
```

---

### .borders()

Bordering countries as ISO alpha-3 codes.

```python
CountryInfo("Germany").borders()
# ['AUT', 'BEL', 'CHE', 'CZE', 'DNK', 'FRA', 'LUX', 'NLD', 'POL']

# or
country = CountryInfo("Singapore")
country.borders()
```

---

### .neighbors()

Bordering countries as `CountryInfo` objects. New in v1.0.0.

```python
for neighbor in CountryInfo("France").neighbors():
    print(neighbor.name(), neighbor.capital())
# Germany  Berlin
# Belgium  Brussels
# ...
```

---

### .calling_codes()

Returns international calling codes for a specified country

```python
CountryInfo("Singapore").calling_codes()  # ['65']

# or
country = CountryInfo("Singapore")
country.calling_codes()  # ['65']
```

---

### .capital()

Returns capital city for a specified country

```python
CountryInfo("Singapore").capital()  # 'Singapore'

# or
country = CountryInfo("Singapore")
country.capital()  # 'Singapore'
```

---

### .capital_latlng()

Returns capital city latitude and longitude for a specified country

```python
CountryInfo("Singapore").capital_latlng()  # [1.357107, 103.819499]

# or
country = CountryInfo("Singapore")
country.capital_latlng()  # [1.357107, 103.819499]
```

---

### .currencies()

```python
CountryInfo("Singapore").currencies()  # ['SGD']

# or
country = CountryInfo("Singapore")
country.currencies()  # ['SGD']
```

---

### .demonym()

```python
CountryInfo("Singapore").demonym()  # 'Singaporean'

# or
country = CountryInfo("Singapore")
country.demonym()  # 'Singaporean'
```

---

### .geo_json()

Returns GeoJSON `FeatureCollection` for the country boundary.

```python
CountryInfo("Bangladesh").geo_json()
# {'type': 'FeatureCollection', 'features': [...]}

# or
country = CountryInfo("Singapore")
country.geo_json()
# {'type': 'FeatureCollection', 'features': [...]}
```

---

### .languages()

ISO 639-1 language codes.

```python
CountryInfo("Singapore").languages()  # ['en', 'ms', 'ta', 'zh']

# or
country = CountryInfo("Singapore")
country.languages()  # ['en', 'ms', 'ta', 'zh']
```

---

### .latlng()

Approximate country centre coordinates.

```python
CountryInfo("Singapore").latlng()  # [1.36666666, 103.8]

# or
country = CountryInfo("Singapore")
country.latlng()
```

---

### .native_name()

Returns the name of the country in its native tongue

```python
CountryInfo("Germany").native_name()  # 'Deutschland'

# or
country = CountryInfo("Germany")
country.native_name()  # 'Deutschland'
```

---

### .population()

```python
CountryInfo("Singapore").population()  # 5469700

# or
country = CountryInfo("Singapore")
country.population()  # 5469700
```

---

### .provinces()

Return provinces list

```python
CountryInfo("Singapore").provinces()  # ['Singapore']

# or
country = CountryInfo("Singapore")
country.provinces()  # ['Singapore']
```

---

### .region()

```python
CountryInfo("Singapore").region()  # 'Asia'

# or
country = CountryInfo("Singapore")
country.region()  # 'Asia'
```

---

### .subregion()

```python
CountryInfo("Singapore").subregion()  # 'South-eastern Asia'

# or
country = CountryInfo("Singapore")
country.subregion()  # 'South-eastern Asia'
```

---

### .timezones()

Static UTC offset strings.

```python
CountryInfo("Singapore").timezones()    # ['UTC+08:00']
CountryInfo("Switzerland").timezones()  # ['UTC+01:00', 'UTC+02:00']

# or
country = CountryInfo("Singapore")
country.timezones()    # ['UTC+08:00']
```

---

### .timezone_names()

IANA timezone names. New in v1.0.0.

```python
CountryInfo("Singapore").timezone_names()   # ['Asia/Singapore']
CountryInfo("United States").timezone_names()
# ['America/New_York', 'America/Chicago', 'America/Denver', ...]

# or
country = CountryInfo("Singapore")
country.timezone_names()  # ['Asia/Singapore']
```

---

### .current_utc_offset()

DST-aware current UTC offset(s). Uses `zoneinfo` (stdlib). New in v1.0.0.

```python
CountryInfo("Singapore").current_utc_offset()    # ['+08:00']
CountryInfo("Switzerland").current_utc_offset()  # ['+01:00'] or ['+02:00'] depending on season
CountryInfo("United States").current_utc_offset()
# ['-05:00', '-06:00', '-07:00', '-08:00', '-09:00', '-10:00']

# or
country = CountryInfo("Singapore")
country.current_utc_offset()  # ['+08:00']
```

---

### .tld()

```python
CountryInfo("Singapore").tld()  # ['.sg']

# or
country = CountryInfo("Singapore")
country.tld()  # ['.sg']
```

---

### .translations()

Country name in major languages.

```python
CountryInfo("Singapore").translations()
# {'de': 'Singapur', 'es': 'Singapur', 'fr': 'Singapour', 'it': 'Singapore', 'ja': 'シンガポール'}

# or
country = CountryInfo("Singapore")
country.translations()
```

---

### .wiki()

```python
CountryInfo("Singapore").wiki()
# 'http://en.wikipedia.org/wiki/singapore'

# or
country = CountryInfo("Singapore")
country.wiki()
```

---

### .google()

```python
CountryInfo("Singapore").google()
# 'https://www.google.com/search?q=Singapore'

# or
country = CountryInfo("Singapore")
country.google()
```

---

## Filter & Reverse Queries

### all_countries()

Returns every country as a list of `CountryInfo` objects. New in v1.0.0.

```python
from countryinfo import all_countries

countries = all_countries()
capitals = [c.capital() for c in countries]
```

---

### filter_countries()

Filter all countries by field. New in v1.0.0.

```python
from countryinfo import filter_countries

# All countries in Asia
asia = filter_countries(region="Asia")

# All Arabic-speaking countries
arabic = filter_countries(language="ar")

# Eurozone countries
eurozone = filter_countries(currency="EUR")

# Countries that border France
near_france = filter_countries(border="FRA")

# Combine filters (AND logic)
result = filter_countries(region="Europe", currency="EUR")
for c in result:
    print(c.name(), c.capital())
```

Supported keyword arguments: `region`, `subregion`, `language`, `currency`, `border`, `calling_code`, `tld`.

---

### CountryInfo.all()

Returns raw data for all countries as a `dict` (backward-compatible classmethod).

```python
from countryinfo import CountryInfo

data = CountryInfo.all()  # {lowercase_name: {...}, ...}
```

---

## Optional Extras

### Fuzzy / typo-tolerant lookup

```bash
pip install "countryinfo[fuzzy]"
```

Once installed, the constructor automatically falls back to fuzzy matching when an exact match fails:

```python
CountryInfo("Singaproe").name()  # 'Singapore'  (typo corrected)
CountryInfo("Germny").name()     # 'Germany'
```

---

### Pydantic models

```bash
pip install "countryinfo[pydantic]"
```

```python
country = CountryInfo("Singapore")
model = country.model()

print(model.name)          # Singapore
print(model.iso.alpha2)    # SG
print(model.iso.numeric)   # 702
print(model.capital)       # Singapore
print(model.population)    # 5469700
```

---

## CLI

A command-line tool is included.

```bash
# Full country info
countryinfo Singapore

# Specific field
countryinfo Singapore --field capital
countryinfo SG --field iso
countryinfo 702 --field current_utc_offset

# Filter
countryinfo --filter region=Asia
countryinfo --filter currency=EUR
countryinfo --filter region=Europe currency=EUR

# JSON output
countryinfo Singapore --json
countryinfo --filter language=ar --json
```

---

## Errors

```python
from countryinfo import CountryInfo, CountryNotFoundError

try:
    country = CountryInfo("Xanadu")
except CountryNotFoundError as e:
    print(e)  # Country not found: 'Xanadu'. Pass a country name, ISO ...

# CountryNotFoundError is a LookupError
try:
    CountryInfo(None)
except ValueError:
    pass  # None or empty string raises ValueError
```

---

## Contributing

Contributions are welcome — bug reports, data corrections, and pull requests.

See the list of [contributors](https://github.com/porimol/countryinfo/contributors) who have participated in this project.

### How to contribute

1. Fork the repository on GitHub.
2. Clone your fork locally.
3. Create a new branch from `main`.
4. Make your changes and add/update tests in `tests/`.
5. Run the test suite: `poetry run pytest tests/ -v`
6. Open a pull request against `main`.

> **Data corrections:** Each country is a single JSON file in `countryinfo/data/`. Edit the relevant file and open a PR — no Python changes needed for data-only fixes.

---

## Special Thanks

Special thanks to [johan](https://github.com/johan) for [world.geo.json](https://github.com/johan/world.geo.json), which made the GeoJSON data possible.

Inspired by [countryjs](https://github.com/therebelrobot/countryjs) by [Oz Haven](https://github.com/therebelrobot).

---

## Disclaimer

This library is maintained in the contributor's free time. Data is sourced primarily from Wikipedia. If you find an error, please [open an issue](https://github.com/porimol/countryinfo/issues).

---

## License

[MIT License](LICENSE) — Copyright (c) 2018, Porimol Chandro
