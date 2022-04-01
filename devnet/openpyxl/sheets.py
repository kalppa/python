from openpyxl import Workbook

wb = Workbook()
ws = wb.create_sheet("A sheet",0)
ws2 = wb.create_sheet("Sheet nr 2")

for sheet in wb:
    print(sheet.title)
print('\n'*1)

wb.remove(wb["Sheet"])
for sheet in wb:
    print(sheet.title)
print('\n'*1)

# Another way to delete a sheet with 'del'
del wb["Sheet nr 2"]
for sheet in wb:
    print(sheet.title)
print('\n'*1)

# Rename a sheet name
print(ws.title)
ws.title = 'New title'
print(ws.title)

wb.save('added_sheets.xlsx')
