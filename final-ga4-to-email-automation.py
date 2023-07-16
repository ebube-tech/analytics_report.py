import datetime
import os
import pdfkit
import smtplib
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

# Set up Google Sheets credentials
scope_sheets = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials_sheets = ServiceAccountCredentials.from_json_keyfile_name('path/to/sheets_credentials.json', scope_sheets)
client_sheets = gspread.authorize(credentials_sheets)

# Open the first Google Sheet with GA4 names and URLs
sheet_ga4 = client_sheets.open('GA4 Names and URLs').sheet1

# Get GA4 names and URLs from the Google Sheet
ga4_data = sheet_ga4.get_all_records()

# Set up Google Analytics credentials
scope_analytics = ['https://www.googleapis.com/auth/analytics.readonly']
credentials_analytics = ServiceAccountCredentials.from_json_keyfile_name('path/to/analytics_credentials.json', scope_analytics)
analytics = build('analyticsreporting', 'v4', credentials=credentials_analytics)

# Function to get GA4 report data and save as PDF
def get_ga4_report(property_name, view_id):
    # Your GA4 report configurations here
    # For example, you can use the analytics.reports().batchGet() method

    # Convert the GA4 data to HTML for PDF generation
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{property_name} GA4 Report</title>
        <style>
            /* Your CSS styling for the report */
        </style>
    </head>
    <body>
        <h1>{property_name} GA4 Report</h1>
        <!-- Insert GA4 report data here -->
    </body>
    </html>
    """
    pdfkit.from_string(html_template, f'{property_name}_ga4_report.pdf')

# Loop through the GA4 data and download reports
for item in ga4_data:
    property_name = item['Property Name']
    view_id = item['View ID']

    # Login to GA4 and download the report as PDF
    get_ga4_report(property_name, view_id)

    # Rename and move the PDF file
    today = datetime.date.today().strftime('%Y-%m-%d')
    new_filename = f'{property_name}_report_{today}.pdf'
    os.rename('ga4_report.pdf', new_filename)

    # Open the second Google Sheet with manager names
    sheet_managers = client_sheets.open('Managers').sheet1

    # Get manager names responsible for the report
    managers_data = sheet_managers.get_all_records()

    # Create and send email for each manager
    for manager_data in managers_data:
        manager_name = manager_data['Manager Name']
        manager_email = manager_data['Manager Email']

        # Set up the email parameters
        recipient = manager_email
        subject = f"{manager_name} - {property_name} GA4 Report"
        body = f"Please find attached the GA4 report for {property_name}."
        filename = new_filename

        # Create the email message
        message = f"""From: your_email@gmail.com
        To: {recipient}
        Subject: {subject}

        {body}
        """

        # Attach the PDF file to the email
        with open(filename, 'rb') as attachment:
            message += attachment.read()

        # Send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        server.sendmail('your_email@gmail.com', recipient, message)
        server.quit()

        # Remove the generated PDF file
        os.remove(new_filename)
