# KREDIT Messanger Bot

## Introduction
### Getting Started
Boradcasting promotion message to all user who used to chat with Kredit facebook

### Features
## 1.0.0
* Boradcasting promotion message to all user who used to chat with Kredit facebook page

### Built With
* Python
* Oracle
* Facebook API

### Prerequisites
What things you need to have before run this project

* Python 2.7
* pm2
* Python pip
* Oracle Client

## Installation

### Install dependencies
* Run command `pip install -r requirements.txt`

### Change datasource connection
* Go to `config.py` then find `SQLALCHEMY_DATABASE_URI` and change database url

### Change port listener
* For webhook API go to `api\bankingbot_api.py` then find `PORT = int(os.environ.get('SERVER_PORT', xxxx))` and change `xxxx` to port that you want to run
* For Portal go to `bankingbot_webportal.py` then find `PORT = int(os.environ.get('SERVER_PORT', xxxx))` and change `xxxx` to port that you want to run


## Running and tests
* For webhook API run command `pm2 start bankingbot_webportal.py`
* For Portal run command `pm2 start api/bankingbot_api.py`
 

## Dialogflow
Visit link https://github.com/dialogflow/dialogflow-python-client-v2

### How to train your Bot
#### File Template
* Copy file `example.xlsx` from directory `banking-bot\ai\ml\example.xlxs`

#### Import to Dialogflow
* Run command `python banking-bot\ai\ml\import_data.py --file "xlsx_file_path"`




