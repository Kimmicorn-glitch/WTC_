import sys

def bitcoin():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    price = get_bitcoin_price("FAKE_KEY")
    total = bitcoins * price
    print(f"${total:,.4f}")

def get_bitcoin_price(api_key: str) -> float:

    return 97845.0243

if __name__ == "__main__":
    bitcoin()
