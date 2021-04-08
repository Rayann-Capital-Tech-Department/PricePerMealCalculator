from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.pickle.

# Step 1: The ID of the spreadsheets
unitPriceSheet_ID = '1qZgYLUQUAhqbjoYJ9wZZRib8DLfIaGz1gG_o6tSKPWw'
#Tuan's output:
nutritionFactSheet_ID = '1g10_SjiUuvz9am2ADL7yzOZfREGAtP-Jy8NumTt4RzI'
#my output:
outputListSheet_ID = '1d5SOICeHqjFfoL1xEf1bVjOoOgi2ESJOXxhgRjye-u8'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
