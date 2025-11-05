import streamlit as st
import langchainhelp
st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick your cuisine", ("Indian", "American", "Arabic", "Mexican", "Italian", "French"))

if cuisine:
    response = langchainhelp.generate_restaurant_name_and_menu(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("MENU ITEMS")
    for item in menu_items:
        st.write("-", item)