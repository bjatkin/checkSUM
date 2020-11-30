# checkSUM
This is an HCI artifact which was created for CS 656 Interactive Software Systems

# Building the project
Now that we are using webpack, we can auto-generate the bundle.js file.
Simply run 

`npm run build` 

in the top level checkSUM directory in order to recomplie the main.js file.

# Viewing the project
The project runs using a django server. 
You can start the development server by running 

`python manage.py runserver 8080`.

The various endpoints for this project can then be found at [127.0.0.1:8080/checkSUM/home](https://127.0.0.1:8080/checkSUM/home)
The mysite directory contains all the django files for the web project.
The checkSUM directory contains all the django files for the web app.
In order to add new endpoints to this application you'll likely want to edit the checkSUM/urls.py file and the checkSUM/views.py files.
These files contains the http handlers and handler functions repectively.

A fake Youtube page shows what API calls to checkSUM by third parties would look like. To run go to [127.0.0.1:8080/checkSUM/home?verify_demo=true](https://127.0.0.1:8080/checkSUM/home?verify_demo=true)

