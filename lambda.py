def increment(n):
    return lambda x:x+n+40
f=increment(40)
print f(0)
print f(1)

pairs=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key=lambda pair: pair[1])
print pairs