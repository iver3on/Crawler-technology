'''
Created on 2015年12月22日

@author: iverson Zhang
'''
import urllib.request
url = "http://www.baidu.com"
print("第一种方式")
responce = urllib.request.urlopen(url)
print(responce.getcode())
print(responce.read().decode('UTF-8'))
print(len(responce.read()))


