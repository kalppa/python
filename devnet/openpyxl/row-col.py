from openpyxl import workbook
from openpyxl import load_workbook

wb = load_workbook('hello.xlsx')
ws = wb.worksheets[0]
print(ws['C4'].value)

ws.insert_rows(0)
ws.delete_rows(0)

for row in range(1,ws.max_row):
    for col in range(1,ws.max_column):
        cell = ws.cell(row=col,column=row)
        value = cell.value
        print(cell.coordinate, end= " ")
        # print(value)
    print()


# def set_values(ws):
#     ws.delete_cols(1,100)
#     counter = 1
#     for row in ws.iter_rows(min_row=1, max_col=10, max_row=10):
#         for cell in row:
#             cell.value = counter
#             counter +=1


# def print_rows(ws):
#     row_string = ''
#     for row in ws.iter_rows(min_row=1, max_col=ws.max_column, max_row=ws.max_row):
#         for cell in row:
#             row_string += "(:<3)".format(str(cell.value) + " ")
#         row_string += '\n'
#     print(row_string)


