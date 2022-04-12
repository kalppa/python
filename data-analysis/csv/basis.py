import csv

# Open the file
data = open('example.csv', encoding='utf-8')

# csv.reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)
print(data_lines[81][1])
print(len(data_lines))

"""Write to a CSV"""

file_output = open('file_output.csv', mode='w',newline = '')
csv_writer = csv.writer(file_output,delimiter=',')

csv_writer.writerow(['a','b','c'])
file_output.close()