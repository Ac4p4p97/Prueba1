Primera_lista = ['Manzana', 'Banano']
print(Primera_lista)
Nombres = ['Cesar', 'Carlos', 'Camilo']
print(Nombres)

Lista1 = [2, 4, 3.14, 1000, 56]
print(Lista1)
Lista2 = ['a', 123, 'A', 3.456, 'Palabra', True, 1000]
print(Lista2)

# Tamaño de una lista (len):
print(len(Lista1))
print(len(Lista2))
print(len(Primera_lista))

#Tipo de dato lista:
print('Tipo de dato lista')
print(type(Lista1))
print(type(Lista2))

# Otra lista
print('Función lis():')
Num = [1, 2, 3, 4, 5, 6, 7]
print(Num)
Num2 = list((1, 2, 3, 4, 5, 6, 7))
print(Num2)
print('index list:')
print(Num[0])
print(Num[0:3])
print(Num[-1::-1])

print('Uso de la función "IN"')
print(3 in Num)
print(10 in Num)
print(Num)
Num1 = Num
print(Num1 is Num)
print(Num2 is Num)