import os
import sys
import pandas as pd
from dotenv import load_dotenv


sys.path.append(os.path.join(os.getcwd(), 'src'))

load_dotenv()


from steps.clean_data.null_stock_treatment.cleaning_stock_values import NaNTreatment
from steps.clean_data.null_stock_treatment.delete_meaningless_columns import MeaninglessColumnsTreatment
from steps.clean_data.select_english_news import SelectEnglishNews
from steps.feature_engineering.invest_feature_pipe.steps_pi import Ema_aggregation, Mma_agregation, Target_agregation
from steps.feature_engineering.invest_feature_pipe.feature_technical_agg import FeatureAgregation
from pipeline import MastercardDataPipeline
from steps.clean_data.select_data import SelectData
from steps.clean_data.english_news import EnglishNews
from steps.clean_data.transform_values import TransformValues
from steps.feature_engineering.sentimient_classification import SentimentClassification
from steps.integration import DataIntegration
from steps.clean_data.final_null_treatment import NewsFillNaTreatment

def run_production_pipeline():

    load_dotenv()
    api_key = os.getenv("API_KEY")
    
    print("--- INICIANDO PIPELINE DE MASTERCARD ---")


    pipe = MastercardDataPipeline()
    stock_pipe = FeatureAgregation()
    stock_pipe.add_feature(Ema_aggregation(8))
    stock_pipe.add_feature(Ema_aggregation(21))
    stock_pipe.add_feature(Mma_agregation(200))
    stock_pipe.add_feature(Target_agregation(1))

    print("Configurando filtros y modelos...")
    pipe.set_stock_features(stock_pipe)
    pipe.add_news_filter(SelectData())
    pipe.add_news_filter(EnglishNews())
    pipe.add_news_filter(TransformValues())
    pipe.add_news_filter(SelectEnglishNews())
    pipe.add_news_filter(SentimentClassification()) 
    pipe.add_stock_filter(NewsFillNaTreatment())
    pipe.add_stock_filter(MeaninglessColumnsTreatment())
    pipe.add_stock_filter(NaNTreatment())


    try:
        print("Cargando datos de entrada...")
        news_df = pd.read_csv('data/csv/news_from_2024-01-01_to_2026-03-04.csv')
        stock_df = pd.read_csv('data/csv/stock_values_from_2022-09-01_to_2026-03-04.csv')
        
        print("Procesando sentimientos y metricas tecnicas...")
        merger = DataIntegration()
        result = pipe.run(news_df, stock_df, merger)
        
        print(f"¡EXITO! Pipeline completado. Filas procesadas: {len(result)}")
        
    except FileNotFoundError:
        print("ERROR: No se encontraron los archivos CSV.")

if __name__ == "__main__":
    run_production_pipeline()