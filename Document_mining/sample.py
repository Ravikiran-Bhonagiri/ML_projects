
# importing required modules
import PyPDF2


# creating a pdf file object
pdfFileObj = open('Detroit_2017.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)
num = pdfReader.numPages

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

####=======================================================

#pageObj = pdfReader.getPage(1)
#print(pageObj.extractText())

#pageObj = pdfReader.getPage(3)
#print(pageObj.extractText())

#pageObj = pdfReader.getPage(4)
#print(pageObj.extractText())

txt = ""

for index in range(0,num):
    pageObj = pdfReader.getPage(index)
    if pageObj.getContents() is not None:
        print("\n\nPage Number {} starts\n\n".format(index))
        #print(pageObj.extractText())
        txt = pageObj.extractText().strip()
        print(type(txt))
        print(len(txt))
        print("\n\nPage Number {} ends\n\n".format(index))
