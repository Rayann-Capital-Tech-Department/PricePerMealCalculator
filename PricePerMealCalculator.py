from __future__ import print_function
from fractions import Fraction

import Credentials
import helperFunctions

sheet_metadata = Credentials.service.spreadsheets().get(spreadsheetId=Credentials.nutritionFactSheet_ID).execute()
sheets = sheet_metadata.get('sheets', '')

# Get the name of the input and output sheet
# nutritionFactSheet_name = input("Enter the input sheet name for recipe nutrition facts: ")
# unitPriceSheet_name = input("Enter the input sheet name for unit prices: ")
# output_sheet = input("Enter the price per meal output sheet name: ")

# for sheet in nutritionfact_sheets:
#     take unit price data 
#     outputsheet.add(price/meal)

for sheet in sheets:
    nutritionFactSheet_name = sheet["properties"]["title"]
    output_sheet = sheet["properties"]["title"]
    
    nutritionFactSheet_index = helperFunctions.getSheetIndex(Credentials.nutritionFactSheet_ID, nutritionFactSheet_name)
    unitPriceSheet_index = helperFunctions.getSheetIndex(Credentials.nutritionFactSheet_ID, unitPriceSheet_name)

    nutritionFactSheet_range = nutritionFactSheet_name + helperFunctions.getRange(Credentials.nutritionFactSheet_ID, nutritionFactSheet_index)
    unitPriceSheet_range = unitPriceSheet_name + helperFunctions.getRange(Credentials.unitPriceSheet_ID, unitPriceSheet_index)
    output_range = output_sheet + "!A1"

    # Add new worksheet into spreadSheet with ID: outputListID and title: sheet_name

    helperFunctions.add_sheets(Credentials.outputListSheet_ID, output_sheet) #added output

    nurition_facts = Credentials.sheet.values().get(spreadsheetId=Credentials.nutritionFactSheet_ID,
                                                  range=nutritionFactSheet_range).execute() #FIX
    values_nutrition_facts = nurition_facts.get('values', [])

    unit_prices = Credentials.sheet.values().get(spreadsheetId=Credentials.unitPriceSheet_ID,
                                                  range=unitPriceSheet_range).execute()
                                                  
                                                  
                                                  
    # range="Sheet1!A2:H11
    values_unit_prices = unit_prices.get('values', [])

    headerList = ["Meal Name", "Total Price"]
    otherHeaderList = ["Ingredient", "Tag", "Price", "Supplier"]
    # Final results array
    total_results_output = []
    total_results_output.append(headerList)

    total_results_output.append([]) # meal row, fill in last
    total_results_output.append(otherHeaderList) #next header
                            
    unitPriceDict = {(values_unit_prices[i][0], values_unit_prices[i][1]) : [values_unit_prices[i][2], values_unit_prices[i][6], values_unit_prices[i][7], values_unit_prices[i][8]] for i in range(len(values_unit_prices))}
    totalPrice = 0

    for i in range(1, len(values_nutrition_facts)):
        actualIngredient = values_nutrition_facts[i][0]
        tag = values_nutrition_facts[i][1]
        tup = (actualIngredient, tag) #(ingredient, tag)
        if (actualIngredient == ""): # just in case
            break
        else:
            supplier = unitPriceDict.get(tup)[0]
            unit_price = unitPriceDict.get(tup)[1]
            unit_amount = unitPriceDict.get(tup)[2]
            units = unitPriceDict.get(tup)[3]
            
            actual_amount = values_nutrition_facts[i][4]
            splitString = actual_amount.split(" ", 1) #["150", "g"] *1 means 1 line
            final_amount = splitString[0]
            unit = splitString[1]
            price = (int(final_amount) / int(unit_amount)) * int(unit_price)
            totalPrice += price
            total_results_output.append([actualIngredient, tag, price, supplier])

    total_results_output[1].extend([nutritionFactSheet_name, totalPrice])

    # write out the 2D array into the google spreadsheet
    request_1 = Credentials.sheet.values().update(spreadsheetId=Credentials.outputListSheet_ID, range=output_range,
                                                  valueInputOption="USER_ENTERED",
                                                  body={"values": total_results_output}).execute()
