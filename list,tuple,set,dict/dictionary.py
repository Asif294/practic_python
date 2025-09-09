# What is a dictionary in Python?
""" dictionary is a collaction  which is ordered , changable and do not allow duplicates , disctionary are used store data values in  {key:value}  pairs """

#Create a dictionary of 3 students with their names as keys and ages as values.
student={
    "Asif":20,
    "Rubayet":21,
    "Asad":22
}

# . How do you access the value of a dictionary using a key?
print(student["Asad"])

#  Write a program to update the value of a dictionary key.
student["Asad"]=58
print(student)
#  What will happen if you try to access a key that does not exist in a dictionary?

""" if we try to access this a key that does not exist in dictionary give me a keyError  """

# What is the difference between dict.get(key) and dict[key]? Show with an example
"""if we use dict.get(key) then if exist this key we get values or not exist we get none or defult value on the outher hand if we use dict[key] if does not exist key value its give keyError """

#  Explain how nested dictionaries work with an example of storing student data (name, subjects, marks).
student_data = {
   "Asif":{
       "subject":"math",
       "marks":80
   },
   "Asad":{
       "subject":"english",
       "marks":70,
   },
   "Nijam":{
     "subject": "bangla",
     "marks":60
   }
}