import datetime as dt
today = dt.date.today()
last_of_teens = dt.date(2019,12,31)
print(today)
print(last_of_teens.day)
print(last_of_teens.month)
print(last_of_teens.year)
print(f"{last_of_teens:%A, %B, %d, %Y}") #formatted to show weekday,month, day number and year with century
todays_date = f"{today:%d/%m/%Y}"        #format to display date as dd/mm/yyyy
print(todays_date)
midnight = dt.time()
almost_midnight = dt.time(23,59,59,999999)
print(midnight)
print(almost_midnight)
right_now = dt.datetime.now()
print(right_now)
new_years_day = dt.date(2019, 1, 1)
memorial_day = dt.date(2019, 5, 27)
days_between = memorial_day - new_years_day
print(days_between)
#working with timezones
here_now = dt.datetime.now()    #get time from computer clock
utc_now = dt.datetime.utcnow()  #get the utc time now
time_difference = (utc_now-here_now)    #subtract to see difference
print(f"My time : {here_now:%I:%M:%p}")
print(f"UTC time : {utc_now:%I:%M:%p}")
print(f"Difference: {time_difference}")

