from clean_data.ICleanDataFilter import ICleanDataFilter


class TransformValues(ICleanDataFilter):
    def process(self, data):
        data_en = self._delete_non_english_news(data)
        return self._transform_sentimients(data_en)

    def _delete_non_english_news(self, data):
        return data.loc[data.es_ingles == True]
    
    def _transform_sentimients(self, data):
        transformed_data = data
        cols = ["ma", "axp", "cof"]
        sentiment_map = {
            "positive": 1,
            "negative": -1,
            "neutral": 0
        }
        transformed_data[cols] = transformed_data[cols].replace(sentiment_map)
        transformed_data[cols] = transformed_data[cols].fillna(0)
        return transformed_data