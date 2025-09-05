# def green(name):
#     print(f"This is {name}")
# green("banana")

# def add_number(a,b):
#     c=a+b
#     print(c)
# add_number(3,5)
##paramiter 
# def sum(num_1,num_2=0):
#     result =num_1+num_2
#     return result
# total =sum(40,20)
# print(total)
# srri="this is "
# print(srri)

# *args
# def all_sum(*args):
#     a=0
#     for i in args:
#         a+=i
#     print(a)
#     return a
# a=all_sum(30,80,90,8)
# print(a)

def famous_name(first,last,title,aditional):
    name=f"{first} {last} {title} "
    return name

name=famous_name(first="Taher Ali",last='mia',title='khatuni',aditional='hou mau')
print(name)