import time
import datetime
import pytz
from dateutil import parser

# date1 = parser.parse('2019-08-01')
# date2 = parser.parse('2019-08-20')
# diff = date2 - date1
#
# print(diff)
# print(diff.days)

# time.ctime(seconds) convert a time expressed in a seconds since epoch to a readable string
#t = time.ctime(60)

# time.time() return current seconds since epoch
# t = time.time()
# now = time.ctime(time.time())

# format a time string
# t = time.localtime()
# now = time.strftime('%H:%M:%S', t)
# print(now)

# format a time to your own format string
# t = time.strptime('20 May, 2022', '%d %B, %Y')
# print(t)

# convert a time object to a readable string
# time_tuple = (2020, 4, 20, 5, 43, 0, 3, 0, 0) # 9 items
# t = time.asctime(time_tuple)
# time.mktime(time_tuple) # format time since epoch time

#print(t)
#print(now)

# create a date
# d = datetime.date(2022, 6, 1)
# print(d)

tday = datetime.date.today()
print(tday)
# print(tday.weekday()) # monday = 0 sunday = 6
# print(tday.isoweekday()) # monday = 1 sunday = 7

# t = datetime.timedelta(days=5) # a date label to + or -
# tday = datetime.date.today()
# bday = datetime.date(2023, 5, 8)
# till_bday = bday - tday
# # print(tday-t)
# # print(till_bday.days)
# a_day = datetime.date(2022, 12, 1)
# b_day = datetime.date(2022, 12, 3)
# print((b_day-a_day).days)

# print(till_bday.total_seconds())

# create a time
#t = datetime.time(9, 50, 23, 10000)
# t = datetime.datetime(2022, 10, 5, 9, 34, 30, 100000)
# print(t)
# print(t.year)
# print(t.date())
# print(t.time())

# today = datetime.datetime.today()
# now = datetime.datetime.now() # can pass a timezone argument
# uctnow = datetime.datetime.utcnow()
# print(today)
# print(now)
# print(uctnow)

# dt = datetime.datetime(2022, 8, 4, 12, 33, 45, tzinfo=pytz.UTC)
# dt_now = datetime.datetime.now(tz=pytz.UTC)
# dt_tz = dt_now.astimezone(pytz.timezone('Asia/Tokyo'))
# for tz in pytz.all_timezones:
#     print(tz)
# print(dt)
# print(dt_now)
# print(dt_tz)

# to localize timezone
# dt_local = datetime.datetime.now() # naive time(no timezone time)
# local_tz = pytz.timezone('Asia/Tokyo')
# dt_local = local_tz.localize(dt_local)
# dt_east = dt_local.astimezone(pytz.timezone('Asia/Shanghai'))
# print(dt_east)

# strftime - Datetime tp string
# now = datetime.datetime.now(tz=pytz.timezone('Universal'))
# print(now.strftime('%d/%m/%Y'))

# strptime - String to datetime
# now = datetime.datetime.now(tz=pytz.timezone('Universal'))
# string = 'August 5, 2022'
# dt = datetime.datetime.strptime(string, '%B %d, %Y')
# print(dt)

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# a = mylist[-1:]
# b = mylist[:-1]
#
# mylist = a + b
# print(a)
# print(b)
# print(mylist)

# for i in range(1, 5, 1):
#     print(i)

# t=datetime.datetime.now()
# print(t.date())
# print(t.hour)
# print(t.minute)

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)
