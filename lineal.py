import numpy as np
import pandas as pd

# Datos de la tabla
data = {'x1': [1, 1, 2, 3, 1, 2, 3, 3],
        'x2': [-1, 0, 0, 1, 1, 2, 2, 0],
        'y': [1.6, 3, 1.1, 1.2, 3.2, 3.3, 1.7, 0.1]}

# Crear un DataFrame de pandas
df = pd.DataFrame(data)

# Calcular la regresión lineal
X = df[['x1', 'x2']]
y = df['y']
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)

# Coeficientes de la regresión lineal
intercept = model.intercept_
coefficients = model.coef_

# Coeficiente de correlación
correlation = np.corrcoef(X, y)[0, 1]

# Imprimir los resultados
print("Intersección:", intercept)
print("Coeficientes:", coefficients)
print("Coeficiente de correlación:", correlation)

# Ecuación de la función lineal
equation = f"y = {intercept:.2f} + {coefficients[0]:.2f}x1 + {coefficients[1]:.2f}x2"
print("Ecuación de la función lineal:", equation)