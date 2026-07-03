from datetime import datetime, timezone

from database.models import MarketSnapshot


def build_market_snapshot(
    spot,
    trend,
    regime,
    volatility,
    iv_context,
    oi_context,
):

    return MarketSnapshot(

        timestamp=datetime.now(timezone.utc),

        spot_price=spot,

        trend=trend,

        regime=regime,

        atr=volatility["atr"],

        hv=volatility["historical_volatility"],

        atm_iv=iv_context.atm_iv,

        average_iv=iv_context.average_iv,

        pcr_oi=oi_context.pcr_oi,

        pcr_volume=oi_context.pcr_volume,

        put_oi=oi_context.total_put_oi,

        call_oi=oi_context.total_call_oi,

        put_volume=oi_context.total_put_volume,

        call_volume=oi_context.total_call_volume,

        support=oi_context.strongest_support,

        resistance=oi_context.strongest_resistance,

        direction=oi_context.direction,

        confidence=oi_context.confidence,
    )