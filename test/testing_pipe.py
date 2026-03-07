import sys
import os
from dotenv import load_dotenv
import pandas as pd



load_dotenv()
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)
sys.path.append(os.path.join(root_path, 'src'))


from steps.integration import DataIntegration
from steps.feature_engineering.sentimient_classification import SentimentClassification
from main import MastercardDataPipeline
from steps.clean_data.transform_data_types import TransformDateTypes
from steps.clean_data.select_english_news import SelectEnglishNews
from steps.clean_data.english_news import EnglishNews
from steps.clean_data.select_data import SelectData
from steps.clean_data.transform_values import TransformValues
from data_getter.strategies.historical_news_data import HistoricalNewsData
from data_getter.strategies.historical_values_data import FinancialValues


api_key = os.getenv("API_KEY")
print(api_key)


pipeline = MastercardDataPipeline()
news_stock_strat = HistoricalNewsData(api_key) 


values_stock_strat = FinancialValues()
selected_data = SelectData()
english_news = EnglishNews()
transform_values = TransformValues()
select_english_news = SelectEnglishNews()
transform_data_news = TransformDateTypes('date')
transform_data_stock = TransformDateTypes('Date')
#scoring_news = SentimentClassification()
merger = DataIntegration()

#pipeline.set_data_strategy(values_stock_strat)
#data_values = pipeline.obtain_data('MA','2023-07-17','2026-03-04')
#pipeline.set_data_strategy(news_stock_strat)
#news_values = pipeline.obtain_data('MA','2024-01-01','2026-03-04')
data_values = pd.read_csv('data/csv/stock_values_from_2023-07-17_to_2026-03-04.csv')
news_values = pd.read_csv('data/csv/final.csv')
#pipeline.add_filter(selected_data)
#pipeline.add_filter(english_news)
#pipeline.add_filter(transform_values)
#pipeline.add_filter(select_english_news)
#pipeline.add_filter(transform_data_news)
#pipeline.add_filter(scoring_news)
#pipeline.clean_data(news_values)
#pipeline.add_filter(transform_data_stock)
pipeline.mergeData(merger, news_values, data_values)

