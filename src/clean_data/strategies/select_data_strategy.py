from clean_data import ICleanDataStrategy


class SelectData(ICleanDataStrategy):
    def clean_data(self, pipeline):
        important_data = []
        for news in pipeline:
            if "description" in list(news.keys()):
                new_dict = {}
                new_dict["date"] = news["published_utc"]
                new_dict["title"] = news["title"]
                new_dict["real_news"] = news["description"]
                new_dict["ma"] = None
                new_dict["axp"] = None
                new_dict["cof"] = None
                if "insights" in news:
                    self._top3_important_tickers(news["insights"],new_dict)
                important_data.append(new_dict)


    def _top3_important_tickers(self,sentiments, dic):
        count=0
        for ticker in sentiments:
            match ticker["ticker"]:
                case "MA":
                    dic["ma"] = ticker["sentiment"]
                    count += 1
                case "AXP":
                    dic["axp"] = ticker["sentiment"]
                    count += 1
                case "COF":
                    dic["cof"] = ticker["sentiment"]
                    count += 1
                case _:
                    pass

            if count == 3:
                break 
        return dic