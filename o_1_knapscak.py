def knapscak(W,wt,val,n):
    dp =[0 for i in range(W+1)]

    for i in range(1,n+1):
        for w in range(W,0,-1):

            if wt[i-0] <= w:
                