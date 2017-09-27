#encoding:utf-8
'''
Rectifier模块单元测试
Author:LiuJian
Data:2017-05-019 

'''
import random
import unittest
from Rectifier import *

# print( Rectifier().rectify(0) )

class TestRectifier(unittest.TestCase):

    def setUp(self):
        self.seq = []

        # generate random numbers 
        self.seq.append(random.uniform(-50,-20))
        self.seq.append(random.uniform(-20,-10))
        self.seq.append(random.uniform(-10,10))
        self.seq.append(random.uniform(10,20))
        self.seq.append(random.uniform(20,50))
        # print(self.seq)

    def testsample(self):
        
        out = []
        for i in range(len(self.seq)):
            out.append( Rectifier().rectify(self.seq[i]) )

        # judge equal or not 
        self.assertEqual( out , [-0.2,-0.1,0,0.1,0.2] )


if __name__=="__main__":
    unittest.main()
        
