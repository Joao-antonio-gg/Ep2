import EP2_2


class bcolors:
 purple = '\033[95m'
 blue = '\033[94m'
 green = '\033[92m'
 yellow = '\033[93m'
 red = '\033[91m'
 cyan = '\033[96m'
 white = '\033[97m'
 grey = '\033[90m'
 end = '\033[0m'
 bold = '\033[1m'
 underline = '\033[4m'

def cores(n):
    if EP2_2.extrai_naipe(n) == '♠':
        return bcolors.purple + n + bcolors.end
    if EP2_2.extrai_naipe(n) == '♥':
        return bcolors.red + n + bcolors.end
    if EP2_2.extrai_naipe(n) == '♣':
        return bcolors.green + n + bcolors.end
    if EP2_2.extrai_naipe(n) == '♦':
        return bcolors.yellow + n + bcolors.end
    else:
        return bcolors.cyan + n + bcolors.end
