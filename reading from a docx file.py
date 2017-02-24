import os
import docx

acc.open("file.docx","r") #open the file in read mode
file_obj = acc.xreadlines()#returns self i.e file obj

reveal = docx.opendocx(file_obj)#open the document file
data = docx.getdocumenttext(reveal)#returns a list of text


