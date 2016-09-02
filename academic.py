import PyPDF2
import os
import re

def parse_string(line):
	line=line.replace("\n","")
	k=re.search("\d",line).start()
	date=line[k]
	try:
		int(line[k+1])
		date=date+line[k+1]
		info=line[k+2:]
	except:
		info=line[k+1:]

	day=line[:k]
	day=day.replace(" ","")
	return [date,day,info.strip()]



pdfFile=open("AcademicCalendar.pdf","rb")
fo=open("cleaned.csv","w")

reader=PyPDF2.PdfFileReader(pdfFile)
days=["mon","tue","wed","thu","fri","sat","sun"]
month=["JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER","JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE"]
#reader.numPages
for x in range(reader.numPages):
	#print "\nMONTH : ",month[x],"\n"
	fo.write(month[x]+"\n")
	data=reader.getPage(x).extractText()
	j=0
	length=len(data)
	
	while j+3<=length:

		temp=data[j:j+3]

		if temp.lower() in days: 
			varint=j
			j=j+3
			i=(days.index(temp.lower())+1)%7

			while True:
				temp1=data[j:j+3]

				if temp1.lower()==days[i]:
				  rawdata=data[varint:j].split("\n")
				  rawdata=" ".join(rawdata)
				  rawdata=parse_string(rawdata)
				  #print rawdata
				  rawdata=",".join(rawdata)+"\n"
				  fo.write(rawdata)  
				  j=j-1
				  break

				if j+3>=length:
				  rawdata=data[varint:].split("\n")
				  rawdata=" ".join(rawdata)
				  rawdata=parse_string(rawdata)
				  #print rawdata
				  rawdata=",".join(rawdata)+"\n"
				  fo.write(rawdata) 
				  break

				j=j+1
		j=j+1
	#print "\n\n"

fo.close()
				

