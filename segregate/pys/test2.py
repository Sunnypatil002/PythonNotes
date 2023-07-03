team =['rcb','csk','mum','gl','kk']
val= [0,0,0,0,0]
myDict = dict(zip(team,val))
print(myDict)
for i in range(0,len(team)):
    for j in range(i+1,len(team)):
        print(team[i] ,"vs" ,team[j])
        score = input('enter the name of winning team')
        if(team[i]==score):
            myDict[team[i]].append(2)
        elif(team[i]==score):
            myDict[team[j]].append(2)
        else:
            myDict[team[i]].append(1)
            myDict[team[j]].append(1)