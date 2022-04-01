from openpyxl import Workbook

wb = Workbook()
ws = wb.worksheets[0]
ws['A1'].value = 'Train'
ws.cell(1,1).offset(0,1).value = 'Train cart'

print(ws['A1'].value)
print(ws['B1'].value)


mother_cell = ws.cell(3,3)
child_cell = mother_cell.offset(0,1)

print(mother_cell,child_cell)