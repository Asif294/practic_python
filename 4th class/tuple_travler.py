"""Tuple Traversal (tuple + while loop)
Traverse tuple and print elements.
👉 Example Input: (100, 200, 300)
👉 Example Output:
100
200
300 """

n=tuple(map(int,input("Enter number :").split()))
for i in n:
    print(i)