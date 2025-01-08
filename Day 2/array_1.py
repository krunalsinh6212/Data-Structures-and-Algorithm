# import array
# new_object = array.array('d',[1.0,2,3,4,5])
# print(new_object.itemsize)
# print("---------------------")

# new_obj = array.array('i',[1,2,3,4,5])
# print(new_obj.typecode)
# print("---------------------")

# new_o =  array.array('i',[1,2,3,4,5])
# print(new_o.insert(2,6))
# print("---------------------")

# new_o.append(7)
# y = [8,9,10]
# new_o.extend(y)
# print(new_o)
# print("---------------------")

# print(new_o.count(4))
# print("---------------------")

# print(new_o.index(1))
# print("---------------------")

# new_o.pop()
# new_o.remove(3)
# print(new_o)
# print("---------------------")

# new_o.reverse()
# print(new_o)
# print("---------------------")


# print(sorted(new_o))
# print("---------------------")

# import numpy as np
# intarr = np.array([1, 2, 3, 4, 5])
# floatarr = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
# print(intarr)
# print("---------------------")
# print(floatarr)
# print("---------------------")

# a1 = np.empty((3,4))
# a2 = np.zeros((3,4))
# a3 = np.ones((3,4))
# a4 = np.full((2,2),7)
# print(a1)
# print("---------------------")
# print(a2)
# print("---------------------")
# print(a3)
# print("---------------------")
# print(a4)
# print("---------------------")

# a5 = np.eye(3)
# a6 = np.identity(3)
# print(a5)
# print("---------------------")
# print(a6)
# print("---------------------")

# a7 = np.array([1, 2, 3, 4])
# a8 = np.array([1, 1, 2, 2, 3, 3, 4, 4])
# print(a7.dtype)
# print(a8.dtype)
# print("---------------------")
# print(a7.itemsize)
# print(a8.itemsize)
# print("---------------------")
# print(a7.strides)
# print(a8.strides)
# print("---------------------")
# print(a7.nbytes)
# print(a8.nbytes)
# print("---------------------")
# print(a7.data)
# print(a8.data)
# print("---------------------")
# print(a7.ndim)
# print(a8.ndim)
# print("---------------------")
# print(a7.shape)
# print(a8.shape)
# print("---------------------")
# print(a7.size)
# print(a8.size)








import numpy as np;

# a1 =np.array([1,2,3,4])
# a2 =np.array([1.2,2.2,3.3,4.4])
# print(a1.dtype)
# print(a2.dtype)
# print(a1.itemsize)
# print(a2.itemsize)
# print(a1.nbytes)
# print(a2.nbytes)
# print(a1.data)
# print(a1.strides)
# print(a2.data)
# print(a2.strides)

#-----------------
# a1 = np.array([1,2,3,4])
# a2 = np.array([[1,2,3,4],[5,6,7,8]])
# print(a1.ndim)
# print(a2.ndim)
# print(a1.shape)
# print(a2.shape)
# print(a1.size)
# print(a2.size)

# #-----------
# a1 = np.array([[10,2,3,4],[5,6,7,8]])
# a2 = np.array([[1,1,1,1],[2,2,2,2]])
# a3=a1+a2
# print(a3)
# a4=a1-a2
# print(a4)
# a5=a1*a2
# print(a5)
# a6=a1/a2
# print(a6)
# a7=a1%a2
# print(a7)
# a8=a1**a2      
#print(a8)

# a=np.array([[1,2,3],[4,5,6]])
# print(a.sum())
# print(a.min())
# print(a.max(axis=0))
# print(a.max(axis=1))
# print(a.cumsum(axis=1))
# print(np.mean(a))
# print(np.median(a))
# print(np.corrcoef(a))
# print(np.std(a))

# Linear Algebra
a1 = np.array([[1,2,3,4],[5,6,7,8]])
a2 = np.array([[1,1,1,1],[2,2,2,2]])

a3 = a1 * a2
print(a3)
print("---------------------")

a6 = np.transpose(a1)
print(a6)
print("---------------------")

# a5 = a1.dot(a2)
# print(a5)
# print("---------------------")

a7 = np.trace(a1)
print(a7)