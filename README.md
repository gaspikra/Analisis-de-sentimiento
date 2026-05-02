# Mastercard Stock Analysis Pipeline

El proyecto trata sobre prediccion del valor de las acciones, en este caso, analizamos a MASTERCARD (MA). Por un lado, para el analisis fundamental utilicé
una API para obtener noticias financieras viejas sobre la compañia. Para el analisis tecnico saqué los los datos historicos de yfinance.
En base a su resultado, se puede saber si esta accion va a subir o no, y tomar una desición con esta información.

## Tecnologias

* **Lenguaje:** Python

* **Librerias:** Pandas, Numpy, Pandas-ta, Requests, Transformers, Torch, Yfinance, Langdetect, Python-dotenv
* **Modelos:** ProsusAI/finbert,


## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **src/**: Contiene el código principal del pipeline.
  - **pipeline.py**: Clase principal del pipeline que coordina los pasos.
  - **data_getter/**: Módulo para obtener datos usando el patrón Strategy.
    - **IStrategy.py**: Interfaz para estrategias de obtención de datos.
    - **strategies/**: Implementaciones concretas (historical_news_data.py, historical_values_data.py).
  - **steps/**: Pasos del pipeline divididos en categorías.
    - **clean_data/**: Filtros para limpiar datos de noticias y stocks.
    - **feature_engineering/**: Ingeniería de características, incluyendo clasificación de sentimientos.
    - **integration/**: Integración de datos de noticias y stocks.
- **data/**: Carpeta para datos.
  - **csv/**: Archivos CSV de entrada y salida.
- **lab/**: Notebooks y scripts para experimentación y procesamiento de datos.
  - **clean/**: Notebooks para limpieza de datos.
  - **data_procesing/**: Notebooks para procesamiento de datos.
  - **news/**: Scripts relacionados con noticias.
  - **trash/**: Código obsoleto o de prueba.
- **test/**: Pruebas y notebooks de testing.
- **main.py**: Punto de entrada para ejecutar el pipeline.
- **pyproject.toml**: Configuración de dependencias y proyecto.
- **Dockerfile**: Para contenerización.
- **README.md**: Este archivo.


## Orden del Pipeline

El pipeline sigue un orden específico para procesar los datos de noticias y stocks de Mastercard. Los pasos se ejecutan en secuencia para asegurar la integridad y calidad de los datos:

1. **Obtención de Datos**: Se cargan los datos históricos de noticias y valores de acciones desde archivos CSV.
2. **Filtros de Noticias**:
   - **SelectData**: Selecciona y estructura los datos relevantes de noticias (título, descripción, fecha, sentimientos para MA, AXP, COF).
   - **EnglishNews**: Filtra noticias en inglés.
   - **TransformValues**: Transforma valores de sentimientos.
   - **SelectEnglishNews**: Asegura que solo se procesen noticias en inglés.
   - **SentimentClassification**: Clasifica el sentimiento de las noticias usando FinBERT, procesando textos en lotes para evitar uso excesivo de memoria.
3. **Integración de Datos**: Combina datos de noticias y stocks usando DataIntegration.
4. **Ingeniería de Características Técnicas** (opcional): Aplica agregaciones como EMA (8, 21), MMA (200) y target.
5. **Filtros de Stocks**:
   - **NewsFillNaTreatment**: Trata valores nulos en datos de noticias.
   - **MeaninglessColumnsTreatment**: Elimina columnas innecesarias.
   - **NaNTreatment**: Trata valores nulos en datos de stocks.

Este orden garantiza que los datos se limpien y enriquezcan progresivamente antes de la integración final.


## Chalenges

Por un lado, recibir datos de distintas fuentes era un desafio ya que estos tienen que ser procesados para que el modelo pueda procesarlos y realizar predicciones.
Entonces diseñé una estructura utilizando el patron Pipeline para ordenar el paso a paso. Para obtener puntuaciones de las noticias utilicé un modelo pre-entrenado FinBERT para que me de dichos scores.

Primero para obtener los datos de distintas fuentes, use el patron Strategy, una estrategia por cada fuente, asi me evito tener que modificar el codigo principal y simplemente creo una nueva estrategia por cada vez que quiera agregar datos de otras fuentes, manteniendo la escalabilidad y orden del codigo.
Luego cuando dockerize el pipeline, la imagen era bastante pesada, entonces tenia que elegir mejor la forma de implementar las librerias para hacer la imagen lo mas liviana posible, logrando pasar de un 7Gb a 1,29Gb. La imagen es para mantener un mejor versionado del codigo, y que este pueda funcionar en cualquier lugar sin tener que andar revisando dependencias.
Luego, tuve que abandonar el proyecto para estudiar para mis examenes universitarios, aproximadamente 1 mes y medio (si, muchos parciales y 2 finales). Cuando volví, no recordaba los pasos del pipeline, y fallaba en algunas secciones que me costaba mucho tiempo encontrar. Es por eso, que decidí Loggear todo el Pipeline, de esta manera es mas facil ver donde esta el error, y atacar especificamente ese lugar, ahorrandome mucho tiempo :D.
En el momento de ejecutar mi proyecto, mi computadora se relentizaba muchiismo, miraba los procesos y se ocupaban 15Gb de las 16 que tengo... asi que tenia que solucionarlo de alguna manera, entonces es cuando me di cuenta que tenia que procesar por lotes los textos de las noticias para evitar el uso excesivo de memoria.
