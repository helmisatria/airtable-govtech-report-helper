# Govtech Edu - Report Helper

This Python script helps me:

1. Download all attachments from Airtable.
2. List all dates in the Airtable rows.
3. Print all filenames in the Airtable rows.

## Requirements

1. Python 3.6 or higher
2. Airtable base and API keys
3. `pip install -r requirements.txt` to install the necessary Python packages

## How to Use

1. Ensure the environment variables are set in the .env file.
2. Also ensure the table ID is up to date. Get the table ID from [the Airtable API documentation](https://airtable.com/appzYwCLGCE6e0jEA/api/docs#curl/table:pd-6%20juli).
3. To download all attachments from Airtable, run `python download-attachments.py`.
4. To list all dates in the Airtable rows, run `python output-dates-filenames.py`.
5. After that, copy the output and paste it into a Google Sheet (you can clone from this sheet https://docs.google.com/spreadsheets/d/1M1b-icCwtRYv3rBGrW6oRkhkuqVZITCJ0Zg5aZ3rhro/edit#gid=1033690464).
6. Submit your evidences to https://drive.google.com/drive/u/1/folders/1F9LZrW_45pHqZHWAPqzxQBqTIf67dbtv. As reference, you can see the evidences from the previous month at https://drive.google.com/drive/u/1/folders/1CVKWrP20Nzew1Ztzfgy6p-AxOW7-B8CN.
7. Download
   1. XLSX `https://docs.google.com/spreadsheets/d/<KEY>/export?format=xlsx&gid=<GID>` as an Excel file.
   2. PDF via google sheet download as PDF.
      - Format PD-6: `Log Aktivitas Harian - Helmi Satria Nugraha - _Month_`
      - Format PD-7: `Laporan Individu - HELMI SATRIA NUGRAHA - _Month_`
