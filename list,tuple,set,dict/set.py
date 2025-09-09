# What is a set in Python? How is it different from a list?
""" ANS: set is a unordered collection that keep unique eliments . its cannot accept duplicate value  . but list accept duplicate value . list define [] and set define with {} """
# Write a Python program to find the union of two sets.
A={2,4,6,8,9,2,4,5,6,5}
B={8,7,6,3,1,4,2,8,9,7}
print(A.union(B))
#output---{1,2,3,4,5,6,7,8,9}

# What happens if you add duplicate elements to a set?
""" When we add duplicate value in set , set automaticly ignor this and we get unice element  """
# How do you check if an element exists in a set?
X={4,6,8,9,4,5}
if 4 in X:
    print("3 is exists in set")
else:
    print("Not exists in set")

# Write a program to find the intersection of {1,2,3,4} and {3,4,5,6}
num1={1,2,3,4}
num2={3,4,5,6}
print(num1.intersection(num2))
# output--3,4