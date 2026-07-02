from api.delta_client import DeltaClient

client = DeltaClient()

products = client.get_products()["result"]

for product in products:
    symbol = product.get("symbol", "")
    if symbol.startswith("BTC"):
        print(symbol)