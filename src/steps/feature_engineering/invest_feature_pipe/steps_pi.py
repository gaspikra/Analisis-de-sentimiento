from steps.feature_engineering.I_featuring import IFeaturing
import pandas_ta as ta
import logging

logger = logging.getLogger(__name__)

class Ema_aggregation(IFeaturing):

    def __init__(self, periods):
        self.periods = periods
        
    def process(self, data):
        logger.info(f"iniciando agregacion de Emas")
        try:
            data[f'ema{str(self.periods)}'] = data['Adj Close'].ewm(span=self.periods,adjust=False).mean()
            data = self._get_distance(data)
            data.drop([f'ema{str(self.periods)}'],axis=1, inplace=True)
            logger.debug(f"EMA {self.periods} procesada correctamente.")
        except Exception as e:
            logger.exception("error en {__name__}, checkear error:")
            raise e

        return data
    
    def _get_distance(self, data):
        try:
            data[f'distance_ema_{str(self.periods)}'] = (data[f'ema{str(self.periods)}'] - data['Adj Close']) / data[f'ema{str(self.periods)}']
        except Exception as e:
            logger.exception(f"error en {__name__}, al calcular las distancias de precio y EMA")
            raise e
        return data 
    
    

class Mma_agregation(IFeaturing):

    def __init__(self, periods):
        self.periods = periods

    def process(self, data):
        logger.info(f"calculando MMA{self.periods}")
        try:
            data[f'mma{str(self.periods)}'] = data['Adj Close'].rolling(self.periods).mean()
            data = self._get_distance(data)
            data.drop([f'mma{str(self.periods)}'],axis=1, inplace=True)
            logger.debug(f"MMA {self.periods} procesada correctamente.")

        except Exception as e:
            logger.exception("error en {__name__}, revisar problema con los logs")
            raise e
        
        
        return data

    def _get_distance(self, data):
        data[f'distance_mma_{str(self.periods)}'] = (data[f'mma{str(self.periods)}'] - data['Adj Close']) / data[f'mma{str(self.periods)}']
        return data 
        

class Rsi_aggregation(IFeaturing):

    def __init__(self, periods):
        self.periods = periods
        self.logging = logging.getLogger(__name__)
    
    def process(self, data):
        logger.info(f"calculando RSI en {__name__}")
        try:
            data[f'rsi_{str(self.periods)}'] = ta.rsi(data['Adj Close'], length= int(self.periods))
            logger.debug("rsi calculado correctamente")
        except Exception as e:
            logger.exception("problema en RSI, revisar logs")
            raise e
        
        
        return data


class Target_agregation(IFeaturing):

    def __init__(self, periods):
        self.periods = periods
        self.logging = logging.getLogger(__name__)
        
    def process(self, data):
        logger.info(f"agregando TARGET a la tabla en {__name__}")
        try:
            future_price = data['Adj Close'].shift(-int(self.periods))
        except Exception as e:
            logger.exception("error al agregar target: ")
            raise e

        data['target'] = (future_price / data['Adj Close']) - 1
        return data