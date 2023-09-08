import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
      return None
    return r.json()

lottie_coder1 = load_lottieurl("https://lottie.host/79ed564b-7e14-4a8f-980f-3f592addf735/XmjPS9Ja2t.json")
lottie_coder2 = load_lottieurl("https://lottie.host/9ce700d3-8d1f-4c45-b92e-139912b4b12d/sdF8hW5aVU.json")
lottie_coder3 = load_lottieurl("https://lottie.host/6b69c3fe-e094-435a-8b5d-affd578c02a2/L3lYYqqt6D.json")
lottie_coder4 = load_lottieurl("https://lottie.host/e991dae4-ad0a-41ad-8a31-942d07f75f80/DZoHPPfOCH.json")
                               
st.write("##")
st.subheader("Hey Guys :wave:")
st.title("Welcome to my digital portfolio to uncover my skills, achievements, and potential contributions to your organization.")
st.write("""Feel free to explore my portfolio to witness my dedication to the world of finance and connect with me for exciting job opportunities or to collaborate and expand our knowledge together :smile:
""")
st.write("Connect with me for starting new ventures together https://www.linkedin.com/in/stutijain0201")
st.write('---')

with st.container():
    selected = st.selectbox(
    "Select a Section:",
    ["About Me", "Education and Achievements", "Goals and Aspirations", "Contact Page "]
    icons = ['book','book','bar-chart','mailbox']
    )     
if selected == 'About Me':

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("Hello :wave:, I'm Stuti Jain, a Bachelor of Business Administration graduate :mortar_board:, and I'm proud to share that I've successfully cleared CFA Level 1 with strong proficiency :medal: and will be appearing for CFA level 2 this winter :snowflake: .")
            st.subheader("Currently, I am thriving in my role as an OPERATIONS ANALYST at JPMorgan Chase & Co.:briefcase:, where my dedication and performance have earned me a Certificate of Excellence:chart_with_upwards_trend:, showcasing my commitment to delivering exceptional results:fist:.")
        with col2:
            st_lottie(lottie_coder1)
    st.write("---")

if selected =="Education and Achievements":
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
         st.subheader("""
         Education And Achievements
       - Delhi Public School Raipur :open_book:
                - Class 10th CBSE BOARD
                - Grade: 10 CGPA
        - Delhi Public School Raipur :open_book:
                - Class 12th CBSE BOARD Commerce
                - Grade: 93%
        - Christ University Bangalore:mortar_board:
                - Bachelor of Buisness Administration
                - Batch of: 2021
                - Grade: 3.8/4 With Distinction:reminder_ribbon:
        - OPERATION ANALYST :female-technologist:
                - JP MORGAN CHASE AND CO
                - (JUL 2021 - PRESENT)           
        - BUSINESS DEVELOMPENT INTERN :female-technologist:
                - Matar 
                - (Aug 2019 - Sep 2019)
        - Sales and Marketing Intern :female-technologist:
                - Seal Ripped by Bayside Media 
                - (Jan 2019 - Feb 2019)
        - Team Leader :female-technologist:
                - Step Up for India
                - (Jul 2018 - Sep 2018))
        - Head of Sales and Marketing :female-technologist:
                - IndiCrochet India 
                - (Jul 2017 - Nov 2017)
        - Certificate of Scholarship :female-student:
                - Christ University for consecutive two years 
                - (2019-2020-2021)
        - Certificate of Merit :female-student:
                - Delhi Public School Raipur for consecutive six years
                - (2012-2013-2014-2015-2016-2017-2018)
        """)
        with col4:
            st_lottie(lottie_coder2)
    st.write("---")

if selected == 'Goals and Aspiration':

    with st.container():
        col5, col6 = st.columns(2)
        with col5:
            st.write("##")
            st.write("Hello, I'm thrilled to share my goals and aspirations with you. As I embark on this journey, my overarching goal is to continuously learn, grow, and make a meaningful impact in both my personal and professional life. Here are some of my key aspirations. Career Advancement: I aspire to excel in my chosen career path, continuously improving my skills and knowledge. I aim to take on increasingly challenging roles that allow me to contribute to my field and the organizations I work for. Education and Skill Development: Learning is a lifelong endeavor for me. I am committed to expanding my knowledge and honing my skills in areas that are relevant to my interests and career goals. This includes pursuing additional degrees, certifications, and staying up-to-date with industry trends. Leadership: I aspire to be a leader who inspires and empowers others. Whether it's in a professional setting or within my community, I want to contribute to positive change and guide others toward success. Personal Growth: Achieving a healthy work-life balance is essential. I aim to cultivate personal well-being, including physical and mental health, to ensure I can give my best in all aspects of life. Giving Back: It's important to me to give back to society. I want to actively participate in charitable and community service initiatives that make a difference in the lives of those in need.")

        with col6:
            st_lottie(lottie_coder3)
    st.write("---")

if selected == 'Contact Page':
    st.header("Get in Touch! Via Mail Or Via Linkedin")
    st.write("stutijain0201@gmail.com")
    st.write("https://www.linkedin.com/in/stutijain0201")
    st_lottie(lottie_coder4)
    st.write('---')

    
