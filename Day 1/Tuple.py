#create a Tupple:
#type 1
my_tuple1=()
#cheack the type... 
print(type(my_tuple1))   #output: <class 'tuple'>
print(my_tuple1)

#type 2
my_tuple=tuple()
print(my_tuple)

#Print the Same number in 5 times
my_tuple=(10,)*5
print(my_tuple)


#Student Tuple:
stud_list=('aaa','bbb','ccc','ddd','eee')

#Marks Tuple:
Marks_list=(80,90,89,70,75)

#Print the data of both list togather
for item in zip(stud_list,Marks_list):
    print(item)


#apply all method & function of List in tuple

# Note: Tuple is unmutable so we can't use Remove,add,append,extend,insert,pop,clear,sort,reverse
 

#tuple:1
x=(1,2,3,4)

#tuple:2
y=(10,20,x,30)   
print(y)         #output: (10, 20, (1, 2, 3, 4), 30)

#above code insert a tuple 1 in tuple 2 as single element


#tuple:1
x=(1,2,3,4)

#tuple:2
y=(10,20,*x,30)   
print(y)         #output: (10, 20, 1, 2, 3, 4, 30)

#above code insert a tuple 1 in tuple 2 as indivisual element


#tpl is boys group
tpl=('Aayush','Swapnil','Vaibhav','Rohan')

#list is Mixture of boys & Girls
list=['Rohan','Vaibhav','Nidhi','radha']

#count the boys & girls in list
boys=0
girls=0


#cheack the element of list is availble in tpl or not..
for ele in list:
    if isinstance(ele, str) and ele in tpl:
        boys +=1
    else:
        girls +=1

print(f"boys:{boys}")
print(f"girls:{girls}")

#output:
"""
boys:2
girls:2

"""
