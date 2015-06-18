Nutritionix Challenge
=====================

A simple search application using the Nutritionix API. Built in Flask and Angular.js

#Installing

Create a python virtual environment in order to install the dependencies of the Flask application.

`virtualenv venv`

You may need to install virtualenv via `pip install virtualenv`

Activate the new virtualenv by calling

`source venv/bin/activate`

Finally install the depencies of the project specified in the `requirements.txt` file

`pip install -r requirements.txt`


#Running Application

To run the application, you first need to add your application id and application key to the file `app.py`. You can retrieve them from https://developer.nutritionix.com.

After adding the keys and saving the file, run the application locally using the command `python app.py`. This will start the server on `127.0.0.1:5000`. 

This application is also hosted on Heroku using the link https://desolate-fjord-2941.herokuapp.com/
