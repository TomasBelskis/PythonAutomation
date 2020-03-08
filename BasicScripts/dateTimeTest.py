# Testing time
# "event_date": "1566549041",
import time
import datetime

alert_trigger_time = 1566549041
alert_date = datetime.datetime.fromtimestamp(alert_trigger_time).date()

christmas_eve = datetime.datetime(2019, 12, 24)
chritmas_day = datetime.datetime(2019, 12, 25)
chritmas_day_2 = datetime.datetime(2019, 12, 26)
new_years_day = datetime.datetime(2020, 1, 1)

print (alert_date)
if alert_date == christmas_day.date():
    print ("It's christmas day yay!")
else:
    print (christmas_day.date())
    print ("I didn't not work")
