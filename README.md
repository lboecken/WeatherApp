#WeatherApp 

This is a Python, Postgres, Heroku App that sends out scheduled weather messages with the requested information by the user. 

It stores what information is required in a db that is checked every minute with a cron job. 
If the cron jobs finds a match, it will send this information to the python backend. First the weather information is retrieved from the openWeatherAPI.
Then the returning data is formatted to be sent over to Twilio which then sends out an SMS to the provided phone number. 
