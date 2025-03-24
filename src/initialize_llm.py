import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
#import google.generativeai as genai


def initialize_llm(model_option):
    """Initialize LLM based on available API keys"""
    # openai_api = st.secrets.get("OPENAI_API_TOKEN")
    # gemini_api = st.secrets.get("GEMINI_API_KEY")

    # Retrieve the API key from the environ var in Render.com file
    openai_api = os.getenv("OPENAI_API_TOKEN")
    gemini_api = os.getenv("GEMINI_API_KEY")
    
    
    if model_option == "GPT-4o":
        if not openai_api:
            st.sidebar.error('OpenAI API key is missing in secrets.toml')
            return None
        try:
             llm = ChatOpenAI(
                model_name="gpt-4o",
                temperature=0,
                api_key=openai_api,
                verbose=True
            )
             return llm
            
            
        except Exception as e:
            st.sidebar.error(f'Error initializing ChatOpenAI: {e}')
            return None
            
    else:  # Gemini-2.0
        if not gemini_api:
            st.sidebar.error('Gemini API key is missing in secrets.toml')
            return None
        try:
            
            # return ChatGoogleGenerativeAI(
            #     model="gemini-2.0-flash",
            #     temperature=0,
            #     api_key=gemini_api,
            #     convert_system_message_to_human=False,
            #     verbose=True
            # )
        
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
                api_key=gemini_api,
                convert_system_message_to_human=False
                )
            return llm
            

            
        except Exception as e:
            st.sidebar.error(f'Error initializing Gemini: {e}')
            return None