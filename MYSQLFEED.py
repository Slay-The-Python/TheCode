import mysql.connector
import takepass

u=takepass.username()
p=takepass.password()

connection=mysql.connector.connect(host="localhost",username=u,password=p,database="feedback")
cursor=connection.cursor()

a=int(input("Enter No. of Inputs:"))
l=[]
r=("GOOD","MODERATE","NOT GOOD")

for i in range(a):
    n=input("Enter Name:")
    tmr=input("Enter Your _______________ From (Good, Moderate, Not Good):")
    tms=input("Enter Your______________________(Not More Than 100 Characters):")
    ur=input("Enter Your ___________________ From (Good, Moderate, Not Good):")
    us=input("Enter Your __________________(Not More Than 100 Characters):")
    ovr=input("Enter Your ________________ From (Good, Moderate, Not Good):")
    ovs=input("Enter Your __________________(Not More Than 200 Characters):")
    
    if tmr.upper() in r and ur.upper() in r and ovr.upper() in r and len(tms)<=100 and len(us)<=100 and len(ovs)<=200:
        tupl=(n,tmr.title(),tms,ur.title(),us,ovr.title(),ovs)
        l.append(tupl)

query="insert into feedback1(name,tmr,tms,ur,us,ovr,ovs) values(%s,%s,%s,%s,%s,%s,%s)"
cursor.executemany(query,l)
connection.commit()
