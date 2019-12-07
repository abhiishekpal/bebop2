## story_001
* greet
   - utter_greet
* inform
   - utter_ask_location
* inform{"location":"London"}
   - slot{"location": "London"}
   - action_weather
* goodbye
   - utter_goodbye

## story_002
* greet
   - utter_greet
* inform{"location":"Paris"}
   - slot{"location": "Paris"}
   - action_weather
* goodbye
   - utter_goodbye

## story_003
* greet
   - utter_greet
* inform
   - utter_ask_location
* inform{"location":"Vilnius"}
   - slot{"location": "Vilnius"}
   - action_weather
* goodbye
   - utter_goodbye

## story_004
* greet
   - utter_greet
* inform{"location":"Italy"}
   - slot{"location": "Italy"}
   - action_weather
* goodbye
   - utter_goodbye

## story_005
* greet
   - utter_greet
* inform
   - utter_ask_location
* inform{"location":"Lithuania"}
   - slot{"location": "Lithuania"}
   - action_weather
* goodbye
   - utter_goodbye


## interactive_story_1
* greet{"greet": "hi"}
    - utter_greet

## interactive_story_1
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_weather
    - slot{"location": "noida"}

## interactive_story_1
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_weather
    - slot{"location": "delhi"}
* goodbye
    - utter_goodbye
