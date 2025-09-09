# How do you create a list in Python? Write an example.
number=[21,45,65,78,65,95,68]
# What is the difference between append() and extend() in a list?
number.append(24)   #append push data in last possition
print(number) 
# output -- [21,45,65,78,95,68,24]
# Write a Python program to find the maximum and minimum values in a list.
max_value=max(number)
print(max_value)
# output----95
min_valu=min(number)
print(min_valu)
#output----21
# How do you remove duplicate values from a list??
unicqe_list=list(set(number))
print(unicqe_list)
# [21,45,65,78,95,68]
# If you have fruits = ["apple", "banana", "mango"], how do you replace "banana" with "orange"?
fruits=["apple","banana","mango"]
fruits[1]="orange"
print(fruits)
# output---["apple","banana","mango"]
# Given a nested list: [[1,2], [3,4], [5,6]], write code to flatten it into [1,2,3,4,5,6].
nested_list=[[1,2],[3,4],[5,6]]
new_list=[]
for i in nested_list:
    for j in i:
        new_list.append(j)
print(new_list)
# output---[1,2,3,4,5,6]
# What will happen if you use a list as a default argument in a function? Why is it dangerous?
# Ans # if i use a default argument in a function same object is reused across all calls to the function.