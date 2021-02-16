# Historical Stock Price Listing Web Application
This web application project demonstrate a Listing of all Historical Stock Price Items extracted from an external API. This project is built with Python (Django Framework). This application also has a pagination facility where each page containing 100 listing entries.

## Setup
1. Clone the repository
```sh
$ git clone https://github.com/jeet-khondker/historical-stock.git
$ cd historical-stock
```
2. Install and create a virtual environment and activate it
```sh
$ pip3 install virtualenv
$ virtualenv historicalstock-venv
$ source historicalstock-venv/bin/activate
```
3. Install the dependencies
```sh
(historicalstock-venv)$ pip3 install -r requirements.txt
```
Note the `(historicalstock-venv)` in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by `virtualenv`.

4. Navigate to https://financialmodelingprep.com/developer/docs/ to get your API Key. If you are not a registered user, please sign up and get the API Key.

5. Create a `.env` file in the root directory and paste the following code in the file.
```sh
API_KEY = "your-api-key"
```
6. Migrate the database
```sh
(historicalstock-venv)$ python manage.py migrate
```
7. Run the server
```sh
(historicalstock-venv)$ python manage.py runserver
```
8. Open `http://127.0.0.1:8000/` in the browser.

# Technology Used
Python (Django Framework), HTML5, CSS3

# Author
Jeet Z. H. Khondker, Full Stack Web Developer
