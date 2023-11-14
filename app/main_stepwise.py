from definitions import *
from oauth_test import *
from introspect import *
import validators
from cProfile import run
from pickle import APPEND
import streamlit as st
import snowflake.connector
import base64
from datetime import date
from select import select
st.set_page_config(page_title="Learn more", layout="wide")


if 'conn' not in st.session_state:
        st.session_state.conn=None


#hide streamlit ui
st.markdown("""
            <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                }
            </style>
            """, unsafe_allow_html=True)
####################################            
#Login Page start
placeholder = st.empty()

# @st.cache(suppress_st_warning=True)
def Login_Pannel(): 
    with st.container():
        title, empty1, empty2, login_title = st.columns([4, 1, 1, 2.5], gap="large")
    
        # with title:
        #     st.title("SHAREMON")
        with title:
            logoimage = Image.open('./data/KIPI_Logo_Design.webp')
            st.image(logoimage)
        with login_title:
            
            pass

    with st.container():
        div1, div2 = st.columns(2, gap="medium")
        with div1:
            with st.container():
                st.write('')
                st.write('')
                h2 = st.markdown('''     
                <h3 class="heading" style=" margin-top: 20px; padding: 5px 5px 0 5px;">ShareMon allows you to create and monitor shares through UI</h3>
                
        
                <p class="paragraph" style="font-size: 16px;margin: 0 30px 0 0; padding: 25px 25px 0 5px; text-align: justify;">ShareMon is an Interactive web application used to automate and ease the processes of Snowflake's Direct Data Sharing and monitoring. Its UI allows you to Create & Maintain shares without having to write a single line of code. This no-code Application is developed to ease the process of writing long & repeated SQL codes on Snowflake to Share Data with your consumers. It uses Streamlit and Snowflake connectors on the back end to interpret the user's choices.
                </p>
        
                <p class="paragraph" style="font-size: 16px;margin: 0 30px 0 0; padding: 25px 25px 0 5px; text-align: justify;">ShareMon allows you to create Snowflake shares, add consumers to them, create a reader account, monitor shares, and delete (Drop Shares) them. As of now, the focus is on direct data sharing from the provider's perspective.
                </p>
        
                
                ''', unsafe_allow_html=True)
        with div2:
            with st.container():
                # Login_Pannel()
                # run_custom_code()
                # placeholder = st.empty()

                my_query_params = st.experimental_get_query_params()
                set_background('./data/images.jpg')
                add_logo('./data/logo.png')

                # with placeholder.container():
                st.markdown('''
            
                <p id="cardhelper_authentication" style="font-size:16px; visibility: hidden;">CardHelper</p>

                ''', unsafe_allow_html=True)
                s2 = st.markdown('''
                
                <p style="font-size:16px;">Snowflake URL</p>

                ''', unsafe_allow_html=True)
                Url=st.text_input("snowflake_URL",label_visibility="collapsed")
                s2 = st.markdown('''
                
                <p style="font-size:16px;">Snowflake username</p>

                ''', unsafe_allow_html=True)
                Username=st.text_input("snowflake_Username",label_visibility="collapsed")
                s2 = st.markdown('''
                
                <p style="font-size:16px;">Snowflake password</p>

                ''', unsafe_allow_html=True)
                Password=st.text_input("snowflake_Password",label_visibility="collapsed")
                print(Url)
                if st.button("Sign in"):
                    print("Start URl",Url)
                    if Url[0:8]=="https://":
                        if Url[0:11]!="https://app":
                            print("2")
                            a=Url.split('.snowflake')
                            l=a[0]
                            Url=l[8:]
                        elif 'app.snowflake.com' in Url.split('/'):
                            b=Url.split('.snowflake')
                            a=Url.split('/')
                            h=a[3].split('.')
                            if (len(h)==1):
                                l=b[1]
                                k=l.split('/')
                                Url=k[2]
                            else:
                                l=a[4]
                                m=a[3]
                                Url=l+'.'+m
                    else:
                        Url=Url
                    print("End Url",Url)
                    print("Username=",Username)
                    print("Password=",Password)
                    try:
                        conn=dynamic_connection(Username,Password,Url)
                        st.success("Logged in Successfully!")
                    except :
                        print("entered except")
                        st.error("Please check the URL, Username and Password")
                    

                # st.markdown("""<hr style="padding-top: 0rem;padding-bottom: 0rem;">""",unsafe_allow_html=True)                
                url = 'https://trial-3092291.okta.com/oauth2/aus2qwpybjCWluQqJ697/v1/authorize?response_type=code&client_id=0oa2qwpyxx9mXjzCR697&state=sharemon&scope=session%3Arole-any%20offline_access&redirect_uri=http%3A%2F%2F192.168.1.41%3A8501%2FLogin'
                st.markdown("""<centre><a style="padding-left:35%;" href="https://trial-3092291.okta.com/oauth2/aus2qwpybjCWluQqJ697/v1/authorize?response_type=code&client_id=0oa2qwpyxx9mXjzCR697&state=sharemon&scope=session%3Arole-any%20offline_access&redirect_uri=http%3A%2F%2Fec2-13-233-174-134.ap-south-1.compute.amazonaws.com%2FLogin"><p style="color:white;background-color: transparent;padding: 7px 12px;border-radius: 4px;border: none;font-size: 16px">Sign in with SSO</p></a></centre>""",unsafe_allow_html=True)
                if my_query_params:
                    st.session_state.okta=authenticate()
                    st.success("Logged in Successfully")

# with st.container():


# Login Page end
####################################
# Create shares page start
def Create_shares():
    st.session_state.load_state_add_consumers_reader=False
    st.markdown('''<style>
    .element.style{
        border: 1px solid #ffff;
    }
    </style>''',unsafe_allow_html=True)
    warehouse_creation_container=st.empty()
    with warehouse_creation_container.container():
    
        #set layout width to wide
        # st.set_page_config(page_title="Learn more", layout="wide")    
        
        #hide streamlit ui
        st.markdown("""
                    <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        header {visibility: hidden;}
                        .block-container {
                            padding-top: 0rem;
                            padding-bottom: 0rem;
                        }
                    </style>
                    """, unsafe_allow_html=True)

        
        submitbutton()
        newbutton()
        
        add_logo('./data/logo.png')
        
        st.session_state.load_state_reader_setup=False
        st.session_state.load_state_monitor=False
        if 'conn' not in st.session_state:
            st.session_state.conn=None
        if st.session_state.conn!=None:
            

            with hc.HyLoader('Connecting to Snowflake...',hc.Loaders.standard_loaders,index=5):
                time.sleep(2)
            


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
            



            # run_query("use warehouse compute_wh;")
            run_query("use secondary roles all;")
            run_query("use role SHAREMON_ADMIN;")
            # run_query("use warehouse compute_wh;")
            run_query("use warehouse SHAREMON_WH;")

           
            role=beautify(run_query("select current_role();"))
            print("role1=",(role[0]))            
            c="'"            
            if role[0]=="SHAREMON_ADMIN":
                pass
            else:
                st.warning("You don't have sharemon admin role")                
            if role[0]=="SHAREMON_ADMIN":         
                col5,col6=st.columns([1,1],gap="large")
                with col5:
                    run_query("show warehouses;")
                    warehouses=run_query("select \"name\" from table(result_scan(last_query_id()));")
                    beautiful_warehouses=(beautify(warehouses))
                    # beautiful_warehouses.insert(0, "select")
                    warehousesbox=st.selectbox("Select from the available warehouse ",(beautiful_warehouses))
                    if len(warehousesbox)>1 and 'select' not in warehousesbox:
                        run_query('use warehouse '+warehousesbox+';')

                # creating a warehouse start
                with col5: 
                    st.write("Do you want to create new warehouse? (Optional)")
                    with st.expander('Warehouse'):
                        wn=st.text_input("Warehouse name")
                        st.caption("Suggested name format: <PROJECT>_<ENV>_<BUSINESS_FUNCTION>")
                        st.caption("For Eg: kipi_Dev_Shares")
                        print(len(wn))
                        if wn.upper() in beautiful_warehouses:
                            # st.error(""+wn+" warehouse alredy exists")
                            pass
                        # elif wn.upper() !='':
                        #     st.success(""+wn+" name is available to use")
                        ws=["XSMALL","SMALL","MEDIUM","LARGE","XLARGE","XXLARGE","XXXLARGE","4XLARGE","5XLARGE","6XLARGE"]
                        #with col3:
                        WAREHOUSE_SIZE_BOX=st.selectbox("Select warehouse size",(ws))
                        if WAREHOUSE_SIZE_BOX=='4XLARGE':
                            WAREHOUSE_SIZE_BOX='X4LARGE'
                        elif WAREHOUSE_SIZE_BOX=='5XLARGE':
                            WAREHOUSE_SIZE_BOX='X5LARGE'
                        elif WAREHOUSE_SIZE_BOX=='6XLARGE':
                            WAREHOUSE_SIZE_BOX='X6LARGE'
                        timelist=['5','10','15','20','30','45','60',]
                        AUTO_SUSPEND_TIME_MIN=st.selectbox("Please enter suspend time in minutes",timelist)
                        AUTO_SUSPEND=int(AUTO_SUSPEND_TIME_MIN)*60
                        # st.write(AUTO_SUSPEND)
                        # print(AUTO_SUSPEND)
                        clusters_count=['1','2','3','4','5','6','7','8','9','10']
                        MIN_CLUSTER_COUNT = st.selectbox("Enter minimum clusters required",clusters_count)
                        MAX_CLUSTER_COUNT = st.selectbox("Enter maximum clusters required",clusters_count)
                        if MIN_CLUSTER_COUNT > MAX_CLUSTER_COUNT:
                            st.error("Minimum clusters required must be lessthan maximum clusters required")
                        SCALING_POLICY_list=["STANDARD","ECONOMY"]
                        SCALING_POLICY=st.selectbox("Select scaling policy size",(SCALING_POLICY_list))
                        AUTO_RESUME=st.radio("Auto resume",('TRUE', 'FALSE',))
                        # if wn.upper() not in beautiful_warehouses:
                        if st.button('Create warehouse',key="wh"):
                            if wn.upper() in beautiful_warehouses:
                                st.error(""+wn+" warehouse alredy exists")
                            else:
                            # CREATE WAREHOUSE njjii WITH WAREHOUSE_SIZE = 'XLARGE' WAREHOUSE_TYPE = 'STANDARD' AUTO_SUSPEND = 600 AUTO_RESUME = FALSE MIN_CLUSTER_COUNT = 1 MAX_CLUSTER_COUNT = 2 SCALING_POLICY = 'STANDARD';
                                rr=run_query("CREATE WAREHOUSE "+wn+" WITH WAREHOUSE_SIZE = '"+WAREHOUSE_SIZE_BOX+"' WAREHOUSE_TYPE = 'STANDARD' AUTO_SUSPEND ="+str(AUTO_SUSPEND)+" AUTO_RESUME = "+AUTO_RESUME+" MIN_CLUSTER_COUNT = "+MIN_CLUSTER_COUNT+" MAX_CLUSTER_COUNT = "+MAX_CLUSTER_COUNT+" SCALING_POLICY = '"+SCALING_POLICY+"';")
                                if rr:
                                    # beautiful_warehouses.append(wn)
                                    st.success("Warehouse created")     
                                    time.sleep(3)                              
                                    st.experimental_rerun()
                                
    create_share_container=st.empty()
    with create_share_container.container():    
                if len(warehousesbox)>1 and 'select' not in warehousesbox:
                    # creting a share Start
                    with col6:                                        
                        if "load_state_share" not in st.session_state:
                            st.session_state.load_state_share = True
                        # if 'no' in flag or nofil or st.session_state.load_state_share  :
                        if  st.session_state.load_state_share  :
                            with col6:
                                form = st.form(key='my_form',clear_on_submit=True)
                                Share_name= form.text_input(label='Share name')
                                
                                comment = form.text_area('Comment box (optional)',)

                                submit_button = form.form_submit_button(label='Submit')
                                if Share_name and submit_button:
                                    comment = c + comment + c
                                    create_share = run_query('create share '+Share_name+ ' Comment ='+comment+ ';')
                                    # success_msg = '<p style="font-family:sans-serif; color:Green; font-size: 16px;">Share '  +str(Share_name)+  ' successfully created.</p>'
                                    st.success('Share '  +str(Share_name)+  ' successfully created.')
                                    # st.markdown(success_msg, unsafe_allow_html=True)
                                elif not Share_name and submit_button:
                                    st.warning("Please Enter valid Share Name")


