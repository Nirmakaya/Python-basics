import calendar
from datetime import datetime

today = datetime.now()

curr_year_num = today.strftime("%Y")
curr_month_num = today.strftime("%m")

last_date = (calendar.monthrange(int(curr_year_num),int(curr_month_num[1])))[1]
curr_day = int(today.strftime("%d"))
remaining_day = last_date-curr_day

num = round(400.4)
rum = abs(-300)
print(num)
print(rum)

print(remaining_day)


curr_month_full_str = today.strftime("%B")
curr_month_abr_str = today.strftime("%b")
curr_day = today.strftime("%d")

