if __name__ == '__main__':

    lst=list()

    nlst=list()

    di=dict()

    num=input()

    for _ in range(int(num)):

        name = input()

        score = float(input())

        lst.append([name,score])

lst.sort()

for k,v in lst:

    nlst.append([v,k])

min1 = None

for v,k in nlst:

    if min1 is None or v <= min1:

        min1 = v

nlst = [[v,k] for [v,k] in nlst if v != min1]

min2=None

for v,k in nlst:

    if min2==None or v<=min2:

        min2=v

for v,k in nlst:

    if v==min2:

        print(k)
