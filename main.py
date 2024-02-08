# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
'''


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pymysql
class AccountDoesNotExist(Exception):
    pass
class BalanceLow(AccountDoesNotExist):
    pass
con=pymysql.connect(host='localhost',user='root',password='root',database='faizan8')
cur=con.cursor()
try:
    saccno=int(input('Enter Acount Number:'))
    tamt=int(input('Enter Transfer Amount:'))
    damt = int(input('Enter Destination Account Number:'))
    query1="select bal from customer where caccno={}".format(saccno)
    cur.execute(query1)
    balance=cur.fetchone()

    if (cur.rowcount != 1):
        print("1st Account Number is Not Available")
        raise AccountDoesNotExist

    if balance is None or int(tamt)>balance[0]:
        print("Check your account balance")
        raise BalanceLow

    query2="update customer set bal=bal-{} where caccno={}".format(tamt,saccno)
    cur.execute(query2)
    '''
    if(cur.rowcount!=1):
        print("1st Account is Not Available")
        raise AccountDoesNotExist
    '''
    query3="update customer set bal=bal+{} where caccno={}".format(tamt,damt)
    cur.execute(query3)
    if(cur.rowcount!=1):
        print('2nd Account Number is Not Available')
        raise AccountDoesNotExist
    else:
        print("Transfer Successfull")
    cur.close()
    con.commit()
except:
    con.rollback()
    print("Transfer Failed")
finally:
    if con!=None:
        con.close()

