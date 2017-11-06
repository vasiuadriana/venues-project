### Description

A service that decides what venues the users should go to based on food and drink preferences.

### Installation Steps
*Notes*: 
- the installation steps assume that `python >=3.5` and `pip >=9` are installed on the machine. Pip 8.+ should work to but the installation was done using `pip 9.0.1`.
- the installation can be done globally on the system but the steps below assume best practices for python development, so it makes use of virtual environments

Steps:
- install `virtualev` and `virtualenvwrapper` (this depends on OS distribution but usually the installation is straight forward using pip)
- `mkvirtualenv --python=python3 venues`
- `workon venues`
- go to the directory where the project was cloned
- `pip install -r venues/requirements.txt`

### Running the app

`python -m venues.run`

The app is using the default flask development server and it will run on: `http://127.0.0.1:5000/` which is also the entrypoint
for the venues selector service.

### Running the tests
`nosetests`

### Design and implementation considerations

- the app uses flask framework because is minimal and serves the purpose of exposing the service
- for a very minimal design improvement it uses the library `Flask-Bootstrap`
- the state of the app is maintained in memory using a pattern of loading the feed data at startup. I am using the concept 
of Flask Application Context
- the input for this app is considered to be json so no trailing comas are allowed. Also, the assumption is that the json has a specific format and is a location which is known to the app, 
otherwise the app will fail at startup. In a production application you would probably have a mechanism that validates and publishes this data accordingly.
- for simplicity all the libraries needed for this app to be run and tested are in the same file: `requirements.txt` but in a production
app you would separate those dependencies so that you don't install testing libraries on the production server
- the design is very simple: a flask view, a selector service that accesses directly the data in memory and no business models.
As soon as more requirements are added you would probably have User, Venue objects and a data access layer. 
For now, the core python objects suffice to represent the data.
- for simplicity the templates are doing minimal rendering logic so further improvements would be to actually separate that into a separate 
renderer. The more logic you add, the more unreadable the templates would become. Also, in a production app you would add functional tests
for the actual service, and that would cover all the rendering logic. 
