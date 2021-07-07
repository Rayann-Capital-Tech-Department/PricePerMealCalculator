import Credentials

# Function to get the index of the sheet inside the spreadsheet
def getSheetIndex(IDFiles, sheetName):
    sheet_metadata = Credentials.service.spreadsheets().get(spreadsheetId=IDFiles).execute()
    sheets = sheet_metadata.get('sheets', '')
    sheetIndex = 0

    for i in sheets:
        if i["properties"]["title"] == sheetName:
            sheetIndex = i["properties"]["index"]

    return sheetIndex


# Function to get the range of the data inside the documents
def getRange(IDFiles, sheetIndex):
    res = Credentials.service.spreadsheets().get(spreadsheetId=IDFiles, fields='sheets('
                                                                               'data/rowData'
                                                                               '/values'
                                                                               '/userEnteredValue,'
                                                                               'properties(index,'
                                                                               'sheetId,'
                                                                               'title))').execute()
    sheetName = res['sheets'][sheetIndex]['properties']['title']
    
    lastRow = len(res['sheets'][sheetIndex]['data'][0]['rowData'])
    
    lastColumn = max([len(e['values']) for e in res['sheets'][sheetIndex]['data'][0]['rowData'] if e])
    

    string = ""
    while lastColumn > 0:
        lastColumn, remainder = divmod(lastColumn - 1, 26)
        string = chr(65 + remainder) + string
    range = "!A1:" + string + str(lastRow)
    return range

# Function creates new worksheet into sheet_name worksheet with ID: outputListID
def add_sheets(outputListID, sheet_name):
    try:
        request_body = {
            'requests': [{
                'addSheet': {
                    'properties': {
                        'title': sheet_name,
                        'tabColor': {
                            'red': 0.44,
                            'green': 0.99,
                            'blue': 0.50
                        }
                    }
                }
            }]
        }

        # Update the worksheet
        response = Credentials.sheet.batchUpdate(
            spreadsheetId=outputListID,
            body=request_body
        ).execute()

        return response
    except Exception as e:
        print(e)