####################################
# Create shares page end
####################################
# Warehouse selection/creation start
####################################
def warehouse_creation():
    st.markdown("""
                <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    .block-container {
                        padding-top: 0rem;
                        padding-bottom: 0rem;
                    }
                </style>
                """, unsafe_allow_html=True)

    
    submitbutton()
    newbutton()
    
    add_logo('./data/logo.png')
    
    st.session_state.load_state_reader_setup=False
    st.session_state.load_state_monitor=False
    if 'conn' not in st.session_state:
        st.session_state.conn=None
    if st.session_state.conn!=None:
        

        with hc.HyLoader('Connecting to Snowflake...',hc.Loaders.standard_loaders,index=5):
            time.sleep(2)
        if 'warehousesbox' not in st.session_state:
            st.session_state.warehousesbox=None


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
        



        # run_query("use warehouse compute_wh;")
        run_query("use secondary roles all;")
        run_query("use role SHAREMON_ADMIN;")
        # run_query("use warehouse compute_wh;")
        run_query("use warehouse SHAREMON_WH;")


        st.write('Validating if your role has the right access to create share.')

        role=beautify(run_query("select current_role();"))
        print("role1=",(role[0]))

        c="'"

        if role[0]=="SHAREMON_ADMIN":
            st.write('Success!, Please proceed.')

        if role[0]=="SHAREMON_ADMIN":         
            col5,col6=st.columns([1,1],gap="large")
            with col5:
                run_query("show warehouses;")
                warehouses=run_query("select \"name\" from table(result_scan(last_query_id()));")
                beautiful_warehouses=(beautify(warehouses))
                beautiful_warehouses.insert(0, "select")
                st.session_state.warehousesbox=st.selectbox("Select from the available warehouse ",(beautiful_warehouses))
                if len(st.session_state.warehousesbox)>1 and 'select' not in st.session_state.warehousesbox:
                    run_query('use warehouse '+st.session_state.warehousesbox+';')

            # creating a warehouse start
            with col5: 
                st.write("Do you want to create new Warehouse? (Optional)")
                with st.expander('Warehouse'):
                    wn=st.text_input("Warehouse name")
                    st.caption("Suggested name format: <PROJECT>_<ENV>_<BUSINESS_FUNCTION>")
                    st.caption("For Eg: kipi_Dev_Shares")
                    print(len(wn))
                    if wn.upper() in beautiful_warehouses:
                        st.error(""+wn+" warehouse alredy exists")
                    elif wn.upper() !='':
                        st.success(""+wn+" name is available to use")
                    ws=["XSMALL","SMALL","MEDIUM","LARGE","XLARGE","XXLARGE","XXXLARGE","4XLARGE","5XLARGE","6XLARGE"]
                    #with col3:
                    WAREHOUSE_SIZE_BOX=st.selectbox("Select warehouse size",(ws))
                    if WAREHOUSE_SIZE_BOX=='4XLARGE':
                        WAREHOUSE_SIZE_BOX='X4LARGE'
                    elif WAREHOUSE_SIZE_BOX=='5XLARGE':
                        WAREHOUSE_SIZE_BOX='X5LARGE'
                    elif WAREHOUSE_SIZE_BOX=='6XLARGE':
                        WAREHOUSE_SIZE_BOX='X6LARGE'
                    timelist=['5','10','15','20','30','45','60',]
                    AUTO_SUSPEND_TIME_MIN=st.selectbox("Please enter suspend time in minutes",timelist)
                    AUTO_SUSPEND=int(AUTO_SUSPEND_TIME_MIN)*60
                    # st.write(AUTO_SUSPEND)
                    # print(AUTO_SUSPEND)
                    clusters_count=['1','2','3','4','5','6','7','8','9','10']
                    MIN_CLUSTER_COUNT = st.selectbox("Enter minimum clusters required",clusters_count)
                    MAX_CLUSTER_COUNT = st.selectbox("Enter maximum clusters required",clusters_count)
                    if MIN_CLUSTER_COUNT > MAX_CLUSTER_COUNT:
                        st.error("Minimum clusters required must be lessthan maximum clusters required")
                    SCALING_POLICY_list=["STANDARD","ECONOMY"]
                    SCALING_POLICY=st.selectbox("Select scaling policy size",(SCALING_POLICY_list))
                    AUTO_RESUME=st.radio("Auto resume",('TRUE', 'FALSE',))
                    if wn.upper() not in beautiful_warehouses:
                        if st.button('Create warehouse',key="wh"):
                    
                            # CREATE WAREHOUSE njjii WITH WAREHOUSE_SIZE = 'XLARGE' WAREHOUSE_TYPE = 'STANDARD' AUTO_SUSPEND = 600 AUTO_RESUME = FALSE MIN_CLUSTER_COUNT = 1 MAX_CLUSTER_COUNT = 2 SCALING_POLICY = 'STANDARD';
                            rr=run_query("CREATE WAREHOUSE "+wn+" WITH WAREHOUSE_SIZE = '"+WAREHOUSE_SIZE_BOX+"' WAREHOUSE_TYPE = 'STANDARD' AUTO_SUSPEND ="+str(AUTO_SUSPEND)+" AUTO_RESUME = "+AUTO_RESUME+" MIN_CLUSTER_COUNT = "+MIN_CLUSTER_COUNT+" MAX_CLUSTER_COUNT = "+MAX_CLUSTER_COUNT+" SCALING_POLICY = '"+SCALING_POLICY+"';")
                            if rr:
                                # beautiful_warehouses.append(wn)
                                st.success("warehouse created")
                                # st.experimental_rerun()
            # creating a warehouse end
                if st.button('Reload'):
                    st.empty()

            if len(st.session_state.warehousesbox)>1 and 'select' not in st.session_state.warehousesbox:
                if st.button("next"):
                    st.session_state.default_index =1

####################################
# Warehouse selection/creation end
####################################
####################################
# share creation start
####################################
def share_creation():
    
    if len(st.session_state.warehousesbox)>1 and 'select' not in st.session_state.warehousesbox:
                                    
        if "load_state_share" not in st.session_state:
            st.session_state.load_state_share = True
        # if 'no' in flag or nofil or st.session_state.load_state_share  :
        if  st.session_state.load_state_share  :
            # with col6:
                form = st.form(key='my_form',clear_on_submit=True)
                Share_name= form.text_input(label='Enter Share Name')
                
                comment = form.text_area('Comment Box (optional)',)

                submit_button = form.form_submit_button(label='Submit')
                if st.button("Back"):
                    st.session_state.default_index=0
                if Share_name and submit_button:
                    c="'"
                    comment = c + comment + c
                    create_share = run_query('create share '+Share_name+ ' Comment ='+comment+ ';')
                    
                    st.success('Share '  +str(Share_name)+  ' successfully created.')
                   
                elif not Share_name and submit_button:
                    st.warning("Please Enter valid Share Name")  
                 
