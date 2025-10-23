import logging
import sys
from extract import extract, extract_list_detail
from transform import transform
from load import load, load_list_details

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Updated endpoints: 3 APIs total (2 from CoinGecko + 1 from Open-Meteo)
endpoints = [
    "coins/markets?vs_currency=usd",   # Crypto market data
    "exchange_rates",                  # Currency exchange rates
    "weather"                          # We'll manually handle this one
]

def run_etl():
    for ep in endpoints:
        logging.info(f"Fetching {ep}")
        if ep == "weather":
            # Separate API base for Open-Meteo
            from extract import fetch_url
            weather_url = "https://api.open-meteo.com/v1/forecast?latitude=10&longitude=76&hourly=temperature_2m"
            data = fetch_url(weather_url)
        else:
            data = extract(ep)

        if not data:
            logging.error(f"No data fetched for {ep}")
            continue

        records = transform(data, limit=5)  # Limit 5 for demo clarity
        load(ep, records)

        # 🖨️ Print a preview of data in terminal
        print(f"\n---- Sample output from {ep} ----")
        for i, rec in enumerate(records[:3]):
            print(rec)
        print("----------------------------------\n")

        if ep == "lists":
            load_list_details(records, extract_list_detail)

if __name__ == "__main__":
    try:
        run_etl()
        logging.info("ETL process completed successfully")
    except Exception as e:
        logging.critical(f"Fatal error: {e}")
