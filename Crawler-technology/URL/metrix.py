'''
Created on 2016年1月20日

@author: iverson Zhang
'''
# -*- coding:utf-8 -*-
class Solution:
    global matrix
    matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    def printClock(self,sX,sY,eX,eY):
        if sX==eX:
            for i in range(sY,eY):
                print (i)
            return
        if sY==eY:
            for i in range(sX,eX):
                print (i)
            return
        for p in range(sY,eY):
            print (self.matrix[sX][p])
        for p in range(sX,eX):
            print (self.matrix[p][eY])
        for p in range(eY,sY,-1):
            print (self.matrix[eX][p])
        for p in range(eX,sX,-1):
            print (self.matrix[p][sY]) 
    def printMatrix(self):
        # write code here
        rows=len(matrix)
        cols=len(matrix[0])
        if rows<0 or cols<0:
            return
        startX=0
        startY=0
        endX=rows-1
        endY=cols-1
        while True:
            if startX>endX and startY>endY:
                break
            if startX==endX and startY>endY:
                break
            if startX>endX and startY==endY:
                break
            self.printClock(startX,startY,endX,endY)            
            startX += 1
            startY += 1
            endX -= 1
            endY -=1        
        for row in matrix:
            print (row)
X = Solution()
X.printMatrix()     
