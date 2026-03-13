from binance.client import Client

API_KEY = "eEffHkSp9dcVbpADPhuUYYS5wwlW93YLYvsvqxiC4Ari3VPG1FBob2uWJbiLMyRh"
API_SECRET = "CUXlDBDkE5CDAk45MMyhuZGgnxQJn4czMU6qkpojd6AK9MH4RNmd9GEm6I7Hdekb"

def get_client():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    return client