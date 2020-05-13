name = "DeePak"
lower_name = name.lower()
print(lower_name)
print("Hello".lower() + " " + lower_name)
print(lower_name.upper())

# find method in string

x = lower_name.find("pa")
print(x)
y = lower_name.find('z')
print(y)

# replace method in strings

z=lower_name.replace('ee','aa')
print(z)

# to remove spaces // strippind whitespaces

ky = "    Hello, Good Morning !    "
print(ky)
ls = ky.lstrip()
print(ls)
rs = ky.rstrip()
print(rs)
s = ky.strip()
print(s)

# method to find //prefixes//

if lower_name.startswith('d') :
    print("Yes it starts with d")

#   Parsing and extraction // slicing specific things from a strings

id = "deepak.1923cs1112@kiet.edu Tuesday"
pos1 = id.find("@")
pos2 = id.find(" ",pos1)
print(id[pos1+1 : pos2])
