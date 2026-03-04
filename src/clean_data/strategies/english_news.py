from langdetect import detect
from clean_data import ICleanDataStrategy

class EnglishNewsStrategy(ICleanDataStrategy):
    def clean_data(self, dataframe):
        dataframe["es_ingles"] = dataframe["real_news"].apply(self._es_ingles) 
        return dataframe

    def _es_ingles(self ,text):
        if detect(text) == "en":
            return True
        else:
            return False
