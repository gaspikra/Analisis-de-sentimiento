
import requests
import os

spy500_ticker = "SPY"
api_key = os.getenv("API_KEY")



try:
    data = requests.get(f"https://api.massive.com/v2/reference/news?ticker={spy500_ticker}&apiKey={api_key}")
except Exception as e:
    print(f"no funciono porque mira: \n : {e}")


