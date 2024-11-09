from __future__ import print_function
from googleapiclient.discovery import build 
from google.oauth2 import service_account
import pandas as pd
import os
import time
from nylas import Client
from nylas.models.webhooks import CreateWebhookRequest
from nylas.models.webhooks import WebhookTriggers
from dotenv import load_dotenv
load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
credentials = service_account.Credentials.from_service_account_info({
  "type": os.getenv('TYPE'),
  "project_id": os.getenv('PROJECT_ID'),
  "private_key_id": os.getenv('PRIVATE_KEY_ID'),
  "private_key": os.getenv('PRIVATE_KEY').replace("\\n", "\n"),
  "client_email": os.getenv('CLIENT_EMAIL'),
  "client_id": os.getenv('CLIENT_ID'),
  "auth_uri": os.getenv('AUTH_URI'),
  "token_uri": os.getenv('TOKEN_URI'),
  "auth_provider_x509_cert_url": os.getenv('AUTH_PROVIDER_CERT_URL'),
  "client_x509_cert_url": os.getenv('CLIENT_CERT_URL'),
  "universe_domain": os.getenv('UNIVERSE_DOMAIN')
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

API_KEY = os.getenv('API_KEY')
GRANT_ID = os.getenv('GRANT_ID')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
EMAIL = os.getenv('EMAIL')
API_URI = os.getenv('API_URI')
API_KEY_WEBHOOK_URL = os.getenv('API_KEY_WEBHOOK_URL')

nylas = Client(
    API_KEY
)

webhooks = nylas.webhooks.list()
webhook_url_list = []

for webhook in webhooks.data:
    if webhook.status == 'active':
        webhook_url_list.append(webhook.webhook_url)

if WEBHOOK_URL not in webhook_url_list:
    webhook = nylas.webhooks.create(
      request_body={
        "trigger_types": [WebhookTriggers.MESSAGE_OPENED, WebhookTriggers.MESSAGE_LINK_CLICKED],
        "webhook_url": WEBHOOK_URL,
        "description": "track-email",
        "notification_email_address": EMAIL,
      }
    )