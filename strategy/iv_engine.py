from dataclasses import dataclass
import math


# =====================================================
# IV CONTEXT
# =====================================================

@dataclass
class IVContext:

    atm_iv: float

    average_iv: float

    weighted_iv: float

    iv_rv_ratio: float

    expected_move: float

    iv_state: str

    iv_score: float

    selling_allowed: bool

    explanation: list[str]


# =====================================================
# IV ENGINE
# =====================================================

class IVEngine:

    ATM_PERCENT = 0.02

    def analyze(

        self,

        tickers,

        spot,

        historical_volatility,

        days_to_expiry=1,

    ):

        lower = spot * (1 - self.ATM_PERCENT)

        upper = spot * (1 + self.ATM_PERCENT)

        atm_values = []

        weighted_sum = 0

        total_weight = 0

        all_iv = []

        explanation = []

        for ticker in tickers:

            if ticker.get("underlying_asset_symbol") != "BTC":

                continue

            try:

                strike = float(
                    ticker.get("strike_price", 0)
                )

                quotes = ticker.get("quotes", {})

                iv = float(
                    quotes.get("mark_iv", 0)
                )

                oi = float(
                    ticker.get("oi", 0)
                )

            except Exception:

                continue

            if iv <= 0:

                continue

            all_iv.append(iv)

            weighted_sum += iv * max(oi, 1)

            total_weight += max(oi, 1)

            if lower <= strike <= upper:

                atm_values.append(iv)

        # ----------------------------------
        # Average IV
        # ----------------------------------

        atm_iv = (

            sum(atm_values) / len(atm_values)

            if atm_values else 0

        )

        average_iv = (

            sum(all_iv) / len(all_iv)

            if all_iv else 0

        )

        weighted_iv = (

            weighted_sum / total_weight

            if total_weight else average_iv

        )

        # ----------------------------------
        # IV/RV Ratio
        # ----------------------------------

        if historical_volatility > 0:

            iv_rv_ratio = (

                atm_iv /

                historical_volatility

            )

        else:

            iv_rv_ratio = 0

        # ----------------------------------
        # Expected Move
        # ----------------------------------

        expected_move = (

            spot *

            atm_iv *

            math.sqrt(days_to_expiry / 365)

        )

        # ----------------------------------
        # Classification
        # ----------------------------------

        selling_allowed = False

        score = 0

        state = "UNKNOWN"

        if iv_rv_ratio >= 1.80:

            state = "EXCELLENT_FOR_SELLING"

            score = 100

            selling_allowed = True

            explanation.append(

                "IV much higher than RV"

            )

        elif iv_rv_ratio >= 1.50:

            state = "GOOD_FOR_SELLING"

            score = 85

            selling_allowed = True

            explanation.append(

                "High IV relative to RV"

            )

        elif iv_rv_ratio >= 1.20:

            state = "NEUTRAL"

            score = 60

            explanation.append(

                "Average IV environment"

            )

        elif iv_rv_ratio >= 1.00:

            state = "LOW_PREMIUM"

            score = 40

            explanation.append(

                "Premiums relatively low"

            )

        else:

            state = "AVOID_SELLING"

            score = 20

            explanation.append(

                "IV lower than RV"

            )

        return IVContext(

            atm_iv=round(atm_iv, 4),

            average_iv=round(average_iv, 4),

            weighted_iv=round(weighted_iv, 4),

            iv_rv_ratio=round(iv_rv_ratio, 2),

            expected_move=round(expected_move, 2),

            iv_state=state,

            iv_score=score,

            selling_allowed=selling_allowed,

            explanation=explanation,

        )