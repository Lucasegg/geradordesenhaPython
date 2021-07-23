import random, string
import sys

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        tamanho = int(input('Digite o tamanho de senha que você deseja de no mínimo 8 e'
                            ' no máximo 20 caracteres: '))
        if tamanho < 8:
           raise InputError("Digitou uma quantidade inválida para gerar a senha")

        elif tamanho > 20:
            raise InputError("Digitou uma quantidade inválida para gerar a senha")
        break
    except ValueError:
        print('Valor inválido. Deve-se Digitar somente números: ')
    except InputError as ex:
         print(ex)

chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+,.;:/?[]'

rnd = random.SystemRandom() #os.urandom

#retornando uma lista com caracteres randomicos
print(''.join(rnd.choice(chars) for i in range(tamanho)))




