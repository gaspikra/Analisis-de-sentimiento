import pandas as pd
import sys
sys.path.append('src')

from steps.feature_engineering.sentimient_classification import SentimentClassification

data = pd.DataFrame({
    'real_news': ['Mastercard announces new partnership', None, 'Market downturn affects stocks'],
    'ma': [0, 1, 0]
})

classifier = SentimentClassification()
result = classifier.process(data)

print("Resultado:")
print(result)
print("Columnas:", result.columns.tolist())