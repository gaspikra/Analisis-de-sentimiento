from steps.clean_data.ICleanDataFilter import ICleanDataFilter


class MeaninglessColumnsTreatment(ICleanDataFilter):
    def process(self, data):
        result = data.drop(columns = ["Open", "High", "Low", "Close", "Adj Close", "Stock Splits", "Date", "Dividends"], axis = 1)
        return result
