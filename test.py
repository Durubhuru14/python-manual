import schedule
import time
from datetime import datetime

def job():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Task executed at: {current_time}")

# Schedule the job every minute
schedule.every(1).minutes.do(job)

print("Scheduler started. Press Ctrl+C to stop.")

try:
    while True:
        # Run the scheduled tasks
        schedule.run_pending()
        time.sleep(1)  # Sleep to prevent busy waiting
except KeyboardInterrupt:
    print("Scheduler stopped.")
