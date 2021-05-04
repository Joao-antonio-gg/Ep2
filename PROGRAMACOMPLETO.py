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

for n, item in enumerate(cria_baralho()):
    y = n + 1
    print(n + 1, item)

while len(cria_baralho()) > 1 and EP2_6.possui_movimentos_possiveis(cria_baralho()) == True:

    carta_desejada = int(input('Digite o número da carta desejada:'))

    # if carta_desejada > len(cria_baralho()) or carta_desejada <= 0:
    #     print('Essa carta é invalida, digite uma carta valida.')
    #     carta_desejada = int(input('Digite o número da carta desejada:'))
    
    indice_carta = carta_desejada - 1
    verifica_funcionamento = EP2_4.lista_movimentos_possiveis(cria_baralho(),indice_carta)
    indice_igual_carta = cria_baralho()[indice_carta]

    if  verifica_funcionamento == []:
        Try_again = int(input('Essa carta não pode ser empilhada, escolha outra:'))
        indice_try_again = Try_again - 1
        verifica_funcionamento = EP2_4.lista_movimentos_possiveis(cria_baralho(),indice_try_again)
    
    if verifica_funcionamento == [1] :
        for n, item in enumerate(EP2_5.empilha(cria_baralho(), indice_carta , indice_carta - 1)):
            print (n + 1, item)
        
    
    
    if verifica_funcionamento == [3]:
        for n, item in enumerate(EP2_5.empilha(cria_baralho(), indice_carta , indice_carta - 3)):
            print (n + 1, item)
        
    
    if verifica_funcionamento == [1,3]:
        Qual_carta = int(input('Qual carta deseja empilhar ?'))
        while Qual_carta == indice_carta - 3 or Qual_carta == indice_carta - 1 :
            for n, item in enumerate(EP2_5.empilha(cria_baralho(), indice_carta , Qual_carta)):
                print (n+1 , item)
        #if Qual_carta != indice_carta - 3 or Qual_carta != indice_carta - 1:
            #pergunta_novamente = int(input('Carta invalida, digite uma carta valida:'))
           # EP2_5.empilha(cria_baralho(), indice_carta , pergunta_novamente)
        
    