# Solicita al usuario la longitud de los vectores
n = int(input("Ingrese la longitud de los vectores: "))

# Crea dos vectores vacíos
vector1 = []
vector2 = []

# Solicita al usuario que ingrese los elementos del primer vector
print("Ingrese los elementos del primer vector:")
for i in range(n):
    vector1.append(float(input(f"Elemento {i + 1}: ")))

# Solicita al usuario que ingrese los elementos del segundo vector
print("Ingrese los elementos del segundo vector:")
for i in range(n):
    vector2.append(float(input(f"Elemento {i + 1}: ")))

# Calcula el producto escalar de los dos vectores
producto_escalar = 0
for i in range(n):
    producto_escalar += vector1[i] * vector2[i]

# Imprime el producto escalar
print(f"El producto escalar de los dos vectores es: {producto_escalar}")