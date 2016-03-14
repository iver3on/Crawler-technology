'''
Created on 2015年12月22日

@author: iverson Zhang
'''
#coding=utf-8

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
#向管理器中加入一个URL
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
#批量加入URLS
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.new_urls.add(url)
#判断管理器中是否有新的带爬取的URL
    def has_new_url(self):
        #result =  len(self.new_urls) != 0 
        if len(self.new_urls) != 0 :
            return True;
        return False;
#从URL管理器获取带爬取URL
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url