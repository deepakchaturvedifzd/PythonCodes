x='letter'
i=0
while i < len(x):
    print(i,x[i])
    i = i+1

y="DEEPAK"
for letter in y :
    print(letter)

#find no. of a in a word

z= input("Enter a string : ")
i=0
count =0
while i < len(z) :
    if z[i]=='a':
        count = count + 1
    i=i+1
print(count)

flag=0
for letter in z :
    if letter == 'i':
        flag = flag + 1
print(flag)

print(z[0:5])
print(z[:])
print(z[9:])
