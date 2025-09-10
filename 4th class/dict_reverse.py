"""Dictionary Reversal (dict + for loop)
Reverse key-value pairs in a dictionary.
👉 Example Input: {1:"a", 2:"b", 3:"c"}
👉 Example Output: {"a":1, "b":2, "c":3} """
dic={
    "a":1,
    "b":2,
    "c":3
}
rever_dict= {value:key for  key, value in dic.items()}
print(rever_dict)