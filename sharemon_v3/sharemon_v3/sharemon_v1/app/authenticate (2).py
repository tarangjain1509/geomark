# import jwt
# import bcrypt
from unittest import result
import streamlit as st
# from datetime import datetime, timedelta
# import extra_streamlit_components as stx
# from snowflake.snowpark import Session

# from introspect import access_token_val_1, refresh_token_active
# from .hasher import Hasher
# from urllib.parse import urlencode,quote_plus
# import requests
# from .utils import generate_random_pw
# import streamlit.components.v1 as components

# from .oauth_test import authenticate

# from .exceptions import (
#     CredentialsError,
#     ResetError,
#     RegisterError,
#     ForgotError,
#     UpdateError,
# )

# _component_Login = components.declare_component(
#     "Login_component", url="http://localhost:3001/login"
# )


# class Authenticate:
#     def __init__(
#         self,
#         credentials: dict,
#         cookie_name: str,
#         key: str,
#         cookie_expiry_days: int = 30,
#         preauthorized: list = None,
#     ):  # type: ignore

#         self.credentials = credentials
#         self.credentials["usernames"] = {
#             key.lower(): value for key, value in credentials["usernames"].items()
#         }
#         self.cookie_name = cookie_name
#         self.key = key
#         self.cookie_expiry_days = cookie_expiry_days
#         self.preauthorized = preauthorized
#         self.cookie_manager = stx.CookieManager()

#         if "authentication_status" not in st.session_state:
#             st.session_state["authentication_status"] = None
#         if "username" not in st.session_state:
#             st.session_state["username"] = None
#         if "logout" not in st.session_state:
#             st.session_state["logout"] = None
#         if "account_name" not in st.session_state:
#             st.session_state["account_name"] = None
#         if "snow_session" not in st.session_state:
#             st.session_state["snow_session"] = None
#         if "active_session" not in st.session_state:
#             st.session_state["active_session"] = None
#         if "token_conn" not in st.session_state:
#             st.session_state["token_conn"] = None
#         if "params" not in st.session_state:
#             st.session_state["params"] = None

#     def _token_encode(self) -> str:
#         return jwt.encode(
#             {
#                 "account_name": st.session_state["account_name"],
#                 "params": st.session_state["params"],
#                 "username": st.session_state["username"],
#                 "exp_date": self.exp_date,
#             },
#             self.key,
#             algorithm="HS256",
#         )

#     def _token_decode(self) -> str:
#         try:
#             return jwt.decode(self.token, self.key, algorithms=["HS256"])  # type: ignore
#         except:
#             return False  # type: ignore

#     def _set_exp_date(self) -> str:
#         return (datetime.utcnow() + timedelta(days=self.cookie_expiry_days)).timestamp()  # type: ignore

#     def _check_pw(self) -> bool:
#         return bcrypt.checkpw(
#             self.password.encode(),
#             self.credentials["usernames"][self.username]["password"].encode(),
#         )

#     def _check_cookie(self):

#         self.token = self.cookie_manager.get(self.cookie_name)
#         if self.token is not None:
#             self.token = self._token_decode()
#             if self.token is not False:
#                 if not st.session_state["logout"]:
#                     if self.token["exp_date"] > datetime.utcnow().timestamp():  # type: ignore
#                         if "account_name" in self.token:
#                             st.session_state["account_name"] = self.token["account_name"]  # type: ignore
#                             st.session_state["username"] = self.token["username"]  # type: ignore
#                             st.session_state["params"] = self.token["params"]  # type: ignore
#                             st.session_state[
#                                 "active_session"
#                             ] = Session.builder.configs(
#                                 st.session_state["params"]
#                             ).create()
#                             st.session_state["authentication_status"] = True

#     def _check_credentials(self, conn_params, inplace: bool = True) -> bool:  # type: ignore
#         """
#         Checks the validity of the entered credentials.

