import pandas as pd
from steps.feature_engineering.I_featuring import IFeaturing
from transformers import  pipeline


class SentimentClassification(IFeaturing):

    def __init__(self):
        self.nlp = pipeline("sentiment-analysis", model="ProsusAI/finbert")

    def process(self, data):
        process_data = data.copy()
        return self._get_sentiment(process_data)

    def _get_sentiment(self, data):
        contextualized_texts = [
            self._contextualize_model(str(txt)[:2000]) if pd.notna(txt) and txt else ""
            for txt in data["real_news"]
        ]
        score_result = self.nlp(contextualized_texts, batch_size=10)
        scores_finales = []
        for i, result in enumerate(score_result):
            noticia_original = data.iloc[i]['real_news']
            if not noticia_original or pd.isna(noticia_original):
                scores_finales.append(0.0)
            else:
                ai_label = result['label'].lower()
                ai_score = result['score']
                ma_val = data.iloc[i]["ma"]
                scores_finales.append(
                    self._calcular_score_final(ai_label,ai_score,ma_val)
                )
        data["news_scores"] = scores_finales
        return data


    def _calcular_score_final(self, ai_label, ai_score, ma_label):        
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