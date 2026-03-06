from clean_data.ICleanDataFilter import ICleanDataFilter


class SelectEnglishNews(ICleanDataFilter):
    def process(self, data):
        return data.loc[data['es_ingles'] == True].copy()