"""
FOR variable IN secuencia:
    #bloque a repetir

WHILE condición:
     #bloque a repetir

DEF identificador(parametros):   #Para secuencia ordenada de elementos.
    #cuerpo de la función
    #valor de retorno

"""
7%2
# 7%(5//2) = 1  ==> "//" me quedo con la parte ENTERA; "%" me quedo con el RESIDUO
#
#
#
#
#
#
#
# ----------------------------------------------------------------------------------
# 1)
# Realizar un programa que solicite:
#a)El nombre del alumno.
#b)La cantidad de calificaciones que se promediarán.
#c)Calcular el promedio. Si es mayor o igual a 70 estará aprobado, si no desaprobado.
#d)Preguntarle al usuario, al final del programa, si desea tomar otro alumno.
#e)El programa deberá repetirse mientras la respuesta de "d)" sea "No".

from random import *
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
        cantidad += 1  # Al final tendrá la cantidad de dígitos del DNI.
        # Si 45567183//10 => 4556718,3 y me quedo con la parte entera => elimino un nro porque "//" se saca de encima el decimal.
        dni = dni//10
    # Si se dan alguno de estos casos devuelve "TRUE", si no devuelve "False".
    return cantidad == 7 or cantidad == 8

DNIvalido(12345678)

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

lenUltimaPalabra("se viene aaaaaaca")

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
    # mientras el nro NO tenga 3 dígitos ("999" es el nro más grande de 3 dígitos).
    while numero >= 1000:
      # elimino un nro y me quedo con la parte entera en la línea de abajo.
        numero = numero//10
    return int(numero)  # Me quedo con la parte entera del nro.


#Función que debería ser creada en un archivo aparte "funciones.py"
def obtenerIdentificador(nombre, dni):
    nombre = nombre.strip()  # "strip()" elimina espacios del ppio y el final.
    # Desde el ppio hasta que encuentre el 1er espacio, pero obtiene hasta
    # un caracter antes, y es lo que quiero; el "0" podría no haberlo puesto.
    i = nombre[0:nombre.find(" ")]
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

# 13) RECURSIÓN
# Imprimir, de manera recursiva, el resultado del producto entre los nros de una lista.

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
# Imprimir una lista de atrás para adelante recursivamente. (imprimir el antes y el después)


def reverseList(data, low, high):  # "low" y "high" las dos posiciones iniciales de la lista
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

# 16)
# Usar un WHILE para mostrar los nros del 1 al 100.

i = 1
while(i <= 100):
    print(i)
    i += 1
print("Fin del bucle")

#----------------------------------------------------------------------------------------------------------------

# 17)
# Usar un FOR para mostrar los nros del 1 al 100.

for i in range(1, 101):
    print(i)

#----------------------------------------------------------------------------------------------------------------

# 18)
# Mostrar los caracteres de la cadena "Hola mundo".

for i in "Hola mundo":
    print(i)

#----------------------------------------------------------------------------------------------------------------

# 19)
# Mostrar los nros PARES del 1 al 100.

# 1°forma.
for i in range(1, 101):
    if((i % 2) == 0):
        print(i)
    print("")

# 2°forma,
print("2°forma")
for i in range(2, 101, 2):
    print(i)

#----------------------------------------------------------------------------------------------------------------

# 20)
# Generar un RANGO entre 0 y 10.

rango = list(range(10))
print(rango)

#----------------------------------------------------------------------------------------------------------------

# 21)
# Generar un NÚMERO entre 5 y 10.

rAngo = list(range(5, 10))
print(rAngo)

#----------------------------------------------------------------------------------------------------------------

# 22)
# Generar un RANGO de 10 a 0.

Rango = list(range(10, 0, -1))  # "-1" mustra la regresión.
print(Rango)

#----------------------------------------------------------------------------------------------------------------

# 23)
# Generar un rango de 0 a 10 y de 15 a 20, incluidos el 10 y el 20.

rango1 = list(range(0, 11))
rango2 = list(range(15, 21))
union = rango1 + rango2
print(union)

#----------------------------------------------------------------------------------------------------------------

# 24)
# Generar un rango desde 0 hasta la longitud de la cadena "Hola mundo".

rango24 = list(range(0, len("Hola mundo")))
print(rango24)

#----------------------------------------------------------------------------------------------------------------

# 25)
# Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas y con los 2 primeros caracteres
# intercambiados. Por ejemplo, "hola mundo" pasaría a "mula hondo".

cadena1 = input("ingrese 1°cadena: ")
cadena2 = input("ingrese 2°cadena: ")
print(cadena2[:2] + cadena1[2:] + "" + cadena1[:2] + cadena2[2:])
# "[:2]" = empieza en el inicio (ext. cerrado) y termina en el 2do caracter (ext. abierto); "[2:]" = arranca desde el 3er caracter.
# Esto se basa en el operador slice (rodaja) cuya sintaxis general es: "iterable [ inicio : fin : paso ]"

#----------------------------------------------------------------------------------------------------------------

