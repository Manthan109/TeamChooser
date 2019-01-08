from random import choice 
n=int(input("Enter number of players - "))
players=[]
for i in range(n):
    name=input()
    players.append(name)


teamA=[]
teamB=[]
while(len(players)>0):
    playerA=choice(players)
    teamA.append(playerA)
    players.remove(playerA)
    print("TeamA : ",teamA)
    print("Players Left : ",players)

    if(players!=[]):
        playerB=choice(players)
        teamB.append(playerB)
        players.remove(playerB)
        print("TeamB : ",teamB)
        print("Players Left : ",players)

print("The Final Team Looks Like : ")
print("TeamA : ",teamA)
print("TeamB : ",teamB)
    
    
