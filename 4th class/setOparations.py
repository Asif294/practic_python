"""
set Operations (set + for loop)
Find all unique vowels in a string.
👉 Example Input: "Programming is awesome"
👉 Example Output: {'a', 'i', 'o', 'e'}
"""
value ="Programming is awesome"
list =[]
for i in value:
    if i=="a":
        list.append('a')
    elif i=="e":
        list.append("e")
    elif i=="i":
        list.append("i")
    elif i=="o":
        list.append("o")
    elif i=="u":
        list.append("u")
print(set(list))

