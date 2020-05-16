print('conditional statement')

#always use try and except so that you 
#can avoid tracebacks 

istr=input('Enter anything :')
try:
    astr=int(istr)
    print("You entered number")
    if astr<100:
        print('Number is less than 100')
    else:
        print('Number is greater or equal to 100')
except:
    print("You entered characters")
