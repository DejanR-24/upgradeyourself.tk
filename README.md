# Upgrade yourself

This project should represent the psychologist's office, 
the client has options for registration, login, logout, 
seeing the schedule of the chosen psychologist and making an appointment. 

Setup:

The first thing to do is to clone the repository:
```
$ git clone https://github.com/DejanR-24/upgrade_yourself.git
$ cd upgrade_yourself
```
Create a virtual environment to install dependencies in and activate it:
```
$ python3.9 -m venv .venv
$ source .venv/bin/activate
```
Then install the dependencies:
```
(env)$ pip3 install -r requirements.txt
```
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by venv

Once pip has finished downloading the dependencies migrate db and load data in it:
```
(env)$python3.9 manage.py migrate
(env)$python3.9 manage.py loaddata db.json
(env)$ python3.9 manage.py runserver
```
```
login for admin is: dejan 
password:1234
```
### ER diagram of the project 
![Upgrade_youself_ER](https://user-images.githubusercontent.com/67160398/153058665-a00eb640-d4cd-40a8-8068-c6fd4761aec5.png)
