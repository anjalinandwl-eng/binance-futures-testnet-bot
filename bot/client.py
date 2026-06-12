from binance.client import Client

# Binance Testnet API Keys
api_key = "YOUR_API_KEY"
api_secret = "YOUR_SECRET_KEY"

client = Client(
    api_key,
    api_secret,
    testnet=True
)
