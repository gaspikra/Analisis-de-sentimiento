import pandas as pd
from steps.feature_engineering.I_featuring import IFeaturing
from transformers import  pipeline


class SentimentClassification(IFeaturing):

    def __init__(self):
        self.nlp = pipeline("sentiment-analysis", model="ProsusAI/finbert")

    def process(self, data):
        final_df = data.copy()
        final_df["news_score"] = final_df.apply(
            lambda row: self._get_sentiment(row['real_news'], row['ma']), 
            axis=1
        )
        return final_df

    def _get_sentiment(self, text, ma_label):
        if not text or pd.isna(text):
            return 0.0
        result = self.nlp(self._contextualize_model(text[:512]))
        ai_label = result[0]['label'].lower()
        ai_score = result[0]['score']
        if ma_label == 0:
            if ai_label == 'negative':
                return ai_score * -1
            elif ai_label == 'neutral':
                return 0.0
            else:
                return ai_score
        else:
            return ai_score * ma_label
        
    def _contextualize_model(self, text):
        return f'Regarding Mastercard: {text}'