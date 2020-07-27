#Ejercicio#
#Un uso muy común de las listas es el de representar tableros con ellas.
# Para eso se utilizan listas de listas, de este modo, se puede entender una lista de listas como una matriz.
# Así, para acceder a un elemento i,j de la matriz, se debe acceder a: matriz[i][j].
#Para ese ejercicio se dispone de un tablero de buscaminas especial,
# donde lo único que hay es bombas en las distintas posiciones.
# Este tablero es de la forma:

#Donde las X representan las bombas. Ese tablero, en representación matricial de Python,
# donde se utilizan strings con un espacio: " " y "X" para representar espacios libres y bombas respectivamente,
# viene dado por:
tablero=[['X',' ',' ',' ',' ','X','X',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ','X','X',' ',' ','X','X',' '],
         [' ',' ','X',' ',' ',' ',' ',' ',' '],
         [' ',' ','X',' ',' ',' ','X',' ','X'],
         ['X',' ',' ','X',' ',' ',' ','X',' '],
         ['X',' ',' ',' ','X',' ','X',' ',' '],
         [' ',' ','X',' ',' ','X',' ',' ','X'],
         [' ',' ','X',' ','X',' ',' ','X',' ']
         ]
for row in tablero:
    for elem in row:
        print(elem, end=' ')
    print()
print(tablero)

#El objetivo de este ejercicio, es que programes una función buscaminas que reciba como argumento a una matriz tablero y dos coordenadas i, j,
# y que entregue la cantidad de bombas que rodean a esa posición.
#Por ejemplo, si la el tablero dado es el representado en la tabla,
# y la posición viene dada por i=0 y j=0, tu función debe retornar el valor 2, ya que hay dos bombas rodeándola, en (0,1) y (1,0).
#Por otro lado, si el tablero es el mismo, y las coordenadas son i=1, j=1, tu función debe retornar 4, pues hay bombas rodeando la posición en (1,0), en (0,1), en (2,1) y en (2,2).
#Hint: recuerda que el tablero puede ser de un tamaño arbitrario y que al escribir posiciones más grandes que ese tamaño o menores que 0, tu programa arrojará error.
i=0
j=6
def buscaminas(tablero,i,j):
    filas=len(tablero)
    columnas=len(tablero)
    x = 0
    y = 0
    for x in range(filas):
        for y in range(columnas):
            n=0
            if i > 0 and j > 0 and tablero[i - 1][j - 1]=='X':
                n += 1
            if i>0 and tablero[i-1][j]=='X':
                n += 1
            if i > 0 and j < columnas - 1 and tablero[i - 1][j + 1] == 'X':
                n += 1
            if j < columnas - 1 and tablero[i][j + 1] == 'X':
                n += 1
            if i < filas - 1 and j < columnas - 1 and tablero[i + 1][j + 1] == 'X':
                n += 1
            if i < filas - 1 and tablero[i + 1][j] == 'X':
                n += 1
            if i < filas - 1 and j > 0 and tablero[i + 1][j - 1] == 'X':
                n += 1
            if i>=0 and j>0 and tablero[i][j - 1] == 'X':
                n += 1
    return n
print(buscaminas(tablero,i,j))



