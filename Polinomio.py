import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([-0.9, 0, 2, 4.5, 8.3, 13, 18])

# Ajustar un polinomio de segundo grado
coef = np.polyfit(x, y, 2)
poly = np.poly1d(coef)

# Calcular el coeficiente de correlación
r = np.corrcoef(x, y)[0, 1]

# Mostrar los resultados
print(f"Ecuación del polinomio: {poly}")
print(f"Coeficiente de correlación: {r}")

# Graficar los datos y el polinomio ajustado
plt.plot(x, y, 'o', label="Datos")
plt.plot(x, poly(x), '-', label="Polinomio ajustado")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ajuste de un polinomio de segundo grado')
plt.legend()
plt.show()