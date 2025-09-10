"""Sum Until Limit (list + while loop)
Keep adding numbers until sum exceeds 100. Print how many numbers were added.
👉 Example Input: [20, 30, 25, 40, 15]
👉 Example Output:
Sum exceeded 100 after adding 4 numbers"""

n=list(map(int,input("Enter value : ").split()))
sum=0
counter=0
for i in n:
    sum=sum+i
    counter+=1
    if sum>=100:
        break
print(f"Sum exceeded 100 after adding {counter} numbers")