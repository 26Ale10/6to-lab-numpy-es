# 1. Importa el paquete NUMPY bajo el nombre np.

# [tu código aquí]
import numpy as np

# 2. Imprime la versión de NUMPY y la configuración.

# [tu código aquí]
print(np.version.version)

# Imprimir información de configuración


# 3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?

# [tu código aquí]
# La primera opción: genero dos matrices de 3 filas y 5 columnas con números aleatorios del 0-100
a = np.random.randint(0, 100, (2, 3, 5))


# La segunda opción: genero una matriz de 2 x 3 x 5 con números aleatorios del 0-1
a2 = np.random.rand(2, 3, 5)


# la tercera opción: genero matriz 2 x 3 x 5 con número aleatorios entre 0-1
a3 = np.random.random_sample((2, 3, 5))

# 4. Imprime a.

# [tu código aquí]
print(f"Esta es matriz a:\n{a}\n")

# 5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
# Asigna el array a la variable "b"

# [tu código aquí]

b = np.ones((5, 2, 3))

# 6. Imprime b.

# [tu código aquí]

print(f"Este es el array b:\n{b}\n")

# 7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?

# [tu código aquí]

if a.size == b.size:
    print(
        f"\nel tamaño de 'a' y 'b' es el mismo, ambas tienen un tamaño de {a.size}\n")
else:
    print(f"""\nel tamaño de 'a' y 'b' es diferente, el tamaño de 'a' es :
          {a.size}, mientras que el de 'b' es de {b.size}\n""")

# 8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?

# [tu código aquí]

""" no es posible sumar a y b
        #sum_ab = np.add(a, b)
        #print(sum_ab)
        sum_ab = np.add(a, b)
        #ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3)
¿Por qué pasa esto?

Las reglas de "broadcasting" en NumPy determinan como pueden operar  matrices de diferentes formas. Para que dos matrices sean compatibles, tienen que cumplir una de estas condiciones:

Las dimensiones deben ser iguales: Las matrices deben de tener la misma forma.
Una de las dimensiones debe ser 1: Si una dimensión en una de las matrices es 1, se replicará esa dimensión para que sea compatible con la otra matriz.
Una de las dimensiones debe ser 0: Si una dimensión en una de la matrices tiene un tamaño de 0, esa dimensión desaparecerá."""


# 9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".

# [tu código aquí]
c = np.copy(b)
c = np.transpose(c, (1, 2, 0))
print(f"Esta es matriz c:\n{c}\n")
# 10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?

# [tu código aquí]

d = np.add(a, c)
print(f"Esta es matriz d:\n{d}\n")

# 11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.

# [tu código aquí]
print(f"Esta es matriz a:\n{a}\n")
print(f"Esta es matriz d:\n{d}\n")

# 12. Multiplica a y c. Asigna el resultado a e.

# [tu código aquí]

e = np.multiply(a, c)
print(f"Este es el resultado de la multiplicación de a*c:\n{e}\n")

# 13. ¿Es e igual a a? ¿Por qué sí o por qué no?

# [tu código aquí]

if a.all == e.all:
    print("\nSi, 'a' y 'e' son iguales\n")
else:
    print("\nNo, 'a' y 'e' no son iguales\n")

# 14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"
# [tu código aquí]
d_max = d.max()
d_min = d.min()
d_mean = d.mean()

print(f"""El valor máximo de 'd' es: {d_max}
El valor mínimo de 'd' es: {d_min}
El valor medio de 'd' es: {d_mean}""")

# 15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío "f" con la misma forma (es decir, 2x3x5) que d usando `np.empty`.

# [tu código aquí]
f = np.empty((2, 3, 5))
print(f"\nEsta es la original 'f' {f}\n")

"""
#16. Rellena los valores en f. Para cada valor en d, si es mayor que d_min pero menor que d_mean, asigna 25 al valor correspondiente en f.
Si un valor en d es mayor que d_mean pero menor que d_max, asigna 75 al valor correspondiente en f.
Si un valor es igual a d_mean, asigna 50 al valor correspondiente en f.
Asigna 0 al valor correspondiente(s) en f para d_min en d.
Asigna 100 al valor correspondiente(s) en f para d_max en d.
Al final, f debería tener solo los siguientes valores: 0, 25, 50, 75 y 100.
Nota: no necesitas usar Numpy en esta pregunta.
"""

# [tu código aquí]
for i, submatriz in enumerate(d):
    for j, fila in enumerate(submatriz):
        for k, dato in enumerate(fila):
            if d_min < d[i][j][k] < d_mean:
                f[i][j][k] = 25
            elif d_mean < d[i][j][k] < d_max:
                f[i][j][k] = 75
            elif d[i][j][k] == d_mean:
                f[i][j][k] = 50
            elif d[i][j][k] == d_min:
                f[i][j][k] = 0
            elif d[i][j][k] == d_max:
                f[i][j][k] = 100

print(f"\nEsta es la nueva 'f' \n{f}\n")

"""#17. Imprime d y f. ¿Tienes el f esperado?
Por ejemplo, si tu d es:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Tu f debería ser:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])"""

# [tu código aquí]
print(f"\nEsta es la matriz 'd':\n{d}\n")
print(f"\nEsta es la matriz 'f':\n{f}\n")

"""
#18. Pregunta de bonificación: en lugar de usar números (es decir, 0, 25, 50, 75 y 100), ¿cómo usar valores de cadena
("A", "B", "C", "D" y "E") para etiquetar los elementos del array? Esperas el resultado sea:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
De nuevo, no necesitas Numpy en esta pregunta.
"""
f2 = np.copy(f)
# [tu código aquí]
aa = "A"
for i, submatriz in enumerate(d):
    for j, fila in enumerate(submatriz):
        for k, dato in enumerate(fila):
            if d_min < d[i][j][k] < d_mean:
                f2[i][j][k] = aa
            elif d_mean < d[i][j][k] < d_max:
                f2[i][j][k] = aa
            elif d[i][j][k] == d_mean:
                f2[i][j][k] = aa
            elif d[i][j][k] == d_min:
                f2[i][j][k] = aa
            elif d[i][j][k] == d_max:
                f2[i][j][k] = aa

print(f"\nEsta es la nueva 'f' \n{f2}\n")
