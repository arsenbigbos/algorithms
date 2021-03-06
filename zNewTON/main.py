import math as m
import copy as c
def gauss_seidel(A,b,epsilon):
    k=0
    maxk=100
    res=[]
    global deltaresgauss
    x=[0 for i in range(len(b))]

    while(k<maxk):
        x0=c.copy(x)
        for i in range(len(x)):
            sum1=0
            for j in range(i):
                sum1+=A[i][j]*x[j]
            sum2=0
            for j in range(i+1,len(x)):
                sum2+=A[i][j]*x0[j]

            x[i]=(b[i]-sum1-sum2)/A[i][i]

        delta=[]
        for i in range(len(x)):
            delta.append(abs(x[i]-x0[i]))

        res.append(c.copy(x))
        deltaresgauss.append(delta)
        if max(delta)<epsilon:
            break

        k+=1
        x0=x
    if k==maxk:
        print("Незбіжність ітераційного процесу!!!")
        return 1
    else:
         print("Метод Гаусa-Зейделя:")

         for i in range(k):
             print("k:", i+1, "x(k) ", "Похибка наближення: ",
max(deltares[i]))
             for n in range(len(x)):
                 print(" ", f'{res[i][n]:.5f}')
         return res[-1]
def jacobi(A,b,epsilon):
    k=0
    maxk=100
    res=[]
    global deltares
    x = [0 for i in range(len(b))]

    while(k<maxk):
        x0=c.copy(x)
        for i in range(len(x)):
            sum=0
            for n in range(len(x)):
                if n!=i:
                    sum+=A[i][n]*x0[n]
            x[i]=(b[i]-sum)/A[i][i]
        delta=[]
        for i in range(len(x)):
            delta.append(abs(x[i]-x0[i]))

        deltares.append(delta)
        res.append(c.copy(x))
        if max(delta)<epsilon:
            break
        k+=1
    if k==maxk:
        print("Незбіжність ітераційного процесу!!!")
        return 1
    else:
        print("Метод Якобі:")
        for i in range(k):
            print("k:", i+1, "x(k) ", "Похибка наближення: ",
max(deltares[i]))
            for n in range(len(x)):
                print(" ", f'{res[i][n]:.5f}')
        return res[-1]
A=[[5.9,1.1,3.2],
 [2.1,5.1,-0.5],
 [1.3,0.5,4.3]]
b=[3.5,1.7,-0.2]
epsilon=0.0001
r=[]
deltares=[]
deltaresgauss=[]
x=jacobi(A,b,epsilon)

for i in range(len(b)):
    Ax=0
    for k in range(len(b)):
        Ax+=A[i][k]*x[k]
    r.append(Ax-b[i])
print("Вектор нев'язок: ")
[print(f'{i:.5f}') for i in r]
print("\n")
gauss_seidel(A,b,epsilon)
k=[i for i in range(len(deltares))]
lgdelta=[m.log10(max(i)) for i in deltares]
kgs=[i for i in range(len(deltaresgauss))]
lgdeltags=[m.log10(max(i)) for i in deltaresgauss]
plt.title("№7")
plt.xlabel("k")
plt.ylabel("lg(delta)")
plt.grid()
plt.scatter(k,lgdelta,color='orange')
plt.show()
plt.title("№9")
plt.xlabel("k")
plt.ylabel("lg(delta)")
plt.grid()
plt.scatter(kgs,lgdeltags,color='green')
plt.show()

