"""Unique Number Collector (set + while loop)
Keep asking user for numbers until -1. Store unique numbers in a set.
👉 Example Input: 5, 10, 5, 20, -1
👉 Example Output:
Unique Numbers: {10, 20, 5}"""

# n=list(map(int,input("Enter number :").split()))
n=5, 10, 5, 20, -1
li=[]
for i in n:
    if i>=0:
        li.append(i)
li=set(li)
print(f"Unique Number : {li}")
