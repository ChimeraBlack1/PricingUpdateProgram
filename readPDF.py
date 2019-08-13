# importing required modules 
import PyPDF2 

# creating a pdf file object in read binary mode
pdfFileObj = open('2machineTest.pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
# print(pdfReader.numPages) 

# creating a page object 
pageObj = pdfReader.getPage(0) 

# extracting text from page 
extractedText = pageObj.extractText()

# split text at newline
extractedText = extractedText.split(' \n ')

# get the number of configs in the pdf
configs = len(extractedText) / 7

#create config pointer
configPointer = 0

for x in range(0, int(configs)):
  #print("x is:" + str(x))
  print(" ")
  print("Config " + str(x + 1) + " ...")
  itemNumber = extractedText[configPointer + 0]
  itemName = extractedText[configPointer + 1]
  itemDesc = extractedText[configPointer + 2]
  itemMAPP = extractedText[configPointer + 3]
  itemRMAP1 = extractedText[configPointer + 4]
  itemRMAP2 = extractedText[configPointer + 5]
  itemMSRP = extractedText[configPointer + 6]
  itemName = itemName.replace("\n", "")
  itemDesc = itemDesc.replace("\n","")
  itemMAPP = itemMAPP.replace("\n","")
  itemRMAP1 = itemRMAP1.replace("\n","")
  itemRMAP2 = itemRMAP2.replace("\n","")
  itemMSRP = itemMSRP.replace("\n","")
  print("item Number: " + itemNumber)
  print("item Name: " + itemName)
  print("item Desc: " + itemDesc)
  print("item MAPP: " + itemMAPP)
  print("item RMAPP1: " + itemRMAP1)
  print("item RMAPP2: " + itemRMAP2)
  print("item MSRP: " + itemMSRP)
  configPointer =  configPointer + 7


# closing the pdf file object 
pdfFileObj.close()
