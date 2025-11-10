import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Cargar dataset de ejemplo
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(" Dataset original cargado correctamente")
print(df.head())

# --- 1 Eliminación de duplicados ---
df = df.drop_duplicates()

# --- 2 Manejo de valores nulos ---
# Reemplazar valores nulos en 'Age' con la media
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Reemplazar valores nulos en 'Embarked' con el valor más frecuente
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# --- 3 Codificación de variables categóricas ---
label_cols = ['Sex', 'Embarked']
encoder = LabelEncoder()
for col in label_cols:
    df[col] = encoder.fit_transform(df[col])

# --- 4 Normalización de datos numéricos ---
numeric_cols = ['Age', 'Fare']
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# --- 5 Exportar dataset procesado ---
df.to_csv('titanic_preprocesado.csv', index=False)

print(" Preprocesamiento completado con éxito.")
print(df.head())
