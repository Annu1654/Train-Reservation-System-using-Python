status=" "

import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="1905")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists train")

mydb=mysql.connector.connect(host="localhost",user="root",passwd="1905",database="train")
mycursor = mydb.cursor()
mycursor.execute("create table if not exists accounts(Mobile varchar(15), Email varchar(100), Username varchar(20),Password varchar(20), Name varchar(50), DOB varchar(20), Gender varchar(20), Nationality varchar(50), Address varchar(100), PIN varchar (10))")
mycursor.execute("create table if not exists trains(No varchar(10),Name varchar(100), Source varchar (50), Destination varchar(50), 2S varchar(10), SL varchar(10), AC varchar(10), Deparature varchar(20), Arrival varchar(20))")
mycursor.execute("create table if not exists tickets(Name varchar(100),Age varchar(10), Gender varchar(50),Nationality varchar(50),Fare varchar(20),TransId varchar(50),PNR varchar(50),Train varchar(100),No varchar(10),Date varchar(20),Deparature varchar(20),Arrival varchar(20),Source varchar(50),Destination varchar(50),Passengers varchar(10),Class varchar(10),Berth varchar(10),Mode varchar(50),TransDate varchar(100),TransTime varchar(100))")
mycursor.execute("create table if not exists cancels(Train varchar(100), No varchar(10), TransId varchar(50), TransDate varchar(100),Source varchar(50),Destination varchar(50), CancelDate varchar(100),PNR varchar(50),CancelId varchar(50),Refund varchar(20),Deducted varchar(20))")

def displayMenu():
    print("\n")
    print('*'*13)
    print("SYSTEM LOGIN")
    print('*'*13)
    print("\n1. REGISTER USER\n","\n2. SIGN IN")
    st=int(input("\nSELECT: "))
    if st ==1:
        newUser()
    elif st ==2:
        oldUser()

def Main():
    print("\n")
    print('*'*28)
    print("TRAIN TICKET BOOKING SYSTEM")
    print('*'*28)
    print("\n1. BOOK TICKET\n","\n2. MY BOOKINGS\n","\n3. PNR ENQUIRY\n", "\n4. LAST TRANSACTIONS\n", "\n5. CANCEL TICKET\n", "\n6. REFUND HISTORY\n", "\n7. TRAIN SCHEDULE\n","\n8. LOG OUT")
    s=int(input("\nSELECT OPTION: " ))
    if s==1:
        book_ticket()
    elif s==2:
        my_bookings()
    elif s==3:
        pnr_enquiry()
    elif s==4:
        last_transactions()        
    elif s==5:
        cancel_ticket()
    elif s==6:
        refund_history()
    elif s==7:
        train_schedule()
    elif s==8:
        log_out()
    else:
        print("\nINCORRECT OPTION\n")

