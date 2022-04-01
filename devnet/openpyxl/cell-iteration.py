from openpyxl import Workbook
from openpyxl import load_workbook

wb = Workbook()
ws = wb.create_sheet("sheet")

for row in range(1,4):
    for col in range (1,4):
        # cell = ws.cell(row=row,column=col)
        cell = ws.cell(row=col,column=row)
        print(cell.coordinate, end= " ")
    print()

for row in ws.iter_rows(min_row=1, min_col=1, max_row=4, max_col=3):
    print(row)
    for cell in row:
        print(cell.coordinate, end = " ")
    print()


for col in ws.iter_cols(min_col=1, max_col=3):
    print(col)
    for cell in col:
        print(cell.coordinate, end = " ")
    print()


""" Get the Max Columns and Rows"""

wb = load_workbook('hello.xlsx')
ws = wb.worksheets[0]
print(ws)
print(ws['A2'].value)
print(ws.max_row)
print(ws.max_column)
