from notice_getter.IStrategy import IDataStrategy
import yfinance as yf

class FinancialValues(IDataStrategy):
    
    def obtain_data(self, ticker, start, end):
        empresa = yf.Ticker(ticker)
        return {
            "results": empresa.history(
            start = start,
            end = end,
            auto_adjust = False
        ), 
        "csv name": f"stock_values_from_{start}_to_{end}.csv" }
    

    

