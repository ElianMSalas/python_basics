# Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
def max():
    number_1 = int(input("Ingrese el primer número: "))
    number_2 = int(input("Ingrese el segundo número: "))
    if number_1 > number_2:
        print(number_1)
    elif number_2 > number_1:
        print(number_2)
max()

# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def max_de_tres():
    number_1 = int(input("Ingrese el primer número: "))
    number_2 = int(input("Ingrese el segundo número: "))
    number_3 = int(input("Ingrese el tercer número: "))
    if number_1 > number_2 > number_3:
        print(number_1)
    elif number_2 > number_1 > number_3:
        print(number_2)
    else:
        print(number_3)
max_de_tres()

# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
def vocales(caracter):
    vocales = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    if caracter in vocales:
        return True
    else:
        return False
print(vocales("k"))

# Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
def sum(lista):
    result = 0
    for n in lista:
        result = result + (n)
    print(result)
sum([1,2,3,4])

def multip(lista):
    result = 1
    for i in lista:
        result *= i
    print(result)
multip([1,2,3,4])

# Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
def inversa(cadena):
    longitud = -(len(cadena)-1)
    nueva_cadena = str()
    for n in range(longitud,1):
        n = abs(n)
        nueva_cadena += cadena[n]
    print(nueva_cadena)
inversa("Hola")

# Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
def es_palindromo(cadena):
    nueva_cadena = inversa(cadena)
    if nueva_cadena == cadena:
        return True  
print(es_palindromo("radar"))
# Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
def superPosicion(lista_1, lista_2):
    for elem in lista_1:
        if elem in lista_2:
            return True 
        return False
    print('Superposicion:')
print(superPosicion(["Manchester City", "Chelsea"],["Liverpool", "Manchester City"]))
# Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
def generar_n_caracteres():
    palabra = input("Ingrese una palabra: ")
    numero = int(input("Ingrese un numero: "))
    resultado = numero * palabra
    print(resultado)
generar_n_caracteres() 

# Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
def procedimiento():
    lista = [1,2,3,4]
    for x in lista:
        print(x * "*")
procedimiento()