import streamlit as st
import json
import requests
import urllib
from urllib.parse import urlencode,quote_plus
from snowflake.snowpark.session import Session
import pandas as pd
# import schedule
import time

def access_token_val_1():
    path="./save.json"
    #path = r"C:\Users\hp\Desktop\NIKHIL\APISERO\L&D\Sharemon_with_SSO\save.json"
    with open(path, 'r') as openfile:
        json_object = json.load(openfile)
        # print(json_object["access_token"])
    return json_object["access_token"]
def refresh_token_val_1():
    path="./save.json"
    #path = r"C:\Users\hp\Desktop\NIKHIL\APISERO\L&D\Sharemon_with_SSO\save.json"
    with open(path, 'r') as openfile:
        json_object = json.load(openfile)
        # print(json_object["refresh_token"])
    return json_object["refresh_token"]

# from okta_refresh_token import access_token_val, refresh_token_val

###to check the refresh token is active or expired###

def refresh_token_active():

    revocation_endpoint="https://trial-3092291.okta.com/oauth2/aus2qwpybjCWluQqJ697/v1/introspect"

    payload = { 
        'client_id': "0oa2qwpyxx9mXjzCR697",
        "client_secret": "oY0eTAZkkNyYRjwE_E4-CGvSBLiYF6AwDvRMXH4E",
        
        # 'token': "eyJraWQiOiJLTkx0R21HRGpQN09kQUxxbzQ5SHp3d1pFNjJIVWVxVTM4Q1BKNzRIUW5RIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULjlIRVI5QVVnY09qc0xUMXRQbkgzY1JnSXh6aGZVeFpTbERXQ3ZXLXprcjQub2FyYmYwZGl1R2gzRzl1MzY2OTYiLCJpc3MiOiJodHRwczovL3RyaWFsLTUzNzExNTkub2t0YS5jb20vb2F1dGgyL2F1czJqMDdyb2w4dTNMM04wNjk3IiwiYXVkIjoiaHR0cHM6Ly9jczcxNzI1LmFwLXNvdXRoLTEuYXdzLnNub3dmbGFrZWNvbXB1dGluZy5jb20iLCJpYXQiOjE2NjU5OTY5MzgsImV4cCI6MTY2NjA4MzMzOCwiY2lkIjoiMG9hMmowNW14cHdYWXc3ZmY2OTciLCJ1aWQiOiIwMHUyajA0eHF3QmhEM1liRzY5NyIsInNjcCI6WyJvZmZsaW5lX2FjY2VzcyIsInNlc3Npb246cm9sZS1hbnkiXSwiYXV0aF90aW1lIjoxNjY1OTkwMjgzLCJzdWIiOiJoaW1hLmIubmFybmlAa2lwaS5iaSJ9.mZAXWm1fcSuVT53U-GflxISeRJzN8cnccqVoy5TuECthkI2JPZv1LDOfDE4taYFJLG98_ppze-kP5vga2jQ0zBV-NDkpp8LbkG-C2xfonm7UcLZUI3liN3EneW0cuihOM2F__7CT4sW2vYQ5NXCclUEMQ0u3iIwtE2SeQQcVI62MJsJRg0X_zPp2r6hDwukBQTuoZlo42RgTVMn8X7djefjFMD9Qye3wlh5Zhw7brwqly4T2I-6XWwFyEsneyTJ5NDwo54lbfi11S0REjP9lumHXrMzIqTVsbutb1fivBd5MkQZda8asz9YHC2bDDgOYZby7sC5572dOuR1Wxyc-0w",
        # 'token_type_hint': 'access_token'
        'token':refresh_token_val_1(),#"KEjeU9N_lzup6O2U1wMZ8cP0r1MD4mIpmkhp4_3s7G0", 
        'token_type_hint': 'refresh_token'
        }

    headers = {
            # u'Authorization': u'Basic MG9hMmowNW14cHdYWXc3ZmY2OTc6TUttZk8zcTJPbTljd1MtMWJqd29SS3pNd2pOdE5ZMnNTTGtfUW1fbQ==',
            u'content-type': u'application/x-www-form-urlencoded'
        }
    result = urlencode(payload, quote_via=quote_plus)
    r = requests.post(revocation_endpoint,headers=headers,data=payload)
    print(r.json()['active'])
    return r.json()['active']

