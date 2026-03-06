class CountryNotFoundError(LookupError):
    """Raised when a country cannot be resolved from the given identifier."""

    def __init__(self, identifier: str) -> None:
        self.identifier = identifier
        super().__init__(
            f"Country not found: {identifier!r}. "
            "Pass a country name, ISO alpha-2/alpha-3/numeric code, or native name. "
            "Install countryinfo[fuzzy] to enable typo-tolerant matching."
        )
