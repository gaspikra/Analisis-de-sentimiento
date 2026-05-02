import pandas as pd
import logging

class DataIntegration:
    def __init__(self):
        self.logger = logging.getLogger(__name__)


    def integration(self, news_dataFrame, stock_dataFrame):
        self.logger.info(f"iniciando paso de merging")
        modificated_news_df = news_dataFrame.rename(columns={'date':'Date'})
        modificated_news_df = self._daily_mean_score(modificated_news_df)
        self.logger.info(f"media de los datos obtenida correctamente")
        stock_dataFrame['Date'] = pd.to_datetime(stock_dataFrame['Date'], utc=True).dt.tz_localize(None).dt.normalize()
        try:
            joined_dataframe = pd.merge(stock_dataFrame, modificated_news_df, how="left", on = "Date")
        except Exception as e:
            self.logger.exception(f"Error critico en MERGING, leer error:")
            raise e
        self.logger.info(f"mergeo satisfactorio")
        return joined_dataframe
    
    def _daily_mean_score(self, data):
        self.logger.info(f"configurando campos para mergear:")
        try:
            data['Date'] = pd.to_datetime(data['Date'], utc=True).dt.tz_localize(None).dt.normalize()
            data.drop(['title','real_news'], axis=1, inplace=True)
            agrupated_df = data.groupby('Date').agg({
                'ma':'mean',
                'axp': 'mean',
                'cof':'mean',
                'news_scores':'mean'
            }).reset_index()
        except Exception as e:
            self.logger.exception(f"Error critico en el paso de hacer la media de las columnas")
            raise e

        return agrupated_df
    
    