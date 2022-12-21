import sys
import math

case = sys.argv[1]

if case == "A":
    print(int(sys.argv[2]) + int(sys.argv[3]) + int(sys.argv[4]))

if case == "B":
    sum = 0
    for x in range (2,len(sys.argv)):
        sum = sum + int(sys.argv[x])
    print(sum)
    
if case == "C":
    div_list = []
    for x in range (2,len(sys.argv)):
        if(int(sys.argv[x]) % 3 == 0):
            div_list.append(sys.argv[x])
    print(div_list)

if case == "D":
    num1 = 0
    num2 = 1
    fib_list = []
    for x in range (1,int(sys.argv[2])+ 1):
        fib_list.append(num2)
        saver = num1
        num1 = num2
        num2 = saver + num2
        x = x + 1
    print(fib_list)

if case == "E":
    int1 = int(sys.argv[2])
    int2 = int(sys.argv[3])
    if 2 <= int1 <= 5:
        print((int1 * int1 - 3 * int1 + 2))
    if 2 <= int2 <= 5:
        print((int2 * int2 - 3 * int2 + 2))
    
if case == "F":
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    c = float(sys.argv[4])

    if a+b>=c and b+c>=a and a+c>=b:
        s = (a+b+c)/2
        area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
        print(area)
    else:
        print('Invalid triangle')

if case == "G":
    vow = sys.argv[2]
    vowels = set("aeiouAEIOU")
    vowdict = {'a': 0, 'e': 0, 'i':0,'o':0, 'u':0}
    for alphabet in vow:
        if alphabet in vowels:
            if alphabet == 'a' or alphabet == 'A':
                vowdict['a'] = int(vowdict['a']) + 1
            if alphabet == 'e' or alphabet == 'E':
                vowdict['e'] = int(vowdict['e']) + 1
            if alphabet == 'i' or alphabet == 'I':
                vowdict['i'] = int(vowdict['i']) + 1
            if alphabet == 'o' or alphabet == 'O':
                vowdict['o'] = int(vowdict['o']) + 1
            if alphabet == 'u' or alphabet == 'U':
                vowdict['u'] = int(vowdict['u']) + 1
    print(vowdict)
