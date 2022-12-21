import sys
import math
import time
from collections import deque

case = sys.argv[1]

def read():
    with open(case) as f:
        line_list = [line.strip() for line in f]
    return line_list

def puzzle(n):
    return read()[n][2:]

def print_initial(n):
    str = read()[n]
    return print_puzzle(str[2:])

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
            return count, ls
        for n in get_children(node):
            if n not in theset:
                s = print_puzzle(n)
                q.append((n,count+1,ls+[s]))
                theset.add(n)
    return None


start0 = time.perf_counter()
count0, ls0 = BFS(puzzle(0))
end0 = time.perf_counter()
start1 = time.perf_counter()
count1, ls1 = BFS(puzzle(1))
end1 = time.perf_counter()
start2 = time.perf_counter()
count2, ls2 = BFS(puzzle(2))
end2 = time.perf_counter()
start3 = time.perf_counter()
count3, ls3 = BFS(puzzle(3))
end3 = time.perf_counter()
start4 = time.perf_counter()
count4, ls4 = BFS(puzzle(4))
end4 = time.perf_counter()
start5 = time.perf_counter()
count5, ls5 = BFS(puzzle(5))
end5 = time.perf_counter()
start6 = time.perf_counter()
count6, ls6 = BFS(puzzle(6))
end6 = time.perf_counter()
start7 = time.perf_counter()
count7, ls7 = BFS(puzzle(7))
end7 = time.perf_counter()
start8 = time.perf_counter()
count8, ls8 = BFS(puzzle(8))
end8 = time.perf_counter()
print("Line 0: %s" % puzzle(0) + ", "+ str(count0) + " moves found in " + str(end0-start0) + " seconds")
print("Line 1: %s" % puzzle(1) + ", "+ str(count1) + " moves found in " + str(end1-start1) + " seconds")
print("Line 2: %s" % puzzle(2) + ", "+ str(count2) + " moves found in " + str(end2-start2) + " seconds")
print("Line 3: %s" % puzzle(3) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")
print("Line 4: %s" % puzzle(4) + ", "+ str(count4) + " moves found in " + str(end4-start4) + " seconds")
print("Line 5: %s" % puzzle(5) + ", "+ str(count5) + " moves found in " + str(end5-start5) + " seconds")
print("Line 6: %s" % puzzle(6) + ", "+ str(count6) + " moves found in " + str(end6-start6) + " seconds")
print("Line 7: %s" % puzzle(7) + ", "+ str(count7) + " moves found in " + str(end7-start7) + " seconds")
print("Line 8: %s" % puzzle(8) + ", "+ str(count8) + " moves found in " + str(end8-start8) + " seconds")


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

hard = findHardest()

for n in hard:
    start = time.perf_counter()
    count,ls = BFS(n)
    end = time.perf_counter()
    for x in ls:
        print(x)
    print("Hardest Puzzle: %s" % n + ", "+ str(count) + " moves found in " + str(end-start) + " seconds")

print(hard)