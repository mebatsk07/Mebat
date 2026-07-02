import pandas as pd

from database.db import get_session
from database.models import BTCCandle


def load_btc_dataframe():

    db = get_session()

    candles = (
        db.query(BTCCandle)
        .order_by(BTCCandle.timestamp)
        .all()
    )

    data = []

    for c in candles:

        data.append({
            "time": c.timestamp,
            "open": c.open,
            "high": c.high,
            "low": c.low,
            "close": c.close,
            "volume": c.volume,
        })

    return pd.DataFrame(data)