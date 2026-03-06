from langdetect import detect
from steps.clean_data.ICleanDataFilter import ICleanDataFilter

class EnglishNews(ICleanDataFilter):
    def process(self, dataframe):
        dataframe["es_ingles"] = dataframe["real_news"].apply(self._es_ingles) 
        return dataframe

    def _es_ingles(self ,text):
        if detect(text) == "en":
            return True
        else:
            return False