###to check the access token is active or expired###


def access_token_active():

    revocation_endpoint="https://trial-3092291.okta.com/oauth2/aus2qwpybjCWluQqJ697/v1/introspect"

    payload = { 
        'client_id': "0oa2qwpyxx9mXjzCR697",
        "client_secret": "oY0eTAZkkNyYRjwE_E4-CGvSBLiYF6AwDvRMXH4E",
        
        
        'token': access_token_val_1(),
        # 'token': "eyJraWQiOiJLTkx0R21HRGpQN09kQUxxbzQ5SHp3d1pFNjJIVWVxVTM4Q1BKNzRIUW5RIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULjlIRVI5QVVnY09qc0xUMXRQbkgzY1JnSXh6aGZVeFpTbERXQ3ZXLXprcjQub2FyYmYwZGl1R2gzRzl1MzY2OTYiLCJpc3MiOiJodHRwczovL3RyaWFsLTUzNzExNTkub2t0YS5jb20vb2F1dGgyL2F1czJqMDdyb2w4dTNMM04wNjk3IiwiYXVkIjoiaHR0cHM6Ly9jczcxNzI1LmFwLXNvdXRoLTEuYXdzLnNub3dmbGFrZWNvbXB1dGluZy5jb20iLCJpYXQiOjE2NjU5OTY5MzgsImV4cCI6MTY2NjA4MzMzOCwiY2lkIjoiMG9hMmowNW14cHdYWXc3ZmY2OTciLCJ1aWQiOiIwMHUyajA0eHF3QmhEM1liRzY5NyIsInNjcCI6WyJvZmZsaW5lX2FjY2VzcyIsInNlc3Npb246cm9sZS1hbnkiXSwiYXV0aF90aW1lIjoxNjY1OTkwMjgzLCJzdWIiOiJoaW1hLmIubmFybmlAa2lwaS5iaSJ9.mZAXWm1fcSuVT53U-GflxISeRJzN8cnccqVoy5TuECthkI2JPZv1LDOfDE4taYFJLG98_ppze-kP5vga2jQ0zBV-NDkpp8LbkG-C2xfonm7UcLZUI3liN3EneW0cuihOM2F__7CT4sW2vYQ5NXCclUEMQ0u3iIwtE2SeQQcVI62MJsJRg0X_zPp2r6hDwukBQTuoZlo42RgTVMn8X7djefjFMD9Qye3wlh5Zhw7brwqly4T2I-6XWwFyEsneyTJ5NDwo54lbfi11S0REjP9lumHXrMzIqTVsbutb1fivBd5MkQZda8asz9YHC2bDDgOYZby7sC5572dOuR1Wxyc-0w",
        'token_type_hint': 'access_token'
        }

    headers = {
           
            u'content-type': u'application/x-www-form-urlencoded'
        }
    result = urlencode(payload, quote_via=quote_plus)
    r = requests.post(revocation_endpoint,headers=headers,data=payload)
    print(r.json()['active'])
    return r.json()['active']

# access_token_active()
# refresh_token_active()

