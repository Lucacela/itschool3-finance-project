from domain.asset.asset import Asset
import yahooquery


class AssetFactory:
    def make_new(self, ticker: str) -> Asset:
        # TODO error handling&tests
        t = yahooquery.Ticker(ticker)
        profile = t.summary_profile[ticker]
        name = self.__extract_name(profile)
        country = profile["country"]
        sector = profile["sector"]
        return Asset(
            ticker=ticker,
            nr=0,
            name=name,
            country=country,
            sector=sector,
        )

