import yfinance as yf
from data_getter.IStrategy import IDataStrategy
from datetime import datetime

class FinancialValues(IDataStrategy): 
    def obtain_data(self, ticker, start, end):
        empresa = yf.Ticker(ticker)
        df = empresa.history(
            start = start,
            end = end,
            auto_adjust = False
        )
        df.reset_index(inplace=True)
        return{
            "results": df,
            "csv name": f"stock_values_from_{start}_to_{end}.csv"
        }
        
    def obtain_today_data(self, ticker):
        today = datetime.now().strftime("%Y-%m-%d")
        return self.obtain_data(ticker, today, today)

