purse=dict()
purse['money']=12
purse['pen']=3
purse['cards']=2
purse['cards']=purse['cards']+2
print(purse)

ooo={} #Empty dictionary
print(ooo)

#Counting With Dictionary

ccc=dict()
ccc['deepak']=5
ccc['anurag']=2
ccc['hani']=1
names=["saurabh",'vibhanshu','deepak','prashant','devendra','anurag','vidit','hani']
for name in names:
    if name not in ccc:
        ccc[name]=1
    else:
        ccc[name]=ccc[name]+1
print(ccc)

#Get method in Dictionary

ccc=dict()
ccc['deepak']=5
ccc['anurag']=2
ccc['hani']=1
names=["saurabh",'vibhanshu','deepak','prashant','devendra','anurag','vidit','hani']
for name in names:
    ccc[name]=ccc.get(name,0)+1    #if key found the get will get value
                                    #if key not found get will get default value 0(zero)
print(ccc)

#for loop in Dictionary runs through keys not values

for key in ccc:
    print(key,ccc[key])

#Retriving keys and values from dictionary

jjj={'amit':1,'suresh':45,'ramesh':23}
print(list(jjj))  #list of keys
print(jjj.keys())  #list of keys
print(jjj.values()) #list of values
print(jjj.items())  #tuple


#Using Two Iteration variables

for aaa,bbb in jjj.items():
    print(aaa,bbb)     # aaa goes on keys and bbb goes on values
