# importing required modules 
import PyPDF2 
import csv
from openpyxl import Workbook

#create workbook object
wb = Workbook()

#grab active worksheet
ws = wb.active

#set PDF source to read from
sourceDoc = '2machineTest.pdf'

# creating a pdf file object in read binary mode
pdfFileObj = open(sourceDoc, 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

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
  # print("Product Number: " + itemNumber)
  # print("Name: " + itemName)
  # print("Description: " + itemDesc)
  # print("MAPP: " + itemMAPP)
  # print("RMAPP1: " + itemRMAP1)
  # print("RMAPP2: " + itemRMAP2)
  # print("MSRP: " + itemMSRP)
  configPointer =  configPointer + 7


#assign data to cells
ws['A1'] = itemNumber
wb.save('sample.xlsx')

ws.append([1,2,3])
# closing the pdf file object 
# pdfFileObj.close()

# row = [itemNumber, itemName]

# csvFile = open('newMFP.csv', 'w')
# try:
#   writer = csv.writer(csvFile)
#   writer.writerows(row)
# finally:
#   csvFile.close()    


#attach model-specific accessories


#attach global accessories to each model as appropriate
