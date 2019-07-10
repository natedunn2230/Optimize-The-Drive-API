# Road Trip Optimizer API
*Thanks to [rhiever](https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects/blob/master/optimal-road-trip/Computing%20the%20optimal%20road%20trip%20across%20the%20U.S..ipynb) for his open source software to greatly aid in the development of this software [© Randal S. Olson](http://www.randalolson.com/)* 
## Setup
**Note:** *This application is intended for development on ubuntu / linux systems* 

1. Create a *.env* file like *example.env* and fill out variable values.
2. Install virtualenv for a python virtual environment ([learn more](https://virtualenv.pypa.io/en/latest/)): `pip install virtualenv`
3. Inside the base directory, create a virtual environment: `virtualenv env --python=python3`
4. Start up the virtual environment: `source env/bin/activate`
5. Install python packages: `pip install -r requirements.txt`
6. Start the server in development mode: `python web/app.py`
## Releasing to Production
1. Install Heroku ([learn more](https://www.heroku.com/what)): `sudo snap install --classic heroku`
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