from openpyxl import load_workbook

wb = load_workbook('hello.xlsx')

ws = wb.create_sheet('sheet2')
ws2 = wb.create_sheet('sheet3')

for sheet in wb:
    print(sheet.title)

""" Get worksheet by index """
ws1 = wb.worksheets[0]
ws2 = wb.worksheets[1]
ws3 = wb.worksheets[2]

worksheets = wb.sheetnames
print(worksheets)
print(ws3)

""" Get worksheet by name """
ws1 = wb['Sheet1']
ws2 = wb['sheet2']
ws3 = wb.worksheets[2]

worksheets = wb.sheetnames
print(worksheets)
print(ws2)

for index,sheet in enumerate(wb):
    print(index,sheet)
