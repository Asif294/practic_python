"""👉 Example Input: [("Rafi", 20), ("Mina", 16), ("Kamal", 25)]
👉 Example Output:
Eligible: Rafi, Kamal
Not Eligible: Mina """

tup=[("Rafi", 20), ("Mina", 16), ("Kamal", 25)]
eligibal=[]
notelegible=[]
for name ,age in tup:
    if age>=18:
        eligibal.append(name)
    else:
        notelegible.append(name)
print(f"Eligibale {eligibal}")
print(f"NotEligibale {notelegible}")
        