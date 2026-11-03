import random
print('Rock-Paper-Scissor game')
user=input('My choice:')
computer=['rock','paper','scissor']
res=random.choice(computer)
print('My choice:',user)
print('computer choice:',res)
if user=='rock' and res=='scissor':
    print('congrats...you won')
elif user=='paper' and res=='rock':
    print('congrats...you won')
elif user=='scissor' and res=='paper':
    print('congrats...you won')
elif user==res:
    print('draw')
else:
    print('computer wins')
    
