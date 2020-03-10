## Corrects costs in produce sales spreadsheet.

import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb['Sheet']

PRICE_UPDATES = {'Garlic': 3.07, 
                 'Lemon': 1.27, 
                 'Celery': 1.19}

for row in range(2, sheet.max_row):
    produce = sheet.cell(row=row, column=1).value
    # cost = sheet['B' + str(row)].value
    if produce in PRICE_UPDATES:
        sheet.cell(row=row, column=2).value = PRICE_UPDATES[produce]
        
wb.save('updatedProduceSales.xlsx')

print('Prices Updated!')
