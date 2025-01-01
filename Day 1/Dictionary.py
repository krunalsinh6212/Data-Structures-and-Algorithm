#create a Dictiory:

#type:1
my_dict={}
#cheack the type... 
print(type(my_dict))   #output: <class 'dict'>
print(my_dict)


#type:2
my_dict=dict()
print(type(my_dict))   #output: <class 'dict'>
print(my_dict)

dict1={
    'A101':'Rohan',
    'A102':'Swapnil',
    'A103':'Vedant',
    'A104':'Krunal',

}

for item in dict1.items():
    print(item)

#output:
"""
('A101', 'Rohan')
('A102', 'Swapnil')
('A103', 'Vedant')
('A104', 'Krunal')
"""
 
for k in dict1.keys():
    print(k)

#output:
"""
A101
A102
A103
A104
"""
for v in dict1.values():
    print(v)

#output:
"""
Rohan
Swapnil
Vedant
Krunal
"""
for k,v in dict1.items():
    print(k,v)  

#output:
"""
A101 Rohan
A102 Swapnil
A103 Vedant
A104 Krunal
"""

#Dictonary Methods:
fir_dict={
    101:'Rohan',
    102:'Swapnil',
    103:'Vedant',
    104:'Krunal',
}
print(fir_dict.pop(101))

print(fir_dict.get(105,'Absent'))

sec_dict={105:'shyam'}
#update 
fir_dict.update(sec_dict)
print(fir_dict)

#pop last items
fir_dict.popitem()
print(fir_dict)

#remove all element
fir_dict.clear()
print(fir_dict)

