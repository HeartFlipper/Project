import numpy as np

#1D array
num1 = [1,2,3,4,5]
num2 = [5,6,7,8,9]
ar1 = np.array(num1)
ar2 = np.array(num2)
# l=len(ar1)        #length of array
# print(l)
print(ar1.shape)    #shape of the array
print(ar1+ar2)
print(ar1*ar2)
a=np.power(ar1,ar2)
print(a)

#2D array
num=[1,2,3,4,5],[5,6,7,8,9]
ar=np.array(num)
print(ar*ar)
print(a)
print(ar[1,4])      #pos_row,column

#3D array
r=np.random.random((3,4,4))
print(r)
print(r[2,2,2])

#math_analysis
# Sw=np.linspace(1,50,25)                #start,stop,no.of.values between start and stop
t=np.arange(0,11,1)                      #start,stop,step
# t=float(input("Enter = "))
log=np.log10(t)                          #log base 10
print(log)
exp=np.exp(t)
print(exp)
sqrt=np.sqrt(t)
print(sqrt)
x=np.sin(np.pi)
print(x)
x=np.arcsin(1)
print(x)

#dictionary
data={"poro":[0.1,0.2,0.3],"perm":[50,100,150],"lith":["sst","shale","lst"]}
x=np.array(data)
print(x)
#dictionary can't be converted to array


