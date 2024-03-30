import re
from datetime import datetime
 
line = "-rwxr-xr-x 1 root root 502131 Feb 14 20:00 information_schema_19-02-2024_20h-00m-01s.sql.gz"
 
# Define a regular expression pattern to match the date
date_pattern = re.compile(r'(\d{2}-\d{2}-\d{4})')
 
# Find matches in the line
matches = date_pattern.search(line)
print(matches.group(1))
 
# Print the match
today_date = datetime.now().strftime("%d-%m-%Y")
print(today_date)
if today_date==matches.group(1):
    print("Date pattern found:", matches.group(1))
else:
    print("No date pattern found.")