def book_ticket():
    print("\n")
    print('*'*11)
    print("BOOK TICKET")
    print('*'*11)
    import mysql.connector
    from tabulate import tabulate
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1905",database="train")
    mycursor=mydb.cursor()
    fr=input("\nFROM: ")
    to=input("\nTO: ")
    print("\nD.O.J.:")
    date1=input("DD: ")
    date2=input("MM: ")
    date3=input("YYYY: ")
    c={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
    m=c[date2]
    dt=str(date1) + " " + m + "," + str(date3)
    print("\n")
    tup1=tuple(map(str,fr.split(',')))
    tup2=tuple(map(str,to.split(',')))
    tup=tup1+tup2
    sql="select * from trains where Source=%s and Destination=%s"
    mycursor.execute(sql,tup)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['Train No.', 'Train Name', 'From', 'To', '2S', 'SL', 'AC', 'Deparature','Arrival'], tablefmt='psql'))
    trno=input("\nENTER TRAIN NO: ")
    tup3=tuple(map(str,trno.split(',')))
    s="select Name from trains where No=%s"
    mycursor.execute(s,tup3)
    tr = mycursor.fetchall()
    l=tr[0]
    print("\nTRAIN NAME:",l[0])
    nam=input("\nNAME: ")
    age=input("\nAGE: ")
    print("\nGENDER: M for MALE | F for FEMALE | T for TRANSGENDER")
    gender=input("\nGENDER: ")
    gen=gender.upper()
    a={'M':'MALE','F':'FEMALE','T':'TRANS'}
    v=a[gen]
    nat=input("\nNATIONALITY: ")
    print("\nBERTH PREFERENCE: LB for LOWER | MB for MIDDLE | UB for UPPER | SL for SIDE LOWER | SU for SIDE UPPER")
    ber=input("\nSELECT: ")
    print("\nCLASS: 1 for 2S | 2 for SL | 3 for AC")
    cl=int(input("\nSELECT: "))
    tc=int(input("\nNO. OF TICKETS: "))
    if cl==1:
        p="select 2S from trains where No=%s"
        mycursor.execute(p,tup3)
        r = mycursor.fetchall()
        lt=r[0]
        am=int(lt[0])*tc
        cl="2S"
    elif cl==2:
        p="select SL from trains where No=%s"
        mycursor.execute(p,tup3)
        r = mycursor.fetchall()
        lt=r[0]
        am=int(lt[0])*tc
        cl="SL"
    elif cl==3:
        p="select AC from trains where No=%s"
        mycursor.execute(p,tup3)
        r = mycursor.fetchall()
        lt=r[0]
        am=int(lt[0])*tc
        cl="AC"
    fd=input("\nDo you want meal(₹ 500 each)? (yes/no): " )
    if fd=="yes":
        a=500*tc
        a=a+am
        ta=a+11.80
        print("\nPAYMENT DETAILS")
        print("BASE FARE: ₹",a)
        print("CONVENIENCE FEE: ₹ 11.80:")
        print("\nTOTAL FARE: ₹",ta)
    elif fd=="no":
        a=am
        ta=a+11.80
        print("\nPAYMENT DETAILS")
        print("BASE FARE: ₹",a)
        print("CONVENIENCE FEE: ₹ 11.80:")
        print("\nTOTAL FARE: ₹",ta)
    print("\nPAYMENT MODE:", "\n1. CARDS/NET BANKING", "\n2. BHIM/UPI")
    ch=input("\nSELECT: " )
    j={'1':'CARDS/NET BANKING','2':'BHIM/UPI'}
    k=j[ch]
    import random
    msg=""
    m="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&+"
    for i in range(6):
        msg=msg+m[random.randint(0,69)]
    print('\n',msg)
    captcha=input("Enter Captcha: ")
    if captcha==msg:
        print("₹",ta,"PAID SUCCESSFULLY BY",k)
    else:
        print("\nWrong Captcha")
    import random
    ti=str(random.randint(1000000000,9999999999))+str(random.randint(10000,99999))
    pnr=random.randint(1000000000,9999999999)
    from datetime import datetime
    today=datetime.today()
    day=today.day
    mon=str(today.month)
    year=today.year
    b={'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'May','6':'Jun','7':'Jul','8':'Aug','9':'Sep','10':'Oct','11':'Nov','12':'Dec'}
    d=b[mon]
    dt_now=str(day) + " " + d + "," + str(year)
    hr=today.hour
    mn=today.minute
    tm=str(hr) + ":" + str(mn)
    e="select Deparature,Arrival,Source,Destination from trains where No=%s"
    mycursor.execute(e,tup3)
    rs = mycursor.fetchall()
    lt=rs[0]
    sql="insert into tickets(Name,Age,Gender,Nationality,Fare,TransId,PNR,Train,No,Date,Deparature,Arrival,Source,Destination,Passengers,Class,Berth,Mode,TransDate,TransTime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(nam,age,v,nat,ta,ti,pnr,l[0],trno,dt,lt[0],lt[1],lt[2],lt[3],tc,cl,ber,k,dt_now,tm)
    mycursor.execute(sql,val)
    mydb.commit()
    print("\n")
    print('*'*6)
    print("TICKET")
    print('*'*6)
    print("TRANSACTION ID:",ti)
    print("Thank You",nam)
    print(l[0],'(',trno,')','       ',"PNR:",pnr)
    print("Deparature:",lt[0],'                 ',"Arrival:",lt[1])
    print("Source:",lt[2],'               ',"Destination:",lt[3])
    print(tc,"Adult 0 Child|",cl,"|GENERAL|",lt[2],"|",dt)
    print("TICKET STATUS: CONFIRMED")
    print("Coach: B3    Berth: 7    Berth Type:",ber,"\n")
    cont=input("\nDo you want to continue? (yes/no): " )
    if cont=="yes":
        Main()
    elif cont=="no":
        log_out()
    
def my_bookings():
    print("\n")
    print('*'*11)
    print("MY BOOKINGS")
    print('*'*11)
    import mysql.connector
    from tabulate import tabulate
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1905",database="train")
    mycursor = mydb.cursor()
    sql="select No,Train,Source,Destination,Passengers,Date,Deparature,Arrival,PNR from tickets"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if not myresult:
        print("\nNO BOOKINGS")
        cont=input("\nDo you want to continue? (yes/no): " )
        if cont=="yes":
            Main()
        elif cont=="no":
            log_out()
    else:
        print(tabulate(myresult, headers=['Train No.', 'Train Name', 'From', 'To', 'Passengers', 'Date', 'Deparature', 'Arrival', 'PNR'], tablefmt='psql'))
        cont=input("\nDo you want to continue? (yes/no): " )
        if cont=="yes":
            Main()
        elif cont=="no":
            log_out()
        
def pnr_enquiry():
    print("\n")
    print('*'*11)
    print("PNR ENQUIRY")
    print('*'*11)
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1905",database="train")
    mycursor = mydb.cursor()
    pnr=input("\nSEARCH PNR: ")
    tup=tuple(map(str,pnr.split(',')))
    sql="select No,Train,PNR,Date,Source,Destination,Passengers,Class,Fare,Berth from tickets where PNR=%s"
    mycursor.execute(sql,tup)
    rs = mycursor.fetchall()
    lt=rs[0]
    print(lt[1],'(',lt[0],')','     ',"PNR:",lt[2])
    print("Date:",lt[3])
    print("Source:",lt[4],'                ',"Destination:",lt[5])
    print(lt[6],"Adult 0 Child|",lt[7],"|GENERAL|",lt[4],"|",lt[3])
    print("BOOKING STATUS: CONFIRMED")
    print("TICKET FARE: ₹",lt[8])
    print("Charting Status: Chart Prepared")
    print("Coach: B3    Berth: 7    Berth Type:",lt[9],"\n")
    cont=input("\nDo you want to continue? (yes/no): " )
    if cont=="yes":
        Main()
    elif cont=="no":
        log_out()
    
def last_transactions():
    print("\n")
    print('*'*16)
    print("LAST TRANSACTION")
    print('*'*16)
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1905",database="train")
    mycursor = mydb.cursor()
    sql="select Train,No,TransID,TransDate,Source,Destination,Date,Fare from tickets"
    mycursor.execute(sql)
    rs = mycursor.fetchall()
    m=mycursor.rowcount
    n=m-1
    if not rs:
        print("\nNO BOOKINGS")
        cont=input("\nDo you want to continue? (yes/no): " )
        if cont=="yes":
            Main()
        elif cont=="no":
            log_out()
    else:
        lt=rs[n]
        print(lt[0],'      ',"Transaction Id: ",lt[2])
        print('(',lt[1],')','               ',"Transaction Date: ",lt[3])
        print(lt[4],'→',lt[5])
        print(lt[6],'                             ',"STATUS: BOOKED")
        print("Payment Status:")
        print("Amount deducted: ₹",lt[7])
        print("Bank Name: Credit & Debit cards/UPI(Powered by RazorPay)")
        cont=input("\nDo you want to continue? (yes/no): " )
        if cont=="yes":
            Main()
        elif cont=="no":
            log_out()
    
def cancel_ticket():
    print("\n")
    print('*'*13)
    print("CANCEL TICKET")
    print('*'*13)
    import mysql.connector
    from tabulate import tabulate
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1905",database="train")
    mycursor = mydb.cursor()
    sql="select No,Train,Source,Destination,Name,Fare,Date,Deparature,Arrival,PNR from tickets"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if not myresult:
        print("\nNO BOOKINGS")
        cont=input("\nDo you want to continue? (yes/no): " )
        if cont=="yes":
            Main()
        elif cont=="no":
            log_out()
    else:
        print(tabulate(myresult, headers=['Train No.', 'Train Name', 'From', 'To', 'Name' , 'Fare' , 'Date', 'Deparature', 'Arrival', 'PNR'], tablefmt='psql'))
        pnr=input("\nSEARCH PNR: ")
        tup=tuple(map(str,pnr.split(',')))
        sql="select No,Train,PNR,Date,Source,Destination,Passengers,Class,Fare,Berth,TransId,TransDate from tickets where PNR=%s"
        mycursor.execute(sql,tup)
        rs = mycursor.fetchall()
        lt=rs[0]
        print(lt[1],'(',lt[0],')','     ',"PNR:",lt[2])
        print("Date:",lt[3])
        print("Source:",lt[4],'                ',"Destination:",lt[5])
        print(lt[6],"Adult 0 Child|",lt[7],"|GENERAL|",lt[4],"|",lt[3])
        print("BOOKING STATUS: CONFIRMED")
        print("TICKET FARE: ₹",lt[8])
        print("Charting Status: Chart Prepared")
        print("Coach: B3    Berth: 7    Berth Type:",lt[9],"\n")
        c=input("CANCEL? (yes/no): ")
        if c=="yes":
            print("Cancelling Ticket.....")
            ded=(2*float(lt[8]))//100
            ref=float(lt[8])-ded
            print("Refund Amount: ₹",ref)
            import random
            ci=str(random.randint(1000000000,9999999999))+str(random.randint(10000,99999))
            from datetime import datetime
            today=datetime.today()
            day=today.day
            mon=str(today.month)
            year=today.year
            b={'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'May','6':'Jun','7':'Jul','8':'Aug','9':'Sep','10':'Oct','11':'Nov','12':'Dec'}
            d=b[mon]
            dt_now=str(day) + " " + d + "," + str(year)
            sql="insert into cancels(Train,No,TransId,TransDate,Source,Destination,CancelDate,PNR,CancelId,Refund,Deducted) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(lt[1],lt[0],lt[10],lt[11],lt[4],lt[5],dt_now,lt[2],ci,ref,ded)
            mycursor.execute(sql,val)
            mydb.commit()
            s="delete from tickets where PNR=pnr"
            mycursor.execute(s)
            mydb.commit()
            cont=input("\nDo you want to continue? (yes/no): " )
            if cont=="yes":
                Main()
            elif cont=="no":
                log_out()
        elif c=="no":
            cont=input("\nDo you want to continue? (yes/no): " )
            if cont=="yes":
                Main()
            elif cont=="no":
                log_out()
        
def refund_history():
    print("\n")
    print('*'*14)
    print("REFUND HISTORY")
    print('*'*14)
    import mysql.connector
    from tabulate import tabulate
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1905",database="train")
    mycursor = mydb.cursor()
    sql="select Train,No,TransId,TransDate,Source,Destination,CancelDate from cancels"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if not myresult:
        print("\nNO BOOKINGS")
        cont=input("\nDo you want to continue? (yes/no): " )
        if cont=="yes":
            Main()
        elif cont=="no":
            log_out()
    else:
        print(tabulate(myresult, headers=['Train Name', 'Train No.', 'Transaction Id','Transaction Date','From', 'To', 'Cancel Date'], tablefmt='psql'))
        no=input("\nTRAIN NO.: ")
        tup=tuple(map(str,no.split(',')))
        sql="select Train,No,TransId,TransDate,Source,Destination,CancelDate,PNR,CancelId,Deducted,Refund from cancels where No=%s"
        mycursor.execute(sql,tup)
        rs = mycursor.fetchall()
        lt=rs[0]
        print(lt[0],'          ',"Transaction Id: ",lt[2])
        print('(',lt[1],')','                     ',"Transaction Date: ",lt[3])
        print(lt[4],'→',lt[5])
        print(lt[6],'                                ',"STATUS: CANCELLED")
        print("PNR: ",lt[7],'   ',"CANCELLATION/REFUND ID: ",lt[8])
        print("Refund Status: REFUNDED")
        print("Refund Detail: Amount Credited To Bank With Reference No. rfnd_F2sP73q81TGHUT")
        print("Amount deducted: ₹",lt[9],'           ',"Refunded Amount: ₹",lt[10])
        print("Bank Name: Credit & Debit cards/Net Banking/UPI(Powered by Paytm)")
        cont=input("\nDo you want to continue? (yes/no): " )
        if cont=="yes":
            Main()
        elif cont=="no":
            log_out()

def train_schedule():
    print("\n")
    print('*'*14)
    print("TRAIN SCHEDULE")
    print('*'*14)
    import mysql.connector
    from tabulate import tabulate
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="1905",database="train")
    mycursor = mydb.cursor()
    sql="select No,Name,Source,Destination,Deparature,Arrival from trains"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=['Train No.', 'Train Name', 'From', 'To', 'Deparature', 'Arrival'], tablefmt='psql'))
    cont=input("\nDo you want to continue? (yes/no): " )
    if cont=="yes":
        Main()
    elif cont=="no":
        log_out()
        
