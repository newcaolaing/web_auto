
class a():
    pass
class b(a):
    pass

c = b()
print(isinstance(c,b))
print(isinstance(c,a))
print(type(c)  == a)
print(type(c)  is b)