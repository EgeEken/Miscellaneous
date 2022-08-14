from english_words import english_words_lower_set

while True:
    a = input('Word: ')
    truth = a in english_words_lower_set
    if truth:
        print('Yes')
    if not truth:
        print('No')
    print('-----------------------------')
