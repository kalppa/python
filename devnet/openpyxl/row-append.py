from openpyxl import load_workbook
wb = load_workbook('hello.xlsx')
ws = wb.worksheets[0]
ws.append(["sales",2018,2019])
# wb.save('test.xlsx')

sales_data = [
    ["north", 100, 200],
    ["sought", 101, 201],
    ["east", 102, 202],
    ["west", 103, 203]
]

for row in sales_data:
    ws.append(row)
wb.save('test.xlsx')
