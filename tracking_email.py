from __future__ import print_function
from googleapiclient.discovery import build 
from google.oauth2 import service_account
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
print(os.getenv('SPREADSHEET_ID'), os.getenv('TYPE'), os.getenv('PROJECT_ID'), os.getenv('PRIVATE_KEY_ID'), os.getenv('PRIVATE_KEY'), os.getenv('CLIENT_EMAIL'), os.getenv('CLIENT_ID'), os.getenv('AUTH_URI'), os.getenv('TOKEN_URI'), os.getenv('AUTH_PROVIDER_CERT_URL'), os.getenv('CLIENT_CERT_URL'), os.getenv('UNIVERSE_DOMAIN'))
# credentials = service_account.Credentials.from_service_account_info({
#   "type": os.getenv('TYPE'),
#   "project_id": os.getenv('PROJECT_ID'),
#   "private_key_id": os.getenv('PRIVATE_KEY_ID'),
#   "private_key": os.getenv('PRIVATE_KEY'),
#   "client_email": os.getenv('CLIENT_EMAIL'),
#   "client_id": os.getenv('CLIENT_ID'),
#   "auth_uri": os.getenv('AUTH_URI'),
#   "token_uri": os.getenv('TOKEN_URI'),
#   "auth_provider_x509_cert_url": os.getenv('AUTH_PROVIDER_CERT_URL'),
#   "client_x509_cert_url": os.getenv('CLIENT_CERT_URL'),
#   "universe_domain": os.getenv('UNIVERSE_DOMAIN')
# })
# spreadsheet_service = build('sheets', 'v4', credentials=credentials)

# SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
# RANGE_NAME = 'tracking_email'
# sheet = spreadsheet_service.spreadsheets()
# result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
# values = result.get('values', [])
# max_cols = max(len(row) for row in values)
# values = [row + [''] * (max_cols - len(row)) for row in values]
# df = pd.DataFrame(values[1:], columns=values[0])
# df = df.fillna('')
# # df.head()