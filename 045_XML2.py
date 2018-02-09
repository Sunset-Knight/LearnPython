#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request
from datetime import datetime

class DefaultSaxHandler(object):
	def __init__(self):
		self.city = {}
		self.forecast = []
	def start_element(self, name, attrs):
		if name == 'yweather:location':
			self.city = attrs['city']
		if name == 'yweather:forecast':
			cday = datetime.strptime(attrs['date'], '%d %b %Y')
			date = cday.strftime('%Y-%m-%d')
			self.forecast.append({'date': date,
			                      'high': attrs['high'],
			                      'low': attrs['low']
			                      })
			
	def end_element(self, name):
		pass
		# print('sax:end_element: %s' % name)
	def char_data(self, text):
		pass
		# print('sax:char_data: %s' % text)
	
def parseXml(xml_str):
	handler = DefaultSaxHandler()
	parser = ParserCreate()
	parser.StartElementHandler = handler.start_element
	parser.EndElementHandler = handler.end_element
	parser.CharacterDataHandler = handler.char_data
	parser.Parse(xml_str)
	return {'city': handler.city, 'forecast': handler.forecast}
# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
with request.urlopen(URL, timeout= 4) as f:
	data = f.read()

xml = r'''
<query yahoo:count="1" yahoo:created="2018-02-09T12:52:10Z" yahoo:lang="zh-CN"><results><channel><yweather:units distance="mi" pressure="in" speed="mph" temperature="F"/><title>Yahoo! Weather - Beijing, Beijing, CN</title><link>http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/</link><description>Yahoo! Weather for Beijing, Beijing, CN</description><language>en-us</language><lastBuildDate>Fri, 09 Feb 2018 08:52 PM CST</lastBuildDate><ttl>60</ttl><yweather:location city="Beijing" country="China" region=" Beijing"/><yweather:wind chill="19" direction="320" speed="25"/><yweather:atmosphere humidity="13" pressure="1022.0" rising="0" visibility="16.1"/><yweather:astronomy sunrise="7:14 am" sunset="5:44 pm"/><image><title>Yahoo! Weather</title><width>142</width><height>18</height><link>http://weather.yahoo.com</link><url>http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif</url></image><item><title>Conditions for Beijing, Beijing, CN at 07:00 PM CST</title><geo:lat>39.90601</geo:lat><geo:long>116.387909</geo:long><link>http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/</link><pubDate>Fri, 09 Feb 2018 07:00 PM CST</pubDate><yweather:condition code="23" date="Fri, 09 Feb 2018 07:00 PM CST" temp="30" text="Breezy"/><yweather:forecast code="34" date="09 Feb 2018" day="Fri" high="38" low="13" text="Mostly Sunny"/><yweather:forecast code="34" date="10 Feb 2018" day="Sat" high="32" low="15" text="Mostly Sunny"/><yweather:forecast code="32" date="11 Feb 2018" day="Sun" high="32" low="15" text="Sunny"/><yweather:forecast code="32" date="12 Feb 2018" day="Mon" high="42" low="15" text="Sunny"/><yweather:forecast code="34" date="13 Feb 2018" day="Tue" high="46" low="17" text="Mostly Sunny"/><yweather:forecast code="30" date="14 Feb 2018" day="Wed" high="42" low="27" text="Partly Cloudy"/><yweather:forecast code="30" date="15 Feb 2018" day="Thu" high="41" low="18" text="Partly Cloudy"/><yweather:forecast code="30" date="16 Feb 2018" day="Fri" high="42" low="21" text="Partly Cloudy"/><yweather:forecast code="28" date="17 Feb 2018" day="Sat" high="44" low="26" text="Mostly Cloudy"/><yweather:forecast code="30" date="18 Feb 2018" day="Sun" high="38" low="22" text="Partly Cloudy"/><description><![CDATA[<img src="http://l.yimg.com/a/i/us/we/52/23.gif"/>
<BR />
<b>Current Conditions:</b>
<BR />Breezy
<BR />
<BR />
<b>Forecast:</b>
<BR /> Fri - Mostly Sunny. High: 38Low: 13
<BR /> Sat - Mostly Sunny. High: 32Low: 15
<BR /> Sun - Sunny. High: 32Low: 15
<BR /> Mon - Sunny. High: 42Low: 15
<BR /> Tue - Mostly Sunny. High: 46Low: 17
<BR />
<BR />
<a href="http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/">Full Forecast at Yahoo! Weather</a>
<BR />
<BR />
<BR />
]]></description><guid isPermaLink="false"/></item></channel></results></query><!-- total: 5 -->
'''

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print(result)
print('ok')

