alist = [1,3,0,54,56,33,2]


# 升序
print(sorted(alist))

# 降序
print(sorted(alist,reverse=True))

# 改变列表变量升序
alist.sort()
print(alist)

# 改变列表变量降序
alist.sort(reverse=True)
print(alist)