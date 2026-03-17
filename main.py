import numpy as np
#1. numpy 사용해서 배열 생성하기
data1 = np.array([40,30,20,10])
print(data1)

data2 = np.array([[1,2],[3,4]])
print(data2)

data3 = np.zeros((3,4,2))
print(data3)

data4 = np.ones((8))
print(data4)

#arange, full, linsapce, random 등등

#2. numpy shape, ndim(n차원), dtype(데이터타입), size 등등
print(data1.dtype, data2.dtype, data3.dtype, data4.dtype)

#size, T, itemsize ...