####################################
# share creation end
####################################                           
####################################
# Add Objects Page Start
####################################
def Add_Objects():
    st.session_state.load_state_add_consumers_reader=False

    with st.container():
        submitbutton()
        newbutton()

        st.session_state.load_state_reader_setup=False
        st.session_state.load_state_monitor=False
        if 'conn' not in st.session_state:
            st.session_state.conn=None
        if st.session_state.conn!=None:
            
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
                                
                    except Exception as e:
                        print(e)
                        return {'success': False}
                else:
                    with st.session_state.conn.cursor() as cur:
                        cur.execute(query)
                        return cur.fetchall()
                    
                
            


           
            add_logo('./data/logo.png')

            global flag
            flag='no'

           
            run_query("use secondary roles all;")
            run_query("use role SHAREMON_ADMIN;")
            
            run_query("use warehouse SHAREMON_WH;")
            c="'"
            run_query("SHOW ROLES;")
            roles=run_query("select \"name\" from table(result_scan(last_query_id()));")
            roles=beautify(roles)

            if 'SHAREMON_ADMIN'  in roles:
                
                
                run_query("use role SHAREMON_ADMIN;")
                               
                col5,col6=st.columns([1,1])
                col9,col10=st.columns([1,1])
                with col5:
                    
                    warehousesbox=run_query("select current_warehouse()")
                    
                
                if len(warehousesbox)>=1 and 'select' not in warehousesbox:
                    # with col5:
                            doublequote='"'

                            run_query("show shares;")
                            outboundshares=run_query("select \"name\" from table(result_scan(last_query_id())) where \"kind\"='OUTBOUND';")
                            B_outboundshares=(beautify(outboundshares))
                            share_name_list=[]
                            
                            for share in B_outboundshares:
                                share_name_list.append(share) ##Added by Nikhil Ranade to handle change of snowflake schema for show shares command##
                            
                            # for share in B_outboundshares:
                            #     print("each share:",share)
                            #     if share.split('.')[2] not in share_name_list:
                            #         share_name_list.append(share.split('.')[2]) 
                            
                            if(share_name_list[0] != 'select'):
                                share_name_list.insert(0,"select")
                            Share_name=st.selectbox("Displaying the available outbound shares",(share_name_list))
                            if len(Share_name)>=1 and 'select' not in Share_name:
                                pass
                            run_query("show databases;")
                            tt=beautify(run_query("select \"name\" from table(result_scan(last_query_id())) where \"origin\" ='';"))
                            print(tt)
                            db_list=tt
                            box1=st.selectbox("Displaying the available databases",(db_list))
                            if len(box1)>1 and 'select' not in box1:
                                inf=c + 'INFORMATION_SCHEMA' + c
                                schem=run_query('select SCHEMA_NAME from "'+box1+'"."INFORMATION_SCHEMA"."SCHEMATA" where SCHEMA_NAME<>'+inf+';')
                                schem_list=beautify(schem)
                               
                                box2=st.multiselect("Available schemas",(schem_list))
                                
                                refusagelst=[]
                                refusagelstnew=[]
                                refusagelst_udf=[]
                                tables_list=[]
                                lst=[]
                                udflst=[]
                                udflsttemp=[]
                                ext_tables=[]
                                tab_only=[]
                                #newlst is for refernce db
                                reflst=[]
                                secure_view_name=[]
                                tab_only_sche=[]
                                if 'newsecureviewslist' not in st.session_state:
                                    st.session_state.newsecureviewslist=[]
                                if 'removetableviewlist' not in st.session_state:    
                                    st.session_state.removetableviewlist=[]
                                if 'selected_tables' not in st.session_state:
                                    st.session_state.selected_tables=[]
                                
                                # with col9:
                                if (1):                                
                                    run_query('use role SHAREMON_ADMIN;')
            #####################################################################################################                                   
                                    for row in box2 :   
                                        c="'"
                                        sch_name=c + row + c
                                       
                                        if len(box2)>=1 :
                                            with st.expander("Select objects in schema "+row+"",expanded=True):
                                                run_query("use schema "+box1+"."+row+";")
                                                tab=beautify(run_query('select distinct TABLE_NAME from '+box1+'.INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA='+sch_name+' AND TABLE_TYPE='+c+'BASE TABLE'+c+'ORDER BY 1;'))
                                                st.empty()
                                                st.session_state.selected_tables=st.multiselect("Available tables for selected schema  " +row+"",(tab))
                                                time.sleep(3)
                                                run_query("create procedure if not exists show_Objects_in_accounte(DB VARCHAR, SC VARCHAR)  returns varchar not null  language javascript  execute as caller  as  $$ var sql_command00 = snowflake.createStatement({ sqlText:`use schema `+DB+ `.`+SC+ ``}); var sql_command0 = snowflake.createStatement({ sqlText:`show views`});  var sql_command1 = snowflake.createStatement({ sqlText:`select $2 as view_name from table(result_scan(last_query_id())) where $9=true and $4 ='` +DB+ `' and $5 ='` +SC+ `'`});    var db_list = [];  try  { sql_command00.execute(); sql_command0.execute();  var db = sql_command1.execute();  while (db.next())  {  var db_name= db.getColumnValue(1);  db_list.push([db_name]);  }      return db_list;  }  catch (err)  {  return 'Failed: ' + err;  }  $$;")                                               
                                                views=run_query("call show_Objects_in_accounte('"+box1+"',"+sch_name+");")
                                                vl=beautify(views)                                                
                                                v_list=(split_string(vl[0]))                                                                               
                                                box3=st.multiselect("Available views from selected schema "+row+"",(v_list))
                                                
                                                if 'selected_udfs' not in st.session_state:
                                                    st.session_state.selected_udfs = []

                                                if 'selected_extbs' not in st.session_state:
                                                    st.session_state.selected_extbs = []

                                                #clear session state for mv,udf & extb
                                                def clear_selected_lists():
                                                    """clears the session state for selected_mvs, selected_udfs, selected_extbs
                                                        args: None
                                                        returns: None
                                                    """
                                                    # del st.session_state.selected_mvs
                                                    del st.session_state.selected_udfs
                                                    del st.session_state.selected_extbs

                                                
                                            #code block for secure UDFs
                                            # with sudf:
                                                keycount=1                                               
                                                run_query('''
                                                create procedure if not exists show_udfs(DB VARCHAR, SC VARCHAR)
                                                returns varchar not null
                                                language javascript
                                                execute as caller
                                                as
                                                $$
                                                var sql_command0 = snowflake.createStatement({ sqlText:`show user functions in ` + DB +`.`+ SC +`;`});
                                                var sql_command1 = snowflake.createStatement({ sqlText:`select "name" from TABLE(RESULT_SCAN(LAST_QUERY_ID())) where "is_builtin" = 'N' and "is_secure" = 'Y';`});
                                                var col_list = [];
                                                try
                                                {
                                                sql_command0.execute();
                                                var col = sql_command1.execute();
                                                while (col.next())
                                                {
                                                var col_name= col.getColumnValue(1);
                                                col_list.push([col_name]);
                                                }
                                                return col_list;
                                                }
                                                catch (err)
                                                {
                                                return "Failed: " + err;
                                                }
                                                $$;
                                                ''')
                                                
                                                secure_udfs = run_query("call show_udfs('"+box1+"',"+sch_name+");")                                                
                                                #secure UDFs selected by user
                                                disp_secure_udfs=beautify(secure_udfs)[0].split(',')
                                                if '' not in disp_secure_udfs:
                                                    print("disp_secure_udfs=",disp_secure_udfs)
                                                    print("secure_udfs=",beautify(secure_udfs))
                                                    secure_udf_choice = st.multiselect(f'Select secure UDFs from {sch_name} schema',disp_secure_udfs,key=str(keycount)+row+'')
                                                    keycount+=1
                                                else:
                                                    secure_udf_choice=[]
                                                
                                                #store selected udfs in session state
                                                
                                                
                                                udf_param=[]
                                                if len(secure_udf_choice)>0:
                                                    for i in secure_udf_choice:                                                       
                                                        run_query('''create procedure if not exists show_udfs_in_account(SUDF STRING)
                                                                returns STRING not null
                                                                language javascript
                                                                execute as caller
                                                                as
                                                                $$
                                                                var sql_command0 = snowflake.createStatement({ sqlText:`show user functions ;`});
                                                                var sql_command1 = snowflake.createStatement({ sqlText:`select $9 from table(result_scan(last_query_id())) where $2= '`+SUDF+`'; `});
                                                                try
                                                                {
                                                                test = sql_command0.execute();
                                                                var obje = sql_command1.execute();
                                                                while (obje.next())
                                                                {
                                                                var UDF_name= obje.getColumnValue(1);
                                                                }
                                                                return UDF_name;
                                                                }
                                                                catch (err)
                                                                {
                                                                return 'Failed: ' + err + obje;
                                                                }
                                                                $$;
                                                                ''')
                                                        fuludf=run_query("call show_udfs_in_account('"+i+"');") 
                                                        beautiful_fuludf=beautify(fuludf)
                                                        
                                                        udfstr=str(fuludf[0])
                                                        
                                                        udfsepp=udfsep(udfstr)[0]
                                                        sliced = udfsepp[2:]
                                                        
                                                        udflsttemp.append(sliced)
                                                    udflst.append(udflsttemp)
                                                                                                            
                                                    if secure_udf_choice != '' :
                                                        for choice in secure_udf_choice:
                                                            if choice not in st.session_state.selected_udfs:
                                                                st.session_state.selected_udfs.append(choice)

                                                else:
                                                    udflst.append([])                

                                                run_query('''
                                                    create procedure if not exists show_external_tables(DB VARCHAR, SC VARCHAR)
                                                    returns varchar not null
                                                    language javascript
                                                    execute as caller
                                                    as
                                                    $$
                                                    var sql_command0 = snowflake.createStatement({ sqlText:`show external tables in ` + DB +`.`+ SC +`;`});
                                                    var sql_command1 = snowflake.createStatement({ sqlText:`select "name" from TABLE(RESULT_SCAN(LAST_QUERY_ID()));`});
                                                    var col_list = [];
                                                    try
                                                    {
                                                    sql_command0.execute();
                                                    var col = sql_command1.execute();
                                                    while (col.next())
                                                    {
                                                    var col_name= col.getColumnValue(1);
                                                    col_list.push([col_name]);
                                                    }
                                                    return col_list;
                                                    }
                                                    catch (err)
                                                    {
                                                    return "Failed: " + err;
                                                    }
                                                    $$;
                                                    ''')
                                                external_tables = run_query(f'''call show_external_tables('{box1}','{row}');''')
                                                disp_external_tables=beautify(external_tables)[0].split(',')
                                                if '' not in disp_external_tables:
                                                    external_table_choice = st.multiselect(f'Select External tables from {row} schema',disp_external_tables,key='smv'+row+'')
                                                else:
                                                    external_table_choice=[]
                                                
                                                print(len(external_table_choice))
                                                if len(external_table_choice)>0:
                                                    print("lst",lst)
                                                    print(external_table_choice)
                                                    ext_tables.append(external_table_choice)
                                                else:
                                                    ext_tables.append([])
                                                print(ext_tables)
                                                #store the selected external tables in session state 
                                            
                                                if external_table_choice != '' :
                                                    for choice in external_table_choice:
                                                        if choice not in st.session_state.selected_extbs:
                                                            st.session_state.selected_extbs.append(choice)
                                    
                                            ########Other secure objects end

                                            if len(st.session_state.selected_tables)>=1:
                                                tables_list.append(st.session_state.selected_tables)
                                        
                                            else:
                                                tables_list.append([])
                                            #box3 have selecrted views
                                            if len(box3)>=1 :                                           
                                                lst.append(box3)
                                                reflst.append(box3)
                                            else:
                                                lst.append([])
                                            t_lst=[]
                                            
                                                # for row1 in box3 :
                                            if  len(st.session_state.selected_tables)>=1:
                                                for row1 in st.session_state.selected_tables :
                                                    # st.write('You selected:', row1)
                                                    #print(lst)
                                                    
                                                    tab=run_query('select TABLE_NAME from '+box1+'.INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA='+sch_name+' AND TABLE_TYPE='+c+'BASE TABLE'+c+' AND TABLE_NAME='+c+row1+c+' ;')
                                                    tab_list=beautify(tab)
                                                    
                                                    if tab_list:                                                   
                                                        t_lst.append(tab_list[0])
                                                                                                                                                            
                                                    if tab_list :
                                                        flag='yes'
                                                    else :
                                                        flag='no'
                                                if "load_state" not in st.session_state:
                                                    st.session_state.load_state = True
                                                if 'yes' in flag:                                                    
                                                    # with col10:
                                                        if st.session_state.load_state :
                                                            t_lst.insert(0, "select")
                                                            with st.expander('Create secure view ('+row+') schema',expanded=True):
                                                                tab_only=st.selectbox('Select the table from '+row+' schema to create a secure view', (t_lst))
                                                                print("tab_only",tab_only)
                                                                tab_only_sche.append(row)
                                                                if len(tab_only)>=1 and  'select' not in tab_only:
                                                                    print("tab_only",tab_only)
                                                                    print("len=",len(tab_only))
                                                                    if len(tab_only)>=1 :
                                                                        print("in if")
                                                                        single_quote="'"
                                                                        box11= single_quote+box1+single_quote
                                                                        row2= single_quote+row+single_quote
                                                                        tab_only1=single_quote+tab_only+single_quote
                                                                        run_query('create procedure if not exists show_columns_in_table(BOX1 VARCHAR, SC VARCHAR,TAB_ONLY VARCHAR) returns varchar not null language javascript execute as caller as $$  var sql_command0 = snowflake.createStatement({ sqlText:`SHOW COLUMNS in table `+BOX1+`.`+SC+`.`+TAB_ONLY+`;`}); var sql_command1 = snowflake.createStatement({ sqlText:`select $3 from table(result_scan(last_query_id()));`}); var col_list = []; try { sql_command0.execute(); var col = sql_command1.execute(); while (col.next()) { var col_name= col.getColumnValue(1); col_list.push([col_name]); } return col_list; } catch (err) { return "Failed: " + err; } $$;')

                                                                        columns=run_query("call show_columns_in_table("+box11+","+row2+","+tab_only1+");")
                                                                        cl=beautify(columns)
                                                                        columns=(split_string(cl[0]))
                                                                        print(columns)
                                                                        columns_checkbox = st.multiselect("Please select the columns to create secure view",columns,key="row1"+row+"")
                                                                        print("columns_checkbox=",columns_checkbox)
                                                                        if len(columns_checkbox)>= 1 :
                                                                            columns_checkbox = ['"' + item + '"' for item in columns_checkbox] #Added by Nikhil Ranade on 21-08 to handle columns with spaces,small case etc.
                                                                            print("columns_checkbox",columns_checkbox)
                                                                            beautiful_columns=listbeautifytostr(columns_checkbox)
                                                                            #print("columns of beautyfy again ="+beautiful_columns)    
                                                                            secure_view_name=st.text_input("Enter view name",key="key"+row1+"")
                                                                            if st.button('Create secure view',key="button"+row1+""):
                                                                                run_query("use schema "+box1+"."+row+"")
                                                                                run_query("create or replace secure view "+secure_view_name+" as select "+beautiful_columns+" from "+box1+"."+row+"."+tab_only+";")
                                                                                st.success("Secure View "+secure_view_name+" created successfully")
                                                                                if secure_view_name not in  st.session_state.newsecureviewslist:
                                                                                    st.session_state.newsecureviewslist.append(secure_view_name)
                                                                                if tab_only not in st.session_state.removetableviewlist:
                                                                                    st.session_state.removetableviewlist.append(tab_only)
                                                                                print("newsecureviewslist0",st.session_state.newsecureviewslist)
                                                                                print("removetableviewlist0",st.session_state.removetableviewlist)
                                                                                print("length=0=",len(st.session_state.newsecureviewslist))
                                                                                time.sleep(3)
                                                                                st.experimental_rerun()
                                                                elif 'select' in tab_only or len(tab_only)<1:
                                                                    print("entered elif")
                                                                    st.session_state.newsecureviewslist.append([])
                                                                    st.session_state.removetableviewlist.append([])
                                                                print("newsecureviewslist",st.session_state.newsecureviewslist)
                                                                print("removetableviewlist",st.session_state.removetableviewlist)
                                            else:
                                                lst.append([])                                                                                           
                                        

                                    def clear_list():
                                        """clears the session state for account_list, share_name_list and clears the list choices
                                            args: None
                                            returns: None
                                        """
                                        del st.session_state.account_list
                                        
                                        del st.session_state.share_name_list
                                    

                                    if "load_state_share" not in st.session_state:
                                        st.session_state.load_state_share = True
                                    # if 'no' in flag or nofil or st.session_state.load_state_share  :
                                    if 'no' in flag  or st.session_state.load_state_share  :
                                        # with col9:
                                            form = st.form(key='my_form')
                                            

                                            submit_button = st.button(label='Submit')
                                            if submit_button:                                                                                        
                                                run_query('GRANT USAGE ON DATABASE '+ box1+ ' TO SHARE '+ Share_name + ';')
                                                print("list=",lst)                                               
                                                run_query("use role ACCOUNTADMIN;") 
                                                run_query("use secondary roles all;")
                                                run_query('''create procedure if not exists get_ref_db(DB VARCHAR, SC VARCHAR,VW VARCHAR)
                                                returns varchar not null
                                                language javascript
                                                execute as caller
                                                as
                                                $$
                                                var sql_command1 = snowflake.createStatement({ sqlText:`select listagg(distinct referenced_database_name,',') within group (order by referenced_database_name) "referenced_database_names"
                                                from table(get_object_references(database_name=>`+DB+`, schema_name=>`+SC+`, object_name=>`+VW+`));`});
                                                var col_list = [];
                                                try
                                                {
                                                var col = sql_command1.execute();
                                                while (col.next())
                                                {
                                                var col_name= col.getColumnValue(1);
                                                col_list.push([col_name]);
                                                }
                                                return col_list;
                                                }
                                                catch (err)
                                                {
                                                return "Failed: " + err;
                                                }
                                                $$;
                                                ''')
                                                run_query("use role SHAREMON_ADMIN;")
                                                # box2 have schema
                                                countt=-1
                                                for sche in box2:
                                                    countt +=1
                                                    # st.write("lst",lst)
                                                    print("lst==",lst)
                                                    if len(lst)!=0:
                                                        print('countt=',countt)
                                                        # print(lst[countt])
                                                        if lst[countt]!=0:
                                                            print("lst=",lst)
                                                            print(lst[countt])
                                                            for viewext in lst[countt] :
                                                                ext_db=beautify(run_query("call get_ref_db('"+box1+"','"+sche+"','"+viewext+"');"))
                                                                refusagelst.append(*ext_db)
                                                                for db in refusagelst:
                                                                    db_temp = db.split(',')
                                                                    print("dbtemp=",db_temp)
                                                                    for item in db_temp:
                                                                        refusagelstnew.append(item)
                                                    
                                                

                                                #reference dbs for udf
                                                print("sec_udf choice len",len(udflst))
                                                print("udflst==",udflst)
                                                if len(udflst)>=1:
                                                    run_query("use role ACCOUNTADMIN;")
                
                                                    run_query('''create procedure if not exists get_ref_db_udf(DB VARCHAR, SC VARCHAR,UDF VARCHAR)
                                                    returns varchar not null
                                                    language javascript
                                                    execute as caller
                                                    as
                                                    $$
                                                    var sql_command1 = snowflake.createStatement({ sqlText:`select listagg(distinct referenced_database,',') within group (order by referenced_database)
                                                    from snowflake.account_usage.object_dependencies
                                                    where referencing_database = '`+DB.toUpperCase()+`' and referencing_schema = '`+SC.toUpperCase()+`' and referencing_object_name = '`+UDF.toUpperCase()+`';`});
                                                    var col_list = [];
                                                    try
                                                    {
                                                    var col = sql_command1.execute();
                                                    while (col.next())
                                                    {
                                                    var col_name= col.getColumnValue(1);
                                                    col_list.push([col_name]);
                                                    }
                                                    return col_list;
                                                    }
                                                    catch (err)
                                                    {
                                                    return "Failed: " + err;
                                                    }
                                                    $$;
                                                    ''')
                                                    run_query("use role SHAREMON_ADMIN;")
                                                schcnt=-1    
                                                for sche in box2:
                                                    schcnt+=1
                                                    
                                                    print("sche udflst",udflst)
                                                    print(schcnt)
                                                    print(udflst[schcnt])
                                                    # for eachudf in secure_udf_choice:
                                                    for eachudf in udflst[schcnt]:
                                                        print("eachudf=",eachudf)
                                                        eachudf=eachudf.split('(')[0]
                                                        print("eachudf split=",eachudf)
                                                        ext_db_udf=beautify(run_query("call get_ref_db_udf('"+box1+"','"+sche+"','"+eachudf+"');"))
                                                        print("ext_db_udf=",ext_db_udf)
                                                        print("len",len(ext_db_udf))
                                                        if ext_db_udf != [''] :
                                                            refusagelst_udf.append(*ext_db_udf)
                                                        print("refusagelst_udf",refusagelst_udf)
                                                        for db in refusagelst_udf:
                                                            db_temp = db.split(',')
                                                            print("dbtemp=",db_temp)
                                                            for item in db_temp:
                                                                refusagelstnew.append(item)
                                                
                                                refgrantdblist=set(refusagelstnew)
                                                for eachdb in refgrantdblist:
                                                    if eachdb:
                                                        run_query("grant reference_usage on database "+eachdb+" to share "+Share_name+";")
                                                count=-1                                                
                                                f_db_name = box1
                                                f_Share_name =Share_name
                                                db_grant=run_query('GRANT USAGE ON DATABASE '+ f_db_name+ ' TO SHARE '+ f_Share_name + ';')
                                                for row in box2 :
                                                    #box2 have schema
                                                    sch_grant=run_query('GRANT USAGE ON SCHEMA '+ f_db_name+'.'+row+ ' TO SHARE '+ f_Share_name + ';')

                                                    count +=1
                                                    udfcnt=0
                                                    tabcnt=0
                                                    lentab=len(lst)
                                                    lenUdflst=len(udflst)
                                                    
                                                    if len(tables_list)>=1:
                                                        for tables in tables_list[count]:
                                                            print("tables_list2=",tables_list)
                                                            run_query('GRANT SELECT ON VIEW ' + f_db_name+'.'+row+ '.' + tables +'  TO SHARE '+ f_Share_name + ';')
                                                    if len(ext_tables)>=1:
                                                        for exttable in ext_tables[count]:
                                                            run_query('GRANT SELECT ON VIEW ' + f_db_name+'.'+row+ '.' + exttable +'  TO SHARE '+ f_Share_name + ';')
                                                    if len(udflst)>=1:
                                                        for udfrow in udflst[count]:
                                                            udfcnt+=1
                                                            print("udflst2=",udflst)
                                                            print("udf list=",udflst[count])
                                                            print("granting udfs")
                                                            print("udfrow=",udfrow)
                                                            if len(udfrow)>=1:
                                                                run_query("use schema "+row+";")
                                                                udf_grant=run_query('grant usage on function '+udfrow+'  TO SHARE '+ f_Share_name + ';')
                                                            # udf
                                                            if lenUdflst==udfcnt:
                                                                pass
                                                    if len(lst)>=1:
                                                        for row1 in lst[count] :
                                                            print(row1)
                                                            tbl_grant=run_query('GRANT SELECT ON VIEW ' + f_db_name+'.'+row+ '.' + row1 +'  TO SHARE '+ f_Share_name + ';')

                                                            tabcnt+=1
                                                            if lentab==tabcnt:
                                                                pass
                                                    print("removetableviewlistmid",st.session_state.removetableviewlist)
                                                    print("newsecureviewslistmid",st.session_state.newsecureviewslist)
                                                    print("length==",len(st.session_state.newsecureviewslist))
                                                    if len(st.session_state.newsecureviewslist)>0:
                                                        pass
                                                        
                                                    
                                                st.success("Objects added successfully")
                                            elif not Share_name and submit_button:
                                                st.warning("Please Enter valid Share Name")   
                                                             
                
                       
            else :
                st.write("you don't have proper privileges")                                    
        else:
            st.warning('Please login!')