#         Parameters
#         ----------
#         inplace: bool
#             Inplace setting, True: authentication status will be stored in session state,
#             False: authentication status will be returned as bool.
#         Returns
#         -------
#         bool
#             Validity of entered credentials.
#         """
#         if self.username:
#             try:
#                 if self.password:
#                     st.session_state["active_session"] = Session.builder.configs(
#                         conn_params
#                     ).create()
#                     if inplace:
#                         # st.session_state['account_name'] = self.credentials['usernames'][self.username]['account_name']
#                         self.exp_date = self._set_exp_date()
#                         self.token = self._token_encode()
#                         self.cookie_manager.set(
#                             self.cookie_name,
#                             self.token,
#                             expires_at=datetime.now()
#                             + timedelta(days=self.cookie_expiry_days),
#                         )
#                         st.session_state["authentication_status"] = True
#                     else:
#                         return True
#                 elif self.password == 'token':
#                     pass
#                 else:
#                     if inplace:
#                         st.session_state["authentication_status"] = False
#                     else:
#                         return False
#             except Exception as e:
#                 print(e)
#         else:
#             if inplace:
#                 st.session_state["authentication_status"] = False
#             else:
#                 return False

#     def login_component(self, key=None):
#         Component_value = _component_Login(key=key, default=0)
#         return Component_value

#     def login(self, form_name: str, location: str = "main", token: str = '') -> tuple:
#         """
#         Creates a login widget.

#         Parameters
#         ----------
#         form_name: str
#             The rendered name of the login form.
#         location: str
#             The location of the login form i.e. main or sidebar.
#         Returns
#         -------
#         str
#             Name of the authenticated user.
#         bool
#             The status of authentication, None: no credentials entered,
#             False: incorrect credentials, True: correct credentials.
#         str
#             Username of the authenticated user.
#         """
#         if location not in ["main", "sidebar"]:
#             raise ValueError("Location must be one of 'main' or 'sidebar'")
#         if not st.session_state["authentication_status"]:
#             self._check_cookie()
#             if st.session_state["authentication_status"] != True:
#                 # if location == 'main':
#                 #     login_form = st.form('Login')
#                 # elif location == 'sidebar':
#                 #     login_form = st.sidebar.form('Login')
#                 # login_form.subheader(form_name)

#                 login_details = self.login_component()
                
#                 query_params = st.experimental_get_query_params()
#                 if login_details:
#                     self.account_name = login_details["creds"]["account"]
#                     self.username = login_details["creds"]["username"]
#                     self.password = login_details["creds"]["password"]

                   
#                     conn_params = {
#                         "account": self.account_name,
#                         "user": self.username,
#                         "password": self.password,
#                         "database": "ACCELERATOR_DB",
#                         "schema": "RBAC",
#                         "warehouse" :"NEW_WH"
#                     }
                    
#                     st.session_state["params"] = conn_params
#                     self._check_credentials(conn_params)

#                 elif query_params and (query_params["code"])[0]!=None :
#                     # def _make_request():
#                     #     def read_authcode():
#                     #         c=query_params["code"]
#                     #         return c

#                     #     token_url = "https://cs71725.ap-south-1.aws.snowflakecomputing.com/oauth/token-request"
#                     #     headers = {
#                     #         u'Authorization': u'Basic Mm0vNTlIbzVaVkRuWXIyNGQ3L0l2ODhhMW04PTpxMUZ2QXdzSHdQSmtodytLaXM0ZnNWL0RFeExTWi9JejFBck1wbTV5ZzFNPQ==',
#                     #         u'content-type': u'application/x-www-form-urlencoded'
#                     #     }
#                     #     payload = {
#                     #         'grant_type': 'authorization_code',
#                     #         'redirect_uri': "http://localhost:8501",
#                     #         'client_id': '2m/59Ho5ZVDnYr24d7/Iv88a1m8=',
#                     #         'code': read_authcode()
#                     #     }
                    
#                     #     result = urlencode(payload, quote_via=quote_plus)
#                     #     r = requests.post(token_url,headers=headers,data=result)
#                     #     return r.json()["access_token"]

