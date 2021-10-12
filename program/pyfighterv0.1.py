import random
player1=1
player2=2
player1Health=20
player2Health=20
player1Defense=5
player2Defense=5
player1Attack=5
player2Attack=5
currentPlayerTurn=1
gamePlaying=True
def punch(attack, health, defense):
    hitScore= randint(1,10) + attack
    damage=3
    if hitScore>5+defense:
        if currentPlayerTurn==1:
            player2Healthplayer2Health-damge
            hitScore=hitScore+1
            damage=damage-1
        else:
            player1Health=player1Health-damage
            hitScore=hitScore+1
            damage=damage-1
        return True
    else:
        hitScore=hitScore+1
        damage=damage-1
        return False
def kick(attack,health,defense):
    hitScore= randint(1,10) + attack
    damage=3
    if hitScore>5+defense:
        if currentPlayerTurn==1:
            player2Healthplayer2Health-damge
            hitScore=hitScore-1
            damage=damage+1
        else:
            player1Health=player1Health-damage
            hitScore=hitScore-1
            damage=damage+1
        return True
    else:
        hitScore=hitScore-1
        damage=damage+1
        return False
while gamePlaying==True:
    if currentPlayerTurn == 1:
        currentAttack=player1Attack
        currentDefense=player2Defense
        currentHealth= player2Health
        answer=input("Would you like to punch or kick? ")
        if answer=="Punch" or "punch":
            punch(currentAttack, currentHealth, currentDefense)
            if punch()==True:
                print("You have hit the target. The opponent's health is " + str(currentHealth))
                currentPlayerTurn=2
            else:
                print("You have miss.")
                currentPlayerTurn=2
        elif answer=="Kick" or 'kick':
            kick(currentAttack,currentHealth,currentDefense)
            if kick()==True:
                print("You have hit the target. The opponet's health is " + str(currentHealth))
                currentPlayerTurn=2
            else:
                print("You have miss.")
                currentPlayerTurn=2
        else:
            print("You lost your turn")
            currentPlayerTurn=2
    else:
        currentAttack=player2Attack
        currentDefense=player1Defense
        currentHealth= player1Health
        answer=input("Would you like to punch or kick? ")
        if answer=="Punch" or "punch":
            punch(currentAttack, currentHealth, currentDefense)
            if punch()==True:
                print("You have hit the target. The opponent's health is " + str(currentHealth))
                currentPlayerTurn=1
            else:
                print("You have miss.")
                currentPlayerTurn=1
        elif answer=="Kick" or 'kick':
            kick(currentAttack,currentHealth,currentDefense)
            if kick()==True:
                print("You have hit the target. The opponet's health is " + str(currentHealth))
                currentPlayerTurn=1
            else:
                print("You have miss.")
                currentPlayerTurn=1
        else:
            print("You lost your turn")
            currentPlayerTurn=1
    if currentHealth ==0:
        print("The player who is still alive wins.")
        break
        
                
    
        
        
