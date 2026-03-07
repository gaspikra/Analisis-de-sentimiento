import pandas as pd
class DataIntegration:

    def integration(self, news_dataFrame, stock_dataFrame):
        modificated_news_df = news_dataFrame.rename(columns={'date':'Date'})
        modificated_news_df = self._daily_mean_score(modificated_news_df)
        stock_dataFrame['Date'] = pd.to_datetime(stock_dataFrame['Date'], utc=True).dt.tz_localize(None).dt.normalize()
        joined_dataframe = pd.merge(stock_dataFrame, modificated_news_df, how="left", on = "Date")
        return joined_dataframe
    
    def _daily_mean_score(self, data):
        data['Date'] = pd.to_datetime(data['Date'], utc=True).dt.tz_localize(None).dt.normalize()
        data.drop(['title','real_news'], axis=1, inplace=True)
        agrupated_df = data.groupby('Date').agg({
            'ma':'mean',
            'axp': 'mean',
            'cof':'mean',
            'news_score':'mean'
        }).reset_index()
        return agrupated_df
    
    