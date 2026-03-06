"""CLI entry point for countryinfo.

Usage::

    countryinfo Singapore
    countryinfo Singapore --field capital
    countryinfo Singapore --field iso
    countryinfo --filter region=Asia
    countryinfo --filter language=ar
    countryinfo --filter currency=EUR region=Europe
"""

from __future__ import annotations

import argparse
import json
import sys

from .exceptions import CountryNotFoundError


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="countryinfo",
        description="Look up country data from the command line.",
    )
    parser.add_argument(
        "country",
        nargs="?",
        help="Country name, ISO alpha-2/alpha-3, or numeric code.",
    )
    parser.add_argument(
        "--field",
        metavar="FIELD",
        help=(
            "Return a specific field: capital, region, subregion, iso, "
            "languages, currencies, timezones, population, area, borders, "
            "latlng, tld, calling_codes, provinces, translations, wiki, "
            "timezone_names, current_utc_offset, neighbors."
        ),
    )
    parser.add_argument(
        "--filter",
        nargs="+",
        metavar="KEY=VALUE",
        dest="filters",
        help="Filter all countries by field (e.g. region=Asia language=ar).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Output as JSON.",
    )

    args = parser.parse_args()

    if args.filters and not args.country:
        _handle_filter(args)
    elif args.country:
        _handle_country(args)
    else:
        parser.print_help()
        sys.exit(1)


def _handle_country(args: argparse.Namespace) -> None:
    from .countryinfo import CountryInfo

    try:
        country = CountryInfo(args.country)
    except (CountryNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    if args.field:
        method = args.field.replace("-", "_")
        if not hasattr(country, method):
            print(f"Error: unknown field '{args.field}'", file=sys.stderr)
            sys.exit(1)
        result = getattr(country, method)()
    else:
        result = country.info()

    _print(result, args.as_json)


def _handle_filter(args: argparse.Namespace) -> None:
    from ._filters import filter_countries

    kwargs: dict[str, str] = {}
    for item in args.filters:
        if "=" not in item:
            print(f"Error: filter must be KEY=VALUE, got: {item!r}", file=sys.stderr)
            sys.exit(1)
        key, _, value = item.partition("=")
        kwargs[key.strip()] = value.strip()

    results = filter_countries(**kwargs)
    if args.as_json:
        _print([c.info() for c in results], as_json=True)
    else:
        for c in results:
            print(c.name())


def _print(data: object, as_json: bool = False) -> None:
    if as_json:
        print(json.dumps(data, indent=2, default=str))
    elif isinstance(data, dict):
        for key, value in data.items():
            print(f"{key}: {value}")
    elif isinstance(data, list):
        for item in data:
            print(item)
    else:
        print(data)


if __name__ == "__main__":
    main()
