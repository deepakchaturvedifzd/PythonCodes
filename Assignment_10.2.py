fhand=open("mbox-short.txt")
di=dict()
lst=list()
for line in handle:
    if line.startswith("From "):
        pos1=line.find("Jan")
        pos2=line.find(":")
        part=(line[pos1+7:pos2])
        di[part]=di.get(part,0)+1

for k,v in di.items():
    lst.append((k,v))
lst=sorted(lst)
for k,v in lst:
    print(k,v)
