from datetime import datetime
import os
import re
import requests
from pyairtable import Table
from datetime import datetime
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()

filenames_by_date = defaultdict(list)

# Get the API key from an environment variable
api_key = os.environ.get('AIRTABLE_API_KEY')

# Get the base ID and table name from environment variables
base_id = os.environ.get('AIRTABLE_BASE_ID')
table_id = os.environ.get('AIRTABLE_TABLE_ID')

# !! Change the table id (in env), take a look at the airtable API docs https://airtable.com/appzYwCLGCE6e0jEA/api/docs#curl/table:pd-6%20april
table = Table(api_key, base_id, table_id)

data = table.all(fields=['Tanggal', 'Log Aktivitas', 'Bukti Log Aktivitas'])

# Get the current month name
current_month_name = datetime.now().strftime('%B')

# Create a directory to store the downloaded images
folder_name = f"Govtech - Log Activity {current_month_name}"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


for item in data:
    fields = item.get('fields', {})
    bukti_log_aktivitas = fields.get('Bukti Log Aktivitas', [])

    if bukti_log_aktivitas:
        image_data = bukti_log_aktivitas[0]
        image_url = image_data.get('url', '')
        date_str = fields.get('Tanggal', '')

        # Convert the date format from "YYYY-MM-DD" to "DD-MM"
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        date_formatted = date_obj.strftime('%m-%d')

        activity = fields.get('Log Aktivitas', '')

        # Check if the activity is "Cuti/cuti" and adjust the filename accordingly
        if activity.lower() == 'cuti':
            filename = f"{date_formatted} - Bukti Approval - Cuti Tahunan.png"
        else:
            filename = f"{date_formatted} - Screenshot {activity}.png"

        # Replace invalid characters in the filename with spaces
        filename = re.sub(r'[\\/:"*?<>|_]', ' ', filename)

        # Download and save the image
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(os.path.join(folder_name, filename), 'wb') as f:
                f.write(response.content)
            print(f'Downloaded: {filename}')

            # Add the filename to the dictionary
            filenames_by_date[date_formatted].append(filename)
        else:
            print(f"Failed to download: {filename}")
