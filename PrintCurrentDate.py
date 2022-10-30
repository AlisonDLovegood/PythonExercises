import datetime

now = datetime.datetime.now()

s1 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("now: ", s1)