####################################
# Add Objects Page end
####################################
# Add Consumers Page start
####################################
def Add_Consumers():

    newbutton()

    st.session_state.load_state_reader_setup=False
    st.session_state.load_state_monitor=False

    add_logo('./data/logo.png')

    if 'conn' not in st.session_state:
        st.session_state.conn=None
    if st.session_state.conn!=None:

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
                except Exception as e:
                    print(e)
                    return {'success': False}
            else:
                with st.session_state.conn.cursor() as cur:
                    cur.execute(query)
                    return cur.fetchall()

        run_query("use secondary roles all;")
        run_query("use role SHAREMON_ADMIN;")
        run_query("use warehouse SHAREMON_WH;")

        def clear_list():
            """clears the session state for account_list, share_name_list and clears the list choices
                args: None
                returns: None
            """
            del st.session_state.account_list

        if "load_state_add_consumers_reader" not in st.session_state:
            st.session_state.load_state_add_consumers_reader = False
        run_query("show shares;")
        outboundshares=run_query("select \"name\" from table(result_scan(last_query_id())) where \"kind\"='OUTBOUND';")
        B_outboundshares=(beautify(outboundshares))
        share_name_list = []
        
        for share in B_outboundshares:
            share_name_list.append(share)  ###Added by Nikhil ranadeto handle show shares schema change issue###

        # for share in B_outboundshares:
        #     if share.split('.')[2] not in share_name_list:
        #         share_name_list.append(share.split('.')[2]) 
        st.markdown('''     
                <h4 class="heading" style="margin-top: 20px;">Add consumers</h4>
                ''', unsafe_allow_html=True)
        if(share_name_list[0] != 'select'):
            share_name_list.insert(0,"select")
        selected_share=st.selectbox("Displaying the available outbound shares",(share_name_list))
        if len(selected_share)>=1 and 'select' not in selected_share:
            pass
        ac=["Full account","Reader account"]
        acct_list=beautify(ac)
        box4=st.selectbox("Select the account type to share your data",(acct_list))

        #Temporary access code
        run_query("use schema sharemon_db.sharemon_schema;")
        # Temporary access - create sp for Upsert
        run_query('''
        CREATE PROCEDURE IF NOT EXISTS temp_access_upsert(share_name_op varchar, consumer_ac_op varchar, revoke_date_op date,account_type_op varchar)
        RETURNS VARCHAR
        LANGUAGE javascript
        EXECUTE AS CALLER
        AS
        $$
        try{
            var revoke_date_op_new = REVOKE_DATE_OP.toISOString();
            
            const date = new Date();
            let day = date.getDate();
            let month = date.getMonth() + 1;
            let year = date.getFullYear();      
            let currentDate = `${year}-${month}-${day}`;
            
            var result_set = snowflake.execute( { sqlText:"select * from SHAREMON_DB.SHAREMON_SCHEMA.CONSUMER_TEMP_ACCESS_TB;"});
            var consumer_accounts = [];
            var share_names = [];
            
            while (result_set.next()){
                consumer_accounts.push(result_set.getColumnValue(2));
                share_names.push(result_set.getColumnValue(3));
            }
            if(consumer_accounts.length != 0){
                for(i=0;i<consumer_accounts.length;i++){
                if(consumer_accounts[i] == CONSUMER_AC_OP && share_names[i] == SHARE_NAME_OP){
                    snowflake.execute( { sqlText:"update SHAREMON_DB.SHAREMON_SCHEMA.CONSUMER_TEMP_ACCESS_TB \
                    set date_added ='"+currentDate+"', date_to_be_revoked ='"+revoke_date_op_new+"' where consumer_account_name ='"+CONSUMER_AC_OP+"' \
                    and share_name = '"+SHARE_NAME_OP+"';"});
                    break;
                }
                else if(i == consumer_accounts.length -1){
                    snowflake.execute({sqlText:"insert into SHAREMON_DB.SHAREMON_SCHEMA.CONSUMER_TEMP_ACCESS_TB (consumer_account_name,share_name,date_added,date_to_be_revoked,account_type) \
                    values('"+CONSUMER_AC_OP+"','"+SHARE_NAME_OP+"','"+currentDate+"','"+revoke_date_op_new+"','"+ACCOUNT_TYPE_OP+"');"});
                }
                }
            } 
            else{
            snowflake.execute({sqlText:"insert into SHAREMON_DB.SHAREMON_SCHEMA.CONSUMER_TEMP_ACCESS_TB (consumer_account_name,share_name,date_added,date_to_be_revoked,account_type) \
            values('"+CONSUMER_AC_OP+"','"+SHARE_NAME_OP+"','"+currentDate+"','"+revoke_date_op_new+"','"+ACCOUNT_TYPE_OP+"');"});
            }
            return "Succeeded";
        }
        catch(err){
        return "Failed" + err;
        }
        $$;
        ''')

        # Temporary access - create sp for revoking access
        run_query('''
        CREATE PROCEDURE IF NOT EXISTS temp_access_sp()
        RETURNS VARCHAR
        LANGUAGE javascript
        EXECUTE AS CALLER
        AS
        $$
        try{
            var result_set = snowflake.execute( { sqlText:"select * from SHAREMON_DB.SHAREMON_SCHEMA.CONSUMER_TEMP_ACCESS_TB;"});
            while (result_set.next()){
                    var consumer_account_name = result_set.getColumnValue(2);
                    var share_name = result_set.getColumnValue(3);
                    var date_revoked = new Date(result_set.getColumnValue(5));
                    
                    var todays_date = new Date();
                    var difference_in_time = date_revoked.getTime() - todays_date.getTime();
                    var date_diff = Math.round( difference_in_time / (1000 * 3600 * 24));
                    
                    if (date_diff == 0) {
                    snowflake.execute( { sqlText:"alter share "+share_name+" remove account= "+consumer_account_name+";"});  
                    }
            }
            return "Succeeded";
        }
        catch(err){
            return "Failed" + err;
        }
        $$;
        ''')
        run_query("use secondary roles all;")
        #temporary access - Task to revoke access runs everyday
        run_query('''
        CREATE TASK if not exists temp_access_task
        WAREHOUSE = sharemon_wh
        SCHEDULE = 'USING CRON 0 2 * * * UTC'
        AS
        call temp_access_sp();
        ''')

        #resume task
        run_query("alter task temp_access_task resume;")

        #code block for full account
        if box4=="Full account" :
            #store region,cloud,account name of provider
            user_snowflake_region = run_query('select current_region();')
            user_snowflake_account = beautify(run_query('select current_account();'))

            provider_snowflake_region = user_snowflake_region[0][0].replace('_','-').lower()
            provider_cloud = provider_snowflake_region.split('-',1)[0]
            provider_region = provider_snowflake_region.split('-',1)[1]

            # store account list in session state
            if 'account_list' not in st.session_state:
                st.session_state.account_list = []
            
            #radio select to validate using url or using locator
            selected_validate_method = st.radio('Select validation method',['Validate using url','Validate using account locator'])

            #validate url
            if selected_validate_method == 'Validate using url':
                #URL input
                with st.form('url_form',clear_on_submit=True):
                    account_locator = st.text_input("Enter consumer account locator url")
                    st.caption('Ex: https://app.snowflake.com/ap-south-1.aws/rj94508/data/databases ')
                    account_locator_re = st.text_input("Re-enter consumer account locator url")
                    print("account_locator=",account_locator)
                    print("account_locator_re=",account_locator_re)
                    if account_locator != account_locator_re:
                        st.error("Account locator url's did not match, please re-enter")
                    elif account_locator=='' and account_locator_re=='':
                        st.write("Please enter account locators")
                    else:
                        st.write("Account locator url's are matching, click on validate")


                    # Account validation , if on the same cloud & region or not  
                    validated = st.form_submit_button('Validate') 
                    st.caption('''To add multiple accounts to same share, validate all the required accounts first and then choose the 
                    accounts you want to add to the share in the drop down box below.''')
                    if validated :
                        #url validation using validators library
                        valid = validators.url(account_locator)
                        if valid == True:
                            if 'app.snowflake.com' in account_locator.split('/'):
                                consumer_account_name = account_locator.split('/')[4]
                                consumer_region = account_locator.split('/')[3].split('.')[0]
                                consumer_cloud = account_locator.split('/')[3].split('.')[1]
                            else:
                                consumer_account_name = account_locator.split('.')[0].split('//')[1]
                                consumer_region = account_locator.split('.')[1]
                                consumer_cloud = account_locator.split('.')[2]
                            if consumer_account_name == user_snowflake_account[0].lower():
                                    st.error('You have used the Snowflake account you have currently logged in with. Please use a different account to add to the share')
                            else:
                                if consumer_cloud == provider_cloud:
                                    if consumer_region == provider_region:
                                        if consumer_account_name not in st.session_state.account_list:
                                            st.session_state.account_list.append(consumer_account_name)
                                            st.success('Consumer is on the same cloud & region')
                                    else:
                                        st.error(f'Consumer on different region, please use snowflake data replication to share data to a differnt region')
                                else:
                                    st.error(f'Consumer on different snowflake cloud, please use snowflake data replication to share data to a differnt cloud')
                        else:
                            st.error("Invalid url please make sure you've added the correct url format")    
                # adding consumer accounts 
                with st.form('add_account_to_share',clear_on_submit=True):  
                    choices = st.multiselect("Select accounts",st.session_state.account_list)

                    #temporary access to share
                    with st.expander("Provide temporary access to share",expanded=True):
                        revoke_date = st.date_input('Select date after which access should be removed from consumer on selected share')
                        st.caption('Leave date field empty or as it is if temporary access is not required')
                        confirm_temp_access = st.checkbox("Click on check box to confirm temporary access")

                    #after submit add consumer to share
                    # with Add_consumer_to_share_button
                    submitted = st.form_submit_button('Add consumer to share')
                    if submitted:
                        for consumer in choices:
                            #pets_share to be replaced with share name inputed by provider
                            query = run_query(f'ALTER SHARE {selected_share} ADD ACCOUNTS = {consumer}')
                            st.success(f'Share {selected_share} has been shared with account {consumer}')

                            #Temporary access - calling SP to upsert consumer details
                            if revoke_date == date.today() and not confirm_temp_access:
                                run_query(f"call temp_access_upsert('{selected_share}','{consumer}','9999-12-12','{box4}');")
                                st.caption("Temporary access not applied")
                            elif revoke_date > date.today() and confirm_temp_access:
                                run_query(f"call temp_access_upsert('{selected_share}','{consumer}','{revoke_date}','{box4}');")
                                st.caption("Temporary access applied")
                        clear_list()
            
            #validate using locator inputs
            else:
                #locator as input
                with st.form('locator_form',clear_on_submit=True):
                    consumer_account_locator = st.text_input('Enter consumer snowflake account locator')
                    st.caption('For example : xy1234 from xy1234.ap-south-1.aws.snowflakecomputing.com')
                    consumer_cloud = st.text_input('Enter consumer snowflake cloud')
                    st.caption('For example : aws')
                    consumer_region = st.text_input('Enter consumer snowflake region')
                    st.caption('For example : ap-south-1')

                    # Account validation , if on the same cloud & region or not  
                    validated = st.form_submit_button('Validate')
                    st.caption('''To add multiple accounts to same share, validate all the required accounts first and then choose the 
                    accounts you want to add to the share in the drop down box below.''') 
                    if validated :
                        if consumer_account_locator == user_snowflake_account[0].lower():
                            st.error('You have used the Snowflake account you have currently logged in with. Please use a different account to add to the share')
                        else:
                            if consumer_cloud.lower() == provider_cloud:
                                if consumer_region.lower() == provider_region:
                                    if consumer_account_locator not in st.session_state.account_list:
                                        st.session_state.account_list.append(consumer_account_locator.lower())
                                        st.success('Consumer is on same cloud & region')
                                else:
                                    st.error(f'Consumer is on different region, please replicate to {consumer_region} before sharing')
                            else:
                                st.error(f'Consumer is on different snowflake cloud, please replicate to {consumer_cloud} before sharing data')
                            
                # adding consumer accounts 
                with st.form('add_account_to_share_2',clear_on_submit=True):  
                    choices = st.multiselect("Select accounts",st.session_state.account_list)

                    #temporary access to share
                    with st.expander("Provide temporary access to share",expanded=True):
                        revoke_date = st.date_input('Select date after which access should be removed from consumer on share selected')
                        st.caption('Leave date field empty or as is if temporary access is not required')
                        confirm_temp_access = st.checkbox("click on check box to confirm temporary access.")

                    #after submit add consumer to share
                    submitted = st.form_submit_button('Add consumer to share')
                    if submitted:
                        for consumer in choices:
                            #pets_share to be replaced with share name inputed by provider
                            query = run_query(f'ALTER SHARE {selected_share} ADD ACCOUNTS = {consumer}')
                            st.write(f'Share {selected_share} has been shared with account {consumer}')

                            #Temporary access - calling SP to upsert consumer details
                            if revoke_date == date.today() and not confirm_temp_access:
                                run_query(f"call temp_access_upsert('{selected_share}','{consumer}','9999-12-12','{box4}');")
                                st.caption("Temporary access not applied")
                            elif revoke_date > date.today() and confirm_temp_access:
                                run_query(f"call temp_access_upsert('{selected_share}','{consumer}','{revoke_date}','{box4}');")
                                st.caption("Temporary access applied")
                        clear_list()



        elif box4=="Reader account":
            run_query("SHOW MANAGED ACCOUNTS;")
            reader_accounts=run_query("select concat(\"name\",' ','(',\"locator\",')') as account_name from table(result_scan(last_query_id())) ;")
            reader_accounts_list=beautify(reader_accounts)
            reader_accounts_list.insert(0,"Select")
            box1=st.multiselect("Please select the existing reader account of your choice",(reader_accounts_list))

            #temporary access
            with st.expander("Provide temporary access to share",expanded=True):
                revoke_date = st.date_input('Select date after which access should be removed from consumer on share selected')
                st.caption('Leave date field empty or as is if temporary access is not required')
                confirm_temp_access = st.checkbox("click on check box to confirm temporary access.")

            text_col,button_col,empty1,empty2=st.columns([1,1,1,1],gap="small")
            with text_col:
                st.write("Want to create a new reader account?")
            with button_col:
                b1 = st.button("Click here",key='Reader form button')
            if b1 or st.session_state.load_state_add_consumers_reader:
                st.session_state.load_state_add_consumers_reader=True
                with st.form('Reader account form',clear_on_submit=True):
                    st.markdown("<h4 style = 'text-align:left; color:white;'>Reader account details</h4>", unsafe_allow_html=True)
                    account_name = st.text_input('Account name', '')
                    user_name = st.text_input('User name', '')
                    password = st.text_input('Password', '',type="password")
                    confirm_password = st.text_input('Confirm password', '',type="password")
                    comments = st.text_input('Comments', '')
                    submit=st.form_submit_button('Submit')
                    if submit:    
                        if account_name and user_name and password:
                            if password==confirm_password:
                                query_string='CREATE MANAGED ACCOUNT '+account_name+' admin_name="'+user_name+'",admin_password="'+password+'", type=reader, COMMENT="'+comments+'";'
                                result_URL=run_query(query_string)
                                print('Reader account details: ',result_URL)
                                print("type is: ",type(result_URL))
                                dic_reader={}
                                dic_reader=split1=result_URL[0][0]
                                print('probably tuple is: ',split1)
                                print('Probably dictionary is: ',dic_reader)
                                st.write('Reader account successfully created! Please check below details')
                                outputinlist=(beautify(result_URL)[0]).split('"')
                                st.write("Account name:",outputinlist[3])
                                st.write("Account url:",outputinlist[7])
                                print("result_url=",outputinlist)
                                st.session_state.load_state_add_consumers_reader=False
                                b1=0

                                time.sleep(7)
                                st.experimental_rerun() 
                            else:
                                st.write('Passwords are not matching :(')
                        else:
                            st.write('Please fill all the details')
                    else:
                        pass
            
            selected_share=selected_share.split('.')

            if 'Select' not in box1 and len(box1) > 0:

                if st.button('Add consumer to share'):
                    for i in box1:        
                        temp=beautify(i.split())

                        run_query('ALTER SHARE '+selected_share[0]+ ' ADD ACCOUNTS = '+temp[1]+';')

                        #Temporary access - calling SP to upsert consumer details
                        if revoke_date == date.today() and not confirm_temp_access:
                            run_query(f"call temp_access_upsert('{selected_share[0]}','{temp[1]}','9999-12-12','{box4}');")
                            st.caption("Temporary access not applied")
                        elif revoke_date > date.today() and confirm_temp_access:
                            run_query(f"call temp_access_upsert('{selected_share[0]}','{temp[1]}','{revoke_date}','{box4}');")
                            st.caption("Temporary access applied")

                    st.success('Consumers added successfully!')
    else:
        st.warning('Please login!')




