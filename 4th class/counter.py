"""For Loop (with dict, list, tuple, set)
Word Frequency Counter (dict + for loop)
Count how many times each word appears in a string.
👉 Example Input: "apple banana apple orange banana apple"
👉 Example Output:
{"apple": 3, "banana": 2, "orange": 1} """


from collections import Counter
fruts=input("Enter word : ").split()
word_count=Counter(fruts)
print(word_count)