#                     #     if r.status_code == 200:
#                     #         return r.json()["access_token"]
#                     #     else:
#                     #         print(f'''
                    
#                     #     Request failed
#                     #     {r}

#                     #     {code}
                        
#                     #     ''')
#                     #         return f'Failed request with error code {r.status_code}'

#                     # token=_make_request()

#                     # if st.session_state["authentication_status"]:
#                     # if access_token_val_1()!="NONE":
#                     st.session_state["active_session"] = authenticate()
#                     st.session_state["authentication_status"] = True

#                     self.account_name = 'cs71725.ap-south-1.aws'
#                     self.username = 'SSO_User'
#                     self.password = 'token'

#                     conn_params = {
#                         "account": 'cs71725.ap-south-1.aws',
#                         "user": 'SSO_User',
#                         "token":token,
#                         "database": "ACCELERATOR_DB",
#                         "schema": 'RBAC',
#                         "authenticator":'oauth',
#                         "warehouse":'NEW_WH'
#                         }
#                     st.session_state["params"] = conn_params
#                     # else: 
#                     #     print("LOGOUT")
                    
#                     # self._check_credentials(conn_params)
                    

#         return (
#             st.session_state["authentication_status"],
#             st.session_state["active_session"],
#         )

#     def logout(self, button_name: str, location: str = "main"):
#         """
#         Creates a logout button.

#         Parameters
#         ----------
#         button_name: str
#             The rendered name of the logout button.
#         location: str
#             The location of the logout button i.e. main or sidebar.
#         """
#         if location not in ["main", "sidebar"]:
#             raise ValueError("Location must be one of 'main' or 'sidebar'")
#         if location == "main":
#             # if st.button(button_name):
#             self.cookie_manager.delete(self.cookie_name)
#             st.session_state["logout"] = True
#             st.session_state["account_name"] = None
#             st.session_state["username"] = None
#             st.session_state["authentication_status"] = None
#         elif location == "sidebar":
#             # if st.sidebar.button(button_name):
#             self.cookie_manager.delete(self.cookie_name)
#             st.session_state["logout"] = True
#             st.session_state["account_name"] = None
#             st.session_state["username"] = None
#             st.session_state["authentication_status"] = None
 

#     def _update_password(self, username: str, password: str):
#         """
#         Updates credentials dictionary with user's reset hashed password.

#         Parameters
#         ----------
#         username: str
#             The username of the user to update the password for.
#         password: str
#             The updated plain text password.
#         """
#         self.credentials["usernames"][username]["password"] = Hasher(
#             [password]
#         ).generate()[0]

#     def reset_password(
#         self, username: str, form_name: str, location: str = "main"
#     ) -> bool:
#         """
#         Creates a password reset widget.

#         Parameters
#         ----------
#         username: str
#             The username of the user to reset the password for.
#         form_name: str
#             The rendered name of the password reset form.
#         location: str
#             The location of the password reset form i.e. main or sidebar.
#         Returns
#         -------
#         str
#             The status of resetting the password.
#         """
#         if location not in ["main", "sidebar"]:
#             raise ValueError("Location must be one of 'main' or 'sidebar'")
#         if location == "main":
#             reset_password_form = st.form("Reset password")
#         elif location == "sidebar":
#             reset_password_form = st.sidebar.form("Reset password")

#         reset_password_form.subheader(form_name)
#         self.username = username.lower()
#         self.password = reset_password_form.text_input(
#             "Current password", type="password"
#         )
#         new_password = reset_password_form.text_input("New password", type="password")
#         new_password_repeat = reset_password_form.text_input(
#             "Repeat password", type="password"
#         )

#         if reset_password_form.form_submit_button("Reset"):
#             if self._check_credentials(inplace=False):
#                 if len(new_password) > 0:
#                     if new_password == new_password_repeat:
#                         if self.password != new_password:
#                             self._update_password(self.username, new_password)
#                             return True
#                         else:
#                             raise ResetError("New and current passwords are the same")
#                     else:
#                         raise ResetError("Passwords do not match")
#                 else:
#                     raise ResetError("No new password provided")
#             else:
#                 raise CredentialsError

