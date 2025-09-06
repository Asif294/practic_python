thisngs=('sunglass','phone','headphone','moneyBag','watch','airpod','mouse')
print(thisngs)
print(thisngs[1])  #show 1 number index value
print(thisngs[-1]) #-1 index use for last value print
print(thisngs[2:5]) #indexing start from 2 and end befor 5
print(thisngs[:4]) # its print value befor 4 index
print(thisngs[3:]) #this is started from 3 number index to last 
print(thisngs[-5:-1]) # its reverse indexing 
print(thisngs[::-1]) #reverse all tuple

if 'phone' in thisngs:
    print("Its avaible")

for item in thisngs:
    print(item)
# for length
print(len(thisngs))

#append value in touple 
y=list(thisngs)
y.append('keybord')
thisngs=tuple(y)
print(thisngs)

#index value change
x=list(thisngs)
x[0]="apole"
thisngs=tuple(x)
print(thisngs)

#join tuple 
tuple_1=('show','t-shart','shart')
join =thisngs+tuple_1
print(join)

