# priemra forma de hacerlo

#print('este es el juego de la adivinanza dime que es cafe pero huele bien y tal vez te agrada ')
#respuesta = input('ingresa tu respuesta: ')
#lista = ['cafe', 'chocolate', 'nueces']
#if respuesta == lista[0] or respuesta == lista[1]:
#                      print('felicidades has adivinado una de las tres posibles respuestas ')
#elif respuesta == lista[2]:
#                     print('felicidades has adivinado una de las tres posibles respuestas ')
#else:
#      print('no has adivinado ninguna pero puedes volver a tratar')


# segunda forma de hacerlo
respuesta = input('ingresa tu respuesta: ')
lista = ['cafe', 'chocolate', 'nueces', 'avellanas','cereal']

if lista.count(respuesta) > 0:
    print('tienes una respuesta correcta :)')

else:
    print('sorry no has atinado ninguna palabra :(')