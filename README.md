# langchain-py-js-tutorial
A small repo for a tutorial I wrote on using LangChain's python library from a JS app.

## Overview
This repo was created for a blog post I wrote on using the [python langchain library](https://python.langchain.com/en/latest/index.html) from a Javascript app. 
The code is organized in two folders. The flask server code lives in `langchain-flask-server` and the JS test file and data lives in `js-test`. 
The flask server has one POST endpoint that accepts json and a query, and then uses LangChain's pandas_dataframe_agent to answer the query. 

🔗 [Blog Post URL](https://medium.com/@michaelbranconier/use-the-python-langchain-library-in-a-javascript-application-bfbdbc8c59fe)

## Prerequisites
You must have the following installed on your computer:
- python
- pip
- virtualenv
- node version 17.5 or greater

## Installation
1. Clone the Repo
2. Create the virtual environment
```
python3 -m venv .venv
```
3. Activate the virtual environment
```
. .venv/bin/activate
```
4. Install the required packages:
```
pip install Flask
pip install pandas
pip install langchain
pip install python-dotenv
```

## Running the flask server
1. Open a new terminal window for the `langchain-flask-server` 
2. Run the server
```
flask run
```
You'll know it's working if you navigate to http://127.0.0.1:5000/ and see "I'm building something cool today!"

In order for the API to execute the langchain POST request, you'll have to create a `.env` file and add your OpenAI API key.

([more on python-dotenv](https://pypi.org/project/python-dotenv/))


## Using the API
1. Open a terminal window for the js test file
2. Run the code
```
node api-test
```

Replace the JSON data or update the query to see what the pandas_dataframe_agent can do! 



