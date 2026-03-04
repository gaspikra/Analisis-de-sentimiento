from clean_data import ICleanDataStrategy


class TransformValues(ICleanDataStrategy):
    def clean_data(self, pipeline):
        pipe = self._delete_non_english_news(pipeline)
        return self._transform_sentimients(pipe)



    def _delete_non_english_news(self, pipeline):
        return pipeline.loc[pipeline.es_ingles == True]
    
    def _transform_sentimients(self, pipeline):
        cols = ["ma", "axp", "cof"]
        sentiment_map = {
            "positive": 1,
            "negative": -1,
            "neutral": 0
        }
        pipeline[cols] = pipeline[cols].replace(sentiment_map)
        pipeline[cols] = pipeline[cols].fillna(0)
        return pipeline