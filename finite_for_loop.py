for i in [1,2,3,4,5]:
    print(i)

friends = ["Deepak", "Anurag", "Saurabh", "Hani"]
for name in friends:
    print("Hello", name)

#Finding Largest number
largest_num=None
num=[28,57,92,19,63]
for i in num:
    if largest_num is None:
        largest_num=i
    elif i>largest_num:
        largest_num=i
print(largest_num)
print("Okay Done")
