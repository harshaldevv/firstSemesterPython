####import random
####
####def random_walk(n):
####    """return co-od after 'n' block random walk"""
####
####    x = 0
####    y = 0
####    for i in range(n):
####        step = random.choice(['N','S','E','W'])
####        if step == "N":
####            y +=1
####
####        elif step== "S":
####            y -=1
####
####        elif step == "E":
####            x -=1
####        else:
####            x +=1
####
####        return (x,y)
####
####for i in range(50):
####    walk = random_walk(10)
####    print(walk , "distance from home = " , abs(walk[0]) + abs(walk[1]))
####    
##
##import random
##def random_walk2(n):
##    x,y = 0,0
##
##    for i in range(n):
##        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
##                                                     
##        x +=dx
##        y += dy
##        return (x,y)
##
##number_of_walks = 10000
##for walk_length in range(1,31):
##    no_transport = 0
##    for i in range(number_of_walks):
##        (x,y) = random_walk2(walk_length)
##        distance = abs(x)+ abs(y)
##        if distance <=4:
##            no_transport +=1
##
##        no_transport_percentage = float(no_transport)/number_of_walks
##        print("walk size = ",walk_length, " / % of no transport = ",100*no_transport_percentage)
##        

import time

def is_prime_v1(n):
    if n==1:
        return False
    for d in range(2,n-1):
        if n%d ==0:
            return False
        
    return True
t0 = time.time()
for n in range(1,100000):
    #print(n,is_prime_v1(n))
    is_prime_v1(n)

t1 = time.time()
print("time req" , t1 - t0)
    
    
