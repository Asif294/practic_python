# What is a tuple? How is it different from a list?
"""ANS: tuple is a collaction data type that can hold multiple item .tuple are immutable ,its can not cange there element |  major defferent is tuple immutable and list mutable and tuple define with {} and list define with [] """

# Write a tuple containing the names of 5 countries.

countries = ("Bangladesh", "Japan", "Canada", "Germany", "Australia")
print(countries)

# Can you change the value of a tuple after creating it? Why or why not?
""" after creating tuple i cannot change value because tuple are immutable   """
# How do you access the last element of a tuple?
countries=countries[-1]
print(countries)

# Convert the tuple (10, 20, 30) into a list.
t=(10,20,30)
t=list(t)
print(t)
#Given a tuple t = (1, [2, 3], 4), can you modify t[1][0]? Why or why not?
a=(1,[2,3],4)
a[1][0]=44
print(a)
""" Yes its changable because [1][0] its a list and muteable """
# Write a Python program that takes a list of tuples (e.g., [("a", 1), ("b", 2)]) and converts it into a dictionary.

list_of_tuple=[('e',4),('a',3)]
list_of_tuple=dict(list_of_tuple)
print(list_of_tuple)


# Given a nested tuple like ((1,2), (3,4), (5,6)), write a program to flatten it into a single tuple (1,2,3,4,5,6).
tou=((1,2),(3,4),(5,6))
simple_list=[]
for i in tou:
    for j in i:
        simple_list.append(j)
print(tuple(simple_list))
        
