import os
import sqlite3
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function for using Google Gemini to process the question
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to process the question into an SQL query (if applicable)
def process_question_into_sql(query):
    prompt = [
        "You are an expert in converting English questions to SQL query! The SQL database has a table called MOVIES with columns TITLE, GENRE, RATING.\n"
        "For example:\nExample 1 - What is the highest rated movie? -> SELECT * FROM MOVIES ORDER BY RATING DESC LIMIT 1;\n"
        "Example 2 - What movies are in the Comedy genre? -> SELECT * FROM MOVIES WHERE GENRE='Comedy';\n"
        "Please convert the following query into an SQL query: "
    ]
    sql_query = get_gemini_response(query, prompt)
    return sql_query

# Function to retrieve data from SQLite
def read_sql_query(sql, db='movies.db'):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Streamlit interface
def main():
    st.title("Movie Recommendation App")

    st.write("### Ask a movie-related question and get recommendations!")

    # Get user input
    question = st.text_input("What do you want to know about movies?")

    if question:
        # Show the user’s question
        st.write(f"**You asked**: {question}")
        
        # Process question into SQL query
        sql_query = process_question_into_sql(question)
        st.write("### Generated SQL Query:")
        st.write(sql_query)

        # Fetch movie data from the database
        response = read_sql_query(sql_query)
        
        if response:
            st.write("### Movie Recommendations:")
            for row in response:
                st.write(f"**Title**: {row[0]}, **Genre**: {row[1]}, **Rating**: {row[2]}")
        else:
            st.write("No results found.")

if __name__ == "__main__":
    main()
