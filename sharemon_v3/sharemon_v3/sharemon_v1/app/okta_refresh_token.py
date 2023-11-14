#from tkinter import EXCEPTION
import streamlit as st
import json
import requests
import urllib
from urllib.parse import urlencode,quote_plus
from snowflake.snowpark.session import Session
import pandas as pd
# import schedule
import time
import snowflake.connector

from introspect import refresh_token_active
def access_token_val():
    path = r".\save.json"
    with open(path, 'r') as openfile:
        json_object = json.load(openfile)
        # print(json_object["access_token"])
    return json_object["access_token"]
def refresh_token_val():
    path = r".\save.json"
    with open(path, 'r') as openfile:
        json_object = json.load(openfile)
        # print(json_object["refresh_token"])
    return json_object["refresh_token"]
def token_refresh():
    token_url = "https://trial-3092291.okta.com/oauth2/aus2qwpybjCWluQqJ697/v1/token"
    headers = {
        u'Authorization': u'Basic MG9hMnF3cHl4eDltWGp6Q1I2OTc6b1kwZVRBWmtrTnlZUmp3RV9FNC1DR3ZTQkxpWUY2QXdEdlJNWEg0RQ==',
        u'content-type': u'application/x-www-form-urlencoded'
    }
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token':refresh_token_val()
    }
    result = urlencode(payload, quote_via=quote_plus)
    r = requests.post(token_url,headers=headers,data=result)
    new_token=r.json()["access_token"]
    with open("save.json", "r") as jsonFile:
        data = json.load(jsonFile)

        data["access_token"] = new_token
        # json_object = json.dumps(k, indent=5)

        with open("save.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    print(new_token)
    return new_token
def authenticate_1():
    if refresh_token_active()==True:
        
        connection_params = {
            "account": 'qx82888.ap-south-1.aws',
            "user": "krushik.r.nallamilli@kipi.bi",
            "token":token_refresh(),
            "database": "PETS",
            "schema": 'PUBLIC',
            "authenticator":'oauth',
            "warehouse":'COMPUTE_WH'
            }
        session = Session.builder.configs(connection_params).create()
        return session
