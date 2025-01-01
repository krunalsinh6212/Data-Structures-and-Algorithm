#Creation of List
#Type 1:
list1=[]
print(list1)
#Type 2:
my_list=list()
print(my_list)

my_list=[1,2,3,4,5]

#Find The Length Of List
print(len(my_list))

#Find Maximum Number of Giving List
print(max(my_list))

#Find The sum Of the List
print(sum(my_list))

#Returns True if at least one element in the iterable is truthy (non-zero, non-None, non-false equivalent). Otherwise, it returns False
print(any(my_list))

#Returns True if all elements in the iterable are truthy. If any element is falsy, it returns False
print(all(my_list))

#Print List In sorted Form(Ascending )
print(sorted(my_list))

#Print List In sorted Form(Descending)
print(sorted(my_list,reverse=True))

#delete a list
del(my_list)