import numpy as np

# key = size of the house , value = number of bedrooms 
x = np.array([ [200 , 6] ,[300 ,5]  , [400 , 4] , [500 ,3] , [600 ,2]] , dtype = float) 

y = np.array([200 , 300 , 500 , 600 , 650 ],dtype = float)


m = len(y)

w1 = 0 
w2 = 0 
b = 0 

alpha = 0.000001 

iterations = 10000

for i in range(iterations):
    y_pred = b + w1*x[:,0] + w2*x[:,1] 


    error = y_pred-y

    cost =(1/(2*m)) * np.sum(error ** 2)

    dw1 = (1/m)*np.sum(error*x[:,0])
    dw2 = (1/m)*np.sum(error*x[:,1])
    db = (1/m)*np.sum(error) 


    w1 = w1 - alpha * dw1 
    w2 = w2 - alpha * dw2 
    b  = b - alpha * db


    if i % 1000 == 0:
        print("iteration:" , i , "cost:" , cost) 



print("\n Final Parameters:")
print("w1 = ", w1) 
print("w2 = ", w2)
print("b=", b)