#     def _register_credentials(
#         self,
#         username: str,
#         account_name: str,
#         password: str,
#         email: str,
#         preauthorization: bool,
#     ):
#         """
#         Adds to credentials dictionary the new user's information.

#         Parameters
#         ----------
#         username: str
#             The username of the new user.
#         name: str
#             The name of the new user.
#         password: str
#             The password of the new user.
#         email: str
#             The email of the new user.
#         preauthorization: bool
#             The pre-authorization requirement, True: user must be pre-authorized to register,
#             False: any user can register.
#         """
#         self.credentials["usernames"][username] = {
#             "account_name": name,
#             "password": Hasher([password]).generate()[0],
#             "email": email,
#         }
#         if preauthorization:
#             self.preauthorized["emails"].remove(email)

#     def register_user(
#         self, form_name: str, location: str = "main", preauthorization=True
#     ) -> bool:
#         """
#         Creates a password reset widget.

#         Parameters
#         ----------
#         form_name: str
#             The rendered name of the password reset form.
#         location: str
#             The location of the password reset form i.e. main or sidebar.
#         preauthorization: bool
#             The pre-authorization requirement, True: user must be pre-authorized to register,
#             False: any user can register.
#         Returns
#         -------
#         bool
#             The status of registering the new user, True: user registered successfully.
#         """
#         if not self.preauthorized:
#             raise ValueError("Pre-authorization argument must not be None")
#         if location not in ["main", "sidebar"]:
#             raise ValueError("Location must be one of 'main' or 'sidebar'")
#         if location == "main":
#             register_user_form = st.form("Register user")
#         elif location == "sidebar":
#             register_user_form = st.sidebar.form("Register user")

#         register_user_form.subheader(form_name)
#         new_email = register_user_form.text_input("Email")
#         new_username = register_user_form.text_input("Username").lower()
#         new_account_name = register_user_form.text_input("account_name")
#         new_password = register_user_form.text_input("Password", type="password")
#         new_password_repeat = register_user_form.text_input(
#             "Repeat password", type="password"
#         )

#         if register_user_form.form_submit_button("Register"):
#             if (
#                 len(new_email)
#                 and len(new_username)
#                 and len(new_account_name)
#                 and len(new_password) > 0
#             ):
#                 if new_username not in self.credentials["usernames"]:
#                     if new_password == new_password_repeat:
#                         if preauthorization:
#                             if new_email in self.preauthorized["emails"]:
#                                 self._register_credentials(
#                                     new_username,
#                                     new_account_name,
#                                     new_password,
#                                     new_email,
#                                     preauthorization,
#                                 )
#                                 return True
#                             else:
#                                 raise RegisterError(
#                                     "User not pre-authorized to register"
#                                 )
#                         else:
#                             self._register_credentials(
#                                 new_username,
#                                 new_account_name,
#                                 new_password,
#                                 new_email,
#                                 preauthorization,
#                             )
#                             return True
#                     else:
#                         raise RegisterError("Passwords do not match")
#                 else:
#                     raise RegisterError("Username already taken")
#             else:
#                 raise RegisterError(
#                     "Please enter an email, username, name, and password"
#                 )

#     def _set_random_password(self, username: str) -> str:
#         """
#         Updates credentials dictionary with user's hashed random password.

#         Parameters
#         ----------
#         username: str
#             Username of user to set random password for.
#         Returns
#         -------
#         str
#             New plain text password that should be transferred to user securely.
#         """
#         self.random_password = generate_random_pw()
#         self.credentials["usernames"][username]["password"] = Hasher(
#             [self.random_password]
#         ).generate()[0]
#         return self.random_password

#     def forgot_password(self, form_name: str, location: str = "main") -> tuple:
#         """
#         Creates a forgot password widget.

