contact={
    'kavya':1234567890,
    'Ashwardh':9876543210
    }

def add_contact():
    name=input('Enter contact name:')
    phone=int(input('Enter phone number:'))
    contact[name]=phone
    print('contact added successfully')
def search_contact():
    name=input('Enter name to search:')
    if name in contact:
        print('Name:',name)
        print('phone number:',contact[name])
    else:
        print('contact not found')
def update_contact():
    name=input('Enter name to update:')
    if name in contact:
        phone=int(input('Enter new phone number:'))
        contact[name]=phone
        print('contact updated successfully')
    else:
        print('contact not found')
def delete_contact():
    name=input('Enter name to delete:')
    if name in contact:
        del contact[name]
        print('contact deleted successfully')
    else:
        print('contact not found')
def view_contact():
    if len(contact)==0:
        print('No contacts available')
    else:
        for i in contact:
            print('Name:',i,'Phone number:',contact[i])
def show_menu():
    print('1.Add contact')
    print('2.search contact')
    print('3.update contact')
    print('4.delete contact')
    print('5.View contact')
    print('6.Exit')

for i in range(1000):
    option=int(input('Enter your option:'))
    if option==1:
        add_contact()
    elif option==2:
        search_contact()
    elif option==3:
        update_contact()
    elif option==4:
        delete_contact()
    elif option==5:
        view_contact()
    elif option==6:
        print('Exit')
    else:
        print('Invalid')
