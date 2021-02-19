def doSomething(aQueue):
    N=len(aQueue)
    theMax=0
    while N>0:
        item=aQueue[0]
        aQueue.remove(aQueue[0])
        if item > theMax:
            theMax=0.5*item
            aQueue.append(theMax)
        N=N-1
    return theMax


Q=[10, 15, 2, 8, 3, 12]
print(doSomething(Q))
        
