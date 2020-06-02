fhand=open("mbox-short.txt")
lst=list()
dt=dict()
for line in fhand:
    if line.startswith("From "):
        newlst=line.split()
        lst.append(newlst[1])

for key in lst:
    dt[key]=dt.get(key,0)+1


bigCount=None
bigWord=None
for k,v in dt.items():
    if bigCount is None or v>bigCount:
        bigCount=v
        bigWord=k
print(bigWord,bigCount)
