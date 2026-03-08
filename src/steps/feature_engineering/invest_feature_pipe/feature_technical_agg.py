from steps.feature_engineering.I_featuring import IFeaturing


class FeatureAgregation(IFeaturing):
    def __init__(self):
        self.features = []

    def process(self, data):
        for feature in self.features:
            result = feature.process(data)
        return result
    
    def add_feature(self, feature):
        self.features.append(feature)



        
