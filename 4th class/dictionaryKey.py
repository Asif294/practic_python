""" Dictionary Key Existence (dict + if-else)
Check if a user-input key exists in a dictionary.
👉 Example Dictionary: {"id":101, "name":"Tarek", "age":22}
👉 Input: name → Output: Value: Tarek
👉 Input: salary → Output: Key not found """

dic={
    "id":1001,
    "name":"Asif",
    "age":"20",
    "distic":"Sherpur"
}
n=input("Enter a key : ")
if n in dic:
    print(f"value : {dic[n]}")
else:
    print("Key not found")