#         Parameters
#         ----------
#         form_name: str
#             The rendered name of the forgot password form.
#         location: str
#             The location of the forgot password form i.e. main or sidebar.
#         Returns
#         -------
#         str
#             Username associated with forgotten password.
#         str
#             Email associated with forgotten password.
#         str
#             New plain text password that should be transferred to user securely.
#         """
#         if location not in ["main", "sidebar"]:
#             raise ValueError("Location must be one of 'main' or 'sidebar'")
#         if location == "main":
#             forgot_password_form = st.form("Forgot password")
#         elif location == "sidebar":
#             forgot_password_form = st.sidebar.form("Forgot password")

#         forgot_password_form.subheader(form_name)
#         username = forgot_password_form.text_input("Username").lower()

#         if forgot_password_form.form_submit_button("Submit"):
#             if len(username) > 0:
#                 if username in self.credentials["usernames"]:
#                     return (
#                         username,
#                         self.credentials["usernames"][username]["email"],
#                         self._set_random_password(username),
#                     )
#                 else:
#                     return False, None, None
#             else:
#                 raise ForgotError("Username not provided")
#         return None, None, None

#     def _get_username(self, key: str, value: str) -> str:
#         """
#         Retrieves username based on a provided entry.

#         Parameters
#         ----------
#         key: str
#             Name of the credential to query i.e. "email".
#         value: str
#             Value of the queried credential i.e. "jsmith@gmail.com".
#         Returns
#         -------
#         str
#             Username associated with given key, value pair i.e. "jsmith".
#         """
#         for username, entries in self.credentials["usernames"].items():
#             if entries[key] == value:
#                 return username
#         return False

#     def forgot_username(self, form_name: str, location: str = "main") -> tuple:
#         """
#         Creates a forgot username widget.

#         Parameters
#         ----------
#         form_name: str
#             The rendered name of the forgot username form.
#         location: str
#             The location of the forgot username form i.e. main or sidebar.
#         Returns
#         -------
#         str
#             Forgotten username that should be transferred to user securely.
#         str
#             Email associated with forgotten username.
#         """
#         if location not in ["main", "sidebar"]:
#             raise ValueError("Location must be one of 'main' or 'sidebar'")
#         if location == "main":
#             forgot_username_form = st.form("Forgot username")
#         elif location == "sidebar":
#             forgot_username_form = st.sidebar.form("Forgot username")

#         forgot_username_form.subheader(form_name)
#         email = forgot_username_form.text_input("Email")

#         if forgot_username_form.form_submit_button("Submit"):
#             if len(email) > 0:
#                 return self._get_username("email", email), email
#             else:
#                 raise ForgotError("Email not provided")
#         return None, email

#     def _update_entry(self, username: str, key: str, value: str):
#         """
#         Updates credentials dictionary with user's updated entry.

#         Parameters
#         ----------
#         username: str
#             The username of the user to update the entry for.
#         key: str
#             The updated entry key i.e. "email".
#         value: str
#             The updated entry value i.e. "jsmith@gmail.com".
#         """
#         self.credentials["usernames"][username][key] = value

#     def update_user_details(
#         self, username: str, form_name: str, location: str = "main"
#     ) -> bool:
#         """
#         Creates a update user details widget.

#         Parameters
#         ----------
#         username: str
#             The username of the user to update user details for.
#         form_name: str
#             The rendered name of the update user details form.
#         location: str
#             The location of the update user details form i.e. main or sidebar.
#         Returns
#         -------
#         str
#             The status of updating user details.
#         """
#         if location not in ["main", "sidebar"]:
#             raise ValueError("Location must be one of 'main' or 'sidebar'")
#         if location == "main":
#             update_user_details_form = st.form("Update user details")
#         elif location == "sidebar":
#             update_user_details_form = st.sidebar.form("Update user details")

#         update_user_details_form.subheader(form_name)
#         self.username = username.lower()
#         field = update_user_details_form.selectbox(
#             "Field", ["account_name", "Email"]
#         ).lower()
#         new_value = update_user_details_form.text_input("New value")

