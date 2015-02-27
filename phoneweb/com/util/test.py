__author__ = 'chenjiabao'

class User:
    name = []
    def __init__(self):
        print "init"
        User.name = [1,2]
    def __del__(self):
        print "dellllll"
    @classmethod
    def classInvoke(self):
        print self.name

if __name__ == '__main__':
   # User.name = "fffffff"
    print User.name