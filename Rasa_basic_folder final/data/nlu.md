## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thanks
- cool,thanks
- that's great
- amazing, thank you so much
- cheers
- good thank you

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- no,good bye
- no,thank you

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hi
- hi
- hello
- hey buddy
- hey dude
- hii dude
- hii bot
- hiiiii bottttttt
- hello, mister
- hello
- hello sweatheart
- Whats up my bot
- hello?
- hey, let's talk

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- [american](cuisine)
- [mexican](cuisine)
- show me some [South Indian](cuisine) restaurants
- show me nearest restaurants in [Agra](location)
- show me great [Italian](cuisine) restaurants in [Ahmedabad](location)
- please help me to find a restaurants in [Mumbai](location)
- show some great restaurants in [Allahabad](location)
- i am looking to search for [mexican](cuisine) restaurants in [Amritsar](location)
- find a restaurants for [Italian](cuisine)
- i am hungry looking for some great [South Indian](cuisine) food?
- can you help me to find restaurants in [Aurangabad](location)
- could you please show me restaurants in [Banglore](location)
- help me to find restaurants in [Bombay](location:Mumbai)
- show me restaurants in [Bengaluru](location:Banglore)
- suugest me a good restaurants in [dilli](location:New Delhi)
- show me few restaurants in [Bhopal](location)
- recomend me a [american](cuisine) places in [Bhubaneshwar](location)
- recomend a best restaurants in [Chandigarh](location)
- what is the good place to eat food in [Chennai](location)
- i want to eat [Italian](cuisine) food in [Coimbatore](location)
- [Faridabad](location)
- [Dehradun](location)
- [Gangtok](location)
- [Ghaziabad](location)
- help me to find a restaurant in [Goa](location)
- help me to find [North Indian](location) food in [Gurgaon](location)
- [Gurugram](location)
- [Guwahati](location)
- [mexican](cuisine) food in [Hyderabad](location)
- [Indore](location)
- okay, show me some best places to eat in [Jaipur](location)


## intent:send_email
- send me this information to [user.001@gmail.com](email)
- can you mail me to [adfa@gmail.com](email)
- please send this to [manojgadde13@gmail.com](email)
- yes ,this is my mail address [sdsfs@123.edu](email)
- [jddk.2jmd@kdl.co.in](email)
- please send this to [email.123@123.456.com](email)

## intent:budget_for_two
- [<300](budget)
- [>700](budget)
- [200](budget)
- [400](budget)
- [600](budget)
- Lesser than Rs. [300](budget)
- More than [700](budget)

    
## synonym:2
- two
- dho
- do

## synonym:4
- four
- chaar
- char

## synonym:Allahabad
- prayagraj
- prayagraj
- Prayagraj

## synonym:Amritsar
- amratsar
- Amrathsar
- Amratsar
- amrathshar

## synonym:Chandigarh
- cahndigarh
- chandighar
- Chandighar

## synonym:Chennai
- chennai
- chenai
- Madras
- madras

##synonym:Delhi
- delhi
- dilli
- New Delhi
- new delhi
- new dilli
- New Dilli
- newdilli
- newdelhi

## synonym:Hyderabad
- hyderabad
- cyderabadh
- secunderabadh
- Hyderabadh
- hyderabad

## synonym:Jamshedpur
- jamshedpur
- Jamsedpur
- jamsedpur

## synonym:Kolkata
- kolkata
- culcutta
- kolkattha
- culcuttha
- Kolkattha

## synonym:Lucknow
- lucknow
- Lakhanpur

## synonym:Mangalore
- mangalore
- mangalore
- mangaluru
- Mangaluru

## synonym:Mysore
- mysore
- mysore
- mysuru
- Mysuru

## synonym:Nashik
- nashik
- Nasik
- nasik

## synonym:Pondicherry
- pondicherry
- puducherry
- Puducherry

## synonym:Rajahmundry
- rajahmundry
- Rajahmundri
- rajahmundri
- Rajamundry
- rajamundry
- Rajamundri
- rajamundri

## synonym:Rourkela
- rourkela
- Raurkela
- raurkela

## synonym:Thiruvananthapuram
- thiruvananthapuram
- trivandrum
- Trivandrum
- Travancore
- travancore

## synonym:Vadodara
- vadodara
- Vadodra
- vadodra

## synonym:Visakhapatnam
- visakhapatnam
- Vizag
- vizag

## synonym:bangalore
- Bengaluru
- Bangaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym: vegetarian
- veggie
- vegg
- vegan

## regex:email
- ([\w.-]+)@(([[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.)|(([\w-]+.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(]?)

## synonym:greet
- hey[^\s]*
- hi[^\s]*

## synonym:pincode
- [0-9]{6}

## lookup:cities
- /.Data/cities.txt