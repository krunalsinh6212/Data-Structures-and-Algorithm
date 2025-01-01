#create a Set:

my_set=()
#cheack the type... 
print(type(set))   #output: <class 'set'>
print(my_set)


my_set1={'A','B','c'}
my_set={'gate','fate','late'}


my_set.add('rate')
print(my_set)     #output:{'fate', 'late', 'rate', 'gate'}

my_set.update(my_set1)
print(my_set)    #output:{'fate', 'late', 'B', 'c', 'rate', 'gate', 'A'}

newSet=my_set1.copy()
print(newSet)    #output:{'B', 'c', 'A'}

my_set.remove('gate')
print(my_set)     #output:{'fate', 'late', 'B', 'c', 'rate', 'A'}

my_set.discard('fate')
print(my_set)     #output:{'late', 'B', 'c', 'rate', 'A'}

my_set.clear()
print(my_set)     #output:set()


my_set={12,15,10,5,1}
sec_set={20,30,50}

print(my_set.issuperset(sec_set)) #output:False
print(my_set.issubset(sec_set))   #output:False
print(my_set.isdisjoint(sec_set)) #output:True


#set-1
Engineer={'Rohan','Vijay','Sanjay','Ajay','Dinesh'}
#set-2
Managers={'Adity','Sanjay','Ajay'}

#union
new_Set=Engineer|Managers
print(new_Set)    #output:{'Vijay', 'Dinesh', 'Ajay', 'Adity', 'Sanjay', 'Rohan'}


#intersection
new_Set=Engineer & Managers
print(new_Set)    #output:{'Ajay', 'Sanjay'}


#differance
new_Set=Engineer- Managers
print(new_Set)    #output:{'Vijay', 'Dinesh', 'Rohan'}


# Symentic differance
new_Set=Engineer^Managers
print(new_Set)    #output:{'Vijay', 'Dinesh', 'Rohan', 'Adity'}

