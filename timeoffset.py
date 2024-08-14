import os
from datetime import datetime, timedelta

# Function to adjust the file date
def adjust_file_date(file_path, delta):
    # Get the current creation time
    creation_time = os.path.getmtime(file_path)
    print(f"Found creation time {creation_time} for {file_path}")
    # Convert to datetime object
    creation_date = datetime.fromtimestamp(creation_time)
    print(f"Found creation time {creation_date} for {file_path}")
    # Apply the offset
    new_creation_date = creation_date + delta

    # Set the new creation date
    new_creation_time = new_creation_date.timestamp()
    new_creation_time_date = datetime.fromtimestamp(new_creation_time)
    print(f"Would adjust offset to {new_creation_time_date}")
    os.utime(file_path, (new_creation_time, new_creation_time))

# Directory containing the .360 files
directory = 'D:\Temp'

actual_time = datetime(2024, 8, 4, 11, 20)
incorrect_time = datetime(2016, 3, 17, 21, 50)

# Calculate the timedelta
offset = actual_time - incorrect_time

# Process each .360 file
for filename in os.listdir(directory):
    if filename.endswith(".360"):
        file_path = os.path.join(directory, filename)
        adjust_file_date(file_path, offset)
        print(f"Adjusted {filename} to new date and time.")

print("All files adjusted.")
