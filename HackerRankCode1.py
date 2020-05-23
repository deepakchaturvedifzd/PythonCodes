n=input()
n=int(n)
try :
    if n>=1 and n<=100:
        if n%2 != 0:
            print("Weird")
        if n%2==0:
            if n>=2 and n<=5 :
                print("Not Weird")
            if n>=6 and n<=20:
                print("Weird")
            if n>20:
                print("Not Weird")
except:
    print("Error")
    quit()
