l = [3,2,1,3,4,5] 

# sum = 0 

# for i in l :
#     sum += i ;

# print(i) 



# product = 1 

# for i in l :
#     product *= i 


# print(product)



# python list is a dyanmic array in nature .
# refrential arrays can have multiple types of input init.


import ctypes

class clist:
    def __init__(self):
        self.n = 0 ;
        self.size = 10 ;
        self.A = self.__build__array(self.size) 

    def __build__array(self , capacity):
        return (capacity*ctypes.py_object)()


    def __len__(self):
        return self.n 

    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ',' 
        return result

    def __getitem__(self, index):
        if 0 <= index <= self.n:
            return self.A[index] 
        else:
            return "ERROR ouT OF BOonNdS" 
         
        


    def __append__(self , item):
        if self.n == self.size :
            self.resize__(self.size*2) 

    def __resize__ (self , new_capacity):
        B = self.__build__array(new_capacity)
        self.size = new_capacity


        # now copy the content of A to B 

        for i in range(self.n):
            B[i] = self.A[i]
            
        self.A = B 

    
l = clist()

l.append("hello")
l.append(5) 
l.append(False)
l.append(5.4)


# len__(l)

print(l)

            







l = clist()

print(l)

