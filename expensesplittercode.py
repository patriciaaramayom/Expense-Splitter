def create_new_group(): 
    title=input('Title: ')
    des=input('Description: ')
    cur=input('Currency: ')
    cat=input('Category: ')
    par=float(input('Participants: '))
    return title,des,cur,cat,par


def calc(title,des,cur,cat,par):
    expense=float(input('Expense: '))
    amount= expense/par
    print (amount)
    return

def menu():
    print('WELCOME TO EXPENSE SPLITTER')
    print('	1.New Group')
    print('	2.Exit')
    data=int(input("Enter your choice: "))
    return data
data=menu()
if data==1:
    title,des,cur,cat,par=create_new_group()
    calc(title,des,cur,cat,par)
else:
    print('Goodbye')