import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

# Set up the layout of the page-------------------
st.set_page_config(layout='centered')

# --------------- for side bar----------------
fig_height = st.sidebar.slider(
    'Height of the figure',
    min_value=40.0, max_value=70.0, step=10.0, value=65.0
)


st.title('Academic Performance Monitor:')
st.subheader( 'A Visual Representation of My Semester-wise Subject Scores')
st.text("    ")

#------------------------ FOR BAR CHART OF THEORY MARKS ----------------------------------------------------------------------------------------------------------
def generate_bar_chart1():
    st.subheader("Theory Scores ")
    source_file = st.file_uploader(
        'Upload custom CSV. Default included.'
    )
    if source_file is None:
        data = pd.read_csv('theory_marks.csv')
        st.write("Opened the default file!")
        st.dataframe(data, width= 600, height = 180)
    else:
        data = pd.read_csv(source_file)
        st.write('Read the custom file!')

    #---------------------------
    st.subheader("BAR CHART")
    st.markdown('This is a bar chart created with Streamlit. The chart displays the marks obtained in each subject for a given semester. To view the marks obtained out of total marks in a particular subject, simply hover over the corresponding bar.')
    # Create a list of semesters
    semesters = list(range(1, 9))

    # Sidebar to select semester
    selected_semester = st.selectbox("Choose Semester", semesters)

    # Filter data based on selected semester
    semester_data = data[data["Semester"] == selected_semester]


    # Create a bar chart of subjects and marks for selected semester
    fig = px.bar(semester_data, x="Subject", y="Marks", 
                hover_data=["Subject", "Marks", "Out of "], 
                labels={"Marks": "Obtained Marks", "Out of ": "Total Marks"}, height= fig_height*9)


    # Show the chart
    x= st.plotly_chart(fig, use_container_width=True)
    return x


#------------------------ FOR BAR CHART OF PRACTICAL MARKS ----------------------------------------------------------------------------------------------------------

def generate_bar_chart2():
    st.subheader("Practical Scores ")

    source_file = st.file_uploader(
        'Upload custom CSV. Default included.'
    )
    if source_file is None:
        data = pd.read_csv('practical_marks.csv')
        st.write("Opened the default file!")
        st.dataframe(data, width= 600, height = 180)
    else:
        data = pd.read_csv(source_file)
        st.write('Read the custom file!')

    #---------------------------
    st.subheader("BAR CHART")
    st.markdown('This is a bar chart created with Streamlit. The chart displays the marks obtained in each subject for a given semester. To view the marks obtained out of total marks in a particular subject, simply hover over the corresponding bar.')
    # Create a list of semesters
    semesters = list(range(1, 9))

    # Sidebar to select semester
    selected_semester = st.selectbox("Choose Semester", semesters)

    # Filter data based on selected semester
    semester_data = data[data["Semester"] == selected_semester]


    # Create a bar chart of subjects and marks for selected semester
    fig = px.bar(semester_data, x="Subject", y="Marks", 
                hover_data=["Subject", "Marks", "Out of "], 
                labels={"Marks": "Obtained Marks", "Out of ": "Total Marks"}, height= fig_height*9)


    # Show the chart
    x= st.plotly_chart(fig, use_container_width=True)
    return x


#----------------------------------------FOR LINE CHART OF OVERALL PERCENTAGE--------------------------------------------------------------------------------------

def generate_line_chart():
    df = pd.read_csv('overall_per.csv')
    st.subheader(' Percentage Scored in each Semester')
    st.markdown('This is a line chart created with Streamlit. You can hover on each data marker to view the percentage scored on that particular semester.')
    st.text(" ")

    chart = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X('Semester:N', scale=alt.Scale(padding=0.5)),
    y=alt.Y('Percentage:Q'),
    tooltip=[alt.Tooltip('Semester:N'), alt.Tooltip('Percentage:Q')]
    ).properties(  
        width= 800,
        height = fig_height*5)

    x = st.altair_chart(chart, use_container_width=True)
    return x

#-------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    navigation = st.sidebar.radio("Navigation", ["Theory Scores", "Practical Scores", "Overall Percentage"])
    if navigation == "Theory Scores":
        generate_bar_chart1()
    elif navigation=='Practical Scores':
        generate_bar_chart2()
    elif navigation == "Overall Percentage":
        generate_line_chart()

if __name__ == '__main__':
    main()

