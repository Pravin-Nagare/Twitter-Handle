import twitter
from datetime import date
import time
import sys

def getdate(from_date):
	day,month,date_of,time_of,s,year = from_date.split(' ')	#from_date is a string. split by the spaces gives the details
	if month == "Jan" :
		mon = 1
	elif month == "Feb" :
		mon = 2
	elif month == "Mar" :
		mon = 3
	elif month == "Apr" :
		mon = 4
	elif month == "May" :
		mon = 5
	elif month == "Jun" :
		mon = 6
	elif month == "Jul" :
		mon = 7
	elif month == "Aug" :
		mon = 8
	elif month == "Sep" :
		mon = 9
	elif month == "Oct" :
		mon = 10
	elif month == "Nov" :
		mon = 11
	elif month == "Dec" :
		mon = 12
	
	date_of_tweet = date(int(year),mon,int(date_of))
	#placing the date, month and date in the format of date
	
	return date_of_tweet

def getcount(handle,num_days):
	if num_days < 1:
		print 'Usage: Number of days should be greater than 0'
		return 0
	
	date_from = date(date.today().year, date.today().month, date.today().day - num_days)	
	#getting date of 7 days prior to today's date
	
	api = twitter.Api()
	
	#GetUserTimeline returns status of the tweets. include_rts is the parameter for setting the retweets as well. count sets it to a maximum of 200 tweets. The maximum upper limit is 200.
	
	status = api.GetUserTimeline(handle, include_rts = 1, count=200)	
	count = 0
	
	for each_status in status:
		date_of_tweet = getdate(each_status.created_at)
		if date_of_tweet>date_from:
			print "%d . The Tweet : %s " % (count+1,each_status.text),
			print "Tweeted on: %s\n\n" % (each_status.created_at)
			count = count+1
		
	return count
	
if __name__ == "__main__":
	
	if len(sys.argv) == 1:
		print 'Usage: Username is the first argument\nDefault = "PravinNagare"\n'
		handle = "PravinNagare"
		print 'Usage: Number of days from when to find the count is the second parameter\nDefault = "7"\n'
		num_days = 7
	elif len(sys.argv) == 2:
		handle = sys.argv[1]
		print 'Usage: Number of days from when to find the count is the second parameter\nDefault = "7"\n'
		num_days = 7
	elif len(sys.argv) == 3:
		handle = sys.argv[1]
		num_days = sys.argv[2]
			
	count = getcount(handle,int(num_days))
	print "Total tweets in the past seven days : %d\n" % count


