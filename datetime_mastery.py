import datetime
import pytz

# --- PART 1: Creating Specific Dates ---
date_y = datetime.datetime(2023, 12, 25, 10, 30, 59)
print(f"Full Date: {date_y}")
print(f"Year: {date_y.year}, Month: {date_y.month}, Day: {date_y.day}")

# --- PART 2: Timedelta (Time Arithmetic) ---
# Adding 7 days and 12 hours to current time
date_now = datetime.datetime.now()
delta_days = datetime.timedelta(days=7)
delta_hours = datetime.timedelta(hours=12)

print(f"Current Time: {date_now}")
print(f"7 Days from now: {date_now + delta_days}")
print(f"12 Hours from now: {date_now + delta_hours}")

# --- PART 3: Timezones (UTC & Paris) ---
# Working with UTC and specific timezones using pytz
date_utc = datetime.datetime.now(tz=pytz.UTC)
date_paris = datetime.datetime.now(tz=pytz.timezone("Europe/Paris"))
print(f"UTC Time: {date_utc}")
print(f"Paris Time: {date_paris}")

# --- PART 4: Formatting (strftime & strptime) ---
# strftime: Formatting date to string
print(f"Day Name: {date_paris.strftime('%A')}") # Full day name
print(f"Formatted: {date_paris.strftime('%B, %d, %Y')}") # January, 28, 2026

# strptime: Converting string back to date object
date_str = 'January 04 2026'
date_obj = datetime.datetime.strptime(date_str, '%B %d %Y')
print(f"Converted from string: {date_obj}")
