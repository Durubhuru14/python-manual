from datetime import datetime
import pytz

# Create a timezone-aware datetime object
utc_zone = pytz.utc
utc_datetime = datetime.now(utc_zone)

# Convert UTC time to a different time zone (e.g., US/Eastern)
eastern_zone = pytz.timezone('US/Eastern')
eastern_datetime = utc_datetime.astimezone(eastern_zone)

print("UTC Datetime:", utc_datetime)
print("Eastern Datetime:", eastern_datetime)
