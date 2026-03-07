from steps.clean_data.ICleanDataFilter import ICleanDataFilter
import pandas as pd

class TransformDateTypes(ICleanDataFilter):
    def __init__(self, column_name):
        self.column_name = column_name
    def process(self, data):
        final_df = data.copy()
        final_df[self.column_name] = pd.to_datetime(final_df[self.column_name])
        final_df[self.column_name] = final_df[self.column_name].dt.normalize()
        return final_df