def log_out():
    print("\n*****THANK YOU:::::VISIT AGAIN*****\n")
    displayMenu()
    
def newUser():
    print('\n')
    print('*'*17)
    print("USER REGISTRATION")
    print('*'*17)
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1905",database="train")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from accounts")
    col=mycursor.fetchall()
    x=col[0]
    mob=input("\nMOBILE NUMBER: ")
    em=input("\nE-MAIL: ")
    user=input("\nCREATE USERNAME: ")
    mycursor.execute("select Username from accounts")
    users=mycursor.fetchall()
    y=()
    for i in range(x[0]):
        y=y+users[i]
    if user in y:
        print("\nUSERNAME IS UNAVAILABLE\n")
    else:
        createPasswd=input("\nCREATE PASSWORD: ")
        confirmrPasswd=input("\nCONFIRM PASSWORD: ")
        if createPasswd==confirmrPasswd:
            nam=input("\nNAME: ")
            print("\nD.O.B.:")
            date1=input("DD: ")
            date2=input("MM: ")
            date3=input("YYYY: ")
            date=date1+"/"+date2+"/"+date3
            gender=input("\nGENDER (M/F/T): ")
            gen=gender.upper()
            a={'M':'MALE','F':'FEMALE','T':'TRANS'}
            v=a[gen]
            nat=input("\nNATIONALITY: ")
            add=input("\nRESIDENCE ADDRESS: ")
            print('\n')
            print('*'*12)
            print("GENERATE PIN")
            print('*'*12)
            createPin=input("\nCREATE 4-DIGIT PIN: ")
            if len(createPin)==4:
                confirmPin=input("\nCONFIRM PIN: ")
                if createPin==confirmPin:
                    sql="insert into accounts(Mobile,Email,Username,Password,Name,DOB,Gender,Nationality,Address,PIN) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val=(mob,em,user,createPasswd,nam,date,v,nat,add,createPin)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    print("\nACCOUNT CREATED SUCCESSFULLY\n")
                else:
                    print("\nPIN DIDN'T MATCHED\n")
            else:
                print("\nPIN should be of 4 digit")
        else:
            print("\nPASSWORD DIDN'T MATCHED\n")
    oldUser()
                
