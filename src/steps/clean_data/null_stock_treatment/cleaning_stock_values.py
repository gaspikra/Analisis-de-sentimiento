from steps.clean_data.ICleanDataFilter import ICleanDataFilter


class NaNTreatment(ICleanDataFilter):
    def process(self, data):
        return data.dropna()