#         if update_user_details_form.form_submit_button("Update"):
#             if len(new_value) > 0:
#                 if new_value != self.credentials["usernames"][self.username][field]:
#                     self._update_entry(self.username, field, new_value)
#                     if field == "account_name":
#                         st.session_state["account_name"] = new_value
#                         self.exp_date = self._set_exp_date()
#                         self.token = self._token_encode()
#                         self.cookie_manager.set(
#                             self.cookie_name,
#                             self.token,
#                             expires_at=datetime.now()
#                             + timedelta(days=self.cookie_expiry_days),
#                         )
#                     return True
#                 else:
#                     raise UpdateError("New and current values are the same")
#             if len(new_value) == 0:
#                 raise UpdateError("New value not provided")



########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
# from snowflake.snowpark.session import Session
# from snowflake.snowpark.functions import avg, sum, col,lit
# import streamlit as st
# import pandas as pd
# connection_params = {
#      "account": 'qx82888.ap-south-1',
#      "user": 'KRUSHIK.R.NALLAMILLI@KIPI.BI',
#      "token":'eyJraWQiOiI2eFNxRk1YNm9rZG1MXzRvLXpmNV9IcE9CM2JFTHBDTUdwelBvbENLd2hrIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULlk1TWtTNmVaSGp5UUFPZ2ZUTTdhZkRHNXlIOHBpcnRRemptckxaLURDOGsub2FyYzQ4eDdnZ1JWMWJZSFU2OTYiLCJpc3MiOiJodHRwczovL3RyaWFsLTMwOTIyOTEub2t0YS5jb20vb2F1dGgyL2F1czJxd3B5YmpDV2x1UXFKNjk3IiwiYXVkIjoiaHR0cHM6Ly9xeDgyODg4LmFwLXNvdXRoLTEuYXdzLnNub3dmbGFrZWNvbXB1dGluZy5jb20vIiwiaWF0IjoxNjY3MjE0MzAwLCJleHAiOjE2NjczMDA3MDAsImNpZCI6IjBvYTJxd3B5eHg5bVhqekNSNjk3IiwidWlkIjoiMDB1MnF2dHB0MzRub1hlYWU2OTciLCJzY3AiOlsib2ZmbGluZV9hY2Nlc3MiLCJzZXNzaW9uOnJvbGUtYW55Il0sImF1dGhfdGltZSI6MTY2NzIxNDE1OCwic3ViIjoia3J1c2hpay5yLm5hbGxhbWlsbGlAa2lwaS5iaSJ9.zy_nRjdLrLcjNfvZ9hM2VlVuJ50JOushVZ6GwBo4BZc_GLZ8DIdQPH7Ra_MsS8Hflkq-wEsBjUac7DJOcvV5VPH88opJRJHAwm-hEQAeu6pAswQ6cwFyW1ccek3DSQwP4dScDkSxbwNF0ptKa5K4Z6z3Gz3s9AxFCA0oc_N0WuxvpoedtXHu_b4ipmpmgM0ELPv18v-I7ylpAC_QhSdL3tjwLdwEDKA5551H1EJs988XM7MFo7b4veoqjzvLYv6CKcXiFLAlKCzs5phV_6PDXm--hLrqjfVodSG3ahB0q7rLg4XyMTjBkPnQp68Yyhx6dnluVGw-fFxHINGWohY2Ug',
#      "database": "PETS",
#      "schema": 'PUBLIC',
#      "authenticator":'oauth',
#      "warehouse":'compute_wh'
#      }
# session = Session.builder.configs(connection_params).create()
# print(session.sql('select current_warehouse(), current_database(), current_schema()').collect())
# s=session.sql('select * from dummay_table_1').collect()
# st.write(s)