def oldUser():
    print('\n')
    print('*'*7)
    print("SIGN IN")
    print('*'*7)
    print("\nLOGIN VIA","\n1. USERNAME","\n2. 4-DIGIT PIN")
    s=int(input("\nSELECT OPTION: " ))
    if s==1:
        username()    
    elif s==2:
        pin()
    else:
        print("\nINCORRECT OPTION\n")
        oldUser()
        
def username():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1905",database="train")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from accounts")
    col=mycursor.fetchall()
    x=col[0]
    mycursor.execute("select Username from accounts")
    users=mycursor.fetchall()
    t=()
    for i in range(x[0]):
        t=t+users[i]
    mycursor.execute("select Password from accounts")
    passw=mycursor.fetchall()
    l=()
    for j in range(x[0]):
        l=l+passw[j]
    login=input("\nUSERNAME: ")
    passwd=input("\nPASSWORD: ")
    if login in t and passwd in l:
        import random
        msg=""
        m="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&+"
        for i in range(6):
            msg=msg+m[random.randint(0,69)]
        print('\n',msg)
        captcha=input("Enter Captcha: ")
        tup=tuple(map(str,login.split(',')))
        if captcha==msg:
            sql="select Name from accounts where Username=%s"
            mycursor.execute(sql,tup)
            name=mycursor.fetchall()
            n=name[0]
            print("\nWELCOME",n[0])
            Main()
        else:
                print("\nWrong Captcha\n")
    else:
        print("\nUser doesn't exist or Wrong password\n")    
        
def pin():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1905",database="train")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from accounts")
    col=mycursor.fetchall()
    x=col[0]
    mycursor.execute("select PIN from accounts")
    users=mycursor.fetchall()
    z=()
    for i in range(x[0]):
        z=z+users[i]
    pin=input("\nEnter PIN: ")
    import random
    msg=""
    m="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&+"
    for i in range(6):
        msg=msg+m[random.randint(0,69)]
    print('\n',msg)
    captcha=input("Enter Captcha: ")
    tup=tuple(map(str,pin.split(',')))
    if pin in z and captcha==msg:
        sql="select Name from accounts where PIN=%s"
        mycursor.execute(sql,tup)
        name=mycursor.fetchall()
        n=name[0]
        print("\nWELCOME",n[0])
        Main()
    else:
        print("\nIncorrect PIN or Captcha\n")
        
while status!=0:
    displayMenu()