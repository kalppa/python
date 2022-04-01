import openpyxl

wb = openpyxl.Workbook()
wb.save('My first workbook.xlsx')

wb = openpyxl.load_workbook('hello.xlsx')
for sheet in wb:
    print(sheet.title)