def revoke_refresh_token():
    revocation_endpoint="https://trial-3092291.okta.com/oauth2/aus2qwpybjCWluQqJ697/v1/revoke"
    payload = { 
        'client_id': "0oa2qwpyxx9mXjzCR697",
        "client_secret": "oY0eTAZkkNyYRjwE_E4-CGvSBLiYF6AwDvRMXH4E",
        
        'token': refresh_token_val_1(),#"5oV5D6MC_AdUNbH6ZN4sCAHhP9uEA7vlEJ7MRo5qRtQ",
        'token_type_hint': 'refresh_token'
        }

    headers = {
            # u'Authorization': u'Basic MG9hMmowNW14cHdYWXc3ZmY2OTc6TUttZk8zcTJPbTljd1MtMWJqd29SS3pNd2pOdE5ZMnNTTGtfUW1fbQ==',
            u'content-type': u'application/x-www-form-urlencoded',
            u"Accept": "application/json"
        }
    result = urlencode(payload, quote_via=quote_plus)
    r = requests.post(revocation_endpoint,headers=headers,data=result)
    print("refresh token revoked")
    
def revoke_access_token():
    revocation_endpoint="https://trial-3092291.okta.com/oauth2/aus2qwpybjCWluQqJ697/v1/revoke"

    payload = { 
        'client_id': "0oa2qwpyxx9mXjzCR697",
        "client_secret": "oY0eTAZkkNyYRjwE_E4-CGvSBLiYF6AwDvRMXH4E",
        
        'token':access_token_val_1(),# "eyJraWQiOiJLTkx0R21HRGpQN09kQUxxbzQ5SHp3d1pFNjJIVWVxVTM4Q1BKNzRIUW5RIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULjloaTdxRmJtWlgyNlFJSEtKUE01aGVINTdrMHV4MVlDTVQ4bHotMHYweWMub2FyYmZiYWFneVdPUWFPT1M2OTYiLCJpc3MiOiJodHRwczovL3RyaWFsLTUzNzExNTkub2t0YS5jb20vb2F1dGgyL2F1czJqMDdyb2w4dTNMM04wNjk3IiwiYXVkIjoiaHR0cHM6Ly9jczcxNzI1LmFwLXNvdXRoLTEuYXdzLnNub3dmbGFrZWNvbXB1dGluZy5jb20iLCJpYXQiOjE2NjYwMTE0NjcsImV4cCI6MTY2NjA5Nzg2NywiY2lkIjoiMG9hMmowNW14cHdYWXc3ZmY2OTciLCJ1aWQiOiIwMHUyajA0eHF3QmhEM1liRzY5NyIsInNjcCI6WyJvZmZsaW5lX2FjY2VzcyIsInByb2ZpbGUiLCJvcGVuaWQiLCJzZXNzaW9uOnJvbGUtYW55Il0sImF1dGhfdGltZSI6MTY2NTk5MDI4Mywic3ViIjoiaGltYS5iLm5hcm5pQGtpcGkuYmkifQ.nomi4skiiCuC9caeItx4YJXulGhiteVWDwt5cuTep8JepBu6n-tyPGvypgR2ZxHNMK7ayxkS2aapqjeM5Dy1uHpe_0zoZX708LAXv_Q8zDxJGJ5R5EBAMpSyTWmpH3PYv-XUOsp79Yo-yj3Q8sWmwkhE4fzPA2IrzBsH1dTA-8y7I6dpNLKE4uBzkFRo4DQtOx-TPrtM0mMCTQWBi8Y7qxogOIg_hbNcmyT7geEhnJ61XGeHE0LQOFyJHmbE6Km7hKV_SNeOTIfSwfc5sLKE2TOCQyOQvhaZvuyU7kY5sC431UJ1RciQNAEXwPA9Rl4Gtue3oytoKI_pVWI1TKloxw",
        'token_type_hint': 'access_token'
        }

    headers = {
            # u'Authorization': u'Basic MG9hMmowNW14cHdYWXc3ZmY2OTc6TUttZk8zcTJPbTljd1MtMWJqd29SS3pNd2pOdE5ZMnNTTGtfUW1fbQ==',
            u'content-type': u'application/x-www-form-urlencoded',
            u"Accept": "application/json"
        }
    result = urlencode(payload, quote_via=quote_plus)
    r = requests.post(revocation_endpoint,headers=headers,data=result)
    print("access token revoked")
# revoke_access_token()
# revoke_refresh_token()
