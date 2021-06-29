import mysql.connector
import takepass

u=takepass.username()
p=takepass.password()

connection=mysql.connector.connect(host="localhost",username=u,password=p,database="bank")
cursor=connection.cursor()

accept=None

while 0==0:
    print("Welcome To Bank Portal")
    a=input("Enter Who You Are (User/Bank Guy):")
    if a.title()=="User":
        c=input("Enter Account No.:")
        cursor.execute("select id from accounts;")
        li=cursor.fetchall()
        connection.commit()
        if c in li[0]:
            b=input("Enter Type of Authorization(CVV/PIN):")
            if b=="CVV":
                d=int(input("Enter CVV:"))
                cursor.execute("select CVV from accounts where id="+str(c)+";")
                e=cursor.fetchall()[0][0]
                connection.commit()
                if d==e:
                    accept=True
                else:
                    accept=False
            elif b=="PIN":
                d=int(input("Enter PIN:"))
                cursor.execute("select PIN from accounts where id="+str(c)+";")
                e=cursor.fetchall()[0][0]
                connection.commit()
                if d==e:
                    accept=True
                else:
                    accept=False
            else:
                print("Wrong Input")
            if accept==True:
                print("Actions:")
                print("1.Withdraw Money\n2.Deposit Money\n3.Check Account Balance\n4.None")
                i=int(input("Enter Action No.:"))
                if i==1:
                    cursor.execute("select balance from accounts where id="+str(c)+";")
                    bal=cursor.fetchall()[0][0]
                    connection.commit()
                    wit=int(input("Enter Amount To Be Withdrawn:"))
                    if wit<=bal:
                        bal=bal-wit
                        cursor.execute("update accounts set balance="+str(bal)+" where id="+str(c)+";")
                        print("Successfully Transaction Completed")
                        print("Collect Your Amount:"+str(wit))
                    else:
                        print("Amount Higher Than Balance Left")
                elif i==2:
                    cursor.execute("select balance from accounts where id="+str(c)+";")
                    bal=cursor.fetchall()[0][0]
                    connection.commit()
                    dep=int(input("Enter Amount To Be Deposited:"))
                    bal=bal+dep
                    cursor.execute("update accounts set balance="+str(bal)+" where id="+str(c)+";")
                    print("Successfully Transaction Completed")
                elif i==3:
                    cursor.execute("select balance from accounts where id="+str(c)+";")
                    bal=cursor.fetchall()[0][0]
                    connection.commit()
                    print(bal,"Is Your Account Balance")
                elif i==4:
                    pass
                else:
                    print("Wrong Input")
            elif accept==False:
                print("Wrong Input. Access Denied")
        else:
            print("Account Not Found")
    elif a.title()=="Bank Guy":
        pas=input("Enter Password")
        if pas=="Pa5sw0rD":
            print("Actions:")
            print("1.Add Account\n2.Delete Account\n3.Change Details\n4.Display All Accounts\n5.None")
            i=int(input("Enter Action No.:"))
            if i==1:
                name=input("Enter Name:")
                no=int(input("Enter Account No:"))
                cursor.execute("select id from accounts;")
                v=cursor.fetchall()
                connection.commit()
                
                if len(str(no))<=12 and no not in v[0]:
                    cvv=int(input("Enter CVV:"))
                    if len(str(cvv))<=3:
                        pin=int(input("Enter PIN:"))
                        if len(str(pin))<=4:
                            mon=int(input("Enter Expiry Month:"))
                            if mon<=12:
                                yr=int(input("Enter Expiry Year's Last Two Nos.:"))
                                
                                if len(str(yr))<=2:
                                    balance=int(input("Enter Account Balance:"))
                                    cursor.execute("insert into accounts(name,id,PIN,CVV,expmn,expyr,balance) values(%s,%s,%s,%s,%s,%s,%s);",(name,str(no).zfill(12),pin,cvv,mon,yr,balance))
                                    connection.commit()
                                    print("Account Added")
                                else:
                                    print("Wrong Input")
                            
                            else:
                                print("Wrong Input")
                        else:
                            print("Wrong Input")
                    else:
                        print("Wrong Input")
                elif no in v[0]:
                    print("Account No. Already In")
                else:
                    print("Wrong Input")
            elif i==2:
                acc=input("Enter Account Number To Be Deleted:")
                cursor.execute("select id from accounts;")
                lt=cursor.fetchall()
                connection.commit()
                if acc in lt[0]:
                    cursor.execute("delete from accounts where id="+acc+";")
                    connection.commit()    
                else:
                    print("ID Not Available")
            elif i==3:
                acc=input("Enter Account Number of Account To Be Changed:")
                cursor.execute("select id from accounts;")
                lt=cursor.fetchall()
                connection.commit()
                if acc in lt[0]:
                    print("Data:")
                    print("1.Name\n2.CVV\n3.PIN\n4.Expiry Month\n5.Expiry Year")
                    choice=int(input("Enter Data No.:"))
                    if choice==1:
                        y=input("Enter New Name:")
                        cursor.execute("update accounts set name=%s where id=%s;",y,acc)
                        connection.commit()
                    elif choice==2:
                        y=int(input("Enter New CVV:"))
                        cursor.execute("update accounts set CVV=%s where id=%s;",y,acc)
                        connection.commit()
                    elif choice==3:
                        y=int(input("Enter New PIN:"))
                        cursor.execute("update accounts set PIN=%s where id=%s;",y,acc)
                        connection.commit()
                    elif choice==4:
                        y=int(input("Enter New Expiry Month:"))
                        cursor.execute("update accounts set expmn=%s where id=%s;",y,acc)
                        connection.commit()
                    elif choice==5:
                        y=int(input("Enter New Expiry Year:"))
                        cursor.execute("update accounts set expyr=%s where id=%s;",y,acc)
                        connection.commit()
                    else:
                        print("Wrong Input")
                else:
                    print("Account Not Found")
            elif i==4:
                cursor.execute("select * from accounts;")
                lst=cursor.fetchall()
                for j in lst:
                    print(j)
            elif i==5:
                pass
            else:
                print("Wrong Input")
                            
        else:
            print("Access Denied")
    else:
        print("Wrong Input")
    exi=input("Do You Want To Exit The Portal?(Y/N):")
    if exi.upper()=="Y":
        break
print("Thank You")