############################################################################################
import snowflake.connector
import pandas as pd
ctx = snowflake.connector.connect(
   user="KRUSHIK.R.NALLAMILLI@KIPI.BI",#login name
   account="qx82888.ap-south-1",
   authenticator="oauth",
   token="eyJraWQiOiI2eFNxRk1YNm9rZG1MXzRvLXpmNV9IcE9CM2JFTHBDTUdwelBvbENLd2hrIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULnVhN2dWZWtYOGhDR1UyRDJKTnpJbXlEQlJwY2pheTdrUV9QNmVZY2pySWMub2FyY2I5YmpuVnBETmVMZ042OTYiLCJpc3MiOiJodHRwczovL3RyaWFsLTMwOTIyOTEub2t0YS5jb20vb2F1dGgyL2F1czJxd3B5YmpDV2x1UXFKNjk3IiwiYXVkIjoiaHR0cHM6Ly9xeDgyODg4LmFwLXNvdXRoLTEuYXdzLnNub3dmbGFrZWNvbXB1dGluZy5jb20iLCJpYXQiOjE2Njc0NjU3MjksImV4cCI6MTY2NzU1MjEyOSwiY2lkIjoiMG9hMnF3cHl4eDltWGp6Q1I2OTciLCJ1aWQiOiIwMHUycXZ0cHQzNG5vWGVhZTY5NyIsInNjcCI6WyJvZmZsaW5lX2FjY2VzcyIsInNlc3Npb246cm9sZS1hbnkiXSwiYXV0aF90aW1lIjoxNjY3NDY1NzE3LCJzdWIiOiJrcnVzaGlrLnIubmFsbGFtaWxsaUBraXBpLmJpIn0.uflLBeoeme7nPbCGbChuRJUF2AHHOnAFl8DcyCdWusZtgBnLc0WBTHMTqIcpyAnFE1dV5op1FgTvzdxcv7k4g_Kl5AXwUdyUR9bNSPINb438dCwdTSuM1cbkYSQwBVo6Lnp6Ik3dv6dApe1gFqrJIXLbhgVvRSoohP1XRcjt5Wn01qhtzds02f2JEeGvgKdhThk3zxjag_hIPFJB_XHA6tz5rFia5JYdemuYmqigYcG7Y-Qmjqo9gfqAEpWe81mCRjJWIlnF5Kurw0OuSwSARJC5PfE-HAgOsmCjy5bsM7hiN4ou5E5WLEeu4NS8pjH1Ls0E1Q2od9mLgazV5yRLBg",
   #token="Y5NyIsInNjcCI6WyJvZmZsaW5lX2FjY2VzcyIsInNlc3Npb246cm9sZS1hbnkiXSwiYXV0aF90aW1lIjoxNjY3MjE0MTU4LCJzdWIiOiJrcnVzaGlrLnIubmFsbGFtaWxsaUBraXBpLmJpIn0.JHTnJcc68d-Jexr5c8C223nT2320XP9TBtnCo7fmpcgIMtnaBqHYntuknlvP0rJ-HY7QXELIZHaAkcOp5nYzXdm5nnq5jkvJfXOmtwqRsH1A0yXpeo65FdtvoFKslLHDFwt9OG3xktNywEvrG-WdUG3LQCToPuPcMxJfrLIpxghIpGmcOSSUY8Azo6mmA1lei4QQBOHuUNurj3iKRdWuiXvK_F-e1VV2T8UNrzRfAR6tQwagluParI-9PMwuGxMjWK9eD39eCcr3FOyQlQkSXERNEdMoLx8Glwbe7kZz0Xf--tz3wQBJU0x2gcIFU7cGYQj2gkcThh8XcdGTKipyQA",
   warehouse="compute_wh",
   database="PETS",
   schema="PUBLIC"
)
# st.session_state.conn=ctx.cursor()
st.session_state.conn=ctx
print(st.session_state.conn)
# ctx.cursor().execute("use role accountadmin")
#sql='''select * from dummay_table_1'''
# df1=st.session_state.conn.execute("create database d_11")
# results = st.session_state.conn.fetchall()
from definitions import *
results=run_query("show roles;")
print(results)







