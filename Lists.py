y=[1,2,8.8,"frIend"] #declaring a list
for x in y:
    print("hello",x)

#range returns a list
z=len(y)
print(z)
print(range(len(y)))

#without using loop accessing the elements of a List
for i in range(len(y)):
    ele = y[i]
    print("hello",ele)

#Concatenating Lists
a=[1,2,3]
b=[0,9,8]
c=a+b
print(c)
print(c[2:5]) #slicing of list

#Building a List from scratch
x=list()
x.append("Deepak")
x.append(99)
x.append(20)         #Lists are mutable so after appendind the x(list) is changed
print(x)
x.append("ok")
print(x)
if 99 in x:
    print("YES")
if 24 not in x:
    print("NO")

#Sorting of a List
z=[2,44,7,95,11001,67]
d=["Deepak","Anurag","Vibhanshu","Saurabh"]
z.sort()
d.sort()
print(z)
print(d)      #the original list will be sorted and hence changed

#How to convert a string into a List
abc= "My name is Deepak"
dab=abc.split()     #now dab is a list
print(dab)
print(len(dab))     #it splits based on spaces
for i in dab:
    print(i)
str="This;is;splitted;by;a;semicolon"
a=str.split(";")
print(a)