####################################
# Add Consumers Page end
####################################\


#########################Create role - reader account setup definition############
def create_role_for_reader_setup():
    @st.cache(suppress_st_warning=True)
    def run_reader(query):
        with st.session_state.conn_reader.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()
    role_flag=0
    user_flag=0
    run_reader("USE ROLE ACCOUNTADMIN;")
    if 'reader_setup_role' not in st.session_state:
        st.session_state.reader_setup_role=None
    with st.form('Role'):
        st.session_state.reader_setup_role=st.text_input("Enter role name")
        comment_role=st.text_input("Comments")
        if(st.form_submit_button()):
            if(len(st.session_state.reader_setup_role)>0):
                run_reader('CREATE ROLE '+st.session_state.reader_setup_role+';')
                run_reader(f'GRANT ROLE {st.session_state.reader_setup_role} TO ROLE SYSADMIN;')
                st.success('Role '+st.session_state.reader_setup_role+' created successfully!')
                role_flag=1
                time.sleep(2)
                st.write("")
                st.session_state.default_index_reader_setup=1
                st.experimental_rerun()
            else:
                role_flag=0
                print(len(st.session_state.reader_setup_role))
                st.warning('Please enter appropriate role name')
        #Need to insert this after role is created
    back,empty,next=st.columns([1,10,1],gap="large")
    with next:
        if st.button("Next",key='reader setup role'):
            st.session_state.default_index_reader_setup=1
            st.experimental_rerun()
   
##################################################################################

########################Create user - reader account setup definition##############
def create_user_for_reader_setup():
    @st.cache(suppress_st_warning=True)
    def run_reader(query):
        with st.session_state.conn_reader.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    with st.form('User'):
        username=st.text_input("Enter user name")
        password=st.text_input("Password",type="password")
        confirm_password=st.text_input("Confirm password",type="password")
        if(st.form_submit_button()):
            if len(username)>0:
                if(len(password)>0 and password==confirm_password):
                    query_create_user='CREATE USER '+username+' PASSWORD = "'+password+'" DEFAULT_ROLE = "'+st.session_state.reader_setup_role+'" MUST_CHANGE_PASSWORD = FALSE;'
                    print(query_create_user)
                    run_reader(query_create_user)
                    run_reader(f'GRANT ROLE {st.session_state.reader_setup_role} to user '+username+' ;')
                    st.success('User '+username+' created successfully!')
                    user_flag=1
                    time.sleep(2)
                    st.write("")
                    st.session_state.default_index_reader_setup=2
                    st.experimental_rerun()
                else:
                    user_flag=0
                    st.warning('Passwords are not matching')
            else:

                st.warning('Please check the username')
    back,empty,next=st.columns([1,10,1],gap="large")
    with next:
        if st.button("Next",key='reader setup user'):
            st.session_state.default_index_reader_setup=2
            st.experimental_rerun()
    with back:
        if st.button("Back",key='reader setup user1'):
            st.session_state.default_index_reader_setup=0
            st.experimental_rerun()
###################################################################################

########################Create warehouse - reader account setup definition##############
def create_warehouse_for_reader_setup():
    @st.cache(suppress_st_warning=True)
    def run_reader(query):
        with st.session_state.conn_reader.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()
    with st.form('Warehouse'):
        wh_flag=0
        wn=st.text_input("Warehouse name")
        st.caption("Suggested name format: <PROJECT>_<ENV>_<BUSINESS_FUNCTION>")
        st.caption("For Eg: kipi_Dev_Share_wh")
        print(len(wn))
        ws=["XSMALL","SMALL","MEDIUM","LARGE","XLARGE","XXLARGE","XXXLARGE","4XLARGE","5XLARGE","6XLARGE"]
        WAREHOUSE_SIZE_BOX=st.selectbox("Select warehouse size",(ws))
        if WAREHOUSE_SIZE_BOX=='4XLARGE':
            WAREHOUSE_SIZE_BOX='X4LARGE'
        elif WAREHOUSE_SIZE_BOX=='5XLARGE':
            WAREHOUSE_SIZE_BOX='X5LARGE'
        elif WAREHOUSE_SIZE_BOX=='6XLARGE':
            WAREHOUSE_SIZE_BOX='X6LARGE'
        timelist=['5','10','15','20','30','45','60',]
        AUTO_SUSPEND_TIME_MIN=st.selectbox("Please enter suspend time in minutes",timelist)
        AUTO_SUSPEND=int(AUTO_SUSPEND_TIME_MIN)*60
        clusters_count=['1','2','3','4','5','6','7','8','9','10']
        MIN_CLUSTER_COUNT = st.selectbox("Enter minimum clusters required",clusters_count)
        MAX_CLUSTER_COUNT = st.selectbox("Enter maximum clusters required",clusters_count)
        if MIN_CLUSTER_COUNT > MAX_CLUSTER_COUNT:
            st.error("Minimum clusters required must be less than maximum clusters required")
        SCALING_POLICY_list=["STANDARD","ECONOMY"]
        SCALING_POLICY=st.selectbox("Select scaling policy size",(SCALING_POLICY_list))
        AUTO_RESUME=st.radio("Auto resume",('TRUE', 'FALSE',))
        if st.form_submit_button():
            if wn:
                rr=run_reader("CREATE WAREHOUSE "+wn+" WITH WAREHOUSE_SIZE = '"+WAREHOUSE_SIZE_BOX+"' WAREHOUSE_TYPE = 'STANDARD' AUTO_SUSPEND ="+str(AUTO_SUSPEND)+" AUTO_RESUME = "+AUTO_RESUME+" MIN_CLUSTER_COUNT = "+MIN_CLUSTER_COUNT+" MAX_CLUSTER_COUNT = "+MAX_CLUSTER_COUNT+" SCALING_POLICY = '"+SCALING_POLICY+"';")
                if rr:
                    st.success("Warehouse created!")
                    run_reader(f'GRANT USAGE ON WAREHOUSE {wn} TO ROLE {st.session_state.reader_setup_role};')
                    wh_flag=1
                    time.sleep(2)
                    st.write("")
                    st.session_state.default_index_reader_setup=3
                    st.experimental_rerun()
                else:
                    st.warning('Please check the details again')
                    wh_flag=0
            else:
                st.warning('Please enter warehouse name')
                wh_flag=0
    back,empty,next=st.columns([1,10,1],gap="large")
    with next:
        if st.button("Next",key='reader setup warehouse'):
            st.session_state.default_index_reader_setup=3
            st.experimental_rerun()
    with back:
        if st.button("Back",key='reader setup warehouse1'):      
            st.session_state.default_index_reader_setup=1
            st.experimental_rerun()
###################################################################################

########################Create resource monitor - reader account setup definition##############
def create_resource_monitor_for_reader_setup():
    @st.cache(suppress_st_warning=True)
    def run_reader(query):
        with st.session_state.conn_reader.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    with st.form('Resource Monitor'):
        run_reader('USE ROLE ACCOUNTADMIN;')
        st.markdown('''<h6 style="color:grey"><i>This is an optional step</i></h6>''',unsafe_allow_html=True)
        rm_name=st.text_input('Enter resource monitor name')
        rm_credits=st.text_input('Enter credit quota')
        rm_level=st.selectbox('Select monitor level',['ACCOUNT','WAREHOUSE'])
        if rm_level=='WAREHOUSE':
            run_reader('SHOW WAREHOUSES;')
            wh_list=run_reader('select \"name\" as warehouse_name from table(result_scan(last_query_id()));')
            whs=st.multiselect('Select warehouses you would like to monitor',beautify(wh_list))
        st.markdown('''     
                <h4 class="heading" style="margin-top: 20px;">Actions and notifications</h4>
                ''', unsafe_allow_html=True)
        st.caption('Specify what action to perform when the quota is reached - Please enter a value between 1 to 100 in whole(Not decimal)')
        suspend1=st.text_input('Suspend and notify when')
        suspend2=st.text_input('Suspend immediately and notify when')
        if st.form_submit_button():
            if rm_name and rm_credits.isnumeric() and suspend1.isnumeric() and suspend2.isnumeric():
                print('in if')
                if rm_level=='ACCOUNT':
                    account_query=f'CREATE RESOURCE MONITOR "{rm_name}" WITH CREDIT_QUOTA = {rm_credits}  TRIGGERS ON {suspend1} PERCENT DO SUSPEND  ON {suspend2} PERCENT DO SUSPEND_IMMEDIATE;'
                    run_reader(account_query)
                    run_reader(f'ALTER ACCOUNT SET RESOURCE_MONITOR = "{rm_name}";')
                    st.success('Resource Monitor created successfully!')
                    st.session_state.default_index_reader_setup=4
                    st.experimental_rerun()
                else:
                    print('Warehouse level')
                    wh_level_query=f'CREATE RESOURCE MONITOR "{rm_name}" WITH CREDIT_QUOTA = {rm_credits}  TRIGGERS ON {suspend1} PERCENT DO SUSPEND  ON {suspend2} PERCENT DO SUSPEND_IMMEDIATE;'
                    run_reader(wh_level_query)
                    for i in whs:
                        run_reader(f'ALTER WAREHOUSE "{i}" SET RESOURCE_MONITOR = "{rm_name}";')
                    st.success('Resource monitor created successfully!')
                    time.sleep(2)
                    st.write("")
                    st.session_state.default_index_reader_setup=4
                    st.experimental_rerun()

            else:
                st.warning('Please enter all the valid details')
    back,empty,next=st.columns([1,10,1],gap="large")
    with next:
        if st.button("Next",key='reader setup rm'):          
            st.session_state.default_index_reader_setup=4
            st.experimental_rerun()
    with back:
        if st.button("Back",key='reader setup rm1'):
            st.session_state.default_index_reader_setup=2
            st.experimental_rerun()
