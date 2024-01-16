import streamlit as st
from results_gen import generate_season, generate_genre

genres = ()
genre_choice = ()


st.set_page_config(
    page_title="Generate Anime")
tab1, tab2 = st.tabs(["Seasons", "Genre"])


if "count" not in st.session_state:
    st.session_state.count = 0
def increment_count_season():
    st.session_state.count +=1
    
if "count2" not in st.session_state:
    st.session_state.count2 = 0
def increment_count_genre():
    st.session_state.count2 +=1

with tab1:
    #create sub-headers
    st.subheader("| Seasons")

    year = st.slider(
        "Select a year",
        min_value=1965,
        max_value=2023)
  

    season = st.selectbox(
        'What season are you interested in?',
        ('Spring', 'Summer', 'Fall', 'Winter'))

    st.write("You selected:", season, year)

    if st.button("Generate", on_click=increment_count_season):
        # This block will be executed only when the button is clicked
        if st.session_state.count % 2 != 0 and st.session_state.count > 0:
            generate_season(year, season)



with tab2:
    options = st.multiselect(
    'Pick your genres',
    ['Action', 'Adventure', 'Comedy', 'Drama', "Romance"])

    genre_ex = st.checkbox("Exclude some genres")
    if genre_ex:
        options_ex = st.multiselect(
        'What genres do you want to exclude',
        ['Action', 'Adventure', 'Comedy', 'Drama', "Romance"])

        if options_ex: #mapping number keys to options
            for n, g in enumerate(options_ex):
                    # replace the green, yellow etc with anime categories and corresponding
                if options_ex[n] == "Action":
                    options_ex[n] = "1"
                if options_ex[n] == "Adventure":
                    options_ex[n] = "2"
                if options_ex[n] == "Comedy":
                    options_ex[n] = "4"
                if options_ex[n] == "Drama":
                    options_ex[n] = "8"
                if options_ex[n] == "Horror":
                    options_ex[n] = "14"
                if options_ex[n] == "Romance":
                    options_ex[n] = "22"


    if options: #mapping number keys to options

        for n, g in enumerate(options):
                # replace the green, yellow etc with anime categories and corresponding
            if options[n] == "Action":
                options[n] = "1"
            if options[n] == "Adventure":
                options[n] = "2"
            if options[n] == "Comedy":
                options[n] = "4"
            if options[n] == "Drama":
                options[n] = "8"
            if options[n] == "Horror":
                options[n] = "14"
            if options[n] == "Romance":
                options[n] = "22"

    genre_choice = tuple(options)
    
    if genre_ex and options_ex:
        genre_choice = tuple(set(options) - set(options_ex))

    print(genre_choice) # in your terminal, check if what is being selected is what you expect
    if st.button("Get results", on_click=increment_count_genre, disabled=not genre_choice):
        # This block will be executed only when the button is clicked
        if st.session_state.count2 % 2 != 0 and st.session_state.count2 > 0:
            generate_genre(*genre_choice)