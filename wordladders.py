import sys
import math
import time
from collections import deque


case1 = sys.argv[1]
case2 = sys.argv[2]

def readLadders():
    with open(case2) as f:
        line_list = [line.strip() for line in f]
    return line_list

ladders = readLadders()

def createDict():
    with open(case1) as f:
        line_list = {line.strip() for line in f}
    return line_list

def words(n):
    words = ladders[n].split(" ")
    return words

def findAllAdj(word,d):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ls = deque()
    for x in range(0,len(word)):
        for i in letters:
            newword = word[0:x] + i + word[(x+1):len(word)]
            newword2 = word[0:x] + i + word[x:len(word)]
            if newword in d and newword != word:
                ls.append(newword)
            if newword2 in d:
                ls.append(newword2)
            newword4 = word + i
            if newword4 in d:
                ls.append(newword4)
        newword3 = word[0:x] + word[x+1:len(word)]
        if newword3 in d:
            ls.append(newword3)
    return ls

start1 = time.perf_counter()
d = createDict()
adjDict = {}

for i in d:
    adjDict[i] = findAllAdj(i,d)

def findAdj(word):
    return adjDict.get(word)

def BFS(word,goal):
    q = deque()
    theset = {word}
    ls = [word]
    q.append((word,ls))
    while q:
        s,ls0 = q.popleft()
        if s == goal:
            return ls0
        for i in findAdj(s):
            if i not in theset:
                theset.add(i)
                q.append((i,ls0+[i])) 
    return None

for n in range (0,len(ladders)): 
    start0 = time.perf_counter()
    ls = BFS(words(n)[0],words(n)[1])
    end0 = time.perf_counter()
    print("Line: %s" % n)
    if ls == None:
        print("No Solution!")
    else:
        print("Length: %s" % len(ls))
        for l in ls:
            print(l)
    print(end0-start0 )
    print("")
end1 = time.perf_counter()
print("Time to solve all puzzles: %s" % (end1-start1))

def noFriends():
    count = 0 
    friendSet = set()
    for i in d:
        if i not in friendSet:
            k = findAdj(i)
            if len(k) == 0:
                count = count + 1
            else:
                for j in k:
                    friendSet.add(j)
    return count
print("Words without friends, Count: %s" % noFriends())


def bigSub():
    length = 0 
    already = set()
    q = deque()
    for i in d:
        if i not in already:
            words = [i]
            q.append((i))
            already.add(i)
            count = 0 
            while q:
                j = q.popleft()
                count = count + 1
                for k in findAdj(j):
                    if k not in already:
                        q.append((k))
                        already.add(k)
                        words = words + [k]
                if count > length:
                    length = count
                    clump = words
    return length,clump
length,clump = bigSub()
print("The biggest subcomponent word count: %s" % length)

def comCount():
    count = 0 
    visitedSet = set()
    q = deque()
    clump = deque()
    for i in d:
        if i not in visitedSet:
            if len(findAdj(i)) != 0:
                count = count + 1
                clump.append(i)
                visitedSet.add(i)
                q.append(i)
                hold = set()
                hold.add(i)
                while q:
                    word = q.popleft()
                    for j in findAdj(word):
                        if j not in hold:
                            q.append(j)
                            visitedSet.add(j)
                            hold.add(j)
    return count

count = comCount()
print("Subcomponent Count: %s" % count)

def idealPath(clump):
    maxlength = 0 
    q = deque()
    i = clump[20]
    words = [i]
    q.append((i,0,[i]))
    already = set()
    already.add(i)
    while q:
        j,count,words = q.popleft()
        for k in findAdj(j):
            if k not in already:
                q.append((k,count+1,words+[k]))
                already.add(k)
        if count > maxlength:
            longword = j
            maxlength = count
    path = [longword]
    maxlength = 0
    visited = set()
    q.append((longword,0,path))
    visited.add(longword)
    while q:
        j,count,words = q.popleft()
        if count > maxlength:
            path = words
            maxlength = count
        for k in findAdj(j):
            if k not in visited:
                q.append((k,count+1,words+[k]))
                visited.add(k)
        
    return len(path),path

ideal,path = idealPath(clump)

for i in path:
    print(i)
print("Ideal path length: %s" % ideal)
