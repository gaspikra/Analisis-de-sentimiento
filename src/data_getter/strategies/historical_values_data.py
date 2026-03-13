import yfinance as yf
from data_getter.IStrategy import IDataStrategy

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
        
    

    

