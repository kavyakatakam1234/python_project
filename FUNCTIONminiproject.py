print('******Sample Calculator******')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
print('5.Exit')

n1=int(input('Enter a first number:'))
n2=int(input('Enter a second number:'))

def add(n1,n2):
    print('Addition:',n1+n2)
add(n1,n2)

def sub(n1,n2):
    print('Subtraction:',n1-n2)
sub(n1,n2)

def mul(n1,n2):
    print('Multiplication:',n1*n2)
mul(n1,n2)

def div(n1,n2):
    print('Division:',n1/n2)
div(n1,n2)
       
option=int(input('Enter your option:'))
if option==1:
    add(n1,n2)
elif option==2:
    sub(n1,n2)
elif option==3:
    mul(n1,n2)
elif option==4:
    div(n1,n2)
elif option==5:
    print('Exit')
else:
    print('Invalid')
