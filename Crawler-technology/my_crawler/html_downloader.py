'''
Created on 2015年12月22日

@author: iverson Zhang
'''
#coding=utf-8
import urllib.request

class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            print("wrong url")
            return None
        responce = urllib.request.urlopen(url)
        if responce.getcode() != 200:
            print("wrong")
            return None
        print("good")
        return responce.read()
