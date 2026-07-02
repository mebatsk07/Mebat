from api.delta_client import DeltaClient
from parsers.candidate_builder import build_candidate
from strategy.candidate_filter import CandidateFilter

# --------------------------------------------------
# CHANGE THIS TO TEST DIFFERENT MARKET REGIMES
# --------------------------------------------------
regime = "STRONG_DOWNTREND"
# regime = "SIDEWAYS"
# regime = "VOLATILE_RANGE"

print("=" * 60)
print("Current Regime:", regime)
print("=" * 60)

client = DeltaClient()

response = client.get_tickers(
    contract_types=["call_options", "put_options"]
)

tickers = response["result"]

filter_engine = CandidateFilter()

accepted = []

print("\nChecking candidates...\n")

for ticker in tickers:

    candidate = build_candidate(ticker)

    ok, reason = filter_engine.filter(candidate, regime)

    if ok:
        accepted.append(candidate)

        print(
            f"[ACCEPT] {candidate.symbol} | "
            f"Premium=${candidate.premium:.2f} | "
            f"Delta={candidate.delta:.4f}"
        )

    else:
        print(
            f"[REJECT] {candidate.symbol} | "
            f"Premium=${candidate.premium:.2f} | "
            f"Delta={candidate.delta:.4f} | "
            f"Reason: {reason}"
        )

print("\n" + "=" * 60)
print(f"Accepted: {len(accepted)}")
print("=" * 60)

if accepted:
    print("\nAccepted Candidates:\n")

    for c in accepted:
        print(
            f"{c.symbol:25}"
            f" Premium=${c.premium:7.2f}"
            f" Delta={c.delta:8.4f}"
        )