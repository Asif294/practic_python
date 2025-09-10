"""Dictionary Search (dict + while loop)
Continuously ask user for a key until "exit".
👉 Example Dictionary: {"id":1, "name":"Sami", "age":25}
👉 Input: name → Output: Sami
👉 Input: salary → Output: Not found
👉 Input: exit → Program stops"""
dict={
    "id":1,
    "name":"Asif",
    "age":25
}
n =input("Enter a key :")

if n in dict:
    print(dict[n])
elif n=='exit':
    print("Program stops")
else:
    print("Not found")
