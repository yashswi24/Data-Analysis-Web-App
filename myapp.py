import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

st.set_page_config(page_title="EDA App", page_icon=":bar_chart:")


#Navigation Bar
selected=option_menu(
       
       menu_title=None,
       options=["Home","Demo","About"],
       icons=["house","book","pen"],
       menu_icon="cast",
       default_index=0,
       
)

    


# Web App Title
st.markdown('''
## **The Data Analysis App**

Data analysis is a process of inspecting, cleansing, transforming, and modelling data with the goal of 
discovering useful information, informing conclusions, and supporting decision-making.
Data analysis has multiple facets and approaches, encompassing diverse techniques under a variety of 
names, and is used in different business, science, and social science domains. 

Created By:- YASHSWI SINGH \n

''')
st.write("[Learn more About me >](https://in.linkedin.com/in/yashswi-singh-6305bb205?trk=people-guest_people_search-card)")
st.write("---")



# Upload CSV data
with st.sidebar.title('Upload your dataset'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    
    st.sidebar.markdown("""
[Example CSV input file](https://gist.githubusercontent.com/noamross/e5d3e859aa0c794be10b/raw/b999fb4425b54c63cab088c0ce2c0d6ce961a563/cars.csv)
""")
    


# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.subheader('**Pandas Profiling Report/Data Analysis Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press here to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.subheader('**Pandas Profiling Report/Data Analysis Report**')
        st_profile_report(pr)


#footer
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.subheader("Contact Us")
st.write("[Contact Us by clicking here !!](https://form.jotform.com/yashswi2412/web-contact-form-EDA)")



