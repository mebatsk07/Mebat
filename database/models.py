
from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
class Base(DeclarativeBase):
    pass


class BTCCandle(Base):
    __tablename__ = "btc_candles"

    __table_args__ = (
        UniqueConstraint(
            "symbol",
            "timeframe",
            "timestamp",
            name="uq_btc_candle",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    symbol: Mapped[str] = mapped_column(String(20), index=True)

    timeframe: Mapped[str] = mapped_column(String(5))

    timestamp: Mapped[datetime] = mapped_column(DateTime, index=True)

    open: Mapped[float] = mapped_column(Float)
    high: Mapped[float] = mapped_column(Float)
    low: Mapped[float] = mapped_column(Float)
    close: Mapped[float] = mapped_column(Float)
    volume: Mapped[float] = mapped_column(Float)

class OptionSnapshot(Base):
    __tablename__ = "option_snapshots"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    timestamp: Mapped[datetime] = mapped_column(DateTime, index=True)

    product_id: Mapped[int] = mapped_column(Integer, index=True)

    symbol: Mapped[str] = mapped_column(String(50), index=True)

    contract_type: Mapped[str] = mapped_column(String(20))

    strike: Mapped[float] = mapped_column(Float)

    spot_price: Mapped[float] = mapped_column(Float)

    bid: Mapped[float] = mapped_column(Float)

    ask: Mapped[float] = mapped_column(Float)

    mark_price: Mapped[float] = mapped_column(Float)

    mark_iv: Mapped[float] = mapped_column(Float)

    delta: Mapped[float] = mapped_column(Float)

    gamma: Mapped[float] = mapped_column(Float)

    theta: Mapped[float] = mapped_column(Float)

    vega: Mapped[float] = mapped_column(Float)

    volume: Mapped[float] = mapped_column(Float)

    open_interest: Mapped[float] = mapped_column(Float)