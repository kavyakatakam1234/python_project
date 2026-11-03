import random
print('Two Dice Game')
user=input('Press enter to roll the dice:')
dice1=random.randint(1,6)
dice2=random.randint(1,6)
print('Dice 1:',dice1)
print('Dice 2:',dice2)
total=dice1+dice2
print('Total:',total)
if total>7:
    print('Congratulations...you won!')
elif total==7:
    print('Draw')
else:
    print('Computer wins!')
