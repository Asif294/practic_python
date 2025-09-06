# dictionar follow {key:value ,key: value}
thisdect={
     'name':'asif',
     'address':'Sherpur',
     'age':20,

}
print(thisdect)
print(thisdect['name'])
print(thisdect.keys()) #only for find key 
print(thisdect.values())  # get all values
thisdect['language']='python'  #its adding new values
print(thisdect)
thisdect['name']='sada pakhi' #updated value 
print(thisdect)
del thisdect['age']  #delete any items 
print(thisdect)

#special looping for dictionary 
for key,value in thisdect.items():
    print(key ,value)
