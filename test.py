from datetime import time

# Create a time object
my_time = time(10, 30, 45)

# Format the time as "HH:MM:SS"
formatted_time = my_time.strftime("%H:%M:%S")
print("Formatted Time:", formatted_time)
