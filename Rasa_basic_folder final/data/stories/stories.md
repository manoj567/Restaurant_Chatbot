## complete_path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget_for_two
* restaurant_search{"budget":"300"}
    - slot{"budget":"300"}
    - action_search_restaurants
- utter_ask_email
* send_email{"email": "krishnagadde143@gmail.com"}
    - slot{"email":"krishnagadde143@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    

## location_specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget_for_two
* restaurant_search{"budget":"700"}
    - slot{"budget":"700"}
    - action_search_restaurants
- utter_ask_email
* send_email{"email": "manojgadde13@gmail.com"}
    - slot{"email":"manojgadde13@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
* affirm
    - utter_goodbye
    - export