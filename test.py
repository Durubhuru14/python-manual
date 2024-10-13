from datetime import datetime

# Function to log data with a timestamp
def log_data_entry(entry):
    # Fetch current date and time
    timestamp = datetime.now()
    
    # Format the log message
    log_message = f"{timestamp}: {entry}"
    return log_message

# Log an example data entry
log_entry = log_data_entry("User logged in successfully.")
print(log_entry)
