import sys
import math
import time
import heapq
from collections import deque
from math import pi , acos , sin , cos

import tkinter as tk
import time



start = time.perf_counter()

stationfile = "rrNodes.txt"
cityfile = "rrNodeCity.txt"
routefile = "rrEdges.txt"

def calcd(node1, node2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   y1, x1 = node1
   y2, x2 = node2

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

def stationcollect():
    with open(stationfile) as f:
        line_list = [line.strip() for line in f]
    return line_list

stationinfo = stationcollect()

def stat(n):
    return stationinfo[n].split(" ")[0],stationinfo[n].split(" ")[1],stationinfo[n].split(" ")[2]

def stationdict():
    statdictionary = {}
    for i in range (0,len(stationinfo)):
        a,b,c = stat(i)
        statdictionary[a] = float(b),float(c)
    return statdictionary

statdict = stationdict()

def cities():
    with open(cityfile) as f:
        line_list = [line.strip() for line in f]
    return line_list

forfindcity = cities()

def findCity(n):
    return forfindcity[n]

def cityname(n):
    name = ""
    for j in range (1,len(findCity(n).split(" "))):
        name  = name + " " + findCity(n).split(" ")[j]
    return name[1:]

def createCityDict():
    citydict = {}
    revcitydict = {}
    for i in range (0,len(forfindcity)):
        citydict[findCity(i).split(" ")[0]] = cityname(i)
        revcitydict[cityname(i)] = findCity(i).split(" ")[0] 
    return citydict,revcitydict

cdict,revdict = createCityDict()

def tag(n):
    return findCity(n).split(" ")[0]

def routecollect():
    with open(routefile) as f:
        line_list = [line.strip() for line in f]
    return line_list

routelist = routecollect()

def routedest(n):
    return routelist[n].split(" ")[0],routelist[n].split(" ")[1]

def findRoute(n):
    return routelist[n].split(" ")[0],routelist[n].split(" ")[1]

root = tk.Tk()
canvas = tk.Canvas(root, height=800, width=2000, bg='white')

def createDict(c):
    routedict = {}
    lineDict = {}
    for i in range (0,len(routelist)):
        a,b = routedest(i)
        dist = calcd(statdict.get(a),statdict.get(b))
        if routedict.get(a) == None:
            routedict[a] = [(dist,b)]
            q,r= statdict[a]
            p,t = statdict[b]
            line = c.create_line([((r+150)*10,q*(-10)+650),((t+150)*10,p*(-10)+650)], tag='grid_line')
            lineDict[a] = [line]
        else:
            ls = routedict.get(a)
            routedict[a] = ls + [(dist,b)]
            q,r= statdict[a]
            p,t = statdict[b]
            line = c.create_line([((r+150)*10,q*(-10)+650),((t+150)*10,p*(-10)+650)], tag='grid_line')
            lineDict[a] = lineDict.get(a) + [line]
        if routedict.get(b) == None:
            routedict[b] = [(dist,a)]
            q,r= statdict[a]
            p,t = statdict[b]
            line = c.create_line([((r+150)*10,q*(-10)+650),((t+150)*10,p*(-10)+650)], tag='grid_line')
            lineDict[b] = [line]
        else:
            ls = routedict.get(b)
            routedict[b] = ls + [(dist,a)]
            q,r= statdict[a]
            p,t = statdict[b]
            line = c.create_line([((r+150)*10,q*(-10)+650),((t+150)*10,p*(-10)+650)], tag='grid_line')
            lineDict[b] = lineDict.get(b)+ [line]
    return routedict,lineDict

distDict,lines = createDict(canvas)


def makeRed(r,c,line,count):
    for i in line:
        c.itemconfig(i, fill="red")
        count = count + 1
    #if count >= 1500:
        #r.update()

def makeBlue(r,c,line,count):
    for i in line:
        c.itemconfig(i, fill="blue")
    # if count >= 500:
    #     r.update()

def makeGreen(r,c,line):
    c.itemconfig(line, fill="green")

def updateline(r):
    r.update()

canvas.pack(expand=True)

def get_children(n):
    return distDict.get(n)

end = time.perf_counter()

print("Time to create data structure: " + str(end-start))

a,b = routedest(1)


def dijkstra(city1,city2):
    start = revdict.get(city1)
    end = revdict.get(city2)
    theset = set()
    fringe = []
    heapq.heappush(fringe,(0,start,[],0))
    while fringe:
        total,node,ls,count = heapq.heappop(fringe)
        root.update()
        # if count >= 500:
        #     root.update()
        #     count = count - 500
        if node == end:
            for i in ls:
                for j in i:
                    makeGreen(root,canvas,j)
            updateline(root) 
            return total
        if node not in theset:
            theset.add(node)
            for i in get_children(node):
                line = lines.get(i[1])
                if i[1] not in theset:
                    makeRed(root,canvas,line,count)
                    heapq.heappush(fringe,(float(i[0])+total,i[1],ls+[line],count+len(line)))
    return None

city1 = sys.argv[1]
city2 = sys.argv[2]

start = time.perf_counter()
x = dijkstra(city1,city2)
end = time.perf_counter()
print(city1 + " to " + city2 + " with Dijkstra: " + str(x) + " in " + str(end-start) + " seconds.")

def greatCircleDict():
    circDict = {}
    for i in statdict:
        circDict[i] = calcd(statdict.get(i),statdict.get(revdict.get(city2)))
    return circDict

circleDict = greatCircleDict()

def a_star(city1,city2):
    start = revdict.get(city1)
    end = revdict.get(city2)
    theset = set()
    fringe = []
    heapq.heappush(fringe,(circleDict.get(start),0,start,[start],0))
    while fringe:
        heuristic,total,node,ls,count = heapq.heappop(fringe)
        newroot.update()
        # if count >= 500:
        #     newroot.update()
        #     count = count - 500 
        if node == end:
            for i in ls:
                for j in i:
                    makeGreen(newroot,newcanvas,j)
            updateline(newroot)
            return total
        if node not in theset:
            theset.add(node)
            for i in get_children(node):
                line = lines.get(i[1])
                if i[1] not in theset:
                    makeBlue(newroot,newcanvas,line,count) 
                    heapq.heappush(fringe,(circleDict.get(i[1])+i[0]+total,float(i[0])+total,i[1],ls+[line],count+len(line)))
    return None

root.mainloop()

newroot = tk.Tk()
newcanvas = tk.Canvas(newroot, height=800, width=2000, bg='white')

distDict,lines = createDict(newcanvas)

newcanvas.pack(expand=True)

start = time.perf_counter()
x = a_star(city1,city2)
end = time.perf_counter()
print(city1 + " to " + city2 + " with A*: " + str(x) + " in " + str(end-start) + " seconds.")

newroot.mainloop()