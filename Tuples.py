#They are like list ....difference of using paranthesis()

ooo=('Deepak','Anurag','Some_other_guy')
print(ooo[2])
jjj=(4,5,87,12)
print(max(jjj))

#tuples are non mutable...we cant change value of it same as of strings
#list are mutable
#so we cant sort,append,etc the tuples

(a,b)=("Deepak",99)
print(a)

di={}
di['ok']=3
di['not_ok']=67
print(di.items()) #This di.items gives a tupple

#We can compare tuples

if (0,1,2)<(0,4,1):
    print("Compared")

#How to sort tuples :
    #By keys
aaa={'a':1,'b':34,'c':21}
temp=list()
for k,v in aaa.items():
    print(k,v)
temp=sorted(aaa.items())
print(temp)

    #By value
aaa={'a':1,'b':34,'c':21}
temp=list()
for k,v in aaa.items():
    temp.append((v,k))  #Each element in a list is a tuple
temp=sorted(temp,reverse=True) #In decreasing order
print(temp)
