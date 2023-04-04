*** # Operaciones Aritmeticas ***

Number = int(input('Digite un número: '))

# Suma (+)
print(f'La suma con 2 es: {Number + 2}') 

# Resta (-)
print(f'La Resta con 2 es: {Number - 2}')

# Multiplicación (*)
print(f'La Multiplicación con 2 es: {Number * 2}')

# Divisioón (/)
print(f'La División con 2 es: {Number / 2}')

# División Entera (//)
print(f'La División Entera con 2 es: {Number // 2}')

# Residio o Módulo (%)
print(f'La Resuduo con 2 es: {Number % 2}')

# Potenia (**)
print(f'La Potencia con 2 es: {Number ** 2}')

*** # Operaciones Asignación ***

Contador = 1
print(f'antes de la operación += {Contador}')

Contador += 1  # Contador = Contador + 1 ( += Oper. Incrementar )
print(f'Después de la operación += {Contador}')

Contador -= 9
Contador -= 1  # Contador = Contador + 1 ( += Oper. Decrementar )

Number += 1
print(f'Al usar operador incremental += El esultado es {Number}')

Number -= 1
print(f'Al usar operador Decremental -= El resultado es {Number}')

Number *= 2
print(f'Al usar operador *= El resultado es {Number}')

Number /= 2
print(f'Al usar operador /= El resultado es {Number}')

Number //= 2
print(f'Al usar operador //= El resultado es {Number}')

Number %= 3
print(f'Al usar operador %= El resultado es {Number}')

Number **= 2
print(f'Al usar operador **= El resultado es {Number}')
