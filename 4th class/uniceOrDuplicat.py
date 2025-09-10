element =input("Enter item :").split()
if len(element) == len(set(element)):
    print("All Unique")
else :
    print("Duplicat found")