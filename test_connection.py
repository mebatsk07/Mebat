from api.delta_client import DeltaClient

client = DeltaClient()

products = client.get_products()["result"]

found = False

for product in products:
    symbol = product.get("symbol", "")
    contract_type = product.get("contract_type", "")

    if "BTC" in symbol.upper() and contract_type == "perpetual_futures":
        found = True
        print("=" * 60)
        print(f"ID: {product['id']}")
        print(f"Symbol: {symbol}")
        print(f"Type: {contract_type}")

if not found:
    print("No BTC perpetual contract found.")