from datetime import datetime

mytime = datetime(2021,10,3,14,20,1)
print(mytime)
print(mytime.replace(year=2020))

from datetime import date
date1 = date(2021,11,3)
date2 = date(2022,11,3)

print(date1 - date2)
