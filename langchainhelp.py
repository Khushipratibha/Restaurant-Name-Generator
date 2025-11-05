from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import streamlit as st
#from mykey import groq_api_key
groq_api_key=st.secrets["GROQ_API_KEY"]
import os
os.environ["GROQ_API_KEY"] = groq_api_key

# Initialize LLM
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

# Prompt to generate restaurant name
prompt_name = PromptTemplate(
    input_variables=["cuisine"],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy, short restaurant name. Only give one name. No description"
             ""
)

# Prompt to generate menu items
prompt_menu = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Suggest 5 unique menu items for a restaurant named {restaurant_name}. Return them as a comma-separated list, no descriptions."
)

# Chain using modern Runnable syntax
name_chain = prompt_name | llm
menu_chain = prompt_menu | llm

def generate_restaurant_name_and_menu(cuisine):
    # Step 1: Generate restaurant name
    name_response = name_chain.invoke({"cuisine": cuisine})
    restaurant_name = name_response.content.strip()

    # Step 2: Generate menu items
    menu_response = menu_chain.invoke({"restaurant_name": restaurant_name})
    menu_items = menu_response.content.strip()

    return {"restaurant_name": restaurant_name, "menu_items": menu_items}



