from openpyxl import Workbook

wb = Workbook()
ws = wb.worksheets[0]

# Using relevant reference
ws['A1'].value = 56
ws['C3'].value = 'abc'

# Using absolute reference
ws.cell(row=4, column=3).value = 'def'
ws.cell(4,3).value = 're-def'

print(ws['C4'].value)

""" Get Column Letter """
from openpyxl.utils.cell import get_column_letter

print(get_column_letter(5))
print(get_column_letter(26))
print(get_column_letter(260))

from openpyxl.utils.cell import column_index_from_string

print(column_index_from_string("A"))
print(column_index_from_string("IZ"))
