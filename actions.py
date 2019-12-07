from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		
		loc = tracker.get_slot('location')
		
		
		import requests, json 
		city = loc
		response = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=15295460f958fff5afe709d205204238&q={}".format(city))

		description = response.json()['weather'][0]['description']
		temp = response.json()['main']['temp']
		print(description, temp)
		
		

		response = """It is currently {} in {} at the moment. The temperature is {} degrees kelvin""".format(description, loc, temp)
						
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

