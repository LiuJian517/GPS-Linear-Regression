'''
纠偏器：接收偏移量信息，转换为车轮转角修正值
Author:LiuJian
Data:2017-05-02 09:22

'''

class Rectifier:
    def __init__(self):

        # 10m/s的常规运动速度下，每个50ms车轮转角经验修正值(tan a = a)
        self.__ans = [-0.2,-0.1,0,0.1,0.2] 

    def rectify(self,deviation):

        index = len(self.__ans)/2
        cnt = 0

        if deviation <= -20:
            cnt = -2

        elif deviation < -10:
            cnt = -1
            
        elif deviation < 10:
            cnt = 0
            
        elif deviation <20:
            cnt = 1

        else:
            cnt = 2
            
        return self.__ans[int(index+cnt)]
