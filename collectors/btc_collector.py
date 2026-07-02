import time

from api.delta_client import DeltaClient


class BTCCollector:

    def __init__(self):
        self.client = DeltaClient()

    def latest_day(self):

        end = int(time.time())

        start = end - 86400

        data = self.client.get_history(
            symbol="BTCUSDT",
            resolution="1m",
            start=start,
            end=end,
        )

        return data