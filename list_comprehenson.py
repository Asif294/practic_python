numbers=[12,15,45,85,96,67,3,85,54,49,27,31,45]
odds=[]
for num in numbers:
    if num % 2==1:
        odds.append(num)
print(odds)
# odd_number=[num for num in numbers if num % 2==0 ]
# print(odd_number)