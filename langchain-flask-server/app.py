from flask import Flask, jsonify, request
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>I’m building something cool today!</p>"

@app.route("/queryJson", methods=['POST'])
def queryJson():
    req = request.get_json()
    data = req['data']
    query = req['query']
    df = pd.DataFrame.from_dict(data)
    agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)
    result = agent.run(query)
    return jsonify(result)