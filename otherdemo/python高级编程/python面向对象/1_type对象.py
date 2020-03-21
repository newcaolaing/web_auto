

a  = 1

b = "adb"

# 变量有对应的类生成
print(type(a))
print(type(1))

# 类由type类生成
print(type(int))

# 类由type类生成,实例由对应的类生成
class test():
    pass
test1 = test()
print(type(test))
print(type(test1))

#object是最顶层的基类

print(type.__bases__)
print(test.__bases__)

# object 和 type 相互生成
print(type(object))
