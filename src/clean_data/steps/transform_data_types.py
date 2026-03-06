from clean_data.ICleanDataFilter import ICleanDataFilter
import pandas as pd

class TransformDateTypes(ICleanDataFilter):
    def process(self, data):
        final_df = data.copy()
        final_df['date'] = pd.to_datetime(final_df['date'])
        final_df['date'] = final_df['date'].dt.normalize()
        return final_df