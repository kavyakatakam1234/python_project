balance=10000
print('1.Check_balance')
print('2.deposit')
print('3.withdraw')
print('4.Show_menu')

def Check_balance():
    print('available balance:',balance)
Check_balance()
def deposit():
    global balance
    amount=int(input("Enter amount: "))
    balance=balance+amount
    print('Balance:',balance)
def withdraw():
    global balance
    amount=int(input('Enter withdraw amount:'))
    if amount>0:
        balance=balance-amount
        print('available balance:',balance)
    elif amount<=0:
        print('valid amount')
    else:
        print('insufficient balance')
def show_menu():
    print('1.Check_balance')
    print('2.deposit')
    print('3.withdraw')
    print('4.Exit')
              
option=int(input('Enter your option:'))
if option==1:
    Check_balance() 
elif option==2:
    deposit()
elif option==3:
    withdraw()
else:
    print('exit')
    
              
