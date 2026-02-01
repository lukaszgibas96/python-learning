# Problem set 4 - bitcoin price index

import sys
import requests

try:
    bitcoin = float(sys.argv[1])

    response = requests.get(
    "https://rest.coincap.io/v3/assets/bitcoin?apiKey=3191a1522924d44a56b36179a8368f5235100ffb54951b9424d484ff93af1609"
                        )
    response.raise_for_status()

    content = response.json()
    price_usd = float(content["data"]["priceUsd"])

    price = bitcoin * price_usd

    print(f"${price:,.4f}")

except ValueError:
     sys.exit("Command-line argument is not a number")
except IndexError:
     sys.exit("Missing command-line argument ")


