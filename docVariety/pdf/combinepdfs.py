## Combines all the PDFs in the current working directory into a single PDF

import PyPDF2, os

pdfOnly = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfOnly.append(filename)

pdfOnly.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfOnly:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()