# importing required modules 
import PyPDF2 

# creating a pdf file object in read binary mode
pdfFileObj = open('MAPP.pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
# print(pdfReader.numPages) 

# creating a page object 
pageObj = pdfReader.getPage(0) 

# extracting text from page 
extractedText = pageObj.extractText()

# split text at whitespace
extractedText = extractedText.split('\n')

#Item Data
itemNumber = extractedText[0]
itemName = extractedText[2]
itemDesc = extractedText[4]
itemMAPP = extractedText[6]
itemRMAP1 = extractedText[4]
itemRMAP2 = extractedText[5]

# print variables
print("item Number: " + itemNumber)
print("item Name: " + itemName)
print("item Desc: " + itemDesc)
print("item MAPP: " + itemMAPP)
print(extractedText)
# closing the pdf file object 
pdfFileObj.close()
