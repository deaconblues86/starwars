# Starwars
Prerequisites
- MySQL (8.0.15)
- Python 3.6

# Description
Two test scripts are included in this repo to demonstrate how one may pull data from an API, in this the Star Wars API (swapi), load it to a local MySQL database, and perfrom some basic operations on it.  Detailed descriptions of both scripts can be found below.

# Installation
Before running any of the scripts, please ensure you meet the prerequisites listed above.  Both MySQL Community Edition and Python 3.6 are available for free at the links below:
- MySQL: https://dev.mysql.com/downloads/mysql/
- Python: https://www.python.org/downloads/release/python-360/
Note that this project was developed on a Windows 10 box so you're installation process may be slightly different -- mostly referring to installing python when using Linux.

# task_one.py
1. GET 15 random characters and the names of the films they have been in using Python.
2. Insert into MySQL (SQL database schema(s) for any table(s) created are included)
3. Characters, by film, received will be written to the console

# task_two.py
1. Pulls data from the films endpoint for the movie A New Hope
2. Replaces the data for each of the endpoints listed in the JSON object received from the API request (e.g. for all the character endpoints, data will be pulled for each and inserted into the JSON object)
2a. A New Hope has character, planet, starship, vehicle, and species data that will be retrieved and replaced.
3. All metric heights and weights of each character will be converted to standard units.
4. All cross referencing material from the data being replaced will be removed (e.g. Luke Skywalker, when pulledwould have unwanted cross referencing urls such as films, species, vehicles, and spaceships)
5. Lastly, the dictionary that's been created will be writtem to a JSON file locally named task_two.json.
