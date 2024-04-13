
# variables en python 
name = "hola" 

print(name)

# cuando la variable tiene más de una palabra se usa "_"
last_name = "chao"

print (last_name)

# mala practica (no usar "_" cuando hay 2 palabras)
lastname= "G"

print(lastname)

# errores de sintaxis: 
# last.name = "primero"
# last*name = "primero"
# last-name = "primero"

# operadores matemáticos
num_1 = float (input("ingrese número 1:")  )
#num_1 = float(num_1)

num_2 = float (input("ingrese número 2:")  ) 
#num_2 = float(num_2)


# sumas
result_1 = num_1 + num_2
print(f"el resultado de la suma es : {result_1}")
# resta 
result_2 = num_1 - num_2
print(f"el resultado de la resta es : {result_2}") 
# multiplicación
result_3 = num_1 * num_2
print(f"el resultado de la multiplicación es : {result_3}") 
# división
result_4 = num_1 / num_2
print(f"el resultado de la división es : {result_4}") 
# saludos
name = "Josefino"
print(f"hola {name}")


# resultados 
print(f"el resultado de la suma es : {result_1}")
print(f"el resultado de la resta es : {result_2}") 
print(f"el resultado de la multiplicación es : {result_3}") 
print(f"el resultado de la división es : {result_4}") 

# saludos
name = input ("¿cual es tu nombre?")
print(f"mi nombre es {name}")

# ejercicio
# Solicita el primer número al usuario y conviértelo a entero
num_1 = int(input("Ingresa el primer número: "))

# Solicita el segundo número al usuario y conviértelo a entero
num_2 = int(input("Ingresa el segundo número: "))

# Realiza la suma
suma = num_1 + num_2

# Imprime el resultado
print("La suma de", num_1, "y", num_2, "es:", suma)

num_3 = input("num_3: ")
num_3 = float (num_3)
type (num_3)
print(type)

# operadores de comparacion

# mayor que >
# menor que <
# mayor igual >=
# menor igual <=
# igual ==
# diferente !=

# operadores lógicos
# and or not

10 != 20
print(10 != 20)

# condicionales
name = input("ingrese su nombre: ")

# if condicion:
 # hago algo (lo que yo quiera que haga)

if name == "josefino":
     print("otra vez tú!")

num = float (input ("ingrese un número: ") )

if num >=10 and num <= 20:
    print("mayor o igual a 10")
    print("menor o igual a 20")
else: 
    print("es menor que 10")
    print("es mayor que 20")
