from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_core_sdk.events import AllSlotsReset
import pandas as pd
import json

ZomatoData = pd.read_csv(r'zomato.csv', encoding='latin1')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City,Cuisine,budget):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		bud = tracker.get_slot('budget')
		results = RestaurantSearch(City=loc,Cuisine=cuisine,budget=bud)
		response=""
		if results.shape[0] == 0:
			response= "sorry we dont oprate in this city, please try another city"
		else:
			for restaurant in RestaurantSearch(loc,cuisine,bud).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']} \n\n"
				
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

import smtplib
class actionsendemail(Action):
    def name(self):
        return 'action_send_email'
    def run(self, dispatcher, tracker, domain):
        email=tracker.get_slot('email')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("manojgadde13@gmail.com", "____")
        message = "The details of all the restaurants you inquried \n"
        global response
        message = message + response
        s.sendmail("manojgadde13@gmail.com", str(email), message)
        s.quit()
			
             
        
         
            


