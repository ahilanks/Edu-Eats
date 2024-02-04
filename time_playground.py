from datetime import datetime


# now = datetime.now()


# current_hour = int(now.strftime("%H"))

# meal_period = ''

# if (current_hour>=0 and current_hour<=10):
#     meal_period = 'B'
# elif (current_hour>10 and current_hour<=15):
#     meal_period = 'L'
# elif (current_hour>15 and current_hour<=21):
#     meal_period = 'D'


# print(meal_period)

today = datetime.today()

weekday = today.weekday()

print(weekday)