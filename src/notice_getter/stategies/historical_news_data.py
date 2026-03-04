import requests
from notice_getter.IStrategy import IDataStrategy


class HistoricalNewsData(IDataStrategy):

    api_key = None
    def __init__(self, api_key):
        self.api_key = api_key

    def obtain_data(self,ticker, start, end):
        config_data = {
            "ticker": ticker,
            "published_utc_start": start,
            "published_utc_end": end,
            "sort": "published_utc",
            "limit":"950",
            "apiKey": self.api_key
        }
        try:
            return {"results": requests.get("https://api.massive.com/v2/reference/news", params=config_data).json()["results"],
                    "csv name": f"news_from_{start}_to_{end}.csv"}
        
        except Exception as e:
            print(f"ocurrió un error, paso esto: {e}")

    