# Planets API [![Build Status](https://travis-ci.org/victorprs/planetsapi.svg?branch=master)](https://travis-ci.org/victorprs/planetsapi)  [![Coverage Status](https://coveralls.io/repos/github/victorprs/planetsapi/badge.svg?branch=master)](https://coveralls.io/github/victorprs/planetsapi?branch=master)

Star Wars planets API

## Features

This is a Star Wars Planets API made with Python and it handles planets operations such as:

- Create a planet with its name, terrain and climate properties
- List all the created planets
- Search for a planet by its name
- Search for a planet by its id
- Deletes a planet from the database
- Shows in how many films a planet has appeared in*

## Requirements

A running MongoDB Server 3.6.2

## Installing/Running

### Environment Variables

There are some environment variables necessary to be configured if you run any configuration of MongoDb Server different from the default one

- DB_HOST represents the URL of the running mongodb server
- DB_PORT represents the port of the running mongodb server
- DB_NAME represents the name of the database in the mongodb server

### Installing

To install, run the following command:

```bash
pip install -r requirements.txt
```

### Running
To run, use the following command:

```bash
FLASK_APP=server.py flask run
```

## Usage

GET /planets - Lists all the planets in the database

GET /planets?name=<planet_name> - Filter planets search based in the planet name given as querystring

GET /planets?name=<object_id> - Filter planets search based in the document ObjectId given as querystring

POST /planets - Creates the given planet. It accepts JSON format, e.g.: { "name": "Tatooine", "climate": "arid", "terrain": "desert" }

DELETE /planets/<object_id> - Delete the planet which has the given document ObjectId

## Dependencies

Made with:

- Python 3.6.4
- MongoDB 3.6.2
- Pip 9.0.1
- Flask 0.12.2
- Flask-RESTful 0.36.6
- Requests 2.18.4
- Coveralls 1.2.0
- Pylint 1.8.2
- PyMongo 3.6.0
- Pytest 3.4.1

## Code quality

To ensure code quality, I used Pylint to a certain extent and followed an style guide to mantain readability and cohesion. Pytest and Coveralls were used to ensure code coverage by the implemented tests. 

___
###### *planets that doesn't exist within the swapi.co API return a -1 count

