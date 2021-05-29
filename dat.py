from datetime import date, datetime, time, timedelta

dt_now = datetime.now()
delta = timedelta(days = 1)
delta_30 = timedelta(days = 30)
date_yesterday = dt_now - delta
date_30days = dt_now - delta_30

date_string = "01/01/25 12:10:03.234567" 
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

print(dt_now)
print(date_yesterday)
print(date_30days)
print(date_dt)