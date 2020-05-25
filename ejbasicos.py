# 1)
# Realizar un programa que solicite:
#a)El nombre del alumno.
#b)La cantidad de calificaciones que se promediarán.
#c)Calcular el promedio. Si es mayor o igual a 70 estará aprobado, si no desaprobado.
#d)Preguntarle al usuario, al final del programa, si desea tomar otro alumno.
#e)El programa deberá repetirse mientras la respuesta de "d)" sea "No".

resp = "Si"
while (resp != "No"):
    print("Ingrese el nombre del alumno:")
    nom = input()
    print("¿Cuántas calificaciones va a promediar?")
    nCal = input()
    nCal = int(nCal)
    suma = 0
    for i in range(1, nCal+1):  # Proceso para el ingreso manual de calificaciones
        print("ingrese la", i, "calificación:")
        cal = input()
        cal = float(cal)
        suma = suma + cal
promedio = suma / nCal

if (promedio >= 70):
    print("El alumno", nom, "tiene un promedio de", promedio, "y está aprobado")
else:
    print("El alumno", nom, "tiene un promedio de",
          promedio, "y está desaprobado")

print("¿Desea tomar otro alumno? (Si/No)")
resp = input()

#-------------------------------------------------------------------------------------------------------------

# 2)
#Escribir una función que, dado un número de DNI, retorne "True" si el número es válido o "False" si no lo es.
#-Para que un número de DNI sea válido, debe tener entre 7 u 8 dígitos.


def DNIvalido(dni):
    cantidad = 0
    while dni != 0:
        cantidad = +1  # Al final tendrá la cantidad de dígitos del DNI.
        # Si 45567183//10 => 4556718,3 y me quedo con la parte entera => elimino un nro porque "//" se saca de encima el decimal.
        dni = dni//10
    # Si se dan alguno de estos casos devuelve "TRUE", si no devuelve "False".
    return cantidad == 7 or cantidad == 8

#A esta función la puedo llamar desde el intérprete interactivo de Python.

#-----------------------------------------------------------------------------------------------------------------

# 3)
#Escribir una función que, dado un string, retorne la logitud de la última palabra.
#-Se considera que las palabras están separadas por uno o más espacios.
#-También podría haber espacios al principio o al final del string pasado por parámetro.


#La var. "cantidad" llevará la cant. de caracteres de una palabra (se reiniciará si encontramos una palabra nueva).
#Cuando llegue al final de la cadena, "cantidad" tendrá la cantidad de caracteres de la última palabra.

def lenUltimaPalabra(cadena):
    longitud = len(cadena)
    if longitud == 0:
        return 0
    cantidad = 0
    for i in range(longitud):
        if cadena[i] != " ":
            cantidad += 1
        else:
            if cadena[i] == " " and i < (longitud-1) and cadena[i+1] != " ":
                cantidad = 0  # pongo cantidad en cero porque hay más palabras
    return cantidad

#------------------------------------------------------------------------------------------------------------------

# 4)
#Escribir un programa que permita al usuario obtener un identificador para cada
#uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio,
#indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.

#Precondición: el formato del nombre de los socios será: nombre apellido. Podría
#ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido.
#Si un socio tuviera más de un apellido, el usuario sólo ingresará uno.

#Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar
#al usuario en un bucle hasta que ingrese un DNI correcto.

#Por cada socio se debe imprimir su identificador único, el cual estará formado por:
#el primer nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI. Ejemplo:
#NOMBRE: Alba María Linares
#DNI: 25834911
#Alba7258


#Función que debería ser creada en un archivo aparte "funciones.py"
# recibe un nro, no importa si representa un DNI u otra cosa.
def primerosTresDigitos(numero):
    # mientras el nro tenga 3 dígitos ("999" es el nro más grande de 3 dígitos).
    while numero >= 1000:
        # elimino un nro y me quedo con la parte entera en la línea de abajo.
        numero = numero/10
    return int(numero)  # Me quedo con la parte entera del nro.


#Función que debería ser creada en un archivo aparte "funciones.py"
def obtenerIdentificador(nombre, dni):
    nombre = nombre.strip()  # "strip()" elimina espacios del ppio y el final.
    # Desde el ppio hasta que encuentre el 1er espacio, pero obtiene hasta
    i = nombre[0:nombre.find(" ")]
    #un caracter antes, y es lo que quiero; el "0" podría no haberlo puesto.
    # El nro  de "lenUltima...()" lo paso a STRING para concatenar con el nombre.
    i = i+str(lenUltimaPalabra(nombre))
    i = i+str(primerosTresDigitos(dni))
    return i


#PROGRAMA PPAL

#Debería importar lo de "funciones.py" => " from funciones import * "

nombre = input("Nombre del socio: ")
while nombre != "":
    # DNI es un nro entero, por eso tengo que convertilo a "int".
    dni = int(input("DNI del socio:"))
    # Es lo mismo que "DNIvalido(dni)==False"; función del ejercicio "2)".
    while not (DNIvalido(dni)):
        print("Número inválido")
        dni = int(input("DNI del socio:"))
    identificador = obtenerIdentificador(nombre, dni)
    print("El identificador del socio es: ", identificador)
    # Leo el nombre del siguiente socio; salgo si el usuario sólo apreta "enter".
    nombre = input("Nombre del socio: ")
#----------------------------------------------------------------------------------------------------------------

# 5) RECURSIÓN
# Sumatoria.


def sumatoria(num):
    if num == 1:  # Caso base.
        return 1
    else:
        return num + sumatoria(num-1)  # Si ingreso 4 => 4 + 3 + 2 + 1 = 10


