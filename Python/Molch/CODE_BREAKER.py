import random
Molch = ""

ErM = (input('Would you like to ENCRYPT english (E) or DECODE Molch(M)'))
if ErM == 'M':
    Molch = str(input('Please Enter Your Molch here'))
    result = Molch.replace('1', '')
    Molch = result
    result = Molch.replace('2', '')
    Molch = result
    result = Molch.replace('3', '')
    Molch = result
    result = Molch.replace('4', '')
    Molch = result
    result = Molch.replace('5', '')
    Molch = result
    result = Molch.replace('6', '')
    Molch = result
    result = Molch.replace('7', '')
    Molch = result
    result = Molch.replace('8', '')
    Molch = result
    result = Molch.replace('9', '')
    Molch = result
    result = Molch.replace('0', '')
    Molch = result
    result = Molch.replace('~', '')
    Molch = result
    result = Molch.replace('/', '')
    Molch = result
    result = Molch.replace('<', '')
    Molch = result
    result = Molch.replace('>', '')
    Molch = result
    result = Molch.replace('|', '')
    Molch = result
    result = Molch.replace('?', '')
    Molch = result
    result = Molch.replace('/', '')
    Molch = result
    result = Molch.replace('-', '')
    Molch = result
    result = Molch.replace('=', '')
    Molch = result
    result = Molch.replace('+', '')
    Molch = result

    result = Molch.replace('"^', 'z')
    Molch = result
    result = Molch.replace('"%', 'y')
    Molch = result
    result = Molch.replace('"$', 'x')
    Molch = result
    result = Molch.replace('"£', 'w')
    Molch = result
    result = Molch.replace('""', 'v')
    Molch = result
    result = Molch.replace('"!', 'u')
    Molch = result
    result = Molch.replace('")', 't')
    Molch = result
    result = Molch.replace('!(', 's')
    Molch = result
    result = Molch.replace('!*', 'r')
    Molch = result
    result = Molch.replace('!&', 'q')
    Molch = result
    result = Molch.replace('!^', 'p')
    Molch = result
    result = Molch.replace('!%', 'o')
    Molch = result
    result = Molch.replace('!$', 'n')
    Molch = result
    result = Molch.replace('!£', 'm')
    Molch = result
    result = Molch.replace('!"', 'l')
    Molch = result
    result = Molch.replace('!!', 'k')
    Molch = result
    result = Molch.replace('!)', 'j')
    Molch = result
    result = Molch.replace('(', 'i')
    Molch = result
    result = Molch.replace('*', 'h')
    Molch = result
    result = Molch.replace('&', 'g')
    Molch = result
    result = Molch.replace('^', 'f')
    Molch = result
    result = Molch.replace('%', 'e')
    Molch = result
    result = Molch.replace('$', 'd')
    Molch = result
    result = Molch.replace('£', 'c')
    Molch = result
    result = Molch.replace('"', 'b')
    Molch = result
    result = Molch.replace('!', 'a')
    Molch = result






    result = Molch.replace('@', '')
    Molch = result
    result = Molch.replace('#', ' ')
    Molch = result

    print(result)

else:
    decoy = ['1','2','3','4','5','6','7','8','9','0','~','/','<','>','|','?','/','-','=','+',]
    Molch = str(input('Please Enter Your English here'))
    length = len(Molch.replace(' ',''))
    print(length)
    result = Molch.replace('z', '"^@')
    Molch = result
    result = Molch.replace('y', '"%@')
    Molch = result
    result = Molch.replace('x', '"$@')
    Molch = result
    result = Molch.replace('w', '"£@')
    Molch = result
    result = Molch.replace('v', '""@')
    Molch = result
    result = Molch.replace('u', '"!@')
    Molch = result
    result = Molch.replace('t', '")@')
    Molch = result
    result = Molch.replace('s', '!(@')
    Molch = result
    result = Molch.replace('r', '!*@')
    Molch = result
    result = Molch.replace('q', '!&@')
    Molch = result
    result = Molch.replace('p', '!^@')
    Molch = result
    result = Molch.replace('o', '!%@')
    Molch = result
    result = Molch.replace('n', '!$@')
    Molch = result
    result = Molch.replace('m', '!£@')
    Molch = result
    result = Molch.replace('l', '!"@')
    Molch = result
    result = Molch.replace('k', '!!@')
    Molch = result
    result = Molch.replace('j', '!)@')
    Molch = result
    result = Molch.replace('i', '(@')
    Molch = result
    result = Molch.replace('h', '*@')
    Molch = result
    result = Molch.replace('g', '&@')
    Molch = result
    result = Molch.replace('f', '^@')
    Molch = result
    result = Molch.replace('e', '%@')
    Molch = result
    result = Molch.replace('d', '$@')
    Molch = result
    result = Molch.replace('c', '£@')
    Molch = result
    result = Molch.replace('b', '"@')
    Molch = result
    result = Molch.replace('a', '!@')
    Molch = result

    result = Molch.replace(' ', '#')
    Molch = result

    for i in range(length):
        irand = random.randrange(0, len(Molch))
        irand_decoy = random.randrange(0,19)

        Molch = "".join((Molch[:irand], decoy[irand_decoy], Molch[irand:]))

    print(Molch)










