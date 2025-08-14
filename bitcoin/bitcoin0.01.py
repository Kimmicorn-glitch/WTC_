import sys
import requests

API_KEY = "5f226d975e41ce0d4069065e51df2ad79171ffab7ae231e635721649043f7f4b"
API_URL = "https://rest.coincap.io/v3/assets/bitcoin"

def bitcoin():
    if len(sys.argv) !=2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    price = get_bitcoin_price(API_KEY)
    cost = bitcoins * price
    print(f"${cost:,.4f}")

def get_bitcoin_price(api_key: str) -> float:

    try:
        response = response.get( API_URL , params={"apiKey": api_key}, timeout=10)
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching Bitcion price")
    except (KeyError, ValueError):
        sys.exit("Unexpected data format from API")

if __name__ == "__main__":
    bitcoin()

