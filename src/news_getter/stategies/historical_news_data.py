import requests
from news_getter.IStrategy import IDataStrategy



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
        url = "https://api.massive.com/v2/reference/news"
        
        try:
            response = requests.get(url, params=config_data)
            data_json = response.json()
            if "results" in data_json:
                return {
                    "results": data_json["results"],
                    "csv name": f"news_from_{start}_to_{end}.csv"
                }
            else:
                print(f"Massive no devolvio 'results'. Respuesta cruda: {data_json}")
                return {"results": [], "csv name": f"error_news.csv"}
                
        except Exception as e:
            print(f"Ocurrio un error en la peticion a Massive: {e}")
            return {"results": [], "csv name": f"error_news.csv"}

    