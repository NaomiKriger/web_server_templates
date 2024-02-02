# Welcome to the Web Server Templates!

## The App's Purpose
Web Server Templates is a Python Flask application that demonstrates how to use templates to render dynamic web pages. 
It includes several example templates that you can use as a starting point for your own web applications.

## Running the App Locally
### Steps:
1. Clone the repository `git clone https://github.com/NaomiKriger/web_server_templates.git`
2. Navigate to the project directory
3. Install the required dependencies: `pip install -r requirements.txt`
3. Run the app either via your IDE (run button) or using the command `python app.py`.
This will start the web server on port 5000. You can access the home page 
   by navigating to `http://localhost:5000` in your web browser.

## Running the App on Docker
### Steps:
1. Clone the repository `git clone https://github.com/NaomiKriger/web_server_templates.git`
2. Navigate to the project directory
3. Run the following commands:

`docker build -t <name:version> .` e.g. `docker build -t webapp:1.0 .`
Note the dot at the end of the command
   
`docker run -d -p <chosen_machine's_port:app's_port> <name:version> ` e.g. `docker run -d -p 5000:5000 webapp:1.0`

To stop the container run `docker stop <first 4 container's characters>`

## Usage examples
Here are several terminal commands you can run on this app:

`curl -X POST -H "Content-type: application/json" -d "{\"key_3\" : \"value_3\", \"key_4\" : \"value_4\"}" "http://127.0.0.1:5000/data"`

`curl -X DELETE http://127.0.0.1:5000/data/delete/key_3`

`curl "http://127.0.0.1:5000/data"`