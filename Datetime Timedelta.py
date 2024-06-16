from datetime import datetime, timedelta

current_datetime = datetime.now()
print(f"Current Datetime: {current_datetime}")


# ABC = (5+2/24 +4/(24*60)+5/(60*60*24))
# new_datetime1 = current_datetime + timedelta(ABC)
# print(f"New Datetime 1::: {new_datetime1}")

# new_datetime2 = current_datetime + timedelta(days=5, hours=2, minutes=4, seconds=5)
# print(f"New Datetime2::: {new_datetime2}")

# current_time_3 = datetime.now().strftime('%Y-%m-%d' + ' %I %M' + ' %p')
# print(current_time_3)



datetime_format = '%Y-%m-%d' + ' %I %M' + ' %p' #this for show in my style good

duration_to_add = timedelta(days=2, hours=11)
new_datetime = current_datetime + duration_to_add
print(f"New Datetime: {new_datetime.strftime(datetime_format)}")


