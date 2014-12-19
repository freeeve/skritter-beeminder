skritter-beeminder
==================

Sorry for the lack of documentation... I'm using this myself. 
Properly configured, you can make a similar script to run every day at ~3AM to update your skritter progress on beeminder.
Feel free to use it--you'll need to: 

* set up a new account on skritter for the API use
* create environment variables with the proper stuff (see top of the python file)
* update URLs to match your user and goal
* create a cron job that runs this at 3AM or so (probably make a script to set the environment variables along with it)
