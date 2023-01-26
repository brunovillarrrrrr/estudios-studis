#calculñadora basica muy muy basica :)

#print('esta es una calculadora')

#numero_1 = input('coloca el primer numero: ')
#numero_2 = input('coloca el primer segundo: ')

#recordatorio los input son tomados como strings entonces debemos pasarlos a int
#primernumero = int(numero_1 )
#segundonumero = int(numero_2)

#print('deseas poner un tercer numero')

#si_no = input('si/no: ')

#if si_no == 'si':
 #   numero_3 = input('coloca el primer tercer: ')
  #  tercernumero = int(numero_3)
   # respuesta = primernumero + segundonumero + tercernumero
    #print (respuesta)

#else:
 #   respuesta = primernumero + segundonumero
  #  print (respuesta)


print('hola esto es una calculadora\nsuma + \nresta -\nmultipilcacion *\ndivicion / ')
operacion = input('coloca el signo de la operacion que quieres llevar a cabo: ')

if operacion == '+':
   numero_1 = input('dame el primer numero:')
   numero_2 = input('dame el segundo numero:')

   numerouno = int(numero_1)
   numerodos = int(numero_2)

   print(numerouno + numerodos)
elif operacion == '-':
   numero_1 = input('dame el primer numero:')
   numero_2 = input('dame el segundo numero:')

   numerouno = int(numero_1)
   numerodos = int(numero_2)

   print(numerouno - numerodos)
elif operacion == '*':
   numero_1 = input('dame el primer numero:')
   numero_2 = input('dame el segundo numero:')

   numerouno = int(numero_1)
   numerodos = int(numero_2)

   print(numerouno * numerodos)
elif operacion == '/':
   numero_1 = input('dame el primer numero:')
   numero_2 = input('dame el segundo numero:')

   numerouno = int(numero_1)
   numerodos = int(numero_2)

   print(numerouno / numerodos)

else:
    print('perdon no podemos completar esa operacion')