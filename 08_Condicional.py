#Condicional if
Adivinar = 42
Numero = int(input('Señor usuario, dígite un número: '))
if(Numero > Adivinar):
  print('Bájele el Volumen')
elif (Numero < Adivinar):
  print('subale al Volumen')
else:
  print('Verdadero')

# if anidado 2:
if (Numero >= Adivinar):
  if (Numero < Adivinar):
    print('Coloque un número menor.')
  else:
    print('¡Acertado!')
 else:
   print('Coloque un número mayor.')

# Fin del if.
print('La instrucción "if" finalizo.')