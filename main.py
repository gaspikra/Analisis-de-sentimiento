import pandas as pd
import os

class MastercardDataPipeline:
    def __init__(self):
        self.filter = []
        self.data_strategy = None
    def set_data_strategy(self, strategy):
        self.data_strategy = strategy

    def obtain_data(self, ticker, start, end):
        results = self.data_strategy.obtain_data(ticker, start, end)
        data = results["results"]
        data_frame = pd.DataFrame(data)
        self.__save_csv(data_frame, results['csv name'])
        return data_frame, f"{results['csv name']}.csv"

    def add_filter(self, filter_obj):
        self.filter.append(filter_obj)
        return self

    def clean_data(self, data):
        result = data
        for f in self.filter:
            result = f.process(result)
        self.__save_csv(result, 'final.csv')
        return result


    def __save_csv(self,df, name):
        folder_path = "data/csv"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, name)
        df.to_csv(file_path, index=False)

        


    
