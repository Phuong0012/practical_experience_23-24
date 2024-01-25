import requests
import json
import random
import streamlit as st

""" GENRE LIST
1 = Action
2 = Adventure
28 = Boys Love
4 = Comedy
8 = Drama 
14 = Horror
22 = Romance
"""

def generate_season(year, season):
    payload = {"filter":("tv", "movie")}   #decides what genres should be picked


    season_url = "https://api.jikan.moe/v4/seasons/"
    date = str(year) + "/" + str(season)
    release = season_url + date


    r = requests.get(release, params=payload).text   #searches for titles that fulfill the user choice
    sex = json.loads(r) #transforms into json



    #collects number of pages of chosen anime and randomly chooses 1
    pages = (sex["pagination"]["last_visible_page"]-1)
    rand_page = random.randint(1,pages)
    payload["page"] = rand_page
    x = requests.get(release, params=payload).text
    sex3 = json.loads(x)
    print(sex3)

    print("_______________________")


    #prints all anime from randomly picked page
    num = random.randint(1,23)
    title = sex3["data"][num]["title"]
    syn = sex3["data"][num]["synopsis"]
    img = sex3["data"][num]["images"]["webp"]["image_url"]
    url = sex3["data"][num]["trailer"]["url"]

    st.write(title)
    st.image(img)
    st.write(syn)
    if url == None:
       st.write("No trailer available")
    else:
        st.write(f"Link to  trailer: {url}")


def generate_genre(*genre_choice):
    payload = {"type":"tv",
               "genres": genre_choice}   #decides what genres should be picked
    anime_url = "https://api.jikan.moe/v4/anime"
    r = requests.get(anime_url, params=payload).text   #searches for titles that fulfill the user choice
    sex = json.loads(r) #transforms into json

    #collects number of pages of chosen anime and randomly chooses 1
    pages = (sex["pagination"]["last_visible_page"]-1)
    rand_page = random.randint(1,pages)
    payload["page"] = rand_page
    x = requests.get(anime_url, params=payload).text
    sex3 = json.loads(x)

   # print(f"number of all pages: {pages}")
    #print(payload)
    print("_______________________")

    #prints all anime from randomly picked page
    num = random.randint(1,24)
    title = sex3["data"][num]["title"]
    syn = sex3["data"][num]["synopsis"]
    img = sex3["data"][num]["images"]["webp"]["image_url"]
    url = sex3["data"][num]["trailer"]["url"]


    st.write(title)
    st.image(img)
    st.write(syn)
    if url == None:
       st.write("No trailer available")
    else:
        st.write(f"Link to  trailer: {url}")

