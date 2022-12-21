import sys
import math
import time
import heapq
from collections import deque

case = sys.argv[1]

def read():
    with open(case) as f:
        line_list = [line.strip() for line in f]
    return line_list

puzzles = read()
numofpuzz = len(puzzles)
def puzzle(n):
    ls = puzzles[n].split(" ")
    return ls[1]

def findType(n):
    ls = puzzles[n].split(" ")
    return ls[2]

def print_initial(n):
    str = puzzles[n]
    return print_puzzle(str[:])

def find_goal(str):
    sort = sorted(str)
    key = "".join(sort)
    key = key[1:len(key)] + key[0:1]
    return key

def print_proper(n):
    return print_puzzle(find_goal(n))

def print_puzzle(s):
    length = int(len(s) ** .5)
    z = 0 
    output = ""
    for x in range (0,length):
        for y in range (0,length):
            output = output + (s[z]) + " "
            z = z + 1
        output = output + "\n"
    return output

def up(s):

    length = int(len(s) ** .5)
    ind = s.find(".")
    if ind - length < 0:
        return s
    else:
        return s[0:ind-length] + s[ind:ind+1] + s[ind-length+1:ind] + s[ind-length:ind-length+1]+ s[ind+1:len(s)]

def down(s):
    length = int(len(s) ** .5)
    ind = s.find(".")
    if ind + length >= len(s):
        return s
    else:
        return s[0:ind] + s[ind+length:ind+length+1] + s[ind+1:ind+length] + s[ind:ind+1] + s[ind+length+1:len(s)]

def left(s):
    length = int(len(s) ** .5)
    ind = s.find(".")
    if ind % length == 0:
        return s
    else:
        return s[0:ind-1] + s[ind:ind+1] + s[ind-1:ind] + s[ind+1:len(s)]

def right(s):
    length = int(len(s) ** .5)
    ind = s.find(".")
    if ind % length == (length - 1):
        return s
    else:
        return s[0:ind] + s[ind+1:ind+2] + s[ind:ind+1] + s[ind+2:len(s)]

def goal_test(n,s):
    if find_goal(n) == s:
        return True
    else:
        return False 

def get_children(str):
    list = []
    y = str
    uppuzz = up(y)
    if uppuzz != y:
        list.append(uppuzz)
    downpuzz = down(y)
    if downpuzz != y:
        list.append(downpuzz)
    leftpuzz = left(y)
    if leftpuzz != y:
        list.append(leftpuzz)
    rightpuzz = right(y)
    if rightpuzz != y:
        list.append(rightpuzz)
    return list 

def print_children(l):
    output = ""
    for s in l:
        output = output + print_puzzle(s)
        output = output + "\n"
    return output
        
def BFS(start):
    q = deque()
    theset = {start}
    s = print_puzzle(start)
    goal = find_goal(start)
    q.append((start,0,[s]))
    while q:
        node,count,ls = q.popleft()
        if node == find_goal(start):
            return count
        for n in get_children(node):
            if n not in theset:
                s = print_puzzle(n)
                q.append((n,count+1,ls+[s]))
                theset.add(n)
    return None

def KDFS(start, k):
    stack = []
    s = print_puzzle(start)
    goal = find_goal(start)
    stack.append((start,0,{start}))
    while stack:
        node,count,theset = stack.pop()
        if node == goal:
            return count
        if count < k:
            for n in get_children(node):
                if n not in theset:
                    s = print_puzzle(n)
                    newset = theset.copy()
                    newset.add(n)
                    stack.append((n,count+1,newset))
                    theset.add(n)
    return None

def IDDFS(start):
    max_depth = 0 
    result = None
    while result is None:
        result = KDFS(start,max_depth)
        max_depth = max_depth + 1
    return result 

def parity(puzz):
    length = int(len(puzz) ** .5)
    goal = find_goal(puzz)
    count = 0 
    for first in range (0,(length**2)-2):
        place = puzz.find(goal[first])
        for second in range (first+1,(length**2)-1):
            if place > puzz.find(goal[second]):
                count = count + 1
    row = puzz.find(".") // length
    if length ==5:
        if count % 2 == 0:
            return True
    elif length == 4:
        if(row % 2 != 0 and count % 2 == 0) or (row % 2 == 0 and count % 2 != 0):
            return True
    elif length == 3:
        if count % 2 == 0:
            return True
    elif length == 2:
        if count % 2 != 0:
            return True
    return False


