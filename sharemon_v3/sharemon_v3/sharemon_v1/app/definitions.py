from pickle import APPEND
import streamlit as st
import pandas as pd
import snowflake.connector
from streamlit_option_menu import option_menu
from PIL import Image
import base64,time
from tokenize import single_quoted
#from streamlit_autorefresh import st_autorefresh
from cProfile import run
from json import *
import hydralit_components as hc
import plotly.express as px
import plotly.graph_objects as go
import json
import pickle
from pathlib import Path
from operator import le
import streamlit_authenticator  as stauth
import webbrowser
import numpy as np
from introspect import *
from okta_refresh_token import *
import streamlit.components.v1 as components
#set background image

if 'load_state_monitor' not in st.session_state:
    st.session_state.load_state_monitor=False
if 'load_state_reader_setup' not in st.session_state:
    st.session_state.load_state_reader_setup=False

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
 
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

@st.experimental_singleton(suppress_st_warning=True)
def init_reader(username,password,reader_account_name):
    return snowflake.connector.connect(user=f"{username}",password=f"{password}",account=f"{reader_account_name}")


# conn=''
# Initialize connection.
# Uses st.experimental_singleton to only run once.
# @st.experimental_singleton
# def init_connection():
#     return snowflake.connector.connect(**st.secrets["snowflake"])
# conn = init_connection()


# if 'username' not in st.session_state:
#     st.session_state.username=None
# if 'password' not in st.session_state:    
#     st.session_state.password= None
# if 'url' not in st.session_state:
#     st.session_state.url=None# 
if 'conn' not in st.session_state:
    st.session_state.conn=None

# @st.cache(persist=True)
#@st.experimental_singleton(suppress_st_warning=True)
def dynamic_connection(username,password,url):
    print("inside if")     
    st.session_state.conn=snowflake.connector.connect(user=f"{username}",password=f"{password}",account=f"{url}")
    return  st.session_state.conn

# def snowflake_login(username,password,url):
#     print("password=",password)
#     st.session_state.username=username
#     st.session_state.password=password
#     st.session_state.url=url
#     conn=dynamic_connection() 


   

# log=None

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
# @st.experimental_memo(ttl=600)
@st.cache(suppress_st_warning=True)
def run_query(query):
    url_parameters=st.experimental_get_query_params()
    if url_parameters:
        try:
            if access_token_active()==True:
                if st.session_state.conn:
                    with st.session_state.conn.cursor() as cur:
                        cur.execute(query)
                        return cur.fetchall()
            else:
                print("access token expired")
                if refresh_token_active()==True:
                    st.session_state.conn = authenticate_1()
                    with st.session_state.conn.cursor() as cur:
                        cur.execute(query)
                        return cur.fetchall()
                    print("access token refreshed")
                else:
                    print("refresh token expired")
                    # authenticator.logout('Button', "main")
        except Exception as e:
            print(e)
            return {'success': False}
    else:
        with st.session_state.conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()
        
    


        
def beautify(db):
    special_char = '@_!#$%^&*()<>?/\|}{~:;.[]'
    out_list = [''.join(filter(lambda i: i not in special_char, string)) for string in db]
    return out_list
def beautify2(db):
    special_char = '@_!#$%^&*()<>?/\|}{~:;.[]'
    out_list = [','.join(filter(lambda i: i not in special_char, string)) for string in db]
    return out_list
def removedoublequote(db):
    replaced_string = db.replace('"', "")
    splited_string=replaced_string.split(':')
    return splited_string[0]

def split_string(string):
    list_string = string.split(',')     
    return list_string
def listbeautifytostr(lst):
    # lst=['a','b','c']
    # print("Original list",lst)
    new_lst=(','.join(lst))
    return(new_lst)