###################################################################################

########################Create database from share - reader account setup definition##############
def create_database_for_reader_setup():
    @st.cache(suppress_st_warning=True)
    def run_reader(query):
        with st.session_state.conn_reader.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    with st.form('Database'):
        run_reader("USE ROLE ACCOUNTADMIN;")
        run_reader("SHOW SHARES;")
        reader_accounts=run_reader("select \"owner_account\" || '.' || \"name\"as \"account_and_share\" from table(result_scan(last_query_id())) where \"kind\" = 'INBOUND' and \"database_name\"='';") ##Added by Nikhil Ranade to handle show shares issue###
        #validation to pick only those shares for which databases have not been created
        available_shares=[]
        for i in reader_accounts:
            available_shares.append(i)
        print('Available shares are: ',available_shares)
        #print('Available accounts are: ',availabe_accounts)
        print("Type of avaialbe shares is ",type(available_shares))
        box1=st.selectbox("Select from available shares",beautify(available_shares),key='box1')
        database_name=st.text_input('Database name','')
        run_reader("SHOW ROLES;")
        available_roles=run_reader("select \"name\" from table(result_scan(last_query_id()));")
        role_to_assign=st.multiselect('Select roles',beautify(available_roles))
        if st.form_submit_button():
            if len(box1)>0:
                if len(database_name)>0:
                    if len(role_to_assign)>0:
                        query_create_db=f"CREATE DATABASE IDENTIFIER ('\"{database_name}\"') FROM SHARE IDENTIFIER('{box1}');"
                        print(query_create_db)
                        run_reader(query_create_db)
                        for i in role_to_assign:
                            run_reader(f'GRANT IMPORTED PRIVILEGES ON DATABASE "{database_name}" TO ROLE "{i}";')
                        st.write("Database created successfully!!")
                        st.success('Reader account setup is completed!')
                    else:
                        st.warning("Please select a role")
                else:
                    st.warning("Please enter a database name")
            else:
                st.warning("Please select a share to create database")
    st.write('')
    if st.button("Back",key='reader setup rm1'):
        st.write('')
        st.session_state.default_index_reader_setup=3
        st.experimental_rerun()
###################################################################################
####################################
# Reader Account Setup Page Start
####################################

def Reader_Account_Setup():
    st.session_state.load_state_add_consumers_reader=False
    newbutton()
    st.session_state.load_state_monitor=False

    add_logo('./data/logo.png')

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
    if 'conn' not in st.session_state:
        st.session_state.conn=None
    if st.session_state.conn!=None:
        @st.experimental_singleton(suppress_st_warning=True)
        def init_reader(username_reader,password_reader,reader_account_name):
            return snowflake.connector.connect(user=f"{username_reader}",password=f"{password_reader}",account=f"{reader_account_name}")
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
                            
                except Exception as e:
                    print(e)
                    return {'success': False}
            else:
                with st.session_state.conn.cursor() as cur:
                    cur.execute(query)
                    return cur.fetchall()
                
        def beautify(db):
            special_char = '@!#$%^&*()<>?/\|}{~:;.[]'
            out_list = [''.join(filter(lambda i: i not in special_char, string)) for string in db]
            return out_list

       
        @st.cache(suppress_st_warning=True)
        def run_reader(query):
            with st.session_state.conn_reader.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()

        
        
        st.markdown('''     
                <h4 class="heading" style="margin-top: 20px; ">Reader account login</h4>
                ''', unsafe_allow_html=True)
        run_query("use secondary roles all;")
        run_query("use warehouse compute_wh;")
    ###code to fetch the list of available reader accounts####
        run_query('SHOW MANAGED ACCOUNTS;')
        reader_accounts=run_query("select concat(\"name\",' ','(',\"url\",')') as account_name from table(result_scan(last_query_id()));")
        box1=st.selectbox("Available reader accounts",beautify(reader_accounts),key='box1_reader')
        username_reader=st.text_input('Enter username')
        password_reader=st.text_input('Enter password',type='password')
        print('type of box is ',type(box1))
        if 'load_state_reader_setup' not in st.session_state:
            st.session_state.load_state_reader_setup=False
        if 'conn_reader' not in st.session_state:
            st.session_state.conn_reader=None
        if st.button('Submit',key='reader_setup_submit') or st.session_state.load_state_reader_setup:
            st.session_state.load_state_reader_setup=True
            reader_account_name=box1.split(' ')[0]
            reader_account_url=box1.split(' ')[1].replace('(','').replace(')','')
            print("Start URl",reader_account_url)
            if reader_account_url[0:8]=="https://":
                if reader_account_url[0:11]!="https://app":
                    print("2")
                    reader_a=reader_account_url.split('.snowflake')
                    reader_l=reader_a[0]
                    reader_account_url=reader_l[8:]
                elif 'app.snowflake.com' in reader_account_url.split('/'):
                    reader_b=reader_account_url.split('.snowflake')
                    reader_a=reader_account_url.split('/')
                    reader_h=reader_a[3].split('.')
                    if (len(reader_h)==1):
                        reader_l=reader_b[1]
                        reader_k=reader_l.split('/')
                        reader_account_url=reader_k[2]
                    else:
                        reader_l=reader_a[4]
                        reader_m=reader_a[3]
                        reader_account_url=reader_l+'.'+reader_m
            else:
                reader_account_url=reader_account_url
            print("End reader_account_url",reader_account_url)
            print("username_reader=",username_reader)
            print("Password=",password_reader)


            print('reader account URL is:',reader_account_url)
            print('user is:'+username_reader+' password is '+password_reader+' account is '+reader_account_name)
            st.session_state.conn_reader=init_reader(username_reader,password_reader,reader_account_url)
            print('connection string is ',st.session_state.conn_reader)
            reader_account_locator_list_setup=[]
            run_query('SHOW MANAGED ACCOUNTS;')
            reader_account_locator_tupple_setup=run_query(f"select \"locator\" as locator from table(result_scan(last_query_id())) where \"name\"='{reader_account_name}'")
            for r in reader_account_locator_tupple_setup:
                for l in r:
                    reader_account_locator_list_setup.append(l)
            reader_account_locator_setup=reader_account_locator_list_setup[0].replace("'","").replace('[','').replace(']','')
            available_wh_reader=run_query(f"SELECT DISTINCT WAREHOUSE_NAME FROM SNOWFLAKE.READER_ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY WHERE READER_ACCOUNT_NAME = '{reader_account_locator_setup}' AND WAREHOUSE_NAME != 'CLOUD_SERVICES_ONLY' LIMIT 1;")
            if len(available_wh_reader)==1:
                available_wh_reader_clean=available_wh_reader[0][0].replace("'","").replace('[','').replace(']','')
                print("clean warehouse:",available_wh_reader_clean)
                run_reader(f"USE WAREHOUSE {available_wh_reader_clean};")
            else:
                run_reader("create warehouse if not exists compute_wh;")

####################################
# Reader Account Setup Page end
####################################
####################################
# Reader Drop Objects Page start
####################################
def Drop_Objects():
    st.session_state.load_state_add_consumers_reader=False
    submitbutton()
    newbutton()
    st.session_state.load_state_reader_setup=False
    st.session_state.load_state_monitor=False

    add_logo('./data/logo.png')
    if 'conn' not in st.session_state:
        st.session_state.conn=None
    if st.session_state.conn!=None:

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
                except Exception as e:
                    print(e)
                    return {'success': False}
            else:
                with st.session_state.conn.cursor() as cur:
                    cur.execute(query)
                    return cur.fetchall()
        
        run_query("use secondary roles all;")
        run_query("use role SHAREMON_ADMIN;")
        run_query("use warehouse SHAREMON_WH;")

        run_query("ALTER SESSION SET USE_CACHED_RESULT = FALSE")


        run_query("show shares;")
        outboundshares=run_query("select \"name\" from table(result_scan(last_query_id())) where \"kind\"='OUTBOUND';")
        B_outboundshares=(beautify(outboundshares))

        data_types_list=["FLOAT","VARCHAR","NUMBER","DECIMAL","NUMERIC","INT","INTEGER","BIGINT","CHAR","CHARACTER","STRING","TEXT","BINARY","BOOLEAN","DATE","DATETIME","TIME","VARIANT",")"]
        share_name_list_drop=[]

        for share in B_outboundshares:
            if share not in share_name_list_drop:
                share_name_list_drop.append(share) 
        if(share_name_list_drop[0] != 'select'):
            share_name_list_drop.insert(0,"select")
            # selectin share
        Share_name_drop=st.selectbox("Displaying the available outbound shares",(share_name_list_drop))
        print("Share_name_drop=",Share_name_drop)
        if len(Share_name_drop)>0 and Share_name_drop != 'select':
            seltables=''
            selviews=''
            selfunctions=''
            selet=''
            remover=[]
            funcremover=[]
            refusagelst=[]
            refusagelstnew=[]
            run_query("DESC SHARE identifier('"+Share_name_drop+"');")
            get_schema_of_share=beautify(run_query("select $2 from table(result_scan(last_query_id())) where $1='SCHEMA' limit 1;"))
            if get_schema_of_share:
                print("get_schema_of_share",get_schema_of_share)
                run_query(f'use schema {str(get_schema_of_share[0])}')


            run_query("DESC SHARE identifier('"+Share_name_drop+"');")
            tables_in_share=beautify(run_query("select $2 from table(result_scan(last_query_id())) where $1='TABLE';"))
            print("Tables",tables_in_share)
            if tables_in_share:
                seltables=st.multiselect("Tables present in selected share "+Share_name_drop+"",tables_in_share)
                remover.append(seltables)

            run_query("DESC SHARE identifier('"+Share_name_drop+"');")
            views_in_share=beautify(run_query("select $2 from table(result_scan(last_query_id())) where $1='VIEW';"))
            if views_in_share:
                selviews=st.multiselect("Views present in selected share "+Share_name_drop+"",views_in_share)
                remover.append(selviews)
                if len(selviews)>0:
                    run_query('''create procedure if not exists get_ref_db(DB VARCHAR, SC VARCHAR,VW VARCHAR)
                    returns varchar not null
                    language javascript
                    execute as caller
                    as
                    $$
                    var sql_command1 = snowflake.createStatement({ sqlText:`select listagg(distinct referenced_database_name,',') within group (order by referenced_database_name) "referenced_database_names"
                    from table(get_object_references(database_name=>`+DB+`, schema_name=>`+SC+`, object_name=>`+VW+`));`});
                    var col_list = [];
                    try
                    {
                    var col = sql_command1.execute();
                    while (col.next())
                    {
                    var col_name= col.getColumnValue(1);
                    col_list.push([col_name]);
                    }
                    return col_list;
                    }
                    catch (err)
                    {
                    return "Failed: " + err;
                    }
                    $$;
                    ''')
                    for eachview in selviews:
                        Z=eachview.split('.')
                        print("view_sep",Z[0],Z[1],Z[2])
                        ext_db=beautify(run_query("call get_ref_db('"+Z[0]+"','"+Z[1]+"','"+Z[2]+"');"))
                        refusagelst.append(*ext_db)
                        for db in refusagelst:
                            db_temp = db.split(',')
                            print("dbtemp=",db_temp)
                            for item in db_temp:
                                refusagelstnew.append(item)
                        print("refusageist",refusagelstnew)
                        for i in refusagelstnew:
                            run_query("REVOKE REFERENCE_USAGE ON DATABASE "+i+" FROM SHARE "+Share_name_drop+";")
                        print("ext db remover",ext_db)

            run_query("DESC SHARE identifier('"+Share_name_drop+"');")
            functions_in_share=beautify(run_query("select $2 from table(result_scan(last_query_id())) where $1='FUNCTION';"))
            if functions_in_share:

                selfunctions=st.multiselect("Functions present in selected share "+Share_name_drop+"",functions_in_share)
                funcremover.append(selfunctions)
            print(selfunctions)

            run_query("DESC SHARE identifier('"+Share_name_drop+"');")
            et_in_share=beautify(run_query("select $2 from table(result_scan(last_query_id())) where $1='EXTERNAL_TABLE';"))
            if et_in_share:
                selet=st.multiselect("External tables present in selected share "+Share_name_drop+"",et_in_share)
                remover.append(selet)
            print(selet)
            clearselection, empty1, empty2, RemoveObjects = st.columns([4, 5, 1, 2.5], gap="large")
            if len(Share_name_drop)>=1 and 'select' not in Share_name_drop and len(seltables)==0 and len(selviews)==0 and len(selfunctions)==0 and len(selet)==0:
                with RemoveObjects:
                    drop=st.button("Drop share")
                    if drop:
                        run_query('DROP SHARE "'+str(Share_name_drop)+'";')
                        st.success("Share Dropped successfully")
                        time.sleep(5)
                        st.experimental_rerun()



            
            if len(Share_name_drop)>=1 and 'select' not in Share_name_drop and ( len(seltables)>0 or len(selviews)>0 or len(selfunctions)>0 or len(selet)>0):
                with RemoveObjects:
                    RemoveObjects=st.button("Remove objects")
                    print("remover1",remover)
                    remover = np.concatenate(remover)
                    funcremover=beautify(funcremover)
                    if RemoveObjects:
                        
                        
                        if len(remover)>0:
                            print("remover=",remover)
                            for obj in remover:
                                print("obj=",obj)
                                if len(obj)>0:
                                    run_query("REVOKE SELECT ON VIEW "+str(obj)+" FROM SHARE "+str(Share_name_drop)+";")

                        print("funcremover",funcremover)
                        print("funcremover len",len(funcremover))
                        if len(funcremover)>0 and '' not in funcremover:
                            for obj in funcremover:
                                    print(obj)
                                    udfrem=removedoublequote(obj)
                                    cutudf=udfrem.split("(")
                                    print(cutudf[0])
                                    for i in data_types_list:
                                        if i in cutudf[1]:
                                            cutudf[1]="("+i+")"
                                            print("succ")
                                            if i==")":
                                                cutudf[1]="()"
                                            break

                                    udfrem=cutudf[0]+cutudf[1]    
                                    run_query("REVOKE all privileges on FUNCTION "+str(udfrem)+" FROM SHARE "+str(Share_name_drop)+";")
                        st.success("Object removed successfully")
            with clearselection:
                if st.button('Clear selection'):
                    st.empty()
    else:
        st.warning('Please login again')



