from steps.feature_engineering.I_featuring import IFeaturing
import pandas_ta as ta

class Ema_aggregation(IFeaturing):

    def __init__(self, periods):
        self.periods = periods

    def process(self, data):
        data[f'ema{str(self.periods)}'] = data['Adj Close'].ewm(span=self.periods,adjust=False).mean()
        data = self._get_distance(data)
        data.drop([f'ema{str(self.periods)}'],axis=1, inplace=True)
        return data
    
    def _get_distance(self, data):
        data[f'distance_ema_{str(self.periods)}'] = (data[f'ema{str(self.periods)}'] - data['Adj Close']) / data[f'ema{str(self.periods)}']
        return data 
    
    

class Mma_agregation(IFeaturing):

    def __init__(self, periods):
        self.periods = periods

    def process(self, data):
        data[f'mma{str(self.periods)}'] = data['Adj Close'].rolling(self.periods).mean()
        data = self._get_distance(data)
        data.drop([f'mma{str(self.periods)}'],axis=1, inplace=True)
        return data

    def _get_distance(self, data):
        data[f'distance_mma_{str(self.periods)}'] = (data[f'mma{str(self.periods)}'] - data['Adj Close']) / data[f'mma{str(self.periods)}']
        return data 
        

class Rsi_aggregation(IFeaturing):

    def __init__(self, periods):
        self.periods = periods
    
    def process(self, data):
        data[f'rsi_{str(self.periods)}'] = ta.rsi(data['Adj Close'], length= int(self.periods))
        return data


class Target_agregation(IFeaturing):

    def __init__(self, periods):
        self.periods = periods
        
    def process(self, data):
        data['target'] = data['Adj Close'].shift( - int(self.periods)).pct_change()
        return data
