import sqlite3
import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from prompt import prompt   

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model once (better performance)
model = genai.GenerativeModel('gemini-2.5-flash')   # or gemini-1.5-pro if you have access

def get_gemini_response(system_prompt, user_question):
    try:
        response = model.generate_content(
            [
                {"role": "user",    "parts": [system_prompt]},
                {"role": "model",   "parts": ["Understood!"]},   # optional but helps
                {"role": "user",    "parts": [user_question]},
            ],
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=512,
                temperature=0.2,
            )
        )
        return response.candidates[0].content.parts[0].text.strip()
    
    except Exception as e:
        return f"Error from Gemini: {str(e)}"


def execute_sql(sql, db_path='students.db'):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        conn.close()
        return columns, rows
    except Exception as e:
        return None, f"SQL Error: {str(e)}"


# ── Streamlit UI ────────────────────────────────────────────────

st.title("AI SQL Query Generator with Gemini")

question = st.text_input("Ask anything about the students database:")

if st.button("Generate & Run Query"):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Thinking..."):
            sql_query = get_gemini_response(prompt, question)

        st.subheader("Generated SQL Query:")
        st.code(sql_query, language="sql")

        columns, result = execute_sql(sql_query)

        st.subheader("Query Result:")

        if columns is None:
            st.error(result)           # result contains error message here
        elif not result:
            st.info("Query executed successfully — no rows returned.")
        else:
            # Nice table output
            st.dataframe(
                result,
                column_config={col: col for col in columns},
                use_container_width=True,
                hide_index=True,
            )