####################################
# Reader Drop Objects Page end
####################################
####################################
# Reader Monitor Page start
####################################
def Monitor():
    st.session_state.load_state_add_consumers_reader=False
    newbutton()
    st.session_state.load_state_reader_setup=False
    

    if 'conn' not in st.session_state:
        st.session_state.conn=None
    if st.session_state.conn!=None:

        st.session_state.load_state_reader_setup=False

        @st.cache(suppress_st_warning=True)
        def run_reader(query):
            with ctx.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()

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
                except Exception as e:
                    print(e)
                    return {'success': False}
            else:
                with st.session_state.conn.cursor() as cur:
                    cur.execute(query)
                    return cur.fetchall()
        

        run_query("use secondary roles all;")
        run_query("ALTER SESSION SET USE_CACHED_RESULT = FALSE")
        run_query("use role SHAREMON_ADMIN;")
        run_query("use warehouse SHAREMON_WH;")
        run_query("show shares;")
        outboundshares=run_query("select \"name\" from table(result_scan(last_query_id())) where \"kind\"='OUTBOUND';")
        B_outboundshares=(beautify(outboundshares))


        share_name_list = []
        for share in B_outboundshares:
            if share not in share_name_list:
                share_name_list.append(share) 
        if(share_name_list[0] != 'select'):
            share_name_list.insert(0,"select")
        Share_name_monitor=st.selectbox("Displaying the available outbound shares",(share_name_list))
        if len(Share_name_monitor)>=1 and 'select' not in Share_name_monitor:
            run_query("show shares;")
            table=run_query(f'''with shares_info as (select org."name" as "share_name",
            org."database_name",
            table1.value as "consumer_account" ,
            org."owner",
            org."comment",
                case
                    when SPLIT_PART("owner_account",'.',0)=SPLIT_PART("to",'.',0) then 'Reader Account'
                    else 'Full Account'
                    end as "Account_type",
                    org."created_on"
            from table(result_scan(last_query_id())) as org ,table(split_to_table(org."to", ',')) as table1
            where "kind"='OUTBOUND' and length("to")>1 ) select $2 as Database_Associated, SPLIT_PART($3,'.',2) as Consumer_Account, $6 as Account_Type,$7 from shares_info where $1='{Share_name_monitor}' ;''') # Change the query to handle show shares command
            
            finaltable_df=pd.DataFrame(table, columns=['Database_Associated','Consumer_Account','Account_Type','Created on'])
            print("Shares dataframe is:",finaltable_df)
            st.dataframe(finaltable_df,width=1200)

        run_query("show shares;")
        account_locator=beautify(run_query(''' with shares_info as (select org."name" as "share_name",
            org."database_name",
            table1.value as "consumer_account" ,
            org."owner",
            org."comment",
                case
                    when SPLIT_PART("owner_account",'.',0)=SPLIT_PART("to",'.',0) then 'Reader Account'
                    else 'Full Account'
                    end as "Account_type",
                    org."created_on"
            from table(result_scan(last_query_id())) as org ,table(split_to_table(org."to", ',')) as table1
            where "kind"='OUTBOUND' and length("to")>1 ) select distinct SPLIT_PART($3,'.',2) from shares_info  ; '''))
        account_locator.insert(0, "select")
        consumer_selected=st.selectbox("Select the consumer",account_locator)
        if len(consumer_selected)>1 and 'select' not in consumer_selected:
            run_query("show shares;")
            info_account_locator=run_query(f'''  with shares_info as (select "name" AS "share_name",
                org."database_name",
                table1.value as "consumer_account" ,
                org."owner",
                org."comment",
                    case
                        when SPLIT_PART("owner_account",'.',0)=SPLIT_PART("to",'.',0) then 'Reader Account'
                        else 'Full Account'
                        end as "Account_type",
                        org."created_on"
                from table(result_scan(last_query_id())) as org ,table(split_to_table(org."to", ',')) as table1
                where "kind"='OUTBOUND' and length("to")>1 ) select "share_name" as sharename,$2 as Database_Associated, SPLIT_PART($3,'.',2) as Consumer_Account, $6 as Account_Type,$7 from shares_info where $3 like'%{consumer_selected}%' ;  ''')  #Changed the query by Nikhil Ranade to handle show shares command
            info_account_locator_df=pd.DataFrame(info_account_locator,columns=['Share Name','Database_Associated','Consumer_Account','Account_Type','Created on'])
            st.dataframe(info_account_locator_df,width=1200)
        #####################################################################################################
        st.markdown('''     
                <h4 class="heading" style="margin-top: 20px;">Reader account monitoring</h4>
                ''', unsafe_allow_html=True)
        select =option_menu(
                menu_title=None,
                options=["Storage usage","Warehouse history","Resource monitors","Last login"],
                styles={
                        "container": {"font-family": "Source Sans Pro"},
                        "icon": {"color": "white", "font-size": "16px", "text-align": "center"},
                        "nav-link": {"font-size": "15px", "text-align": "center", "margin": "10px"},
                        "nav-link-selected": {"color": "#ffffff","background-color": "#B3D943"},                        
                    },
                icons=["house-fill","person-square","gear","eye"],
                orientation="horizontal",
        )
        if (select== "Storage usage"):
            st.write("Reader account storage usage")
            STORAGE_USAGE=run_query("select distinct(READER_ACCOUNT_NAME),SUM(STORAGE_BYTES),SUM(STAGE_BYTES) FROM SNOWFLAKE.READER_ACCOUNT_USAGE.STORAGE_USAGE GROUP BY READER_ACCOUNT_NAME ;")
            STORAGE_USAGE_df=pd.DataFrame(STORAGE_USAGE, columns=['READER_ACCOUNT_NAME','STORAGE_BYTES','STAGE_BYTES'])
            STORAGE_USAGE_df['STORAGE_BYTES'] = STORAGE_USAGE_df['STORAGE_BYTES'].astype(float)
            STORAGE_USAGE_df['STAGE_BYTES'] = STORAGE_USAGE_df['STAGE_BYTES'].astype(float)
            st.dataframe(STORAGE_USAGE_df,width=1200)
        elif(select == "Warehouse history"):
            st.write("Reader account warehouse metering history")
            WAREHOUSE_METERING_HISTORY=run_query("select distinct READER_ACCOUNT_NAME,SUM(CREDITS_USED),ListAgg(WAREHOUSE_NAME,', ') from SNOWFLAKE.READER_ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY Group by READER_ACCOUNT_NAME;")
            WAREHOUSE_METERING_HISTORY_df=pd.DataFrame(WAREHOUSE_METERING_HISTORY, columns=['READER_ACCOUNT_NAME','CREDITS_USED','WAREHOUSE_NAME'])
            WAREHOUSE_METERING_HISTORY_df['CREDITS_USED'] = WAREHOUSE_METERING_HISTORY_df['CREDITS_USED'].astype(float)
            st.dataframe(WAREHOUSE_METERING_HISTORY_df,width=1200)
        elif(select=="Resource monitors"):
            RESOURCE_MONITORS=run_query("SELECT distinct READER_ACCOUNT_NAME,NAME,CREDIT_QUOTA,USED_CREDITS,REMAINING_CREDITS FROM SNOWFLAKE.READER_ACCOUNT_USAGE.RESOURCE_MONITORS;")
            RESOURCE_MONITORS_df=pd.DataFrame(RESOURCE_MONITORS, columns=['READER_ACCOUNT_NAME','NAME','CREDIT_QUOTA','USED_CREDITS','REMAINING_CREDITS'])
            #print(RESOURCE_MONITORS_df)
            if((RESOURCE_MONITORS_df['CREDIT_QUOTA']=='null').any() | (RESOURCE_MONITORS_df['CREDIT_QUOTA']=='NULL').any() | (RESOURCE_MONITORS_df['CREDIT_QUOTA']==None).any()):
                st.error("You have Null or empty values in the column CREDIT_QUOTA")
                #RESOURCE_MONITORS_df['CREDIT_QUOTA'] = RESOURCE_MONITORS_df['CREDIT_QUOTA'].astype(float)
            else:
                RESOURCE_MONITORS_df['CREDIT_QUOTA'] = RESOURCE_MONITORS_df['CREDIT_QUOTA'].astype(float)
                #st.error("You have Null or empty values in the column CREDIT_QUOTA")
            RESOURCE_MONITORS_df['USED_CREDITS'] = RESOURCE_MONITORS_df['USED_CREDITS'].astype(float)
            if((RESOURCE_MONITORS_df['REMAINING_CREDITS']=='NULL').any() | (RESOURCE_MONITORS_df['REMAINING_CREDITS']=='null').any() | (RESOURCE_MONITORS_df['REMAINING_CREDITS']==None).any()):    
                st.error("You have Null or empty values in the column REMAINING_CREDITS")
                #RESOURCE_MONITORS_df['REMAINING_CREDITS'] = RESOURCE_MONITORS_df['REMAINING_CREDITS'].astype(float)
            else:
                RESOURCE_MONITORS_df['REMAINING_CREDITS'] = RESOURCE_MONITORS_df['REMAINING_CREDITS'].astype(float)
                #st.error("You have Null or empty values in the column REMAINING_CREDITS")
            st.dataframe(RESOURCE_MONITORS_df,width=1200)
        elif(select=="Last login"):
            Last_Login=run_query("select distinct READER_ACCOUNT_NAME,EVENT_TIMESTAMP as LAST_LOGIN_TIME from SNOWFLAKE.READER_ACCOUNT_USAGE.LOGIN_HISTORY lh1 where EVENT_TIMESTAMP=(select max(EVENT_TIMESTAMP) from SNOWFLAKE.READER_ACCOUNT_USAGE.LOGIN_HISTORY lh2 where lh1.reader_account_name=lh2.reader_account_name ) AND IS_SUCCESS='YES';")
            Last_Login_df=pd.DataFrame(Last_Login, columns=['READER_ACCOUNT_NAME','LAST_LOGIN_TIMESTAMP'])
            st.dataframe(Last_Login_df,width=1200)
        #################################################################################################


        @st.experimental_singleton(suppress_st_warning=True)
        def init_reader(username,password,reader_account_name):
            return snowflake.connector.connect(user=f"{username}",password=f"{password}",account=f"{reader_account_name}")
        #Setting up the Title
        st.markdown('''     
                <h4 class="heading" style="margin-top: 20px;">Select a reader account of your choice</h4>
                ''', unsafe_allow_html=True)

        #code to fetch the list of available reader accounts
        run_query('USE ROLE ACCOUNTADMIN;')
        run_query('SHOW MANAGED ACCOUNTS;')
        reader_accounts=run_query("select concat(\"name\",' ','(',\"url\",')') as account_name from table(result_scan(last_query_id()));")
        box1=st.selectbox("Reader accounts",beautify(reader_accounts),key='box1')
        username_monitor=st.text_input('Username')
        password_monitor=st.text_input('Password',type='password')
        print('type of box is ',type(box1))
        if 'load_state_monitor' not in st.session_state:
            st.session_state.load_state_monitor=False
        if st.button('Submit',key="submit_monitor") or st.session_state.load_state_monitor:
            st.session_state.load_state_monitor=True
            reader_account_name=box1.split(' ')[0]
            reader_account_url=box1.split(' ')[1].replace('(','').replace(')','')
            print("Start URl",reader_account_url)
            if reader_account_url[0:8]=="https://":
                if reader_account_url[0:11]!="https://app":
                    print("2")
                    reader_monitor_a=reader_account_url.split('.snowflake')
                    reader_monitor_l=reader_monitor_a[0]
                    reader_account_url=reader_monitor_l[8:]
                elif 'app.snowflake.com' in reader_account_url.split('/'):
                    reader_monitor_b=reader_account_url.split('.snowflake')
                    reader_monitor_a=reader_account_url.split('/')
                    reader_h=reader_monitor_a[3].split('.')
                    if (len(reader_h)==1):
                        reader_monitor_l=reader_monitor_b[1]
                        reader_monitor_k=reader_monitor_l.split('/')
                        reader_account_url=reader_monitor_k[2]
                    else:
                        reader_monitor_l=reader_monitor_a[4]
                        reader_monitor_m=reader_monitor_a[3]
                        reader_account_url=reader_monitor_l+'.'+reader_monitor_m
            else:
                reader_account_url=reader_account_url
            print("End reader_account_url",reader_account_url)
            print("username_reader=",username_monitor)
            print("Password=",password_monitor)

            ctx=init_reader(username_monitor,password_monitor,reader_account_url)
            print('connection string is ',ctx)
            if 'load_state_monitor_1' not in st.session_state:
                st.session_state.load_state_monitor_1=False
            if ctx or st.session_state.load_state_monitor_1:
                st.session_state.load_state_monitor_1=True
                cloud_provider_new_list=[]
                cost_table = pd.read_csv('Cost Table.csv')
                cloud_provider_new=run_reader('select current_region();')
                for t in cloud_provider_new:
                    for x in t:
                        cloud_provider_new_list.append(x)
                print('List is ',cloud_provider_new_list)
                print('New cloud provider is ',cloud_provider_new_list[0])
                print(cost_table)

                cloud_provider=cloud_provider_new_list[0]
                print('Cloud provider is ',cloud_provider)
                for i in cost_table.index:
                    if(cost_table['Cloud_Provider'][i]==cloud_provider):
                        STANDARD_EDITION_COST=cost_table['STANDARD'][i]
                        ENTERPRISE_EDITION_COST=cost_table['ENTERPRISE'][i]
                        BUSINESS_EDITION_COST=cost_table['BUSINESS_CRITICAL'][i]
                        ON_DEMAND=cost_table['ON _DEMAND'][i]
                        CAPACITY_STORAGE=cost_table['CAPACITY_STORAGE'][i]
                reader_account_locator_list_monitor=[]
                #print('On demand cost is '+str(ON_DEMAND)+' and capacity storage cost is '+str(CAPACITY_STORAGE))
                cs = ctx.cursor()
                cs.execute('USE ROLE ACCOUNTADMIN;')
                run_query('SHOW MANAGED ACCOUNTS;')
                reader_account_locator_tupple_monitor=run_query(f"select \"locator\" as locator from table(result_scan(last_query_id())) where \"name\"='{reader_account_name}'")
                for r in reader_account_locator_tupple_monitor:
                    for l in r:
                        reader_account_locator_list_monitor.append(l)
                reader_account_locator_monitor=reader_account_locator_list_monitor[0].replace("'","").replace('[','').replace(']','')
                
                available_wh_reader_monitor=run_query(f"SELECT DISTINCT WAREHOUSE_NAME FROM SNOWFLAKE.READER_ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY WHERE READER_ACCOUNT_NAME = '{reader_account_locator_monitor}' AND WAREHOUSE_NAME != 'CLOUD_SERVICES_ONLY' LIMIT 1;")
                if len(available_wh_reader_monitor)==1:
                    available_wh_reader_clean_monitor=available_wh_reader_monitor[0][0].replace("'","").replace('[','').replace(']','')

                    cs.execute(f"USE WAREHOUSE {available_wh_reader_clean_monitor};")
                else:
                    cs.execute('CREATE WAREHOUSE IF NOT EXISTS MONITOR_WH;')
                    cs.execute('USE WAREHOUSE MONITOR_WH;')

                navbar_options = option_menu(
                    menu_title=None,
                    options=["Compute cost", "Storage cost"],
                    icons=['coin', 'hdd-fill', 'hdd-stack-fill'],
                    menu_icon="cast",
                    orientation="horizontal",

                    styles={
                        "container": {"font-family": "Source Sans Pro"},
                        "icon": {"color": "white", "font-size": "16px", "text-align": "center"},
                        "nav-link": {"font-size": "15px", "text-align": "center", "margin": "10px"},
                        "nav-link-selected": {"color": "#ffffff","background-color": "#B3D943"},
                        
                    }
                )

                if navbar_options == "Compute cost":
                    monitor_option = ['ROLE LEVEL', 'WAREHOUSE LEVEL', 'USER LEVEL']

                    option_selected = st.selectbox('Select level', monitor_option)
                    if option_selected == '--':
                        pass
                    elif "ROLE" in option_selected:
                        df = pd.read_sql(f"WITH ROLE_RESULT AS (select convert_timezone('UTC', start_time)::date as date,ROLE_NAME,user_name,warehouse_name ,count(*) as stmt_cnt, sum(total_elapsed_time/1000 *case warehouse_size  when 'X-Small' then 1/60/60 when 'Small'   then 2/60/60  when 'Medium'  then 4/60/60 when 'Large'   then 8/60/60 when 'X-Large' then 16/60/60 when '2X-Large' then 32/60/60 when '3X-Large' then 64/60/60 when '4X-Large' then 128/60/60 else 0 end) as estimated_credits,estimated_credits * {STANDARD_EDITION_COST} AS estimated_cost from snowflake.account_usage.query_history group by 1, 2, 3, 4 order by 1 desc, 4  desc, 2)  SELECT sum(estimated_credits) as estimated_credits,sum(estimated_cost) as estimated_cost,date,role_name FROM ROLE_RESULT group by role_name,date;",ctx)
                        fig = px.bar(df, x='ESTIMATED_CREDITS', y='DATE', color='ROLE_NAME', orientation='h')
                        fig.update_yaxes(type='category')
                        st.plotly_chart(fig, use_container_width=True)
                        st.dataframe(df,width=1200)

                    elif "USER" in option_selected:
                        df = pd.read_sql(f"WITH USER_RESULT AS( Select convert_timezone('UTC', START_TIME)::date as date, user_name, count(*) as stmt_cnt, sum(total_elapsed_time/1000 *	 case warehouse_size when 'X-Small' then 1/60/60 when 'Small'   then 2/60/60 when 'Medium'  then 4/60/60  when 'Large'   then 8/60/60 when 'X-Large' then 16/60/60 when '2X-Large' then 32/60/60	 when '3X-Large' then 64/60/60	 when '4X-Large' then 128/60/60	 else 0		 end) as estimated_credits,estimated_credits * {STANDARD_EDITION_COST} AS estimated_cost from snowflake.account_usage.query_history group by 1,2 order by 1 desc,4 desc,2) SELECT sum(ESTIMATED_CREDITS) as ESTIMATED_CREDITS,sum(ESTIMATED_COST) as ESTIMATED_COST,DATE,USER_name FROM USER_RESULT group by USER_NAME,DATE;",ctx)
                        fig = px.bar(df, x='ESTIMATED_CREDITS', y='DATE', color='USER_NAME', orientation='h')
                        fig.update_yaxes(type='category')
                        st.plotly_chart(fig, use_container_width=True)
                        st.dataframe(df,width=1200)
                    elif "WAREHOUSE" in option_selected:
                        df = pd.read_sql(f"with result as (SELECT WAREHOUSE_NAME, convert_timezone('UTC', a.start_time)::date as date, SUM(CREDITS_USED) AS DAILY_CREDITS_USED, SUM(CREDITS_USED_COMPUTE) AS DAILY_CREDITS_USED_COMPUTE, SUM(CREDITS_USED_CLOUD_SERVICES) AS DAILY_CREDITS_USED_CLOUD, DAILY_CREDITS_USED*{STANDARD_EDITION_COST}  AS DAILY_WAREHOUSE_USAGE_COST FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY a GROUP BY a.WAREHOUSE_NAME, a.START_TIME )SELECT sum(DAILY_CREDITS_USED) as DAILY_CREDITS_USED,sum(DAILY_WAREHOUSE_USAGE_COST) as DAILY_WAREHOUSE_USAGE_COST,date,WAREHOUSE_NAME from result group by WAREHOUSE_name,date; ;",ctx)
                        fig = px.bar(df, x='DAILY_CREDITS_USED', y='DATE', color='WAREHOUSE_NAME', orientation='h')
                        fig.update_yaxes(type='category',categoryorder='category ascending')
                        st.plotly_chart(fig, use_container_width=True)
                        st.dataframe(df,width=1200)
                # =============================================== Storage Cost =========================================================================================================
                # =============================================== Storage Cost =========================================================================================================
                # =============================================== Storage Cost =========================================================================================================
                # =============================================== Storage Cost =========================================================================================================
                # =============================================== Storage Cost =========================================================================================================
                # =============================================== Storage Cost =========================================================================================================

                elif navbar_options == 'Storage cost':
                    reader_account_locator_list=[]
                    run_query('SHOW MANAGED ACCOUNTS;')
                    reader_account_locator_tupple=run_query(f"select \"locator\" as locator from table(result_scan(last_query_id())) where \"name\"='{reader_account_name}'")
                    for r in reader_account_locator_tupple:
                        for l in r:
                            reader_account_locator_list.append(l)
                    reader_account_locator=reader_account_locator_list[0].replace("'","").replace('[','').replace(']','')
                    df = pd.read_sql(f"select READER_ACCOUNT_NAME,USAGE_DATE,STORAGE_BYTES/(1024*1024*1024*1024) AS STORAGE_TB ,STAGE_BYTES/(1024*1024*1024*1024) AS STAGE_TB,FAILSAFE_BYTES/(1024*1024*1024*1024) AS FAILSAFE_TB, (STORAGE_TB+STAGE_TB+FAILSAFE_TB) * {CAPACITY_STORAGE} as ACC_CAPACITY_COST,(STORAGE_TB+STAGE_TB+FAILSAFE_TB) * {ON_DEMAND} as ACC_ON_DEMAND_COST from SNOWFLAKE.READER_ACCOUNT_USAGE.STORAGE_USAGE WHERE READER_ACCOUNT_NAME = '{reader_account_locator}';",st.session_state.conn)
                    print(df)
                    yaxes = df['USAGE_DATE'].tolist()
                    fig = go.Figure(data=[
                        go.Bar(name='ACC_CAPACITY_COST', x=df['ACC_CAPACITY_COST'].tolist(), y=yaxes, orientation='h')
                    ])
                    # Change the bar mode
                    fig.update_layout(barmode='stack', title='Account Storage Cost')
                    st.plotly_chart(fig, use_container_width=True)
                    st.dataframe(df,width=1200)
    else:
        st.warning('Please login!')




