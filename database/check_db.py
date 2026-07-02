from database.db import get_session
from database.models import BTCCandle

db = get_session()

count = db.query(BTCCandle).count()

print(f"Total candles in DB: {count}")

latest = (
    db.query(BTCCandle)
      .order_by(BTCCandle.timestamp.desc())
      .first()
)

print(latest.timestamp)
print(latest.close)