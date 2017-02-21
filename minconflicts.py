import sys
import time
import random

def choosevar(x):
    var = []

    for j in range(N):
        conflict = 0
        for k in adjList[j]:
            if x[j] == x[k]:
                conflict = conflict + 1
        if conflict != 0:
            var.append(j)
    return var

def calculateConflicts(v, i, x, adjList): # Calculate conflicts
    conflicts = 0
    for j in adjList[v]:
        if i == x[j]:
            conflicts += 1

    return conflicts

def calculateConflictedvars(adjList): # Returns list of conflicted variables
    for i in range(N):
        for c in range(C):
            c=calculateConflicts(i,c,x,adjList)
            total = total+c


def minconflicts(adjList,maxsteps,x):
    count=0
    for i in range(1,maxsteps):
        count=count+1
        conflict = 0
        for j in range(N):
            for k in adjList[j]:
                if x[j] == x[k]:
                    conflict=conflict+1
        if conflict ==0:
            #print("steps:",count)
            return x
        else:

            array = choosevar(x)
            #print(array)
            v = random.choice(array)

            min = 1000

            for i in range(C):

                value = calculateConflicts(v,i,x,adjList)
                if (value<min):
                    min = value
                    color = i
            num = random.randint(0,10)
            if num<7:
                x[v] = color
            else:
                x[v] = random.randint(0,2)
    #print("steps:",count)
    return 0



if __name__ == "__main__":

    global N,M,C

    if len(sys.argv) == 3:
        in_file = sys.argv[1]
        out_file = sys.argv[2]

    else:
       print('Wrong number of arguments.')


    d = []
    with open(in_file, 'r') as f:
        for line in f:
            data = line.split()
            for i in data:
                d.extend(i.split(','))

        k = [int(x) for x in d]
        print(k)
    N = k[0]
    M = k[1]
    C = k[2]
    x=[]


    for i in range(N):
       x.append(random.randrange(C)) #Start with random configuration

    #print(x)

    adjList = [[] for k in range(N)]
    for i in range(3,2*(M+1),2):

        adjList[k[i]].append(k[i+1])
        adjList[k[i+1]].append(k[i])
    print(adjList)

    start_time = time.time()
    maxsteps = N*100
   # print(maxsteps)
    c = minconflicts(adjList,N*100,x)
    if c==0:
        print("No answer")
    else:
        print("--- %s seconds ---" % (time.time() - start_time))
        print(c)
        #print(c[0])
        #c[1]=0
        for i in range(N):
            for j in adjList[i]:
                if c[i] == c[j]:
                    print("error")
        print("No error")

        file = open(out_file, 'w')
        for i in c:
            file.write(str(i) + '\n')


