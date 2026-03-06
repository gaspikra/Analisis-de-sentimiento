import yfinance as yf
from datetime import datetime
from data_getter.IStrategy import IDataStrategy

class FinancialValues(IDataStrategy): 
    def obtain_data(self, ticker, start, end):
        empresa = yf.Ticker(ticker)
        start_str = start if isinstance(start, str) else start.strftime('%Y-%m-%d')
        end_str = end if isinstance(end, str) else end.strftime('%Y-%m-%d')
        return {
            "results": empresa.history(
            start = start_str,
            end = end_str,
            auto_adjust = False
        ), 
        "csv name": f"stock_values_from_{start}_to_{end}.csv"}
    

    

