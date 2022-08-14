import time
import random

def equationseperate(equationstr):
    donea = -1
    equation = ''
    for i in range(len(equationstr)):
        if donea == -1:
            if equationstr[i] != '=':
                equation += equationstr[i]
            else:
                donea = i
    result = equationstr[donea+1:]
    return [equation, result]

def basic4(a,b,calctype):
    if calctype == '+':
        return a + b
    elif calctype == '-':
        return a - b
    elif calctype == '*':
        return a * b
    elif calctype == '/':
        if b != 0:
            if a%b != 0:
                #print('Error: Non integer result from division')
                return random.randint(14531920,19201453)
            else:
                return a // b
        else:
            #print('Error: Division by 0')
            return random.randint(14531920,19201453)

def operatorcount(s):
    res = 0
    for op in s:
        if op in '+-*/':
            res += 1
    return res

def operatorseperate(equation):
    numbers = []
    numtemp = ''
    operators = {}
    for i in range(len(equation)):
        if equation[i] in '+-*/':
            numbers.append(numtemp)
            numtemp = ''
            first = numbers[len(numbers) - 1]
            temp = ''
            tempcontinue = True
            for j in range(len(equation))[i + 1:]:
                if equation[j] not in '+-*/' and tempcontinue:
                    temp += equation[j]
                else:
                    tempcontinue = False
            second = temp
            operators[equation[i]] = (first, second, equation[i])
        elif equation[i] in '0123456789':
            numtemp += equation[i]
    numbers.append(numtemp)
    return [numbers, operators]

def ordercheck(equation):
    numop = operatorseperate(equation)
    for op in numop[1]:
        if op in '*/':
            return numop[1][op]
    return -1

def replace_part(equation, part):  #part = tuple (a,b,calctype)
    a,b,c = part
    res = ''
    partcheck = a + c + b
    removed = False
    added = False
    for i in range(len(equation)):
        if not removed:
            if equation[i:i + len(partcheck)] == partcheck:
                res += str(basic4(int(a),int(b),c))
                removed = True
                restarti = i + len(partcheck)
            else:
                res += equation[i]
        else:
            if i > restarti - 1:
                res += equation[i]
    return res

def calculate_rec(equation):
    if equation == '':
        return -1
    numop = operatorseperate(equation)
    if '' in numop[0] or '' in numop[1]:
        return -2
    if operatorcount(equation) == 0:
        return int(equation)
    elif operatorcount(equation) == 1:
        return basic4(int(numop[0][0]), int(numop[0][1]), [op for op in numop[1]][0])
    else:
        if ordercheck(equation) != -1:
            return calculate_rec(replace_part(equation,ordercheck(equation)))
        else:
            return calculate_rec(replace_part(equation,(numop[0][0], numop[0][1], [op for op in numop[1]][0])))

def equalscheck(equation):
    equalscount = 0
    for a in equation:
        if a == '=':
            equalscount += 1
    if equalscount > 1:
        return False
    return True

def truthcheck(equation):
    return calculate_rec(equationseperate(equation)[0]) == calculate_rec(equationseperate(equation)[1])
    
def misplacedcheck(misplaced, equation):
    for m in misplaced:
        if m not in equation:
            return False
    return True

def operatornexttooperatorcheck(equation):
    for o in range(len(equation)):
        if equation[o] in '+-*/=':
            if equation[o-1] in '+-*/=' or equation[o+1] in '0+-*/=':
                return False
    return True

