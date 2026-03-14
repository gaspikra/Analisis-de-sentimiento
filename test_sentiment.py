import pandas as pd
import sys
sys.path.append('src')

from steps.feature_engineering.sentimient_classification import SentimentClassification

# Datos de prueba
data = pd.DataFrame({
    'real_news': ['Mastercard announces new partnership', None, 'Market downturn affects stocks'],
    'ma': [0, 1, 0]
})

# Instanciar y procesar
classifier = SentimentClassification()
result = classifier.process(data)

print("Resultado:")
print(result)
print("Columnas:", result.columns.tolist())