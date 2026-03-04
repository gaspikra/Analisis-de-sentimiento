from dotenv import load_dotenv
import requests
import os 

load_dotenv()

def get_notice(apikey,ticker, topic, time_from, time_to):
    
    topics = {
        "financial": "financial_markets",
        "economy":"economy_fiscal",
        "finance": "finance",
        "manufacturing":"manufacturing",
        "technology": "technology"
    }
    if topic not in list(topics):
        raise ValueError(f"Periodo inválido: '{topic}'. Opciones: {', '.join([t for t in topics.values()])} ")
    
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={apikey}&topics={topics[topic]}&time_from={time_from}&time_to={time_to}'
    try:
        response = requests.get(url)
        return response.json()
    except Exception as er:
        print(f"ocurrio un error del tipo {er}")


print(get_notice(os.getenv("API_KEY"),"SPY", "financial","20200610T0130","20260710T0130"))

