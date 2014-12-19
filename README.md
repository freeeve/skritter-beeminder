skritter-beeminder
==================

Sorry for the lack of documentation... I'm using this myself. 
Properly configured, you can make a similar script to run every day at ~3AM to update your skritter progress on beeminder.
Feel free to use it--you'll need to: 

* update the zapier URL to a "webhook post"-based zap, that updates beeminder with a "minutesStudied" field
* set up a new account on skritter for the API use
* create environment variables with the proper stuff (see top of the python file)
