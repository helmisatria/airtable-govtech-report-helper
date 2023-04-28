# Govtech Edu - Report Helper

This Python script helps me:

1.	Download all attachments from Airtable.
2.	List all dates in the Airtable rows.
3.	Print all filenames in the Airtable rows.

## Requirements

1.	Python 3.6 or higher
2.	Airtable base and API keys
3.  `pip install -r requirements.txt` to install the necessary Python packages

## How to Use

1.	Ensure the environment variables are set in the .env file.
2.	Also ensure the table ID is up to date.
3.	To download all attachments from Airtable, run `python download-attachments.py`.
4.	To list all dates in the Airtable rows, run `python output-dates-filenames.py`.
5.	After that, copy the output and paste it into a Google Sheet (you can clone from this sheet https://docs.google.com/spreadsheets/d/1_gihKxaG75fHwansP7dzgYEhwg9YrHUDogLqDsaUm-Y/edit#gid=1033690464).