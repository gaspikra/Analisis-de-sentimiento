import pandas as pd

class MastercardDataPipeline:
    clean_strategy = None
    data_strategy = None 
    api_key = None


    def __init__(self, api_key):
        self.api_key = api_key

    def set_data_strategy(self, strategy):
        self.data_strategy = strategy

    def set_data_clean_strategy(self):
        pass

    def obtain_data(self, ticker, start, end):
        results = self.data_strategy.obtain_data( self.api_key ,ticker, start, end)
        data = results["results"]
        data_frame = pd.DataFrame(data)
        self.__save_scv(data_frame, results["csv name"])

    def clean_data(self, archive_name):
        data = self.__read_data(archive_name)
    


























    def __read_data(self, archive):
        return pd.read_csv(archive)


    def __save_scv(self,df, name):
        df.to_csv(f"../data/csv/{name}")

        


    
