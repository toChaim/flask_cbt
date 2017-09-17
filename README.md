# About this app:  
As we go through our lives thoughts automaticly come into our consciousness. Many of these are unpleasant, unhelpful, and untrue. We often just accept them because we thought them. Cognitive Behavioral Therapy (CBT) is one of the most studied and successful forms of therapy, it gets us to think critically about what we are saying to ourselves and associate new thoughts with these automatic thoughts.
My idea is to harness the ability of computer games to create associations between stimulus and response to install the new associations of CBT.

Come and Give it a try at https://flask-cbt.herokuapp.com

# Technologies used:  
* Flask  
* Postgres  
* Jquery with AJAX   
* The human mind.  
* The idea of Games and Gamefulness.

# Setup:
This project is not intended for users to setup their own game. Infact many of my stretch goals depend on haveing a large userbase.  
If you want to set up your own or you want to contribute to the code, here are the steps:  
1. Prereckwisits: Git, github account, Postgres, Python3, pip3, and virtualenv.  
2. Fork my github repository.  
3. Clone your github repository.  
4. In the terminal type 'createdb flask_cbt'. To crate the postgress database locally.  
5. In the terminal type 'mkvirtualenv flask_cbt'. To crate a virtual enviorment to isolate dependancies.  
6. In the terminal in the project root directory, type 'workon flask_cbt'. To enter the virtual enviorment.  
7. In the terminal in the project root directory, type 'pip3 install -r requirements.txt'. To install dependancies.  
8. In the terminal in the project root directory, type 'python3 manage.py db upgrade'. To update your local database to the schema for game.  
9. In the terminal in the project root directory, type 'python3 app.py'. To start the server.
10. Finnaly open your browser and type 'localhost:3000' and play.

# Goals:
* Finish Readme. Done.  
* Setup Schema. Done.  
* Get users working. Done.  
* Must have root route. Done.  
* Must Get working on heroku. Done.  
* Have some testing including security. Done.  
* 404 must return a code 404.  

# Next Steps:
* Finish css styling.  
* Save data when the player makes a selection.   
* Refactor schema to reflec what I learded from building this. Promps and Responses should be a many to many self join Thoughts table (id, Promp, Response, value) and matches should be a many to many of PrompResponses table.

# Stretch Goals:
* Add Special thoughts / kinds of thoughts, like counter eveidence, logic errors / stinking thinking, etc. 
* Improve start up process for new users. Start off with default prompts.
* Suggest thoughts that many other users use.
* Add data visualizations.
* Calculate peoples improvment.
* Addd A/B testing.

# Thanks:
* Jane McGonigal for changein how I think about games and what can be done with them.
	*  [Gaming can make a better world](https://www.ted.com/talks/jane_mcgonigal_gaming_can_make_a_better_world)  
	*  [Jane McGonigal: The game that can give you 10 extra years of life](https://www.ted.com/talks/jane_mcgonigal_the_game_that_can_give_you_10_extra_years_of_life)

# Tests:
Uniqe Prompts for each User.  
Uniqe Responses for each Prompt.  
No match lasting longer then five minutes.  
cascading delete.  

# A/B test:
Dose first person (I am handsome.) or second (You are handsome.) or even third (Hank is handsome.) or a mix work better for prompts?
Dose counter evidence work better than affermations?
Do question or statements work better as prompts?
