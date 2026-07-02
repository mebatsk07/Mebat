from api.delta_client import DeltaClient


class OptionMarketCollector:

    def __init__(self):
        self.client = DeltaClient()

    def snapshot(self):

        response = self.client.get_tickers(
            [
                "call_options",
                "put_options",
            ]
        )

        return response["result"]