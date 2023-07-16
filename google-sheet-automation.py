import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open('Your Google Sheet Name').sheet1  # Replace 'Your Google Sheet Name' with the actual sheet name

# Access data from a cell in sheet
cell_value = sheet.cell(1, 1).value
print(f"Cell value at (1, 1): {cell_value}")