####################################
# Reader Monitor Page end
####################################

selected = "Share"
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        
        options=["Share","Objects","Consumers","Reader account","Monitor","Logout"],
        icons=["share","nut","person-plus","book","eye","bi-box-arrow-right"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "25px", "background-color": "transparent"},
            "icon": {"color": "#FFFFFF", "font-size": "16px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "right",
                "margin": "0px",
                "font-weight": "100",
                "background-color": "transparent"
            },
            "nav-link-selected": { "color":"#B3D943", "font-weight": "100", "background-color": "transparent"},
        },
    )
    return selected
selected = "Home"
selected1="Add"
def Objects():

    options=["Add objects", "Drop objects"]
    selected1=st.radio(" ",options)
    return selected1
if st.session_state.conn==None:
    with placeholder.container():
        Login_Pannel()
        run_custom_code()
###################################
# create share nav bar start
###################################  
if 'default_index' not in st.session_state:
    st.session_state.default_index=0
def create_share_nav():
    create_share_nav_options = option_menu(
        menu_title=None,
        options=["Warehouse","Create Share"],
        default_index=st.session_state.default_index,
        orientation="horizontal",
        styles={
            "container": {"padding": "20px", },
            "icon": {"color": "#FFFFFF", "font-size": "16px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "centre",
                "margin": "0px",
                "font-weight": "100",
                "background-color": "transparent",
                "pointer-events": "none"
            },
            "nav-link-selected": { "color":"#B3D943", "font-weight": "100", "background-color": "transparent"},
        },
    )

    return create_share_nav_options
###################################
# create share nav bar end
###################################  
#####################################
# Reader account setup nav bar start
###################################  

def reader_account_setup_nav_bar():
    if 'default_index_reader_setup' not in st.session_state:
        st.session_state.default_index_reader_setup=0
    selected_reader_setup = option_menu(
            menu_title=None,
            options=["Create role","Create user","Create warehouse","Create resource monitor","Create database"],
            icons=["person-badge","people","device-ssd","eye","box-seam"],
            default_index=st.session_state.default_index_reader_setup,
            orientation="horizontal",
            styles={
                "container": {"padding": "20px", },
                "icon": {"color": "#FFFFFF", "font-size": "16px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "centre",
                    "margin": "0px",
                    "font-weight": "100",
                    "background-color": "transparent",
                    "pointer-events": "none"
                },
                "nav-link-selected": { "color":"#B3D943", "font-weight": "100", "background-color": "transparent"},
            },
        )
    return selected_reader_setup
#####################################
# Reader account setup nav bar end
################################### 
if st.session_state.conn!=None:
    with st.container():
        logo, menu = st.columns([1, 5], gap="small")

        with logo:
            logoimage = Image.open('./data/KIPI_Logo_Design.webp')
            st.image(logoimage)
        
        with menu:
            selected = streamlit_menu()   
            print("connection success")
        placeholder.empty() 
        if selected == "Login":
            Login_Pannel()
            run_custom_code()
        elif selected == "Share":
                Create_shares()
        elif selected == "Objects":
            selected1=Objects()
            if (selected1=="Add objects"):
                Add_Objects()
            if(selected1=="Drop objects"):
                Drop_Objects()
        elif selected=="Consumers":
            Add_Consumers()
            run_custom_code()
        elif selected=="Reader account":
            Reader_Account_Setup()
            if st.session_state.conn_reader:
                selected_reader_setup=reader_account_setup_nav_bar()
                if selected_reader_setup=="Create role":
                    create_role_for_reader_setup()
                    print("value after creating role is ",st.session_state.default_index_reader_setup)
                elif selected_reader_setup=="Create user":
                    create_user_for_reader_setup()
                elif selected_reader_setup=="Create warehouse":
                    create_warehouse_for_reader_setup()
                elif selected_reader_setup=="Create resource monitor":
                    create_resource_monitor_for_reader_setup()
                elif selected_reader_setup=="Create database":
                    create_database_for_reader_setup()
            st.session_state.conn_reader=None


        elif selected=="Monitor":
            Monitor()
        elif selected=="Logout":
            st.write('Logged out successfully!')
            st.session_state.conn=None
            for key in st.session_state.keys():
                del st.session_state[key]
            Login_Pannel()
            run_custom_code()
            st.experimental_rerun()