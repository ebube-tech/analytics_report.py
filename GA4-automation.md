# GA4 Automation System

This repository contains a Python automation system that integrates Google Sheets, Google Analytics, and Gmail to streamline the process of generating GA4 reports and sending them to respective managers via email as PDF attachments.

## How it Works

The automation system follows the following flow:

1. Open the Google Sheet containing GA4 property names and view IDs.
2. Access GA4 using the provided view IDs.
3. Download each GA4 report as a PDF.
4. Save each PDF with the property name and current date.
5. Open another Google Sheet with manager names and email addresses responsible for each GA4 report.
6. Create and send an email to each manager, attaching the corresponding GA4 report PDF.
7. Write the email subject as "Manager's Name - GA4 Report Name."
8. The email body contains a brief message along with the attached PDF.

## Setup

Before running the automation system, you need to set up the necessary credentials for both Google Sheets and Google Analytics. Follow the instructions below:

### Google Sheets Credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or use an existing one.
3. Enable the Google Sheets API for the project.
4. Create credentials for the project (Service Account Key) and download the JSON file containing the credentials.
5. Save the JSON file as `sheets_credentials.json` in the root directory of this repository.

### Google Analytics Credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or use an existing one.
3. Enable the Google Analytics Reporting API for the project.
4. Create credentials for the project (OAuth client ID) and download the JSON file containing the credentials.
5. Save the JSON file as `analytics_credentials.json` in the root directory of this repository.

## Usage

1. Install the required Python libraries:

```bash
pip install gspread google-auth google-auth-oauthlib google-auth-httplib2
pip install pdfkit
```

2. Fill in the GA4 property names, view IDs, and manager details in the corresponding Google Sheets. Make sure to share the Google Sheets with the service account email (found in the JSON credentials) to allow access.

3. Run the Python script `final-ga4-to-email-automation.py` to initiate the automation process.

```bash
python final-ga4-to-email-automation.py
```

## Notes

- The automation system generates PDF reports using the `pdfkit` library. Ensure you have [wkhtmltopdf](https://wkhtmltopdf.org/) installed on your system for proper PDF conversion.

- The script sends emails using the `smtplib` library. Make sure to use valid Gmail credentials (`your_email@gmail.com` and `your_password`) or consider using an application-specific password for better security.

- This automation system is intended to be used responsibly and in compliance with Google's terms of service.

## Contributions

Contributions to this automation system are welcome! If you have any ideas, bug fixes, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

---
