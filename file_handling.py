fhand = open("project description.txt")
print(fhand)
#fr=fhand.read()
#print(len(fr)) #this shows number of characters in the file
#print(fr[:])

# to check the no. of lines
# or to get how many times the loop executes

count=0
for line in fhand :
    count = count + 1
    line=line.rstrip()
    if not line.startswith("From"):
        continue
    print(line)

print("Number of lines are : ",count)
