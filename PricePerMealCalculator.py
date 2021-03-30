from __future__ import print_function

from fractions import Fraction

import Credentials
import helperFunctions

# TODOs
# - exact value --> what to actually order

# Get the name of the input and output sheet
nutritionFactSheet_name = input("Enter the input sheet name for recipe nutrition facts: ")
unitPriceSheet_name = input("Enter the input sheet name for unit prices: ")
output_sheet = input("Enter the output sheet name: ")

nutritionFactSheet_index = helperFunctions.getSheetIndex(Credentials.nutritionFactSheet_ID, nutritionFactSheet_name)
unitPriceSheet_index = helperFunctions.getSheetIndex(Credentials.nutritionFactSheet_ID, unitPriceSheet_name)

nutritionFactSheet_range = nutritionFactSheet_name + helperFunctions.getRange(Credentials.nutritionFactSheet_ID, nutritionFactSheet_index)
unitPriceSheet_range = unitPriceSheet_name + helperFunctions.getRange(Credentials.unitPriceSheet_ID, unitPriceSheet_index)
output_range = output_sheet + "!A1"

# Add new worksheet into spreadSheet with ID: outputListID and title: sheet_name

helperFunctions.add_sheets(Credentials.outputListSheet_ID, output_sheet) #added output

nutritionRange = nutritionFactSheet_name + "!A2:C6"

nurition_facts = Credentials.sheet.values().get(spreadsheetId=Credentials.nutritionFactSheet_ID,
                                              range=nutritionRange).execute() #FIX
values_nutrition_facts = nurition_facts.get('values', [])

unit_prices = Credentials.sheet.values().get(spreadsheetId=Credentials.unitPriceSheet_ID,
                                              range="Sheet1!A2:H11").execute()
values_unit_prices = unit_prices.get('values', [])

# print(values_nutrition_facts)
# print("\n")
# print(values_unit_prices)

# ingredient_list = Credentials.sheet.values().get(spreadsheetId=Credentials.input_unit_prices_ID,
#                                                  range="sheet1!A1:Z15").execute()

# Step 3: Write the header for columns of output file

headerList = ["Meal Name", "Total Price"]
otherHeaderList = ["Ingredient", "Price", "Supplier"]
# Final results array
total_results_output = []
total_results_output.append(headerList)

total_results_output.append([""]) # meal row, fill in last
total_results_output.append(otherHeaderList) #next header

# values_unit_prices = [[tomato	|   Jayce’s tomatoes	| 200	yes      |    50 |	grams   |  	7], ...]
# values_nutrition_facts = [Potato - boile   2	150 g]

# #NUTIRIONFACTS
# ingredient, amount needed
#
# match ingredient == ingredient
# (amount needed / per amount) * price

# dictionary for {ingrient, amount needed} in recipe
                        # Price (¥)	Amount	Units
unitPriceDict = {values_unit_prices[i][0] : [values_unit_prices[i][5], values_unit_prices[i][6], values_unit_prices[i][7]] for i in range(len(values_unit_prices))}
#ingredient : [price, amount, units]
#mushrooms : [300, 100,	g]

# print("\n")
# print(unitPriceDict)

totalPrice = 0

for i in range(len(values_nutrition_facts)):
    ingredient = values_nutrition_facts[i][0] #'potato - boiled'
    if (ingredient == ""):
        break
    else:
        splitIngredient = ingredient.split(" ", 1)
        actualIngredient = splitIngredient[0] #potato
        print(actualIngredient)
        print("\n")
        unit_price = unitPriceDict.get(actualIngredient)[0] #594
        unit_amount = unitPriceDict.get(actualIngredient)[1]
        # units = unitPriceDict.get(actualIngredient)[2]
        supplier = values_unit_prices[i][1]
        actual_amount = values_nutrition_facts[i][2]
        splitString = actual_amount.split(" ", 1) #["150", "g"] *1 means 1 line
        final_amount = splitString[0]
        price = (int(final_amount) / int(unit_amount)) * int(unit_price)
        totalPrice += price
        total_results_output.append([actualIngredient, price, supplier])

total_results_output[1].extend([nutritionFactSheet_name, totalPrice])

# write out the 2D array into the google spreadsheet
request_1 = Credentials.sheet.values().update(spreadsheetId=Credentials.outputListSheet_ID, range=output_range,
                                              valueInputOption="USER_ENTERED",
                                              body={"values": total_results_output}).execute()
