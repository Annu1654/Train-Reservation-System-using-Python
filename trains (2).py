import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1905",database="train")
mycursor = mydb.cursor()
mycursor.execute("create table if not exists trains(No varchar(10) primary key, Name varchar(100), Source varchar (50), Destination varchar(50), 2S varchar(10), SL varchar(10), AC varchar(10), Deparature varchar(20), Arrival varchar(20))")
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12019,'Shatabdi Express','Howrah','Ranchi',1170,1780,2000,'06:05','13:15')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12130,'Azad Hind Express','Howrah','Pune',1120,1865,2690,'07:20','22:10')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12277,'Shatabdi Express','Howrah','Puri',1070,1120,1860,'14:15','21:50')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12860,'Gitanjali Express','Howrah','Mumbai',1740,1840,2655,'14:05','21:20')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12839,'Chennai Mail Express','Howrah','Chennai',1630,2520,4185,'03:15','23:55')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(20822,'Pune Humsafar Express','Howrah','Pune',400,750,2000,'02:45','19:25')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12129,'Azad Hind Express','Pune','Howrah',1120,1865,2690,'01:45','18:35')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(20821,'Pune Humsafar Express','Pune','Howrah',400,750,2000,'10:40','23:25')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(22201,'Duronto Express','Kharagpur','Puri',240,400,1085,'03:55','22:15')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(22202,'Duronto Express','Puri','Howrah',330,630,1585,'03:55','12:15')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12837,'HWH PURI SF Express','Howrah','Puri',145,645,960,'00:18','08:15')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(18409,'Jagannath Express','Howrah','Puri',165,295,980,'04:30','20:55')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12887,'SHM Puri SF Express','Kharagpur','Puri',145,275,705,'05:10','22:30')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12821,'Dhahuli Express','Kharagpur','Puri',145,210,375,'10:55','18:00')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12278,'Shatabdi Express','Puri','Kharagpur',465,935,1450,'05:45','11:37')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12838,'PURI HWH SF Express','Puri','Howrah',145,645,960,'02:15','20:15')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(15643,'PURI KYQ Express','Kharagpur','Puri',150,245,660,'04:30','11:10')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12882,'Garib Rath Express','Puri','Howrah',200,350,600,'06:10','13:50')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(18410,'Jagannath Express','Puri','Howrah',165,295,980,'08:10','17:20')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12665,'HWH Cape SF Express','Howrah','Chennai',635,1665,2390,'16:15','21:38')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12663,'HWH TPJ SUF Express','Howrah','Chennai',700,1840,2580,'17:40','21:38')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12840,'MAS HWH Mail Express','Chennai','Howrah',635,1665,2390,'16:15','21:38')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12842,'Coromandal Express','Chennai','Howrah',323,635,1650,'06:15','19:10')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12664,'TPJ HWH EXP','Chennai','Howrah',700,1840,2580,'18:10','23:55')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12301,'Rajdhani Express','Howrah','New Delhi',2770,3775,4710,'10:50','21:50')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12303,'Poorva Express','Howrah','New Delhi',405,600,1570,'08:50','19:50')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12302,'Rajdhani Express','New Delhi','Howrah',2770,3775,4710,'16:50','09:55')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12304,'Poorva Express','New Delhi','Howrah',405,600,1570,'17:40','17:00')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12273,'NDLS Duronto Express','Howrah','New Delhi',610,1265,3035,'08:35','06:35')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12274,'HWH Duronto Express','New Delhi','Howrah',675,1375,3320,'12:40','10:35')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(18615,'Kriya Yoga Express','Howrah','Ranchi',135,255,695,'21:30','05:30')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(18627,'Intercity Express','Howrah','Ranchi',160,570,705,'12:50','22:15')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12020,'Shatabdi Express','Ranchi','Howrah',1170,1780,2000,'13:45','21:30')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(18628,'Intercity Express','Ranchi','Howrah',160,570,705,'05:40','15:10')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(18616,'Kriya Yoga Express','Ranchi','Howrah',135,255,695,'22:15','06:30')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12810,'Howrah CSMT Mail Express','Howrah','Mumbai',345,705,1840,'19:50','04:25')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12321,'Mumbai Mail Express','Howrah','Mumbai',435,820,2130,'23:35','13:15')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12261,'Howrah Duronto Express','Mumbai','Howrah',3530,4820,6070,'00:15','23:50')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12859,'Gitanjali Express','Mumbai','Howrah',475,705,1840,'06:05','03:30')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12322,'Kolkata Mail Express','Mumbai','Howrah',500,740,1925,'22:15','17:40')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12314,'Sealdah Rajdhani Express','New Delhi','Sealdah',2785,3805,4760,'16:30','10:10')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12987,'SDAH AII SF Express','Sealdah','Ajmer',690,1805,2595,'22:55','19:35')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12988,'AII SDAH SF Express','Ajmer','Sealdah',625,1635,2350,'12:45','23:50')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12259,'BKN Duronto Express','Sealdah','New Delhi',3030,4170,5210,'17:00','11:00')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12379,'Jalianwala B Express','Sealdah','Delhi',635,1665,2385,'13:10','09:05')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12329,'Sampark K Express','Anand Vihar','Sealdah',635,1665,2385,'13:10','08:40')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(22317,'Humsafar Express','Jammu Tawi','Sealdah',630,1600,2305,'13:10','23:10')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12330,'Sampark K Express','Sealdah','Anand Vihar',635,1665,2385,'20:20','16:35')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(22318,'SDAH Humsafar Express','Sealdah','Jammu Tawi',630,1600,2305,'07:20','17:30')
mycursor.execute(sql,val)
mydb.commit()
sql="insert into trains(No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(12380,'Jalianwala B Express','Amritsar','Sealdah',635,1665,2385,'13:25','03:45')
mycursor.execute(sql,val)
mydb.commit()
from tabulate import tabulate
sql="select No,Name,Source,Destination,2S,SL,AC,Deparature,Arrival from trains"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(tabulate(myresult, headers=['Train No.', 'Train Name', 'From', 'To', '2S', 'SL', 'AC' 'Deparature', 'Arrival'], tablefmt='psql'))