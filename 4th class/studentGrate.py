"""👉 Example Input: {"Alice":85, "Bob":60, "John":30}
👉 Example Output:
Alice → Grade A
Bob → Grade B
John → Fail """ 
dict={}
n=int(input())
for i in range(n):
    key=input()
    Value=int(input())
    dict[key]=Value

for x,y in dict.items():
    if y >=80 :
        print(f"{x} -> Grade A+")
    elif y>=70 and y<=79:
        print(f"{x} -> Grade A")
    elif y>=60 and y<=69:
        print(f"{x} -> Grade A-")
    elif y>=50 and y<=59:
        print(f"{x} -> Grade B")
    elif  y>=40 and y<=49:
        print(f"{x} -> Grade B-")
    else :
        print(f"{x} -> Fail")

