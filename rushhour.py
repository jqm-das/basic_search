import sys
import math
import time
import heapq
from collections import deque

boardfile = sys.argv[1]
length = 6
def boardread():
    with open(boardfile) as f:
        line_list = [line.strip() for line in f]
    return line_list

boardlist = boardread()

def boardPrint(board):
    boardstring = ""
    for i in range (0,length):
        for j in range (0,length):
            boardstring = boardstring + (board[i*length + j])
        boardstring = boardstring + "\n"
    return boardstring

def classifyTrains(board):
    vertList = []
    horzList = []
    theset = set()
    for i in range (0, len(board)):
        if board[i] != "0" and board[i] not in theset:
            theset.add(board[i])
            let = board[i]
            train = [(let,i)]
            place = i
            while board[place+1:].find(let) >= 0:
                k = board[place+1:].find(let) + place + 1
                train.append((let,k))
                place = k
            test = board[i+1:].find(let)
            if board[i+1:].find(let) == 5:
                vertList.append(train)
            else:
                horzList.append(train)
    return vertList, horzList

def trainList(board):
    theset = set()
    theset.add("0")
    ls = []
    for x in board:
        if x not in theset:
            ls.append(x)
            theset.add(x)
    return ls 

trains = trainList(boardlist[0])
v,h = classifyTrains(boardlist[0])

def moveLeft(board,let):
    first = board.find(let)
    if first % 6 == 0:
        return board
    if board[first-1] != "0" or board[first+1] != let:
        return board
    i = first
    while board[i+1:].find(let) != -1:
        i = i + 1
    board = board[0:first-1] + board[first:i+1] + "0" + board[i+1:]
    return board

def moveRight(board,let):
    first = board.find(let)
    i = first
    while board[i+1:].find(let) != -1:
        i = i + 1
    if i % 6 == 5:
        return board
    if board[i+1] != "0" or board[first+1] != let:
        return board
    board = board[0:first] + "0" + board[first:i+1] + board[i+2:]
    return board

def moveUp(board,let):
    first = board.find(let)
    if first < 6:
        return board
    if board[first+1] == let:
        return board
    i = first
    if board[i-6] != "0":
        return board
    length = 1
    while board[i+6:].find(let) != -1:
        i = i + 6
        length = length + 1
    x = len(board)
    if length == 2:
        board = board[0:first-6] + let + board[first-5:first] + let + board[first+1:first+6] + "0" + board[first+7:]
    if length == 3:
        board = board[0:first-6] + let + board[first-5:first] + let + board[first+1:first+6] + let + board[first+7:first+12] + "0" + board[first+13:]
    if length == 4:
        board = board[0:first-6] + let + board[first-5:first] + let + board[first+1:first+6] + let + board[first+7:first+12] + let + board[first+13:first+18] + "0" + board[first+19:]
    return board

def moveDown(board,let):
    first = board.find(let)
    i = first
    length = 1
    while board[i+6:].find(let) != -1:
        i = i + 6
        length = length + 1
    if i > 29 or i < 6:
        return board
    if board[i+6] != "0" or board[first+1] == let:
        return board
    if length == 2:
        board = board[0:first] + "0" + board[first+1:first+6] + let + board[first+7:first+12] + let + board[first+13:]
    if length == 3:
        board = board[0:first] + "0" + board[first+1:first+6] + let + board[first+7:first+12] + let + board[first+13:first+18] + let + board[first+19:]
    if length == 4:
        board = board[0:first] + "0" + board[first+1:first+6] + let + board[first+7:first+12] + let + board[first+13:first+18] + let + board[first+19:first+23] + let + board[first+24:]
    return board

def get_children(board,let):
    list = []
    y = board
    upboard = moveUp(y,let)
    while upboard != y:
        list.append(upboard)
        y = upboard
        upboard = moveUp(upboard,let)
    y = board
    downboard = moveDown(y,let)
    while downboard != y:
        list.append(downboard)
        y = downboard
        downboard = moveDown(downboard,let)
    y = board
    leftboard = moveLeft(y,let)
    while leftboard != y:
        list.append(leftboard)
        y = leftboard
        leftboard = moveLeft(leftboard,let)
    y = board
    rightboard = moveRight(y,let)
    while rightboard != y:
        list.append(rightboard)
        y = rightboard
        rightboard = moveRight(rightboard,let)
    return list 

def get_all_children(board):
    bigList = []
    for x in trains:
        bigList = bigList + get_children(board,x)
    return bigList

def BFS(start):
    q = deque()
    theset = {start}
    s = boardPrint(start)
    q.append((start,0,[s]))
    while q:
        node,count,ls = q.popleft()
        if node[16] == "X" and node[17] == "X":
            return count, ls
        for n in get_all_children(node):
            if n not in theset:
                s = boardPrint(n)
                q.append((n,count+1,ls+[s]))
                theset.add(n)
    return None

start = time.perf_counter()
count,ls = BFS(boardlist[0])
end = time.perf_counter()

for i in ls:
    print(i)
print(boardPrint(boardlist[0]) + "Moves: "+ str(count) + " time: " + str(end-start) + " seconds")

