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
extractedText = extractedText.split(' \n ')

#Item Data
itemNumber = extractedText[0]
itemName = extractedText[1]
itemDesc = extractedText[2]
itemMAPP = extractedText[3]
itemRMAP1 = extractedText[4]
itemRMAP2 = extractedText[5]

#remove \n
itemName = itemName.replace("\n", "")
itemDesc = itemDesc.replace("\n","")
itemMAPP = itemMAPP.replace("\n","")
itemRMAP1 = itemRMAP1.replace("\n","")
itemRMAP2 = itemRMAP2.replace("\n","")

# print variables
print("item Number: " + itemNumber)
print("item Name: " + itemName)
print("item Desc: " + itemDesc)
print("item MAPP: " + itemMAPP)
print("item RMAPP1: " + itemRMAP1)
print("item RMAPP2: " + itemRMAP2)

# closing the pdf file object 
pdfFileObj.close()
