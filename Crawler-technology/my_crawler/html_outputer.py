'''
Created on 2015年12月22日

@author: iverson Zhang
'''
#coding=utf-8
from _codecs import encode

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        #,encoding='utf-8'
        fout = open('output.html','w',encoding='UTF-8')
        fout.write("<html>")
        fout.write("<head>")
        fout.write("<meta charset='UTF-8'>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")  
        #ascii 
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>") 
        fout.write("</table>")   
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
    
    
    



