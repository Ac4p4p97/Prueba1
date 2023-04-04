# *** Operaciones Reales o Comparación ***
# True (1) / False (0)

Number = int(input('Digite un número: '))
print(Number > 3)  # Pregunta si en Number es Mayor 3
print(Number >= 3)  # Pregunta si Number es mayor o igual a 3
print(Number < 3)  # Pregunta si Number es menor 3
print(Number <= 3)  # Pregunta si Number es menor o igual a 3
print(Number == 3)  # Pregunta si Number es igual a 3
print(Number != 3)  # Pregunta si Number es diferente a 3

# *** Operaciones Lógicas ***
print("Operaciones Lógicas.")

# True (1) / False (0) cuando todas las opciones son verdades el resultado dara verdarero, si una es falsa, siempre dara falso

print(True and True)
print((Number >= 3) and True)

print(True & True)
print((Number >= 3) & True)

print(False and False)
print((Number >= 3) and False)

print(True and False)
print((Number >= 3) and False)

print(False and True)
print((Number >= 3) and True)

print(True and True and True)
print((Number >= 3) and True and True)

# Conjunción / And (&)
print('Conjunción')  # si uno de sus valores es falso, simore dara falso
print(False & False & True)
print(False and False and True)
print(Number >= 3 and False and True)

# Disyunción / Or (|)
print(
  'Disyunción')  # si uno de sus valores es verdadero siempre dara verdadero.
print(False or False)
print(False or True)
print(True or False)
print(True or True)
print(Number > 3 or True)
print(Number > 3 or Number < 10)
print(Number <= 3 | Number >= 10)

# Negación / Not (~)
print('Negación')
print(not (True))

# Or Explusiva (^) #si los valores son iguales dara True, si son diferentes dara False
print(' Explusiva')
print(True ^ False)
print(False ^ True)
print(False ^ False)
print(True ^ True)

# Operaciones de contenido o pertenenecia
# In 
print('Operador in') #Preguntar si un valor esta en la variable, si cumple true, si no false
Nombre = 'Carolina Paredes'
print('C' in Nombre)
print('a' in Nombre)



