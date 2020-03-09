import win32com.client, docx

wordFilename = 'test.docx'
pdfFilename = 'your_pdf_file.pdf'

doc = docx.Document()
doc.add_paragraph('This is on the first page!')
doc.save(wordFilename)
wdFormatPDF = 17
wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.close()
wordObj.quit()
