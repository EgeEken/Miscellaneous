from english_words import english_words_lower_set
import time

wordliststr = set()

for word in english_words_lower_set:
        if len(word) == 5:
            wordliststr.add(word)

def misplacedcheck(misplaced, word):
    for m in misplaced:
        if m not in word:
            return False
    return True

def alloptions(given, misplaced, taken):
    '''given dict str: set[int], misplaced: dict str: set[int], taken: set str'''
    timestart = time.time()
    word = ''
    infoind = []
    infochr = []
    res = []
    i= 0
    alphabet = [[chr(a + 97) for a in range(26) if chr(a+97) not in taken] for five in range(5)]
    for g in given:
        for gi in given[g]:
            alphabet[gi] = [g]
    infoind += [[l for l in misplaced[k]] for k in misplaced]
    infochr += [k for k in misplaced]
    for ind in range(len(infoind)):
        for indind in range(len(infoind[ind])):
            if len(alphabet[infoind[ind][indind]]) != 1:
                alphabet[infoind[ind][indind]] = [chr(a + 97) for a in range(26) if (chr(a+97) not in taken) and (chr(a+97) != infochr[ind][0])]
    for a1 in range(len(alphabet[0])):
        for a2 in range(len(alphabet[1])):
            for a3 in range(len(alphabet[2])):
                for a4 in range(len(alphabet[3])):
                    for a5 in range(len(alphabet[4])):
                        word += alphabet[0][a1]
                        word += alphabet[1][a2]
                        word += alphabet[2][a3]
                        word += alphabet[3][a4]
                        word += alphabet[4][a5]
                        #print(word) -   (to debug, will spam)
                        i += 1
                        if (word in wordliststr) and misplacedcheck(misplaced,word):
                            print(word)
                            res.append(word)
                        word = ''        
    print('--------------------------------------------------')
    print(' ')
    print('Iterated through ' + str(i) + ' 5 letter combinations.')
    timeend = time.time()
    print('Took ' + str(round(timeend - timestart, 4)) + ' seconds')
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
    print('Enter the given letters (for example: \'a\') and then their position in the word (1 to 5)')
    givencontinue = True
    misplacedcontinue = True
    takencontinue = True
    given = {}
    misplaced = {}
    taken = set()
    givenletterposs = set()
    while givencontinue:
        print('Letter? (Enter \'done\' when finished)')
        givenletter = input()
        givenletter = givenletter.lower()
        if len(givenletter) == 1:
            if (ord(givenletter) >= 97) and (ord(givenletter) <= 122):
                print('What is the position of ' + givenletter + '?')
                givenletterpos = input()
                if givenletterpos == '' or ord(givenletterpos[0]) < 48 or ord(givenletterpos[0]) > 57:
                    print('Enter a number')
                else:
                    givenletterpos = int(givenletterpos)
                    if (not givenletterpos <= 5) or (not givenletterpos >= 1):
                        print('That position is not within 1 and 5, misclick? (Enter \'done\' if not)')
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
                print('That is not a letter, misclick? (Enter \'done\' if not, anything else if it is)')
        elif givenletter == 'done':
            givencontinue = False
        else:
            print('That is not A letter, misclick? (Enter \'done\' if not)')
    print('Given letters: ' + str(given))
    tempreslist = ['_','_','_','_','_']
    tempres = ''
    for letter in given:
        for indgi in given[letter]:
            tempreslist[indgi] = letter
    for letter2 in tempreslist:
        tempres += letter2
    print(tempres)
    if len(given) == 5:
        print('You gave all of the correct letters')
        wtflist = ['','','','','']
        wtfres = ''
        for wtf in given:
            for wtfgi in given[wtf]:
                wtflist[wtfgi] = wtf
        for wtfwtf in wtflist:
            wtfres += wtfwtf
        print(wtfres)
        return None
    print('--------------------------------------------------')
    print(' ')
    print('Enter the misplaced letters (for example: \'a\') and then their position in the word (1 to 5)')
    print('--------------------------------------------------')
    while misplacedcontinue:
        print('Letter? (Enter \'done\' when finished)')
        misplacedletter = input()
        misplacedletter = misplacedletter.lower()
        if len(misplacedletter) == 1:
            if (ord(misplacedletter) >= 97) and (ord(misplacedletter) <= 122):
                print('What is NOT the position of ' + misplacedletter + '?')
                misplacedletterpos = input()
                if misplacedletterpos == '' or ord(misplacedletterpos[0]) < 48 or ord(misplacedletterpos[0]) > 57:
                    print('Enter a number')
                else:
                    misplacedletterpos = int(misplacedletterpos)
                    if (misplacedletter in given) and (misplacedletterpos - 1 in given[misplacedletter]):
                        print('That letter can not both be and not be in that spot, misclick?')
                    elif (misplacedletterpos > 5) or (misplacedletterpos < 1):
                        print('That position is not within 1 and 5, misclick? (Enter \'done\' if not)')
                    else:
                        if misplacedletter not in misplaced:
                            misplaced[misplacedletter] = set()
                        if len(misplaced[misplacedletter]) >= 4:
                            print('That letter can not both be in the word but not be in any of the 5 slots, misclick?')
                        else:
                            misplaced[misplacedletter].add(misplacedletterpos - 1)
            else:
                print('That is not a letter, misclick? (Enter \'done\' if not)')
        elif misplacedletter == 'done':
            misplacedcontinue = False
        else:
            print('That is not A letter, misclick? (Enter \'done\' if not)')
    print('Misplaced letters: ' + str(misplaced))
    print('--------------------------------------------------')
    print(' ')
    if len({mi for mi in misplaced} | {gi for gi in given}) > 5:
        print('Among the info given, there are more correct letters than 5')
        return None
    print('Enter the taken letters (for example: \'a\')')
    print('--------------------------------------------------')
    while takencontinue:
        print('Letter? (Enter \'done\' when finished)')
        takenletter = input()
        takenletter = takenletter.lower()
        if len(takenletter) == 1:
            if (ord(takenletter) >= 97) and (ord(takenletter) <= 122) and (takenletter not in given) and (takenletter not in misplaced) and (takenletter not in taken):
                taken.add(takenletter)
            elif (takenletter in given) or (takenletter in misplaced) or (takenletter in taken):
                print('That letter is already used as info, misclick? (Enter \'done\' if not)')
            else:
                print('That is not a letter, misclick? (Enter \'done\' if not)')
        elif takenletter == 'done':
            takencontinue = False
        else:
            print('That is not A letter, misclick? (Enter \'done\' if not)')
    print(' ')
    print('--------------------------------------------------')
    print('All given info:')
    print('Taken letters: ' + str(taken))
    print('Given: ' + str(given))
    print('Misplaced: ' + str(misplaced))
    print('--------------------------------------------------')
    deduce = False
    gmismmischeck = False
    for gmis in given:
        for mmis in misplaced:
            if mmis != gmis:
                misplaced[mmis] = misplaced[mmis] | given[gmis]
                if len(misplaced[mmis]) > 4:
                    print('Something is wrong with the info you gave for ' + mmis + ', as it stands, it\'s in the word but it\'s not in any of the 5 slots, try again.')
                    return None
                gmismmischeck = True
                deduce = True
    findeduce = False
    for mfin in misplaced:
        if len(misplaced[mfin]) == 4:
            misgiven = [veryspecific for veryspecific in {0,1,2,3,4} - misplaced[mfin]]
            if mfin not in given:
                given[mfin] = set()
            given[mfin].add(misgiven[0])
            if len(given) > 5 or len({giv for giv in given} | {mis for mis in misplaced}) > 5:
                print('Something is wrong with the info you gave, as it stands, it has more than 5 different correct letters, try again.')
                return None
            findeduce = True
            deduce = True
    if len({giv for giv in given} | {mis for mis in misplaced}) == 5: #double check
        for gmis2 in given:
            for mmis2 in misplaced:
                if mmis2 != gmis2:
                    misplaced[mmis2] = misplaced[mmis2] | given[gmis2]
        for mfin2 in misplaced:
            if len(misplaced[mfin2]) == 4:
                misgiven2 = [veryspecific2 for veryspecific2 in {0,1,2,3,4} - misplaced[mfin2]]
                if mfin2 not in given:
                    given[mfin2] = set()
                given[mfin2].add(misgiven2[0])
    if deduce:
        print('All deduced info:')
        if gmismmischeck:
            print('Misplaced (Deduced info from a character being forced to not be in a given slot): ' + str(misplaced))
        if findeduce:
            print('Given (Deduced info from a character being misplaced in 4 slots): ' + str(given))
        print('--------------------------------------------------')
        print(' ')
    if len(given) == 5:
        winnerlist = ['','','','','']
        winnerres = ''
        for winner in given:
            winnerlist[given[winner]] = winner
        for winnerwinner in winnerlist:
            winnerres += winnerwinner
        print('We have all 5 slots, the answer is: ' + winnerres + '.')
        if winnerres not in wordliststr:
            print('However that is not in the word list, so you probably gave some wrong info')
        return None
    print('Information set, press enter to get possible answers')
    cont = input()
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
