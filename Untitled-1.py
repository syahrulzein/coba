import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_excel('healthcare-dataset-stroke-data.xlsx', engine='openpyxl')

#1. Membaca Dataset
st.write('**1. Dataset**')
st.dataframe(df.head())

#2. Visualisasi Data - Jumlah Pasien Berdasarkan Usia
st.write('**2. Visualisasi Data - Jumlah Pasien Berdasarkan Usia**')
age_count = df['age'].value_counts().reset_index()
age_count.columns = ['age', 'count']

chart_age = (
    alt.Chart(age_count)
    .mark_line(point=True)
    .encode(
        x=alt.X('age:Q', title='Age'),
        y=alt.Y('count:Q', title='Jumlah Pasien'),
        tooltip=['age', 'count']
    )
    .properties(height=300)
)
st.altair_chart(chart_age, use_container_width=True)

#3. Visualisasi Data - Tipe Pekerjaan
st.write('**3. Visualisasi Data - Tipe Pekerjaan**')
work_count = df['work_type'].value_counts().reset_index()
work_count.columns = ['work_type', 'count']

chart_work = (
    alt.Chart(work_count)
    .mark_bar()
    .encode(
        x=alt.X('work_type:N', title='Work Type'),
        y=alt.Y('count:Q', title='Jumlah'),
        tooltip=['work_type', 'count']
    )
    .properties(height=300)
)
st.altair_chart(chart_work, use_container_width=True)

#5. Interaktif Komponen
st.write('**5. Button**')
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")

#6. Checkbox
st.write('**6. Checkbox**')
agree = st.checkbox("I agree")
if agree:
    st.write("Great!")

#7. Multiselect
st.write('**7. Multiselect**')
options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)
st.write("You selected:", options)

#8. Slider
st.write('**8. Slider**')
start_tyres, end_tyres = st.select_slider(
    "Pilih komponen ban untuk race pekan ini",
    options=[
        "Hyper Soft",
        "Ultrs Soft",
        "Super Soft",
        "Soft",
        "Medium",
        "Hard",
        "Super Hard",
    ],
    value=("Hyper Soft", "Soft"),
)
st.write("Anda memilih", start_tyres, "dan", end_tyres)

#9. Toggle
st.write('**9. Toggle**')
on = st.toggle("Activate feature")
if on:
    st.write("Feature activated!")

#10. Number Input
st.write('**10. Number Input**')
number = st.number_input(
    "Insert a number", value=None, placeholder="Type a number..."
)
st.write("The current number is ", number)

#11. Date Input
st.write('**11. Date Input**')
import datetime
d = st.date_input("When's your birthday", datetime.date(1999, 9, 14))
st.write("Your birthday is:", d)

#12 Image
st.write('**12. Input Image**')
link = "https://unair.ac.id/wp-content/uploads/2023/04/Foto-by-Kompas-Money.jpg"
st.image(link, caption="Rumah Sakit")

#13. Membuat Kolom
st.write('**13. Membuat Kolom**')
col1, col2= st.columns(2)

with col1:
    st.write('**Jumlah Pasien Berdasarkan Usia**')
    st.altair_chart(chart_age, use_container_width=True)

with col2:
    st.write('**Visualisasi Data - Tipe Pekerjaan**')
    st.altair_chart(chart_work, use_container_width=True)

#14. Membuat tab
st.write('**14. Membuat Tab**')
tab1, tab2 = st.tabs(["Line", "Bar"])

with tab1:
    st.write('**Jumlah Pasien Berdasarkan Usia**')
    st.altair_chart(chart_age, use_container_width=True)

with tab2:
    st.write('**Visualisasi Data - Tipe Pekerjaan**')
    st.altair_chart(chart_work, use_container_width=True)

#15. Expander
st.write('**15. Expander**')
with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")