# 26)
# Pide una cadena e indica si es o no un palíndromo (que se lea igual de izq. a derecha como de derecha a izq.).

cad1 = input("ingrese una cadena: ")
# Se recorre hacia atrás y se invierte la cadena por no incluir inicio ni final.
cadena_al_reves = cad1[::-1] #el último caracter de la cadena, cuando voy hacia atrás, es -1, el anteúltimo -2 y así.
print(cadena_al_reves)
if(cad1 == cadena_al_reves):
    print("Es palíndromo")
else:
    print("No es palíndromo")

#----------------------------------------------------------------------------------------------------------------

# 27)
# Adivina el nro entre 1 y 100.


def generaNroAleatorio(min, max):
    try:
        if min > max:
            aux = min
            min = max
            max = aux
        # Devuelve un nro random del par ordenado, incluyendo extremos.
        return randint(min, max)
    except TypeError:
        print("Debes escribir números")
        return -1  # ¿¿¿???

#MAIN
nro_buscado = generaNroAleatorio(1, 100)
encontrado = False
intentos = 0

while not encontrado:
    nro_usuario = int(input("Introduce el número buscado: "))
    if nro_usuario > nro_buscado:
        print("El número que buscas es menor")
        intentos = intentos + 1
    elif nro_usuario < nro_buscado:
        print("El número que buscas es mayor")
        intentos = intentos + 1
    else:
        encontrado = True
        print("Has acertado, el número correcto es", nro_usuario, "te ha llevado", intentos,
              "intentos ganar este juego")

#----------------------------------------------------------------------------------------------------------------

# 28)
# Definir una función "max()" que tome como argumento dos números y devuelva el mayor de ellos.


def max(n1, n2):
    if n1 < n2:
        print(n2)
    elif n1 > n2:
        print(n1)
    else:
        print("Son iguales")

#----------------------------------------------------------------------------------------------------------------

# 29)
# Definir una función "max_de_tres()" que tome tres nros como argumentos y devuelva al mayor de ellos.


def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 < n3:
        print(n1)
    elif n1 < n2 and n2 > n3:
        print(n2)
    elif n1 < n3 and n2 < n3:
        print(n3)
    else:
        print("Son iguales")

#----------------------------------------------------------------------------------------------------------------

# 30)
# Definir una función que calcule la longitud de una lista o una cadena dada.

