import math
import time

def startinputs():
    res = []
    n = 0
    while str(n) not in 'done|stop|end' or str(n) == '':
        n = input("Input #" + str(len(res) + 1) + ': ')
        try:
            n = float(n)
            res.append(n)
        except:
            if str(n) not in 'done|stop|end' or str(n) == '':
                print('Enter a number.')
    print("List of inputs:", res)
    return res

def easydifcheck(inputs):
    difference = inputs[1] - inputs[0]
    for i in range(1, len(inputs) - 1):
        if difference != inputs[i + 1] - inputs[i]:
            return False
    if difference >= 0:
        return '+' + str(difference)
    else:
        return str(difference)

def easyfaccheck(inputs):
    if 0 in inputs:
        return False
    facdif = inputs[1] / inputs[0]
    for i in range(1, len(inputs) - 1):
        if facdif != inputs[i + 1] / inputs[i]:
            return False
    return '*' + str(facdif)

def anybelow0(inputs):
    for i in inputs:
        if i <= 0:
            return True
    return False

def easypowercheck(inputs):
    if 1 in inputs or anybelow0(inputs):
        return False
    power = math.log(inputs[1], inputs[0])
    for i in range(1, len(inputs) - 1):
        if power != math.log(inputs[i + 1], inputs[i]):
            return False
    return '**' + str(power)

def patterncontinue(inputs, equation, contcount):
    res = inputs
    for i in range(contcount):
        try:
            res.append(eval(str(res[len(res) - 1]) + equation))
        except OverflowError:
            #print("Number too large to compute, stopping earlier than requested")
            break
    return res

def patterncheck(inputs, equation):
    for i in range(len(inputs) - 1):
        #print(str(inputs[i]) + equation + '==' + str(inputs[i+1]))
        if not eval("(" + str(inputs[i]) + ")" + equation + '==' + str(inputs[i+1])):
            return False
    return True

def main():
    inputs = startinputs()
    contcount = int(input("How many more elements do you want to add? (enter integer): "))
    start = time.time()
    dif = easydifcheck(inputs)
    if dif:
        print(patterncontinue(inputs, dif, contcount))
        print("Found pattern:", dif, "in", round(time.time()-start, 4), "seconds.")
        return patterncontinue(inputs, dif, contcount)
    fac = easyfaccheck(inputs)
    if fac:
        print(patterncontinue(inputs, fac, contcount))
        print("Found pattern:", fac, "in", round(time.time()-start, 4), "seconds.")
        return patterncontinue(inputs, fac, contcount)
    pow = easypowercheck(inputs)
    if pow:
        print(patterncontinue(inputs, pow, contcount))
        print("Found pattern:", pow, "in", round(time.time()-start, 4), "seconds.")
        return patterncontinue(inputs, pow, contcount)
    operators = [['*', '/'], ['+', '-']]
    numbers = '0123456789'
    nonzero = '123456789'
    for a in numbers:
        zero = '**' + a
        for c in operators[0]:
            one = c
            for d in numbers:
                for e in numbers:
                    if int(d+e) != 0:
                        two = str(int(d + e))
                    else:
                        two = '1'
                    for f in operators[1]:
                        three = f
                        for g in numbers:
                            for h in numbers:
                                for i in numbers:
                                    four = str(int(g + h + i))
                                    res = zero + one + two + three + four
                                    if patterncheck(inputs, res):
                                        print(patterncontinue(inputs, res, contcount))
                                        print("Found pattern:", res, "in", round(time.time()-start, 4), "seconds.")
                                        return patterncontinue(inputs, res, contcount)
    print("Could not find pattern in", round(time.time()-start, 4), "seconds.")
    

while True:
    main()
    print('--------------------------')
