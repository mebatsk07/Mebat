import requests
from config.settings import settings


class DeltaClient:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.session = requests.Session()

    def get_products(self):
        """Get all trading products."""
        url = f"{self.base_url}/v2/products"

        response = self.session.get(url, timeout=15)
        response.raise_for_status()

        return response.json()

    def ping(self):
        return self.get_products()

    def get_history(self, symbol: str, resolution: str, start: int, end: int):
        """
        Download historical candles.

        resolution:
            "1"   = 1 minute
            "5"   = 5 minutes
            "15"  = 15 minutes
            "60"  = 1 hour
            "1D"  = Daily
        """

        url = f"{self.base_url}/v2/history/candles"

        params = {
            "symbol": symbol,
            "resolution": resolution,
            "start": start,
            "end": end,
        }

        response = self.session.get(
            url,
            params=params,
            timeout=20,
        )

        print("Request URL:", response.url)
        print("Status Code:", response.status_code)
        print("Response Body:")
        print(response.text)

        response.raise_for_status()

        return response.json()

    def get_tickers(self, contract_types=None):
        """
        Get live tickers.

        contract_types examples:
            ["call_options"]
            ["put_options"]
            ["call_options", "put_options"]
            ["perpetual_futures"]
        """

        url = f"{self.base_url}/v2/tickers"

        params = {}

        if contract_types:
            params["contract_types"] = ",".join(contract_types)

        response = self.session.get(
            url,
            params=params,
            timeout=20,
        )

        response.raise_for_status()

        return response.json()