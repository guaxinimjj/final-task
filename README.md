# Department App
[![Build Status](https://travis-ci.com/guaxinimjj/final-task.svg?branch=master)](https://travis-ci.com/guaxinimjj/final-task)
[![Coverage Status](https://coveralls.io/repos/github/guaxinimjj/final-task/badge.svg?branch=master)](https://coveralls.io/github/guaxinimjj/final-task?branch=master)

Web application for managing departments and employees. Display a list of departments and the average salary. Display a 
list of employees in the departments, and a search field to search for employees born on a certain date or in the period
between dates change, or name.

##[Production](https://department-app-kv.herokuapp.com)

##Start:
#### Ensure docker is installed.
[Install Docker](https://docs.docker.com/compose/install/)
#### Run application
```
docker-compose build

docker-compose up
```
#### [LocalHost](http://localhost:5000/)

#### For test application:
```
make test
```
#### For pylint checks:
```
pylint checks
```