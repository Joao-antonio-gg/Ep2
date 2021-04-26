
import EP2_1
import EP2_2
import EP2_3
import EP2_4
import EP2_5
import EP2_6

baralho = EP2_1.cria_baralho()

for n, item in enumerate(baralho):
    print(n+1, item)
    
carta_desejada = int(input('Digite o número da carta desejada:'))

verifica = EP2_4.lista_movimentos_possiveis(baralho,carta_desejada)
