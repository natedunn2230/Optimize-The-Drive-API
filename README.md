# Road Trip Optimizer API
*Thanks to [rhiever](https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects/blob/master/optimal-road-trip/Computing%20the%20optimal%20road%20trip%20across%20the%20U.S..ipynb) for his open source software to greatly aid in the development of this software [© Randal S. Olson](http://www.randalolson.com/)* 
## Running In Development
*Development is done with a Docker environment*
1. Download [Docker](https://www.docker.com/products/docker-desktop).
2. Sign up as a [Here Developer](https://developer.here.com/) and create a project to generate a Rest API key.
3. Sign up as a [LocationIQ Developer](https://locationiq.com/) and generate a Geocoding API Key.
4. Create *.dev.env* file in the root directory, referencing *example.env* (populate the newly acquired API keys).
5. Within the root directory, issue the Docker environment build command: `docker-compose build`
6. Run the Docker containers: `docker-compose up`
7. To stop the services: `ctl + c`
8. Alternatively, stopping and starting services can be done through the Docker Desktop application.
## Releasing to Production
Release to production can be done one of two ways: Through the Heroku CLI or their webiste.
### Through Heroku CLI
1. Install Heroku CLI ([learn more](https://devcenter.heroku.com/articles/heroku-cli))
2. Login to Heroku: `heroku login`
3. Create Heroku Application: `heroku create <app-name>`
4. Add Redis-To-Go addon to application: `heroku addons:create redistogo:nano`
5. Add config vars (same that are in *.env*) on Heroku's Website. This can be found under your application's settings. Alternatively, you can add them on the [command line](https://devcenter.heroku.com/articles/config-vars) as well.
6. Release to Heroku
	* Create a git repo (if not done already): `git init`
	* Point repo to application: ` heroku git:remote -a <app-name>`
	* Stage changes for release: `git add .`
	* release to heroku: `git push heroku master`
### Through Heroku Website
1. Register with Heroku and create a new app.
2. Under Resources / Addons, find Redis To Go and add that to your app.
3. Under Settings / Config vars, enter your production config variables (same as those found in .dev.env, but with values replaced for production).
4. Under Deploy tab / Deployment method, select Github.
5. Search for your app's repository and click connect. You can now choose to enable automatic deployments or deploy manually based off your branch of choice.