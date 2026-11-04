import random
secret_num=random.randint(1,100)
while 'True':
    guess=int(input('Guess a number between 1 and 100:'))
    if guess<secret_num:
         print('Too Low! Try Again.')
    elif guess>secret_num:
         print('Too High! Try Again.')
    elif guess==secret_num:
        print('Congratulations!,You Won')
        print('Game over!')
    else:
        print('Invalid Choice')

