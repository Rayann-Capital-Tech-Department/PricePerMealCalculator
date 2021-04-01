from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.pickle.

# Step 1: The ID of the spreadsheets
# unitPriceSheet_ID = '1qZgYLUQUAhqbjoYJ9wZZRib8DLfIaGz1gG_o6tSKPWw'
unitPriceSheet_ID = '1dXsQooj-8lJOWAYF9MyTHgC4t-ZV8z4eGaERwYj9K-c' #mine
#Tuan's output:
# nutritionFactSheet_ID = '1g10_SjiUuvz9am2ADL7yzOZfREGAtP-Jy8NumTt4RzI'
nutritionFactSheet_ID = '1c4L_QCy4h2MzQYs5DfgSANthZ_GsbBnDN8RO20otMnE'#me
#my output:
# outputListSheet_ID = '1d5SOICeHqjFfoL1xEf1bVjOoOgi2ESJOXxhgRjye-u8'
outputListSheet_ID = '1bnsDV-xiwJrH02umKhmr_Yn3ubYVwKNs1RnVhEceWS8' #mine

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
