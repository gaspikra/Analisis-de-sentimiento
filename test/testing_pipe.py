import sys
import os
from dotenv import load_dotenv
import pandas as pd



load_dotenv()
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)
sys.path.append(os.path.join(root_path, 'src'))


from steps.clean_data.final_null_treatment import NewsFillNaTreatment
from steps.integration import DataIntegration
from steps.feature_engineering.sentimient_classification import SentimentClassification
from main import MastercardDataPipeline
from steps.clean_data.select_english_news import SelectEnglishNews
from steps.clean_data.english_news import EnglishNews
from steps.clean_data.select_data import SelectData
from steps.clean_data.transform_values import TransformValues
from data_getter.strategies.historical_news_data import HistoricalNewsData
from data_getter.strategies.historical_values_data import FinancialValues

sys.path.append(os.path.abspath("../src"))

from steps.feature_engineering.invest_feature_pipe.feature_technical_agg import FeatureAgregation
from steps.feature_engineering.invest_feature_pipe.steps_pi import Ema_aggregation, Mma_agregation, Rsi_aggregation, Target_agregation

api_key = os.getenv("API_KEY")
print(api_key)


pipeline = MastercardDataPipeline()
news_stock_strat = HistoricalNewsData(api_key) 
stock_pipe = FeatureAgregation()

values_stock_strat = FinancialValues()
selected_data = SelectData()
english_news = EnglishNews()
transform_values = TransformValues()
select_english_news = SelectEnglishNews()
null_treatment = NewsFillNaTreatment()
scoring_news = SentimentClassification()
merger = DataIntegration()

#pipeline.set_data_strategy(values_stock_strat)
#data_values = pipeline.obtain_data('MA','2022-09-01','2026-03-04')

#pipeline.set_data_strategy(news_stock_strat)
#news_values = pipeline.obtain_data('MA','2024-01-01','2026-03-04')

last_data = pd.read_csv('data/csv/news_from_2024-01-01_to_2026-03-04.csv')
data_values = pd.read_csv('data/csv/stock_values_from_2022-09-01_to_2026-03-04.csv')

#pipeline.add_news_filter(selected_data)
#pipeline.add_news_filter(english_news)
#pipeline.add_news_filter(transform_values)
#pipeline.add_news_filter(select_english_news)
#pipeline.add_news_filter(scoring_news)
#pipeline.add_stock_filter(null_treatment)


ema8 = Ema_aggregation(8)
ema21 = Ema_aggregation(21)
rsi14 = Rsi_aggregation(14)
mma200 = Mma_agregation(200)
target = Target_agregation(1)

stock_pipe.add_feature(ema8)
stock_pipe.add_feature(ema21)
stock_pipe.add_feature(rsi14)
stock_pipe.add_feature(mma200)
stock_pipe.add_feature(target)

pipeline.add_stock_filter(null_treatment)
pipeline.set_stock_features(stock_pipe)

#pipeline.run()

news_data = pd.read_csv('data/csv/final.csv')






