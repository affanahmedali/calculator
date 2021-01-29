mat1=[]
n=int(input('Enter number of rows for matrix: '))
# for loop generates no. of rows in a matrix
for i in range(n):
    print ('Enter contents of row',i+1,'separated by space for matrix 1: ', end='')
    row=input()
    #for creating sub list
    table= row.split()
    #for assinging sub list to x(list)
    mat1.append(table)
#for converting str_list to int
mat1=[list(map( int,i) )for i in mat1]
for s in mat1:
    print(*s)


p=int(input('Enter number of rows in matrix 2: '))
q=int(input('Enter number of columns in matrix 2: '))
mat2=[]
for i in range(0,p):
    mat2.append([])
for i in range(0,p):
    for j in range(0,q):
        mat2[i].append(j)
        print('Entery in row ',i+1,' column',j+1)
        mat2[i][j]=int(input())
for s in mat2:
    print(*s)


def add(n,q):
    res1=[]
    for i in range(0,n):
        res1.append([])
    for i in range(0,n):
        for j in range(0,q):
            res1[i].append(j)
    for i in range (len(mat1)):
        for j in range (len (mat2)):
            res1[i][j]=mat1[i][j]+ mat2[i][j]
    return res1


def sub(n,q):
    res2=[]
    for i in range(0,n):
        res2.append([])
    for i in range(0,n):
        for j in range(0,q):
            res2[i].append(j)
    for i in range (len(mat1)):
        for j in range (len (mat2)):
            res2[i][j]=mat1[i][j]- mat2[i][j]
    return res2

def mul(n,q):
    res3=[]
    for i in range(0,n):
        res3.append([])
    for i in range(0,n):
        for j in range(0,q):
            res3[i].append(j)
            res3[i][j]=0
    for p in range(len(mat1)):
        for t in range(len(mat2[0])):
            for r in range(len(mat2)):
                res3[p][t]+=mat1[p][r] *mat2[r][t]
    return res3


value=int(input('\n OPERATIONS MENU \n 1.Add matrices \n 2.Subtract matrices \n 3.Multiply matrices \n 4.Exit\n '))

if value==1:
    for s in add(n,q):
        print(*s)

if value==2:
    for s in sub(n,q):
        print(*s)

if value==3:
    for s in mul(n,q):
        print(*s)

if value==4:
    print(' Exit')



