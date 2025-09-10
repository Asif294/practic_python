""" While Loop (with dict, list, tuple, set)
List Pop Simulation (list + while loop)
Keep popping elements until list is empty.
👉 Example Input: [10, 20, 30]
👉 Example Output:
Removed: 30
Removed: 20
Removed: 10
List is empty now """


number=[10,20,30,40]
i=1
while i<=len(number):
    print(f"Removed : {number.pop()}")
print("List is empty now ")

