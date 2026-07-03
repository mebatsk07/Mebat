from dataclasses import dataclass, field
from collections import defaultdict
from typing import List


# =====================================================
# OI CONTEXT (V2)
# =====================================================

@dataclass
class OIContext:

    total_put_oi: float
    total_call_oi: float

    total_put_volume: float
    total_call_volume: float

    pcr_oi: float
    pcr_volume: float

    atm_put_oi: float
    atm_call_oi: float

    atm_put_volume: float
    atm_call_volume: float

    put_wall: float
    call_wall: float

    strongest_support: float
    strongest_resistance: float

    bullish_score: float
    bearish_score: float

    confidence: float

    direction: str

    dealer_bias: str

    gamma_wall: float

    max_pain: float

    explanation: List[str] = field(default_factory=list)


# =====================================================
# OI ENGINE V2
# =====================================================

class OIEngine:

    ATM_PERCENT = 0.02

    STRONG_LEVEL = 80

    NORMAL_LEVEL = 60

    def analyze(self, tickers, spot):

        put_oi = 0.0
        call_oi = 0.0

        put_volume = 0.0
        call_volume = 0.0

        atm_put_oi = 0.0
        atm_call_oi = 0.0

        atm_put_volume = 0.0
        atm_call_volume = 0.0

        put_by_strike = defaultdict(float)
        call_by_strike = defaultdict(float)

        all_strikes = defaultdict(float)

        explanation = []

        lower = spot * (1 - self.ATM_PERCENT)
        upper = spot * (1 + self.ATM_PERCENT)

        # -------------------------------------------------
        # DATA AGGREGATION LOOP
        # -------------------------------------------------

        for ticker in tickers:

            if ticker.get("underlying_asset_symbol") != "BTC":
                continue

            try:
                strike = float(ticker["strike_price"])
                oi = float(ticker.get("oi", 0))
                volume = float(ticker.get("volume", 0))
                option_type = ticker["contract_type"]

            except Exception:
                continue

            all_strikes[strike] += oi

            # PUT SIDE
            if option_type == "put_options":

                put_oi += oi
                put_volume += volume
                put_by_strike[strike] += oi

            # CALL SIDE
            else:

                call_oi += oi
                call_volume += volume
                call_by_strike[strike] += oi

            # ATM REGION
            if lower <= strike <= upper:

                if option_type == "put_options":

                    atm_put_oi += oi
                    atm_put_volume += volume

                else:

                    atm_call_oi += oi
                    atm_call_volume += volume
    
        # =====================================================
        # PCR CALCULATION
        # =====================================================

        pcr_oi = (
            put_oi / call_oi
            if call_oi > 0
            else 0
        )

        pcr_volume = (
            put_volume / call_volume
            if call_volume > 0
            else 0
        )

        bullish = 0
        bearish = 0

        # =====================================================
        # PCR SIGNALS
        # =====================================================

        if pcr_oi > 1.5:

            bearish += 35
            explanation.append("Strong put OI dominance")

        elif pcr_oi < 0.7:

            bullish += 35
            explanation.append("Strong call OI dominance")

        else:

            bullish += 15
            bearish += 15

        if pcr_volume > 1.3:

            bearish += 20
            explanation.append("Put volume dominant")

        elif pcr_volume < 0.7:

            bullish += 20
            explanation.append("Call volume dominant")

        else:

            bullish += 10
            bearish += 10

        # =====================================================
        # TOTAL OI SIGNALS
        # =====================================================

        if put_oi > call_oi * 1.2:

            bearish += 15
            explanation.append("Total put OI higher")

        elif call_oi > put_oi * 1.2:

            bullish += 15
            explanation.append("Total call OI higher")

        # =====================================================
        # ATM FLOW SIGNALS
        # =====================================================

        if atm_put_oi > atm_call_oi * 1.1:

            bearish += 10

        elif atm_call_oi > atm_put_oi * 1.1:

            bullish += 10

        if atm_put_volume > atm_call_volume * 1.1:

            bearish += 10

        elif atm_call_volume > atm_put_volume * 1.1:

            bullish += 10

        # =====================================================
        # SUPPORT / RESISTANCE LEVELS
        # =====================================================

        strongest_support = 0.0
        strongest_resistance = 0.0

        put_wall = 0.0
        call_wall = 0.0

        if put_by_strike:

            strongest_support = max(
                put_by_strike,
                key=put_by_strike.get
            )

            put_wall = put_by_strike[strongest_support]

        if call_by_strike:

            strongest_resistance = max(
                call_by_strike,
                key=call_by_strike.get
            )

            call_wall = call_by_strike[strongest_resistance]

        # =====================================================
        # MAX PAIN (APPROXIMATION)
        # =====================================================

        max_pain = min(
            all_strikes,
            key=lambda k: all_strikes[k]
        ) if all_strikes else 0.0

        # =====================================================
        # DEALER BIAS LOGIC
        # =====================================================

        if bearish >= self.STRONG_LEVEL:

            direction = "STRONG_BEARISH"

            dealer_bias = "SHORT_COVERING_EXPECTED"

        elif bearish >= self.NORMAL_LEVEL:

            direction = "BEARISH"

            dealer_bias = "DOWNWARD_PRESSURE"

        elif bullish >= self.STRONG_LEVEL:

            direction = "STRONG_BULLISH"

            dealer_bias = "SHORT_SQUEEZE_RISK"

        elif bullish >= self.NORMAL_LEVEL:

            direction = "BULLISH"

            dealer_bias = "UPWARD_PRESSURE"

        else:

            direction = "NEUTRAL"

            dealer_bias = "BALANCED"

        # =====================================================
        # CONFIDENCE SCORE
        # =====================================================

        total = bullish + bearish

        confidence = (
            max(bullish, bearish) / total * 100
            if total > 0
            else 0
        )

        # =====================================================
        # FINAL CONTEXT RETURN
        # =====================================================

        return OIContext(

            total_put_oi=put_oi,
            total_call_oi=call_oi,

            total_put_volume=put_volume,
            total_call_volume=call_volume,

            pcr_oi=pcr_oi,
            pcr_volume=pcr_volume,

            atm_put_oi=atm_put_oi,
            atm_call_oi=atm_call_oi,

            atm_put_volume=atm_put_volume,
            atm_call_volume=atm_call_volume,

            put_wall=put_wall,
            call_wall=call_wall,

            strongest_support=strongest_support,
            strongest_resistance=strongest_resistance,

            bullish_score=bullish,
            bearish_score=bearish,

            confidence=round(confidence, 2),

            direction=direction,

            dealer_bias=dealer_bias,

            gamma_wall=strongest_support,

            max_pain=max_pain,

            explanation=explanation,
        )                