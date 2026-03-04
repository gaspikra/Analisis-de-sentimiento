import os
import pandas as pd
from datetime import date
import requests

api_key = os.getenv("API_KEY")

def top3_important_tickers(sentiments, dic):
    count=0
    for ticker in sentiments:
        match ticker["ticker"]:
            case "MA":
                dic["ma"] = ticker["sentiment"]
                count += 1
            case "AXP":
                dic["axp"] = ticker["sentiment"]
                count += 1
            case "COF":
                dic["cof"] = ticker["sentiment"]
                count += 1
            case _:
                pass
                
        if count == 3:
            break 
    return dic

today = date.today().strftime("%Y-%m-%d")

def get_today_params(date):
    return {
        "ticker": "MA",
        "published_utc.gte": date,
        "limit":"5",
        "apiKey":api_key
    }

def obtener_noticia_hoy(today):
    try:
        data = requests.get("https://api.massive.com/v2/reference/news", params = get_today_params(today))
        json_res = data.json()
        if len(json_res.get("results", []))> 0:
            return json_res
        else:
            print("No hubo noticias hoy :)")
            return None
    except Exception as e:
        print(e)
        return None

news = obtener_noticia_hoy(today)

if news is not None:
    data = pd.read_csv("./data/fechas_faltantes.csv")
    important_data = news.json()
    
    new_dict = {}
    new_dict["date"] = important_data["published_utc"]
    new_dict["title"] = important_data["title"]
    new_dict["ma"] = None
    new_dict["axp"] = None
    new_dict["cof"] = None
    if "insights" in important_data:
        top3_important_tickers(important_data["insights"],new_dict)

    new_row = pd.DataFrame([new_dict])

    data = pd.concat([data, new_row], ignore_index= True)

    data.to_csv(".data/datos_2023-07-10_a_2026-02-04", index = False)

