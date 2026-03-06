from steps.clean_data.ICleanDataFilter import ICleanDataFilter
import pandas as pd
import ast

class SelectData(ICleanDataFilter):
    def process(self, data):
        important_data = []
        records = data.to_dict('records')
        for news in records:
            if pd.notna(news.get("description")):
                new_dict = {}
                new_dict["date"] = news["published_utc"]
                new_dict["title"] = news["title"]
                new_dict["real_news"] = news["description"]
                new_dict["ma"] = None
                new_dict["axp"] = None
                new_dict["cof"] = None
                if pd.notna(news.get("insights")):
                    self._top3_important_tickers(news["insights"],new_dict)
                important_data.append(new_dict)
        return pd.DataFrame(important_data)


    def _top3_important_tickers(self, sentiments, dic):
        if isinstance(sentiments, str):
            try:
                sentiments = ast.literal_eval(sentiments)
            except (ValueError, SyntaxError):
                return dic 
        if not isinstance(sentiments, list):
            return dic
        count = 0
        for ticker in sentiments:
            ticker_name = ticker.get("ticker")
            match ticker_name:
                case "MA":
                    dic["ma"] = ticker.get("sentiment")
                    count += 1
                case "AXP":
                    dic["axp"] = ticker.get("sentiment")
                    count += 1
                case "COF":
                    dic["cof"] = ticker.get("sentiment")
                    count += 1
            if count == 3:
                break 
        return dic