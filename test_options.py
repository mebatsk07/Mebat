from collectors.option_chain_collector import OptionChainCollector

collector = OptionChainCollector()

options = collector.btc_options()

print(f"BTC Options Found: {len(options)}")

print()

for option in options[:10]:
    print(
        option["symbol"],
        option["contract_type"],
        option["id"],
    )