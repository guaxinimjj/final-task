##Introduction
###Purpose
-  web application for managing departments and employees.
###Specific requirements
##External interface requirements
- Static mockup version of the application in HTML format with hardcoded data.
- Include a four pages: departments.html, department.html, employees.html, and employee.html.
- Pages have to include hyperlinks to simulate application use cases.
##Functional requirements
- web service for storing data and reading from database.
- Should be able to deploy the web application on Gunicorn using command line.
- All public functions / methods on all levels should include unit tests.
- Debug information should be displayed at the debugging level in the console and in a separate file.
- display a list of departments and the average salary (calculated automatically) for these departments
- display a list of employees in the departments with an indication of the salary for each employee and 
a search field to search for employees born on a certain date or in the period between dates change 
(add / edit / delete) the above data
##Logical database requirement
- Create two tables: 
    - "department"
        - should store their names
    - "employee":
        - related department
        - employee name
        - date of birth
        - salary  
