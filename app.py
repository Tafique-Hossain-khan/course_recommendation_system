import streamlit as st
import preprocessing
import pandas as pd
import recommend

def load_data():
    data = pd.read_csv('udemy_course_data.csv') 
    return data

#df = load_data()

st.title('Course Recommendation System')

course_name = st.text_input('Enter the related course name:')
recommend_button = st.button('Recommend')
if recommend_button:
    try:
        if course_name:
            data = load_data()
            course_title, course_url = recommend.recommend_courses(data, course_name)
            title_url = dict(zip(course_title, course_url))
            
            if(len(title_url!=0)):
                #if title_url:
                    cols = st.columns(2)  # Create two columns
                    for idx, (title, url) in enumerate(title_url.items()):
                        col = cols[idx % 2]  # Alternate between columns
                        with col:
                            st.markdown(
                                f"""
                                <div style="border: 1px solid #ddd; padding: 10px; margin: 10px; border-radius: 5px;">
                                    <h4>{title}</h4>
                                    <a href="{url}" target="_blank">
                                        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 5px;">Browse Course</button>
                                    </a>
                                </div>
                                """, 
                                unsafe_allow_html=True
                            )
            else:
                st.write("No courses found.")

    except:
        ##key word recommedndataion
        pass
        #st.write("couse comming soons")
    else:
        st.write("Please enter a course name.")


