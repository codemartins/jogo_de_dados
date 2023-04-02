#Crie um programa  onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses dados em um dicionário.
#No final, coloque esse dicionário em ordem, sabendo  que o vencedor  tirou  o maior número  no dado.

from random  import randint
from time import sleep
from operator import itemgetter

print('')
#Title
print('======= Jogue os Dados. Valendo! =======')
print('')

#Dicionário com os Jogadores dos Dados
jogo =  {'Jogador 1 -->': randint(1, 12),
         'Jogador 2 -->': randint(1, 12),
         'Jogador 3 -->': randint(1, 12),
         'Jogador 4 -->': randint(1, 12)}

#Ordenando o Placar dos Jogadores:
ranking = list()

print('Valores Sorteados: ')
for k, v in jogo.items():
    print(f'{k} Tirou {v} no dado.')
    sleep(2)
ranking = sorted(jogo.items(), key= itemgetter(1), reverse=True)
print('')
print('=======Os Ganhadores são: =======')
for i, v in enumerate(ranking):
    print(f'{i} lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
print('')
print('FIM DO JOGO. OBRIGADO A TODOS OS PARTICIPANTES!')