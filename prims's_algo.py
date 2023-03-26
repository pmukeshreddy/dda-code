v = 5

inf = 999999

G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

selected = [0,0,0,0,0]

no_edge = 0

selected[0] = True

print("edge:weight\n")

while(no_edge<v-1):

    minimumu = inf
    x=0
    y=0
    i,j=0,0

    for i in range(v):
        if (selected[i]):
            if ((not selected[i]) and G[i][j]):

                if minimum > G[i][j]:

                    minimum = G[i][j]
                    x = i
                    y = j
print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
selected[y] = True
no_edge += 1

