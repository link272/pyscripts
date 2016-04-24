sol=[]
n=9
numero=[]
modif="true"
ligne=[]
colonne=[]
pilex=0
piley=0



sol=[[[], [], [1], [], [], [9], [3], [], []]
,[[], [], [], [], [], [], [], [7], [8]]
,[[], [5], [3], [], [], [], [], [], []]
,[[], [], [], [], [], [7], [], [8], []]
,[[8], [], [9], [], [], [1], [4], [], []]
,[[], [2], [], [], [], [5], [1], [], []]
,[[9], [], [], [5], [], [], [], [], [3]]
,[[], [], [4], [], [8], [2], [], [6], []]
,[[], [], [], [], [6], [], [8], [], []]]

for i in range(0,n):
    for j in range(0,n):
        if sol[i][j]==[]:
            for p in range(1,10):
                sol[i][j].append(p)

print(sol)





while modif=="true":
    modif="false"
    for i in range(0,n):
        for j in range(0,n):
            if len(sol[i][j])==1:
                for x in range(0,n):
                    if x!=j:
                        if sol[i][j][0] in sol[i][x]:
                             sol[i][x].remove(sol[i][j][0])
                             modif="true"



    for i in range(0,n):
        for j in range(0,n):
             if len(sol[i][j])==1:
                for x in range(0,n):
                    if x!=i:
                        if sol[i][j][0] in sol[x][j]:
                            sol[x][j].remove(sol[i][j][0])
                            modif="true"
    for i in range(0,n):
        for j in range(0,n):
            a=i%3
            b=j%3
            if a=="0":
                colonne=[i,i+1,i+2]
            if a=="1":
                colonne=[i-1,i,i+1]
            if a=="2":
                colonne=[i-2,i-1,i]
            if b=="0":
                ligne=[j,j+1,j+2]
            if b=="1":
                ligne=[j-1,j,j+1]
            if b=="2":
                ligne=[j-2,j-1,j]
            for x in ligne:
                for y in colonne:
                    if sol[i][j][0] in sol[x][y] and not(x==j and j==i):
                        sol[x][y].remove(sol[i][j][0])
                        modif="true"


    for k in range(1,10):
        for i in range(0,n):
            count=0
            for j in range(0,n):
                    count=count+sol[i][j].count(k)
            if count==1:
                liste=[1,2,3,4,5,6,7,8,9]
                liste.remove(k)
                for j in range(0,n):
                    if sol[i][j].count(k)==1:
                        for x in liste:
                            if x in sol[i][j]:
                                sol[i][j].remove(x)
                    

    for k in range(1,10):
        for i in range(0,n):
            count=0
            for j in range(0,n):
                count=count+sol[j][i].count(k)
            if count==1:
                liste=[1,2,3,4,5,6,7,8,9]
                liste.remove(k)
                for j in range(0,n):
                    if sol[j][i].count(k)==1:
                        for x in liste:
                            if x in sol[j][i]:
                                sol[j][i].remove(x)
                    
    for k in range(1,10):
        for i in range(0,n,3):
            for j in range(0,n,3):
                count=0
                for x in [0,1,2]:
                    for y in [0,1,2]:
                        count=count+sol[i+x][j+y].count(k)
                if count==1:
                    liste=[1,2,3,4,5,6,7,8,9]
                    liste.remove(k)
                    for x in [0,1,2]:
                        for y in [0,1,2]:
                            if sol[i+x][j+y].count(k)==1:
                                for m in liste:
                                    if m in sol[i+x][j+y]:
                                        sol[i+x][j+y].remove(m)
                                        modif="true"
                        


print(sol)
for i in range(0,n):
    if i%3==0:
        print("-------------------------")
    print ('|',sol[i][0][0],sol[i][1][0],sol[i][2][0],'|',sol[i][3][0],sol[i][4][0],sol[i][5][0],'|',sol[i][6][0],sol[i][7][0],sol[i][8][0],'|')
print("-------------------------")





