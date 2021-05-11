import random
def cria_baralho():
    lista = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','K♠','Q♠','A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','Q♣','K♣','J♣','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','Q♦','K♦','J♦']
    random.shuffle(lista)
    return lista
import EP2_2
import EP2_3
import EP2_4
import EP2_5
import EP2_6
import Cores

print('')
print('Paciência Acordeão')
print('')
print('=====================')
print('')
print('O objetivo deste jogo é colocar todas as cartas em uma mesma pilha')
print('')
print('Existem apenas dois movimentos possíveis:')
print('')
print('1 - Empilhar uma carta sobre a carta imediatamente anterior.')
print('2 - Empilhar uma carta sobre a terceira carta anterior.')
print('')
print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:')
print('')
print('1 - As duas cartas possuem o mesmo valor')
print('     ou    ')
print('2 - As duas cartas possuem o mesmo naipe ')
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada')
print('')
print('Boa sorte e Bom Jogo!')
print('')
print('')

cartas = cria_baralho()
for n, item in enumerate(cartas):
    y = n + 1
    print(('{0}'.format(y))+ ' ' + Cores.cores(item))

Restart = True    
while Restart :
    
    while len(cartas) > 1 and EP2_6.possui_movimentos_possiveis(cartas) == True:

        carta_desejada = int(input('Digite o número da carta desejada de {0} a {1}:'.format(1, len(cartas))))

        while carta_desejada > len(cartas) or carta_desejada <= 0:
            print('Essa carta é invalida, digite uma carta valida.')
            carta_desejada = int(input('Digite o número da carta desejada de {0} a {1}:'.format(1, len(cartas))))
        
        indice_carta = carta_desejada - 1
        verifica_funcionamento = EP2_4.lista_movimentos_possiveis(cartas,indice_carta)
        indice_igual_carta = cartas[indice_carta]

        while  verifica_funcionamento == []:
            Try_again = int(input('Essa carta não pode ser empilhada, escolha outra:'))
            indice_try_again = Try_again - 1
            verifica_funcionamento = EP2_4.lista_movimentos_possiveis(cartas,indice_try_again)
        
        if verifica_funcionamento == [1] :
            for n, item in enumerate(EP2_5.empilha(cartas, indice_carta , indice_carta - 1)):
                y = n + 1
                print(('{0}'.format(y))+ ' ' + Cores.cores(item))
            
        
        
        if verifica_funcionamento == [3]:
            for n, item in enumerate(EP2_5.empilha(cartas, indice_carta , indice_carta - 3)):
                y = n + 1
                print(('{0}'.format(y))+ ' ' + Cores.cores(item))
            
        
        if verifica_funcionamento == [1,3]:
            n_pod = True
            while n_pod:
                Qual_carta1 = int(input('Qual carta deseja empilhar ({0} ou {1})?'.format(indice_carta, indice_carta - 2)))
                Qual_carta = Qual_carta1 - 1

                if Qual_carta == indice_carta - 3 or Qual_carta == indice_carta - 1:
                    for n, item in enumerate(EP2_5.empilha(cartas, indice_carta , Qual_carta)):
                        y = n + 1
                        print(('{0}'.format(y))+ ' ' + Cores.cores(item))
                    n_pod = False
                else:
                    print('Essa carta é inválida, digite outra carta')
                    n_pod = True


            # while Qual_carta != indice_carta - 3 or Qual_carta != indice_carta - 1:
                
            #     Qual_carta = int(input('Carta invalida, digite uma carta valida:')) - 1

            #     # if Qual_carta != indice_carta - 1 or Qual_carta != indice_carta - 3:

            #     #     Qual_carta = int(input('Carta invalida, digite uma carta valida:')) - 1

            #     if Qual_carta == indice_carta - 1:
            #         for n, item in enumerate(EP2_5.empilha(cartas, indice_carta , indice_carta - 1)):
            #             y = n + 1
            #             print(('{0}'.format(y))+ ' ' + Cores.cores(item))

            #     if Qual_carta == indice_carta - 3:
            #         for n, item in enumerate(EP2_5.empilha(cartas, indice_carta , indice_carta - 3)):
            #             y = n + 1
            #             print(('{0}'.format(y))+ ' ' + Cores.cores(item))



        if len(cartas) == 1 and EP2_6.possui_movimentos_possiveis(cartas) != True:
            print ('Fim do jogo')
            jogar_nv = input('Você deseja jogar novamente ?(s/n) ')
            if jogar_nv == 's':
                Restart = True
                for n, item in enumerate(cartas):
                    y = n + 1
                    print(('{0}'.format(y))+ ' ' + Cores.cores(item))
            else:
                Restart = False
            

