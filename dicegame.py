import random
def game():
    choices=[1,2,3,4,5,6]
    computer=random.choice(choices)
    player=input('Do you want to roll the dice?(yes/no):')
    if player=='yes':
        print('Dice number is:',computer)
        if computer==6:
            print('Congratulations! you got 6')
        else:
            print('Move your coin by',computer,'steps')
    elif player=='no':
        print('Thank you for playing')
    else:
        print('Invalid choice!')
game()
        
