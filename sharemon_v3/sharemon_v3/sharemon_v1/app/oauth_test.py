from numpy import save
import streamlit as st
import json
import requests
import urllib
from definitions import *
from urllib.parse import urlencode,quote_plus
from snowflake.snowpark.session import Session
import pandas as pd
# from __init__ import *
# from . import authenticate_1

def read_authcode():
        my_query_params = st.experimental_get_query_params()
        # st.write(my_query_params)
        c=(my_query_params["code"])[0]
        # print(c)
        return ((my_query_params["code"])[0]) 

def _make_request():
    token_endpoint = "https://trial-3092291.okta.com/oauth2/aus2qwpybjCWluQqJ697/v1/token"
    headers = {
        u'Authorization': u'Basic MG9hMnF3cHl4eDltWGp6Q1I2OTc6b1kwZVRBWmtrTnlZUmp3RV9FNC1DR3ZTQkxpWUY2QXdEdlJNWEg0RQ==',
        u'content-type': u'application/x-www-form-urlencoded'
    }
    payload = {
        'grant_type': 'authorization_code',
        'redirect_uri': "http://ec2-13-233-174-134.ap-south-1.compute.amazonaws.com/Login",
        # 'client_id': '2m/59Ho5ZVDnYr24d7/Iv88a1m8=',
        'code': read_authcode()
    }
    result = urlencode(payload, quote_via=quote_plus)
    r = requests.post(token_endpoint,headers=headers,data=result)
    # print(f'''
    
    # {r.json()}
    
    
    # ''')
    k=r.json()
    json_object = json.dumps(k, indent=5)
    with open("save.json", "w") as outfile:
        outfile.write(json_object)
    print("hima",r.json()["access_token"],r.json()["refresh_token"])
    return r.json()["access_token"], r.json()["refresh_token"]
def authenticate():
   
    access_token_1, refresh_token_1=_make_request()
    print(access_token_1)
    # connection_params = {
    #     "account": 'qx82888.ap-south-1.aws',
    #     "user": "krushik.r.nallamilli@kipi.bi",
    #     "token":access_token_1,
    #     "database": "PETS",
    #     "schema": 'PUBLIC',
    #     "authenticator":'oauth',
    #     "warehouse":'COMPUTE_WH'
    #     }
    ctx = snowflake.connector.connect(
    user="KRUSHIK.R.NALLAMILLI@KIPI.BI",#login name
    account="qx82888.ap-south-1",
    authenticator="oauth",
    token=access_token_1,
    warehouse="compute_wh",
    database="PETS",
    schema="PUBLIC"
    )
    # session = Session.builder.configs(connection_params).create()
    st.session_state.conn=ctx
    print("session",st.session_state.conn)
    return st.session_state.conn
