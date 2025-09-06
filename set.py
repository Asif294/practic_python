# Intersection       common uncommon all 
A={2,3,5,6,7,8,7}
B={5,7,6,12,5,4,2,}
print(A & B)

# union only take common 
print(A | B)

#add number
A.add(4)
print(A)

#Add multiple element 
A.update([9,8,2])
print(A)

#remove element 
A.remove(9)
print(A)

# work but not error
A.discard(10)
print(A)

#pop arreng this set assending way
A.pop()
print(A)