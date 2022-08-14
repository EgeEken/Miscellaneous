from english_words import english_words_lower_set
import time

def givencheck(given, word):
    for g in given:
        for i in given[g]:
            if word[i] != g:
                return False
    return True

def misplacedcheck(misplaced, word):
    for m in misplaced:
        if m not in word:
            return False
        else:
            for i in misplaced[m]:
                if word[i] == m:
                    return False
    return True

def takencheck(taken, word):
    for t in taken:
        if t in word:
            return False
    return True

def alloptions(given, misplaced, taken,wordlist):
    '''given dict str: set[int], misplaced: dict str: set[int], taken: set str'''
    res = []
    i= 0
    i += 1
    length = str(len(next(iter(wordlist))))
    timestart = time.time()
    for wordcheck in wordlist:
        if givencheck(given,wordcheck) and misplacedcheck(misplaced,wordcheck) and takencheck(taken,wordcheck):
            print(wordcheck)
            res.append(wordcheck)      
    print('--------------------------------------------------')
    print(' ')
    timeend = time.time()
    print('Took ' + str(round(timeend - timestart, 4)) + ' seconds to iterate through the list of ' + length + ' letter words')
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
    wordlist = set()
    lettercountcontinue = True
    print('How many letters?')
    while lettercountcontinue:
        lettercount = input()
        if lettercount == '':
            print('Enter a number')
        elif ord(lettercount[0]) >= 48 and ord(lettercount[0]) <= 57:
            lettercount = int(lettercount)
            lettercountcontinue = False
        else:
            print('Enter a number')
    timebeforestart = time.time()
    for word in english_words_lower_set:
        if len(word) == lettercount:
            wordlist.add(word)
    timestart = time.time()
    print('Took ' + str(round(timestart - timebeforestart, 4)) + ' seconds to create the list')
    print('Enter the given letters (for example: \'a\') and then their position in the word (1 to ' + str(lettercount) + ')')
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
                    if (not givenletterpos <= lettercount) or (not givenletterpos >= 1):
                        print('That position is not within 1 and ' + str(lettercount) + ', misclick? (Enter \'done\' if not)')
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
    tempreslist = ['_' for tempreslistcreate in range(lettercount)]
    tempres = ''
    for letter in given:
        for indgi in given[letter]:
            tempreslist[indgi] = letter
    for letter2 in tempreslist:
        tempres += letter2
    print(tempres)
    if len(given) == lettercount:
        print('You gave all of the correct letters')
        wtflist = ['' for wtflistcreate in range(lettercount)]
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
    print('Enter the misplaced letters (for example: \'a\') and then their position in the word (1 to ' + str(lettercount) + ' )')
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
                    elif (misplacedletterpos > lettercount) or (misplacedletterpos < 1):
                        print('That position is not within 1 and ' + str(lettercount) + ', misclick? (Enter \'done\' if not)')
                    else:
                        if misplacedletter not in misplaced:
                            misplaced[misplacedletter] = set()
                        if len(misplaced[misplacedletter]) >= lettercount-1:
                            print('That letter can not both be in the word but not be in any of the ' + str(lettercount) + ' slots, misclick?')
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
    if len({mi for mi in misplaced} | {gi for gi in given}) > lettercount:
        print('Among the info given, there are more correct letters than ' + str(lettercount))
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
    print('Information set, press enter to get possible answers')
    cont = input()
    alloptions(given, misplaced, taken, wordlist)
    

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
