from selenium import webdriver
from selenium.webdriver.common.by import By
# print(dict(zip([1,2],[3,4])))

a = [1,2]
b= [3,4]
c= { x:b[a.index(x)] for x in a}
print(c)