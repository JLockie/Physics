import numpy as np 
import matplotlib.pyplot as plt
import math 
import random  
from scipy.stats import norm,  gaussian_kde

n = 1000
i = 0

# Defining Brownian Motion
def Brownian(n):
    x = 0                                     # start value of x
    y = 0                                     # 
    xlist = [0]                               # create list for x coordinates 
    ylist = [0]                               # create list for y coordinates 
    placevisited = [(0,0)]                    # create paired list of coordinated
    i = 1
    for i in range(n):                        #Create loop for the movements at any step
        value = random.randint(1,4)           #randomly select a number 1 to 4 
        if value == 1 and ((x + 1), y) not in placevisited:          #if random number is 1 and not be visited
            x += 1                            #move once to the right
            xlist.append(x)                   #record the move to xlist
            ylist.append(y)                   #record the move to ylist
            placevisited.append((x, y))
        elif value == 1 and ((x + 1), y) in placevisited:             #if the particle hits the 
            value = random.choice([2,3,4])      #right wall, it will "bounce" 
        elif value == 2 and ((x - 1), y) not in placevisited:         #if random number is 2
            x += -1                           #move once to the left
            xlist.append(x)                   #record the move to xlist
            ylist.append(y)                   #record the move to ylist
            placevisited.append((x, y))
        elif value == 2 and ((x-1),y) in placevisited:                   #if the particle hits the 
            value = random.choice([1,3,4])       #left wall, it will "bounce"
        elif value == 3 and (x,(y+1)) not in placevisited:         #if random number is 3
            y += 1                            #move upwards once
            xlist.append(x)                   #record the move to xlist
            ylist.append(y)                   #record the move to ylist
            placevisited.append((x, y))
        elif value == 3 and (x,(y+1)) in placevisited:                   #if the particle hits the 
            value = random.choice([1,2,4])       #top wall, it will "bounce"
        elif value == 4 and (x,(y-1)) not in placevisited:         #if random number is 4
            y += -1                           #move downwards once
            xlist.append(x)                   #record the move to xlist
            ylist.append(y)                   #record the move to ylist
            placevisited.append((x, y))
        elif value == 4 and (x,(y-1)) in placevisited:                   #if the particle hits the 
            value = random.choice([1,2,3])       #bottom wall, it will "bounce"
    return placevisited, xlist, ylist, x, y                 #The recorded points are callable  

Rs, X, Y, x, y = Brownian(100)
print(Rs)
print(len(Rs))

def tailstep(snack):
    np.delete(snack,0)
    return snack

def headstep(snacker):
    value = random.randint(1,2)
    snack = []
    if value == 1:
        snack.append(snacker[i])
        return snack
    else:
        snack = np.fliplr(snacker)
        return snack

def distance(xs,ys):
    x, y = xs
    a, b = ys
    return np.sqrt((a-x)**2 +(b-y)**2)

def snackattack(Rs, n, snacksize):
    snack = Rs
    cutoff = snack[0]
    i = 0
    for i in range(n):
        t = snack[1]
        h = snack[len(snack)-1]
        xh, yh = h
        cutoff = snack[0]
        snack = tailstep(snack)
        if len(snack) < snacksize:
            pos1 = (xh + 0, yh + 1)
            pos2 = (xh + 0, yh - 1)
            pos3 = (xh + 1, yh + 0)
            pos4 = (xh - 1, yh + 0)
            d1 = distance(pos1, cutoff)
            d2 = distance(pos2, cutoff)
            d3 = distance(pos3, cutoff)
            d4 = distance(pos4, cutoff)
            mindistance = min(d1, d2, d3, d4)
            if mindistance == d1:
                if pos1 not in Rs:
                    snack.append(pos1)
                    Rs.append(pos1)
                    i += 1
                    snack = headstep(snack)
                elif pos1 in Rs:
                    snack.insert(0,cutoff)
                    snack = headstep(snack)
                    i += 1
            if mindistance == d2:
                if pos2 not in Rs:
                    snack.append(pos2)
                    Rs.append(pos2)
                    i += 1
                    snack = headstep(snack)
                elif pos2 in Rs:
                    snack.insert(0,cutoff)
                    snack = headstep(snack)
                    i += 1
            if mindistance == d3:
                if pos3 not in Rs:
                    snack.append(pos3)
                    Rs.append(pos3)
                    i += 1
                    snack = headstep(snack)
                elif pos3 in Rs:
                    snack.insert(0,cutoff)
                    snack = headstep(snack)
                    i += 1
            if mindistance == d4:
                if pos4 not in Rs:
                    snack.append(pos4)
                    Rs.append(pos4)
                    i += 1
                    snack = headstep(snack)
                elif pos4 in Rs:
                    snack.insert(0,cutoff)
                    snack = headstep(snack)
                    i += 1
    return snack, Rs

fig = plt.figure()
plt.title("N = 1000")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

for count in range(1000):
    Rs, X, Y, x, y = Brownian(1000)
    length = len(Rs)
    snack, newRs = snackattack(Rs, 1000, length)
    a, b = map(list, zip(*newRs))
    c, d = map(list, zip(*snack))
    plt.plot(a, b)

plt.show()