def edit(puzz):
    if "A" in puzz:
        puzz = puzz.replace("A","1")
        puzz = puzz.replace("B","2")
        puzz = puzz.replace("1","B")
        puzz = puzz.replace("2","A")
    else:
        puzz = puzz.replace("1","A")
        puzz = puzz.replace("2","B")
        puzz = puzz.replace("A","2")
        puzz = puzz.replace("B","1")
    return puzz

def cabDist(puzz):
    length = int(len(puzz) ** .5)
    goal = find_goal(puzz)
    count = 0 
    for place in range (0,(length**2)-1):
        act = puzz.find(goal[place])
        rowplace = place % length
        columnplace = place // length
        rowact = act % length
        columnact = act // length
        rowdiff= rowplace - rowact
        columndiff = columnplace - columnact
        count = count + abs(rowdiff) + abs(columndiff)
    return count 

def a_star(start):
    goal = find_goal(start)
    theset = set()
    fringe = []
    heapq.heappush(fringe,(cabDist(start),start,0))
    while fringe:
        heuristic,node,count = heapq.heappop(fringe)
        if node == goal:
            return count
        if node not in theset:
            theset.add(node)
            for i in get_children(node):
                if i not in theset:
                    heapq.heappush(fringe,(count + 1 + cabDist(i),i,count + 1))
    return None

for i in range (0,numofpuzz):
    type = findType(i)
    if(parity(puzzle(i))):
        if type == "!":
            start = time.perf_counter()
            count = BFS(puzzle(i))
            end = time.perf_counter()
            print("Line " + str(i) + ": %s" % puzzle(i) + ", BFS - "+ str(count) + " moves found in " + str(end-start) + " seconds")
            start = time.perf_counter()
            count = IDDFS(puzzle(i))
            end = time.perf_counter()
            print("Line " + str(i) + ": %s" % puzzle(i) + ", ID-DFS - "+ str(count) + " moves found in " + str(end-start) + " seconds")
            start = time.perf_counter()
            count = a_star(puzzle(i))
            end = time.perf_counter()
            print("Line " + str(i) + ": %s" % puzzle(i) + ", A* - "+ str(count) + " moves found in " + str(end-start) + " seconds")
        if type == "B":
            start = time.perf_counter()
            count = BFS(puzzle(i))
            end = time.perf_counter()
            print("Line " + str(i) + ": %s" % puzzle(i) + ", BFS - "+ str(count) + " moves found in " + str(end-start) + " seconds")
        if type == "I":
            start = time.perf_counter()
            count = IDDFS(puzzle(i))
            end = time.perf_counter()
            print("Line " + str(i) + ": %s" % puzzle(i) + ", ID-DFS - "+ str(count) + " moves found in " + str(end-start) + " seconds")
        if type == "A":
            start = time.perf_counter()
            count = a_star(puzzle(i))
            end = time.perf_counter()
            print("Line " + str(i) + ": %s" % puzzle(i) + ", A* - "+ str(count) + " moves found in " + str(end-start) + " seconds")
    else:
        start = time.perf_counter()
        parity(puzzle(i))
        end = time.perf_counter()
        print("Line " + str(i) + ": %s" % puzzle(i) + ", no solution determined in " + str(end-start) + " seconds")
    print("")

#for i in range (0,numofpuzz):
 #   start = time.perf_counter()
  #  count, ls = BFS(puzzle(i))
   # end = time.perf_counter()
   # print("Line " + str(i) + ": %s" % puzzle(i) + ", "+ str(count) + " moves found in " + str(end-start) + " seconds")
   # start = time.perf_counter()
   # count, ls = IDDFS(puzzle(i))
   # end = time.perf_counter()
   # print("Line " + str(i) + ": %s" % puzzle(i) + ", "+ str(count) + " moves found in " + str(end-start) + " seconds \n")
   # j = edit(puzzle(i))
   # k = puzzle(i)
   # bool = parity(j)
   # print(bool)
   # print(j + "\n" + k)



def findHardest():
    start = find_goal(puzzle(3))
    q = deque()
    theset = {start}
    s = print_puzzle(start)
    goal = find_goal(start)
    q.append((start,0,[s]))
    max = 0 
    ps = []
    while q:
        node,count,ls = q.popleft()
        if count == max:
            ps.append(node)
        if count > max:
            max = count
            ps = [node]
        for n in get_children(node):
            if n not in theset:
                s = print_puzzle(n)
                q.append((n,count+1,ls+[s]))
                theset.add(n)
    return ps 