import pandas as pd
import os

class MastercardDataPipeline:

    def __init__(self):
        self.news_filters = []
        self.stock_filters = []
        self.data_strategy = None
        self.stocks_features = None
        
        
    def set_data_strategy(self, strategy):
        self.data_strategy = strategy

    def obtain_data(self, ticker, start, end):
        results = self.data_strategy.obtain_data(ticker, start, end)
        data = results["results"]
        data_frame = pd.DataFrame(data)
        self.__save_csv(data_frame, results['csv name'])
        return data_frame, f"{results['csv name']}.csv"

    def add_news_filter(self, filter_obj):
        self.news_filters.append(filter_obj)
        return self
    
    def add_stock_filter(self, filter_obj):
        self.stock_filters.append(filter_obj)
        return self
    
    def set_stock_features(self, stock_features):
        self.stocks_features = stock_features

    def _apply_filters(self, data, filters):
        result = data.copy()
        for f in filters:
            result = f.process(result)
        return result
    
    def run(self, news_df, stock_df, merger, apply_features= True):
        
        cleaned_news = self._apply_filters(news_df, self.news_filters)
        self.__save_csv(cleaned_news, 'cleaned_news.csv')

        merged_df = merger.integration(cleaned_news, stock_df)
        self.__save_csv(merged_df, 'merged.csv')

        if apply_features and self.stocks_features:
            final_df = self.stocks_features.process(processed_df)
            self.__save_csv(final_df, 'first_data_featured.csv')
        else:
            final_df = processed_df
    
        processed_df = self._apply_filters(merged_df, self.stock_filters)
        self.__save_csv(processed_df, 'final.csv')

        return final_df
    
    
    def __save_csv(self,df, name):
        folder_path = "data/csv"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, name)
        df.to_csv(file_path, index=False)
