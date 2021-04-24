def cria_baralho():
    lista = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','K♠','Q♠','A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','Q♣','K♣','J♣','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','Q♦','K♦','J♦']
    
    return lista

def extrai_naipe(card):
    if card == 'A♦' or card =='2♦' or card =='3♦' or card =='4♦' or card =='5♦' or card =='6♦' or card =='7♦' or card =='8♦' or card =='9♦' or card =='10♦' or card =='J♦' or card =='K♦' or card =='Q♦':
        return '♦'
    if card == 'A♠' or card =='2♠' or card =='3♠' or card =='4♠' or card =='5♠' or card =='6♠' or card =='7♠' or card =='8♠' or card =='9♠' or card =='10♠' or card =='J♠' or card =='K♠' or card =='Q♠':
        return '♠' 
    if card == 'A♥' or card =='2♥' or card =='3♥' or card =='4♥' or card =='5♥' or card =='6♥' or card =='7♥' or card =='8♥' or card =='9♥' or card =='10♥' or card =='J♥' or card =='K♥' or card =='Q♥':
        return '♥'
    if card == 'A♣' or card =='2♣' or card =='3♣' or card =='4♣' or card =='5♣' or card =='6♣' or card =='7♣' or card =='8♣' or card =='9♣' or card =='10♣' or card =='J♣' or card =='K♣' or card =='Q♣':
        return '♣'

def extrai_valor(card):
    if card == '2♦' or card =='2♠'or card =='2♥'or card =='2♣':
        return '2'
    if card == '3♦'or card =='3♠'or card =='3♥'or card =='3♣':
        return '3'
    if card =='4♦'or card =='4♠'or card =='4♥'or card =='4♣':
        return '4'
    if card == '5♦' or card =='5♠'or card =='5♥'or card =='5♣':
        return '5'
    if card == '6♦'or card =='6♠'or card =='6♥'or card =='6♣':
        return '6'
    if card == '7♦'or card =='7♠'or card =='7♥'or card =='7♣':
        return '7'
    if card  == '8♦'or card =='8♠'or card =='8♥'or card =='8♣':
        return '8'
    if card == '9♦'or card =='9♠'or card =='9♥'or card =='9♣':
        return '9'
    if card == '10♦'or card =='10♠'or card =='10♥'or card =='10♣':
        return '10'
    if card == 'Q♦'or card =='Q♠'or card =='Q♥'or card =='Q♣':
        return 'Q'
    if card == 'J♦'or card =='J♠'or card =='J♥'or card =='J♣':
        return 'J'
    if card == 'K♦'or card =='K♠'or card =='K♥'or card =='K♣':
        return 'K'
    if card == 'A♦'or card =='A♠'or card =='A♥'or card =='A♣':
        return 'A'

def lista_movimentos_possiveis(cartas, indice):
    
    lr = []
    k = cartas[indice]
    
    if indice == 0:
        lr = []
            
    if indice > 0:
        l = cartas[indice - 1]
        if extrai_naipe(k) != extrai_naipe(l) or extrai_valor(k) != extrai_valor(l):
            lr = []

        if extrai_naipe(k) == extrai_naipe(l) or extrai_valor(k) == extrai_valor(l):
            lr.append(1)

        if indice > 2:
            m = cartas[indice - 3]
            if extrai_naipe(k) != extrai_naipe(m) or extrai_valor(k) != extrai_valor(m) and extrai_naipe(k) != extrai_naipe(l) or extrai_valor(k) != extrai_valor(l):
                lr = []

            if extrai_naipe(k) == extrai_naipe(l) or extrai_valor(k) == extrai_valor(l):
                lr.append(1)
                
            if extrai_naipe(k) == extrai_naipe(m) or extrai_valor(k) == extrai_valor(m):
                lr.append(3)

    
    return lr 

