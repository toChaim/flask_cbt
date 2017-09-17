# About this app:
As we go through our lives thoughts automatically come into our consciousness. Many of these are unpleasant, unhelpful, and untrue. We often just accept them because we thought them. Cognitive Behavioral Therapy (CBT) is one of the most studied and successful forms of therapy. It gets us to think critically about what we are saying to ourselves and associate new thoughts with our automatic thoughts. My idea is to harness the ability of computer games to reinforce connecting helpful responses to automatic thoughts.  
Come and give it a try at https://flask-cbt.herokuapp.com.  
# Technologies used:
Flask
* PostgreSQL  
* jQuery with AJAX  
* The human mind  
# Setup:
This project is not intended for users to setup their own game. In fact many of my stretch goals depend on having a large user base.  
1. Prerequisites: Git, Github account, PostgreSQL, Python3, pip3, and Virtualenv.  
2. Fork my Github repository.  
3. Clone your Github repository.  
4. In the terminal type “createdb flask_cbt”. This creates the Postgres database locally.  
5. In the terminal type “mkvirtualenv flask_cbt”. This creates a virtual environment to isolate dependencies.  
6. In the terminal go to the project root directory, type “workon flask_cbt”. This enters the virtual environment.  
7. In the terminal in the project root directory, type “pip3 install -r requirements.  txt”. This installs the dependencies.  
8. In the terminal in the project root directory, type “python3 manage.  py db upgrade”. This updates your local database to the schema for the game.  
9. In the terminal in the project root directory, type “python3 app.  py”. This starts the server. 
10. Finally open your browser and type “localhost:3000” in the URL bar and play.  
# Next Steps:
* Finish CSS styling.  
* Change game to save data when the player makes a selection.  
* Refactor schema to change Prompts and Responses into a Thoughts table. This allows  response to have a different values for different prompts. 
* Ensure that matches lasting longer than five minutes don’t get recorded as data.  
* Make sure cascading deletion works.  
* Add testing for all routes
* Add front end testing  

# Stretch Goals:
* Add Tags to thoughts table. This allows users to identify and explain categories of thoughts, for example counter evidence, logic errors, stinking thinking, etc. 
* Improve start up process for new users. Start off with default prompts.  
* Suggest thoughts that many other users use.  
* Allow users to share list of thoughts.  
* Add data visualizations.  
* Make website responsive.  
* Calculate user’s improvements.  
* Add A/B testing, for example to try and determine if questions or statements work better as prompts?  

# What were the challenges:
* Designing the database schema for the current requirements and to accommodate my stretch goals.  
* Getting all the Flask modules to work together.  
* Understanding what queries were being run and when by FlaskSQLAlchemy.  
* Writing tests that checked what I thought they did and what I wanted them to.  
* Making tests that are robust and should still be accurate for later versions. 

# What I learned:
* Flask and related modules.  
* Integration of Flask and AJAX calls.  
* That iteration works. Having a product made it much easier to see how to improve my schema.  
* How to adapt CRUD routeing to more complex projects. 
 
# Thanks:
* Jane McGonigal for changing how I think about games and what can be done with them.  
	* [Gaming can make a better world](https://www.ted.com/talks/jane_mcgonigal_gaming_can_make_a_better_world)  
	* [Jane McGonigal: The game that can give you 10 extra years of life](https://www.ted.com/talks/jane_mcgonigal_the_game_that_can_give_you_10_extra_years_of_life)   

