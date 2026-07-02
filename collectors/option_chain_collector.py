from api.delta_client import DeltaClient


class OptionChainCollector:

    def __init__(self):
        self.client = DeltaClient()

    def btc_options(self):

        products = self.client.get_products()["result"]

        options = []

        for product in products:

            symbol = product.get("symbol", "")

            contract_type = product.get("contract_type", "")

            if (
                "BTC" in symbol
                and contract_type in ("call_options", "put_options")
            ):
                options.append(product)

        return options