l= [1,2,34,5,0]

print(all(l))


from hdfs import *

client  = Client("http://hadoop100:9870")
print( client.list("/"))

