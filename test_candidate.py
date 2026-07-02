from api.delta_client import DeltaClient

from parsers.candidate_builder import build_candidate

client = DeltaClient()

ticker = client.get_tickers(
    ["call_options", "put_options"]
)["result"][0]

candidate = build_candidate(ticker)

print(candidate)