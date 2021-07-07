from __future__ import print_function
from fractions import Fraction

import Credentials
import helperFunctions

#nutirion fact sheet data array
sheet_metadata = Credentials.service.spreadsheets().get(spreadsheetId=Credentials.nutritionFactSheet_ID).execute()
sheets = sheet_metadata.get('sheets', '')

#unit price fact sheet data array
unitprice_metadata = Credentials.service.spreadsheets().get(spreadsheetId=Credentials.unitPriceSheet_ID).execute()
unitsheets = unitprice_metadata.get('sheets', '')

"""
for each recipe in the nutrition fact spreadsheet, it will update
all existing price per meal sheets and add new ones if they don't exist.
"""
def updateAll():
    for sheet in sheets:
        nutritionFactSheet_name = sheet["properties"]["title"]
        unitPriceSheet_name = unitsheets[0]["properties"]["title"]
        output_sheet = nutritionFactSheet_name
        nutritionFactSheet_index = helperFunctions.getSheetIndex(Credentials.nutritionFactSheet_ID, nutritionFactSheet_name)
        unitPriceSheet_index = helperFunctions.getSheetIndex(Credentials.nutritionFactSheet_ID, unitPriceSheet_name)

        nutritionFactSheet_range = nutritionFactSheet_name + helperFunctions.getRange(Credentials.nutritionFactSheet_ID, nutritionFactSheet_index)
        unitPriceSheet_range = unitPriceSheet_name + helperFunctions.getRange(Credentials.unitPriceSheet_ID, unitPriceSheet_index)
        output_range = nutritionFactSheet_name + "!A1"

        # Add new worksheet into spreadSheet with ID: outputListID and title: sheet_name
        helperFunctions.add_sheets(Credentials.outputListSheet_ID, output_sheet) #added output

        # get arrays of nutrition facts and unit price sheet values
        nutrition_facts = Credentials.sheet.values().get(spreadsheetId=Credentials.nutritionFactSheet_ID, range=nutritionFactSheet_range).execute().get('values', [])
        unit_prices = Credentials.sheet.values().get(spreadsheetId=Credentials.unitPriceSheet_ID, range=unitPriceSheet_range).execute().get('values', [])
        print(unit_prices)

        header = ["Meal Name", "Total Price"]
        subheader = ["Ingredient", "Tag", "Price", "Supplier"]

        # prep final results array
        results = []
        results.append(header)
        results.append([]) # empty row, fill in later
        results.append(subheader) # next header

        # build unit price dictionary
        # (pork, chuckeye) : [costco, 10, 100, g]
                            # supplier, price in yen, amount, unit
        unit_price_dict = {(unit_prices[i][0], unit_prices[i][1]) : [unit_prices[i][2], unit_prices[i][6], unit_prices[i][7], unit_prices[i][8]] for i in range(len(unit_prices))}
        total_price = 0

        for i in range(1, len(nutrition_facts)):
            ingredient = nutrition_facts[i][0] # e.g. "pork"
            tag = nutrition_facts[i][1] # e.g. "chuckeye"
            tup = (ingredient, tag) # (ingredient, tag)
            if (ingredient == ""):
                break
            else:
                supplier = unit_price_dict.get(tup)[0]
                price = unit_price_dict.get(tup)[1]
                amount = unit_price_dict.get(tup)[2]
                units = unit_price_dict.get(tup)[3]
                
                actual_amount = nutrition_facts[i][4]
                final_amount, unit = actual_amount.split(" ", 1) #["150", "g"] from "150 g"
                price = (int(final_amount) / int(amount)) * int(price)
                total_price += price
                results.append([ingredient, tag, price, supplier])

        results[1].extend([nutritionFactSheet_name, total_price])

        # write out the 2D array into the google spreadsheet
        request_1 = Credentials.sheet.values().update(spreadsheetId=Credentials.outputListSheet_ID, range=output_range,
                                                    valueInputOption="USER_ENTERED",
                                                    body={"values": results}).execute()

updateAll()
