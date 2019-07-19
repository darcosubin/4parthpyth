def f(n):
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result
for x in range(input('n=')):
    print (f(x))  