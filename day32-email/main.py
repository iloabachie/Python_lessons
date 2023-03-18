import smtplib

my_gmail = 'ezue.python@gmail.com'
my_ymail = 'ezue.python@yahoo.com'
password = 'n3^wwa6*V#i23!'

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()  # makes connection secure
connection.login(user=my_gmail, password=password)
connection.sendmail(from_addr=my_gmail, to_addrs='udemezue@gmail.com', msg='testing this')
connection.close()

# This closes the connection immediately no need for close syntax
with smtplib.SMTP('smtp.mail.yahoo.com') as connection2:
    connection2.starttls()
    connection2.login(user=my_ymail, password=password)
    connection2.sendmail(from_addr=my_ymail, to_addrs='udemezue@gmail.com', msg='Subject: Hello\n\ntesting this')
    

import datetime as dt

now = dt.datetime.now()

year = now.year
month = now.month
day_of_week = now.weekday()

# in day of week, 0 = Monday
print(now, year)

#to create my own date time

date_of_birth = dt.datetime(year=1984, month=3, day=15)
print(date_of_birth)
