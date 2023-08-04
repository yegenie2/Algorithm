import datetime

now = datetime.datetime.now()
print(now.date() - datetime.timedelta(hours=9))