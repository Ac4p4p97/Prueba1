# 1. formatos de impresión
Edad = 27
Estatura = 1.70
print('La edad es:', Edad)
print('La estatura es:', Estatura)

# 1ra. Manera uso formato
print('La edad es:', Edad, 'La estatura es:', Estatura)

#2da Manera uso formato
'La edad es:', Edad, 'La estatura es:', Estatura
print(f'La edad es: {Edad} La estatura es: {Estatura}')

#3ra Manera uso formato
print('La edad es: {} La estatura es: {}'.format(Edad, Estatura))
print('la edad más la estatura es:', Edad + Estatura)
print(f'la edad más la estatura es: {Edad + Estatura}')
print('la edad mas la estatura es: {}'.format(Edad + Estatura))
suma = Edad + Estatura
print(f'la edad mas la estatura es: {suma}')