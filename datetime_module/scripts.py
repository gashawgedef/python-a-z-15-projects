import datetime
# dt =datetime.datetime.now()
# date_today =datetime.date.today()
# dt1 = datetime.date(2024,6,26)
# dt2 = datetime.timedelta(40)
# print(dt1+dt2)
# print(date_today)
dt1 = datetime.date.today()
print("Current Year:", dt1.year)
print("Current Month:", dt1.month)
print("Current Day:", dt1.day)
print(dt1.strftime("%A ,%B %d, %Y"))


