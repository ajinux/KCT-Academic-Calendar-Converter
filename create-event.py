import csv
import CalendarApi

out=open("cleanedCalendar.csv","rb")

data=csv.reader(out)

month={"JUNE":"2016-06","JULY":"2016-07","AUGUST":"2016-08","SEPTEMBER":"2016-09","OCTOBER":"2016-10","NOVEMBER":"2016-11","DECEMBER":"2016-12","JANUARY":"2017-01","FEBRUARY":"2017-02","MARCH":"2017-03","APRIL":"2017-04","MAY":"2017-05","JUNE":"2017-06"}

p_month="Hello"
num=0

for row in data:
	#print row
	#if not row[1] and not row[2]:
	if len(row)==1:
		p_month=month[row[0]]
		num+=1
		if num==13:
			p_month="2017-06"
		print p_month
		continue
	if row[1].lower()=="sun":
		continue
	if row[2]:
		temp=row[2]
		temp=temp.lower()
		if "v"  in temp.split() or "vi" in temp.split():
			#print "date: "+p_month+"-"+row[0]+", Info:"+temp
			if len(row[0])==1:
				day="0"+row[0]
			else:
				day=row[0]
			#print row[2]+" "+p_month+"-"+day
			CalendarApi.create_remainder(row[2],p_month+"-"+day)
		#if "holiday" in temp:
		#if "v"  in temp.split() or "vi" in temp.split() or "holiday" in temp:

#KCT Calendar
#KCT academic calendar version1 for 3rd years  2016-2017:
# This calendar contains all the holidays and Exam schedule for 3rd-year(14 batch) student at Kumaraguru college of technology.
#Kumaraguru college of technology,Chinnavedampatti, Saravanampatty, Coimbatore, Tamil Nadu 641049
