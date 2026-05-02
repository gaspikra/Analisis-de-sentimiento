from steps.clean_data.ICleanDataFilter import ICleanDataFilter


class NewsFillNaTreatment(ICleanDataFilter):
    def process(self, data):
        cols = ['ma','axp','cof', 'news_scores']
        data['has_news'] = data['news_scores'].notna().astype(int)
        data[cols] = data[cols].fillna(0)
        return data
