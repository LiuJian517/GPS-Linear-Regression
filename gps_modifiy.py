import numpy as np
from math import * 
from sklearn import linear_model

GPS_NUMBER = 4  # 每500ms的任务执行过程中，GPS的采样点数（暂定为4）

def modify(GPS_X_Points,GPS_Y_Points,Road_X_Points,Road_Y_Points,Theta):
    
    '''
    根据路径信息以及GPS定位点信息进行预测纠偏

    '''

    X=[]
    for i in range(GPS_NUMBER):
        line = [i]
        X.append(line)
        
    offest = []  # 记录每个GPS点相对于原始数据的偏移量，正负号分别表示左右偏移
    
    for i in range(GPS_NUMBER):

        X1 = GPS_X_Points[i]
        Y1 = GPS_Y_Points[i]

        X2 = Road_X_Points[(i+1)*2]
        Y2 = Road_Y_Points[(i+1)*2]
        
        vec1 = np.array([X1,Y1])
        vec2 = np.array([X2,Y2])
        dist = np.linalg.norm(vec1-vec2)
        
        if Theta[(i+1)*2]*((X2-X1)+Y1) < 0:  # 小于零表示往右偏
            dist = -dist
             
        offest.append(dist)
        

    regr = linear_model.LinearRegression()
    regr.fit(X,offest)

    return float(regr.predict(GPS_NUMBER))


#测试数据
'''
X1 = [2.1,4.2,6.3,8.4]
Y1 = [2,4,6,8]
X2 = [0,1,2,3,4,5,6,7,8,9]
Y2 = [0,1,2,3,4,5,6,7,8,9]
T= [1,1,1,1,1,1,1,1,1,1]

'''
X1 = [2.8,4.9,6.8,8.4]
Y1 = [4.4,16.3,35.2,55]

X2 = [1,1.788,2.85,3.884,4.904,5.917,6.841,7.636,8.348,8.996]
Y2 = [1,1.620944,4.4225,9.317456,16.24122,25.17689,35.11728,45.0365,54.9931,64.93602]
T= [0.788,2.02,3.946,5.934,7.933,9.934,11.766,13.347,14.763,16.054]

print(modify(X1,Y1,X2,Y2,T))




def calcDistance(Lat_A, Lng_A, Lat_B, Lng_B):
    '''
    # input Lat_A 纬度A
    # input Lng_A 经度A
    # input Lat_B 纬度B
    # input Lng_B 经度B
    # output distance 距离(km)

    '''
    ra = 6378.140  # 赤道半径 (km)
    rb = 6356.755  # 极半径 (km)
    flatten = (ra - rb) / ra  # 地球扁率
    rad_lat_A = radians(Lat_A)
    rad_lng_A = radians(Lng_A)
    rad_lat_B = radians(Lat_B)
    rad_lng_B = radians(Lng_B)
    pA = atan(rb / ra * tan(rad_lat_A))
    pB = atan(rb / ra * tan(rad_lat_B))
    xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))
    c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
    c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (xx + dr)
    return distance



    
    
