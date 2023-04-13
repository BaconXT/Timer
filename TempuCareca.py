

import time


def contagemRegressiva(segundos):

    while segundos > 0:

        minutes = int(segundos / 60)

        seconds = int(segundos % 60)

        tempo = f'{minutes} : {seconds}'
        print(tempo)
        time.sleep(1)

        segundos -= 1
    print("Desculpe lhe dizer mais seu tempo esgotou :(")



segundos = input("Digite ao lado seu tempo em segundo: ")

contagemRegressiva(int(segundos))



