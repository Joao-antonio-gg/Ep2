def extrai_naipe(card):
    if card == 'A♦' or card =='2♦' or card =='3♦' or card =='4♦' or card =='5♦' or card =='6♦' or card =='7♦' or card =='8♦' or card =='9♦' or card =='10♦' or card =='J♦' or card =='K♦' or card =='Q♦':
        return '♦'
    if card == 'A♠' or card =='2♠' or card =='3♠' or card =='4♠' or card =='5♠' or card =='6♠' or card =='7♠' or card =='8♠' or card =='9♠' or card =='10♠' or card =='J♠' or card =='K♠' or card =='Q♠':
        return '♠' 
    if card == 'A♥' or card =='2♥' or card =='3♥' or card =='4♥' or card =='5♥' or card =='6♥' or card =='7♥' or card =='8♥' or card =='9♥' or card =='10♥' or card =='J♥' or card =='K♥' or card =='Q♥':
        return '♥'
    if card == 'A♣' or card =='2♣' or card =='3♣' or card =='4♣' or card =='5♣' or card =='6♣' or card =='7♣' or card =='8♣' or card =='9♣' or card =='10♣' or card =='J♣' or card =='K♣' or card =='Q♣':
        return '♣'