num = int(input("Número de la sumatoria: "))
print(sumatoria(num))

#----------------------------------------------------------------------------------------------------------------

# 6) RECURSIÓN
# factorial.


def factorial(n):
    if n == 1:  # Caso base.
        return 1
    else:
        return n * factorial(n-1)  # Si ingreso 3 => 3 * 2 * 1 = 6


n = int(input("Número del factorial: "))
print(factorial(n))

#----------------------------------------------------------------------------------------------------------------

# 7) RECURSIÓN
# Dado un número, imprimirlo e ir sacándole de a un caracter (de atrás para adelante). En cada paso, ir imprimiendo el
# el número que queda. Repetir esta secuencia hasta que quede un sólo caracter en el número inicial. Luego hacer el proceso inverso.
# e ir incrementando e imprimiendo de a un caracter hasta llegar al número inicial.
# EJEMPLO: si ingreso 4003, entonces:
#4003
#400
#40
#4
#40
#400
#4003


def p_p_n(num):
    if num < 10:  # Caso base (C.B.)
        # Cuando imprime C.B., devuelve ejecución al "print()" posterior al "p_p_n(num//10)". Ese "print()" viene con "num"=40.
        print(num)
        #Luego, devuelve la ejecución al "print()" posterior al "p_p_n(num//10)" del paso anterior. Ese "print()" viene con "num"=400.
        #Luego, lo mismo, y ese "print()" viene con "num"=4003.
    else:
        print(num)
        p_p_n(num//10)
        print(num)


num = int(input("Número del experimento: "))

#----------------------------------------------------------------------------------------------------------------

# 8) RECURSIÓN
# Fibonacci.
#Escribir una función que devuelva el n-término de la secuencia de Fibonacci.

fibonacci_cache = {}  # Dictionary wich will store recent function calls


def fibonacci(n):

    #Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    #If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    #Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    #Cache the value in the dictionary and return it
    fibonacci_cache[n] = value
    return value


for n in range(1, 1001):
    print(n, ":", fibonacci(n))

#----------------------------------------------------------------------------------------------------------------

# 9) RECURSIÓN
# imprimir 1 a 10


def printN(n):
    if n == 0:  # Caso Base
        return
    else:
        printN(n - 1)
        print(n)


printN(10)

#----------------------------------------------------------------------------------------------------------------

# 10) RECURSIÓN
# imprmir de 10 a 1


def printN2(n):
    if n == 0:  # Caso Base
        return
    else:
        print(n)
        printN2(n - 1)


printN2(10)

#----------------------------------------------------------------------------------------------------------------

# 11) RECURSIÓN   ¿¿¿???
# Imprimir de 0 a 99 en una matriz, orientándose por el orden de las columnas. Ejemplo:
# 0 5 10 15 20 [...]
# 1 6 11 16 21 [...]
# 2 7 12 17 22 [...]
# 3 8 13 18 23 [...]
# 4 9 14 19 24 [...]
#[...][...][...][...]


def printCol(i, j):
    if j < 0 or j >= 10:
        return
    else:
        printCol(i, j-1)
        print('', j * 10 + i, end='')  # ????


def printRow(i, j):
    if i < 0 or i >= 10:
        return
    else:
        printRow(i-1, j)
        printCol(i, j)
        print()


printRow(9, 9)  # Matriz 9x9

#----------------------------------------------------------------------------------------------------------------

# 12) RECURSIÓN
# Imprimir de 99 a 0 en una matriz, orientándose por el orden de las columnas. Ejemplo:
# 99 94 89 84 79 [...]
# 98 93 88 83 78 [...]
# 97 92 87 82 77 [...]
# 96 91 86 81 76 [...]
# 95 90 85 80 75 [...]
#[...][...][...][...]


def printCol2(i, j):
    if j < 0 or j >= 10:
        return
    else:
        print('', j * 10 + i, end='')  # ????
        printCol2(i, j-1)


def printRow2(i, j):
    if i < 0 or i >= 10:
        return
    else:
        printRow2(i-1, j)
        print()
        printCol2(i, j)


printRow2(9, 9)  # Matriz 9x9

#----------------------------------------------------------------------------------------------------------------

# 13) RECURSIÓN  ¿¿¿???
# Imprimir el resultado del producto entre los nros de una lista, de manera recursiva.

nums = [2, 10, 4]
print(f"numbers: {nums}")


def calcProduct(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] * calcProduct(n[1:])


productL = calcProduct(nums)
print(f"product: {productL}")

#----------------------------------------------------------------------------------------------------------------

# 14) RECURSIÓN
# Imprimir una lista (¿array en realidad?) de atrás para adelante recursivamente. (imprimir el antes y el después)


def reverseList(data, low, high):  # "low" y "high" dos las dos posiciones iniciales del array
    if low < high:
        newLow = data[low]
        data[low] = data[high]
        data[high] = newLow
        reverseList(data, low + 1, high - 1)


#MAIN
numberss = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Antes: {numberss}")

reverseList(numberss, 0, len(numberss) - 1)

print(f"Después: {numberss}")

#----------------------------------------------------------------------------------------------------------------

# 15) RECURSIÓN
# Hacer la suma, recursivamente, de n-términos de una lista.


def sumNumbers(data, n):
    if n <= 0 or n > len(data):  # Caso Base.
        return 0
    else:
        return sumNumbers(data, n-1) + data[n-1]


#MAIN
numbersss = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Numbers: {numbersss}")

nTerms = 5
summ = sumNumbers(numbersss, nTerms)

print(f"Sum of first {nTerms}: {summ}")

#----------------------------------------------------------------------------------------------------------------

