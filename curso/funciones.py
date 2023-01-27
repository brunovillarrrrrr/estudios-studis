#de esta manera se crea una funcion :) 
# posdata tenemos que poner ()al final del nombre de nuestra 
#def miFuncion():
 #   print('mi primera funcion!')


#miFuncion()

#def imprimirdato(argumento_1):
 #      print('mi argumento es',argumento_1)
#cuando le damos un valor a la funcion dentro de los parentesis le estamos dando un parametro
#por lo que el argumento tendra el valor dentro de los parantesis que sera el parametro
#imprimirdato('parametro 1')

#def imprimirdato(nombre, apellido):
 #       print('el nombre completo es:', nombre, apellido)
#cuando le damos un valor a la funcion dentro de los parentesis le estamos dando un parametro
 
#por lo que el argumento tendra el valor dentro de los parantesis que sera el parametro
#imprimirdato('bruno', 'villarreal')

#def imprimirdato(*nombre):
 #       print('el nombre completo es:', nombre)
#cuando le damos un valor a la funcion dentro de los parentesis le estamos dando un parametro
 
#por lo que el argumento tendra el valor dentro de los parantesis que sera el parametro
#imprimirdato('bruno', 'villarreal')

#def imprimirdato(*nombre):
#aqui le decimo que en el nombre solo imprimira el primer dato
 #   print('el nombre completo es:', nombre[0])
#cuando le damos un valor a la funcion dentro de los parentesis le estamos dando un parametro
#por lo que el argumento tendra el valor dentro de los parantesis que sera el parametro
#imprimirdato('bruno', 'villarreal', 'leija')

#def nombre(apellidos, nombre):
 #      print(nombre, apellidos)
#aqui le estamos dando los valores especificamente a los argumentos de esta forma si no recordamos el orden etc solo se los otorgamos directamente
#name(nombre = 'bruno' apellidos= 'villarreal')

def nombre2(**diccionario):
       print(diccionario['nombre'], diccionario['apellido'] )
 
nombre2(nombre = 'bvl', apellido= 'lol')