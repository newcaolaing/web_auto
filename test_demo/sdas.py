
class aa():
    def a(self):
        print(1111111)

def c(x):
    lists = list()
    lists.append(x)
    return lists
if __name__ == '__main__':
    # sd = aa()
    # a=getattr(sd,'a')
    # a()

    # a = ['1', '2']
    # a = list(map(tuple, a))
    print("方法一")
    print(list(map(tuple,['1','222'])))
    print("方法二")
    print(list(map(lambda x:tuple(list(x)),['1','222'])))
    print("方法三")
    print(list(map(tuple,[[x] for x in ['1','222']])))

