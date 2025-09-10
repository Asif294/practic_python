"""Even/Odd Categorizer (list + dict + if-else)
Take a list of numbers and categorize them into even and odd inside a dictionary.
👉 Example Input: [1, 2, 3, 4, 5, 6]
👉 Example Output:
{"even": [2, 4, 6], "odd": [1, 3, 5]} """

number=list(map(int,input("Enter number : ").split()))
even=[]
odd=[]
for i in number:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
result ={"Even " : even , "Odd" : odd}
print(result)