# WeatherApplication
This is my weather application which work from the cmd. I've installed all packages required into the venv folder.

All what you need to enter in the virtual environment with command : ./venv/scripts/activate
And right after start weather.py with: python weather.py

All done! You can see weather in you region

My application takes your coordinates like lattitude and longitude which depended by one http request, then it goes to openweatherAPI and takes your current weather from the
closest weatherstation and finally formatter takes all necessary options.

Resaults of the programm lie in the history.json

This is the main module which connect all program, I was trying to understand how does typing works, it's taken me about an half an hour to write this application 
