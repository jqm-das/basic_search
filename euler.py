from ast import Num
import sys
import math


def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    else:
        for y in range (2,(int)(x**.5)+1):
            if x % y == 0:
                return False
        return True

def mult3or5():
    sum = 0
    for x in range (1,1000):
        if x % 5 == 0:
            sum = sum + x
        elif x % 3 == 0:
            sum = sum + x
    return sum

print("#1 %s" % mult3or5())

def sumevenfib():
    x = 1
    sum = 0
    while(fib(x) < 4000000):
        y = fib(x)
        if(y % 2 == 0):
            sum = sum + y
        x = x + 1
    return sum 

def fib(x):
    return 1 if x in (0,1) else fib(x-1) + fib(x-2)

print("#2: %s" % sumevenfib())

def lpf(x):
    if(is_prime(x)):
        return x
    fac = 0
    for y in range (2,(int)(x**.5)):
        if x % y == 0 and y > fac and is_prime(y):
            fac = y
    return fac

print("#3 %s" % lpf(600851475143))

def lpp():
    num = 0
    for x in range(100,1000):
        for y in range(100,1000):
            if x * y > num and str(x*y) == str(x*y)[::-1]:
                num = x * y
    return num

print("#4 %s" % lpp())

def gcd(x,y):
    if x > y:
        l = x
        s = y
    else:
        l = y
        s = x
    while l != s:
        ans = l - s
        if ans > s:
            l = ans
        else:
            l = s
            s = ans
    return l

def createOffList(list):
    l = []
    for x in range(len(list)):
        l.append(math.prod(list[0:x]+list[x+1:len(list)]))
    return l

def spn(n):
    lis = []
    prod = 1
    for i in range (2,n):
        lis.append(i)
        prod = prod * i
    offList = createOffList(lis)
    fgcf = gcd(offList[0], offList[1])
    for y in offList[2:]:
        fgcf = gcd(y,fgcf)
    return prod//fgcf
    
print("#5 %s" % spn(20))

def ssd(x):
    sum = 0 
    sumsq = 0 
    for y in range (1,x+1):
        sum = sum + y**2
        sumsq = sumsq + y
    sumsq = sumsq ** 2
    return sumsq - sum 

print("#6 %s" % ssd(100))

def findprime(n):
    count = 0
    num = 1
    while count < n:
        if is_prime(num):
            count = count + 1
        num = num + 1
    return (num - 1)

print("#7 %s" % findprime(10001))

def lps(n):
    num = "73167176531330624919225119674426574742355349194934"
    num = num + "96983520312774506326239578318016984801869478851843"
    num = num + "85861560789112949495459501737958331952853208805511"
    num = num + "12540698747158523863050715693290963295227443043557"
    num = num + "66896648950445244523161731856403098711121722383113"
    num = num + "62229893423380308135336276614282806444486645238749"
    num = num + "30358907296290491560440772390713810515859307960866"
    num = num + "70172427121883998797908792274921901699720888093776"
    num = num + "65727333001053367881220235421809751254540594752243"
    num = num + "52584907711670556013604839586446706324415722155397"
    num = num + "53697817977846174064955149290862569321978468622482"
    num = num + "83972241375657056057490261407972968652414535100474"
    num = num + "82166370484403199890008895243450658541227588666881"
    num = num + "16427171479924442928230863465674813919123162824586"
    num = num + "17866458359124566529476545682848912883142607690042"
    num = num + "24219022671055626321111109370544217506941658960408"
    num = num + "07198403850962455444362981230987879927244284909188"
    num = num + "84580156166097919133875499200524063689912560717606"
    num = num + "05886116467109405077541002256983155200055935729725"
    num = num + "71636269561882670428252483600823257530420752963450"

    great = 0

    for i in range (0, len(num)-n + 1):
        prod = 1
        for x in range (i,i+n):
            prod = prod * int(num[x:x+1])
        if prod > great: 
            great = prod 

    return great

print("#8 %s" % lps(13))

def spt(sum): 
    for a in range (1,sum):
        for b in range (1,sum):
            c = sum - a - b
            if a ** 2 + b ** 2 == c **2:
                return a * b * c
    return -1

print("#9 %s" % spt(1000))

def dp(x,y):
    l = {x**y}
    for i in range (x,y+1):
        for j in range (x,y+1):
            l.add(i ** j)
    return len(l)

print("#29 %s" % dp(2,100))
