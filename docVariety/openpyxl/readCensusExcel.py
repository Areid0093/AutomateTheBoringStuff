## Tabulates population and number of census tracts for each county

import openpyxl, pprint
from openpyxl.utils import get_column_letter, column_index_from_string

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.active
countyData = {}

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    
    countyData.setdefault(state, {})
    
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    
    countyData[state][county]['tracts'] += 1
    
    countyData[state][county]['pop'] += int(pop)
    
print('Writing results...')
resultfile = open('census2010.py', 'w')
resultfile.write('allData =' + pprint.pformat(countyData))
resultfile.close() 
print('Done.')   