def alloptions(given, misplaced, taken):
    timestart = time.time()
    equation = ''
    infoind = []
    infochr = []
    res = []
    i= 0
    options = [[a for a in '123456789' if a not in taken]]
    options.append([a for a in '0123456789+-*/' if a not in taken])
    options.append([a for a in '0123456789+-*/' if a not in taken])
    options.append([a for a in '0123456789+-*/' if a not in taken])
    options.append([a for a in '0123456789+-*/=' if a not in taken])
    options.append([a for a in '0123456789=' if a not in taken])
    options.append([a for a in '0123456789=' if a not in taken])
    options.append([a for a in '0123456789' if a not in taken])
    for g in given:
        for gi in given[g]:
            options[gi] = [g]
    infoind += [[l for l in misplaced[k]] for k in misplaced]
    infochr += [k for k in misplaced]
    for ind in range(len(infoind)):
        for indind in range(len(infoind[ind])):
            if len(options[infoind[ind][indind]]) != 1:
                options[infoind[ind][indind]] = [a for a in [b for b in options[infoind[ind][indind]]] if (a not in taken) and (a != infochr[ind][0])]
    for a1 in range(len(options[0])):
        for a2 in range(len(options[1])):
            for a3 in range(len(options[2])):
                for a4 in range(len(options[3])):
                    for a5 in range(len(options[4])):
                        for a6 in range(len(options[5])):
                            for a7 in range(len(options[6])):
                                for a8 in range(len(options[7])):
                                    equation += options[0][a1]
                                    equation += options[1][a2]
                                    equation += options[2][a3]
                                    equation += options[3][a4]
                                    equation += options[4][a5]
                                    equation += options[5][a6]
                                    equation += options[6][a7]
                                    equation += options[7][a8]
                                    #print(equation) #-   (to debug, will spam)
                                    i += 1
                                    if '=' in equation and equalscheck(equation) and operatorcount(equationseperate(equation)[1]) == 0 and operatornexttooperatorcheck(equation) and misplacedcheck(misplaced,equation) and (truthcheck(equation)):
                                        print(equation)
                                        res.append(equation)
                                    equation = ''
    print('--------------------------------------------------')
    print(' ')
    print('Iterated through ' + str(i) + ' 8 number/operator combinations.')
    timeend = time.time()
    if timeend - timestart < 60:
        print('Took ' + str(round(timeend - timestart, 4)) + ' seconds')
    else:
        print('Took ' + str(int((timeend - timestart)//60)) + ' minutes and ' + str(round((timeend-timestart)%60, 4)) + ' seconds.')
    if len(res) == 0:
        print('No possible answers fit this criteria.')
        return len(res)
    elif len(res) == 1:
        print('One possible answer.')
        return len(res)
    print(str(len(res)) + ' possible answers.')
    print(' ')
    return len(res)

def main():
    print('Enter the given numbers/operators (for example: \'4\') and then their position in the word (1 to 8)')
    givencontinue = True
    misplacedcontinue = True
    takencontinue = True
    given = {}
    misplaced = {}
    taken = set()
    givenletterposs = set()
    while givencontinue:
        print('Number/Operator? (Enter \'done\' when finished)')
        givenletter = input()
        if len(givenletter) == 1:
            if givenletter in '0123456789+-*/=':
                print('What is the position of ' + givenletter + '?')
                givenletterpos = input()
                if givenletterpos == '' or ord(givenletterpos[0]) < 48 or ord(givenletterpos[0]) > 57:
                    print('Enter a number')
                else:
                    givenletterpos = int(givenletterpos)
                    if (not givenletterpos <= 8) or (not givenletterpos >= 1):
                        print('That position is not within 1 and 8, misclick? (Enter \'done\' if not)')
                    elif (givenletterpos - 1) not in givenletterposs:
                        if givenletter not in given:
                            given[givenletter] = {givenletterpos - 1}
                        else:
                            given[givenletter].add(givenletterpos - 1)
                        for i in range(len(given)):
                            for j in [given[b] for b in given][i]:
                                givenletterposs.add(j)
                    else:
                        print('That position is full, misclick? (Enter \'done\' if not)')
            else:
                print('That is not a number/operator, misclick? (Enter \'done\' if not, anything else if it is)')
        elif givenletter == 'done':
            givencontinue = False
        else:
            print('That is not A number/operator, misclick? (Enter \'done\' if not)')
    print('Given numbers/operators: ' + str(given))
    tempreslist = ['_' for tempreslistcreate in range(8)]
    tempres = ''
    for letter in given:
        for indgi in given[letter]:
            tempreslist[indgi] = letter
    for letter2 in tempreslist:
        tempres += letter2
    print(tempres)
    print('--------------------------------------------------')
    print(' ')
    print('Enter the misplaced numbers/operators (for example: \'4\') and then their position in the word (1 to 8)')
    print('--------------------------------------------------')
    while misplacedcontinue:
        print('Number/operator? (Enter \'done\' when finished)')
        misplacedletter = input()
        if len(misplacedletter) == 1:
            if misplacedletter in '0123456789+-*/=':
                print('What is NOT the position of ' + misplacedletter + '?')
                misplacedletterpos = input()
                if misplacedletterpos == '' or ord(misplacedletterpos[0]) < 48 or ord(misplacedletterpos[0]) > 57:
                    print('Enter a number')
                else:
                    misplacedletterpos = int(misplacedletterpos)
                    if (misplacedletter in given) and (misplacedletterpos - 1 in given[misplacedletter]):
                        print('That number/operator can not both be and not be in that spot, misclick?')
                    elif (misplacedletterpos > 8) or (misplacedletterpos < 1):
                        print('That position is not within 1 and 8, misclick? (Enter \'done\' if not)')
                    else:
                        if misplacedletter not in misplaced:
                            misplaced[misplacedletter] = set()
                        if len(misplaced[misplacedletter]) >= 7:
                            print('That number/operator can not both be in the word but not be in any of the 8 slots, misclick?')
                        else:
                            misplaced[misplacedletter].add(misplacedletterpos - 1)
            else:
                print('That is not a number/operator, misclick? (Enter \'done\' if not)')
        elif misplacedletter == 'done':
            misplacedcontinue = False
        else:
            print('That is not A number/operator, misclick? (Enter \'done\' if not)')
    print('Misplaced numbers/operators: ' + str(misplaced))
    print('--------------------------------------------------')
    print(' ')
    if len({mi for mi in misplaced} | {gi for gi in given}) > 8:
        print('Among the info given, there are more correct number/operators than 8')
        return None
    print('Enter the taken letters (for example: \'a\')')
    print('--------------------------------------------------')
    while takencontinue:
        print('Number/operator? (Enter \'done\' when finished)')
        takenletter = input()
        if len(takenletter) == 1:
            if (takenletter in '0123456789+-*/=') and (takenletter not in given) and (takenletter not in misplaced) and (takenletter not in taken):
                if takenletter == '=':
                    print('= has to be in the equation')
                else:
                    taken.add(takenletter)
            elif (takenletter in given) or (takenletter in misplaced) or (takenletter in taken):
                print('That number/operator is already used as info, misclick? (Enter \'done\' if not)')
            else:
                print('That is not a number/operator, misclick? (Enter \'done\' if not)')
        elif takenletter == 'done':
            takencontinue = False
        else:
            print('That is not A number/operator, misclick? (Enter \'done\' if not)')
    print(' ')
    print('--------------------------------------------------')
    print('All given info:')
    print('Taken numbers/operators: ' + str(taken))
    print('Given: ' + str(given))
    print('Misplaced: ' + str(misplaced))
    print('--------------------------------------------------')
    print('Information set, press enter to get possible answers')
    cont = input()
    if '=' not in misplaced:
        misplaced['='] = set()
    misplaced['='].add(0)
    misplaced['='].add(7)
    if '=' in given:
        equalspos = [_ for _ in given['=']][0]
        for equals in range(8):
            if equals != equalspos:
                misplaced['='].add(equals)
    alloptions(given, misplaced, taken)

def startgame():
    print('Press enter to start game')
    a = input()
    print('--------------------------------------------------')
    print(' ')
    
def endgame():
    print('--------------------------------------------------')
    print(' ')
    print('Press enter to start new game')
    a = input()
    print('--------------------------------------------------')
    print(' ')
    main()

startgame()
main()
while True:
    endgame()
