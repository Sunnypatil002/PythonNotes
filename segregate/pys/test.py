n=int(input("enter the guests age"))
userlist = n.split(' ')

l=[]
for i in range(0, n):
    a = int(input())
    l.append(a) 
    
for i in l:
    if(l<=2):
        charges = 0
        print(charges)
    elif(l>2 and l<=12):
        charges = 14
        print(charges)
    elif(l>12 and l<65):
        charges = 18
        print(charges)
    else :
        charges = 23
        print(charges)
    



#I/P read number of guests and ages of all guests
#O/P cost