from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file,client,tools
try:
	import argparse
	flags=argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
	flags=none

def create_remainder(name,date):
	
	#REFERENCE:https://developers.google.com/google-apps/calendar/v3/reference/events/insert#examples
	print name+" "+date
	SCOPES='https://www.googleapis.com/auth/calendar'

	store=file.Storage('storage.json')
	creds=store.get()

	if not creds or creds.invalid:
		flow=client.flow_from_clientsecrets('client_secret.json',SCOPES)
		creds=tools.run_flow(flow,store,flags) \
			  if flags else tools.run(flow,store)

	CAL=build('calendar','v3',http=creds.authorize(Http()))
	 
	#Events in JSON format
	ID="fokql1u8cutplmdfeu6ql4hqs8@group.calendar.google.com"
	EVENT={
	'summary':name,
	'start':{'dateTime':date+'T7:00:00+05:30'},
	'end':  {'dateTime':date+'T8:00:00+05:30'}
		  }

	response = CAL.events().insert(calendarId=ID,sendNotifications=True,body=EVENT).execute()
	
	if response['status']=='confirmed':
		return 'Success'
	else:
		return 'Error Occured'


#print create_remainder("Test0","2016-09-07")