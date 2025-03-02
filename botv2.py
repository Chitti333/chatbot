#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

st.set_page_config(page_title="Career Chatbot 🎯", page_icon="💼", layout="wide")

# Initialize conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

def load_career_data(file_path):
    try:
        if not os.path.exists(file_path):
            st.error(f"File not found: {file_path}")
            return None
        df = pd.read_csv(file_path)
        if df.empty:
            st.error(f"The file {file_path} is empty.")
            return None
        return df
    except Exception as e:
        st.error(f"Error loading career data: {e}")
        return None

def preprocess_career_data(df):
    df = df.fillna("")
    df['Job Title'] = df['Job Title'].str.lower()
    df['skills'] = df['skills'].str.lower()
    return df

def create_career_vectorizer(df):
    vectorizer = TfidfVectorizer()
    job_vectors = vectorizer.fit_transform(df['Job Title'] + " " + df['skills'])
    return vectorizer, job_vectors


def find_best_job(user_query, vectorizer, job_vectors, df):
    query_vector = vectorizer.transform([user_query.lower()])
    similarities = cosine_similarity(query_vector, job_vectors).flatten()
    best_match_index = similarities.argmax()
    best_match_score = similarities[best_match_index]
    if best_match_score > 0.3:
        return df.iloc[best_match_index][['Job Title', 'Company', 'Salary Range', 'location', 'skills', 'Job Description']]
    else:
        return None

def configure_generative_model(api_key):
    try:
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Error configuring the generative model: {e}")
        return None
    
def refine_career_advice(generative_model, user_query, job_details):
    try:
        context = """
        You are a career guidance chatbot. Refine the following job details to provide clear, professional, and structured career advice.
        Include job roles, required skills, and salary expectations in bullet points.
        """
        prompt = f"{context}\n\nUser Query: {user_query}\nBest Matched Job: {job_details}\nRefined Response:"
        response = generative_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error refining the response: {e}"

def career_chatbot(df, vectorizer, question_vectors, generative_model):
    st.title("Career Chatbot 🎯")
    st.write("👋 Welcome! Ask me anything about career options, job roles, required skills, or salary expectations.")
    
    with st.container():
        st.markdown("### Conversation History 🗨️")
        chat_container = st.container()
        for message in st.session_state.conversation:
            role, content = message["role"], message["content"]
            color = "#007ACC" if role == "user" else "#333333"
            text_color = "#ffffff" if role == "user" else "#f8f8f8"

            chat_container.markdown(
                f"<div style='background-color: {color}; color: {text_color}; padding: 12px; border-radius: 8px; margin: 6px 0;'>"
                f"<strong>{role.capitalize()}:</strong> {content}</div>", 
                unsafe_allow_html=True
            )
    
    user_query = st.text_input("💬 Ask a question:", placeholder="Type your career-related question here...")
    if user_query:
        st.session_state.conversation.append({"role": "You", "content": user_query})
        best_job = find_best_job(user_query, vectorizer, job_vectors, df)
        if best_job is not None:
            with st.spinner("Refining the career advice..."):
                refined_advice = refine_career_advice(generative_model, user_query, best_job)
                st.session_state.conversation.append({"role": "Bot", "content": refined_advice})
                st.markdown(
                    f"<div style='background-color: #333333; color: #f8f8f8; padding: 10px; "
                    f"border-radius: 10px;'>"
                    f"<strong>Bot:</strong> {refined_advice}</div>", 
                    unsafe_allow_html=True
                )
            st.write("this os the best answer")
        else:
            try:
                context = """
                You are a career guidance chatbot. Provide detailed, structured career guidance for job seekers.
                Suggest potential career paths based on their skills, qualifications, and job preferences.
                Format the response with bullet points and maintain a professional tone.
                """
                prompt = f"{context}\n\nUser: {user_query}\nBot:"
                response = generative_model.generate_content(prompt)
                st.session_state.conversation.append({"role": "assistant", "content": response.text})
                chat_container.markdown(
                    f"<div style='background-color: #333333; color: #f8f8f8; padding: 12px; border-radius: 8px;'>"
                    f"<strong>Bot:</strong> {response.text}</div>", 
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"Sorry, I couldn't generate a response. Error: {e}")

def main():
    file_path = "careerDSet.csv"
    df = load_career_data(file_path)
    if df is None:
        return
    df = preprocess_career_data(df)
    vectorizer, question_vectors = create_career_vectorizer(df)
    API_KEY = "AIzaSyCMmi8Hzd7GHOzRtbTvsRJTX1CifvJEpFQ"
    if not API_KEY:
        st.error("API key not found. Please set the GOOGLE_API_KEY environment variable.")
        return
    generative_model = configure_generative_model(API_KEY)
    if generative_model is None:
        return
    career_chatbot(df, vectorizer, question_vectors, generative_model)

if __name__ == "__main__":
    main()