def largo_cadena(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

#----------------------------------------------------------------------------------------------------------------

# 31)
# Escribir una función que tome un carácter y devuelva "True" si es una vocal, de lo contrario "False".

x=input("Letra: ")
def es_vocal (x):
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        return True
    elif x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
        return True
    else:
        return False

#otra forma:

x=input("Letra: ")
def es_vocal (x):
    if x.lower() in "aeiou":
        return True
    else:
        return False

#----------------------------------------------------------------------------------------------------------------

# 32)
# Definir una función "inversa()" que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando"
# debería devolver la cadena "odnaborp yotse".

def inversa(cadena32):
    invertida=""
    cont = len(cadena32)
    indice = -1 # Tiene que ser -1 para posicionarse en el final de la cadena
    while cont >= 1:
        invertida += cadena32[indice]
        indice = indice + (-1) #Recorre de atrás para adelante
        cont -= 1
    return invertida

#----------------------------------------------------------------------------------------------------------------

# 33)
# Definir una función "es_palindromo()" que reconozca palíndromos. Ejemplo: "es_palíndromo("radar")" devolvería TRUE.

#Defino la función del punto "32)"

def es_palindromo (cadena33):
    p_invertida = inversa(cadena33)
    indice = 0
    cont33 = 0
    for i in range (len(cadena33)):
        if p_invertida[indice] == cadena33[indice]:
            indice += 1
            cont33 += 1
        else:
            print("False")
            break
    if cont33 == len(cadena33): #Si el contador = cantidad de letras de la cadena es porque todas las letras son iguales
    print("True") # ó "return True"


#----------------------------------------------------------------------------------------------------------------

# 34)
# Definir una función "superposicion()" que tome dos listas y devuelva "true" si tienen al menos un miembro en común
# o False en caso contratrio. Escribir la función usando el bucle FOR anidado.

def superposicion(lista1,lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False

#----------------------------------------------------------------------------------------------------------------

# 35)
# Definir un histograma "procedimiento()" que tome una lista de nros entros e imprima un histograma en pantalla.
# Ejemplo: procedimiento([4,9,7]) debería imprimir lo siguiente:
# ****
# *********
# *******

def procedimiento (lista):
    for i in lista:
        print(i*"x")

#----------------------------------------------------------------------------------------------------------------

# 36) ¿Está bien?
# Escribir la función "mas_larga()" que tome una lista de palabras y devuelva la más larga.


def mas_larga(lista):
    inicio36 = 0
    for i in lista:
        if len(i) > inicio36:
        inicio36 = len(i)
    return inicio36

#----------------------------------------------------------------------------------------------------------------

# 37)
# Escribir la función "filtrar_palabras()" que tome una lista de palabras, un entero n y devuelva las palabras que
# tengan más de n caracteres.

def filtrar_palabras(lista,n):
    for i in lista:
        if len(i) > n:
            print(i)

#----------------------------------------------------------------------------------------------------------------

# 38)
# Escribir un programa que diga al usuario que ingrese una cadena. El programa debe evaluar la cadena y decir cuántas
# letras mayúsculas tiene.

#-*- Codification: utf-8 -*

def c_mayus (cadena):
    cont = 0
    for i in cadena:
        if i != i.lower(): # "lower()" convierte una cadena en minúsculas.
            cont += 1

print("La cadena tiene",cont,"mayuscula(s)")

#----------------------------------------------------------------------------------------------------------------

# 39) ¿¿¿???
# Construir un pequeño programa que convierta números binarios en enteros.

def aDecimal(numeroBin):
    decimal = 0
    exp = len(numeroBin)-1  # ¿Por qué -1?
    for i in numeroBin:
        decimal += (int(i) * 2**(exp))   # ¿2**(exp)?
        exp = exp - 1
    return decimal


#----------------------------------------------------------------------------------------------------------------

# 40)
# Definir una lista con un conjunto de nombres. Imprimir la cantidad que comienza con la letra "a". También se puede
# dar a elegir al usuario la letra que quiera buscar.

def main():
    x = int(input("¿Cuántos nombres quiere ingresar?: "))
    lista = []
    for i in range(x):
        a = input("ingrese el nombre: ")
        list.append(a) #agrega al FINAL de la lista.
    
    print("")
    comienzo = input("¿Con qué letra empieza el nombre?: ")
    cont = 0
    for i in lista:
        if i[0] == comienzo.lower() or i[0] == comienzo.upper():
            cont += 1
    return cont

#----------------------------------------------------------------------------------------------------------------

# Quiero el caracter de la última posición de una cadena.

# c=cadena de 8 caracteres
c="buen dia"
c[len(c)-1] #Devuelve 'a'.

# ó

c[-1:]

#----------------------------------------------------------------------------------------------------------------

"casa" < "cosa" #porque con strings hace la comparación usando de referencia ASCII. Como o=111 y a=97 => es más grande.

#----------------------------------------------------------------------------------------------------------------

"hola"[1+1] #Da igual a "L" porque obtengo el caracter de la posición nro 2.

#----------------------------------------------------------------------------------------------------------------

#Manejo de STRINGS.

cadena3="programación en python"
cadena3.find("python") #Devuelve 16; "find()" indica DÓNDE empieza una sub-cadena. Además devuelve un ÚNICO valor.
cadena3.find("p") # Devuelve 0; devuelve la 1ra "p" que encuentre.
cadena3.find("z") # Devuelve -1; indicando que NO se encuentra.
cadena3.find("z") == -1 # Devuelve TRUE e indica que la sub-cadena (o caracter) NO está.
cadena3.count("p") #Devuelve 2; cuenta ocurrencias de sub-cadenas o caracteres.
cadena.replace("python","****") #Devuelve 'programación en ****'; va a reemplazarla todas las veces que la encuentre.

"python" in cadena3 # Devuelve TRUE.

#----------------------------------------------------------------------------------------------------------------

print("ingresá tu edad: ")
edad=input()

#Es lo mismo que (aunque no hace salto de línea, queda todo en el mismo renglón):

edad=input("ingresá tu edad: ")

#"input()" siempre toma el ingreso de teclado como tipo STRING, entonces:

edad=int(edad)

#ó

edad=int(input("ingresá tu edad: ")) #Esto va a funcionar sólo si se ingresa un nro entero.

#----------------------------------------------------------------------------------------------------------------

# 41)
# Escribir un programa que, dado un número entero, muestre su valor absoluto.

numero = int(input("número: "))
if numero < 0:
    numero = numero * (-1) # Es lo mismo que: " numero *=-1 "
print("El valor absoluto es", numero)

#----------------------------------------------------------------------------------------------------------------

# 42)
# Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables.
# Luego, imprimir "coincidencia" si los nombres comienzan o terminan con la misma letra; "no hay coincidencia"
# en caso contrario.

nom1 = input("Un nombre: ")
nom2 = input("Otro nombre: ")

if nom1[0] == nom2[0] or nom1[-1] == nom2[-1]:
    print("Coincidencia")
else:
    print("No hay coincidencia")

# otra forma (útil para otros lenguajes):

nom3 = input("Un nombre: ")
nom4 = input("Otro nombre: ")
indice_final_nom3 = len(nom3)-1
indice_final_nom4 = len(nom4)-1

if nom3[0] == nom4[0] or nom3[indice_final_nom3] == nom4[indice_final_nom4]:
    print("Coincidencia")
else:
    print("No hay coincidencia")

#----------------------------------------------------------------------------------------------------------------

# 43)
# En un bucle FOR sumar todos los numeros entre 0 y 100 que sean múltiplos de 3.

total = 0
for i in range(101):
    if i % 3 == 0:
    total = total + i  # es igual a "total += i"

print("sumatoria:", total)

#----------------------------------------------------------------------------------------------------------------

# 44)
# Dado un número entero positivo, mostrar su factorial,
# El factorial se obtiene multiplicando todos los números entre el nro dado y 1.

nro = int(input("Número: "))
f = 1
if nro != 0:
    for i in range(1, nro+1):
        f = f * i

print("Factorial: ", f)

#----------------------------------------------------------------------------------------------------------------

# 45)
# Escribir un programa que permita al usuario ingresar 6 nros enteros, que pueden ser positivos o negativos. Al
# finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
# NOTA: Recordar que no es posible dividir por cero.

sumNegativos = 0
sumPositivos = 0
cantidadPositivos = 0

for i in range(6):
    nro45 = int(input("Número: "))
    if nro45 >= 0:
        cantidadPositivos += 1
        sumPositivos += nro45
    else:
        sumNegativos += nro45

print("sumatoria de negativos:", sumNegativos)

if cantidadPositivos != 0:
    print("Promedio de positivos:", sumaPositivos/cantidadPositivos)
else:
    print("No se ingresaron números positivos")

#----------------------------------------------------------------------------------------------------------------

# 46)
# Escribir un programa que muestre el mayor nro positivo ingresado por teclado. Si se ingresa un nro negativo el
# programa corta su ejecución.

mayor = -1
h = int(input("Número positivo:"))
while h >= 0:
    if h > mayor:
        mayor = h
    h = int(input("Número positivo:"))
print("Mayor número ingresado:", mayor)

#----------------------------------------------------------------------------------------------------------------

# 47)
# Escribir un programa que permita descomponer un número dígito por dígito y los vaya sumando a todos.

suma = 0
n = int(input("Número positivo:"))
while n != 0:
    digito = n % 10  # obtengo el último dígito.
    suma += digito
    n = n//10  # elimino el último dígito para la próxima iteración.
print("Suma de los dígitos:", suma)

#----------------------------------------------------------------------------------------------------------------

# 48)
# Escribir un programa que le pida al usuario que ingrese números y corte su ejecución cuando se ingrese el "-1".
# repetir lo del ejercicio 47), pero además contar los números pares ingresados.

pares = 0
ñ = int(input("Ingrese número (-1 para terminar el programa): "))
while ñ != -1:
    if (ñ % 2) == 0:
        pares += 1

    suma = 0
    while ñ != 0:
        digito = ñ % 10  # obtengo el último dígito.
        suma += digito
        ñ = ñ//10  # elimino el último dígito para la próxima iteración.
print(f"Suma de los dígitos: {suma}. 
        La cant. de nros pares ingrsados es: {pares}")

#----------------------------------------------------------------------------------------------------------------

# 49)
# Realizar un programa que permita saber cuántos dígitos pares y cuántos impares tiene un nro ingresado por el usuario.

totalPares = 0
totalImpares = 0
numero49 = int(input("Número: "))

while numero49 != 0:  # Si ingresa un nuevo número !=0, sigue.
    pares49 = 0
    impares49 = 0
    while numero49 != 0:  # Si al ir descontando dígitos el número sigue siendo != 0, sigue.
        ultimoDigito = numero49 % 10
        if (ultimoDigito % 2) == 0:
            pares49 += 1
            totalPares += 1
        else:
            impares += 1
            totalImpares += 1
        numero49 = numero49 // 10  # elimino el último dígito del número
    print("El número ingresado tiene", pares,
          "dígitos pares y", impares, "dígitos impares")
    numero49 = int(input("Número: "))
print("Total de dígitos pares:", totalPares)
print("Total de dígitos impares:", totalImpares)

#----------------------------------------------------------------------------------------------------------------

# BREAK - CONTINUE

# WHILE condicion1:
#   bloque a repetir
#   IF condicion2:
#       BREAK            Corta el bucle (IF) y el resto del bloque (WHILE) no se ejecuta ¡Pasa al resto del programa!
#   *resto del bloque*   Lo mísmo pasaría si el bloque repetitivo fuese un FOR.
# *resto del programa*
#
#
# WHILE condicion1:
#   bloque a repetir
#   IF condicion2:
#       CONTINUE        ¡Vuelve a evaluar la condicion1! Saltea el resto del bloque, pero no va al resto del programa.
#   *resto del bloque*
# *resto del programa*

#----------------------------------------------------------------------------------------------------------------

# 50)
# Ejemplo BREAK en WHILE

while True:  # Se usa cuando necesitamos desplegar un menú o dar opciones y luego desplegar las condiciones de corte.
    print("Opción 1 - comenzar programa")
    print("Opción 2 - imprimir listado")
    print("Opción 3 - finalizar programa")
    opcion = int(input("opcion elegida: "))
    if opcion == 1:
        print("Comenzamos!")
    elif opcion == 2:
        print("Listado:")
        print("U2, Queen, Pink Floyd, Porcupine Tree, Elbow")
    elif opcion == 3:
        print("Hasta la próxima")
        break
    else:
        print("Opcion incorrecta. Debe ingresar 1, 2 ó 3")

#----------------------------------------------------------------------------------------------------------------

# 51)
# Ejemplo CONTINUE y BREAK en WHILE

frase = input("Frase: ")
l = input("Letra para buscar posición: ")
i = 0
while i != len(frase):
    if l != frase[i]:
        print("No se encontró en la posición", i)
        i += 1
        continue
    print("Se encontró en la posición", i)
    break

#----------------------------------------------------------------------------------------------------------------

# 52)
# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando
# cuando se reciba un cero.
# Imprimir la cantidad total de números primos ingresados.

# NOTA: un nro primo es un número NATURAL mayor que 1 que tiene únicamente dos divisores: él mismo y el 1.

cantidad = 0
s = int(input("Número: "))
while s != 0:
    primo = True
    for i in range(2, s):
        if (s % i) == 0:
            primo = False
            break
    if primo:  # si sigue siendo True.
        cantidad += 1
    s = int(input("Número: "))

#----------------------------------------------------------------------------------------------------------------

# 53)
# Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años que sean bisiestos
# y múltiplos de 10, en ese rango dado.

# NOTA: para que un año sea bisiesto debe ser divisible por 4 y NO debe ser divisible por 100, excepto que también
#       sea divisible por 400.

anioInicio = int(input("Año inicial: "))
anioFin = int(input("Año final: "))

for anio in range(anioInicio, anioFin+1):
    if not (anio % 10) == 0:
        continue            # paso a la siguiente iteración
    if not (anio % 4) == 0:
        continue            # paso a la siguiente iteración
    if (anio % 100) != 0 or (anio % 400) == 0:
        print(anio)

# NOTA: Con CONTINUE puedo ahorrarme niveles de anidamiento.

#----------------------------------------------------------------------------------------------------------------

# DICCIONARIOS:

# Estructuras heterogeneas.
# Útil para búsqueda más eficiente entre claves.

# diccionario_vacío = {}
# diccionario_vacío2 = dict()
# diccionario_con_elem = {"hola":"hello", "adios":"bye"}
# diccionario_desde_contenedor = dict([("hola","hello"),("adios","bye")])

# Iterar por pares de un diccionario

# a) Iteración por claves:
#        FOR clave IN diccionario.keys():   ///    FOR clave IN diccionario:
#            print(clave)                   ///         print(clave)

# b) Iteración por valores:
#       FOR valor IN diccionario.values():   ///    FOR clave IN diccionario:
#           print(valor)                     ///        print(diccionario[clave])

# c) Itreación por clave y valor a la vez:
#       FOR clave, valor IN diccionario.items():   ///  FOR par IN diccionario.items()
#           print(clave,valor)                     ///      print(par[0], par[1])


# EJEMPLOS:

traducciones = { "hola":"hello", "adiós":"bye", "día":"day", "noche":"night" }
traducciones.keys() #Devuelve: dict_keys(['hola','adiós','día','noche']); es una lista que contiene los strings.

for clave in traducciones.keys(): #Está iterando por una lista ("traducciones.keys()"), así que imprimo la clave.
        print(clave) #Esta forma de iterar no la tienen todos los lenguajes.
#devuelve:
# hola
# adiós
# día
# noche

for valor in traducciones.values():
    print(valor) #Esta forma de iterar no la tienen todos los lenguajes.
#devuelve:
#hello
#bye
#day
#night

for clave in traducciones.keys():
    print(clave,"==>",traducciones[clave])
#devuelve:
# hola ==> hello
# adiós ==> bye
# día ==> day
# noche ==> night

for clave, valor in traducciones.items(): #Itero por los dos a la vez
    print(clave,"==>",valor)
#devuelve:
# hola ==> hello
# adiós ==> bye
# día ==> day
# noche ==> night

# Iterar por una variable sola que va a contener a los dos elementos del par.
for par in traducciones.items(): #En "par" estoy obteniendo TUPLAS (la clave en la 1ra pos. y el valor en la 2da).
    print(par[0], "---",par[1])

# NOTA: conviene elegir sólo una variante de itreación para evitar confusiones.



# Diccionario desde un contededor:
calendario = [("enero", 1), ("febrero", 2), ("marzo", 3)]
meses = dict(calendario) #Si ejecutase "meses" devolvería: " {'enero': 1, 'febrero': 2, 'marzo': 3} "


# Diccionario para almacenar los datos de un equipo deportivo de niñas. Uso de clave los nros de camiseta,
# y como valores listas, en las cuales voy a poner: nombre, edad y años que lleva en el equipo.
equipo = {8: ["Melina", 8, 3], 2: ["Lucía", 9, 1], 6: ["María", 7, 2], 9: ["Sofía", 9, 1]}

# La cuestión de conocer cómo iterar en un diccionario es para cuando pase a otro lenguaje de programación.


for datos in equipo.values():
    print("nombre:", datos[0],"- edad:",datos[1],"- años en el equipo:", datos[2])
# Devuelve: 
# nombre: Melina - edad: 8 - años en el equipo: 3
# nombre: Lucía - edad: 9 - años en el equipo: 1
# nombre: María - edad: 7 - años en el equipo: 2
# nombre: Sofía - edad: 9 - años en el equipo: 1


# OPERACIONES CON DICCIONARIOS:

 dir(dict)     # Muestra lista de operaciones posibles con diccionarios.
 len(equipo)    # Cuantos PARES de elementos tiene (4).
 "hola" in traducciones.keys()      # Para saber si hay una clave en particular (True).
#                                   NOTA: podría no haber puesto el ".keys()".
 "hello" in traducciones.values()      # Para saber si un valor en particular (True).
#                                      NOTA: si no pongo ".values()" me devuelve False porque buscaría en las keys.
 "Sofía" in equipo.values()  # Devuelve FALSE porque dentro de "equipo" los values son listas y esta operación
#                              busca un value string con el valor que asigné. "Sofía" está contenida por la lista.
 calendario["enero"]    # Devuelve "1"; OBTIENE UN VALOR. Si la clave no existe, devuelve un error.
#           ó
 calendario.get("enero" [,valor])   # Devuelve "1"; OBTIENE UN VALOR. La diferencia es que NO devuelve ERROR.
#                                     Lo de  "[,valor]" es opciónal; se puede agregar un valor específico que
#                                     querramos que devuelva (iría sin los "[]", sólo la coma), si es que la clave
#                                     (en este caso "enero") no existe. Si no pongo el valor, y la clave no existe,
#                                     no retorna nada.
 calendario["enero"] = 01   # MODIFICA un VALOR. En vez de "1" ahora es "01". NOTA: La clave es INMUTABLE.
 calendario["abril"] = 4    # Asigna NUEVA CLAVE-VALOR.
 calendario.update({ "mayo":5, "junio":6, "julio":7 })   # Agrega VARIAS CLAVE-VALOR nuevas.
 del calendario["enero"]    # ELIMINA CLAVE-VALOR.
 calendario.clear()     # VACÍA todo el diccionario.

# MÁS EJEMPLOS:

 equipo[9][1]   # Devuelve "9" (la edad). El "[1]" es porque el valor es de tipo lista, y si quiero acceder a un
#                 campo de la misma, lo hago como a cualquier lista común.
 traducciones.get("reloj", "no existe esa palabra")     # Devuelve "no existe esa palabra" xq "reloj" no existe.
 traducciones.get("hola", "hi")     # Devuelve 'hello'.
 equipo[2][1] = 10      # asigna el 10 pisando el 9 (la edad de Lucía).
 traducciones["reloj"] = "clock"    # Asigno una nueva clave-valor.
 equipo[5] = "Marcela"      # En un diccionario, con todas listas como valores, agrego una nueva clave-valor, pero
#                             ahora el valor es un STRING y lo asigna sin ningún problema y quedaría:
equipo = {8: ["Melina", 8, 3], 2: ["Lucía", 9, 1], 6: ["María", 7, 2], 9: ["Sofía", 9, 1], 5: "Marcela"}



E = { 1:"a", "prueba":[1,2,3,5], (4,5):3 }

1 in E.values()     # Retorna "False". "in" es un operador que retorna un valor booleano e indica la PERTENENCIA.
#                     Acá estoy intentando averiguar si "1" está entre los valores del diccionario, y como los
#                     valores de estos se miden como PARES clave-valor, el "1" por si solo no se considera un
#                     elemento del mismo. No importa que aparezca dentro de los valores (como en la lista) o como
#                     clave por si solo.

#----------------------------------------------------------------------------------------------------------------

# 54) DICCIONARIO
# Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 
# 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings 
# ingresados. Ejemplo: "r":5, "%":3, "a":8, "9":1.
# ¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, incluyendo el valor 0 para las 
# letras que no aparecieron?

contadores={}
for i in range(50):
   cadena=input("Cadena de caracteres: ")
   for caracter in cadena:
       if caracter not in contadores:
           contadores[caracter]=1
       else:
           contadores[caracter]+=1
print("Frecuencia de cada carácter")
for caracter, cantidad in contadores.items():
   print(caracter, ": ", cantidad)

#Para contabilizar sólo letras (mayúsculas y minúsculas por separado):
contadores={}
alfabeto="abcdefghijklmnñopqrstuvwxyz"
for letra in alfabeto+alfabeto.upper():
    contadores[letra]=0
for i in range(50):
   cadena=input("Cadena de caracteres: ")
   for caracter in cadena:
       if caracter.lower() in alfabeto:
           contadores[caracter]+=1
print("Frecuencia de cada letra")
for caracter, cantidad in contadores.items():
   print(caracter, ": ", cantidad)

#----------------------------------------------------------------------------------------------------------------

# TUPLAS:


# Muy similares a las listas:

#    Elementos ordenador por índice.
#    Los elementos pueden repetirse.
#    Elementos heterogéneos.
#    Admiten "rebanadas".
#    Se iteran de la misma forma.

# La diferencia es que son inmutables. No se pueden cambiar (ni modificar, eliminar o agregar) elementos.
# Por lo tanto NO necesitan guardar espacio extra en la memoria como las listas.


# Creacion de una Tupla (parentesis opcionales):

 tupla_vacia = ()
 tupla_vacia2 = tuple()
 tupla_con_elementos = 104, "hola", 0.8, True
 tupla_desde_string = ("ema",)     # => Devuelve: ('ema',)
 tupla_desde_string2 = tuple("ema")  # => Devuelve: ('e','m','a') 
 tupla_desde_rango = tuple(range(5)) # => Devuelve: (0, 1, 2, 3, 4)

# Acciones posibles con Tuplas:

  dir(tuple) #veo qué acciones puedo tomar.
  tupla1 = tuple(C) # Si "C" es una LISTA, ahora "tupla1" va a tener sus mismos elementos, pero formando
#                     una tupla (o sea, delimitados por "()").
 nueva = (A,)+tupla_desde_string[1:] # devuelve "('A','m','a')". Es la forma de agregar algo a una tupla,
#                                      concatenando dos tuplas y aplicando "rebanadas".
 A = [1,2,3]
 B = (A,)  # => "B" devuelve: ([1,2,3],)
 A.append(4) # => "B" devuelve: ([1,2,3,4],) . Esto pasa porque la lista está guardada en una variable ("A").
#                                              "B", en sí, no cambió.

#----------------------------------------------------------------------------------------------------------------

# RECOMENDACIONES


# Usar estructuras repetitivas para imprimir listas y diccionarios:

lista = [ 1, 2, 3, 4 ]
for elemento in lista:
    print(elemento)


articulos = { 154:["jabón en polvo","limpieza", True],
              248:["talco","cosmetica", False],
              199:["cera para pisos", "limpieza", True] }
for clave, valor in articulos.items()  # Imprimir de esta manera para aclararle las cosas al usuario.
    print("Código:", clave)
    print("Descripción:",valor[0])
    print("Rubro:", valor[1])
    if valor[2]:             # Se recomienda imprimir un booleando con un "if".
        print("Hay stock")
    else:
        print("Agotado")
    print("--------")



# Considerar siempre los extremos de una lista o los casos "especiales" (como el de la lista vacía).

liista = [1,3,4,4,6,7,7,8,0,9,9,9]

for i in range(len(liista)-1): 
    if liista[i]==liista[i+1]:
        print(liista[i]) # imprime elementos que son iguales a su adyacente.
# "len()" va desde 0 hasta 11, pero cuando estoy en el "if" con "i=11" (última posición) e intento acceder
# a "i+1", me voy de rango y devuelve ERROR; por eso uso "-1" en el "range()".



#Considerar que quizás sólo queriamos imprimir una vez a los nros que se repiten, pero en el caso del 9 lo
#estaría imprimiendo dos veces. Este es un caso espacial a considerar.



# NO buscar en una estructura a un elemento X que sólo puede estar en una estructura anidada (Ejemplo:
# buscar un elemento como VALOR en un diccionario, cuando en realidad está en una lista que se encuentra
# cumpliendo el rol de VALOR en el diccionario). Ejemplo de lo que sí hay que hacer:

def empleadoExiste(empleados,nombre):
    for datos in empleados.values():
        if datos[0] == nombre:
            return True
    return False     # Importante acordarse de esta linea.

empleados = { 100:["Jorge","RRHH"],
              200:["Ana","Ventas"],
              300:["Guadalupe", "Administración"] }

nombree=input("Nombre de empleado:")
if not empleadoExiste(empleados, nombree): #Evaluo un BOOLEANO (la función).
    print("El empleado no se encuentra en la lista")



# NO iterar para buscar la clave en un diccionario.

# Si la clave existe, se puede acceder de manera directa. Ejemplo:

codigo = input("código a buscar: ")
if codigo in empleados.keys():
    print("el nombre es:" empleados[codigo][0]) # ¿El "[0]" va? Lo agregué yo.


    



# NO querer imprimir valores de un diccionario usando nombres de variables. 
# Ejemplo sobre como sí hacerlo:

def cargarDatos(diccionario):
    dni = int(input("DNI (ingrese 0 para salir): "))
    while dni != 0:
        nombre = input("Nombre: ")
        domicilio = input("Domicilio: ")
        telefono = input("Teléfono: ")
        diccionario[dni] = [nombre,domicilio,telefono] # Aclaro que "dni" es la clave. 
        dni = int(input("DNI (ingrese 0 para salir): "))
    return diccionario

def imprimirDatos(diccionario):
    for clave, valor in diccionario.items():
        print("-DNI:",clave, "-NOMBRE:",valor[0], "-DOMICILIO:",valor[1], "-TELÉFONO:",valor[2]) 
        # Acá NOOOO tengo que poner "dni", "nombre", "domicilio", etc.
        # como variables directas para imprimir.

clientes = { 21069486:["Gastón", "chubaca 444", 29485733]
             68365035:["Tomás","chikaka 098", 458477738]
             12098593:["Camila", "hermosa 221", 33939494] }
clientes = cargarDatos(clientes) # PISA la variable anterior "clientes" con un diccionario nuevo.
imprimirDatos(clientes)




# NO cargar todos los datos en una misma lista cuando deberían ser diferentes.
# Por ejemplo, cuando tengo un diccionario que su VALOR es una lista.

def cargarMercaderias(mercaderias):
    codigo = int(input("Codigo: "))
    while codigo != 0:
        articulo = []      # esta es la clave; definir la lista VACÍA dentro del bucle para cuando termino
                           # de cargar un artículo, la liste se VACÍE para que el próximo articulo arranque
                           # desde 0 y sin ningún dato del artículo anterior.
        descripcion = input("Descripción: ")
        articulo.append(descripcion)
        rubro = input("Rubro: ")
        articulo.append(rubro)
        mercaderias[codigo] = articulo # El valor del diccionario es la lista.
        codigo = int(input("Código: "))
    return mercaderias
# Otra forma de hacerlo sería NO arrancar con una lista vacía la cual ir cargando; es decir, elimino "articulo = []"
# junto a sus respectivas cargas "articulo.append(descripcion)" y "articulo.append(rubro)" para darle lugar a la linea:
  mercaderias[codigo] = [descripcion, rubro] # y cree la lista ahí mismo.

productos = {}
productos = cargaMercaderias(productos)   #PISA la variable anterior "clientes" con un diccionario nuevo.
for codigo, datos in productos.items():
    print("-Código:", codigo,"-Descripción:", datos[0],"-Rubro:", datos[1])



# NO modificar la cantidad de elementos de una estructura DURANTE su iteración.
# EJEMPLO:

a = [1,2,3,4]

for i in range(len(a)):
    if i == 2:
        del a[3] # NOOOO HACER ESTO; devolvería un error porque querría usar un índice fuera del rango.
    print(a[i])

# OTRO EJEMPLO:

b = {"a": [1,2,3], "b": [], "c":[8,6], "d": [], "e":[4]}
    for clave in b.keys():
        if b[clave] == []:
            del b[clave] # NOOOO HACER ESTO; devolvería un error porque querría usar un índice fuera del rango.
                         # Ya que el diccionario cambió su tamaño en la iteración.

# ESTO SE SOLUCIONARÍA ITERANDO OTRA ESTRUCTURA:

b = {"a": [1,2,3], "b": [], "c":[8,6], "d": [], "e":[4]}
claves = list(b.keys) # Convierto a lista las claves del diccionario.
    for clave in claves:
        if b[clave] == []:
            del b[clave]

#----------------------------------------------------------------------------------------------------------------

# TEORIA DE LA DOCUMENTACION OFICIAL



#  The IF statement:

 if_stmt ::= "if" assignment_expression ":" suite
             ("elif" assignment_expression ":" suite)*
             ["else" ":" suite]



# The WHILE statement:

while_stmt ::=  "while" assignment_expression ":" suite
                ["else" ":" suite]



# The FOR statement:

for_stmt ::=  "for" target_list "in" expression_list ":" suite
              ["else" ":" suite]



# The TRY statement:

try_stmt  ::=  try1_stmt | try2_stmt
try1_stmt ::=  "try" ":" suite
               ("except" [expression ["as" identifier]] ":" suite)+
               ["else" ":" suite]
               ["finally" ":" suite]
try2_stmt ::=  "try" ":" suite
               "finally" ":" suite



# The WITH statement:

with_stmt ::=  "with" with_item ("," with_item)* ":" suite
with_item ::=  expression ["as" target]



# FUNCTION definitions:

funcdef                   ::=  [decorators] "def" funcname "(" [parameter_list] ")"
                                ["->" expression] ":" suite
decorators                ::=  decorator+
decorator                 ::=  "@" dotted_name ["(" [argument_list [","]] ")"] NEWLINE
dotted_name               ::=  identifier ("." identifier)*
parameter_list            ::=  defparameter ("," defparameter)* "," "/" ["," [parameter_list_no_posonly]]
                                 | parameter_list_no_posonly
parameter_list_no_posonly ::=  defparameter ("," defparameter)* ["," [parameter_list_starargs]]
                               | parameter_list_starargs
parameter_list_starargs   ::=  "*" [parameter] ("," defparameter)* ["," ["**" parameter [","]]]
                               | "**" parameter [","]
parameter                 ::=  identifier [":" expression]
defparameter              ::=  parameter ["=" expression]
funcname                  ::=  identifier

 

# CLASS definition:

classdef    ::=  [decorators] "class" classname [inheritance] ":" suite
inheritance ::=  "(" [argument_list] ")"
classname   ::=  identifier