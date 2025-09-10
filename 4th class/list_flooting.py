"""List Flattening (list + for loop)
Given a nested list, flatten it.
👉 Example Input: [[1, 2], [3, 4], [5]]
👉 Example Output: [1, 2, 3, 4, 5] """

list_a=[[1, 2], [3, 4], [5]]
list=[]
for i in list_a:
    for j in i:
        list.append(j)
print(list)