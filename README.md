[![Build Status](https://travis-ci.com/Araali1/iReporter-II.svg?branch=develop)](https://travis-ci.com/Araali1/iReporter-II) [![Coverage Status](https://coveralls.io/repos/github/Araali1/iReporter-II/badge.svg?branch=develop)](https://coveralls.io/github/Araali1/iReporter-II?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/6d0d460557f6377c13cb/maintainability)](https://codeclimate.com/github/Araali1/iReporter-II/maintainability)

# iReporter-II

iReporter-II is the backend of the iReporter_UI that is a platform for all citizens to report, and follow up corruption incidents, plus inform where change/improvement is needed.

## Overview
Corruption is a big hinderance to Africa’s development. In order to curb such acts, African countries could adobt the iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

This Api demostrates that a user can create, update or delete and retrieve redflag incidents that have been already created.

# How it works

A user can:

- Get all redflags 
- Get a particular redflag
- Edit the location a specific redflag
- Edit the comment of a specific redflag
- Delete a specific redflag

## API Description
iReporter API is implemented in flask, a python microframework.
The corresponding endpoints and their functionalities are described in the sample below

|Endpoint                                      | Function                          
|----------------------------------------------|----------------------------------------------
|POST /api/v1/redflags                         | adds a redflag and id auto increases
|GET /api/v1/redflags                          | retrieves all redflags created / posted
|GET /api/v1/redflags/1                        | retrives a speicific redflag e.g (with id "1")
|PATCH /api/v1/red-flags/1/location            | edit location of specific redflag e.g (with id 1)
|PATCH /api/v1/red-flags/1/comment             | edit comment of specific redflag e.g (with id 1)
|DELETE /api/v1/redflags/1                     | deletes a specific redflag e.g (with id 1)

This site is published at [Here for UI](https://Araali1.github.io/iReporter_UI/login.html)
The site's API is found [Here](https://aireporterii.herokuapp.com/api/v1/redflags)


When using the API to Create, an example of the input and output data for creating a redflag is shown below:

### Input

{

    "eventType": "redflag",
    
    "comment": "We are tired of this sht", 
    
    "createdBy": 4, 
    
    "location": "Kitgum"
    
}

### Output

{
    "data": {
    
        "CreatedOn": "Wed, 16 Jan 2019 00:00:00 GMT",
        
        "comment": "We are tired of this sht",
        
        "createdBy": 4,

        "eventType": "redflag",

        "id": 1,

        "location": "Kitgum",

        "status": "pending"
    },

    "message": "Created succesfully",

    "status": 201
}

NOTE:
* createdBy should always be an integer and is a required field

### Installation Instructions
To run the API, follow these steps:
* Clone this repository onto your computer
* Install python3 and postman
* Navigate to the repository root and create a virtual environment
```
$ cd iReporter-II
$ virtualenv venv
```
* Activate the virtual environment and install dependencies in requirements.txt
```
$ source venv/bin/activate
$ pip install -r requirements.txt
```
* Run the run.py script
```
$ python run.py
```
* Test the API endpoints using Postman

## Contributors
* Ali Nabende - *nabendeali@gmail.com*
