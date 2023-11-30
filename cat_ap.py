import streamlit as st
import requests

#code to config page
st.set_page_config(
    page_title= "Cat App",
    page_icon= ":cat:")

st.header("WELCOME TO MY CAT APP", divider="rainbow")

def get_content():
    """  GET ACCESS TO API AND GET URL IMAGE """
    contents = requests.get("https://cataas.com//cat")
    return  contents.content

def place_cat_image():
    cat_image = get_content()
    st.image(cat_image, width=200)

#add button
st.button("click here!",
          on_click=place_cat_image)