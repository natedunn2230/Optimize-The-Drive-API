# Road Trip Optimizer API
*Thanks to [rhiever](https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects/blob/master/optimal-road-trip/Computing%20the%20optimal%20road%20trip%20across%20the%20U.S..ipynb) for his open source software to greatly aid in the development of this software [© Randal S. Olson](http://www.randalolson.com/)* 
## Setup
**Note:** This application is intended for development on Unix based systems

1. Install virtualenv for a python virtual environment ([learn more](https://virtualenv.pypa.io/en/latest/)): `pip install virtualenv`
2. Inside the base directory, create a virtual environment: `virtualenv venv --python=python3 (or virtualenv venv for Mac)`
3. Start up the virtual environment: `source venv/bin/activate (to deactivate environment: deactivate)`
4. Install python packages: `pip install -r requirements.txt`
5. Create *.dev.env* file in parent directory, referencing *example.env*
6. If on Mac, run this (there are issues with process forking): `export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES`
7. Start the redis server: `redis-server --port <port_num>`
8. Start Worker: `python worker.py`
9. Start Flask server: `python app.py`
## Releasing to Production
1. Install Heroku CLI ([learn more](https://devcenter.heroku.com/articles/heroku-cli))
2. Login to Heroku: `heroku login`
3. Create Heroku Application: `heroku create <app-name>`
4. Add config vars (same that are in *.env*) on Heroku's Website. This can be found under your application's settings. Alternatively, you can add them on the [command line](https://devcenter.heroku.com/articles/config-vars) as well.
5. Release to Heroku
	* Create a git repo (if not done already): `git init`
	* Point repo to application: ` heroku git:remote -a <app-name>`
	* Stage changes for release: `git add .`
	* release to heroku: `git push heroku master`
## Changes Made to Original Work
## Licensing 
This software is made available under the [Creative Commons Attribution](https://creativecommons.org/licenses/by/4.0/) liscense.