def submitbutton():
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #0099FF;
        color:#ffffff;
    }
    div.stButton > button:hover {
        background-color:  #006400;
        color:#ffffff;
        }
    </style>""", unsafe_allow_html=True)

def newbutton():
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #B3D943;
        color:#ffffff;
        border-radius: 5px;
        visibility: visible;
    }
    div.stButton > button:active {
        background-color: #000000;
        color:#fffff;
        border-color: #000000;
        border-radius: 5px;
        visibility: visible;
        }
    div.stButton > button:focus:not(:active){
        background-color: #B3D943;
        color:#ffffff;
        border-radius: 5px;
        visibility: visible;
    }
    div.stButton > button:hover {
        background-color:  #000000;
        color:#ffffff;
        border: 1px solid #FFFFFF;
        border-radius: 5px;
        }
    </style>""", unsafe_allow_html=True)
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
def build_markup_for_logo(
    png_file,
    background_position="100% -350%",
    margin_top="1%",
    image_width="60%",
    image_height="",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )
def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )


def udfsep(sentence):
    x=sentence.split("RETURN" or "return")
    return(x)




def run_custom_code():
    
    print("Entered runcode")
    # st.write("Entered runcode")
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
         	padding-top: 0rem;
           	padding-bottom: 0rem;
        }
        .heading{
         	font-size: 30px;
         }
        .subheading{
         	font-size: 20px;
         }
         .paragraph{
            font-size: 18px;
          }
          button#signinbutton{
            background-color: #B3D943;
            height: 45px;
            width: 100%;
            color:#000000;
            border-radius: 5px;
            visibility: visible;
        }
        button#signinbutton:hover {
            background-color: #000000;
            color:#FFFFFF;
            border: 1px solid #FFFFFF;
            border-radius: 5px;    
        }
        /* input code */
    input#snowflake_Usernameinput::placeholder {
        color: #757575;
    }
    input#snowflake_Passwordinput::placeholder {
        color: #757575;
    }
    input#snowflake_URLinput::placeholder {
        color: #757575;
    }
    input#snowflake_Usernameinput{
        height: 45px;
        background-color: #EEEEEE;
        color: #000000;
        placeholder: "someone@kipi.com";
        border-radius: 5px;
        caret-color: #000000;
    }
    input#snowflake_URLinput{
        height: 45px;
        background-color: #EEEEEE;
        color: #000000;
        placeholder: "acme-marketing_test_account";
        border-radius: 5px;
        caret-color: #000000;
    }
    input#snowflake_Passwordinput{
        height: 45px;
        background-color: #EEEEEE;
        color: #000000;
        placeholder: "**********";
        border-radius: 5px;
        caret-color: #000000;
    }
    /*card*/
    div#authcardholder{
        background-color: #1D1C21; 
        margin-left: auto;
        margin-right: auto;
        padding: 10px 30px 0 30px;
        border-radius: 15px;
        flex: 20%;
    }
    /*card helper*/
    p#cardhelper_authentication{
        height: 0;
        width: 0;
    }
        </style>""", unsafe_allow_html=True)
    components.html("""

    <script id="jquery" src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script id="customscript">
    const page = window.parent.document;
    $( document ).ready(function() {    
        
        $( page ).find('button').each(function( index ) {
            switch($(this).text()) {
                case 'Sign in':
                    console.log('sign in button');
                    $(this).attr({"id": "signinbutton", "visibility": "hidden"});
                    break;
                default:
                    //$(this).attr("id", "button");
                    console.log('Not defined');
                    break;
            }
        });
        
        function run_card_holder(ref){
            const columndiv = ref.closest("div[data-testid='column']");
            columndiv.attr({"id": "authcardholder"});
        }
        run_card_holder($( page ).find('p#cardhelper_authentication'));

        $( page ).find('input').each(function( index ) {

            switch($(this).attr('aria-label')) {
                case 'snowflake_Username':
                    $(this).attr({"id": "snowflake_Usernameinput", "placeholder": "someone@kipi.bi"});
                    //console.log('username');
                    break;
                case 'snowflake_URL':
                    $(this).attr({"id": "snowflake_URLinput", "placeholder": "acme-marketing_test_account"});
                    //console.log('password');
                    break;
                case 'snowflake_Password':
                    $(this).attr({"id": "snowflake_Passwordinput", "placeholder": "***************", "type": "password"});
                    //console.log('password');
                    break;
                default:
                    //$(this).attr("id", "input");
                    //console.log($(this).attr('aria-label'));
                    break;
            }

        });

    });
    </script>
    """,
        height=0,
        width=0,
    )
