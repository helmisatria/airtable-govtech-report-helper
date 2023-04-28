import re
import os

from pyairtable import Table
from datetime import datetime
from collections import defaultdict

from dotenv import load_dotenv

load_dotenv()
# Get the API key from an environment variable
api_key = os.environ.get('AIRTABLE_API_KEY')

# Get the base ID and table name from environment variables
base_id = os.environ.get('AIRTABLE_BASE_ID')
table_id = os.environ.get('AIRTABLE_TABLE_ID')

# !! Change the table id (in env), take a look at the airtable API docs https://airtable.com/appzYwCLGCE6e0jEA/api/docs#curl/table:pd-6%20april
table = Table(api_key, base_id, table_id)
data = table.all(fields=['Tanggal', 'Log Aktivitas', 'Bukti Log Aktivitas'])

# Sort the data locally by the 'Tanggal' field in ascending order
data_sorted = sorted(data, key=lambda x: x['fields']['Tanggal'])

# Create a dictionary to store the filenames by date
filenames_by_date = defaultdict(list)

for item in data_sorted:
    fields = item.get('fields', {})
    bukti_log_aktivitas = fields.get('Bukti Log Aktivitas', [])

    if bukti_log_aktivitas:
        image_data = bukti_log_aktivitas[0]
        image_url = image_data.get('url', '')
    else:
        image_url = ''

    date_str = fields.get('Tanggal', '')

    if date_str:
        # Convert the date format from "YYYY-MM-DD" to "DD MMMM YYYY" in Indonesian language
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        date_formatted = date_obj.strftime('%d %B %Y')
        print(date_formatted)

        activity = fields.get('Log Aktivitas', '')

        # Check if the activity is "Cuti/cuti" or "Libur/libur" and adjust the filename accordingly
        if 'cuti' in activity.lower():
            filename = f"{date_obj.strftime('%m-%d')} - Bukti Approval - Cuti Tahunan.png"
        elif 'libur' in activity.lower():
            filename = ''
        else:
            filename = f"{date_obj.strftime('%m-%d')} - Screenshot {activity}.png"

        # Replace invalid characters in the filename with spaces
        filename = re.sub(r'[\\/:"*?<>|_]', ' ', filename)

        # Add the filename to the dictionary
        filenames_by_date[date_formatted].append(filename)

for date_formatted, filenames in filenames_by_date.items():
    # Reformat the date to include the month in Bahasa Indonesia
    date_obj = datetime.strptime(date_formatted, '%d %B %Y')
    date_formatted_id = date_obj.strftime('%d %B %Y').replace(
        date_obj.strftime('%B'), date_obj.strftime('%B').capitalize())

    # print(date_formatted_id)
    for filename in filenames:
        print(filename if filename else '')
