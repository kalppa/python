""" Convert PDF to TXT """

from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = 'How_to_be_a_star_engineer.pdf'

# Using PdfFileReader class read the PDF file to a variable.
pdf = PdfFileReader(file_path)

# Store the text to a text file
with open('how-to.txt', 'w', encoding='UTF-8') as f:
    for page_num in range(pdf.numPages):
        # print(f'The total page number is: {page_num}')

        # Store all the page information to pageObj
        page_obj = pdf.getPage(page_num)
        # print(page_obj)

        try:
            text = page_obj.extractText()
            # print(text)

            # Use a seperator to separate each pages
            print(''.center(100,'-'))
        except:
            pass
        else:
            f.write(f'Page {page_num + 1} \n')
            f.write(''.center(100, '-') + '\n')
            f.write(text)
    f.close()
