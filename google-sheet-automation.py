import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open('Your Google Sheet Name').sheet1  # Replace 'Your Google Sheet Name' with the actual sheet name

# Now you can work with the sheet, for example, get data from a cell
cell_value = sheet.cell(1, 1).value
print(f"Cell value at (1, 1): {cell_value}")
