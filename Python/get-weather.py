import requests

def get_precip(gooddate):
  # b922g10eed9bf962f
	urlstart = 'http://api.wunderground.com/api/YOUR-ACCESS-KEY/history_'
	urlend = '/q/COUNTRY/place.json' # example: '/q/IRELAND/dublin.json'

	url = urlstart + str(gooddate) + urlend
	data = requests.get(url).json()
	for summary in data['history']['dailysummary']:
		f.write(','.join((summary['date']['year'], summary['date']['mon'], summary['date']['mday'], summary['maxtempm'], summary['meantempm'], summary['mintempm'])) + "\n")

if __name__ == "__main__":
	from datetime import date
	from dateutil.rrule import rrule, DAILY
	import time
	
	month = 11

	f = open('temp_ire_' + str(month) + '.csv', 'w')
	f.write('date,month,day,max,mean,min\n')

	# a = date(2009, 7, 1)
	a = date(2010, month, 1)
	b = date(2010, month, 30)
	ct = 1
	for dt in rrule(DAILY, dtstart=a, until=b):
		get_precip(dt.strftime("%Y%m%d"))
		ct = ct + 1
		if ct == 10:
			ct = 1
			print "sleeping for 2 minutes"
			time.sleep(120)
	f.close()
