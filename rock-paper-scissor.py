print("welcome to rock paper scissor")

from random import randint

weapon = ['rock', 'scissor', 'paper']
player = str(input ("what weapon do you choose? "))
computer = (weapon[randint(0,2)])



if player == computer:
    print("player choose", player)
    print("computer choose", computer)
    print("Nobody wins! Draw!")
elif player == 'rock':
    print("player choose", player)
    print("computer choose", computer)
    if computer == 'paper':    
        print("You lose! Paper covers rock!")
    elif computer == 'scissor':               
        print("You Win! rock smashes scissor")
elif player == 'scissor':
    print("player choose", player)
    print("computer choose", computer)
    if computer == 'paper':
        print("You win! Scissor cuts paper")
    elif computer == 'rock':
        print("You lose! rock smashes scissor")
elif player == 'paper':
    print("player choose", player)
    print("computer choose", computer)
    if computer == 'scissor':
        print("You lose! Scissor cuts paper")
    elif computer == 'rock':
        print("You win! Paper covers rock")
else :
    print("Invalid input, check again!")


