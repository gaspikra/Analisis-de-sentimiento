import sys
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)


sys.path.append(os.path.join(root_path, 'src'))


from clean_data.steps.english_news import EnglishNews
from clean_data.steps.select_data import SelectData
from clean_data.steps.transform_values import TransformValues
from main import MastercardDataPipeline
from news_getter.stategies.historical_news_data import HistoricalNewsData
from news_getter.stategies.historical_values_data import FinancialValues


api_key = os.getenv("API_KEY")
print(api_key)
pipeline = MastercardDataPipeline()
news_stock_strat = HistoricalNewsData(api_key) 
values_stock_strat = FinancialValues()

selected_data = SelectData()
english_news = EnglishNews()
transform_values = TransformValues()

#pipeline.set_data_strategy(values_stock_strat)
#data_values = pipeline.obtain_data('MA','2024-01-01','2026-03-04')
#pipeline.set_data_strategy(news_stock_strat)
#news_values = pipeline.obtain_data('MA','2024-01-01','2026-03-04')
news_values = pd.read_csv('data/csv/news_from_2024-01-01_to_2026-03-04.csv')
pipeline.add_filter(selected_data)
pipeline.add_filter(english_news)
pipeline.add_filter(transform_values)
pipeline.clean_data(news_values)
