
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

class MarketSnapshot(Base):
    __tablename__ = "market_snapshots"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    timestamp: Mapped[datetime] = mapped_column(DateTime, index=True)

    spot_price: Mapped[float] = mapped_column(Float)

    trend: Mapped[str] = mapped_column(String(30))
    regime: Mapped[str] = mapped_column(String(30))

    atr: Mapped[float] = mapped_column(Float)
    hv: Mapped[float] = mapped_column(Float)

    atm_iv: Mapped[float] = mapped_column(Float)
    average_iv: Mapped[float] = mapped_column(Float)

    pcr_oi: Mapped[float] = mapped_column(Float)
    pcr_volume: Mapped[float] = mapped_column(Float)

    put_oi: Mapped[float] = mapped_column(Float)
    call_oi: Mapped[float] = mapped_column(Float)

    put_volume: Mapped[float] = mapped_column(Float)
    call_volume: Mapped[float] = mapped_column(Float)

    support: Mapped[float] = mapped_column(Float)
    resistance: Mapped[float] = mapped_column(Float)

    direction: Mapped[str] = mapped_column(String(30))

    confidence: Mapped[float] = mapped_column(Float)    

class PaperTrade(Base):
    __tablename__ = "paper_trades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    symbol: Mapped[str] = mapped_column(String(50), index=True)

    strike: Mapped[float] = mapped_column(Float)

    option_type: Mapped[str] = mapped_column(String(20))

    expiry: Mapped[str] = mapped_column(String(30))

    quantity: Mapped[int] = mapped_column(Integer)

    entry_time: Mapped[datetime] = mapped_column(DateTime)

    exit_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    entry_price: Mapped[float] = mapped_column(Float)

    exit_price: Mapped[float | None] = mapped_column(Float, nullable=True)

    pnl: Mapped[float] = mapped_column(Float, default=0)

    theta: Mapped[float] = mapped_column(Float, default=0)

    iv_entry: Mapped[float] = mapped_column(Float)

    iv_exit: Mapped[float | None] = mapped_column(Float, nullable=True)

    rv: Mapped[float] = mapped_column(Float)

    pcr: Mapped[float] = mapped_column(Float)

    regime: Mapped[str] = mapped_column(String(30))

    trend: Mapped[str] = mapped_column(String(30))

    health_entry: Mapped[float] = mapped_column(Float)

    health_exit: Mapped[float | None] = mapped_column(Float, nullable=True)

    exit_reason: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )
class DecisionLog(Base):

    __tablename__ = "decision_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    timestamp: Mapped[datetime] = mapped_column(DateTime)

    symbol: Mapped[str] = mapped_column(String(50))

    premium: Mapped[float] = mapped_column(Float)

    delta: Mapped[float] = mapped_column(Float)

    score: Mapped[float] = mapped_column(Float)

    trend: Mapped[str] = mapped_column(String(30))

    regime: Mapped[str] = mapped_column(String(30))

    decision: Mapped[str] = mapped_column(String(20))

    reason: Mapped[str] = mapped_column(String(200))
        
class DecisionLog(Base):

    __tablename__ = "decision_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    timestamp: Mapped[datetime] = mapped_column(DateTime)

    symbol: Mapped[str] = mapped_column(String(50))

    premium: Mapped[float] = mapped_column(Float)

    delta: Mapped[float] = mapped_column(Float)

    score: Mapped[float] = mapped_column(Float)

    trend: Mapped[str] = mapped_column(String(30))

    regime: Mapped[str] = mapped_column(String(30))

    decision: Mapped[str] = mapped_column(String(20))

    reason: Mapped[str] = mapped_column(String(200))    