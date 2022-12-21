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

def BiBFS(start):
    q1 = deque()
    theset1 = {start}
    goal = find_goal(start)
    q2 = deque()
    theset2 = {goal}
    q1.append((start,0))
    q2.append((goal,0))
    dict1 = {start:0,goal:0}
    while q1:
        node1,count1 = q1.popleft()
        node2,count2 = q2.popleft()
        if node1 == node2:
            return count1 + count2
        if node1 in theset2:
            count2 = dict1[node1]
            return count1 + count2 
        for n in get_children(node1):
            if n not in theset1:
                q1.append((n,count1+1))
                dict1[n] = count1 + 1
                theset1.add(n)
        if node2 in theset1:
            count1 = dict1[node2]
            return count1 + count2
        for n in get_children(node2):
            if n not in theset2:
                q2.append((n,count2+1))
                dict1[n] = count2 + 1
                theset2.add(n)
    return None

start0 = time.perf_counter()
count0,ls = BFS(puzzle(0))
end0 = time.perf_counter()
print("BFS Line 0: %s" % puzzle(0) + ", "+ str(count0) + " moves found in " + str(end0-start0) + " seconds")

start1 = time.perf_counter()
count1 = BiBFS(puzzle(0))
end1 = time.perf_counter()
print("BiBFS Line 0: %s" % puzzle(0) + ", "+ str(count1) + " moves found in " + str(end1-start1) + " seconds")

start2 = time.perf_counter()
count2,ls = BFS(puzzle(1))
end2 = time.perf_counter()
print("BFS Line 1: %s" % puzzle(1) + ", "+ str(count2) + " moves found in " + str(end2-start2) + " seconds")

start3 = time.perf_counter()
count3 = BiBFS(puzzle(1))
end3 = time.perf_counter()
print("BiBFS Line 1: %s" % puzzle(1) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")

start2 = time.perf_counter()
count2,ls = BFS(puzzle(2))
end2 = time.perf_counter()
print("BFS Line 2: %s" % puzzle(2) + ", "+ str(count2) + " moves found in " + str(end2-start2) + " seconds")

start3 = time.perf_counter()
count3 = BiBFS(puzzle(2))
end3 = time.perf_counter()
print("BiBFS Line 2: %s" % puzzle(2) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")

start3 = time.perf_counter()
count3,ls = BFS(puzzle(3))
end3 = time.perf_counter()
print("BFS Line 3: %s" % puzzle(3) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")

start3 = time.perf_counter()
count3 = BiBFS(puzzle(3))
end3 = time.perf_counter()
print("BiBFS Line 3: %s" % puzzle(3) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")

start3 = time.perf_counter()
count3,ls = BFS(puzzle(4))
end3 = time.perf_counter()
print("BFS Line 4: %s" % puzzle(4) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")

start3 = time.perf_counter()
count3 = BiBFS(puzzle(4))
end3 = time.perf_counter()
print("BiBFS Line 4: %s" % puzzle(4) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")

start3 = time.perf_counter()
count3,ls = BFS(puzzle(5))
end3 = time.perf_counter()
print("BFS Line 5: %s" % puzzle(5) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")

start3 = time.perf_counter()
count3 = BiBFS(puzzle(5))
end3 = time.perf_counter()
print("BiBFS Line 5 %s" % puzzle(5) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")

start3 = time.perf_counter()
count3,ls = BFS(puzzle(6))
end3 = time.perf_counter()
print("BFS Line 6: %s" % puzzle(6) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")

start3 = time.perf_counter()
count3 = BiBFS(puzzle(6))
end3 = time.perf_counter()
print("BiBFS Line 6 %s" % puzzle(6) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")


start3 = time.perf_counter()
count3,ls = BFS(puzzle(7))
end3 = time.perf_counter()
print("BFS Line 7: %s" % puzzle(7) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")

start3 = time.perf_counter()
count3 = BiBFS(puzzle(7))
end3 = time.perf_counter()
print("BiBFS Line 7 %s" % puzzle(7) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")


start3 = time.perf_counter()
count3,ls = BFS(puzzle(8))
end3 = time.perf_counter()
print("BFS Line 8: %s" % puzzle(8) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")

start3 = time.perf_counter()
count3 = BiBFS(puzzle(8))
end3 = time.perf_counter()
print("BiBFS Line 8 %s" % puzzle(8) + ", "+ str(count3) + " moves found in " + str(end3-start3) + " seconds")