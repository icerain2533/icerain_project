__author__ = 'chenjiabao'
# -*- coding: utf-8 -*-
' 连接mongo数据库'

list = [2,5,23,26,35,38,44,53,60,72,85,96,105,159,301]
findNunber = 52
front = 0
end = len(list)
mid = (front + end)/2
while (front <= end) :
        if findNunber< list[mid]:
            end = mid-1
            mid = (front+end)/2
        elif findNunber> list[mid]:
            front = mid+1
            mid=(front+end)/2
        else:
            print list[mid], mid
            break
if (front > end):
    print "not find"

