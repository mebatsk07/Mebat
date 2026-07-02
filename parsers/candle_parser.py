from datetime import datetime

from database.models import BTCCandle


def parse_candles(api_result):

    candles = []

    for candle in api_result:

        candles.append(
            BTCCandle(
                symbol="BTCUSDT",
                timeframe="1m",
                timestamp=datetime.fromtimestamp(candle["time"]),
                open=candle["open"],
                high=candle["high"],
                low=candle["low"],
                close=candle["close"],
                volume=candle["volume"],
            )
        )

    return candles