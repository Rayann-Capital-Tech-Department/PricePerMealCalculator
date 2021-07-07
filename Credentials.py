from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.pickle.

# Get sheet keys. Copy/paste from between the last two slashes "/" in the google sheet URL:

# unit price sheet
unitPriceSheet_ID = '1qZgYLUQUAhqbjoYJ9wZZRib8DLfIaGz1gG_o6tSKPWw'
# nutirion facts sheet
nutritionFactSheet_ID = '1g10_SjiUuvz9am2ADL7yzOZfREGAtP-Jy8NumTt4RzI'
# output sheet
outputListSheet_ID = '1d5SOICeHqjFfoL1xEf1bVjOoOgi2ESJOXxhgRjye-u8'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
