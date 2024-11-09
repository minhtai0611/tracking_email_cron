from __future__ import print_function
from googleapiclient.discovery import build 
from google.oauth2 import service_account
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials = service_account.Credentials.from_service_account_info({
  "type": os.environ['TYPE'],
  "project_id": os.environ['PROJECT_ID'],
  "private_key_id": os.environ['PRIVATE_KEY_ID'],
  "private_key": os.environ['PRIVATE_KEY'],
  "client_email": os.environ['CLIENT_EMAIL'],
  "client_id": os.environ['CLIENT_ID'],
  "auth_uri": os.environ['AUTH_URI'],
  "token_uri": os.environ['TOKEN_URI'],
  "auth_provider_x509_cert_url": os.environ['AUTH_PROVIDER_CERT_URL'],
  "client_x509_cert_url": os.environ['CLIENT_CERT_URL'],
  "universe_domain": os.environ['UNIVERSE_DOMAIN']
})
spreadsheet_service = build('sheets', 'v4', credentials=credentials)

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
RANGE_NAME = 'tracking_email'
sheet = spreadsheet_service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
values = result.get('values', [])
max_cols = max(len(row) for row in values)
values = [row + [''] * (max_cols - len(row)) for row in values]
df = pd.DataFrame(values[1:], columns=values[0])
df = df.fillna('')
# df.head()