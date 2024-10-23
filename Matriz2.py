import numpy as np

# 1. Producto escalar de vectores
def producto_escalar(v1, v2):
  """Calcula el producto escalar de dos vectores.

  Args:
    v1: Un vector numpy.
    v2: Un vector numpy.

  Returns:
    El producto escalar de los dos vectores.
  """
  return np.dot(v1, v2)

# Ejemplo de uso para el producto escalar
n = int(input("Ingrese la longitud de los vectores: "))
v1 = np.random.rand(n)
v2 = np.random.rand(n)
print("Vector 1:", v1)
print("Vector 2:", v2)
producto = producto_escalar(v1, v2)
print("El producto escalar de los vectores es:", producto)

# 2. Operaciones con matrices
def sumar_matrices(A, B):
  """Suma dos matrices.

  Args:
    A: Una matriz numpy.
    B: Una matriz numpy.

  Returns:
    La suma de las dos matrices.
  """
  return A + B

def multiplicar_matriz_escalar(A, escalar):
  """Multiplica una matriz por un escalar.

  Args:
    A: Una matriz numpy.
    escalar: Un escalar.

  Returns:
    El producto de la matriz por el escalar.
  """
  return escalar * A

def multiplicar_matrices(A, B):
  """Multiplica dos matrices.

  Args:
    A: Una matriz numpy.
    B: Una matriz numpy.

  Returns:
    El producto de las dos matrices.
  """
  return np.dot(A, B)

# Ejemplo de uso para las operaciones con matrices
filas_A = int(input("Ingrese el número de filas de la matriz A: "))
columnas_A = int(input("Ingrese el número de columnas de la matriz A: "))
A = np.random.rand(filas_A, columnas_A)
print("Matriz A:", A)

filas_B = int(input("Ingrese el número de filas de la matriz B: "))
columnas_B = int(input("Ingrese el número de columnas"))